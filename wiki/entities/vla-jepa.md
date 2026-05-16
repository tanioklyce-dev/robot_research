---
title: VLA-JEPA
type: entity
subtype: model
created: 2026-05-07
updated: 2026-05-07
sources: 1
tags: [vla-jepa, vla-models, jepa, world-model, libero, simplerenv]
---

**VLA-JEPA** — "Enhancing Vision-Language-Action Model with Latent World Model." Augments a [VLA](../concepts/learning/vla-models.md) policy with a **JEPA-style latent world-model auxiliary objective**. Introduced in [Sun et al. (Feb 2026)](../sources/vla-jepa-paper.md) (USTC + collaborators).

## Approach
- "Leakage-free state prediction": a target encoder produces latent representations from future frames; the student pathway sees only the current observation.
- Aim: dynamics abstractions "robust to camera motion and irrelevant background changes" (paper abstract).
- JEPA serves as auxiliary representation-learning objective inside a VLA policy, **not as the policy itself**.

## Environments
- **LIBERO** — manipulation benchmark.
- **LIBERO-Plus** — extended LIBERO.
- **SimplerEnv** — Sapien-adjacent mid-weight simulator suite.
- **Real-world manipulation** — platform not named in abstract.

## Why it matters
- **Third design point** in the JEPA-for-robotics taxonomy (alongside the V-JEPA 2 / LeWM / JEPA-WMs lines): JEPA-as-auxiliary-objective inside a VLA, not standalone world model.
- **Mid-weight sim choice (SimplerEnv)** — sits between LeWM-style classic benches and JEPA-WMs' RoboCasa.
- Strengthens the case in [the revised synthesis](../syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md) that the JEPA literature is **fragmenting across sim weight classes** rather than skipping sim wholesale.

## Related
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — auxiliary objective.
- [VLA models](../concepts/learning/vla-models.md) — wraps JEPA into a VLA policy.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — latent-prediction paradigm.

## Mentioned in
- [VLA-JEPA Paper](../sources/vla-jepa-paper.md)
