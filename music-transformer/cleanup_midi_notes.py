from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from src.midi_cleanup import cleanup_midi_overlaps


DEFAULT_INPUT_DIR = Path("data/input")
DEFAULT_OUTPUT_DIR = Path("data/output")


def _resolve_input(path_str: str) -> Path:
    path = Path(path_str)
    return path if path.exists() else DEFAULT_INPUT_DIR / path


def _timestamped_output_name(input_path: Path) -> str:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"{input_path.stem}-cleaned-{stamp}.mid"


def _resolve_output(output_arg: str | None, input_path: Path) -> Path:
    if output_arg:
        out = Path(output_arg)
        return out if out.is_absolute() or out.parent != Path(".") else DEFAULT_OUTPUT_DIR / out
    return DEFAULT_OUTPUT_DIR / _timestamped_output_name(input_path)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Clean a MIDI file by removing duplicate same-pitch notes and trimming "
            "overlapping same-pitch notes."
        )
    )
    parser.add_argument("--input", required=True, help="Input .mid/.midi file (default base: data/input/)")
    parser.add_argument(
        "--output",
        default=None,
        help="Output .mid path (default: data/output/<input>-cleaned-<timestamp>.mid)",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    input_path = _resolve_input(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.suffix.lower() not in {".mid", ".midi"}:
        raise ValueError("Input file must be .mid or .midi")

    output_path = _resolve_output(args.output, input_path)
    if output_path.suffix.lower() not in {".mid", ".midi"}:
        raise ValueError("Output file must be .mid or .midi")

    stats = cleanup_midi_overlaps(input_path=input_path, output_path=output_path)

    print(f"Wrote cleaned MIDI to: {output_path}")
    print(f"Total notes analyzed: {stats.notes_total}")
    print(f"Duplicate notes removed: {stats.duplicate_notes_removed}")
    print(f"Overlapping notes trimmed: {stats.overlapping_notes_trimmed}")


if __name__ == "__main__":
    main()
