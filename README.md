# Zf2
Materials for the development of the sequel.

## 1. Repository Purpose
This repository gathers composition materials, research protocols, and transformation tooling for iterative human-AI music development.

Current activity is centered on:

1. AI-generation research design and pilot execution.
2. XML/MIDI conversion reliability in the transformation tooling pipeline.
3. ZF1 source-corpus analysis and ZF2 transformation mapping.

## 2. Repository Areas
The repository currently has three major work areas.

1. AI-generation: research documents, protocol design, and experiment logs.
2. music-transformer: Python tools for MIDI cleanup, strict piano enforcement, and MusicXML conversion.
3. materials: source/media archive with provenance catalogs for ZF1 and ZF2 assets.

## 3. Document Naming Convention
Research documents use a Doc-ID system with parent/child structure.

1. D means Document.
2. Dxx.00 is the parent document for a research stream.
3. Dxx.01, Dxx.02, and so on are iterative subprojects under that parent.

Examples in this repository:

1. AI-generation/docs/D01.00_sectional_symbolic_recovery_master_proposal.md
2. AI-generation/docs/D01.01_melodyne_stem_feasibility_pilot.md

The purpose of D is to distinguish research documents from executable tools and other asset types.

## 4. Tooling Workstream Note
The XML/MIDI applications are active development tools and may not always be reliable yet for every source file.

To keep naming clean:

1. Research documents continue with the Dxx.yy pattern.
2. Code filenames stay descriptive and stable unless a controlled refactor is planned.
3. Reliability work for conversion tools should be tracked as numbered documents under a dedicated parent stream, then linked to specific scripts in music-transformer.

## 5. Materials Intake and Cataloging

The repository now includes a formal media intake and provenance flow under materials/.

Start here:

1. Read materials/README.md.
2. Drop incoming files into materials/intake/incoming/.
3. Fill materials/templates/asset_intake_template.md.
4. Add a row to materials/catalogs/asset_catalog.csv.
5. Add or update section linkage in materials/catalogs/section_catalog.csv.
6. Move curated files into materials/sources/ZF1-magic-flute/ or materials/sources/ZF2-sequel/.

Note: empty archive folders are not tracked in git; run scripts/bootstrap_materials_tree.sh to restore the full local placeholder tree.

## 6. New Analysis Stream (D03)

The D03 stream formalizes source-to-sequel scholarship and transformation logic.

1. D03.00 ZF1 source and transformation corpus master plan
2. D03.01 ZF1 source analysis protocol
3. D03.02 ZF1-to-ZF2 transformation mapping protocol

## 7. External Reference Material
Some earlier planning material is still in Google Docs and chat links.

Extracted material:

1. [Extracted Chat GPT Material](https://docs.google.com/document/d/1aD2C_F0yRsx1otk6vEvOy0rPnrpN_BIG8zTjHZesrME/edit?usp=sharing)
2. [Full Download of ChatGPT materials for the PaTa Fight](https://docs.google.com/document/d/1dHCCGN8CMFbc5uEmf15jGeMNvaiF96e3fwA4r9tq9ss/edit?usp=sharing)

Session links:

1. [Acquiring Light vs Wisdom](https://chatgpt.com/share/bce3ce51-55be-41fd-b32a-0a85fd4aedac)
2. [Rewrite Pamina Tamino Dialog](https://chatgpt.com/share/67463184-1430-800f-a61f-8dbc3c81f43d)





