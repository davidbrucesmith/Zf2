#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

mkdir -p \
  materials/intake/incoming \
  materials/intake/processing \
  materials/intake/rejected \
  materials/sources/ZF1-magic-flute/originals/scores \
  materials/sources/ZF1-magic-flute/originals/libretti \
  materials/sources/ZF1-magic-flute/originals/manuscripts \
  materials/sources/ZF1-magic-flute/originals/midi \
  materials/sources/ZF1-magic-flute/originals/musicxml \
  materials/sources/ZF1-magic-flute/originals/audio \
  materials/sources/ZF1-magic-flute/originals/video \
  materials/sources/ZF1-magic-flute/originals/images \
  materials/sources/ZF1-magic-flute/originals/analysis \
  materials/sources/ZF1-magic-flute/originals/references \
  materials/sources/ZF1-magic-flute/transformations/harmonic \
  materials/sources/ZF1-magic-flute/transformations/melodic \
  materials/sources/ZF1-magic-flute/transformations/formal \
  materials/sources/ZF1-magic-flute/transformations/orchestration \
  materials/sources/ZF1-magic-flute/transformations/rhythm \
  materials/sources/ZF1-magic-flute/metadata \
  materials/sources/ZF2-sequel/sketches \
  materials/sources/ZF2-sequel/sections \
  materials/sources/ZF2-sequel/stems \
  materials/sources/ZF2-sequel/notation/dorico \
  materials/sources/ZF2-sequel/notation/musicxml \
  materials/sources/ZF2-sequel/notation/pdf \
  materials/sources/ZF2-sequel/midi \
  materials/sources/ZF2-sequel/audio \
  materials/sources/ZF2-sequel/video \
  materials/sources/ZF2-sequel/analysis \
  materials/sources/ZF2-sequel/exports \
  materials/sources/ZF2-sequel/metadata \
  materials/catalogs \
  materials/templates

echo "Materials directory scaffold ensured at: $repo_root/materials"
