# S02 Experimental Procedure: Suno Duet Role Consistency

Section ID: S02  
Parent stream: D01 Sectional Symbolic Recovery (pre-Melodyne stage)  
Date opened: 2026-08-08  
Status: Active

## 1. Purpose

This experiment tests how to generate a coherent operatic duet in Suno between soprano and tenor without role confusion.

The core issue is role instability in generated outputs, especially when square-bracket role cues are ignored or blended.

This is a pre-Melodyne experiment. The immediate goal is better vocal-role consistency before symbolic recovery.

## 2. Working Strategy

Use Digital Performer (DP) as the authoritative timing and synchronization environment.

Workflow concept:

1. Compose or arrange underscoring in DP for each target section.
2. Generate Suno output one verse or phrase token at a time.
3. Reinsert generated result into DP and align to section boundaries.
4. Extend duet progressively by adding the next token section.
5. Evaluate whether role identity remains stable across concatenated sections.

## 3. Primary Questions

1. Can iterative sectional generation reduce soprano/tenor role confusion compared with single-pass full-duet prompts?
2. Which prompt structures best preserve role assignment?
3. Does consistent DP underscoring improve continuity of voice identity across generations?
4. What section length best balances continuity and role clarity?

## 4. Test Conditions

Test a matrix of approaches. Keep all non-tested variables fixed within each run block.

### 4.1 Prompt Strategy Variants

1. Role labels only (baseline).
2. Role labels plus explicit dramatic action cues.
3. Role labels plus register cues.
4. Alternating single-line entries per role before overlap lines.
5. Overlap lines encoded as staggered entries rather than simultaneous role cues.

### 4.2 Section Stitching Variants

1. One phrase per generation.
2. Two-phrase blocks per generation.
3. Fixed overlap handles (1-2 measures) between consecutive generations.
4. No overlap handles (hard boundary control).

### 4.3 Underscoring Variants

1. Constant orchestral bed across all iterations.
2. Lightly varied underscoring by phrase.
3. Reduced texture in vocal handoff zones.

## 5. Fixed Controls

For each run block, lock:

1. Tempo and meter map in DP.
2. Section boundary markers in measures and beats.
3. Lyric text source edition for that section.
4. Output loudness normalization target.
5. Evaluation rubric and reviewer.

## 6. Procedure

### 6.1 Section Preparation in DP

1. Define section token ID and measure span.
2. Print underscoring reference render from fixed origin.
3. Prepare lyric token for this run.

### 6.2 Suno Generation

1. Submit one token block with selected prompt strategy variant.
2. Render N candidates (set N before block starts).
3. Select best candidate by rubric (Section 7).

### 6.3 DP Reintegration

1. Import selected output at section origin.
2. Align to DP grid.
3. If needed, trim and crossfade using fixed handle policy.
4. Bounce cumulative duet build after each accepted token.

### 6.4 Iterative Extension

1. Carry forward accepted cumulative audio as context.
2. Generate next token section.
3. Repeat until target scene segment is complete.

## 7. Evaluation Rubric (1-5)

1. Role clarity.
2. Role stability across section boundaries.
3. Text intelligibility per role.
4. Musical continuity with prior section.
5. Alignment to DP timing and phrase cadence.
6. Edit burden after import.

Section pass gate:

- Role clarity >= 4 and boundary stability >= 4.

## 8. Failure Taxonomy

1. Role swap.
2. Role merge.
3. Register collapse.
4. Boundary drift.
5. Text-role mismatch.

## 9. Automation Note

If no official, stable Suno API is available for your account tier, treat this as a human-in-the-loop experiment and log runs manually in S02_run_log.csv. If API access becomes available, keep the same run schema so manual and automated runs remain comparable.

## 10. Deliverables

1. Versioned DP section bounces per token stage.
2. Selected Suno outputs per run with metadata.
3. Cumulative stitched duet renders.
4. Completed run log and session journal entries.
5. End summary recommending stable generation strategy.
