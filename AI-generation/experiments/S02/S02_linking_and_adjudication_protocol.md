# S02 Linking and Adjudication Protocol

Date: 2026-08-08  
Scope: Suno duet generation run tracking across one or more workspaces

## 1. Link Types to Capture Per Run

Capture these URLs when available from the Suno interface:

1. suno_workspace_url: the workspace page where generation is managed.
2. suno_project_url: the project or collection URL.
3. suno_result_url: the specific generated result URL.

Also capture:

1. workspace_repo_url: repository anchor for reproducibility.
2. artifact_output_path: local path to downloaded audio or bounced DP render.

## 2. Workspace ID Standard

Use stable IDs:

1. ZF2-MAIN for this repository context.
2. ZF2-EXP-XX for auxiliary experimental workspaces.

Record mappings in materials/catalogs/workspace_registry.csv.

## 3. Adjudication Labels

Use one value in adjudication_label per run:

1. like: best candidate so far within a comparison set.
2. dislike: clearly inappropriate candidate.
3. winner: promoted final choice for that set.
4. hold: uncertain, keep for possible later use.

Use winner_set_id to group runs from the same comparison batch.

Example:

1. winner_set_id = S02-T03-B01 for section token 3, batch 1.
2. All compared runs share this winner_set_id.
3. Exactly one run should end with adjudication_label = winner.

## 4. Minimal Run Entry Sequence

1. Create run row with run_id and section_token_id.
2. Paste Suno URLs immediately after generation.
3. Score role clarity and continuity fields.
4. Assign adjudication_label.
5. Mark final winner for each winner_set_id.

## 5. Persistence Guidance

If Suno interface links later change or become inaccessible:

1. keep the original URL in the run log,
2. store downloaded assets locally,
3. reference local artifact_output_path and DP bounce path as durable evidence.

## 6. Multi-Workspace Practice

When examples become too numerous, split work into additional Suno workspaces but keep one shared run ledger schema.

Use workspace_id plus winner_set_id to compare outcomes across workspaces without losing traceability.
