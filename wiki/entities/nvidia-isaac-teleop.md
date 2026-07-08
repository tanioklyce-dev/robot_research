---
title: NVIDIA Isaac Teleop
type: entity
subtype: product
created: 2026-07-07
updated: 2026-07-07
sources: 1
tags: [isaac-teleop, teleoperation, nvidia, data-collection, xr, vr, cloudxr, lerobot, so-101]
---

**NVIDIA Isaac Teleop** — NVIDIA's teleoperation framework for collecting robot-learning demonstrations, "real and sim, in formats compatible with downstream training pipelines" ([announcement blog](../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md), 2026-07-07). Ships as the pip package `isaacteleop` (~1.3.131 at announcement) with `cloudxr` and `retargeters-lite` extras, and integrates with [LeRobot](lerobot.md) record/teleoperate entry points.

## What it does

- **Two collection modes** on the reference [SO-101](so-arm101.md) setup: a classic **leader arm**, or a **VR/XR headset** (`--teleop.type=xr_controller`) via CloudXR streaming with retargeting from controller pose to robot joints ([blog](../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md)).
- **LeRobot-native output** — recordings go straight to `LeRobotDataset` (Dataset v3.0 for [GR00T](nvidia-groot.md) post-training) and push to the HF Hub, slotting into the standard teleop → record → train → deploy loop.
- Positioned as the data-collection front end of NVIDIA's GR00T fine-tuning story: the announcement pairs it with [GR00T 1.7 in LeRobot](../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md) for the full demonstrate → fine-tune → rollout walkthrough (50 episodes → 20k steps → `lerobot-rollout`).

## Position in the teleop landscape

The wiki's demonstration-collection lineage: leader-arm teleop ([ALOHA](aloha.md) / SO-101 leader, the LeRobot default), whole-body tethered teleop ([Mobile ALOHA](aloha.md)), handheld ungrippered collection ([UMI](../sources/umi-paper.md)), and now vendor XR teleop (Isaac Teleop). The XR mode trades the leader arm's 1:1 kinematic fidelity for headset ubiquity and a sim+real story — relevant wherever a second arm is the cost bottleneck.

## Open questions / TBD

- Supported headsets, CloudXR licensing/requirements, and the full retargeter list are not in the announcement; the Isaac Teleop docs would fill this in.
- Whether it drives Isaac Sim embodiments beyond the SO-101 example (humanoids, bimanual rigs) — implied by "real and sim" but not shown.
- Relationship to earlier NVIDIA teleop work (Isaac Lab teleop devices, GR00T-Teleop/AVP pipelines) — unclear if this is a rebrand, superset, or new stack.

## Mentioned in

- [NVIDIA Isaac Teleop and GR00T 1.7 in LeRobot (HF blog)](../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md) — announcement; primary source.
