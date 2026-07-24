---
title: "H01 — A Browsable Petascale Reconstruction of the Human Cortex (Lichtman Lab / Google Connectomics)"
type: source
url: https://h01-release.storage.googleapis.com/landing.html
author: Lichtman Laboratory (Harvard University) & Connectomics at Google
published: 2024-05-10
ingested: 2026-07-23
venue: "Science 384 (2024), doi:10.1126/science.adk4858 — landing/data-release page"
tags: [connectome, neuroscience, human-brain, electron-microscopy, brain-mapping, dataset, google, harvard]
---

# H01 — A Browsable Petascale Reconstruction of the Human Cortex

## Summary

**H01** is the largest-scale synaptic-resolution reconstruction of **human** brain tissue to date: roughly **one cubic millimeter** of human cerebral cortex imaged by serial-section electron microscopy and reconstructed into a browsable **1.4-petabyte** volume. Produced by the **Lichtman Lab (Harvard)** and **Connectomics at Google**, it is the human-scale entry in the connectomics program this wiki tracks from *C. elegans* → fly → mouse → human. The release page is a data portal (Neuroglancer viewer, embeddings, proofreading tools), with the science written up in *Science* (Shapson-Coe et al., "A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution," 2024).

## Key claims

- **Scale.** A **1.4-petabyte** volume covering **~1 mm³** of human cortex, at nanoscale (serial-section EM) resolution.
- **Contents.** **Tens of thousands of reconstructed neurons**, **millions of neuron fragments**, **183 million annotated synapses**, and many additional subcellular annotations/structures. **100 cells** are fully **proofread**.
- **Not a complete connectome.** Unlike [FlyWire](../entities/flywire.md)'s *complete* adult-fly wiring diagram, H01 is a **dense reconstruction of a small human sample** — automatically segmented, with only a proofread subset verified. It is a fragment, not a whole-brain connectome; the value is scale + human tissue, not completeness.
- **Tooling shipped with the release:**
  - **Neuroglancer** — in-browser volumetric viewer for the segmentation.
  - **SegCLR embeddings** — learned "informative and concise" representations of local fields of view (for classification / similarity search over the segmentation).
  - **CREST** (Connectome Reconstruction and Exploration Simple Tool) and **CAVE** (Connectome Annotation Versioning Engine) — proofreading / annotation infrastructure.
  - Programmatic (API) data access.
- **Publication.** Written up in *Science* (2024), doi:10.1126/science.adk4858; the landing page is the public data release accompanying it.

## Entities mentioned

- [H01 connectome](../entities/h01-connectome.md) — the dataset entity (this page's subject).
- [FlyWire](../entities/flywire.md) — the *complete* fly connectome, contrast case for "dense sample vs whole brain."

## Concepts touched

- [Connectome](../concepts/bio/connectome.md) — H01 is the concrete **human** instance on the *C. elegans* → fly → mouse → human ladder; it sharpens the "mouse and human are the frontier" line into a real petascale human artifact.

## Open questions

- **Can H01 drive a model the way fly connectomes do?** The wiki's connectome→AI pathways ([Shiu et al. 2024](shiu-fly-brain-paper.md) simulation; [Lappalainen et al. 2024](lappalainen-flyvis-paper.md) connectome-constrained nets) both rely on a *complete, verified* connectome. H01 is a fragment with only 100 proofread cells — likely too partial for whole-circuit simulation, but plausibly useful for **local-circuit statistics** and as EM-reconstruction ML training data (the SegCLR direction).
- **Human vs fly gap.** Fly whole-brain = 139k neurons; human = ~86B. H01's 1 mm³ makes the scale gap visceral: petabytes for a pinhead of cortex. What "human connectome" even means at that ratio is an open framing question.
