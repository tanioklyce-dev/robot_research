---
title: FlyWire
type: entity
subtype: dataset-consortium
created: 2026-05-08
updated: 2026-05-08
sources: 1
tags: [flywire, connectome, drosophila, neuroscience, brain-mapping]
---

**FlyWire** — international consortium and public dataset providing the **complete neuronal wiring diagram of the adult *Drosophila melanogaster* brain**: 139,255 neurons and ~50 million synaptic connections. Released in October 2024 across multiple *Nature* papers. Public access at flywire.ai. ([Berkeley News](../sources/berkeley-fly-brain-news.md))

## Scope

- **Brain only** — does not include the ventral nerve cord (VNC). VNC connectomes for male and female *Drosophila* are released separately by other groups (Azevedo, Cheong, Marin, Takemura — see [flybody Paper](../sources/flybody-paper.md) refs 55–58).
- **Adult female fly.** Whole-brain reconstruction at synaptic resolution.

## Anchor papers (October 2024, all *Nature*)

- **Dorkenwald et al.** — *"Neuronal wiring diagram of an adult brain"* (the connectome itself). *Nature* 634, 124–138.
- **Schlegel et al.** — *"Whole-brain annotation and multi-connectome cell typing of *Drosophila*"*. *Nature* 634, 139–152.
- **Shiu et al.** — *"A Drosophila computational brain model reveals sensorimotor processing"*. The leaky-integrate-and-fire dynamic model atop the connectome. ([Berkeley News](../sources/berkeley-fly-brain-news.md))

## Consortium leads

- **MRC Laboratory of Molecular Biology** (Cambridge, UK)
- **Princeton University**
- **University of Vermont**
- **University of Cambridge**

## Funders

NIH BRAIN Initiative, Wellcome, Medical Research Council, Princeton, NSF.

## Why it matters here

- **The brain side of whole-organism agentic AI.** Pairs naturally with [flybody](flybody.md) (the body side) — see [Whole-organism agentic AI](../syntheses/whole-organism-agentic-ai.md).
- **Connectome-constrained predictors.** Lappalainen et al. 2024 (*Nature* 634:1132) and Mi et al. 2022 (ICLR) train deep nets whose connectivity is constrained by the FlyWire wiring — predicting fly visual-system neural activity at single-neuron resolution. This is the ML-on-connectome modality flybody-paper points to as the brain-side complement.

## Related

- [Drosophila melanogaster](drosophila.md) — model organism.
- [flybody](flybody.md) — body-side complement.
- [Connectome](../concepts/connectome.md) — concept page.

## Mentioned in

- [Berkeley News — researchers simulate an entire fly brain on a laptop](../sources/berkeley-fly-brain-news.md)
- [flybody Paper](../sources/flybody-paper.md) (cited as future brain-side integration)
