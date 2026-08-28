---
title: Isaac ROS
type: entity
subtype: software-framework
created: 2026-06-13
updated: 2026-08-17
sources: 6
tags: [isaac-ros, nvidia, ros2, perception, gpu, jetson, thor, robotics]
---

**Isaac ROS** — NVIDIA's collection of **GPU-accelerated ROS 2 packages** ("GEMs") for robot perception, manipulation and navigation. It brings hardware-accelerated perception (3D mapping, stereo/depth, visual SLAM, AprilTag detection, DNN inference) into the ROS 2 ecosystem.

> [!warning] Correction 2026-08-17 — Isaac ROS 4.x dropped Jetson Orin entirely
> This page previously described Isaac ROS as running "on Jetson edge hardware," which was written from a JetPack 6 / Orin recipe and is no longer how the product is scoped. Per the **[supported-platform table](../sources/isaac-ros-release-notes-and-platforms.md)**, the *only* combinations NVIDIA tests and supports are **Jetson Thor (T5000/T4000) on JetPack 7.1**, **x86_64 on Ubuntu 24.04**, and **DGX Spark**. No Orin appears — not under JetPack 6, not under JetPack 7.

## Current release and supported platforms

**Isaac ROS 4.5.0** (2026-07-06) is current ([release notes and platforms](../sources/isaac-ros-release-notes-and-platforms.md)).

| Platform | Hardware | Software | Storage |
|---|---|---|---|
| Jetson | **Thor T5000 / T4000** | **JetPack 7.1** (= Jetson Linux R38.4) | 128+ GB NVMe |
| x86_64 | Ampere+ GPU, 8 GB+ VRAM | Ubuntu 24.04, CUDA 13.0+, driver 580+ | 32+ GB |
| DGX | [DGX Spark](dgx-spark.md) | DGX OS 7.2.3 | 32+ GB |

- **ROS 2 distro: Jazzy.** All 4.x packages are designed and tested against Jazzy; the 3.x line was Humble. Moving from 3.2 to 4.x is a distro migration, not an upgrade.
- The table is explicitly exhaustive — "the only hardware and software combinations that Isaac ROS tests and officially supports" — with a hedge that `cuda-compat`-style utilities *may* let users run elsewhere.

## The Orin cliff

**An [Orin](jetson-orin-nano.md)-class robot's terminal supported configuration is Isaac ROS 3.2 (Update 1+, Jan 2025) on JetPack 6.1/6.2, Ubuntu 22.04, CUDA 12.6, ROS 2 Humble.** That stack has been frozen since early 2025.

This is the decisive constraint for anything in this wiki that pairs an Orin NX / Orin Nano with GPU-accelerated ROS perception — see [Jetson onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md). It cuts both ways at the [JetPack](jetpack.md) 6 → 7 decision:

- **Stay on JetPack 6.2** → keep Isaac ROS 3.2, lose everything in 4.x and every JetPack 7 platform improvement.
- **Move to JetPack 7.2** → gain the unified Orin/Thor toolchain, lose Isaac ROS outright (the [7.2 release page](../sources/nvidia-jetpack-7-2-release.md) lists it "Coming soon").

There is no configuration in which an Orin runs a current Isaac ROS.

> [!note] "Coming soon" understates it
> The JetPack 7.2 release page's *Coming soon* reads as a scheduling note about one BSP release. The Isaac ROS primary shows a **generational break**: 4.0 (Oct 2025) launched *as* a Thor product and no 4.x release has mentioned Orin since. Whether NVIDIA re-adds Orin is an open product question, not a dated commitment.

## Release lineage

| Line | Platform | JetPack | Ubuntu / CUDA | ROS 2 |
|---|---|---|---|---|
| **4.x** (4.0 2025-10-24 → 4.5.0 2026-07-06) | **Thor**, x86_64, DGX Spark | 7.0 → **7.1** | 24.04 / CUDA 13 | **Jazzy** |
| 3.x (3.0 2024-05-30 → 3.2 Update 4) | **Orin**, x86_64 | 6.0 → **6.1/6.2** | 22.04 / CUDA 12.6 | Humble |
| 2.x (2023) | Orin, Xavier | 5.x | 20.04/22.04 | Humble |

Milestones: **4.0** added Thor + JetPack 7.0 (tested with Isaac Sim 5.1); **4.2** added [DGX Spark](dgx-spark.md), JetPack 7.1 and the Thor T4000 SKU; **4.4** refactored `isaac_manipulator` → `isaac_ros_manipulation` and added `isaac_ros_physical_ai` / `isaac_ros_robots`; **4.5** sun-set the GXF implementation inside NITROS and added an **MCAP-to-[LeRobot](lerobot.md) converter** and Unitree G1 [GR00T](nvidia-groot.md) deploy workflows.

## Components seen in this wiki

- **[nvblox](nvblox.md)** — GPU 3D volumetric mapping from RGB-D/stereo depth. The wiki's exposure is via a Seeed [`jetson-examples`](jetson-examples.md) recipe pinned to **Orin + JetPack 6.x**, i.e. the 3.x line.
- `isaac_ros_physical_ai`, `isaac_ros_data_tools` (MCAP→LeRobot), `isaac_ros_teleop` — 4.x-only, Thor/x86/Spark.

## Related

- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) / [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — simulation + RL siblings.
- [ROS 2](ros2.md) — the middleware Isaac ROS extends.
- [JetPack](jetpack.md) — the Jetson software base Isaac ROS containers target.
- [Jetson Thor](jetson-thor.md) — the only Jetson Isaac ROS 4.x supports.

## Mentioned in

- [Isaac ROS — release notes and supported platforms](../sources/isaac-ros-release-notes-and-platforms.md)
- [Seeed jetson-examples — nvblox recipe (README)](../sources/seeed-jetson-examples-nvblox.md)
- [NVIDIA JetPack 7.2 with Jetson Linux 39.2](../sources/nvidia-jetpack-7-2-release.md)
