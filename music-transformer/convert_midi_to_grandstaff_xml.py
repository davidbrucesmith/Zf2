from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime
from pathlib import Path

from music21 import chord, clef, instrument, key, layout, meter, metadata, note, stream, tempo, converter


DEFAULT_INPUT_DIR = Path("data/input")
DEFAULT_OUTPUT_DIR = Path("data/output")


def _resolve_input(path_str: str) -> Path:
    path = Path(path_str)
    return path if path.exists() else DEFAULT_INPUT_DIR / path


def _resolve_output(path_str: str | None, input_path: Path) -> Path:
    if path_str:
        path = Path(path_str)
        return path if path.is_absolute() or path.parent != Path(".") else DEFAULT_OUTPUT_DIR / path

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return DEFAULT_OUTPUT_DIR / f"{input_path.stem}-grandstaff-{stamp}.musicxml"


def _find_source_part(parsed: stream.Score) -> stream.Stream:
    parts = list(parsed.parts)
    if not parts:
        return parsed

    def note_count(p: stream.Stream) -> int:
        return len(p.recurse().notes)

    return max(parts, key=note_count)


def _clone_with_duration(obj: note.Note | chord.Chord, ql: float):
    if isinstance(obj, note.Note):
        out = note.Note(obj.pitch)
    else:
        out = chord.Chord(obj.pitches)
    out.duration.quarterLength = ql
    if obj.volume is not None and obj.volume.velocity is not None:
        out.volume.velocity = obj.volume.velocity
    return out


def convert_midi_to_grand_staff(
    input_path: Path,
    output_path: Path,
    split_note: int = 60,
) -> None:
    parsed = converter.parse(str(input_path))
    source = _find_source_part(parsed)
    source_flat = source.flatten()

    right = stream.PartStaff(id="RH")
    left = stream.PartStaff(id="LH")

    right.partName = "Piano"
    left.partName = "Piano"
    right.partAbbreviation = "Pno."
    left.partAbbreviation = "Pno."

    right.insert(0, instrument.Piano())
    left.insert(0, instrument.Piano())
    right.insert(0, clef.TrebleClef())
    left.insert(0, clef.BassClef())

    for element in source_flat.getElementsByClass((meter.TimeSignature, key.KeySignature, tempo.MetronomeMark)):
        right.insert(float(element.offset), deepcopy(element))
        left.insert(float(element.offset), deepcopy(element))

    for element in source_flat.notesAndRests:
        offset = float(element.offset)
        ql = float(element.duration.quarterLength)
        if ql <= 0:
            continue

        if isinstance(element, note.Rest):
            continue

        if isinstance(element, note.Note):
            target = right if element.pitch.midi >= split_note else left
            target.insert(offset, _clone_with_duration(element, ql))
            continue

        if isinstance(element, chord.Chord):
            high = [p for p in element.pitches if p.midi >= split_note]
            low = [p for p in element.pitches if p.midi < split_note]

            if high:
                high_chord = chord.Chord(high)
                high_chord.duration.quarterLength = ql
                if element.volume is not None and element.volume.velocity is not None:
                    high_chord.volume.velocity = element.volume.velocity
                right.insert(offset, high_chord)

            if low:
                low_chord = chord.Chord(low)
                low_chord.duration.quarterLength = ql
                if element.volume is not None and element.volume.velocity is not None:
                    low_chord.volume.velocity = element.volume.velocity
                left.insert(offset, low_chord)

    right.quantize(quarterLengthDivisors=(8, 6, 4, 3, 2), processOffsets=True, processDurations=True, inPlace=True)
    left.quantize(quarterLengthDivisors=(8, 6, 4, 3, 2), processOffsets=True, processDurations=True, inPlace=True)

    right.makeMeasures(inPlace=True)
    left.makeMeasures(inPlace=True)
    right.makeRests(fillGaps=True, inPlace=True)
    left.makeRests(fillGaps=True, inPlace=True)

    out_score = stream.Score(id="PianoGrandStaff")
    out_score.insert(0, metadata.Metadata())
    out_score.metadata.title = input_path.stem

    out_score.insert(0, right)
    out_score.insert(0, left)

    staff_group = layout.StaffGroup(
        [right, left],
        name="Piano",
        abbreviation="Pno.",
        symbol="brace",
        barTogether=True,
    )
    out_score.insert(0, staff_group)

    # Normalize rhythmic spelling so all notes have exportable MusicXML duration types.
    out_score.makeNotation(inPlace=True)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    out_score.write("musicxml", fp=str(output_path))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert a MIDI file to grand-staff MusicXML (treble + bass split)."
    )
    parser.add_argument("--input", required=True, help="Input .mid/.midi file (default base: data/input/)")
    parser.add_argument(
        "--output",
        default=None,
        help="Output .musicxml file (default: data/output/<input>-grandstaff-<timestamp>.musicxml)",
    )
    parser.add_argument(
        "--split-note",
        type=int,
        default=60,
        help="MIDI pitch split threshold: notes >= threshold go to treble, below go to bass (default: 60).",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    input_path = _resolve_input(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    if input_path.suffix.lower() not in {".mid", ".midi"}:
        raise ValueError("Input must be a .mid or .midi file")

    output_path = _resolve_output(args.output, input_path)
    if output_path.suffix.lower() not in {".musicxml", ".xml"}:
        raise ValueError("Output must be .musicxml or .xml")

    convert_midi_to_grand_staff(input_path, output_path, split_note=args.split_note)
    print(f"Wrote grand-staff MusicXML to: {output_path}")


if __name__ == "__main__":
    main()
