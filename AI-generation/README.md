# AI-generation
Research workspace for iterative human-AI composition methods.

## 1. Scope
This directory contains research documents for AI-assisted compositional workflows, with emphasis on sectional symbolic recovery from generated audio.

## 2. Naming System
This folder uses Doc-ID names for research documents.

1. D means Document.
2. Dxx.00 is the parent document for one research stream.
3. Dxx.01 and above are iterative subprojects under that parent.

The D prefix exists to separate research documents from scripts, audio files, and other technical artifacts.

## 3. Current Document Map
The current hierarchy is:

1. D00.01_ai_music_generation_tooling_overview.md
2. D01.00_sectional_symbolic_recovery_master_proposal.md
3. D01.01_melodyne_stem_feasibility_pilot.md
4. D01.02_experiment_logging_and_journaling_protocol.md
5. D02.00_xml_midi_conversion_reliability_master_plan.md
6. D02.01_cleanup_midi_notes_validation_pilot.md
7. D02.02_midi_to_grandstaff_conversion_accuracy_pilot.md
8. D02.03_strict_piano_enforcement_regression_suite.md

Interpretation:

1. D01.00 is the umbrella research protocol.
2. D01.01 is the first pilot under that umbrella.
3. D01.02 defines run logging and journaling requirements for D01 pilots.
4. D02.00 is the umbrella reliability plan for XML/MIDI conversion tools.
5. D02.01 through D02.03 are initial reliability pilots under D02.00.

## 4.1 Logging Artifacts
Active experiment logging assets:

1. templates/D01_experiment_log_template.md
2. experiments/S01/S01_journal.md

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

## 6. Relation to Code Filenames
Research files should keep Doc-ID names, while Python script names should stay stable and descriptive unless a planned refactor is performed.

If code numbering is desired, prefer adding a script catalog document that maps each script to a stable Tool-ID rather than renaming runtime files immediately.
