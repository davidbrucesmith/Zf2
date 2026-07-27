from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, List, Optional
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element

TransformFunc = Callable[[List[Element]], List[Element]]


@dataclass
class ActiveAttributes:
    divisions: Optional[Element] = None
    key: Optional[Element] = None
    time: Optional[Element] = None
    clefs: Dict[str, Element] = field(default_factory=dict)


def _get_namespace(root: Element) -> str:
    if root.tag.startswith("{"):
        return root.tag.split("}", 1)[0][1:]
    return ""


def _q(ns: str, tag: str) -> str:
    return f"{{{ns}}}{tag}" if ns else tag


def _measure_number(measure: Element, fallback: int) -> int:
    raw = measure.get("number")
    if raw is None:
        return fallback
    try:
        return int(raw)
    except ValueError:
        return fallback


def _collect_active_attributes(
    measures: List[Element],
    first_selected_index: int,
    q,
) -> ActiveAttributes:
    active = ActiveAttributes()

    for m in measures[: first_selected_index + 1]:
        attrs = m.find(q("attributes"))
        if attrs is None:
            continue

        divisions = attrs.find(q("divisions"))
        key = attrs.find(q("key"))
        time = attrs.find(q("time"))

        if divisions is not None:
            active.divisions = deepcopy(divisions)
        if key is not None:
            active.key = deepcopy(key)
        if time is not None:
            active.time = deepcopy(time)

        for clef in attrs.findall(q("clef")):
            clef_no = clef.get("number", "1")
            active.clefs[clef_no] = deepcopy(clef)

    return active


def _ensure_first_measure_attributes(
    first_measure: Element,
    active: ActiveAttributes,
    q,
) -> None:
    attrs = first_measure.find(q("attributes"))
    if attrs is None:
        attrs = ET.Element(q("attributes"))
        first_measure.insert(0, attrs)

    if attrs.find(q("divisions")) is None and active.divisions is not None:
        attrs.append(deepcopy(active.divisions))
    if attrs.find(q("key")) is None and active.key is not None:
        attrs.append(deepcopy(active.key))
    if attrs.find(q("time")) is None and active.time is not None:
        attrs.append(deepcopy(active.time))

    existing_clefs = {c.get("number", "1") for c in attrs.findall(q("clef"))}
    for clef_no, clef in active.clefs.items():
        if clef_no not in existing_clefs:
            attrs.append(deepcopy(clef))


def _strip_ties_from_measure(measure: Element, q) -> None:
    """Remove only cross-measure MusicXML tie endpoints from the first/last notes in a measure."""

    def _remove_tie_children(note: Element, tie_types: set[str]) -> None:
        for tie in list(note.findall(q("tie"))):
            if tie.get("type") in tie_types:
                note.remove(tie)

        notations = note.find(q("notations"))
        if notations is None:
            return

        for tied in list(notations.findall(q("tied"))):
            if tied.get("type") in tie_types:
                notations.remove(tied)

        if len(notations) == 0:
            note.remove(notations)

    notes = measure.findall(q("note"))
    if not notes:
        return

    # The first note can only dangle backward into the previous measure.
    _remove_tie_children(notes[0], {"stop"})
    if len(notes) > 1:
        # The last note can only dangle forward into the next measure.
        _remove_tie_children(notes[-1], {"start"})


def _extract_measure_slice(
    part: Element,
    start_measure: int,
    end_measure: int,
    q,
) -> tuple[List[Element], Optional[int]]:
    original_measures = part.findall(q("measure"))

    selected_indices: List[int] = []
    for i, measure in enumerate(original_measures):
        number = _measure_number(measure, i + 1)
        if start_measure <= number <= end_measure:
            selected_indices.append(i)

    if not selected_indices:
        return [], None

    selected = [deepcopy(original_measures[i]) for i in selected_indices]
    return selected, selected_indices[0]


def detect_musicxml_measure_range(input_path: str | Path) -> tuple[int, int]:
    """Return the inclusive measure-number span found in the first score part."""
    tree = ET.parse(Path(input_path))
    root = tree.getroot()

    ns = _get_namespace(root)

    def q(tag: str) -> str:
        return _q(ns, tag)

    first_part = root.find(q("part"))
    if first_part is None:
        raise ValueError("MusicXML file has no <part> elements")

    measures = first_part.findall(q("measure"))
    if not measures:
        raise ValueError("MusicXML first part contains no <measure> elements")

    nums = [_measure_number(measure, i + 1) for i, measure in enumerate(measures)]
    return min(nums), max(nums)


def extract_and_transform_range(
    input_path: str | Path,
    output_path: str | Path,
    start_measure: int,
    end_measure: int,
    transform_func: TransformFunc,
) -> None:
    """
    Extract a measure range from all parts, apply a transformation, and write a new MusicXML file.

    Guarantees:
    - Dynamic orchestral part handling
    - Measure renumbering from 1..N after transform
    - First extracted measure explicitly contains active divisions/key/time/clef
    """
    if start_measure > end_measure:
        raise ValueError("start_measure must be <= end_measure")

    input_path = Path(input_path)
    output_path = Path(output_path)

    tree = ET.parse(input_path)
    root = tree.getroot()

    ns = _get_namespace(root)

    def q(tag: str) -> str:
        return _q(ns, tag)

    original_parts = root.findall(q("part"))

    transformed_by_part_id: Dict[str, List[Element]] = {}
    transformed_part_count = 0

    for part in original_parts:
        part_id = part.get("id")
        if not part_id:
            continue

        selected_measures, first_selected_index = _extract_measure_slice(
            part, start_measure, end_measure, q
        )

        if not selected_measures or first_selected_index is None:
            raise ValueError(
                f"No measures in requested range {start_measure}-{end_measure} "
                f"for part '{part_id}'. Use measure numbers that exist in this file."
            )

        original_measures = part.findall(q("measure"))
        active = _collect_active_attributes(original_measures, first_selected_index, q)

        transformed = transform_func(selected_measures)
        if not transformed:
            raise ValueError(
                f"Transform produced no measures for part '{part_id}'. "
                "Refusing to write an empty part."
            )

        for measure in transformed:
            _strip_ties_from_measure(measure, q)

        _ensure_first_measure_attributes(transformed[0], active, q)

        for idx, measure in enumerate(transformed, start=1):
            measure.set("number", str(idx))

        transformed_by_part_id[part_id] = transformed
        transformed_part_count += 1

    if transformed_part_count == 0:
        raise ValueError(
            f"No parts contained measures in requested range {start_measure}-{end_measure}."
        )

    new_root = deepcopy(root)
    for part in new_root.findall(q("part")):
        part_id = part.get("id")
        if not part_id:
            continue
        part[:] = transformed_by_part_id.get(part_id, [])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    ET.register_namespace("", ns) if ns else None
    ET.ElementTree(new_root).write(output_path, encoding="utf-8", xml_declaration=True)
