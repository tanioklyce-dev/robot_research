---
title: OpenArm
type: entity
subtype: robot
created: 2026-09-13
updated: 2026-09-13
sources: 4
tags: [robot, robot-arm, bimanual, 7-dof, open-hardware, quasi-direct-drive, damiao, bilateral-teleoperation, force-feedback, evaluation-cell, lerobot, dora, enactic, wowrobo]
---

**OpenArm** — an open-hardware, human-scale **7-DOF arm** (usually bought as a bimanual pair) from [Enactic](enactic.md) (Japan), built on [Damiao](damiao.md) quasi-direct-drive CAN-FD actuators with **4.1 kg nominal / 6.0 kg peak payload** (end-effector included), sold assembled by a directory of manufacturers led by the certified [WowRobo](wowrobo.md) at **$6,500 per bimanual system**, or built from MISUMI/MEVIY/JLCPCB part lists under CERN-OHL-S. Version 2.0 (hardware tag 2026-09-09) adds an in-hand-camera gripper, the **OpenArm Cell** evaluation enclosure and the motorless **KER** leader arm. Primary: [docs.openarm.dev](../sources/openarm-docs.md), [GitHub](../sources/openarm-github.md).

## Lineage and versions

| Release | Date | What |
|---|---|---|
| 0.1 – 0.3 | Feb–May 2025 | early public releases |
| 1.0 (hardware 1.0.0) | 2025-07-23 | 7 DOF, linkage gripper (88 mm), MISUMI base; the arm UME bought from WowRobo at $5,200 |
| 1.1 | 2025-10-31 / 11-19 | *"OpenArm 01: Release No.2"*; WowRobo's V1.1 at $5,400 |
| **2.0** | 2026-09-09 | compact gripper with in-hand camera, replaceable fingers; OpenArm Cell; KER (design finalizing); Dora-based software stack; docs reorganized |

## Specifications (vendor)

- **Motors**: DM-J4310-2EC (3 / 7 Nm), DM4340 (9 / 27 Nm, 40:1 — not QDD), DM-J8009P-2EC (20 / 40 Nm); 14-bit magnetic encoders; CAN-FD.
- **Structure**: aluminium + stainless, MISUMI-frame pillars, M6-tapped base, mechanical joint limits; proportions of a 160–165 cm person.
- **Teleop**: unilateral and **bilateral force-feedback** leader–follower (≥500 Hz loop, tanh friction model) from the teleop package; VR in Isaac Lab only, so far.
- **Data**: native dataset format with **joint torque** recorded; converts to LeRobot v2.1/v3.0; Dora dataflow at 250 Hz with a documented policy-server contract; five-camera default rig (ceiling, head ×2, wrist ×2).
- **Simulation**: Isaac Lab (official upstream integration; reach / lift / drawer envs), MuJoCo MJCF.
- **Cell**: ~100 kg, ~480 W, 300 mm Z-axis, area-sensor reach-in stop, zero-position calibration jig.
- **KER**: 1.7 kg, links at 70%, 16 absolute encoders, 1:1 mapping with no retargeting; $2,599.
- **Not documented**: accuracy, repeatability, power draw, any policy success rate.

## Where it appears in this wiki

- **[UME](ume.md)** (Ant Group + Stanford) evaluated its $1,900 torque-feedback exoskeleton on a *"WowRobo OpenArm 1.0 bimanual, $5,200"* and retargets to a 7-DoF OpenArm — the upstream design, from its certified manufacturer.
- **[Yuri](yuri.md)** ([Sensori Robotics](sensori-robotics.md)) is built on *"OpenArm+"*, an extended-reach derivative; Sensori is not on Enactic's manufacturer list, so it is a fork, not a channel.
- Between them and this page, OpenArm is the wiki's de-facto **open 7-DOF tier** above the [SO-ARM101](so-arm101.md) (5+1 DOF, ~$120 arm) and below the [Franka](franka-panda.md) (7 DOF, ~$30k) — with the payload (4.1 kg) closer to the Franka's 3 kg than to the SO-101's few hundred grams.

## Why it matters

- **A bilateral force-feedback rig you can buy.** [FACTR](../sources/factr-paper.md) built one for ~$1,230 on top of a torque-sensing Franka; OpenArm ships bilateral control on QDD motors whose current gives the torque. The [contact-rich](../concepts/robotics/contact-rich-manipulation.md) thread's argument that force data is scarce meets a platform that records torque by default.
- **Reproducible evaluation as hardware.** The Cell is the first *product* in this wiki built around the [policy-evaluation](../concepts/robotics/robot-policy-evaluation.md) complaint that success rates do not transfer between labs. No published Cell results yet.
- **The distribution model**: copyleft CAD plus a vendor directory with quality tiers, and a warning about an incompatible clone ("OpenArmX Pro Max"). This is what "open arm standard" looks like in practice.

## Related

- [Enactic](enactic.md) — the company. [WowRobo](wowrobo.md) — certified manufacturer. [Damiao](damiao.md) — motors.
- [SO-ARM101](so-arm101.md), [AgileX Piper](agilex-piper.md), [xArm 7](xarm-7.md), [Franka Panda](franka-panda.md) — neighbouring tiers.
- [Robot platforms comparison](../syntheses/platforms/robot-platforms-comparison.md), [Open-source robot AI projects](../syntheses/platforms/open-source-robot-ai-projects.md).

## Mentioned in

- [OpenArm documentation](../sources/openarm-docs.md) — the primary.
- [OpenArm GitHub](../sources/openarm-github.md) — repo family, stats, releases.
- [UME project page](../sources/ume-project-page.md), [UME paper](../sources/ume-paper.md) — evaluation platform (WowRobo OpenArm 1.0).
- [Sensori Robotics — Yuri](../sources/sensori-robotics-yuri.md) — the OpenArm+ derivative.

## Open questions / TBD

- Accuracy, repeatability, power; measured bilateral loop rate.
- Any real-hardware policy result, and any Cell-based comparison between labs.
- What OpenArm+ changes relative to upstream.
