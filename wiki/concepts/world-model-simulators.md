---
title: World-model simulators
type: concept
created: 2026-05-06
updated: 2026-05-07
sources: 4
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
- **[[nvidia-cosmos|NVIDIA Cosmos]]** — world foundation model (Cosmos-Predict2-2B-Video2World powers downstream simulators).
- **[[genie-envisioner|Genie Envisioner]]** / GE-Sim2 — built on Cosmos-Predict2; introduces the World Action Model framework where action is a first-class variable; minute-scale stable rollouts ([[agibot-genie-envisioner-2-announcement|AGIBOT Genie Envisioner 2.0 Announcement]]).
- **[[genesis|Genesis]]** — adjacent: physics-based but uses a [[vla-models|VLM]] agent to *generate* the simulation content from text.

## Paradigm B: JEPA / latent-prediction world models
Predict the next-state *representation* in a learned latent space — no pixels generated. See [[jepa|Joint-Embedding Predictive Architecture]] for the architectural definition. Pioneered in Yann LeCun's group at FAIR / NYU / Mila.

| | Generative-video | JEPA / latent-prediction |
|---|---|---|
| What's predicted | Next-frame pixels | Next-state embedding |
| Training cost | Massive (per-frame generation) | Lower (no decoder) |
| Planning cost | High (video rollout) | Far lower; LeWM reports 48× faster planning |
| Pretraining at scale | Possible but costly | Web-video-scale pretraining is tractable |

Notable systems:
- **[[v-jepa-2|V-JEPA 2 / V-JEPA 2-AC]]** ([[meta-fair|Meta FAIR]] + [[mila|Mila]]) — 1B-param ViT-g pretrained on 1M+ hours of internet video; 300M-param action-conditioned predictor post-trained on 62 hr of Droid robot data; **zero-shot Franka manipulation in new labs** ([[v-jepa-2-paper|V-JEPA 2 Paper]]).
- **[[leworldmodel|LeWorldModel]]** ([[mila|Mila]] + NYU + Samsung SAIL + Brown) — first stable end-to-end JEPA from raw pixels with just two loss terms; 15M params; single-GPU training; 48× faster planning ([[leworldmodel-paper|LeWorldModel Paper]]).

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
- [[vla-models|VLA models]] — the policies that train inside or alongside world-model environments.
- [[sim-to-real-transfer|Sim-to-real transfer]] — relevance shifts: latent-prediction reduces the visual-axis gap but introduces a "model fidelity gap" instead.
- [[jepa|Joint-Embedding Predictive Architecture]] — paradigm B's underlying architecture family.

## Mentioned in
- [[agibot-genie-envisioner-2-announcement|AGIBOT Genie Envisioner 2.0 Announcement]]
- [[genie-envisioner-paper|Genie Envisioner Paper]]
- [[v-jepa-2-paper|V-JEPA 2 Paper]]
- [[leworldmodel-paper|LeWorldModel Paper]]
