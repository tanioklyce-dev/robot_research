---
title: Yuri (Sensori Robotics)
type: entity
subtype: robot
created: 2026-07-13
updated: 2026-07-13
sources: 2
tags: [robot, bimanual, mobile-manipulation, manipulator, physical-ai, teleoperation, lerobot, jetson, vla]
---

**Yuri** — a **dual-arm bimanual manipulation platform** for Physical AI / [VLA](../concepts/learning/vla-models.md) research, made by [Sensori Robotics](sensori-robotics.md) (Southlake, TX). Sold as an integrated, supported system with a day-one data-collection + policy-training stack, in two configurations: **Yuri Desktop** (benchtop) and **Yuri Mobile** (arms on a wheeled OpenBase for room-scale autonomy) ([company site](../sources/sensori-robotics-yuri.md)).

> [!note] "Humanoid" is a stretch
> Sensori's marketing calls it a "dual-arm humanoid," but with two arms on a table or wheeled base and no legs, Yuri is a **bimanual (mobile) manipulator** — the same class as [Reachy 2](reachy.md), [XLeRobot](xlerobot.md), and [Mobile ALOHA](aloha.md), not a legged humanoid like G1 / Optimus.

## Specs (vendor claims)

| Axis | Yuri |
|---|---|
| Arms | 2× **7-DOF** ("14-DOF OpenArm+"), parallel grippers, **backdrivable** joints, real-time **torque feedback** |
| Cameras | 2× wrist RGB + head **Intel RealSense D435i** (depth + IMU) |
| Compute | **NVIDIA Jetson AGX Orin 64 GB (275 TOPS)**, onboard |
| Control | **ROS 2 Humble**, **CAN-FD** arm bus |
| Teleop | **OpenLeader** force-feedback leader arms (**bilateral feedback included**); **Meta Quest 3/3S** for spatial whole-body capture; local Wi-Fi |
| Mobility (Mobile) | **OpenBase** directional wheeled base; hot-swap battery; hardware + wireless e-stop |
| Reach | Extended reach "optimized for bins and tabletops"; **adjustable arm height** |

## Software stack

- Browser-based setup web app; calibration + recording pre-integrated.
- **[LeRobot](lerobot.md)-format dataset recording** — synchronized cameras / joints / grippers / base state.
- **MCAP** logging + **Foxglove** visualization.
- Sim assets: **URDF/MJCF** for [MuJoCo](mujoco.md), [Isaac Lab](nvidia-isaac-lab.md), [Genesis](genesis.md).
- VLA policy support: **[GR00T](nvidia-groot.md), π0.x ([Physical Intelligence](physical-intelligence.md)), X-VLA, SmolVLA.**

## Open hardware

OpenArm+ (arm) and OpenBase (base) are released openly at github.com/SensoriRobotics + docs.openarm.dev.

## Where it fits

Yuri's headline differentiators are **out-of-the-box bilateral force-feedback teleoperation** and an **integrated, supported, US-made** package — versus the self-assembled [LeRobot](lerobot.md)-ecosystem kits. Its natural comparison is [Mobile ALOHA](aloha.md) (also bimanual + whole-body/leader teleop, $32k) on the research side and [XLeRobot](xlerobot.md) ($660–1.3k) on the educational side; Yuri's price is quote-only but the AGX Orin 64 GB + dual torque-controlled 7-DOF arms place it in the research tier. See [robot platforms comparison](../syntheses/platforms/robot-platforms-comparison.md).

## Open questions

- Price, payload, reach (in cm), and leader-arm mechanics are not published.
- Team and funding undisclosed.

## Mentioned in

- [Sensori Robotics — Yuri (company site)](../sources/sensori-robotics-yuri.md)
