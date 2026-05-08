---
title: VLA-JEPA
type: entity
subtype: model
created: 2026-05-07
updated: 2026-05-07
sources: 1
tags: [vla-jepa, vla-models, jepa, world-model, libero, simplerenv]
---

**VLA-JEPA** — "Enhancing Vision-Language-Action Model with Latent World Model." Augments a [[vla-models|VLA]] policy with a **JEPA-style latent world-model auxiliary objective**. Introduced in [[vla-jepa-paper|Sun et al. (Feb 2026)]] (USTC + collaborators).

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
- Strengthens the case in [[why-jepa-research-skips-the-simulator-stack|the revised synthesis]] that the JEPA literature is **fragmenting across sim weight classes** rather than skipping sim wholesale.

## Related
- [[jepa|Joint-Embedding Predictive Architecture]] — auxiliary objective.
- [[vla-models|VLA models]] — wraps JEPA into a VLA policy.
- [[world-model-simulators|World-model simulators]] — latent-prediction paradigm.

## Mentioned in
- [[vla-jepa-paper|VLA-JEPA Paper]]
