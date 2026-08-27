---
title: Star Arm 102
type: entity
subtype: product
created: 2026-08-27
updated: 2026-08-27
sources: 2
tags: [star-arm-102, seeed-studio, leader-arm, teleoperation, lerobot, rebot-arm, inverse-kinematics, pieper-criterion]
---

**Star Arm 102** — [Seeed Studio](seeed-studio.md)'s low-cost **6+1-DOF leader arm** for teleoperating the [reBot Arm B601](rebot-arm-b601.md) follower. **$200**, available assembled or as a DIY kit. [Product page](https://www.seeedstudio.com/Star-Arm-102-p-6765.html).

## Why it has its own page

Two reasons. First, it is the **teleoperation half of the reBot data-collection rig** — without it the B601 cannot produce imitation-learning demonstrations, and the vendor's own buying guide flags it (plus a 12 V 2 A adapter) as the required add-on for anyone who intends to teleoperate. Second, it carries an unusually specific kinematic claim.

## The Pieper claim

Seeed describes the arm as *"featuring 6+1 degrees of freedom and adhering to the **Pieper criterion**, so it supports **analytical inverse kinematics** with transparent algorithms"* ([DLI course §2.1](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md)).

This is a real design constraint, not marketing language. **Pieper's criterion** — three consecutive revolute axes intersecting at a common point (the classic spherical wrist), or three parallel axes — is the condition under which a 6-DOF serial chain admits a **closed-form** inverse-kinematic solution. Arms that violate it require iterative numerical IK, which is slower, can fail to converge, and has no guarantee of finding all solution branches. For a leader arm whose whole job is to map a human's pose onto a follower at 30 Hz inside a recording loop, closed-form IK is the difference between a deterministic mapping and a solver that occasionally stalls mid-episode.

It also matters for **[real-to-sim](../concepts/robotics/real-to-sim-to-real.md) parity**: the same leader arm drives both the physical B601 and the simulated B601 inside [Isaac Sim](nvidia-isaac-sim.md) (over UDP), so an analytically identical IK on both sides removes one source of sim/real divergence before physics is even involved.

## In the reBot pipeline

- Connects over **USB-UART** at `/dev/ttyUSB*`; LeRobot type `rebot_arm_102_leader`, calibrated with `lerobot-calibrate --teleop.type=rebot_arm_102_leader`.
- Drives the real follower via `lerobot-teleoperate`, and the simulated follower via a LeRobot Python bridge over **UDP `127.0.0.1:5005`** into Isaac Sim.
- Provides only manual control commands — in the sim path the simulated arm executes no autonomous trajectory; the human is the entire policy during collection.
- Sold as **"Star Arm 102 for reBot B601-DM & RS Leader Arm"**, i.e. one leader serves both follower variants.

> [!note] Naming
> The course text calls it both "Star Arm 102" and "reBot Arm 102 Leader"; the LeRobot package is `lerobot-teleoperator-rebot-arm-102` and the robot type is `rebot_arm_102_leader`. Same device.

## Related

- [reBot Arm B601](rebot-arm-b601.md) — the follower it drives
- [Seeed Studio](seeed-studio.md) — vendor
- [LeRobot](lerobot.md) — the teleoperation and recording framework
- [SO-ARM101](so-arm101.md) — the leader/follower pattern one tier down (SO-101 leader + follower pairs)

## Mentioned in

- [A Sim-to-Real VLA Pipeline with Seeed reBot Arm and NVIDIA Isaac](../sources/seeed-nvidia-dli-rebot-sim-to-real-course.md) — the leader arm in the data-collection rig; the Pieper claim
- [reBot Arm B601-DM Bundle with Jetson Thor](../sources/seeed-rebot-arm-b601-dm-thor-bundle.md) — sold as a $200 add-on
