---
title: World model
type: concept
created: 2026-05-07
updated: 2026-05-07
sources: 11
tags: [world-model, model-based-rl, planning, prediction, dreamer, jepa, generative-video]
---

**World model** — a **learned predictive model of environment dynamics**: given the current state (or observation) and an action, predict the next state (or observation). The umbrella term covers a wide range of approaches that all share this functional definition. Used for **planning**, **policy improvement** (model-based RL), **imagination**, and **representation learning**.

> [!note] Distinct from [[world-model-simulators|World-model simulators]]
> This page covers the **broad concept** of a learned dynamics model. The companion concept page [[world-model-simulators|world-model-simulators]] is narrower — it specifically addresses world-models-used-as-simulators (i.e. drop-in replacements for traditional rigid-body simulators in agentic-robotics workflows). Many world models in the broader sense (Dreamer-class model-based RL, MuZero) are not "simulators" by that narrower definition.

## Functional definition
A world model is any function `f` learned from data such that `s_{t+1} = f(s_t, a_t)` — possibly with stochasticity, possibly partial observability, possibly in a latent representation. The state space, action conditioning, and prediction target vary widely:

| Axis | Range |
|---|---|
| **Prediction target** | Pixels (generative video) ↔ latent representation ([[jepa\|JEPA]]) ↔ scalar value (Dreamer's `h_t`) |
| **Action conditioning** | None (observation-only video models) ↔ action-as-input (most useful variants) |
| **Stochasticity** | Deterministic ↔ probabilistic ↔ ensemble |
| **Time horizon** | Single-step ↔ multi-step ↔ open-ended rollout |
| **Training signal** | Reward-based (Dreamer) ↔ self-supervised reconstruction ↔ contrastive / latent prediction |
| **Encoder** | Frozen pretrained ([[dinov2\|DINOv2]] in [[dino-wm\|DINO-WM]]) ↔ end-to-end ([[leworldmodel\|LeWM]]) ↔ co-trained with policy |
| **Use** | Planning (MPC, search) ↔ model-based RL training ↔ representation learning |

## Major design points represented in this wiki

- **Generative video world models**: predict pixels. Examples: [[nvidia-cosmos|NVIDIA Cosmos]], [[genie-envisioner|Genie Envisioner]]. Expensive to train and use at planning time, but produce inspectable rollouts. Treated as simulators in the agentic-robotics workflow ([[world-model-simulators|world-model-simulators]] concept).
- **JEPA / latent-prediction**: predict the *representation* of the next state, not pixels. Examples: [[v-jepa-2|V-JEPA 2]], [[leworldmodel|LeWorldModel]], [[jepa-wms|JEPA-WMs]]. ~100× cheaper than pixel-prediction; harder to inspect; LeWM reports up to 48× faster planning than foundation-model-based world models.
- **Frozen-foundation-feature world models**: use [[dinov2|DINOv2]] (or similar) as a frozen encoder; learn only a predictor on top. Examples: [[dino-wm|DINO-WM]], [[dino-world|DINO-world]], [[jepa-wms|JEPA-WMs]] (likely). Trades off representation quality for training simplicity.
- **Reward-conditioned model-based RL**: predict in a latent space optimized for reward prediction. Examples: Dreamer / DreamerV3, TD-MPC. Not yet ingested as standalone source pages but referenced as baselines in [[leworldmodel-paper|LeWM]].

## Common training challenges
- **Representation collapse** — without anti-collapse mechanisms, encoder + predictor can learn trivial constants. Solutions vary by family: EMA targets (V-JEPA), stop-gradient, frozen encoders (DINO-WM), regularizers (LeWM's SIGReg).
- **Sim-to-real gap** — pixel-level world models trained on sim or video may not transfer to real-world dynamics (in the action-conditioned case). Latent-prediction sidesteps this *if* the encoder is invariant to surface details.
- **Compounding error** — multi-step rollouts in any world model accumulate error. Most robotics-relevant world models use short horizons (5–20 steps in MPC) or recurrent state structure.
- **Action-conditioning data scarcity** — pretraining can be observation-only at internet scale, but action-conditioned post-training requires action-labeled data ([[droid|DROID]]'s 350 hr is the standard).

## Why "world model" matters as agentic-robotics terminology
- **Bridges representation learning and planning.** A good world model is *both* a strong representation and a usable planner — you don't have to pick.
- **Decouples policy from environment.** Train a world model once on broad data; plan against it for any task. The promise of zero-shot capability transfers (e.g. [[v-jepa-2|V-JEPA 2]]'s zero-shot Franka).
- **Substitutes for simulators in some pipelines.** If the world model is good enough, you don't need a hand-built simulator — see [[world-model-simulators|world-model-simulators concept]] and [[generative-video-vs-jepa-world-models|the paradigm comparison]].

## Common confusions
> [!warning] "World model" ≠ "world foundation model"
> Some sources (notably NVIDIA marketing for Cosmos) use "world foundation model" for very-large pretrained generative video models. That's a *type* of world model, not a synonym. This wiki uses "world model" as the umbrella term and qualifies with paradigm names (generative-video, JEPA, frozen-feature, model-based-RL).

> [!warning] "World model" ≠ "world simulator"
> [[agibot-genie-envisioner-2-announcement|AGIBOT marketing]] sometimes uses "world simulator" to describe Genie Envisioner 2.0. By this concept page's vocabulary, that's a generative-video world model being used in a simulator role — see [[world-model-simulators|world-model-simulators]].

## Related
- [[world-model-simulators|World-model simulators]] — narrower companion concept (world-model as drop-in simulator replacement).
- [[jepa|Joint-Embedding Predictive Architecture]] — one design point under this umbrella.
- [[generative-video-vs-jepa-world-models|Generative-video vs JEPA world models]] — synthesis comparing two major design points.
- [[why-jepa-research-skips-the-simulator-stack|Why JEPA research skips the simulator stack]] — synthesis on a JEPA-specific question.

## Mentioned in
- [[v-jepa-2-paper|V-JEPA 2 Paper]]
- [[leworldmodel-paper|LeWorldModel Paper]]
- [[jepa-wms-paper|JEPA-WMs Paper]]
- [[dino-wm-paper|DINO-WM Paper]]
- [[dino-world-paper|DINO-world Paper]]
- [[vla-jepa-paper|VLA-JEPA Paper]]
- [[v-jepa-2-1-paper|V-JEPA 2.1 Paper]]
- [[genie-envisioner-paper|Genie Envisioner Paper]]
- [[agibot-genie-envisioner-2-announcement|AGIBOT Genie Envisioner 2.0 Announcement]]
- [[robocasa365-paper|RoboCasa365 Paper]] (training-foundation-model context)
- [[top-10-physical-ai-models-2026|Top 10 Physical AI Models 2026]]

## Open questions / TBD
- Dreamer / DreamerV3 / TD-MPC source pages — would close the model-based-RL family of this concept.
- LeCun's "A Path Towards Autonomous Machine Intelligence" (2022) — the original JEPA position paper, would anchor the LeCun stance behind half of this concept's content.
