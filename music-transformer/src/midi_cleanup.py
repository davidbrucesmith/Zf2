from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Deque, Dict, List, Tuple

from mido import Message, MetaMessage, MidiFile, MidiTrack


@dataclass
class AbsEvent:
    tick: int
    msg: Message | MetaMessage
    order: int
    keep: bool = True


@dataclass
class NoteEvent:
    key: Tuple[int, int]
    start_tick: int
    end_tick: int
    start_event_idx: int
    end_event_idx: int
    removed: bool = False


@dataclass
class CleanupStats:
    duplicate_notes_removed: int = 0
    overlapping_notes_trimmed: int = 0
    notes_total: int = 0


def _is_note_on(msg: Message | MetaMessage) -> bool:
    return (
        isinstance(msg, Message)
        and msg.type == "note_on"
        and msg.velocity > 0
    )


def _is_note_off(msg: Message | MetaMessage) -> bool:
    return (
        isinstance(msg, Message)
        and (msg.type == "note_off" or (msg.type == "note_on" and msg.velocity == 0))
    )


def _to_absolute_events(track: MidiTrack) -> List[AbsEvent]:
    abs_tick = 0
    events: List[AbsEvent] = []
    for order, msg in enumerate(track):
        abs_tick += msg.time
        events.append(AbsEvent(tick=abs_tick, msg=msg.copy(), order=order))
    return events


def _to_delta_track(events: List[AbsEvent]) -> MidiTrack:
    kept = [e for e in events if e.keep]
    kept.sort(key=lambda e: (e.tick, e.order))

    out = MidiTrack()
    prev_tick = 0
    for e in kept:
        delta = e.tick - prev_tick
        prev_tick = e.tick
        out.append(e.msg.copy(time=delta))
    return out


def _extract_notes(events: List[AbsEvent]) -> List[NoteEvent]:
    active: Dict[Tuple[int, int], Deque[Tuple[int, int]]] = defaultdict(deque)
    notes: List[NoteEvent] = []

    for idx, e in enumerate(events):
        msg = e.msg
        if _is_note_on(msg):
            key = (msg.channel, msg.note)
            active[key].append((e.tick, idx))
        elif _is_note_off(msg):
            key = (msg.channel, msg.note)
            if not active[key]:
                continue
            start_tick, start_idx = active[key].popleft()
            notes.append(
                NoteEvent(
                    key=key,
                    start_tick=start_tick,
                    end_tick=e.tick,
                    start_event_idx=start_idx,
                    end_event_idx=idx,
                )
            )

    return notes


def _clean_note_events(notes: List[NoteEvent], events: List[AbsEvent]) -> CleanupStats:
    by_key: Dict[Tuple[int, int], List[NoteEvent]] = defaultdict(list)
    for n in notes:
        by_key[n.key].append(n)

    stats = CleanupStats(notes_total=len(notes))

    for key_notes in by_key.values():
        key_notes.sort(key=lambda n: (n.start_tick, n.end_tick, n.start_event_idx))

        prev: NoteEvent | None = None
        for curr in key_notes:
            if prev is None:
                prev = curr
                continue

            if prev.removed:
                prev = curr
                continue

            # Duplicate onset at the same tick for same pitch/channel.
            if curr.start_tick == prev.start_tick:
                prev.end_tick = max(prev.end_tick, curr.end_tick)
                curr.removed = True
                events[curr.start_event_idx].keep = False
                events[curr.end_event_idx].keep = False
                stats.duplicate_notes_removed += 1
                continue

            # Overlap: trim the earlier note to the later note start.
            if curr.start_tick < prev.end_tick:
                prev.end_tick = curr.start_tick
                stats.overlapping_notes_trimmed += 1

            prev = curr

    for n in notes:
        if n.removed:
            continue
        if n.end_tick <= n.start_tick:
            n.removed = True
            events[n.start_event_idx].keep = False
            events[n.end_event_idx].keep = False
            continue
        events[n.end_event_idx].tick = n.end_tick

    return stats


def cleanup_midi_overlaps(
    input_path: str | Path,
    output_path: str | Path,
) -> CleanupStats:
    """
    Remove duplicate same-pitch notes and trim overlapping same-pitch notes per track.

    Rules:
    - Duplicate notes (same channel+pitch and same start tick): keep one, remove extras.
    - Overlapping notes (same channel+pitch): shorten the earlier note so it ends at
      the later note start.
    """
    midi = MidiFile(str(input_path))
    out_midi = MidiFile(type=midi.type, ticks_per_beat=midi.ticks_per_beat)

    total = CleanupStats()

    for track in midi.tracks:
        events = _to_absolute_events(track)
        notes = _extract_notes(events)
        stats = _clean_note_events(notes, events)

        total.duplicate_notes_removed += stats.duplicate_notes_removed
        total.overlapping_notes_trimmed += stats.overlapping_notes_trimmed
        total.notes_total += stats.notes_total

        out_midi.tracks.append(_to_delta_track(events))

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    out_midi.save(str(output_path))
    return total
