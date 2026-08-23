---
title: NORI A3
type: entity
subtype: robot
created: 2026-08-23
updated: 2026-08-23
sources: 2
tags: [nori, home-robot, bimanual, mobile-manipulator, consumer-robotics, affordable-hardware, raspberry-pi-5, lidar, skills-marketplace]
---

**NORI A3** — a **bimanual wheeled home manipulator** from [Nori Robotics](nori-robotics.md), **$1,688 full price with no deposit**, assembled in San Francisco, shipping Fall 2026 ([product site](../sources/nori-robotics-site.md)). Two 7+1-DOF arms on a torso that raises and lowers on a lift column, a 2D LiDAR for navigation, four RGB cameras, and a laptop app called **Nori Lab** for training and operation.

Marketed tasks: kitchen help, tidying, fetching from the fridge, loading dishes, folding clothes, pouring ingredients. **No success rates, benchmarks or autonomy claims accompany any of them.**

## Specs

| | | Source |
|---|---|---|
| **Price** | **$1,688**, full, no deposit | [site](../sources/nori-robotics-site.md) |
| **Ships** | Fall 2026 (first unit reportedly July 2026 — [contradiction](../sources/nori-robotics-site.md)) | [site](../sources/nori-robotics-site.md) |
| **Arms** | 2 × **7+1 DOF**, **1.5 kg payload per arm** | [site](../sources/nori-robotics-site.md) |
| **Total DOF** | **19** | [YC](../sources/nori-robotics-yc-profile.md) |
| **Linear lift** | **55 kg** (torso column — *not* arm payload) | [YC](../sources/nori-robotics-yc-profile.md) |
| **Cameras** | 4 × **720p RGB**, ≤30 fps — grippers, head, neck | both |
| **LiDAR** | 12 m range, 8–12 Hz, 0.72° at 10 Hz | [site](../sources/nori-robotics-site.md) |
| **Audio** | mic array + speaker, **full-duplex speech** | [YC](../sources/nori-robotics-yc-profile.md) |
| **Compute** | **[Raspberry Pi 5](raspberry-pi-5.md), 4 GB** | [YC](../sources/nori-robotics-yc-profile.md) |
| **Battery** | 6–8 hours | [site](../sources/nori-robotics-site.md) |
| **Software** | **Nori Lab** laptop app — train, operate, manage | [site](../sources/nori-robotics-site.md) |
| **Skills** | **Skills Marketplace** — train at home, share anywhere | [site](../sources/nori-robotics-site.md) |
| Height / mass / reach / base type | **not published** | — |

> [!warning] "Lifts 55 kg" is the column, not the hands
> Secondary launch coverage reports the A3 "can lift 55 kg." Both figures are real and mean different things: **55 kg** is the vertical lift of the torso column; **1.5 kg per arm** is what it can pick up. Quote 1.5 kg for anything involving the grippers.

## Reading the spec sheet

**Two 7-DOF arms at this price is the surprise.** 7 DOF gives a redundant arm — a null space to exploit for obstacle avoidance and posture, and no wrist-singularity trap. The rest of this wiki's sub-$2k tier is 5-DoF ([SO-101](so-arm101.md), [XLeRobot](xlerobot.md), [Sourccey](sourccey.md)) or 6-DoF ([Piper](agilex-piper.md)), and the wiki's [5-DoF analysis](../syntheses/projects/five-dof-arms-in-robotwin.md) spends its length on what those arms *cannot* reach. If the A3's arms are genuinely 7-DOF and repeatable, its **kinematic** story is better than anything at the price. Whether 1.5 kg and hobby-grade actuation deliver it is untested.

**The sensing is thin for manipulation.** Four RGB cameras and a planar LiDAR means **no metric depth at manipulation range** — no stereo pair, no RGB-D, no ToF is claimed. Wrist cameras on both grippers is correct for imitation learning and monocular policies do work ([ACT](act.md), [SmolVLA](smolvla.md)). But it forecloses the classical [6-DOF grasp generation](../concepts/robotics/six-dof-grasp-generation.md) path, which needs a segmented point cloud, and it means every failure mode has to be learned rather than measured.

**The Pi 5 4 GB decides the architecture.** [Sourccey](sourccey.md) uses the same board and cannot run its own 0.9 B [X-VLA](x-vla.md) policies onboard. 4 GB is also the SKU that rules out an 8 GB [Hailo](hailo.md) AI HAT+ 2. So "Nori Lab, the laptop app" is load-bearing: the A3 is a **thin client that thinks on your laptop**. Reasonable at the price, unstated in both primaries.

## Open questions

- What is a marketplace "skill" — a trajectory, a checkpoint, a script? Determines whether the flywheel is real.
- Does the robot do anything with no laptop on the network?
- 19 DOF does not itemise cleanly against 16 arm + 1 lift + head. What is the base?
- No depth sensor and no named policy: what actually closes the loop on a grasp?

## Related
- [Nori Robotics](nori-robotics.md) · [Sourccey](sourccey.md) · [Zeroth M1](zeroth-m1.md) · [XLeRobot](xlerobot.md) — the sub-$2k tier.
- [Raspberry Pi 5](raspberry-pi-5.md) · [Hailo](hailo.md)
- [Consumer robotics value chain](../syntheses/society/consumer-robotics-value-chain.md)

## Mentioned in
- [Nori Robotics — NORI A3 product site](../sources/nori-robotics-site.md)
- [Nori Robotics — Y Combinator company profile (S26)](../sources/nori-robotics-yc-profile.md)
