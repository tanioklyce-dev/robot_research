---
title: Yann LeCun
type: entity
subtype: person
created: 2026-05-07
updated: 2026-05-09
sources: 7
tags: [person, meta-fair, nyu, jepa, world-model, turing-award, ami-labs]
---

> [!note] Reported organizational change (single secondary source)
> A Towards AI blog post (April 2026) reports LeCun departed Meta ~November/December 2025 to found [AMI Labs](ami-labs.md) with a $1.03B seed round. This has not been confirmed by a primary source in this wiki. The affiliation below reflects this uncertainty.

**Yann LeCun** — Silver Professor at NYU; Turing Award (2018, with Bengio + Hinton). Formerly VP & Chief AI Scientist at [Meta FAIR](meta-fair.md). Per secondary reporting (April 2026), now founder of [AMI Labs](ami-labs.md). In this wiki, **the architect of the [JEPA](../concepts/jepa.md) research program** and the senior author or co-author across nearly every Meta-affiliated world-model paper ingested.

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
- [Meta FAIR](meta-fair.md) — prior primary affiliation.
- [AMI Labs](ami-labs.md) — reported new lab (provisional).
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
- [Towards AI — LeCun / AMI Labs article](../sources/towardsai-lecun-ami-labs.md)

## Open questions / TBD
- LeCun's stated position papers ("A Path Towards Autonomous Machine Intelligence," 2022) are not yet source pages — they would anchor the "why latent prediction" rationale that current JEPA papers state only obliquely.
