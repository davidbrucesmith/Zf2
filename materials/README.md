# Materials Library

This directory is the intake and archival backbone for ZF2 development and ZF1 source study.

## 1. Purpose

Use this library to store and track:

1. Original ZF1 source materials used for analysis.
2. ZF1-to-ZF2 transformation analyses.
3. ZF2 working media and generated artifacts.
4. Provenance metadata for all files.

## 2. Top-Level Structure

- intake/: staging area for newly imported files before curation.
- sources/ZF1-magic-flute/: source corpus and transformation analyses rooted in ZF1.
- sources/ZF2-sequel/: active ZF2 composition assets and analyses.
- catalogs/: CSV indexes for assets and section mappings.
- templates/: metadata and analysis templates.

## 3. Intake Workflow

1. Drop raw files into intake/incoming.
2. Create one metadata note using templates/asset_intake_template.md.
3. Assign Asset ID and record row in catalogs/asset_catalog.csv.
4. Move file to final location under sources/.
5. Update section linkage in catalogs/section_catalog.csv when relevant.
6. Move rejected or duplicate files to intake/rejected with a note.

## 4. Asset ID Standard

Use deterministic IDs:

- ZF1-SRC-0001 for source artifacts from ZF1 corpus.
- ZF1-TRN-0001 for transformation-analysis artifacts derived from ZF1.
- ZF2-WIP-0001 for in-progress ZF2 working assets.
- ZF2-REL-0001 for release-ready ZF2 assets.

## 5. Supported Media Types

This repository supports mixed media including:

- .pdf, .png, .jpg, .tif
- .dorico and exported notation bundles
- .mid, .midi, .musicxml, .xml
- .wav, .aif, .aiff, .mp3, .flac
- .mov, .mp4

## 6. Naming Recommendation

Recommended filename shape:

<asset_id>__<short_title>__<yyyymmdd>__v01.<ext>

Example:

ZF1-SRC-0007__queen_of_night_aria_full_score__20260807__v01.pdf

## 7. Provenance Requirement

Every asset in sources/ should have:

1. A row in catalogs/asset_catalog.csv.
2. A metadata markdown file in a nearby metadata folder.
3. Source citation and rights note (if known).

## 8. Notes on Large Media

For very large audio/video assets, use Git LFS or external object storage and track stable links in catalogs/asset_catalog.csv.

## 9. Empty Folder Policy

Empty folders are intentionally not tracked in git.

If you need to re-create the full placeholder tree locally, run:

scripts/bootstrap_materials_tree.sh
