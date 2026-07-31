# Research Proposal and Experimental Procedure

## Sectional Audio-to-MIDI Recovery in an Iterative Human–AI Compositional Workflow

**Working title:**  
**Sectional Symbolic Recovery from Generative Audio: Testing a Digital Performer–Suno–Melodyne Iterative Composition Pipeline**

**Principal investigator:** David B. Smith  
**Status:** Developmental research proposal  
**Document type:** Research proposal and experimental protocol  
**Version:** 0.1  
**Date:** 2026-07-30

---

## 1. Abstract

This project investigates whether generative audio produced through Suno can be recovered as compositionally useful MIDI and reintegrated into an existing Digital Performer project. The workflow begins with music derived from Mozart and transformed through conventional compositional procedures in Digital Performer. Selected sections are bounced to audio and submitted to Suno in Cover mode using high audio and style influence. Multiple generated versions are evaluated, and the most useful result is selected, edited, aligned, crossfaded, and reinserted into the original Digital Performer sequence.

The proposed experiment tests the next stage of this iterative process: whether selected Suno-generated material can be separated into stems, converted into MIDI using Melodyne and comparison systems, aligned to the pre-existing Digital Performer measure-and-beat structure, and used as raw material for further manipulation and reorchestration. The goal is not exact score reconstruction. Instead, the experiment evaluates whether the recovered MIDI preserves enough pitch, rhythm, phrase, register, and formal information to support a subsequent compositional cycle.

The research treats the original Digital Performer project as the authoritative global temporal and formal structure. Suno-generated segments are understood as bounded transformations of specific source sections. Audio-to-MIDI recovery is therefore evaluated sectionally rather than as a reconstruction of an entire continuous performance. Particular attention is given to melody, bass, temporal alignment, measure mapping, stem reconstruction, and the human labor required to convert extracted MIDI into musically useful symbolic material.

---

## 2. Research Context

Generative audio systems can produce musically compelling transformations of existing material, but their outputs are usually delivered as audio rather than as editable symbolic representations. This creates a discontinuity in compositional workflows that depend on notation, MIDI, orchestration, formal manipulation, and iterative rewriting.

In the proposed workflow, generative audio is not treated as a final production endpoint. It functions as an intermediate compositional state. The composer begins with historically existing material, applies transformations in Digital Performer, generates further versions through Suno, selects useful results, and then attempts to recover symbolic material from the generated audio. The recovered MIDI is reintroduced into Digital Performer, where it can be edited, reorchestrated, recomposed, and subjected to another transformation cycle.

The process is therefore recursive:

```text
Mozart-derived source
→ transformation in Digital Performer
→ sectional audio bounce
→ Suno generation
→ selection and placement in Digital Performer
→ stem extraction
→ audio-to-MIDI recovery
→ compositional cleanup and reinterpretation
→ reorchestration
→ subsequent iteration
```

The central research issue is not whether the generated audio can be transcribed perfectly. The relevant question is whether the recovered MIDI is sufficiently coherent, aligned, and editable to become useful compositional material.

---

## 3. Problem Statement

Current audio-to-MIDI conversion systems often produce incomplete, over-dense, rhythmically unstable, or poorly aligned results when applied to complex polyphonic audio. These problems become more pronounced when the source includes:

- multiple instruments occupying similar registers;
- doubled pitches and octave reinforcement;
- reverberation and sustained spectral energy;
- contrapuntal inner voices;
- dense orchestration;
- tremolo, trills, and ornamental activity;
- flexible tempo or local timing drift;
- ambiguous downbeats or metrical interpretation;
- artifacts introduced by automated stem separation.

Suno may also alter the duration, phrase structure, accompaniment, instrumentation, articulation, or metric emphasis of the submitted section. Even when the generated result remains recognizably related to the source material, its events may not align automatically with the original Digital Performer measure grid.

The practical problem is therefore divided into two related tasks:

1. **Symbolic recovery:** extracting useful pitch, onset, duration, register, and phrase information from generated audio.
2. **Temporal reintegration:** mapping those recovered events back into an existing Digital Performer sequence whose measures and beats provide the larger compositional structure.

---

## 4. Purpose of the Study

The purpose of this developmental study is to determine whether a sectional Digital Performer–Suno–Melodyne workflow can reliably produce MIDI that is useful for continued composition.

The study will test:

- whether melody and bass can be recovered with sufficient clarity;
- whether polyphonic harmonic material can provide usable pitch or chord evidence;
- whether extracted MIDI can be aligned to an existing measure-and-beat structure;
- whether Suno-generated stems reconstruct the original generated mix with acceptable fidelity;
- whether processing stems separately improves MIDI recovery;
- how much manual intervention is required;
- whether transcription errors are merely obstructive or can also generate useful compositional alternatives;
- whether the recovered material can be reorchestrated and incorporated into a subsequent compositional iteration.

---

## 5. Research Questions

### 5.1 Primary Research Question

Can selected Suno-generated audio segments be converted into sufficiently coherent and temporally aligned MIDI to support further manipulation, rewriting, and reorchestration in Digital Performer?

### 5.2 Secondary Research Questions

1. Does stem-based transcription produce more useful MIDI than transcription of the complete stereo mix?
2. Which stem categories yield the most useful symbolic material?
3. Are melody and bass recovered more reliably than harmonic or ensemble material?
4. How accurately do extracted MIDI events align with the existing Digital Performer measure-and-beat structure?
5. Is it more effective to transcribe the raw Suno output or a Digital Performer-positioned bounce of the selected segment?
6. How much manual correction is required before the MIDI becomes compositionally usable?
7. Which errors are destructive, and which errors produce useful transformations?
8. Does Suno stem separation preserve the complete generated result when the stems are recombined?
9. How do different audio-to-MIDI systems compare in event accuracy, structural usefulness, and edit burden?
10. Can recovered material be successfully reorchestrated and passed through a subsequent cycle of transformation?

---

## 6. Working Hypotheses

### H1: Sectional recovery will be more useful than global transcription

Because each Suno output corresponds to a bounded section of an existing Digital Performer sequence, local recovery and alignment will be more reliable than attempting to reconstruct an entire work from generated audio.

### H2: Melody and bass will yield the highest-value MIDI

Monophonic or near-monophonic melodic and bass stems are expected to produce more coherent pitch and onset information than dense harmonic or ensemble stems.

### H3: The Digital Performer-positioned render will improve temporal reintegration

A bounce created after the selected Suno segment has been placed in Digital Performer is expected to provide a more reliable transcription source than the raw Suno output because the positioned render reflects the actual edit, offset, duration, and placement used in the composition.

### H4: Stem separation will improve some forms of transcription but introduce other errors

Stem isolation is expected to reduce polyphonic ambiguity, but Suno's automated source separation may omit, duplicate, or misclassify material. The benefit of stem-based transcription must therefore be tested rather than assumed.

### H5: Exact transcription will not be necessary for compositional usefulness

Recovered MIDI may remain valuable even when it contains false positives, missing notes, altered note lengths, octave errors, or simplified rhythms, provided that it preserves salient melodic, bass, harmonic, rhythmic, or formal features.

---

## 7. Scope and Delimitations

This study is not intended to produce a definitive transcription of a complete Suno arrangement. It focuses on the recovery of compositional material from selected sections.

The first experiment will prioritize:

- melody;
- bass;
- clear harmonic material;
- phrase-level structure;
- event placement;
- measure and beat alignment;
- human edit burden;
- compositional usefulness.

The first experiment will not require:

- complete orchestral reconstruction;
- exact recovery of instrumentation;
- exact dynamic reconstruction;
- reliable notation of all ornaments;
- full drum transcription;
- exact separation of every contrapuntal voice;
- complete elimination of transcription artifacts.

Percussion, effects, reverberant textures, and residual material may remain as audio unless they produce clearly useful symbolic information.

---

## 8. Conceptual Model

The workflow uses three forms of representation:

### 8.1 Symbolic Representation

MIDI, notation, tempo maps, meter, formal labels, orchestration, and other editable compositional structures.

### 8.2 Audio Representation

Digital Performer bounces, Suno-generated versions, selected audio segments, stems, crossfades, and re-rendered results.

### 8.3 Interpretive Representation

Human decisions concerning phrase identity, harmonic function, voice leading, formal correspondence, errors, transformations, and compositional value.

The process is not a simple conversion from audio to MIDI. It is a mediated cycle among symbolic, audio, and interpretive forms.

```text
Symbolic composition
        ↓
Audio rendering
        ↓
Generative transformation
        ↓
Audio selection and placement
        ↓
Symbolic recovery
        ↓
Human interpretation and rewriting
        ↓
New symbolic composition
```

---

## 9. System Architecture

### 9.1 Authoritative Global Structure

The original Digital Performer sequence remains the authoritative global structure for:

- measure numbering;
- meter;
- formal placement;
- section boundaries;
- relationships among preceding and following material;
- final arrangement of selected Suno segments.

### 9.2 Local Generated Objects

Each selected Suno result is treated as a bounded transformation object associated with:

- a source section;
- an export region;
- a selected generated version;
- an in-point and out-point;
- a final Digital Performer placement;
- an optional local tempo interpretation;
- a set of stems;
- one or more MIDI recovery outputs.

### 9.3 Hybrid Final Session

The resulting Digital Performer project may contain:

- original MIDI;
- transformed MIDI;
- raw Suno audio;
- selected and positioned Suno audio;
- Suno stems;
- recovered raw MIDI;
- cleaned MIDI;
- reorchestrated MIDI;
- crossfades and composite audio;
- analytical markers and notes.

Not every sound must be converted to MIDI. The final system may remain intentionally hybrid.

---

## 10. Experimental Design

### 10.1 General Design

The study will use a repeated-measures comparative design. The same musical section will be processed through multiple recovery conditions so that differences can be attributed to the source type or transcription method rather than to the musical passage.

### 10.2 Independent Variables

The initial experiment will compare the following conditions:

#### Source Condition

1. Full Suno stereo mix.
2. Suno melody or vocal stem, when relevant.
3. Suno bass stem.
4. Suno harmonic or accompaniment stem.
5. Digital Performer-positioned bounce of the selected Suno segment.
6. Optional composite crossfade bounce.

#### Transcription Condition

1. Melodyne.
2. Suno native MIDI extraction, when available.
3. Basic Pitch or another comparison system.
4. Optional additional system such as RipX.

#### Alignment Condition

1. Original Digital Performer grid.
2. Melodyne-detected grid.
3. Manually corrected local grid.
4. Absolute-time placement followed by structural remapping.

### 10.3 Dependent Variables

The experiment will evaluate:

- pitch recovery;
- onset accuracy;
- duration accuracy;
- octave accuracy;
- measure placement;
- beat placement;
- phrase preservation;
- bass-line preservation;
- melodic-contour preservation;
- harmonic usefulness;
- edit time;
- number of manual corrections;
- compositional usefulness;
- success of reorchestration;
- success of reintegration into the larger sequence.

---

## 11. Selection of Test Material

### 11.1 Passage Length

The initial test should use one section of approximately:

- 16 measures of primary material;
- 2 measures of preceding context;
- 2 measures of following context.

The complete export region will therefore contain approximately 20 measures.

A later phase may compare:

- 8-measure sections;
- 16-measure sections;
- 24- to 32-measure sections.

### 11.2 Musical Characteristics

The selected passage should contain at least three types of musical information:

1. a clearly identifiable melody;
2. a structurally meaningful bass line;
3. a harmonic or contrapuntal accompaniment of moderate complexity.

The passage should also contain:

- at least one clear phrase boundary;
- at least one cadence;
- a stable metric framework;
- enough internal contrast to test transcription quality.

The first test should avoid an exceptionally dense tutti passage. Such material can be introduced in a later stress test.

### 11.3 Source Documentation

The selected source passage should be documented with:

- work and movement;
- source measure numbers;
- Digital Performer sequence name;
- tempo;
- meter;
- instrumentation;
- transformation procedures already applied;
- intended formal function;
- reason for selecting the passage.

---

## 12. Experimental Materials

### 12.1 Software

- Digital Performer
- Suno
- Melodyne Editor or Studio
- Optional comparison system:
  - Suno native MIDI extraction
  - Basic Pitch
  - RipX
  - another audio-to-MIDI system

### 12.2 File Formats

Preferred formats:

- WAV for all audio exchange;
- MIDI Type 1 where supported;
- native Digital Performer project format;
- native Melodyne project or transfer files;
- CSV or Markdown for logs and evaluation;
- PNG or PDF for selected screenshots;
- Markdown for research documentation.

### 12.3 Audio Specifications

Use one consistent format throughout the experiment:

```text
Sample rate: 48 kHz
Bit depth: 24-bit
Channel format: stereo unless a mono stem is explicitly exported
Normalization: disabled
Dither: disabled until final delivery
```

The exact format may be changed if required, but it must remain consistent and documented.

---

## 13. Provenance and Naming Convention

Each experimental object should be traceable to its source.

### 13.1 Section Identifier

Use a stable section identifier:

```text
S01
```

### 13.2 Suggested Naming Pattern

```text
S01_m033-048_DP-SOURCE.mid
S01_m031-050_DP-BOUNCE.wav
S01_m031-050_SUNO-v01_RAW.wav
S01_m031-050_SUNO-v02_RAW.wav
S01_m031-050_SUNO-v03_RAW.wav
S01_m031-050_SUNO-v04_SELECTED.wav
S01_m033-048_SUNO-v04_DP-PLACED.wav
S01_m033-048_SUNO-v04_BASS.wav
S01_m033-048_SUNO-v04_MELODY.wav
S01_m033-048_SUNO-v04_HARMONY.wav
S01_m033-048_MELODYNE-BASS_RAW.mid
S01_m033-048_MELODYNE-MELODY_RAW.mid
S01_m033-048_MELODYNE-HARMONY_RAW.mid
S01_m033-048_MELODYNE-CLEANED.mid
S01_m033-048_REORCHESTRATED.mid
```

### 13.3 Version Control

Large audio files may be stored outside the main Git repository or managed through Git LFS. The repository should contain:

- documentation;
- metadata;
- logs;
- MIDI files;
- screenshots;
- small reference exports;
- checksums or links for externally stored audio.

---

## 14. Repository Structure

```text
/
├── README.md
├── docs/
│   ├── research-proposal.md
│   ├── experimental-protocol.md
│   ├── evaluation-rubric.md
│   └── findings.md
├── experiments/
│   └── S01/
│       ├── metadata/
│       │   ├── section-metadata.md
│       │   ├── suno-generation-log.md
│       │   └── alignment-log.md
│       ├── source/
│       │   ├── midi/
│       │   └── reference-score/
│       ├── audio/
│       │   ├── dp-bounce/
│       │   ├── suno-raw/
│       │   ├── suno-selected/
│       │   ├── stems/
│       │   └── dp-positioned/
│       ├── transcription/
│       │   ├── melodyne/
│       │   ├── suno-midi/
│       │   ├── basic-pitch/
│       │   └── cleaned/
│       ├── dp/
│       │   ├── alignment-session/
│       │   └── reorchestration-session/
│       ├── analysis/
│       │   ├── event-analysis.csv
│       │   ├── timing-analysis.csv
│       │   ├── stem-null-test.md
│       │   └── qualitative-evaluation.md
│       └── renders/
│           ├── recovered-midi-render/
│           └── reorchestrated-render/
└── templates/
    ├── section-metadata-template.md
    ├── generation-log-template.md
    ├── alignment-log-template.md
    └── evaluation-template.md
```

---

## 15. Experimental Procedure

## Phase 1: Prepare the Digital Performer Source

### Step 1. Select the Test Section

Select one approximately 16-measure section from the transformed Mozart-derived Digital Performer project.

Record:

- sequence name;
- source measures;
- export measures;
- tempo;
- meter;
- section function;
- instrumentation;
- existing transformations;
- intended start and end boundaries.

### Step 2. Preserve Context Handles

Include approximately two measures before and two measures after the target section.

Example:

```text
Target replacement region: mm. 33–48
Export region: mm. 31–50
Leading handle: mm. 31–32
Trailing handle: mm. 49–50
```

### Step 3. Create a Reference MIDI Export

Export the source and transformed MIDI for the section.

Preserve:

- original timing;
- tempo map;
- meter map;
- track names;
- measure origin;
- any pickup or preroll.

### Step 4. Bounce the Section

Bounce the complete export region to WAV.

Requirements:

- begin exactly at the first beat of the export region;
- do not trim leading silence;
- do not normalize;
- preserve all tempo changes;
- record the bounce settings;
- create a checksum if the file is stored externally.

---

## Phase 2: Generate Suno Variants

### Step 5. Submit the Section to Suno

Upload the Digital Performer bounce to Suno.

Record:

- date;
- Suno model or mode;
- Cover mode settings;
- audio influence;
- style influence;
- prompt or style description;
- any advanced settings;
- generation identifier.

### Step 6. Generate Multiple Versions

Generate a minimum of four variants.

Do not select solely on similarity. Evaluate each variant for:

- melodic interest;
- bass interest;
- harmonic transformation;
- formal compatibility;
- phrase coherence;
- orchestration;
- ability to connect to surrounding material;
- potential for symbolic recovery.

### Step 7. Select the Most Useful Variant

Choose one primary version for the initial experiment.

Record:

- why it was selected;
- what it preserves;
- what it changes;
- what material appears most promising for MIDI recovery;
- whether the generated duration differs from the source duration.

Retain all versions for later comparison.

---

## Phase 3: Reinsert and Position the Selected Audio

### Step 8. Import the Selected Suno Version into Digital Performer

Import the complete raw Suno result into a copy of the original Digital Performer project.

Do not trim the master source file destructively.

### Step 9. Identify the Retained Segment

Determine:

- selected in-point;
- selected out-point;
- relationship to the source section;
- whether the generated segment is shorter, equal, or longer;
- whether the phrase boundaries correspond to the source;
- whether internal edits are required.

### Step 10. Place the Segment in the Existing Sequence

Position the selected audio relative to the original Digital Performer structure.

Classify the placement method:

- **Conform:** the generated segment is made to fit the original duration;
- **Reflow:** the Digital Performer timeline is altered to accommodate the generated timing;
- **Composite:** part of the generated result is used with crossfades or overlaps;
- **Hybrid:** a combination of the above.

### Step 11. Create Audio Transitions

Create the required edits and crossfades.

Document:

- crossfade start and end;
- fade curve;
- overlapping source material;
- time stretching or compression;
- inserted or removed material;
- any change to the conductor track.

### Step 12. Create a DP-Positioned Transcription Render

Bounce the selected Suno layer from a known Digital Performer origin after it has been positioned.

Preferably:

- begin at the first beat of the source export region or target region;
- include silence before the first generated event when necessary;
- preserve the exact final offset;
- exclude unrelated original material;
- exclude the composite crossfade unless it is being tested separately.

This render becomes the principal Melodyne input.

---

## Phase 4: Obtain and Validate Stems

### Step 13. Export Available Suno Stems

Export all stems that Suno provides.

Possible categories may include:

- vocals or melody;
- bass;
- drums;
- accompaniment;
- other;
- residual material.

Record the exact labels provided by Suno. Do not assume that the labels accurately describe the contents.

### Step 14. Import All Stems into Digital Performer

Import all stems at the same origin.

Do not align stems by their first audible event. Preserve their common file start.

### Step 15. Perform a Stem Reconstruction Test

Create a summed stem mix:

```text
Stem Sum = Stem 1 + Stem 2 + ... + Stem n
```

Compare it with the original selected Suno mix.

Evaluate:

- timing equality;
- duration equality;
- gain difference;
- phase difference;
- missing material;
- duplicated material;
- spectral difference;
- audible artifacts.

Where possible, perform a null test:

```text
Difference Signal = Original Suno Mix − Summed Stems
```

Document whether the stems:

- null closely;
- differ only in gain;
- contain significant residual material;
- introduce audible separation artifacts;
- fail to reconstruct the original.

The stem sum does not need to null perfectly for the stems to be useful, but the discrepancy must be documented.

### Step 16. Assess Stem Purity

For each stem, note:

- dominant musical role;
- interfering instruments;
- leakage;
- omitted notes;
- transient artifacts;
- phase artifacts;
- suitability for monophonic transcription;
- suitability for polyphonic transcription.

---

## Phase 5: Melodyne Transcription

### Step 17. Establish a Common Temporal Origin

Before transcription, confirm that each input file begins at a documented Digital Performer origin.

For example:

```text
File origin: DP measure 31, beat 1
Target material begins: approximately measure 33
```

### Step 18. Transcribe the DP-Positioned Full Segment

Import the positioned full segment into Melodyne.

Test the most appropriate algorithm:

- melodic;
- polyphonic sustain;
- polyphonic decay;
- universal;
- percussive, if relevant.

Do not correct all errors initially.

Export a raw MIDI file that reflects Melodyne's first-pass analysis.

### Step 19. Transcribe the Melody Stem

Use the melodic algorithm when the stem is primarily monophonic.

Export:

- raw MIDI;
- optional corrected MIDI;
- screenshot of note detection;
- notes concerning octave, ornament, and onset errors.

### Step 20. Transcribe the Bass Stem

Use the melodic algorithm when the bass is monophonic or near-monophonic.

Export:

- raw MIDI;
- optional corrected MIDI;
- notes concerning missing fundamentals, octave displacement, and repeated-note errors.

### Step 21. Transcribe the Harmonic Stem

Use an appropriate polyphonic algorithm.

Treat the output as harmonic evidence rather than as a finished performance.

Record:

- missing chord tones;
- added harmonics;
- octave duplication;
- voice confusion;
- useful pitch collections;
- useful registral information.

### Step 22. Correct Melodyne's Tempo Interpretation

Examine:

- tempo;
- downbeat placement;
- measure length;
- pickup interpretation;
- half-time or double-time detection;
- local ritardando or accelerando;
- fermatas;
- phrase boundaries.

Create two exports where possible:

1. MIDI preserving absolute event placement;
2. MIDI using a corrected local tempo and measure interpretation.

Do not replace the original Digital Performer conductor track during the first comparison.

---

## Phase 6: Comparison Transcriptions

### Step 23. Generate Suno Native MIDI

Where available, obtain MIDI from Suno for the same stems or source segment.

Preserve it without correction as a baseline.

### Step 24. Generate Basic Pitch MIDI

Process the same source files through Basic Pitch or another comparison system.

Use identical source boundaries.

### Step 25. Preserve Raw Outputs

Do not overwrite or clean the original outputs.

Each system should produce:

- raw MIDI;
- source metadata;
- processing notes;
- software version;
- algorithm or preset;
- date of processing.

---

## Phase 7: Import and Alignment in Digital Performer

### Step 26. Create an Alignment Sequence

Create a new Digital Performer sequence or chunk dedicated to evaluation.

Include:

- original transformed MIDI;
- source DP bounce;
- raw Suno audio;
- selected positioned audio;
- all available stems;
- all raw MIDI transcriptions;
- measure markers;
- phrase markers;
- cadence markers.

### Step 27. Import MIDI at the Common Origin

Import each MIDI file at the documented file origin.

Do not align the first MIDI note manually to the first audible audio note.

The file origin and silence before the first event must be preserved.

### Step 28. Test Absolute-Time Correspondence

Play each MIDI track against the source stem or selected audio.

Evaluate whether MIDI attacks occur at the same audible moments as the audio events.

At this stage:

- do not quantize;
- do not alter tempo;
- do not move isolated notes for musical correctness;
- do not force the result into the source measure grid.

Record global offsets and local drift.

### Step 29. Test Measure-and-Beat Correspondence

Compare extracted events with the original Digital Performer grid.

For each significant event, determine:

- expected source measure and beat;
- extracted absolute time;
- extracted measure and beat;
- timing displacement;
- whether the displacement is global or local;
- whether the event belongs to the corresponding source location.

### Step 30. Identify Alignment Type

Classify each section or phrase:

- grid-preserving;
- grid-compatible but elastic;
- structurally divergent;
- locally ambiguous;
- unalignable without reinterpretation.

### Step 31. Correct Global Offset

If all extracted events share a consistent offset, correct the track origin once.

Do not correct individual notes until the global offset is resolved.

### Step 32. Correct Local Tempo or Structural Drift

Where necessary:

- create a local tempo map;
- insert or remove measures;
- remap phrase boundaries;
- use time scaling;
- preserve a copy of the unmodified transcription.

Document every structural correction.

---

## Phase 8: MIDI Cleanup

### Step 33. Create a Duplicate for Editing

Duplicate each raw MIDI transcription before cleanup.

### Step 34. Clean Melody and Bass First

Prioritize:

- false short notes;
- octave errors;
- repeated-note fragmentation;
- merged repeated notes;
- missing structural pitches;
- incorrect note endings;
- gross onset errors;
- spurious chromatic events;
- overlapping duplicates.

### Step 35. Preserve Ambiguous Material

Do not automatically delete all unexpected events.

Classify them as:

- transcription artifact;
- plausible generated detail;
- useful compositional mutation;
- unresolved.

### Step 36. Normalize Only After Verification

After confirming audio correspondence, create a compositionally normalized version.

Possible operations include:

- partial quantization;
- metric reinterpretation;
- rhythmic simplification;
- voice separation;
- register reassignment;
- chord reduction;
- duration normalization;
- phrase-level realignment.

Preserve the raw timing version.

---

## Phase 9: Reorchestration and Compositional Test

### Step 37. Reorchestrate the Cleaned MIDI

Assign recovered MIDI to new instruments in Digital Performer.

The reorchestration should not attempt to imitate Suno exactly. It should test whether the recovered symbolic material can support coherent compositional development.

### Step 38. Apply Further Transformations

Apply selected compositional procedures, such as:

- reharmonization;
- inversion;
- fragmentation;
- augmentation or diminution;
- registral redistribution;
- contrapuntal recombination;
- rhythmic displacement;
- orchestral reassignment;
- formal extension;
- recomposition of missing material.

### Step 39. Render the Reorchestrated Result

Bounce the reorchestrated MIDI.

Compare it with:

- the original Digital Performer section;
- the selected Suno audio;
- the raw recovered MIDI render;
- the cleaned MIDI render.

### Step 40. Determine Whether the Cycle Can Continue

Evaluate whether the reorchestrated result is suitable for another Suno iteration.

If so, document it as the beginning of Cycle 2.

---

## 16. Evaluation Framework

The experiment should combine quantitative, structural, and qualitative evaluation.

### 16.1 Event-Level Evaluation

For melody and bass, sample a defined set of significant events.

Measure:

- correct pitch;
- correct octave;
- onset displacement;
- duration displacement;
- missing note;
- false note;
- repeated-note accuracy.

Suggested onset categories:

```text
Excellent: within 30 ms
Usable: within 75 ms
Correctable: within 150 ms
Poor: greater than 150 ms
```

These thresholds are provisional and may be revised based on musical context.

### 16.2 Grid Alignment Evaluation

For each phrase, rate:

- correct measure placement;
- correct beat placement;
- correct downbeat interpretation;
- preservation of phrase length;
- preservation of cadence location;
- degree of local drift.

Suggested scale:

```text
5 — aligned with minimal correction
4 — globally aligned; minor local correction
3 — musically recognizable; moderate remapping required
2 — substantial manual reconstruction required
1 — no reliable measure or beat correspondence
```

### 16.3 Structural Evaluation

Rate preservation of:

- melodic contour;
- bass motion;
- harmonic rhythm;
- phrase boundaries;
- cadence points;
- motivic identity;
- formal direction;
- registral profile.

### 16.4 Stem Evaluation

For each stem, rate:

- isolation quality;
- leakage;
- missing material;
- duplication;
- artifact level;
- transcription suitability;
- usefulness relative to the full mix.

### 16.5 Edit Burden

Record:

- total cleanup time;
- number of note deletions;
- number of pitch corrections;
- number of octave corrections;
- number of onset corrections;
- number of duration corrections;
- number of inserted notes;
- number of structural remappings;
- number of tempo-map edits.

Time should be divided into:

- technical alignment;
- transcription correction;
- compositional reinterpretation;
- reorchestration.

### 16.6 Compositional Usefulness

Use the following provisional scale:

```text
5 — immediately supports substantial new composition
4 — highly useful after limited correction
3 — useful as partial or fragmentary material
2 — useful only as analytical or referential evidence
1 — not compositionally useful
```

A result may receive a low transcription-accuracy score but a high compositional-usefulness score.

### 16.7 Round-Trip Success

The workflow will be considered successful when:

- at least melody or bass can be recovered;
- the recovered material can be aligned to a meaningful section of the DP grid;
- cleanup does not require complete manual retranscription;
- the MIDI supports reorchestration or transformation;
- the new result can be reintegrated into the composition;
- the process can plausibly continue into another iteration.

---

## 17. Data Collection Templates

### 17.1 Section Metadata

```markdown
# Section Metadata

- Section ID:
- Work:
- Movement:
- DP sequence:
- Target measures:
- Export measures:
- Meter:
- Tempo:
- Instrumentation:
- Source transformations:
- Formal function:
- Selection rationale:
```

### 17.2 Suno Generation Log

```markdown
# Suno Generation Log

- Section ID:
- Generation date:
- Model/mode:
- Audio influence:
- Style influence:
- Prompt:
- Version ID:
- Duration:
- Preserved features:
- Transformed features:
- Structural differences:
- Selection status:
- Selection rationale:
```

### 17.3 Alignment Log

```markdown
# Alignment Log

- Section ID:
- Source file:
- MIDI system:
- File origin:
- DP placement:
- Global offset:
- Local drift:
- Original measure span:
- Generated measure interpretation:
- Placement method:
- Tempo-map changes:
- Structural remapping:
- Notes:
```

### 17.4 Evaluation Log

```markdown
# Evaluation Log

- Section ID:
- Source condition:
- Transcription system:
- Stem:
- Pitch accuracy:
- Onset accuracy:
- Duration accuracy:
- Grid alignment:
- Phrase preservation:
- Bass preservation:
- Melody preservation:
- Harmonic usefulness:
- Edit time:
- Compositional usefulness:
- Recommended use:
- Notes:
```

---

## 18. Risks and Mitigations

### Risk 1: Stem Misclassification

Suno may place relevant events in the wrong stem.

**Mitigation:** Inspect all stems, compare them with the complete mix, and allow transcription of multiple stems or stem combinations.

### Risk 2: Stem Sum Does Not Equal the Original Mix

Automated separation may introduce residual differences.

**Mitigation:** Perform a reconstruction and difference test. Retain the original full mix as the authoritative audio reference.

### Risk 3: Melodyne Detects the Wrong Meter or Downbeat

Correct pulse detection may still produce incorrect measure placement.

**Mitigation:** Preserve absolute timing, establish manual phrase anchors, and correct the grid separately from note extraction.

### Risk 4: Audio Placement and MIDI Placement Diverge

Independent trimming or alignment may destroy synchronization.

**Mitigation:** Use a common file origin. Transcribe a DP-positioned render and import MIDI at that same origin.

### Risk 5: Crossfades Produce Ambiguous Composite Material

A crossfade may contain two overlapping musical sources.

**Mitigation:** Transcribe the Suno layer separately. Treat composite crossfades as optional derived objects.

### Risk 6: Polyphonic MIDI Is Too Dense

Harmonics and overlapping sources may create excessive false notes.

**Mitigation:** Treat polyphonic output as harmonic evidence. Reduce, filter, or manually voice the material rather than treating it as a finished score.

### Risk 7: Manual Correction Becomes Equivalent to Retranscription

The process may save little time.

**Mitigation:** Record edit burden explicitly. A method should be considered effective only when it provides meaningful structural material faster or more productively than manual transcription.

### Risk 8: Software or Model Behavior Changes

Suno and transcription tools may change over time.

**Mitigation:** Record software version, model, date, settings, and file checksums for every experiment.

---

## 19. Ethical and Intellectual Property Considerations

The experiment should use source material that is legally appropriate for transformation and research. Mozart's compositions are in the public domain, but specific modern editions, performances, recordings, arrangements, and samples may remain protected.

The study should distinguish among:

- public-domain composition;
- newly created Digital Performer realization;
- generated Suno output;
- automated stems;
- recovered MIDI;
- human-edited and reorchestrated material.

The research record should preserve provenance and avoid presenting generated or recovered material as an authoritative reconstruction of Mozart's score.

Where outputs are published, the repository should document:

- source composition;
- source edition, if relevant;
- human transformations;
- generative platform;
- transcription systems;
- extent of human editing;
- licensing restrictions on audio files.

---

## 20. Reproducibility Requirements

A complete experimental record should include:

- software versions;
- Suno model and settings;
- Melodyne algorithm;
- export settings;
- audio sample rate and bit depth;
- source and target measure numbers;
- exact file origins;
- raw and cleaned MIDI;
- generation identifiers;
- screenshots of tempo and note interpretation;
- stem reconstruction results;
- evaluation logs;
- notes on manual decisions;
- checksums for externally stored audio.

All raw outputs must be preserved separately from edited outputs.

---

## 21. Criteria for Initial Success

The first experiment will be considered successful if all of the following occur:

1. The selected Suno segment can be placed reliably in the original Digital Performer sequence.
2. At least one stem yields recognizable melody or bass MIDI.
3. The extracted MIDI can be synchronized with the corresponding audio.
4. The MIDI can be mapped to meaningful measures and beats with manageable correction.
5. Cleanup requires less effort than complete manual retranscription or provides substantially different creative value.
6. The cleaned MIDI can be reorchestrated into a coherent new passage.
7. The reorchestrated passage can be integrated into the larger composition.
8. The procedure produces enough documentation to repeat the experiment with another section.

---

## 22. Criteria for Failure or Revision

The method should be revised if:

- no stem produces recognizable symbolic material;
- MIDI timing cannot be aligned reliably even in absolute time;
- stem errors obscure the desired material;
- measure mapping requires complete manual reconstruction;
- correction time exceeds the value of the recovered material;
- the recovered MIDI contributes no meaningful new compositional possibilities;
- the experiment cannot be reproduced from the documentation.

A failed transcription may still produce useful findings about source selection, section length, stem quality, model behavior, or appropriate limits of symbolic recovery.

---

## 23. Proposed Experimental Sequence

### Experiment 1: Baseline Sectional Recovery

- One 16-measure target section
- Two-measure handles
- Four Suno generations
- One selected version
- Full mix transcription
- Melody stem transcription
- Bass stem transcription
- Harmonic stem transcription
- Melodyne as primary system
- Suno MIDI and Basic Pitch as comparison systems
- Reimport into original DP grid
- Cleanup and reorchestration

### Experiment 2: Section-Length Comparison

Compare:

- 8 measures;
- 16 measures;
- 24–32 measures.

Evaluate whether longer context improves generation but impairs alignment.

### Experiment 3: Texture Complexity

Compare:

- monophonic melody with accompaniment;
- moderate polyphony;
- dense orchestral texture.

### Experiment 4: Raw versus DP-Positioned Transcription

Compare transcription of:

- raw Suno output;
- selected raw segment;
- DP-positioned bounce;
- DP-positioned and time-conformed bounce.

### Experiment 5: Second-Generation Round Trip

Take the cleaned and reorchestrated MIDI from Experiment 1, render it, submit it to Suno, and repeat the recovery process.

Evaluate whether the system:

- converges;
- diverges;
- preserves motivic identity;
- accumulates artifacts;
- generates productive novelty.

---

## 24. Anticipated Contributions

The study may contribute:

1. a reproducible workflow for sectional symbolic recovery from generative audio;
2. a method for retaining Digital Performer as the authoritative formal structure;
3. a stem-conditioned transcription strategy;
4. a distinction between transcription accuracy and compositional usefulness;
5. a framework for evaluating human labor in AI-assisted music workflows;
6. a hybrid audio/MIDI approach that does not require every sound to become symbolic;
7. a model for iterative human–AI co-composition;
8. a basis for student research, comparative tool evaluation, and future automation.

---

## 25. Developmental Interpretation

The experiment should not be framed as a contest between human transcription and machine transcription. The relevant system is collaborative.

The generative model produces new audio states. Stem separation exposes partial layers. Audio-to-MIDI systems provide candidate symbolic interpretations. Digital Performer supplies the stable formal and temporal environment. The composer supplies theoretical judgment, correction, orchestration, and decisions concerning what should be preserved, rejected, or transformed.

The workflow is therefore best understood as a distributed compositional system in which no single component possesses a complete representation of the work.

---

## 26. Immediate Next Actions

1. Select the first 16-measure test passage.
2. Define the target and handle measures.
3. create the `S01` experiment directory.
4. Export reference MIDI and the DP audio bounce.
5. Generate at least four Suno versions.
6. Select and position one version in Digital Performer.
7. Export the DP-positioned transcription render.
8. Export all available stems.
9. Perform the stem reconstruction test.
10. Run Melodyne on the full segment, melody stem, bass stem, and harmonic stem.
11. Import all raw MIDI at the common Digital Performer origin.
12. Complete the alignment and evaluation logs.
13. Clean melody and bass first.
14. Reorchestrate the recovered material.
15. Document whether the workflow is ready for a second cycle.

---

## 27. Provisional Conclusion

The proposed workflow is technically plausible because it does not depend on exact automatic transcription. Its success depends on maintaining provenance, preserving a common temporal origin, treating the original Digital Performer sequence as the global structural scaffold, and evaluating symbolic recovery section by section.

The most promising initial path is to use the selected and positioned Suno segment as the temporal reference, extract available stems, prioritize melody and bass, preserve raw MIDI before correction, and distinguish absolute-time synchronization from musical-grid interpretation. The experiment will determine whether current tools can provide enough symbolic evidence to support continued compositional work without requiring full manual retranscription.

The broader significance lies in the iterative cycle itself: audio generation becomes neither a final rendering nor an opaque endpoint, but an intermediate stage in a recursive process of transformation, recovery, interpretation, and recomposition.
