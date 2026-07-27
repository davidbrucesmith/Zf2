from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Tuple

from src.core import detect_musicxml_measure_range, extract_and_transform_range
from src.midi_core import detect_midi_measure_range, extract_and_transform_midi_range
from src.transformations import permute_by_indices, retrograde, swap_adjacent_pairs


DEFAULT_INPUT_DIR = Path("data/input")
DEFAULT_OUTPUT_DIR = Path("data/output")


def _parse_index_pattern(raw: str) -> List[int]:
    try:
        return [int(x.strip()) for x in raw.split(",") if x.strip()]
    except ValueError as exc:
        raise ValueError("Permutation pattern must be a comma-separated list of integers") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Transform a measure range in MusicXML or MIDI scores across all parts/tracks."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Input MusicXML or MIDI filename/path (default base: data/input/)",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output filename/path (default base: data/output/)",
    )
    parser.add_argument(
        "--start",
        type=int,
        default=None,
        help="Start measure number (inclusive). Defaults to score start if omitted.",
    )
    parser.add_argument(
        "--end",
        type=int,
        default=None,
        help="End measure number (inclusive). Defaults to score end if omitted.",
    )
    parser.add_argument(
        "--transform",
        required=True,
        choices=["swap_pairs", "retrograde", "permute"],
        help="Transformation to apply",
    )
    parser.add_argument(
        "--pattern",
        default="",
        help="Comma-separated zero-based indices for --transform permute",
    )
    return parser


def _resolve_input(path_str: str) -> Path:
    path = Path(path_str)
    return path if path.exists() else DEFAULT_INPUT_DIR / path


def _resolve_output(path_str: str) -> Path:
    path = Path(path_str)
    return path if path.is_absolute() or path.parent != Path(".") else DEFAULT_OUTPUT_DIR / path


def _resolve_measure_bounds(
    input_path: Path,
    input_ext: str,
    start: int | None,
    end: int | None,
) -> Tuple[int, int]:
    if input_ext in {".mid", ".midi"}:
        full_start, full_end = detect_midi_measure_range(input_path)
    else:
        full_start, full_end = detect_musicxml_measure_range(input_path)

    resolved_start = full_start if start is None else start
    resolved_end = full_end if end is None else end

    if resolved_start > resolved_end:
        raise ValueError("Resolved measure bounds are invalid: start must be <= end")

    if start is None or end is None:
        print(
            "Auto-selected measure range "
            f"{resolved_start}-{resolved_end} from input score."
        )

    return resolved_start, resolved_end


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    input_path = _resolve_input(args.input)
    output_path = _resolve_output(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if args.transform == "swap_pairs":
        transform_func = swap_adjacent_pairs
    elif args.transform == "retrograde":
        transform_func = retrograde
    else:
        index_pattern = _parse_index_pattern(args.pattern)
        if not index_pattern:
            raise ValueError("--pattern is required for permute transform")

        def transform_func(measures):
            return permute_by_indices(measures, index_pattern)

    input_ext = input_path.suffix.lower()
    output_ext = output_path.suffix.lower()
    start_measure, end_measure = _resolve_measure_bounds(
        input_path=input_path,
        input_ext=input_ext,
        start=args.start,
        end=args.end,
    )

    if input_ext in {".mid", ".midi"}:
        if output_ext not in {".mid", ".midi"}:
            raise ValueError(
                "MIDI input must produce MIDI output to preserve controller data; "
                "use an output filename ending in .mid or .midi"
            )
        extract_and_transform_midi_range(
            input_path=input_path,
            output_path=output_path,
            start_measure=start_measure,
            end_measure=end_measure,
            transform_func=transform_func,
        )
    else:
        extract_and_transform_range(
            input_path=input_path,
            output_path=output_path,
            start_measure=start_measure,
            end_measure=end_measure,
            transform_func=transform_func,
        )

    print(f"Wrote transformed score to: {output_path}")


if __name__ == "__main__":
    main()
