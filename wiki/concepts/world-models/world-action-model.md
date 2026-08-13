---
title: World-action model (WAM)
type: concept
created: 2026-06-02
updated: 2026-07-08
sources: 7
tags: [world-action-model, wam, world-model, vla, forward-dynamics, inverse-dynamics, policy, cosmos, dreamzero]
---

**World-action model (WAM)** — a model that jointly couples a **world model** (it predicts how observations evolve) with an **action model** (it predicts or consumes actions), so that the *same* network can do forward dynamics, inverse dynamics, **and** act as a policy. The distinguishing move versus a plain [VLA](../learning/vla-models.md) is that a WAM explicitly models the **visual consequence** of an action, not just the action itself.

## Definition

The vocabulary crystallized in 2026 around three conditional modes over a video–action token stream (each action `aₜ` is the transition `vₜ₋₁ → vₜ`):

| Mode | Given (clean) | Predicted (denoised) | Equivalent to |
|---|---|---|---|
| **Forward dynamics (FD)** | actions + context frames | future frames | action-conditioned [world model](world-model.md) / simulator |
| **Inverse dynamics (ID)** | observed frames | the actions that explain them | action recognition / labeling |
| **Policy** | goal/instruction + current frame | actions **and** their expected future frames | a [VLA](../learning/vla-models.md) that also imagines the outcome |

A WAM is therefore a superset of both the "video generator as simulator" ([world-model simulators](world-model-simulators.md)) and the "VLA emits actions" framings — it is one model that can be queried in any of the three directions.

## Key references

- **[Cosmos 3](../../sources/cosmos-3-technical-report.md)** (NVIDIA, 2026) — the canonical worked example: a single [MoT](../../sources/cosmos-3-technical-report.md) model does FD / ID / policy across camera, autonomous-vehicle, robot, and egocentric embodiments. Its policy variant (Cosmos3-Nano-Policy-DROID) tops RoboArena and beats π0.5 on RoboLab. Its central empirical claim is that **unified action mid-training** across embodiments and modes produces a *reusable action prior* that accelerates downstream adaptation (LIBERO-10: 24.6% vs 0.0% at 500 iters for mid-trained vs pre-trained init).
- **DreamZero / [DreamDojo](../../sources/dreamdojo-paper.md)** ([NVIDIA GEAR](../../entities/nvidia-gear.md)) — the Dream* line, cited by Cosmos 3 as a WAM baseline; DreamDojo uses continuous latent actions as a self-supervised proxy.
- **[Genie Envisioner](../../entities/genie-envisioner.md) / GE-Sim2** ([AGIBOT](../../entities/agibot.md)) — introduced a "World Action Model" framework where action is a first-class variable ([announcement](../../sources/agibot-genie-envisioner-2-announcement.md)).

## Related concepts

- [World model](world-model.md) — the FD direction is exactly an action-conditioned world model.
- [VLA models](../learning/vla-models.md) — the policy direction; a WAM is a VLA that also models consequences. LeCun's "VLA are doomed (no planning)" critique is partly what a WAM's consequence-modeling answers from inside the generative-video camp.
- [World-model simulators](world-model-simulators.md) — FD-as-simulator.
- [Joint-Embedding Predictive Architecture](jepa.md) — the *latent-prediction* alternative; JEPA + a planner is the JEPA-side analogue of a WAM, but predicts embeddings rather than pixels/actions jointly.

## Current state

As of mid-2026 the strongest published WAMs are generative-video / diffusion models (Cosmos 3, the Dream* line, GE-Sim2) — i.e. they live on the **pixel-prediction** side of the [generative-video vs JEPA](../../syntheses/world-models/generative-video-vs-jepa-world-models.md) split. Cosmos 3 is the first to show a WAM's policy mode reaching SOTA on both a sim benchmark (RoboLab) and a real-world crowdsourced benchmark (RoboArena), which is the clearest evidence that the FD+ID+policy unification pays off rather than just adding cost. Whether jointly modeling the visual consequence improves *deployment* robustness over a pure action head, at fixed compute, is not yet isolated.

## Mentioned in
- [History-Guided Video Diffusion (DFoT)](../../sources/history-guided-video-diffusion-paper.md) — sampling-time score composition (History Guidance) as a control knob for action-conditioned video models; physical-robot IL result (83%) composing memory + reactivity behaviors never co-present in training data.
- [Cosmos 3 Technical Report](../../sources/cosmos-3-technical-report.md)
- [Develop Physical AI with NVIDIA Cosmos 3 (HF blog)](../../sources/nvidia-cosmos-3-hf-blog.md)
- [AGIBOT Genie Envisioner 2.0 Announcement](../../sources/agibot-genie-envisioner-2-announcement.md)
