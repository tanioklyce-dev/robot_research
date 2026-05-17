---
title: Yann LeCun
type: entity
subtype: person
created: 2026-05-07
updated: 2026-05-17
sources: 19
tags: [person, meta-fair, nyu, jepa, world-model, turing-award, ami-labs, logical-intelligence, ebm]
---

> [!note] Reported organizational changes
> Two post-Meta affiliations are recorded in this wiki, with different evidentiary weight:
> - **[AMI Labs](ami-labs.md)** (founder, reported) — single secondary source ([Towards AI, April 2026](../sources/towardsai-lecun-ami-labs.md)); provisional.
> - **[Logical Intelligence](logical-intelligence.md)** (Founding Chair of Technical Research Board, announced 2026-01-21) — surfaced via [the Aleph EBM video source](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md) drawing on the BusinessWire press release. The Logical Intelligence/yann-lecun bio page additionally lists him as "Executive Chairman of AMI Labs."
>
> These appear to be two separate companies, both downstream of LeCun's EBM-and-world-models agenda. Whether they collaborate, are parallel, or one is a subsidiary of the other is not addressed by any source in this wiki.

**Yann LeCun** — Silver Professor at NYU; Turing Award (2018, with Bengio + Hinton). Formerly VP & Chief AI Scientist at [Meta FAIR](meta-fair.md). Per secondary reporting (April 2026), now founder of [AMI Labs](ami-labs.md). As of **2026-01-21**, also Founding Chair of the Technical Research Board at **[Logical Intelligence](logical-intelligence.md)**. In this wiki, **the architect of the [JEPA](../concepts/world-models/jepa.md) research program** and the senior author or co-author across nearly every Meta-affiliated world-model paper ingested.

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
- **Latent-prediction over generative-video.** LeCun has argued publicly (talks, blog posts, social media) that pixel-level generative models are the wrong target for video world modeling — that prediction in representation space is more efficient and more aligned with what biological systems do. JEPA is the technical instantiation of that argument. The on-camera framing of this position is the **[Welch Labs explainer "Yann LeCun's $1B Bet Against LLMs" (2026-05-01)](../sources/welchlabs-lecun-1b-bet-against-llms.md)**, which interviews LeCun and traces the blurry-pixels → Siamese → Barlow Twins → DINO → JEPA arc.
- **Canonical position paper.** **["A Path Towards Autonomous Machine Intelligence" (2022-06-27, v0.9.2)](../sources/lecun2022-path-towards-ami.md)** is LeCun's full architectural vision document: a six-module differentiable agent (perception, world model, actor, cost, short-term memory, configurator), JEPA / H-JEPA as the world-model substrate, intrinsic-cost + learned-critic as the reward replacement, and the long-form argument against contrastive SSL and generative video. **Every JEPA paper in this wiki instantiates a piece of this blueprint.** It is also the source of LeCun's repeated public claim that "LLMs are insufficient for common sense."
- **Self-supervised learning at internet-scale.** The V-JEPA 2 framing — internet-scale video pretraining + small action-conditioning — is consistent with LeCun's broader "energy-based models / observation-only learning" agenda predating JEPA. The same Welch Labs video opens with his "intelligence is a cake" metaphor (SSL = cake, supervised = icing, RL = cherry).

## Position in the broader field
LeCun is one of the small number of researchers whose **simultaneous senior position at a major lab + university appointment + Turing-award credibility** lets him drive a multi-year research program at scale. The JEPA program is the visible artifact of that.

## Related
- [Meta FAIR](meta-fair.md) — prior primary affiliation.
- [AMI Labs](ami-labs.md) — reported new lab (provisional).
- [Logical Intelligence](logical-intelligence.md) — Founding Chair of Technical Research Board (2026-01-21); commercializes EBMs for reasoning. Distinct from AMI Labs.
- [Energy-based models](../concepts/learning/energy-based-models.md) — the long-running thread that underlies both JEPA and the new Kona work.
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — research program LeCun architected.
- [Adrien Bardes](adrien-bardes.md) — frequent JEPA co-senior.
- [Basile Terver](basile-terver.md) — JEPA-WMs lead author working under LeCun.

## Earlier work (AT&T Bell Labs era)
- **[Bromley, Guyon, LeCun, Säckinger, Shah 1993 — "Signature Verification using a 'Siamese' Time Delay Neural Network"](../sources/bromley1993-siamese-signature-verification.md)** — co-author (third position). The **original [Siamese network](../concepts/world-models/siamese-network.md) paper**, written during LeCun's AT&T Bell Labs Holmdel period. Architecturally continuous with the 2020s JEPA program: two weight-tied encoders + a similarity head is the J/A in JEPA, 30 years before LeCun named the framework. The Welch Labs explainer's framing of JEPA as "the natural continuation of the Siamese-network research LeCun started in the 1990s" is literally correct — same author, same architectural family, different loss.

## Mentioned in
- [Bromley et al. 1993 — Signature Verification using a Siamese TDNN](../sources/bromley1993-siamese-signature-verification.md) — co-author; original Siamese network paper.
- [Barlow Twins Paper (Zbontar et al., ICML 2021)](../sources/barlow-twins-paper.md) — senior author; first non-asymmetric anti-collapse SSL method.
- [VICReg Paper (Bardes, Ponce, LeCun, ICLR 2022)](../sources/vicreg-paper.md) — senior author; the regularizer LeCun later endorses in his AMI paper as JEPA's anti-collapse method.
- [A Path Towards Autonomous Machine Intelligence (LeCun, 2022)](../sources/lecun2022-path-towards-ami.md)
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
- [V-JEPA 2.1 Paper](../sources/v-jepa-2-1-paper.md)
- [LeWorldModel Paper](../sources/leworldmodel-paper.md)
- [DINO-WM Paper](../sources/dino-wm-paper.md)
- [DINO-world Paper](../sources/dino-world-paper.md)
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)
- [LeJEPA Paper](../sources/lejepa-paper.md)
- [Towards AI — LeCun / AMI Labs article](../sources/towardsai-lecun-ami-labs.md)
- [Welch Labs — Yann LeCun's $1B Bet Against LLMs (video)](../sources/welchlabs-lecun-1b-bet-against-llms.md)
- [Aleph and Energy-Based Models: The AI That Refuses to Bullshit (video)](../sources/2026-05-aleph-ebm-refuses-bullshit-video.md) — names LeCun as Founding Chair of Logical Intelligence's Technical Research Board; verbatim quote on EBMs as "reasoning and inference by minimizing an energy function."

## Open questions / TBD
- Has anyone built a working **Hierarchical JEPA (H-JEPA)** at the multi-time-scale envisioned in the [2022 position paper](../sources/lecun2022-path-towards-ami.md)? No JEPA paper in this wiki clearly does this — V-JEPA 2.1's "dense features" and JEPA-WMs' action-conditioned setup move in that direction but don't fully realize it.
- Has the **configurator** module (Section 6 of the 2022 paper) ever been concretely instantiated? LeCun left it as a sketch; worth checking AMI Labs / later FAIR output.
