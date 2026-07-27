from __future__ import annotations

from math import ceil
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, List, Sequence, Tuple

from mido import Message, MetaMessage, MidiFile, MidiTrack

TrackMessage = Message | MetaMessage
TimedMessage = Tuple[int, TrackMessage]
MeasureChunk = List[Tuple[int, TrackMessage]]
TransformFunc = Callable[[List[MeasureChunk]], List[MeasureChunk]]


@dataclass
class TimeSignature:
    numerator: int = 4
    denominator: int = 4


def _first_time_signature(midi: MidiFile) -> TimeSignature:
    for track in midi.tracks:
        abs_tick = 0
        for msg in track:
            abs_tick += msg.time
            if msg.is_meta and msg.type == "time_signature":
                return TimeSignature(msg.numerator, msg.denominator)
    return TimeSignature()


def _measure_length_ticks(ticks_per_beat: int, ts: TimeSignature) -> int:
    beats_per_measure = ts.numerator * (4 / ts.denominator)
    return int(ticks_per_beat * beats_per_measure)


def _to_absolute_messages(track: MidiTrack) -> List[TimedMessage]:
    abs_tick = 0
    out: List[TimedMessage] = []
    for msg in track:
        abs_tick += msg.time
        out.append((abs_tick, msg.copy()))
    return out


def _to_delta_track(messages: Sequence[TimedMessage]) -> MidiTrack:
    out = MidiTrack()
    prev_tick = 0
    for tick, msg in sorted(messages, key=lambda x: x[0]):
        delta = tick - prev_tick
        prev_tick = tick
        out.append(msg.copy(time=delta))
    return out


def _max_tick(all_tracks: Sequence[List[TimedMessage]]) -> int:
    max_tick = 0
    for track in all_tracks:
        if track:
            max_tick = max(max_tick, track[-1][0])
    return max_tick


def _slice_measure_chunks(
    messages: List[TimedMessage],
    start_tick: int,
    end_tick: int,
    measure_ticks: int,
    measure_count: int,
) -> Tuple[List[TimedMessage], List[MeasureChunk], List[TimedMessage]]:
    before: List[TimedMessage] = []
    chunks: List[MeasureChunk] = [[] for _ in range(measure_count)]
    after: List[TimedMessage] = []

    for abs_tick, msg in messages:
        if abs_tick < start_tick:
            before.append((abs_tick, msg))
            continue
        if abs_tick >= end_tick:
            after.append((abs_tick, msg))
            continue

        rel_tick = abs_tick - start_tick
        measure_index = rel_tick // measure_ticks
        if 0 <= measure_index < measure_count:
            tick_in_measure = rel_tick % measure_ticks
            chunks[measure_index].append((tick_in_measure, msg))

    return before, chunks, after


def _rebuild_selected_range(
    start_tick: int,
    measure_ticks: int,
    transformed_chunks: List[MeasureChunk],
) -> List[TimedMessage]:
    rebuilt: List[TimedMessage] = []
    for i, chunk in enumerate(transformed_chunks):
        measure_start = start_tick + (i * measure_ticks)
        for tick_in_measure, msg in chunk:
            rebuilt.append((measure_start + tick_in_measure, msg))
    return rebuilt


def detect_midi_measure_range(input_path: str | Path) -> tuple[int, int]:
    """Return the inclusive measure-number span available in a MIDI file."""
    midi = MidiFile(str(input_path))
    ts = _first_time_signature(midi)
    measure_ticks = _measure_length_ticks(midi.ticks_per_beat, ts)
    if measure_ticks <= 0:
        raise ValueError("Could not compute a valid measure length from time signature")

    abs_tracks = [_to_absolute_messages(track) for track in midi.tracks]
    total_ticks = _max_tick(abs_tracks)

    # Include a boundary event exactly at measure start as belonging to that measure.
    measure_count = max(1, ceil((total_ticks + 1) / measure_ticks))
    return 1, measure_count


def extract_and_transform_midi_range(
    input_path: str | Path,
    output_path: str | Path,
    start_measure: int,
    end_measure: int,
    transform_func: TransformFunc,
) -> None:
    """
    Transform a measure range in a MIDI file while preserving non-note events such as CC.

    Assumptions:
    - Measures are computed using the first encountered time signature.
    - Selected range length is preserved by permutation-style transforms.
    """
    if start_measure > end_measure:
        raise ValueError("start_measure must be <= end_measure")

    midi = MidiFile(str(input_path))
    ts = _first_time_signature(midi)
    measure_ticks = _measure_length_ticks(midi.ticks_per_beat, ts)
    if measure_ticks <= 0:
        raise ValueError("Could not compute a valid measure length from time signature")

    measure_count = (end_measure - start_measure) + 1
    start_tick = (start_measure - 1) * measure_ticks
    end_tick = end_measure * measure_ticks

    abs_tracks = [_to_absolute_messages(track) for track in midi.tracks]
    total_ticks = _max_tick(abs_tracks)
    if start_tick > total_ticks:
        raise ValueError(
            f"start_measure {start_measure} begins past end of MIDI timeline "
            f"(max tick {total_ticks})"
        )

    out_midi = MidiFile(type=midi.type, ticks_per_beat=midi.ticks_per_beat)

    for abs_messages in abs_tracks:
        before, chunks, after = _slice_measure_chunks(
            abs_messages,
            start_tick=start_tick,
            end_tick=end_tick,
            measure_ticks=measure_ticks,
            measure_count=measure_count,
        )

        transformed = transform_func(chunks)
        if len(transformed) != measure_count:
            raise ValueError(
                "Transform changed selected measure count for MIDI pipeline; "
                "this engine currently supports equal-length reordering transforms"
            )

        rebuilt_range = _rebuild_selected_range(
            start_tick=start_tick,
            measure_ticks=measure_ticks,
            transformed_chunks=transformed,
        )

        merged = before + rebuilt_range + after
        out_midi.tracks.append(_to_delta_track(merged))

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    out_midi.save(str(output_path))
