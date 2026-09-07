# S03 — Melodyne Stem Feasibility Pilot

Experiment ID: S01.03  
Stream: D01  
Date opened: 2026-08-12  
Parent spec: D01.01 Melodyne + Suno Stem Feasibility Pilot  
Logging protocol: D01.02 Experiment Logging and Journaling Protocol  

## Purpose

S01.03 executes the bounded first pilot defined in D01.01. It tests whether Melodyne can recover compositionally useful MIDI from a representative Suno-generated passage and whether stem-based transcription outperforms full-mix transcription.

## Files in this folder

| File | Role |
|---|---|
| `S01.03_experimental_procedure.md` | Locked procedure and evaluation rubric for this pilot |
| `S01.03_run_log.csv` | Objective per-run record (one row per Melodyne pass) |
| `S01.03_melodyne_stem_pilot_journal.md` | Narrative journal: intent, observations, decisions |

## Run Classification

**R01 and R02 are preparatory runs** — technique and workflow development only, not part of the legitimate music corpus sequence:
- **R01**: beat/conductor-track alignment (Variant B conform, DP MIDI reference comparison, 16-measure target confirmation).
- **R02**: first Melodyne extraction probe (2-stem: Lead Vocal + String Section), validating SMF grid alignment before committing to the full 9-stem pass.

**R03 onward is authoritative**: this is where the actual music passages begin and where results should be drawn from for provenance analysis, evaluation, and any downstream (S01.04) work.

## Pilot Gate

Proceed to the larger study only if all four criteria from D01.01 §4 are met. Gate status is updated in the journal at the end of each session.

## External Artifact Storage

Binary artifacts (WAV stems, raw/cleaned MIDI, `.melodyne` project files, DP chunk exports) are stored outside the git repository in Dropbox, not committed to version control.

- **This pilot's Melodyne trial root folder (local path):** `/Users/davidsmith/Dropbox (Personal)/David Music Projects/Flute 2 2023 working/zf1 08 finale - transformations/`
- **This pilot's Melodyne trial materials (Dropbox shared link, folder-level):** https://www.dropbox.com/scl/fo/nlfzfaxo0kccjg456w89n/AByXAkPFx31K8xMD3MhJL4I?rlkey=hl4yessb09ffvjnxu53xyc57q&dl=0
- **Broader ZF2 project folder** (contains additional material beyond this pilot's scope — DP projects, other experiments, general assets): a separate, larger Dropbox folder exists; link to be added here once finalized.

Each run from **R03 onward** has its own sub-folder directly under the root above, named exactly as the Run ID (e.g. `S01.03-R03-20260818/`). Runs **R01–R02 predate this convention** and are not yet collated into dedicated folders (see notes in the run log).

Per-run artifact locations are referenced in `S01.03_run_log.csv` (Persistent Storage Path column) as the **relative sub-folder name only** — resolve against the root path above.

## Status

Open — in progress
