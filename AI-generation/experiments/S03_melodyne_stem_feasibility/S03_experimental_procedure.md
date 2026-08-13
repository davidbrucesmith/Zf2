# S03 Experimental Procedure

Experiment ID: S03  
Parent spec: D01.01 §5–10  
Date locked: 2026-08-12  
Status: Active

## 1. Overview

This document locks the procedure for S03 as derived from D01.01. No conditions are changed mid-pilot without a logged decision entry in `S03_melodyne_stem_pilot_journal.md`.

## 2. Section Selection Criteria

The target passage must satisfy all of the following before any processing begins.

1. Length: 16 target measures with 2-measure handles on both sides.
2. Content: identifiable melody, clear bass function, moderate harmonic density.
3. Form: at least one phrase boundary and one cadence.
4. Texture: no exceptionally dense tutti material.

Record section metadata (§2.1) before any Melodyne work starts.

### 2.1 Section Metadata

- Section ID:
- DP sequence:
- Target measures:
- Handle measures:
- Tempo/meter:
- Selection rationale:

## 3. Fixed Conditions

The following are locked for this pilot and may not be varied without a decision log entry.

1. One selected Suno version only.
2. Melodyne as the sole transcription engine.
3. Comparison scope:
   - Full DP-positioned mix render
   - Melody stem
   - Bass stem
   - Harmonic/accompaniment stem
4. No aggressive preprocessing beyond level matching and documented trimming.

## 4. Procedure

### 4.1 Prepare and Place

1. Select target section and handles per §2.
2. Place selected Suno result into DP against the source structure.
3. Bounce a DP-positioned transcription render from a known origin.

### 4.2 Stem Intake and Reconstruction Check

1. Export all available Suno stems.
2. Import stems at common origin (do not align by first transient).
3. Build summed-stem reconstruction; compare with selected mix.
4. Complete stem reconstruction log (§4.2.1) before proceeding.

#### 4.2.1 Stem Reconstruction Log

- Stem set ID:
- Source mix file:
- Summed stem file:
- Null/residual observation:
- Audible artifacts:
- Practical transcription impact:

### 4.3 Melodyne Passes

Run all four passes before applying any corrections. Export raw MIDI immediately after each pass.

Algorithm assignments (ref D01.03 §5.2):

| Input | Melodyne Algorithm |
|---|---|
| Full DP-positioned render | Melodic or Universal |
| Melody stem | Melodic |
| Bass stem | Melodic |
| Harmonic / accompaniment stem | Universal or Polyphonic (use cautiously) |

1. Full DP-positioned render → raw MIDI export
2. Melody stem → raw MIDI export
3. Bass stem → raw MIDI export
4. Harmonic stem → raw MIDI export

After all four exports: treat stem-derived MIDI as higher-confidence than mix where events conflict; suppress cross-track pitch duplicates.

Complete a transcription log row in `S03_run_log.csv` for each pass.

### 4.4 Alignment and Cleanup

1. Import all raw MIDI at common origin.
2. Measure global offset and local drift.
3. Apply minimal correction workflow: global offset first, then local fixes.
4. Prioritise melody and bass.
5. Complete edit burden log (§4.4.1) per condition.

#### 4.4.1 Edit Burden Log (per condition)

- Input condition:
- Total cleanup minutes:
- Pitch corrections:
- Octave corrections:
- Onset edits:
- Duration edits:
- Inserted notes:
- Deleted notes:

### 4.5 Compositional Trial

1. Reorchestrate cleaned melody/bass material in DP.
2. Render a short proof-of-use passage.
3. Record go/revise judgement in pilot decision log (§4.5.1).

#### 4.5.1 Pilot Decision Log

- Criteria met (1–4, ref D01.01 §4):
- Go / Revise:
- Reasons:
- Required changes before next run:

## 5. Evaluation Rubric

Score each condition on a 1–5 scale after cleanup.

| Dimension | Score (1–5) | Notes |
|---|---|---|
| Melody preservation | | |
| Bass preservation | | |
| Measure/beat alignment | | |
| Harmonic usefulness | | |
| Edit burden efficiency | | |
| Compositional usefulness | | |

Onset timing bands:

| Rating | Threshold |
|---|---|
| Excellent | ≤ 30 ms |
| Usable | ≤ 75 ms |
| Correctable | ≤ 150 ms |
| Poor | > 150 ms |

## 6. Required Deliverables

The pilot is complete when all of the following exist.

1. Raw and cleaned MIDI for each tested input condition.
2. Completed stem reconstruction log.
3. Alignment and edit burden logs for each condition.
4. Short proof-of-use render.
5. Pilot decision (Go or Revise) with rationale.
