# S02 — Suno Operatic Duet Role Consistency Study

## Core Research Question

Can Suno generate a sectionally extended operatic duet with stable role identity between soprano and tenor when built token-by-token over synchronized Digital Performer underscoring?

## Why This Study Exists

The central problem is role confusion during extension passes, especially at handoff boundaries where one voice should yield to another.

## What S02 Tests

1. Prompt framing for role clarity.
2. Extension boundary behavior and stitch stability.
3. Influence settings that preserve harmonic continuity without collapsing vocal identity.
4. Whether clean DAW re-seeding outperforms extension from prior AI vocal tails.

## Artifact Structure

1. Procedure: S02_experimental_procedure.md
2. Mechanical run ledger: S02_run_log.csv
3. Consistency journal (actual entries): S02_suno_duet_role_consistency_journal.md
4. Linking and adjudication rules: S02_linking_and_adjudication_protocol.md
5. Run reports: S02.Rnn_YYYY-MM-DD_short-description.md

Method note:

Journaling instructions and template standards are centralized in docs/D01.02_experiment_logging_and_journaling_protocol.md.

## Naming Convention

1. Run report: S02.R01_2026-08-08_tamino-v2-extension.md
2. Next run example: S02.R02_2026-08-09_clean-reseed-test.md

## Pass Logic

A run is study-pass eligible only when both are met:

1. Role clarity >= 4
2. Boundary stability >= 4
