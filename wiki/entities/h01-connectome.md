---
title: H01 (human cortex connectome fragment)
type: entity
subtype: dataset
created: 2026-07-23
updated: 2026-07-23
sources: 1
tags: [connectome, human-brain, electron-microscopy, dataset, neuroscience, harvard, google]
---

# H01 (human cortex connectome fragment)

**H01** — a **1.4-petabyte, ~1 mm³** serial-section electron-microscopy
reconstruction of **human cerebral cortex**, jointly produced by the **Lichtman
Laboratory (Harvard University)** and **Connectomics at Google**. It is the
largest synaptic-resolution reconstruction of human brain tissue to date and the
**human-scale** data point in this wiki's connectome ladder.

## Key facts

- **~1 mm³** of human cortex, **1.4 PB** volume, nanoscale (serial-section EM)
  resolution ([H01 release](../sources/h01-human-cortex-reconstruction.md)).
- **Tens of thousands of reconstructed neurons**, millions of neuron fragments,
  **183 million annotated synapses**, **100 fully proofread cells**, plus
  subcellular annotations.
- **A dense fragment, not a complete connectome** — auto-segmented, small human
  sample, only a proofread subset verified. Contrast [FlyWire](flywire.md), which
  is a *complete* adult-fly wiring diagram.
- **Access & tools:** browsable in **Neuroglancer**; ships **SegCLR** embeddings,
  **CREST** + **CAVE** proofreading infrastructure, and programmatic APIs.
- **Publication:** *Science* 2024 (Shapson-Coe et al., doi:10.1126/science.adk4858).

## Why it matters in this wiki

H01 turns the [Connectome](../concepts/bio/connectome.md) page's "mouse and human
are the frontier" line into a concrete artifact. It also marks the **ceiling of a
question**: the wiki's two connectome→AI pathways (simulation à la
[Shiu et al. 2024](../sources/shiu-fly-brain-paper.md); connectome-constrained
nets à la [Lappalainen et al. 2024](../sources/lappalainen-flyvis-paper.md)) both
need a *complete, verified* connectome — which H01, a 100-proofread-cell fragment,
is not. Its near-term AI use is more plausibly **local-circuit statistics** and
**EM-segmentation ML** (the SegCLR direction) than whole-circuit modeling.

## Related

- [FlyWire](flywire.md) — complete fly connectome; completeness contrast.
- [Connectome](../concepts/bio/connectome.md) — the concept; H01 is its human instance.

## Mentioned in

- [H01 — A Browsable Petascale Reconstruction of the Human Cortex](../sources/h01-human-cortex-reconstruction.md)
