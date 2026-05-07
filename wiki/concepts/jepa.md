---
title: Joint-Embedding Predictive Architecture
type: concept
created: 2026-05-07
updated: 2026-05-07
sources: 2
tags: [jepa, world-model, self-supervised, latent-prediction, lecun]
---

**JEPA (Joint-Embedding Predictive Architecture)** — a family of world models that learn by **predicting the representation of a future state in a learned latent space**, rather than reconstructing pixels or generating video. Proposed by Yann LeCun (2022) as a path to learning world knowledge from observation alone.

## Core idea
- Encoder maps inputs to a latent embedding `z`.
- Predictor maps `z_t` (and optionally action `a_t`) to a prediction of `z_{t+1}`.
- Loss is computed in **latent space**, not pixel space — sidestepping the cost and ill-posedness of generating high-fidelity video.

## Why this matters for agentic robotics
- **Cost asymmetry**: video-generation world models ([[nvidia-cosmos|NVIDIA Cosmos]], [[genie-envisioner|Genie Envisioner]]) need to render every frame to compute losses; JEPAs only need a representation, which can be ~100× cheaper at training and inference time.
- **Planning speed**: latent-space MPC can run far faster than video-rollout MPC. [[leworldmodel|LeWorldModel]] reports up to **48× faster planning** than foundation-model-based world models.
- **Internet-scale pretraining**: JEPAs can absorb action-free observation data (web video) at scale, then post-train action-conditioned predictors on small interaction datasets. [[v-jepa-2|V-JEPA 2]] is the canonical demonstration: 1M+ hours pretraining → 62 hr post-training → zero-shot Franka manipulation.

## Common training challenges
- **Representation collapse** — without the right inductive biases, both encoder and predictor learn trivial constants. Existing JEPAs use a battery of fixes: EMA target encoders, stop-gradient, frozen pre-trained encoders, multi-term losses.
- **[[leworldmodel|LeWorldModel]]** simplifies this with a single SIGReg regularizer (Gaussian latent enforcement) and no EMA / stop-grad / frozen encoder.

## Notable instances
- **[[v-jepa-2|V-JEPA 2 / V-JEPA 2-AC]]** ([[meta-fair|Meta FAIR]] + [[mila|Mila]]) — large-scale video pretraining + action-conditioned post-training; zero-shot Franka.
- **[[leworldmodel|LeWorldModel]]** ([[mila|Mila]] + NYU + Samsung SAIL + Brown) — first stable end-to-end JEPA with two-term loss; single-GPU training.
- Comparison points (no entity pages yet): DINO-WM (foundation-based), Dreamer (task-specific reward), TD-MPC (state-based), PLDM (end-to-end with 6 hyperparameters).

## Related
- [[world-model-simulators|World-model simulators]] — JEPAs are one of two paradigms (the other being generative-video models).
- [[meta-fair|Meta FAIR]] — center of the JEPA research line.
- [[mila|Mila]] — frequent contributor.

## Mentioned in
- [[v-jepa-2-paper|V-JEPA 2 Paper]]
- [[leworldmodel-paper|LeWorldModel Paper]]
