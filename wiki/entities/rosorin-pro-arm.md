---
title: ROSOrin Pro 6-DOF arm
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-07
sources: 2
tags: [rosorin-pro, arm, manipulator, hx-12h, hiwonder, 6-dof]
status: stub
---

The 6-DOF manipulator that ships on [[rosorin-pro|ROSOrin Pro]]. Built around modular **HX-12H bus servos** with a gripper end-effector. No standalone SKU surfaced — sold as part of the ROSOrin Pro kit. Specific arm dimensions and payload not stated in the manuals.

## What we know
- 6 degrees of freedom.
- Joint actuation: HX-12H bus servos (0–240° rotation, 12 kg·cm stall torque @ 11.0 V, 0.2 s/60° speed).
- Gripper controlled by the same HX-12H servo class.
- Driven by [[openclaw|OpenClaw]]'s skill library (`pick`, `place`, action groups `voice_pick`, `voice_give`, `init`, `camera_up`).
- Software interface: ROS 2 service `~/arm_group_control` accepts string commands.

## Open questions
- Reach / workspace volume.
- Payload at the gripper.
- Repeatability / accuracy.
- Whether the same arm is sold separately from the kit (and as what SKU).

## Related
- [[rosorin-pro|ROSOrin Pro]] — host platform.
- [[openclaw|OpenClaw]] — software that drives it.

## Mentioned in
- [[hiwonder-rosorin-pro-user-manual|Hiwonder ROSOrin Pro User Manual]]
- [[hiwonder-openclaw-tutorial|Hiwonder OpenClaw Practical Tutorial]]
