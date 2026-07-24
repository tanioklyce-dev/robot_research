---
title: World-model simulators
type: concept
created: 2026-05-06
updated: 2026-07-09
sources: 24
tags: [world-model, generative-simulation, video-generation, jepa, latent-prediction, paradigm-shift]
---

**World-model simulators** use learned models — not authored physics engines — as the environment for training, evaluating, or planning robot policies. Two paradigms have emerged.

## Paradigm A: Generative-video world models
Generate the next frame's *pixels*. Train and plan inside a learned video generator.

| | Physics simulator | Generative-video world model |
|---|---|---|
| Environment | Hand-authored geometry, equations of motion | Learned from video |
| Output | Next state via simulation | Next frame via generation |
| Compute bound | Physics solver | Video model inference |

Notable systems:
- **[NVIDIA Cosmos](../../entities/nvidia-cosmos.md)** — world foundation model (Cosmos-Predict2-2B-Video2World powers downstream simulators). **[Cosmos 3](../../sources/cosmos-3-technical-report.md)** (June 2026) goes further: one omnimodal Mixture-of-Transformers model is *itself* a forward-dynamics simulator, an inverse-dynamics model, **and** a policy — a [world-action model](world-action-model.md) rather than a simulator you train a separate policy inside.
- **[Genie Envisioner](../../entities/genie-envisioner.md)** / GE-Sim2 — built on Cosmos-Predict2; introduces the World Action Model framework where action is a first-class variable; minute-scale stable rollouts ([AGIBOT Genie Envisioner 2.0 Announcement](../../sources/agibot-genie-envisioner-2-announcement.md)).
- **[Genesis](../../entities/genesis.md)** — adjacent: physics-based but uses a [VLM](../learning/vla-models.md) agent to *generate* the simulation content from text.

## Paradigm B: JEPA / latent-prediction world models
Predict the next-state *representation* in a learned latent space — no pixels generated. See [Joint-Embedding Predictive Architecture](jepa.md) for the architectural definition. Pioneered in Yann LeCun's group at FAIR / NYU / Mila.

| | Generative-video | JEPA / latent-prediction |
|---|---|---|
| What's predicted | Next-frame pixels | Next-state embedding |
| Training cost | Massive (per-frame generation) | Lower (no decoder) |
| Planning cost | High (video rollout) | Far lower; LeWM reports 48× faster planning |
| Pretraining at scale | Possible but costly | Web-video-scale pretraining is tractable |

Notable systems:
- **[V-JEPA 2 / V-JEPA 2-AC](../../entities/v-jepa-2.md)** ([Meta FAIR](../../entities/meta-fair.md) + [Mila](../../entities/mila.md)) — 1B-param ViT-g pretrained on 1M+ hours of internet video; 300M-param action-conditioned predictor post-trained on 62 hr of Droid robot data; **zero-shot Franka manipulation in new labs** ([V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md)).
- **[LeWorldModel](../../entities/leworldmodel.md)** ([Mila](../../entities/mila.md) + NYU + Samsung SAIL + Brown) — first stable end-to-end JEPA from raw pixels with just two loss terms; 15M params; single-GPU training; 48× faster planning ([LeWorldModel Paper](../../sources/leworldmodel-paper.md)).

## Where world-model simulators are most useful (2026)
- **Pretraining policies on observed-data distributions** before any physics-based fine-tuning.
- **Generating long-horizon scenarios** for evaluation that would be expensive to author.
- **Domains where the visual or representational distribution matters more than precise physics** (high-level reasoning, manipulation strategy).

## Limits
- Not yet a substitute for physics engines on contact-rich, dynamics-critical tasks (true for both paradigms).
- Real-world adoption signals are early.
- Failure modes:
  - **Generative video** — hallucination, drift over long rollouts.
  - **JEPA** — latent collapse during training, predictor overfitting on small interaction sets.

## Related
- [VLA models](../learning/vla-models.md) — the policies that train inside or alongside world-model environments.
- [Sim-to-real transfer](../learning/sim-to-real-transfer.md) — relevance shifts: latent-prediction reduces the visual-axis gap but introduces a "model fidelity gap" instead.
- [Joint-Embedding Predictive Architecture](jepa.md) — paradigm B's underlying architecture family.

## Mentioned in
- [DreamGen Paper](../../sources/dreamgen-paper.md) — video WM used as a **synthetic data generator** ("neural trajectories") rather than a real-time planner; the data-generation face of this concept.
- [History-Guided Video Diffusion (DFoT)](../../sources/history-guided-video-diffusion-paper.md) — the rollout-stability datapoint: history-guided sampling stabilizes autoregressive extension to **862 frames from one image** (~54× training clip length), and existing VDMs can be fine-tuned into it at ~12.5% cost — long-horizon stability being the gating requirement for video-as-simulator.
- [DIAMOND paper](../../sources/diamond-paper.md) — early playable instance: a diffusion WM trained on 87 h of CS:GO becomes an **interactive neural game engine** (Dust II), the research-scale ancestor of the Genie/Cosmos playable-world wave.
- [AGIBOT Genie Envisioner 2.0 Announcement](../../sources/agibot-genie-envisioner-2-announcement.md)
- [Genie Envisioner Paper](../../sources/genie-envisioner-paper.md)
- [V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md)
- [LeWorldModel Paper](../../sources/leworldmodel-paper.md)
- [Cosmos 3 Technical Report](../../sources/cosmos-3-technical-report.md)
