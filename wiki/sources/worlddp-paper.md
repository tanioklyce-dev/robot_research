---
title: "WorldDP: Unifying Object-Centric World Models and Diffusion Policy (Goswami, Krishnamurthy, LeCun, Khorrami 2026)"
type: source
url: https://arxiv.org/abs/2606.08775
author: Raktim Gautam Goswami, Prashanth Krishnamurthy, Yann LeCun, Farshad Khorrami (NYU + AMI Labs)
published: 2026-06-07
ingested: 2026-07-26
local_path: raw/2606.08775.pdf
venue: arXiv preprint (cs.RO)
license: arXiv
format: pdf
tags: [worlddp, world-model, jepa, object-centric, diffusion-policy, hierarchical-planning, mpc, particle-filter, multi-stage-manipulation, dinov2, sam2, ogbench, lecun, ami-labs, nyu]
---

# WorldDP: Unifying Object-Centric World Models and Diffusion Policy

## Summary

**WorldDP** is a **hierarchical framework for multi-stage robotic manipulation** that couples a [JEPA](../concepts/world-models/jepa.md)-style **object-centric world model** (high level, for subgoal planning) with a [Diffusion Policy](../entities/diffusion-policy.md) (low level, for execution). Its thesis: existing latent world models ([DINO-WM](../entities/dino-wm.md), [LeWorldModel](../entities/leworldmodel.md), [V-JEPA 2](../entities/v-jepa-2.md)) plan well on **single-stage** tasks (reach, grasp) but fail on **multi-stage** ones (pick→place→rearrange) because (a) patch-level DINOv2 features are a poor state space for dynamics, (b) flat single-tier planning can't decompose long horizons, and (c) CEM optimization ignores the multi-modality of robot action spaces. WorldDP fixes all three: an **object-centric encoder** (slot attention on frozen DINOv2, guided by SAM2 masks) gives entity-decoupled states; a **two-tier hierarchy** uses the world model as an MPC transition function to propose subgoals that a fast diffusion policy then tracks; and a **particle filter** (not CEM) plus a **contact predictor** in the cost function yield precise, multi-modal subgoals. It is a [Yann LeCun](../entities/yann-lecun.md) co-authored NYU paper — and **the first paper in this wiki to carry an [AMI Labs](../entities/ami-labs.md) affiliation** on LeCun's byline.

## Key claims

- **Problem framing:** world models as MPC transition functions can train on reward-free, suboptimal, unlabeled trajectories and generalize to new goal configurations without fine-tuning — an advantage over end-to-end [Diffusion Policy](../entities/diffusion-policy.md) / [VLA](../concepts/learning/vla-models.md) methods — but prior latent world models are stuck on single-stage tasks.
- **Object-Centric Encoder (OCE):** frozen **DINOv2** patch features → **slot attention** (N slots = robot / objects / background) refined by a GRU "Slot Corrector"; trained with a reconstruction loss + a **Tversky mask-segmentation loss** against **SAM2**-generated masks (privileged guidance, so small objects like cubes aren't under-represented). Novelty vs. prior object-centric work: representations are learned **on top of DINOv2 patches** rather than raw pixels.
- **Dynamics model:** a **Conditional Diffusion Transformer (CDiT)** (12 layers, 4 heads) predicts next object-centric state from current state + a 32-D latent action embedding; trained by teacher-forced MSE with random temporal skips over 100-frame horizons; autoregressive at planning time.
- **Hierarchical planning (the core idea):** upper tier runs the world model in an MPC loop optimized by a **Particle Filter** (chosen over CEM because robot action spaces are **multi-modal** — many valid action sequences reach the same goal); an **object-centric cost** (MSE on object embeddings, excluding agent/background) plus a **contact-prediction cost** (a trained MLP flags robot-object contact, pushing subgoals toward pivotal frames like "handle gripped") select subgoals. Lower tier: a **goal-conditioned Diffusion Policy** (40-step, DINOv2-object-centric inputs) tracks each subgoal; for multi-object tasks it plans/executes per object in an MPC loop.
- **Benchmark:** OGBench manipulation tasks (variants from [LeWM](../entities/leworldmodel.md)/Maes et al. 2026a — different camera + end-effector color), UR5e arm, 5-D action (EE Δx,y,z + yaw + gripper). Tasks: Cube-Single, **Cube-Triple** (rearrange 3 cubes), Scene-Single-Direct, **Scene-Single-Composite** (button-press prerequisite → manipulate). 2M-frame reward-free "play" datasets; single H100; 5 epochs.
- **Results (50 held-out trials/task):**
  - **Cube-Triple, all-3-cubes: WorldDP 30%** vs HECRL* 12, DP100 4, DINO-WM/LeWM 0 — **>2× the next best**. 1-cube 100%, 2-cubes 72%.
  - **Scene-Single-Composite full task: 20%** vs HECRL* 18, DP100 14, others 0.
  - **Cube-Single + Scene-Single-Direct "both-task average": 74.5%** vs HECRL* 63, DP100 63, DP40 32.
  - Ablations: hierarchy beats "w/o DP" (raw-action optimization) and "DP-only"; **object-centric encoding** beats raw-DINOv2-patch states; **40-step DP** beats 100-step (world model gives closely-spaced precise subgoals); **particle filter** beats CEM.
- **Contrast with [HWM](../entities/hwm.md) (Zhang et al. 2026):** both are hierarchical latent-world-model planners, but HWM uses **another world model** at the low level (optimizing physical actions against a patch-level cost), whereas WorldDP uses a **diffusion policy** — faster, more robust to imperfect subgoals, and able to sustain longer multi-stage sequences.

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md) — co-author (Courant NYU + [AMI Labs](../entities/ami-labs.md)).
- [AMI Labs](../entities/ami-labs.md) — LeCun's affiliation on this byline (the wiki's first AMI-Labs-affiliated paper).
- [WorldDP](../entities/worlddp.md) — the framework.
- [DINO-WM](../entities/dino-wm.md), [LeWorldModel](../entities/leworldmodel.md), [HWM](../entities/hwm.md), [V-JEPA 2](../entities/v-jepa-2.md) — JEPA-world-model baselines / contrasts.
- [Diffusion Policy](../entities/diffusion-policy.md) — the low-level tracker.
- Authors: Raktim Gautam Goswami, Prashanth Krishnamurthy, Farshad Khorrami (NYU Tandon Control/Robotics).

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — the latent-world-model paradigm WorldDP extends with object-centric states + hierarchy.
- [VLA models](../concepts/learning/vla-models.md) — the end-to-end alternative WorldDP positions against.
- [World model](../concepts/world-models/world-model.md) — world-model-as-MPC-transition-function usage.

## Open questions

- Object-Centric Encoder, dynamics model, DP, and contact predictor are all **trained per-environment** — no cross-task/cross-embodiment transfer is demonstrated. How much of the multi-stage win survives a shared model?
- Results are **simulation-only (OGBench)** — no real-robot deployment, unlike the LeCun-program's V-JEPA 2 / HWM real-Franka results.
- SAM2 mask guidance is **privileged supervision** at training time; how does OCE degrade without it on cluttered real scenes?
