---
title: RTAB-Map
type: entity
subtype: software-framework
created: 2026-08-13
updated: 2026-08-13
sources: 5
tags: [rtab-map, slam, rgbd, loop-closure, graph-slam, ros2, navigation, xlerobot, introlab]
---

**RTAB-Map** (Real-Time Appearance-Based Mapping) — a **graph-based RGB-D / stereo / LiDAR SLAM** library from IntRoLab (Université de Sherbrooke), built around an **appearance-based loop-closure detector** with a memory-management scheme that bounds the map so loop-closure stays real-time on long runs. [introlab/rtabmap](https://github.com/introlab/rtabmap) — **3,948★ / 950 forks**, C++, created 2014, actively pushed.

## Why it matters in this wiki

It is the **navigation half of the wiki's only measured onboard-Jetson XLeRobot build**. [Cutting the Cord](../sources/cutting-the-cord-untethered-xlerobot.md) (Correll lab) runs **RealSense D435 + RTAB-Map in localization-only mode + [Nav2](nav2.md)** on a Jetson Orin Nano Super inside a $1,202 robot — which is why the [XLeRobot bring-up plan](../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md) treats navigation as the *least* risky leg rather than the hardest.

**Localization-only mode is the load-bearing detail.** Map once offline, then at runtime the robot localizes against the saved map instead of growing it — far cheaper, and it removes the drift accumulation that makes long-session SLAM fragile on a cheap platform.

> [!note] Why RGB-D SLAM and not LiDAR, on this class of robot
> The arm work needs depth anyway, so a single RGB-D camera serves both perception and navigation — which is what makes the D435/D435i the right single purchase for an [XLeRobot](xlerobot.md). The cost is that visual odometry drifts where 2-D LiDAR scan-matching would not, especially on a differential base slipping on carpet. Two mitigations the wiki has recorded: **an IMU** (the reason the [camera analysis](../syntheses/projects/xlerobot-camera-options-low-light.md) prefers the D435i over the D415), and **wheel odometry** — which XLeRobot has via its FeeTech absolute encoders and [Sourccey](sourccey.md) gave up with open-loop PWM wheels.

## The feed-forward challengers

[LingBot-Map](lingbot-map.md) ([Robbyant](robbyant.md), 16,471★) and [Niantic Spatial](niantic-spatial.md)'s ACE→feed-forward line are both attacking this problem **without per-scene optimization**: LingBot-Map folds *"long-range drift correction"* into a transformer via trajectory memory, with no loop-closure detector and no map to re-solve, and demonstrates a 25,000-frame walkthrough.

**For the [XLeRobot plan](../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md) RTAB-Map remains the right choice**, for a specific reason: it is the only option here with a **measured deployment on comparable hardware** ([Cutting the Cord](../sources/cutting-the-cord-untethered-xlerobot.md), Orin Nano Super), and LingBot-Map publishes **no edge latency** and does not describe relocalization against a prior map — which is precisely what localization-only mode provides. Revisit if that changes.

## Related

- [Nav2](nav2.md) — the planner it feeds · [ROS 2](ros2.md)
- [Cutting the Cord](../sources/cutting-the-cord-untethered-xlerobot.md) — the measured XLeRobot precedent
- [XLeRobot bring-up plan](../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md) · [XLeRobot camera options](../syntheses/projects/xlerobot-camera-options-low-light.md)
- [GTSAM](gtsam.md) — the factor-graph optimization underneath this class of SLAM back-end
- [DimOS](dimos.md) — solves the same problem with its own voxel-map + GTSAM pose-graph stack instead

## Open questions

- **No specs read here** — no first-hand source is ingested; everything comes from Cutting the Cord's methods section and the repo description. Loop-closure recall, CPU/GPU cost on Orin-class hardware, and map size limits are all unestablished.
- License reads `NOASSERTION` on the GitHub API (the project is generally BSD) — unconfirmed.

## Mentioned in

- [Cutting the Cord: System Architecture for Low-Cost, GPU-Accelerated Bimanual Mobile Manipulation](../sources/cutting-the-cord-untethered-xlerobot.md)
- [LingBot-Map — Geometric Context Transformer for Streaming 3D Reconstruction (Robbyant, 2026)](../sources/lingbot-map-github.md)
- [Niantic Spatial — research page, product line, and Scaniverse](../sources/niantic-spatial-research.md)
- [Niantic Spatial, Flexion, and NVIDIA: Closing the Sim2Real Gap for Humanoids (Jul 2026)](../sources/niantic-flexion-nvidia-sim2real.md)
- [On the Limits of Pseudo Ground Truth in Visual Camera Re-localisation (Brachmann, Humenberger, Rother, Sattler — ICCV 2021)](../sources/pseudo-ground-truth-paper.md)
