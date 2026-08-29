---
title: Fast Explicit-Input Assistance for Teleoperation in Clutter (Walker et al., IROS 2024)
type: source
url: https://github.com/NVlabs/fast-explicit-teleop
local_path: raw/walker2024explicit.pdf
sha256: fdeeae086dcbad1eee2a8f3db46e5abac7946604fa57f608f6384565c3d9dba5
author: Nick Walker, Xuning Yang, Animesh Garg, Maya Cakmak, Dieter Fox, Claudia Pérez-D'Arpino
published: 2024 (IROS 2024, Abu Dhabi, UAE, October 2024)
ingested: 2026-05-09
tags: [teleoperation, shared-control, hcrlab, maya-cakmak, nvidia, iros2024, clutter]
---

## Summary

Proposes an explicit-input teleoperation assistance interface where the operator points the robot's end-effector toward a target object to communicate a manipulation goal. A local ray-cast optimization generates collision-free grasp or placement pose candidates at interactive speeds. Compared against implicit inference-based assistance in an N=20 within-subjects user study (simulated pick-and-place stacking in clutter). Operators prefer the explicit interface, experience fewer pick failures, and report lower cognitive workload.

## Key claims

- **Problem with implicit assistance**: Prediction-based systems infer operator intent from trajectory history — but in cluttered scenes, many objects are nearby and intent is ambiguous. Poor predictions confuse operators or cause them to modify behavior to "signal" intent, compounding errors.
- **Explicit interface design**: Operator points the end-effector's forward axis toward the target object. A ray-cast from the gripper intersects the scene geometry; a local optimization generates a feasible, collision-free grasp or placement pose. The pose is a suggestion — the operator can reject or refine.
- **Key design choices**: (1) transparent state (pointing axis is immediately visible); (2) smooth assistance (small state changes → small assistance changes); (3) pose as suggestion, not command.
- **Evaluation**: Franka Emika Panda arm; implemented and evaluated in NVIDIA Omniverse Isaac Sim. N=20 within-subjects; task: pick-and-place stacking in cluttered environments.
- **Results**: Operators prefer explicit interface; fewer pick failures; lower cognitive workload (NASA-TLX). No significant speed penalty.
- **Code**: Open-source at github.com/NVlabs/fast-explicit-teleop (NVIDIA Labs).
- **Affiliations**: Walker (UW; internship at NVIDIA), Yang + Pérez-D'Arpino (NVIDIA), Garg (Georgia Tech), Cakmak + Fox (UW; Fox also NVIDIA).

## Entities mentioned

- [Maya Cakmak](../entities/maya-cakmak.md)
- [HCR Lab](../entities/hcrlab.md)
- [NVIDIA](../entities/nvidia.md) — collaboration; NVIDIA Isaac Sim used for evaluation
- [Franka Panda](../entities/franka-panda.md) — robot platform

## Concepts touched

- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — teleoperation interface for assistive manipulation
- [End-user robot programming](../concepts/robotics/end-user-robot-programming.md) — explicit user control vs. autonomous inference

## Open questions

- Was the study with disabled or non-disabled participants? (paper says "operators" — likely non-disabled in simulation)
- Does explicit pointing transfer to real hardware and non-expert users with motor impairments?
