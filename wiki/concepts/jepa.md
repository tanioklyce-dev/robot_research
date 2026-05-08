---
title: Joint-Embedding Predictive Architecture
type: concept
created: 2026-05-07
updated: 2026-05-07
sources: 7
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
- **[[v-jepa-2|V-JEPA 2 / V-JEPA 2-AC]]** ([[meta-fair|Meta FAIR]] + [[mila|Mila]], June 2025) — large-scale video pretraining + action-conditioned post-training; zero-shot Franka.
- **[[v-jepa-2-1-paper|V-JEPA 2.1]]** (FAIR + Mila, March 2026) — successor; "dense features" focus; +20pt real-Franka grasping over V-JEPA 2-AC.
- **[[leworldmodel|LeWorldModel]]** ([[mila|Mila]] + NYU + Samsung SAIL + Brown, March 2026) — first stable end-to-end JEPA with two-term loss; single-GPU training.
- **[[jepa-wms|JEPA-WMs]]** (Terver et al., FAIR, Dec 2025) — moves JEPA into [[robocasa|RoboCasa]] + Metaworld + DROID + real Franka; outperforms DINO-WM and V-JEPA 2-AC on the proposed setup.
- **[[vla-jepa|VLA-JEPA]]** (Sun et al., Feb 2026) — JEPA-as-auxiliary-objective inside a VLA policy; uses LIBERO + SimplerEnv + real.
- **JEPA-adjacent (frozen DINOv2 encoder, not co-trained):**
  - **[[dino-wm|DINO-WM]]** (Zhou et al., NYU + FAIR, Nov 2024) — DINOv2 features + learned predictor; zero-shot planning. Lightweight benches (PushT, Wall, PointMaze, Rope, Granular, Reacher).
  - **[[dino-world|DINO-world]]** (Baldassarre et al., FAIR, July 2025) — DINOv2 features for video world models; predates JEPA-WMs by 5 months and shares Basile Terver as a bridge author.
- Comparison points (no entity pages yet): Dreamer / DreamerV3 (task-specific reward), TD-MPC (state-based), PLDM (end-to-end with 6 hyperparameters).

## Simulator stance — fragmenting, not avoiding
The original wiki synthesis observed [[v-jepa-2|V-JEPA 2]] and [[leworldmodel|LeWM]] both skipping heavy agentic-robotics sim. With five additional ingests in May 2026, the picture is more nuanced: [[jepa-wms|JEPA-WMs]] uses [[robocasa|RoboCasa]]; [[vla-jepa|VLA-JEPA]] uses SimplerEnv; [[dino-wm|DINO-WM]] uses lightweight MuJoCo benches; [[v-jepa-2-1-paper|V-JEPA 2.1]] continues the no-sim line. **The JEPA literature is fragmenting across simulator weight classes**, not avoiding sim wholesale. See [[why-jepa-research-skips-the-simulator-stack|the revised synthesis]].

## Related
- [[world-model-simulators|World-model simulators]] — JEPAs are one of two paradigms (the other being generative-video models).
- [[meta-fair|Meta FAIR]] — center of the JEPA research line.
- [[mila|Mila]] — frequent contributor.

## Mentioned in
- [[v-jepa-2-paper|V-JEPA 2 Paper]]
- [[v-jepa-2-1-paper|V-JEPA 2.1 Paper]]
- [[leworldmodel-paper|LeWorldModel Paper]]
- [[jepa-wms-paper|JEPA-WMs Paper]]
- [[dino-wm-paper|DINO-WM Paper]]
- [[dino-world-paper|DINO-world Paper]]
- [[vla-jepa-paper|VLA-JEPA Paper]]
