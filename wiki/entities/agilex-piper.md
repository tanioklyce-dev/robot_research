---
title: AgileX Piper
type: entity
subtype: robot
created: 2026-08-04
updated: 2026-08-04
sources: 1
tags: [agilex, piper, robot-arm, manipulator, affordable-hardware, realsense, teleoperation]
---

**AgileX Piper** — a **6-DoF lightweight robotic arm** from AgileX Robotics, used as the real-world evaluation platform in the [TurboVLA paper](../sources/turbovla-paper.md). Sits in the affordable-research-arm tier alongside the [SO-101](so-arm101.md) and [Koch](lerobot.md)-class arms, above them in payload/reach and below [Franka](franka-panda.md)-class research arms in price.

## As used in TurboVLA

- Single-arm tabletop setup with **two Intel RealSense D435 RGB-D cameras** — one wrist-mounted, one third-person.
- Four language-conditioned tasks: *grab roller*, *move playing card away*, *press stapler*, *stack three bowls*.
- **65 teleoperated demonstrations per task**; policy fine-tuned from a LIBERO-pretrained checkpoint for 12.5 k steps.
- 40 evaluation trials per task; TurboVLA scored 92.5 / 80 / 90 / 87.5% ([paper](../sources/turbovla-paper.md)).

> [!note] Only the RGB streams are known to be used
> The cameras are D435 **RGB-D** units, but TurboVLA's architecture ingests images through a [DINOv3](dinov3.md) ViT with no depth pathway described. Whether depth is used at all is unstated.

## Open questions
- Price, payload, reach, and repeatability are not documented in the ingested source — this entity is currently a **stub** built from one paper's methods section. A vendor-page ingest would let it be compared properly against the [SO-101](so-arm101.md) / [Yuri](yuri.md) / [Franka](franka-panda.md) tiers in the [robot platforms comparison](../syntheses/platforms/robot-platforms-comparison.md).
- AgileX also produces mobile bases and bimanual kits that appear in Chinese-lab robot-learning papers; none are ingested here yet.

## Mentioned in
- [TurboVLA paper](../sources/turbovla-paper.md)
