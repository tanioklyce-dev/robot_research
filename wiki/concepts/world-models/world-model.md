---
title: World model
type: concept
created: 2026-05-07
updated: 2026-07-09
sources: 23
tags: [world-model, model-based-rl, planning, prediction, dreamer, jepa, generative-video, omnimodal, world-action-model]
---

**World model** — a **learned predictive model of environment dynamics**: given the current state (or observation) and an action, predict the next state (or observation). The umbrella term covers a wide range of approaches that all share this functional definition. Used for **planning**, **policy improvement** (model-based RL), **imagination**, and **representation learning**.

> [!note] Distinct from [World-model simulators](world-model-simulators.md)
> This page covers the **broad concept** of a learned dynamics model. The companion concept page [world-model-simulators](world-model-simulators.md) is narrower — it specifically addresses world-models-used-as-simulators (i.e. drop-in replacements for traditional rigid-body simulators in agentic-robotics workflows). Many world models in the broader sense (Dreamer-class model-based RL, MuZero) are not "simulators" by that narrower definition.

## Functional definition
A world model is any function `f` learned from data such that `s_{t+1} = f(s_t, a_t)` — possibly with stochasticity, possibly partial observability, possibly in a latent representation. The state space, action conditioning, and prediction target vary widely:

| Axis | Range |
|---|---|
| **Prediction target** | Pixels (generative video) ↔ latent representation ([JEPA](jepa.md)) ↔ scalar value (Dreamer's `h_t`) |
| **Action conditioning** | None (observation-only video models) ↔ action-as-input (most useful variants) |
| **Stochasticity** | Deterministic ↔ probabilistic ↔ ensemble |
| **Time horizon** | Single-step ↔ multi-step ↔ open-ended rollout |
| **Training signal** | Reward-based (Dreamer) ↔ self-supervised reconstruction ↔ contrastive / latent prediction |
| **Encoder** | Frozen pretrained ([DINOv2](../../entities/dinov2.md) in [DINO-WM](../../entities/dino-wm.md)) ↔ end-to-end ([LeWM](../../entities/leworldmodel.md)) ↔ co-trained with policy |
| **Use** | Planning (MPC, search) ↔ model-based RL training ↔ representation learning |

## Major design points represented in this wiki

- **Generative video world models**: predict pixels. Examples: [NVIDIA Cosmos](../../entities/nvidia-cosmos.md), [Genie Envisioner](../../entities/genie-envisioner.md), and **[DreamDojo](../../sources/dreamdojo-paper.md)** (NVIDIA GEAR, ICML 2026 Spotlight; 14B-param Cosmos-Predict2.5 derivative pretrained on **44,711 hr of egocentric human video** — the largest WM-pretraining corpus to date; Self-Forcing distillation hits 10.81 FPS real-time). Expensive to train and use at planning time, but produce inspectable rollouts. Treated as simulators in the agentic-robotics workflow ([world-model-simulators](world-model-simulators.md) concept).
- **Omnimodal world models / [world-action models](world-action-model.md)**: predict pixels **and** actions in one network. **[Cosmos 3](../../sources/cosmos-3-technical-report.md)** (NVIDIA, June 2026) is the canonical instance — a dual-tower Mixture-of-Transformers (AR reasoner + diffusion generator) jointly modeling language/image/video/audio/action, queryable as a VLM, video generator, forward-dynamics model, inverse-dynamics model, or video-action policy. Still a pixel-predictor (generative-video family), but it folds the world model, the VLM, and the policy into a single model — see the [WAM concept](world-action-model.md).
- **JEPA / latent-prediction**: predict the *representation* of the next state, not pixels. End-to-end examples: [V-JEPA 2](../../entities/v-jepa-2.md), [LeWorldModel](../../entities/leworldmodel.md), [PLDM](../../entities/pldm.md); frozen-feature variants ([DINO-WM](../../entities/dino-wm.md), [JEPA-WMs](../../entities/jepa-wms.md)) are listed below. ~100× cheaper than pixel-prediction; harder to inspect; LeWM reports up to 48× faster planning than foundation-model-based world models.
- **Frozen-foundation-feature world models**: use [DINOv2](../../entities/dinov2.md) (or similar) as a frozen encoder; learn only a predictor on top. Examples: [DINO-WM](../../entities/dino-wm.md), [DINO-world](../../entities/dino-world.md), [JEPA-WMs](../../entities/jepa-wms.md) (likely). Trades off representation quality for training simplicity.
- **Reward-conditioned model-based RL**: predict in a latent space optimized for reward and/or value prediction. Two flavors now filed:
    - **Generative-WM MBRL**: [Dreamer / DreamerV3](../../entities/dreamer.md) ([source](../../sources/dreamer-v3-paper.md)) — pixel/state reconstruction + actor-critic trained "in imagination." Two 2025–26 refinement axes now ingested: **backbone wall-clock** ([S5WM](../../sources/s5wm-paper.md): RSSM→S5, 4× faster, real quadrotors) and **prediction objective** ([EAWM](../../sources/eawm-paper.md): event segmentation instead of raw frames, +10–45%, ICLR 2026 SOTA).
    - **Decoder-free MBRL**: [TD-MPC / TD-MPC2](../../entities/td-mpc.md) ([source](../../sources/td-mpc2-paper.md)) — implicit latent dynamics + local MPC + TD-bootstrapped value. Architecturally adjacent to JEPA.
  Both cited as baselines in [LeWM](../../sources/leworldmodel-paper.md).

## Common training challenges
- **Representation collapse** — without anti-collapse mechanisms, encoder + predictor can learn trivial constants. Solutions vary by family: EMA targets (V-JEPA), stop-gradient, frozen encoders (DINO-WM), regularizers (LeWM's SIGReg).
- **Sim-to-real gap** — pixel-level world models trained on sim or video may not transfer to real-world dynamics (in the action-conditioned case). Latent-prediction sidesteps this *if* the encoder is invariant to surface details.
- **Compounding error** — multi-step rollouts in any world model accumulate error. Most robotics-relevant world models use short horizons (5–20 steps in MPC) or recurrent state structure.
- **Action-conditioning data scarcity** — pretraining can be observation-only at internet scale, but action-conditioned post-training requires action-labeled data ([DROID](../../entities/droid.md)'s 350 hr is the standard).

## Why "world model" matters as agentic-robotics terminology
- **Bridges representation learning and planning.** A good world model is *both* a strong representation and a usable planner — you don't have to pick.
- **Decouples policy from environment.** Train a world model once on broad data; plan against it for any task. The promise of zero-shot capability transfers (e.g. [V-JEPA 2](../../entities/v-jepa-2.md)'s zero-shot Franka).
- **Substitutes for simulators in some pipelines.** If the world model is good enough, you don't need a hand-built simulator — see [world-model-simulators concept](world-model-simulators.md) and [the paradigm comparison](../../syntheses/world-models/generative-video-vs-jepa-world-models.md).

## Common confusions
> [!warning] "World model" ≠ "world foundation model"
> Some sources (notably NVIDIA marketing for Cosmos) use "world foundation model" for very-large pretrained generative video models. That's a *type* of world model, not a synonym. This wiki uses "world model" as the umbrella term and qualifies with paradigm names (generative-video, JEPA, frozen-feature, model-based-RL).

> [!warning] "World model" ≠ "world simulator"
> [AGIBOT marketing](../../sources/agibot-genie-envisioner-2-announcement.md) sometimes uses "world simulator" to describe Genie Envisioner 2.0. By this concept page's vocabulary, that's a generative-video world model being used in a simulator role — see [world-model-simulators](world-model-simulators.md).

## Related
- [World-model simulators](world-model-simulators.md) — narrower companion concept (world-model as drop-in simulator replacement).
- [Joint-Embedding Predictive Architecture](jepa.md) — one design point under this umbrella.
- [World-action model (WAM)](world-action-model.md) — the FD/ID/policy unification (Cosmos 3, Dream*, GE-Sim2).
- [Generative-video vs JEPA world models](../../syntheses/world-models/generative-video-vs-jepa-world-models.md) — synthesis comparing two major design points.
- [Why JEPA research skips the simulator stack](../../syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md) — synthesis on a JEPA-specific question.

## Mentioned in
- [Wake-Sleep Paper (Hinton et al., 1995)](../../sources/wake-sleep-paper.md) — the sleep phase trains on model-generated "fantasies" — the 1995 ancestor of learning-in-imagination, complete with its stated failure mode (fantasy distribution ≠ data distribution)
- [A Path Towards Autonomous Machine Intelligence (LeCun, 2022)](../../sources/lecun2022-path-towards-ami.md) — canonical LeCun position paper; argues for configurable world model + hierarchical JEPA as the substrate
- [V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md)
- [LeWorldModel Paper](../../sources/leworldmodel-paper.md)
- [JEPA-WMs Paper](../../sources/jepa-wms-paper.md)
- [DINO-WM Paper](../../sources/dino-wm-paper.md)
- [DINO-world Paper](../../sources/dino-world-paper.md)
- [VLA-JEPA Paper](../../sources/vla-jepa-paper.md)
- [V-JEPA 2.1 Paper](../../sources/v-jepa-2-1-paper.md)
- [Genie Envisioner Paper](../../sources/genie-envisioner-paper.md)
- [AGIBOT Genie Envisioner 2.0 Announcement](../../sources/agibot-genie-envisioner-2-announcement.md)
- [RoboCasa365 Paper](../../sources/robocasa365-paper.md) (training-foundation-model context)
- [Top 10 Physical AI Models 2026](../../sources/top-10-physical-ai-models-2026.md)
- [DreamerV3 Paper](../../sources/dreamer-v3-paper.md)
- [FLARE Paper](../../sources/flare-paper.md) — implicit (non-reconstructive) latent WM applied as a VLA policy co-training loss; see [FLARE concept](flare.md)
- [TD-MPC Paper](../../sources/td-mpc-paper.md) — TOLD; the reward-centric decoder-free corner of the WM design space (2022)
- [TD-MPC2 Paper](../../sources/td-mpc2-paper.md)
- [PLDM Paper](../../sources/pldm-paper.md)
- [DreamDojo Paper](../../sources/dreamdojo-paper.md)
- [Cosmos 3 Technical Report](../../sources/cosmos-3-technical-report.md)

## Open questions / TBD
- PlaNet / DreamerV1 / V2 / TD-MPC1 — earlier MBRL milestones; would deepen the family lineage but not strictly required (V3 / TD-MPC2 cover the baseline-citation role).
