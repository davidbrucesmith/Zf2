# AI-generation
Research workspace for iterative human-AI composition methods.

## 1. Scope
This directory contains research documents for AI-assisted compositional workflows, with emphasis on sectional symbolic recovery from generated audio.

## 2. Naming System
This folder uses Doc-ID names for research documents.

D-series protocol and planning documents are stored in docs/.

1. D means Document.
2. Dxx.00 is the parent document for one research stream.
3. Dxx.01 and above are iterative subprojects under that parent.

The D prefix exists to separate research documents from scripts, audio files, and other technical artifacts.

## 3. Current Document Map
The current hierarchy is:

1. docs/D00.01_ai_music_generation_tooling_overview.md
2. docs/D01.00_sectional_symbolic_recovery_master_proposal.md
3. docs/D01.01_melodyne_stem_feasibility_pilot.md
4. docs/D01.02_experiment_logging_and_journaling_protocol.md
5. docs/D02.00_xml_midi_conversion_reliability_master_plan.md
6. docs/D02.01_cleanup_midi_notes_validation_pilot.md
7. docs/D02.02_midi_to_grandstaff_conversion_accuracy_pilot.md
8. docs/D02.03_strict_piano_enforcement_regression_suite.md
9. docs/D03.00_zf1_source_and_transformation_corpus_master_plan.md
10. docs/D03.01_zf1_source_analysis_protocol.md
11. docs/D03.02_zf1_to_zf2_transformation_mapping_protocol.md

Interpretation:

1. D01.00 is the umbrella research protocol.
2. D01.01 is the first pilot under that umbrella.
3. D01.02 defines run logging and journaling requirements for D01 pilots.
4. D02.00 is the umbrella reliability plan for XML/MIDI conversion tools.
5. D02.01 through D02.03 are initial reliability pilots under D02.00.
6. D03.00 is the umbrella plan for ZF1 source analysis and ZF2 transformation mapping.
7. D03.01 and D03.02 define source-analysis and transformation-mapping execution standards.

## 4.1 Logging Artifacts
Active experiment logging assets:

1. templates/D01_experiment_log_template.md
2. experiments/S01/S01_journal.md
3. experiments/S02/S02_experimental_procedure.md
4. experiments/S02/S02_run_log.csv
5. experiments/S02/S02_suno_duet_role_consistency_journal.md

## 4. How to Add New Work
When creating another subproject under the same umbrella:

1. Keep parent as D01.00.
2. Add the next child as D01.02, D01.03, and so on.
3. Keep each child narrow, testable, and executable.

When opening a new umbrella stream:

1. Create a new parent as D02.00.
2. Add children as D02.01, D02.02, and so on.

## 5. Active Reliability Stream
The D02 stream is now active and provides a structured path for debugging and hardening conversion tools.

Use sequence:

1. D02.01 first (note-event correctness baseline)
2. D02.02 second (MusicXML conversion validity)
3. D02.03 third (strict piano rule regression hardening)

## 6. Active Source-to-Sequel Analysis Stream
The D03 stream is now active and provides the research structure for ZF1 source study and ZF1-to-ZF2 transformation mapping.

Use sequence:

1. D03.01 first (source-analysis records)
2. D03.02 second (transformation-mapping records)

## 7. Relation to Code Filenames
Research files should keep Doc-ID names, while Python script names should stay stable and descriptive unless a planned refactor is performed.

If code numbering is desired, prefer adding a script catalog document that maps each script to a stable Tool-ID rather than renaming runtime files immediately.
