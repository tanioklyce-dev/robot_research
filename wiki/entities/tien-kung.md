---
title: Tien Kung (X-Humanoid)
type: entity
subtype: robot
created: 2026-08-13
updated: 2026-08-13
sources: 1
tags: [tien-kung, humanoid, dexterous-hand, x-humanoid, beijing, robomind, teleoperation, dataset-embodiment]
---

**Tien Kung** (天工) — a humanoid robot with **dual dexterous hands** from the **Beijing Innovation Center of Humanoid Robotics** (X-Humanoid). In this wiki it appears as an *embodiment in a dataset* rather than as a product: **15,187 of [RoboMIND](robomind.md)'s 107k teleoperation trajectories** were collected on it ([paper](../sources/robomind-paper.md)).

## What is known

Very little beyond its role in the dataset — no specs, price, availability, DoF count, or hand design are given in the ingested source. What the source does establish:

- **Dual dexterous hands**, used for precise operations the single-arm platforms in the same dataset cannot attempt — the paper's example is *"flipping a toaster switch to toast bread."*
- Task set spans two categories: tasks mirroring the Franka single-arm set (to test cross-embodiment model performance on the same work) and **dexterous-hand-specific** tasks.
- Baseline results: **[ACT](act.md) 34.0% average** across its tasks, including 60% on `HR-CloseDrawerLowerCabinet`; [Diffusion Policy](diffusion-policy.md) beats ACT on several Tien Kung tasks. All at **n=10 per task** — existence proofs, not rankings.

## Why it matters here

It is the wiki's clearest concrete case of the **dexterous-hand exclusion** in cross-embodiment learning. [X-VLA](x-vla.md) consumes RoboMIND for 19.9% of its pretraining and **drops the Tien Kung split entirely** — necessarily, because X-VLA aligns all embodiments to `xyz + Rot6D + binary gripper` and a multi-fingered hand has no representation in that space.

So the wiki's best-performing cross-embodiment VLA is trained on a corpus whose **most capable end-effector data was structurally unusable**. See [RoboMIND](robomind.md) for the full argument and the low-DoF counterpart.

## Related

- [RoboMIND](robomind.md) — the dataset it contributes to
- [X-VLA](x-vla.md) — consumes RoboMIND, excludes this embodiment
- [Sharpa Wave hand](sharpa-wave.md) — the wiki's other dexterous-hand entry, from the [EgoScale](../sources/egoscale-paper.md) line
- [Unitree G1](unitree-g1.md), [Galaxea R1](galaxea-r1.md) — other humanoid dataset embodiments here

## Mentioned in

- [RoboMIND paper](../sources/robomind-paper.md)
