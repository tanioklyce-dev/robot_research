---
title: HHMI Janelia Research Campus
type: entity
subtype: research-institution
created: 2026-05-08
updated: 2026-08-30
sources: 4
tags: [hhmi, janelia, neuroscience, drosophila, fly-brain, biomechanics, mhs, microscopy, lab-automation]
---

**HHMI Janelia Research Campus** — Howard Hughes Medical Institute's pure-research lab in Ashburn, VA. Long-running anchor of *Drosophila* neuroscience and connectomics. Home of the **Turaga Lab** that led both [flybody](flybody.md) (body side, *Nature* 2025) and [flyvis / Lappalainen et al. 2024](../sources/lappalainen-flyvis-paper.md) (brain side, *Nature* 2024 — connectome-constrained deep nets predicting fly visual-system activity). Also a major contributor of *Drosophila* behavioural-tracking and connectomics tooling cited throughout the flybody paper.

## Relevant groups

- **Turaga lab** (Srinivas C. Turaga) — corresponding author on [flybody](../sources/flybody-paper.md); senior author on [Lappalainen et al. flyvis](../sources/lappalainen-flyvis-paper.md). Brain-side and body-side fly modelling sit under one PI here.
- **Branson lab** (Kristin M. Branson) — APT animal-part-tracker; Fly Disco behavioural rig.
- **Reiser lab** (Michael B. Reiser) — fly visual neuroscience; co-author on flybody.
- **Card lab** (Gwyneth M. Card, now Columbia) — fly escape behaviour neuroscience.
- **Janelia FlyEM team** (Aljoscha Nern, Kazunori Shinomiya, Shin-ya Takemura, Eyal Gruntman) — co-authors on [Lappalainen et al. 2024](../sources/lappalainen-flyvis-paper.md); produced the FIB-25 / FIB-19 optic-lobe connectomes that flyvis trains on.

## Co-origin of the Model Hardware Standard (2026)

[MHS](model-hardware-standard.md) — [Anthropic](anthropic.md)'s standard for AI agents operating physical instruments — **began here**. **Arco Bast**, a postdoc in the **Spruston lab** imaging dendrites deep in the brains of mice navigating a virtual environment, put his entire rig's state into a **shared-memory dictionary** so multi-vendor lasers, focusers and cameras could communicate at memory speed. Anthropic's **Alek Kemeny** worked with him to integrate AI models into that interface, and **Bast's microscope was the first rig to run on MHS** ([announcement](../sources/anthropic-model-hardware-standard-preview.md)).

Three Janelia projects are named in the preview:

- **Virginie Ruetten** (Ahrens lab) — whole-body two-photon imaging of larval zebrafish (WHOLISTIC imaging) for sleep research. Her rig previously required **seven vendor programs launched in a fixed order**, spanning MATLAB, Python and C#. With one shared state dictionary, adding a beam camera went from a multi-day project to **a few minutes**, analysis and viewer code is written **once per data type instead of once per device**, and an agentic acquisition loop found an oscillatory cell population a fixed setting would have missed. Her one-line summary of the value: *"the cost of hardware integration stops scaling with the number of devices."*
- **Arco Bast** (Spruston lab) — Claude aligns beams, tunes optics and checks itself against the sensors, turning a half-day of manual setup into a single step.
- **Magdalena Schneider and Hari Shroff** — agentic control of a light-sheet microscope, with Claude deciding in real time how to image developing *C. elegans* embryos and how to trade off competing imaging parameters.

Notable for this wiki: **MHS enforces device-level safety limits**, which is what lets Ruetten hand laser-power control to an agent without risking bleaching the sample — the first ingested case of a safety limit living in the device interface rather than the prompt.

## Why it matters here

- **flybody.** The physical body model + datasets came out of Janelia's confocal microscopy + behavioural-tracking infrastructure.
- **Adjacent connectomics work.** Janelia's fly connectomics (hemibrain, MANC, FANC) and FlyWire (Princeton) form a shared substrate that feeds both [Berkeley News' Shiu et al. brain model](../sources/berkeley-fly-brain-news.md) and the brain-side direction in flybody's discussion.

## Related

- [flybody](flybody.md) — primary product.
- [Google DeepMind](google-deepmind.md) — collaborator on flybody (Tassa, Botvinick).
- [FlyWire](flywire.md) — adjacent fly connectome consortium (Princeton-led; Janelia complements with hemibrain/MANC/FANC).

## Mentioned in

- [flybody Paper](../sources/flybody-paper.md)
- [flybody GitHub](../sources/flybody-github.md)
- [Lappalainen et al. 2024 — Connectome-constrained networks (fly visual system)](../sources/lappalainen-flyvis-paper.md)
- [Previewing the Model Hardware Standard](../sources/anthropic-model-hardware-standard-preview.md) — MHS originated on a Janelia microscope rig
