from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import DefaultDict, Dict, List, Tuple
from collections import defaultdict, deque

from mido import Message, MetaMessage, MidiFile, MidiTrack


@dataclass
class AbsEvent:
    tick: int
    msg: Message | MetaMessage
    order: int
    keep: bool = True


@dataclass
class NotePair:
    track_idx: int
    key: Tuple[int, int]  # (channel, pitch)
    start_tick: int
    end_tick: int
    on_idx: int
    off_idx: int
    remove: bool = False


@dataclass
class StrictStats:
    attack_points_checked: int = 0
    attack_points_flagged: int = 0
    attack_notes_total: int = 0
    attack_notes_removed: int = 0


def _is_note_on(msg: Message | MetaMessage) -> bool:
    return isinstance(msg, Message) and msg.type == "note_on" and msg.velocity > 0


def _is_note_off(msg: Message | MetaMessage) -> bool:
    return isinstance(msg, Message) and (
        msg.type == "note_off" or (msg.type == "note_on" and msg.velocity == 0)
    )


def _to_absolute_events(track: MidiTrack) -> List[AbsEvent]:
    t = 0
    out: List[AbsEvent] = []
    for order, msg in enumerate(track):
        t += msg.time
        out.append(AbsEvent(tick=t, msg=msg.copy(), order=order))
    return out


def _to_delta_track(events: List[AbsEvent]) -> MidiTrack:
    kept = [e for e in events if e.keep]
    kept.sort(key=lambda e: (e.tick, e.order))

    out = MidiTrack()
    prev = 0
    for e in kept:
        delta = e.tick - prev
        prev = e.tick
        out.append(e.msg.copy(time=delta))
    return out


def _extract_note_pairs(track_idx: int, events: List[AbsEvent]) -> List[NotePair]:
    active: DefaultDict[Tuple[int, int], deque[Tuple[int, int]]] = defaultdict(deque)
    pairs: List[NotePair] = []

    for idx, e in enumerate(events):
        msg = e.msg
        if _is_note_on(msg):
            key = (msg.channel, msg.note)
            active[key].append((e.tick, idx))
        elif _is_note_off(msg):
            key = (msg.channel, msg.note)
            if not active[key]:
                continue
            start_tick, on_idx = active[key].popleft()
            pairs.append(
                NotePair(
                    track_idx=track_idx,
                    key=key,
                    start_tick=start_tick,
                    end_tick=e.tick,
                    on_idx=on_idx,
                    off_idx=idx,
                )
            )

    return pairs


def _is_two_octave_compatible(pitches: List[int]) -> bool:
    if not pitches:
        return True
    s = sorted(pitches)
    if s[-1] - s[0] <= 12:
        return True
    n = len(s)
    for k in range(1, n):
        left = s[:k]
        right = s[k:]
        if (left[-1] - left[0] <= 12) and (right[-1] - right[0] <= 12):
            return True
    return False


def _choose_keep_indices_for_attack(pitches: List[int]) -> set[int]:
    """
    Keep the largest subset that can be represented by <=2 pitch groups,
    each spanning <= 12 semitones. Notes are evaluated at the same attack tick.
    """
    n = len(pitches)
    if n <= 1:
        return set(range(n))

    sorted_items = sorted(enumerate(pitches), key=lambda x: (x[1], x[0]))
    idxs = [i for i, _ in sorted_items]
    vals = [p for _, p in sorted_items]

    intervals: List[Tuple[int, int]] = []
    for i in range(n):
        j = i
        while j < n and vals[j] - vals[i] <= 12:
            j += 1
        intervals.append((i, j - 1))

    best_len = 0
    best_choice: List[Tuple[int, int]] = []

    for a in intervals:
        a_len = a[1] - a[0] + 1
        if a_len > best_len:
            best_len = a_len
            best_choice = [a]

    for a in intervals:
        for b in intervals:
            if a[1] < b[0]:
                total = (a[1] - a[0] + 1) + (b[1] - b[0] + 1)
                if total > best_len:
                    best_len = total
                    best_choice = [a, b]

    keep_sorted_positions: set[int] = set()
    for itv in best_choice:
        keep_sorted_positions.update(range(itv[0], itv[1] + 1))

    keep_original = {idxs[pos] for pos in keep_sorted_positions}
    return keep_original


def enforce_two_octave_attack_rule(
    input_path: str | Path,
    output_path: str | Path,
) -> StrictStats:
    """
    Enforce a strict piano-idiomatic attack rule on MIDI:

    - At each note attack tick, keep only the largest subset of attacked notes
      that can be split into <=2 pitch groups with <=1 octave span each.
    - Sustained notes from earlier attacks are ignored for this rule.
    """
    midi = MidiFile(str(input_path))
    out_midi = MidiFile(type=midi.type, ticks_per_beat=midi.ticks_per_beat)

    all_track_events = [_to_absolute_events(track) for track in midi.tracks]
    all_track_pairs = [
        _extract_note_pairs(track_idx=i, events=events)
        for i, events in enumerate(all_track_events)
    ]

    attack_groups: Dict[int, List[NotePair]] = defaultdict(list)
    for pairs in all_track_pairs:
        for pair in pairs:
            attack_groups[pair.start_tick].append(pair)

    stats = StrictStats()

    for tick in sorted(attack_groups.keys()):
        group = attack_groups[tick]
        if not group:
            continue

        pitches = [pair.key[1] for pair in group]
        stats.attack_points_checked += 1
        stats.attack_notes_total += len(group)

        if _is_two_octave_compatible(pitches):
            continue

        stats.attack_points_flagged += 1
        keep_idxs = _choose_keep_indices_for_attack(pitches)

        for i, pair in enumerate(group):
            if i in keep_idxs:
                continue
            pair.remove = True
            stats.attack_notes_removed += 1

    for pairs in all_track_pairs:
        for pair in pairs:
            if not pair.remove:
                continue
            events = all_track_events[pair.track_idx]
            events[pair.on_idx].keep = False
            events[pair.off_idx].keep = False

    for events in all_track_events:
        out_midi.tracks.append(_to_delta_track(events))

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    out_midi.save(str(output_path))
    return stats
