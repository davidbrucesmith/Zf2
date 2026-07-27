# Music Transformer

Python-based modular transformer for MusicXML and MIDI score manipulation.

## Features

- Extract measure ranges across all parts dynamically (MusicXML path)
- Parse and transform MIDI Type 1 measure ranges while preserving controller/meta event content (MIDI path)
- Apply modular transforms:
  - adjacent pair swap
  - retrograde
  - custom index permutation
- Preserve MusicXML score context by explicitly injecting active `divisions`, `key`, `time`, and `clef` into the first extracted measure when missing
- Re-number transformed output measures sequentially from 1..N in each part

## Structure

```text
music-transformer/
├── data/
│   ├── input/
│   └── output/
├── src/
│   ├── __init__.py
│   ├── core.py
│   ├── midi_core.py
│   ├── midi_cleanup.py
│   ├── midi_piano_strict.py
│   └── transformations.py
├── main.py
├── cleanup_midi_notes.py
├── enforce_piano_strict.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

```bash
cd music-transformer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### MusicXML workflow

Use this path when your input is `.musicxml` and you want MusicXML output.

Run adjacent pair swap:

```bash
python main.py \
  --input score.musicxml \
  --output score-swapped.musicxml \
  --start 78 \
  --end 143 \
  --transform swap_pairs
```

Run retrograde:

```bash
python main.py \
  --input score.musicxml \
  --output score-retrograde.musicxml \
  --start 78 \
  --end 143 \
  --transform retrograde
```

Run index permutation:

```bash
python main.py \
  --input score.musicxml \
  --output score-permuted.musicxml \
  --start 78 \
  --end 83 \
  --transform permute \
  --pattern 2,0,1,5,3,4
```

MusicXML-specific behavior:
- Operates on part/measure XML structure.
- Preserves and injects active initial attributes (`divisions`, `key`, `time`, `clef`) into the first extracted measure when needed.
- Re-numbers output measures from `1..N` in each part.

### MIDI workflow

Use this path when your input is `.mid`/`.midi` and you need to preserve controller/meta content.

Run a MIDI-preserving transform (keeps CC/meta data in MIDI domain):

```bash
python main.py \
  --input source.mid \
  --output source-swapped.mid \
  --start 78 \
  --end 143 \
  --transform swap_pairs
```

Clean duplicate and overlapping MIDI notes:

```bash
python cleanup_midi_notes.py --input source.mid
```

Optional explicit output file:

```bash
python cleanup_midi_notes.py --input source.mid --output source-cleaned.mid
```

Cleanup behavior:
- Duplicate notes: if same channel+pitch starts at the same tick, extras are removed.
- Overlapping notes: if same channel+pitch overlaps, the earlier note is shortened to end at the later note start.
- Output is always MIDI.

Generate a strict piano-idiomatic version (2x12 attack rule):

```bash
python enforce_piano_strict.py --input source-cleaned.mid
```

Strict-rule behavior:
- Evaluates notes at each attack tick (new note-ons only).
- Sustained notes from earlier attacks are ignored for this rule (pedal carryover is excluded from the check).
- Keeps the largest subset of attacked notes that can be split into at most two pitch groups, each with span <= 12 semitones.
- Removes attacked notes that violate this strict constraint, and removes their matching note-offs.

Notes:
- If `--input` is just a filename, it resolves from `data/input/`.
- If `--output` is just a filename, it writes to `data/output/`.
- `--start` and `--end` are optional; if omitted, the tool auto-selects the full score range.
- `--pattern` uses zero-based indices and must have the same length as the selected measure count.
- For `.mid`/`.midi` input, output must also be `.mid`/`.midi` so controller data is preserved.
- For `.musicxml` input, use `.musicxml` output to keep notation-domain details.

## Format Warnings

### MusicXML path (`.musicxml` -> `.musicxml`)

What this path preserves:
- Part/measure notation structure
- Measure numbers (re-numbered sequentially in selected output range)
- Active initial notation attributes at extraction start (`divisions`, `key`, `time`, `clef`)

What this path may not preserve from performance-oriented sources:
- Continuous MIDI controller streams (for example modulation, expression, breath CC)
- Exact low-level MIDI event timing semantics and channel event details

What this path currently assumes/ignores:
- Transformation behavior is measure reordering, not beat-level or tick-level inversion
- Input is valid MusicXML with parseable part/measure structure

### MIDI path (`.mid`/`.midi` -> `.mid`/`.midi`)

What this path preserves:
- MIDI-domain controller and meta events that occur inside the selected measure range
- Track structure and ticks-per-beat timing base
- Relative event timing inside each moved measure chunk

What this path may alter:
- Absolute timeline position of events in the transformed range (because measures are reordered)
- Musical interpretation when files contain complex tempo/time-signature changes inside the selected range

What this path currently assumes/ignores:
- Measure boundaries are computed using the first encountered time signature
- Selected-range transforms are equal-length measure reordering operations
- This is not yet a full event-level transformation engine (for example no true tick-level retrograde mode)
