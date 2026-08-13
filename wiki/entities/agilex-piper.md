---
title: AgileX Piper
type: entity
subtype: robot
created: 2026-08-04
updated: 2026-08-13
sources: 3
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

## The Piper is the wiki's case study in low-DoF disadvantage

[RoboTwin 2.0](robotwin.md)'s embodiment-aware grasp adaptation moved automated data-generation success on the 6-DoF Piper from **2.4% to 25.1% (+22.7)**, the largest gain of any of its five embodiments — while 7-DoF [Franka](franka-panda.md) moved **−0.1** and UR5 **−0.5** ([paper](../sources/robotwin2-paper.md)). The mechanism is stated plainly: *"a low-DoF platform like the Piper often relies on lateral grasps due to its limited dexterity, whereas a high-DoF arm such as the Franka is capable of top-down precision grasps."*

The 2.4% figure is the striking one. Before targeted engineering, a state-of-the-art bimanual data generator **could not produce usable demonstrations for this arm at all** — not because the tasks were impossible for it, but because the generator's grasp candidates assumed a dexterity it doesn't have. Cheap arms are not merely worse at tasks; they are worse at *being trained*, and closing that requires deliberate work at the data layer that nobody does by default.

This is the same constraint the wiki meets from two other directions — [X-VLA](x-vla.md) pretraining exclusively on ≥6-DoF arms while [Sourccey](sourccey.md) ships 5-DoF ones, and [RoboMIND](robomind.md)'s dexterous-hand data being structurally unusable by the same model. See [RoboMIND](robomind.md) for the assembled argument.

## The AgileX family across this wiki

| Platform | Where it appears |
|---|---|
| **Piper** (6-DoF single arm) | [TurboVLA](turbovla.md) real-world eval; [RoboTwin 2.0](robotwin.md) embodiment; [DimOS](dimos.md) 🟨 beta |
| **Aloha-AgileX** (bimanual) | [RoboTwin 2.0](robotwin.md)'s *benchmark* embodiment — every published Easy/Hard number is on this platform |
| **Cobot Magic V2.0** (dual-arm) | 10,269 trajectories in [RoboMIND](robomind.md); the sim-to-real platform in RoboTwin 2.0's real-world experiments |
| Bimanual (unspecified) | [X-VLA](x-vla.md)'s **cloth-folding** rig — ~100% success, 33 folds/hr |

AgileX also **part-funded** the RoboTwin 2.0 work (acknowledgments). Worth knowing when reading a benchmark whose reference embodiment is theirs.

## Open questions
- Price, payload, reach, and repeatability are not documented in the ingested source — this entity is currently a **stub** built from one paper's methods section. A vendor-page ingest would let it be compared properly against the [SO-101](so-arm101.md) / [Yuri](yuri.md) / [Franka](franka-panda.md) tiers in the [robot platforms comparison](../syntheses/platforms/robot-platforms-comparison.md).
- AgileX also produces mobile bases and bimanual kits that appear in Chinese-lab robot-learning papers; the bimanual configuration is now attested via [X-VLA](x-vla.md) but no vendor spec has been ingested.
- Which AgileX bimanual product is X-VLA's cloth-folding rig? The paper says only "bi-manual Agilex platform."

## Mentioned in
- [TurboVLA paper](../sources/turbovla-paper.md)
