---
title: World-action model (WAM)
type: concept
created: 2026-06-02
updated: 2026-09-01
sources: 12
tags: [world-action-model, wam, world-model, vla, forward-dynamics, inverse-dynamics, policy, cosmos, dreamzero]
---

**World-action model (WAM)** — a model that jointly couples a **world model** (it predicts how observations evolve) with an **action model** (it predicts or consumes actions), so that the *same* network can do forward dynamics, inverse dynamics, **and** act as a policy. The distinguishing move versus a plain [VLA](../learning/vla-models.md) is that a WAM explicitly models the **visual consequence** of an action, not just the action itself.

> [!note] The same three modes, stated by a vendor as the shape of a robotics foundation model
> Asked whether [World Labs](../../entities/world-labs.md) will build a foundation model for robotics, [Fei-Fei Li](../../entities/fei-fei-li.md) answers with omni-models — *"it's very likely going to involve the output of actions **in addition to the state of the world**, and we're definitely not ruling this out"* — and [Yunzhu Li](../../entities/yunzhu-li.md) gives the FD/policy split verbatim: *"if you think about **actions as inputs**, that is essentially a **forward simulator**… when the **action is output**, this is essentially a **policy**"*, with the omni-model serving as "a backbone for you to fine-tune into specific robotic applications" ([a16z conversation](../../sources/a16z-worldlabs-scenix-conversation.md)). The taxonomy below was crystallized in research papers; this is the same decomposition arriving as a commercial roadmap.

## Definition

The vocabulary crystallized in 2026 around three conditional modes over a video–action token stream (each action `aₜ` is the transition `vₜ₋₁ → vₜ`):

| Mode | Given (clean) | Predicted (denoised) | Equivalent to |
|---|---|---|---|
| **Forward dynamics (FD)** | actions + context frames | future frames | action-conditioned [world model](world-model.md) / simulator |
| **Inverse dynamics (ID)** | observed frames | the actions that explain them | action recognition / labeling |
| **Policy** | goal/instruction + current frame | actions **and** their expected future frames | a [VLA](../learning/vla-models.md) that also imagines the outcome |

A WAM is therefore a superset of both the "video generator as simulator" ([world-model simulators](world-model-simulators.md)) and the "VLA emits actions" framings — it is one model that can be queried in any of the three directions.

## Key references

- **[Cosmos 3](../../sources/cosmos-3-technical-report.md)** (NVIDIA, 2026) — the canonical worked example: a single [MoT](../../sources/cosmos-3-technical-report.md) model does FD / ID / policy across camera, autonomous-vehicle, robot, and egocentric embodiments. Its policy variant (Cosmos3-Nano-Policy-DROID) tops RoboArena, beats π0.5 on RoboLab, and — per the report's **June 2026 revision** — also ranked #1 on **MolmoSpaces** (39.0% oracle success, *All Combined*, 2026-06-20) **submitting the same model and hyperparameters with no benchmark-specific tuning**. Its central empirical claim is that **unified action mid-training** across embodiments and modes produces a *reusable action prior* that accelerates downstream adaptation (LIBERO-10: 24.6% vs 0.0% at 500 iters for mid-trained vs pre-trained init).
- **DreamZero / [DreamDojo](../../sources/dreamdojo-paper.md)** ([NVIDIA GEAR](../../entities/nvidia-gear.md)) — the Dream* line, cited by Cosmos 3 as a WAM baseline; DreamDojo uses continuous latent actions as a self-supervised proxy.
- **[Genie Envisioner](../../entities/genie-envisioner.md) / GE-Sim2** ([AGIBOT](../../entities/agibot.md)) — introduced a "World Action Model" framework where action is a first-class variable ([announcement](../../sources/agibot-genie-envisioner-2-announcement.md)).

## The compact end of the scale

Every WAM named above is a frontier-scale system — Cosmos 3, the Dream* line, GE-Sim2, and the 5B DriveWAM the AV paper cites as concurrent work. [Sharifullin et al.](../../sources/dit-world-action-model-av-paper.md) occupy the opposite end deliberately: **~5.4M parameters**, a single front camera, 2 Hz, 8-second horizon on [nuScenes](../../entities/nuscenes.md). Their argument for the regime is methodological — *"controlled ablations that isolate individual design factors are tractable at this scale but prohibitively expensive at 5B."*

What that buys, and it is worth having:

- **A necessary-ingredients list for a latent DiT**, arrived at by rejecting hypotheses rather than by ablation sweep: spatial tokens, the *x*₀ objective (ε-prediction *collapses* in compact latents; switching recovers 88.5% of the gap), residual anchoring, and sampling matched to target uncertainty.
- **Controllability measured rather than asserted.** Sweeping steering with fixed noise gives Spearman ρ = **+0.81** for the diffusion model against **−0.18** for a matched regressor, plus a non-circular inverse-control probe. This is the property that separates a *world-action* model from a video model with an action input port, and most WAM papers show it qualitatively at best.
- **A structural diagnosis with a counter-intuitive fix.** Predicting every future token as a residual from the *same* present latent biases the model toward re-rendering the current scene; the model produces texture (0.98× GT) but almost no coherent motion (0.44× GT). Re-parameterizing as a Δt=4 jump with per-step re-anchoring recovers **full motion magnitude (1.02× GT) in a 3× smaller model** — the fix was architectural, not capacity.

> [!note] Read it for the diagnoses, not the artifact
> At FID 162.5 this is nowhere near a usable driving world model, and the provenance is a likely course project. The four ingredients are claimed to transfer upward on the strength of a **2-point, 1-seed** capacity probe. Treat the recipe as a hypothesis about larger systems, not a validated one.

## Related concepts

- [World model](world-model.md) — the FD direction is exactly an action-conditioned world model.
- [VLA models](../learning/vla-models.md) — the policy direction; a WAM is a VLA that also models consequences. LeCun's "VLA are doomed (no planning)" critique is partly what a WAM's consequence-modeling answers from inside the generative-video camp.
- [World-model simulators](world-model-simulators.md) — FD-as-simulator.
- [Joint-Embedding Predictive Architecture](jepa.md) — the *latent-prediction* alternative; JEPA + a planner is the JEPA-side analogue of a WAM, but predicts embeddings rather than pixels/actions jointly.

## Current state

As of mid-2026 the strongest published WAMs are generative-video / diffusion models (Cosmos 3, the Dream* line, GE-Sim2) — i.e. they live on the **pixel-prediction** side of the [generative-video vs JEPA](../../syntheses/world-models/generative-video-vs-jepa-world-models.md) split. Cosmos 3 is the first to show a WAM's policy mode reaching SOTA across **three** benchmarks — a sim benchmark (RoboLab), a real-world crowdsourced one (RoboArena), and a controlled-variation generalization suite ([MolmoSpaces](../../sources/cosmos-3-technical-report.md#molmospaces--the-third-benchmark-added-in-the-june-revision), added in the report's June revision) — the last **without benchmark-specific tuning**. That no-retuning detail is the clearest evidence that the FD+ID+policy unification pays off rather than just adding cost, since it is the cross-benchmark transfer the thesis actually predicts. Whether jointly modeling the visual consequence improves *deployment* robustness over a pure action head, at fixed compute, is not yet isolated.

## Mentioned in
- [History-Guided Video Diffusion (DFoT)](../../sources/history-guided-video-diffusion-paper.md) — sampling-time score composition (History Guidance) as a control knob for action-conditioned video models; physical-robot IL result (83%) composing memory + reactivity behaviors never co-present in training data.
- [Cosmos 3 Technical Report](../../sources/cosmos-3-technical-report.md)
- [Develop Physical AI with NVIDIA Cosmos 3 (HF blog)](../../sources/nvidia-cosmos-3-hf-blog.md)
- [AGIBOT Genie Envisioner 2.0 Announcement](../../sources/agibot-genie-envisioner-2-announcement.md)
- [Sharifullin, Jiang & Chew 2026 — Diffusion Transformer World-Action Model for AV Scene Prediction](../../sources/dit-world-action-model-av-paper.md) — the compact-scale end; controllability measured (ρ = 0.81 vs −0.18); the shared-anchor motion diagnosis.
