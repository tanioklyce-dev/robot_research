---
title: ROSOrin Pro 6-DOF arm
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-07
sources: 3
tags: [rosorin-pro, arm, manipulator, hx-12h, hiwonder, 6-dof]
status: stub
---

The 6-DOF manipulator that ships on [ROSOrin Pro](rosorin-pro.md). Built around modular **HX-12H bus servos** with a gripper end-effector. No standalone SKU surfaced — sold as part of the ROSOrin Pro kit. Specific arm dimensions and payload not stated in the manuals.

## What we know
- 6 degrees of freedom.
- Joint actuation: HX-12H bus servos (0–240° rotation, 12 kg·cm stall torque @ 11.0 V, 0.2 s/60° speed).
- Gripper controlled by the same HX-12H servo class.
- Driven via Hiwonder's [`openclaw_controller`](openclaw-controller.md) ROS 2 module, which exposes the skill library (`pick`, `place`, action groups `voice_pick`, `voice_give`, `init`, `camera_up`) to upstream [OpenClaw](openclaw.md).
- Software interface: ROS 2 service `~/arm_group_control` accepts string commands.

## Open questions
- Reach / workspace volume.
- Payload at the gripper.
- Repeatability / accuracy.
- Whether the same arm is sold separately from the kit (and as what SKU).

## Related
- [ROSOrin Pro](rosorin-pro.md) — host platform.
- [OpenClaw](openclaw.md) — LLM-agent that drives it (via [`openclaw_controller`](openclaw-controller.md)).

## Mentioned in
- [Hiwonder ROSOrin Pro User Manual](../sources/hiwonder-rosorin-pro-user-manual.md)
- [Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md)
