---
title: AgileX Piper
type: entity
subtype: robot
created: 2026-08-04
updated: 2026-08-13
sources: 2
tags: [agilex, piper, robot-arm, manipulator, affordable-hardware, realsense, teleoperation, cloth-folding, xvla]
---

**AgileX Piper** — a **6-DoF lightweight robotic arm** from AgileX Robotics, used as the real-world evaluation platform in the [TurboVLA paper](../sources/turbovla-paper.md). Sits in the affordable-research-arm tier alongside the [SO-101](so-arm101.md) and [Koch](lerobot.md)-class arms, above them in payload/reach and below [Franka](franka-panda.md)-class research arms in price.

## As used in TurboVLA

- Single-arm tabletop setup with **two Intel RealSense D435 RGB-D cameras** — one wrist-mounted, one third-person.
- Four language-conditioned tasks: *grab roller*, *move playing card away*, *press stapler*, *stack three bowls*.
- **65 teleoperated demonstrations per task**; policy fine-tuned from a LIBERO-pretrained checkpoint for 12.5 k steps.
- 40 evaluation trials per task; TurboVLA scored 92.5 / 80 / 90 / 87.5% ([paper](../sources/turbovla-paper.md)).

> [!note] Only the RGB streams are known to be used
> The cameras are D435 **RGB-D** units, but TurboVLA's architecture ingests images through a [DINOv3](dinov3.md) ViT with no depth pathway described. Whether depth is used at all is unstated.

## As used in X-VLA — the cloth-folding platform

A **bimanual** AgileX setup with wrist-mounted cameras is [X-VLA](x-vla.md)'s dexterous-manipulation testbed ([paper](../sources/xvla-paper.md)), and the platform on which its flagship real-world result was produced: **cloth folding at ~100% success and 33 folds per hour**, matching a closed-source π0-folding model presumed to have far more training data.

The **Soft-Fold** dataset was collected on it — 1,200 trajectories, ~1.5 min per episode, **20–25 episodes per operator-hour** including resets and discards, so roughly 50–60 operator-hours in total. Release is promised. Collection used a two-stage decomposition (smooth the disordered cloth, then fold it) and **DAgger-style iteration**: retrain [ACT](act.md) every 100 episodes, identify its failure modes, collect against them.

AgileX also appears in X-VLA's *pretraining* mixture as `RoboMind-Agilex` (3.7% of 290 K episodes, 30 Hz, head + wrist) — a different, single-arm configuration.

## Open questions
- Price, payload, reach, and repeatability are not documented in the ingested source — this entity is currently a **stub** built from one paper's methods section. A vendor-page ingest would let it be compared properly against the [SO-101](so-arm101.md) / [Yuri](yuri.md) / [Franka](franka-panda.md) tiers in the [robot platforms comparison](../syntheses/platforms/robot-platforms-comparison.md).
- AgileX also produces mobile bases and bimanual kits that appear in Chinese-lab robot-learning papers; the bimanual configuration is now attested via [X-VLA](x-vla.md) but no vendor spec has been ingested.
- Which AgileX bimanual product is X-VLA's cloth-folding rig? The paper says only "bi-manual Agilex platform."

## Mentioned in
- [TurboVLA paper](../sources/turbovla-paper.md)
