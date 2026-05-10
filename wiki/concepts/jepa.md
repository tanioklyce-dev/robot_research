---
title: Joint-Embedding Predictive Architecture
type: concept
created: 2026-05-07
updated: 2026-05-10
sources: 8
tags: [jepa, world-model, self-supervised, latent-prediction, lecun]
---

**JEPA (Joint-Embedding Predictive Architecture)** — a family of world models that learn by **predicting the representation of a future state in a learned latent space**, rather than reconstructing pixels or generating video. Proposed by Yann LeCun (2022) as a path to learning world knowledge from observation alone.

## What "Joint" means

**Joint** refers to the fact that both the input (context) and the prediction target (future state) are embedded into the **same shared latent space** by the same encoder:

- `z_t = encoder(x_t)` — current frame
- `z_{t+1} = encoder(x_{t+1})` — future frame, *same encoder*
- Loss: `|| predictor(z_t, a_t) − z_{t+1} ||`

Both sides of the prediction live in the *jointly shared* embedding space. This contrasts with generative/autoregressive models, where the target remains in raw pixel space and the encoder only acts on the input side:

| Architecture | Target is… |
|---|---|
| Generative / autoregressive | Raw pixels — not embedded |
| JEPA | An embedding — same space as the input |

The term **Joint Embedding** names the architecture class defined by this property: all learning — both encoding and prediction — happens inside a single shared representation space. It is also why representation collapse is the central failure mode: if the encoder collapses to a constant, the loss is trivially zero, with no pixel-level signal to expose the problem.

## Core idea
- Encoder maps inputs to a latent embedding `z`.
- Predictor maps `z_t` (and optionally action `a_t`) to a prediction of `z_{t+1}`.
- Loss is computed in **latent space**, not pixel space — sidestepping the cost and ill-posedness of generating high-fidelity video.

## Why this matters for agentic robotics
- **Cost asymmetry**: video-generation world models ([NVIDIA Cosmos](../entities/nvidia-cosmos.md), [Genie Envisioner](../entities/genie-envisioner.md)) need to render every frame to compute losses; JEPAs only need a representation, which can be ~100× cheaper at training and inference time.
- **Planning speed**: latent-space MPC can run far faster than video-rollout MPC. [LeWorldModel](../entities/leworldmodel.md) reports up to **48× faster planning** than foundation-model-based world models.
- **Internet-scale pretraining**: JEPAs can absorb action-free observation data (web video) at scale, then post-train action-conditioned predictors on small interaction datasets. [V-JEPA 2](../entities/v-jepa-2.md) is the canonical demonstration: 1M+ hours pretraining → 62 hr post-training → zero-shot Franka manipulation.

## Common training challenges
- **Representation collapse** — without the right inductive biases, both encoder and predictor learn trivial constants. Existing JEPAs use a battery of fixes: EMA target encoders, stop-gradient, frozen pre-trained encoders, multi-term losses.
- **[LeWorldModel](../entities/leworldmodel.md)** simplifies this with a single SIGReg regularizer (Gaussian latent enforcement) and no EMA / stop-grad / frozen encoder.

## Notable instances
- **[V-JEPA 2 / V-JEPA 2-AC](../entities/v-jepa-2.md)** ([Meta FAIR](../entities/meta-fair.md) + [Mila](../entities/mila.md), June 2025) — large-scale video pretraining + action-conditioned post-training; zero-shot Franka.
- **[V-JEPA 2.1](../sources/v-jepa-2-1-paper.md)** (FAIR + Mila, March 2026) — successor; "dense features" focus; +20pt real-Franka grasping over V-JEPA 2-AC.
- **[LeWorldModel](../entities/leworldmodel.md)** ([Mila](../entities/mila.md) + NYU + Samsung SAIL + Brown, March 2026) — first stable end-to-end JEPA with two-term loss; single-GPU training.
- **[JEPA-WMs](../entities/jepa-wms.md)** (Terver et al., FAIR, Dec 2025) — moves JEPA into [RoboCasa](../entities/robocasa.md) + Metaworld + DROID + real Franka; outperforms DINO-WM and V-JEPA 2-AC on the proposed setup.
- **[VLA-JEPA](../entities/vla-jepa.md)** (Sun et al., Feb 2026) — JEPA-as-auxiliary-objective inside a VLA policy; uses LIBERO + SimplerEnv + real.
- **JEPA-adjacent (frozen DINOv2 encoder, not co-trained):**
  - **[DINO-WM](../entities/dino-wm.md)** (Zhou et al., NYU + FAIR, Nov 2024) — DINOv2 features + learned predictor; zero-shot planning. Lightweight benches (PushT, Wall, PointMaze, Rope, Granular, Reacher).
  - **[DINO-world](../entities/dino-world.md)** (Baldassarre et al., FAIR, July 2025) — DINOv2 features for video world models; predates JEPA-WMs by 5 months and shares Basile Terver as a bridge author.
- Comparison points: [Dreamer / DreamerV3](../entities/dreamer.md) (task-specific reward, generative WM); [TD-MPC](../entities/td-mpc.md) (state-based, decoder-free MBRL); [PLDM](../entities/pldm.md) (end-to-end JEPA with VICReg + inverse-dynamics, ~6 hyperparameters; [Sobal et al. 2025](../sources/pldm-paper.md)).

## Simulator stance — fragmenting, not avoiding
The original wiki synthesis observed [V-JEPA 2](../entities/v-jepa-2.md) and [LeWM](../entities/leworldmodel.md) both skipping heavy agentic-robotics sim. With five additional ingests in May 2026, the picture is more nuanced: [JEPA-WMs](../entities/jepa-wms.md) uses [RoboCasa](../entities/robocasa.md); [VLA-JEPA](../entities/vla-jepa.md) uses SimplerEnv; [DINO-WM](../entities/dino-wm.md) uses lightweight MuJoCo benches; [V-JEPA 2.1](../sources/v-jepa-2-1-paper.md) continues the no-sim line. **The JEPA literature is fragmenting across simulator weight classes**, not avoiding sim wholesale. See [the revised synthesis](../syntheses/why-jepa-research-skips-the-simulator-stack.md).

## Related
- [Learned latent space](latent-space.md) — the substrate JEPAs predict in; the entire design choice rests on this.
- [World-model simulators](world-model-simulators.md) — JEPAs are one of two paradigms (the other being generative-video models).
- [Meta FAIR](../entities/meta-fair.md) — center of the JEPA research line.
- [Mila](../entities/mila.md) — frequent contributor.

## Mentioned in
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
- [V-JEPA 2.1 Paper](../sources/v-jepa-2-1-paper.md)
- [LeWorldModel Paper](../sources/leworldmodel-paper.md)
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)
- [DINO-WM Paper](../sources/dino-wm-paper.md)
- [DINO-world Paper](../sources/dino-world-paper.md)
- [VLA-JEPA Paper](../sources/vla-jepa-paper.md)
- [PLDM Paper](../sources/pldm-paper.md)
