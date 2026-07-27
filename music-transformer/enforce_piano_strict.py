from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from src.midi_piano_strict import enforce_two_octave_attack_rule


DEFAULT_INPUT_DIR = Path("data/input")
DEFAULT_OUTPUT_DIR = Path("data/output")


def _resolve_input(path_str: str) -> Path:
    p = Path(path_str)
    return p if p.exists() else DEFAULT_INPUT_DIR / p


def _resolve_output(output_arg: str | None, input_path: Path) -> Path:
    if output_arg:
        p = Path(output_arg)
        return p if p.is_absolute() or p.parent != Path(".") else DEFAULT_OUTPUT_DIR / p
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return DEFAULT_OUTPUT_DIR / f"{input_path.stem}-strict2x12-{stamp}.mid"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Generate a strict piano-idiomatic MIDI by enforcing that each attack "
            "can be split into at most two <= octave pitch groups (2x12 rule)."
        )
    )
    parser.add_argument("--input", required=True, help="Input .mid/.midi file (default base: data/input/)")
    parser.add_argument(
        "--output",
        default=None,
        help="Output .mid path (default: data/output/<input>-strict2x12-<timestamp>.mid)",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    input_path = _resolve_input(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    if input_path.suffix.lower() not in {".mid", ".midi"}:
        raise ValueError("Input must be .mid or .midi")

    output_path = _resolve_output(args.output, input_path)
    if output_path.suffix.lower() not in {".mid", ".midi"}:
        raise ValueError("Output must be .mid or .midi")

    stats = enforce_two_octave_attack_rule(input_path=input_path, output_path=output_path)

    print(f"Wrote strict MIDI to: {output_path}")
    print(f"Attack points checked: {stats.attack_points_checked}")
    print(f"Attack points flagged: {stats.attack_points_flagged}")
    print(f"Attack notes analyzed: {stats.attack_notes_total}")
    print(f"Attack notes removed: {stats.attack_notes_removed}")


if __name__ == "__main__":
    main()
