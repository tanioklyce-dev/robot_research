---
title: Yann LeCun
type: entity
subtype: person
created: 2026-05-07
updated: 2026-05-07
sources: 6
tags: [person, meta-fair, nyu, jepa, world-model, turing-award]
---

**Yann LeCun** — VP & Chief AI Scientist at [Meta](meta-fair.md) and Silver Professor at NYU. Turing Award (2018, with Bengio + Hinton) for foundational contributions to deep learning, particularly convolutional neural networks. In this wiki, **the architect of the [JEPA](../concepts/jepa.md) research program** and the senior author or co-author across nearly every Meta-affiliated world-model paper ingested.

## Role in the JEPA program
LeCun introduced the JEPA framing publicly around 2022 and has driven its application to vision and robotics through the FAIR / Mila pipeline. He is **senior author** on every FAIR-affiliated JEPA / JEPA-adjacent paper this wiki has ingested:

- [V-JEPA 2](../sources/v-jepa-2-paper.md) (2025-06) — co-senior with Rabbat / Ballas / Bardes.
- [V-JEPA 2.1](../sources/v-jepa-2-1-paper.md) (2026-03) — same.
- [LeWorldModel](../sources/leworldmodel-paper.md) (2026-03) — senior author (with Mila / NYU / Samsung / Brown collaborators).
- [DINO-WM](../sources/dino-wm-paper.md) (2024-11) — co-senior with Lerrel Pinto (NYU).
- [DINO-world](../sources/dino-world-paper.md) (2025-07) — listed in author group.
- [JEPA-WMs](../sources/jepa-wms-paper.md) (2025-12) — co-senior with Bardes.

Six papers in this wiki carry his name. The world-model paradigm that distinguishes [FAIR](meta-fair.md) from [NVIDIA](nvidia.md) (generative video) and [AGIBOT](agibot.md) (sim-native) is, for practical purposes, LeCun's research direction.

## Public stance relevant to this wiki
- **Latent-prediction over generative-video.** LeCun has argued publicly (talks, blog posts, social media) that pixel-level generative models are the wrong target for video world modeling — that prediction in representation space is more efficient and more aligned with what biological systems do. JEPA is the technical instantiation of that argument.
- **Self-supervised learning at internet-scale.** The V-JEPA 2 framing — internet-scale video pretraining + small action-conditioning — is consistent with LeCun's broader "energy-based models / observation-only learning" agenda predating JEPA.

## Position in the broader field
LeCun is one of the small number of researchers whose **simultaneous senior position at a major lab + university appointment + Turing-award credibility** lets him drive a multi-year research program at scale. The JEPA program is the visible artifact of that.

## Related
- [Meta FAIR](meta-fair.md) — primary affiliation.
- [Joint-Embedding Predictive Architecture](../concepts/jepa.md) — research program LeCun architected.
- [Adrien Bardes](adrien-bardes.md) — frequent JEPA co-senior.
- [Basile Terver](basile-terver.md) — JEPA-WMs lead author working under LeCun.

## Mentioned in
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
- [V-JEPA 2.1 Paper](../sources/v-jepa-2-1-paper.md)
- [LeWorldModel Paper](../sources/leworldmodel-paper.md)
- [DINO-WM Paper](../sources/dino-wm-paper.md)
- [DINO-world Paper](../sources/dino-world-paper.md)
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)

## Open questions / TBD
- LeCun's stated position papers ("A Path Towards Autonomous Machine Intelligence," 2022) are not yet source pages — they would anchor the "why latent prediction" rationale that current JEPA papers state only obliquely.
