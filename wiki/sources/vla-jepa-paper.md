---
title: VLA-JEPA Paper
type: source
url: https://arxiv.org/abs/2602.10098
local_path: null
author: Jingwen Sun, Wenyao Zhang, Zekun Qi, Shaojie Ren, Zezhi Liu, Hanxin Zhu, Guangzhong Sun, Xin Jin, Zhibo Chen
affiliations: USTC (inferred from author roster) + collaborators
published: 2026-02-10
revised: 2026-02-14
ingested: 2026-05-07
tags: [vla-jepa, jepa, vla-models, libero, simplerenv, world-model]
---

## Summary
**VLA-JEPA — "Enhancing Vision-Language-Action Model with Latent World Model."** Augments a [VLA](../concepts/vla-models.md) policy with a JEPA-style latent world-model objective: "leakage-free state prediction" where a target encoder produces latent representations from future frames while the student pathway sees only the current observation. Trains/evaluates on **LIBERO, LIBERO-Plus, SimplerEnv**, plus real-world manipulation. **First JEPA paper in this wiki to use mid-weight sim (SimplerEnv)** — sits between LeWM-style lightweight benches and Terver et al.'s RoboCasa.

## Key claims
- "Leakage-free state prediction": target encoder produces latent representations from future frames; student sees only current observation.
- Learned dynamics abstractions are "robust to camera motion and irrelevant background changes" (abstract).
- Evaluated on **LIBERO**, **LIBERO-Plus**, **SimplerEnv**, and **real-world manipulation**.
- DOI: https://doi.org/10.48550/arXiv.2602.10098

## Entities mentioned
- [VLA-JEPA](../entities/vla-jepa.md) — model (entity created with this ingest).
- (LIBERO and SimplerEnv are referenced but do not yet have entity pages — added to known-gaps.)

## Concepts touched
- [Joint-Embedding Predictive Architecture](../concepts/jepa.md) — JEPA-as-auxiliary-objective in a VLA pipeline.
- [VLA models](../concepts/vla-models.md) — policy class.
- [World model](../concepts/world-model.md) — JEPA-as-auxiliary design point.
- [World-model simulators](../concepts/world-model-simulators.md) — latent-prediction paradigm.

## Open questions
- Code/project URL not surfaced from the abstract page.
- Author affiliations not on the abstract page — USTC (Chen, Sun) is the inferred primary, but full institutional list needs the paper body.
- Real-world manipulation platform not named in abstract.
- LIBERO and SimplerEnv would benefit from their own entity pages — both are referenced now in multiple sources.

## Why this matters
VLA-JEPA is a **third design point** in the JEPA-for-robotics taxonomy:
- [V-JEPA 2](../entities/v-jepa-2.md) — internet video pretraining → small action-conditioning → real eval.
- [LeWorldModel](../entities/leworldmodel.md) / [DINO-WM](../entities/dino-wm.md) — lightweight benches, end-to-end or DINOv2-feature-based.
- [JEPA-WMs (Terver et al.)](jepa-wms-paper.md) — RoboCasa + Metaworld + real Franka.
- **VLA-JEPA — JEPA-as-auxiliary-objective inside a VLA policy, evaluated on LIBERO + SimplerEnv + real.**

The simulator-environments-of-choice are now **fragmenting across the JEPA literature**, not consolidating. This makes the simple "JEPA skips heavy sim" pattern from the [original synthesis](../syntheses/why-jepa-research-skips-the-simulator-stack.md) hard to defend.
