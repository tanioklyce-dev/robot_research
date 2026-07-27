---
title: WorldDP
type: entity
subtype: model
created: 2026-07-26
updated: 2026-07-26
sources: 1
tags: [worlddp, world-model, jepa, object-centric, diffusion-policy, hierarchical-planning, mpc, particle-filter, multi-stage-manipulation, dinov2, sam2, ogbench, lecun, ami-labs, nyu]
---

# WorldDP

**WorldDP** ([Goswami, Krishnamurthy, LeCun, Khorrami 2026](../sources/worlddp-paper.md), arXiv 2606.08775) is a **hierarchical framework for multi-stage robotic manipulation** that unifies an **object-centric [JEPA](../concepts/world-models/jepa.md) world model** (high-level subgoal planner) with a **[Diffusion Policy](diffusion-policy.md)** (low-level subgoal tracker). It is a [Yann LeCun](yann-lecun.md)-coauthored NYU paper and the **first paper in this wiki to carry an [AMI Labs](ami-labs.md) affiliation** on his byline.

## Why it matters in this wiki

WorldDP is the wiki's first model to **bridge the two rival control paradigms it otherwise tracks separately** — LeCun's JEPA-world-model-as-planner line ([DINO-WM](dino-wm.md), [LeWorldModel](leworldmodel.md), [HWM](hwm.md), [V-JEPA 2](v-jepa-2.md)) and the imitation-learning [Diffusion Policy](diffusion-policy.md) / [VLA](../concepts/learning/vla-models.md) line. Its argument is that neither alone handles **multi-stage** tasks: latent world models plan but stall on long horizons; diffusion policies execute but don't plan. WorldDP makes the world model a **subgoal generator** and the diffusion policy a **subgoal executor** — and empirically that combination more than doubles the next-best success rate on 3-object rearrangement. It also sharpens the contrast with **[HWM](hwm.md)** (the wiki's other hierarchical latent planner), which uses a *second world model* at the low level rather than a diffusion policy.

## Architecture

- **Object-Centric Encoder (OCE):** frozen **DINOv2** patch features → **slot attention** (N slots for robot/objects/background) refined by a GRU "Slot Corrector"; trained with reconstruction + a **Tversky mask loss** against **SAM2**-generated segmentation masks (privileged training-time guidance). Learns object representations *on top of* DINOv2 patches, not raw pixels.
- **Dynamics model:** a **Conditional Diffusion Transformer (CDiT)** (12 layers, 4 heads) over object-centric states, conditioned on a 32-D latent action embedding; autoregressive at planning time.
- **Upper tier (planning):** the world model is the transition function in an **MPC** loop optimized by a **Particle Filter** (multi-modal, unlike CEM's single Gaussian). Cost = object-embedding MSE + a **contact-prediction** term (an MLP flags robot-object contact → pushes subgoals to pivotal frames like "handle gripped").
- **Lower tier (execution):** a **goal-conditioned 40-step Diffusion Policy** tracks each subgoal; multi-object tasks plan/execute per object in an MPC loop.

## Reported numbers (from ingested sources)

OGBench manipulation (UR5e, [LeWM](leworldmodel.md)-variant envs; 50 held-out trials):

- **Cube-Triple, all 3 cubes: 30%** — >2× the next best (HECRL* 12, DP100 4, [DINO-WM](dino-wm.md)/[LeWM](leworldmodel.md) 0).
- **Scene-Single-Composite, full task: 20%** (HECRL* 18, DP100 14, others 0).
- **Cube-Single + Scene-Single-Direct "both-task" avg: 74.5%** (HECRL* 63, DP100 63, DP40 32).
- Ablations confirm the hierarchy, the object-centric encoding, the 40-step (vs 100-step) DP, and the particle filter (vs CEM) each help.

## Related

- [Yann LeCun](yann-lecun.md) — co-author; his AMI-Labs-affiliated paper.
- [Diffusion Policy](diffusion-policy.md) — the low-level tracker WorldDP wraps.
- [HWM](hwm.md) — the other hierarchical latent-world-model planner; uses a world model (not a diffusion policy) at the low level.
- [DINO-WM](dino-wm.md) / [LeWorldModel](leworldmodel.md) / [V-JEPA 2](v-jepa-2.md) — single-stage JEPA-world-model baselines it beats.
- [JEPA](../concepts/world-models/jepa.md) — the paradigm it extends with object-centric states.
- [VLA models](../concepts/learning/vla-models.md) — the end-to-end alternative it positions against.

## Open questions

- Per-environment training (no cross-task/embodiment transfer shown); **simulation-only** (OGBench), unlike the LeCun program's real-Franka V-JEPA 2 / HWM results; SAM2 guidance is privileged supervision.

## Mentioned in

- [WorldDP paper (Goswami et al. 2026)](../sources/worlddp-paper.md) — the primary source.
