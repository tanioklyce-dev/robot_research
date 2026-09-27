---
title: Isaac ROS
type: entity
subtype: software-framework
created: 2026-06-13
updated: 2026-09-27
sources: 7
tags: [isaac-ros, nvidia, ros2, perception, gpu, jetson, thor, orin, lyrical, nitros, agent-skills, robotics]
---

**Isaac ROS** — NVIDIA's collection of **GPU-accelerated ROS 2 packages** ("GEMs") for robot perception, manipulation and navigation. It brings hardware-accelerated perception (3D mapping, stereo/depth, visual SLAM, AprilTag detection, DNN inference) into the ROS 2 ecosystem.

> [!warning] Correction 2026-09-27 — Orin is supported again (reverses the 2026-08-17 correction)
> From 2026-08-17 this page said *"Isaac ROS 4.x dropped Jetson Orin entirely"* and *"There is no configuration in which an Orin runs a current Isaac ROS."* That was true of 4.0–4.5 and stopped being true **the next day**: **Isaac ROS 4.6.0 (2026-08-18) "Added support for Jetson Orin" and "Added support for JetPack 7.2"** ([release notes](../sources/isaac-ros-release-notes-and-platforms.md)). The 4.x Orin gap was a **BSP gap** — Orin had no JetPack 7 until [JetPack 7.2](../sources/nvidia-jetpack-7-2-release.md) (2026-06-02) — not the generational break this page called it. The JetPack 7.2 page's *"Coming soon"* meant exactly what it said.

## Current release and supported platforms

**Isaac ROS 5.0.0** (2026-09-21, announced at ROSCon 2026) is current ([release notes and platforms](../sources/isaac-ros-release-notes-and-platforms.md); [announcement blog](../sources/nvidia-isaac-ros-5-0-blog.md)).

| Platform | Hardware | Software | Storage |
|---|---|---|---|
| Jetson | **Thor T5000 / T4000 and Jetson Orin** | **JetPack 7.2** (= Jetson Linux r39.2) | 128+ GB NVMe |
| x86_64 | Ampere+ GPU, 8 GB+ VRAM | Ubuntu 24.04, CUDA 13.2+, driver 595+ | 32+ GB |
| DGX | [DGX Spark](dgx-spark.md) | DGX OS 7.2.3 | 32+ GB |

- **ROS 2 distro: Lyrical Luth** (5.0). 4.x was **Jazzy**, 3.x **Humble** — each major line is a distro migration.
- The table is explicitly exhaustive — "the only hardware and software combinations that Isaac ROS tests and officially supports."
- **Which Orins**: the table says "Jetson Orin"; the setup guide walks through **AGX Orin**; performance results cover **AGX Orin and Orin Nano**; NVIDIA's blog says *"from entry-level Jetson Orin Nano to high-performance Jetson Thor."* **Orin NX** is covered by the family name and JetPack 7.2 but never named individually.

## The Orin path, as of 5.0

For an [Orin](jetson-orin-nx.md)-class robot the decision is now **JetPack 7.2 + Isaac ROS 4.6/5.0**, not a choice between two dead ends:

- **Stay on JetPack 6.2** → Isaac ROS 3.2 (Humble), frozen since early 2025. Still a legitimate choice for a working robot that should not be reflashed.
- **Move to JetPack 7.2** → Isaac ROS 4.6 (Jazzy) or 5.0 (Lyrical) with the full 4.x feature set: cuMotion 1.1, `isaac_ros_manipulation`, XR teleop, `isaac_ros_physical_ai`, the MCAP→[LeRobot](lerobot.md) converter, [GR00T](nvidia-groot.md) deploy workflows. Costs: a full reflash, the CSI connector/device-tree changes on third-party carriers, and — at 5.0 — the NITROS removal.

> [!note] What went wrong in the 2026-08-17 reading
> "No 4.x release note mentions Orin" was true and was read as intent. The simpler explanation — Isaac ROS 4.x targets JetPack 7, and Orin was not *on* JetPack 7 until 7.2 — fit the same evidence and predicted exactly what happened. Negative claims about a living support matrix have a shelf life; the release-notes source page now carries a `fetch_url` so the drift check can see it.

## Isaac ROS 5.0 (Sep 2026)

From the [release notes](../sources/isaac-ros-release-notes-and-platforms.md) and [announcement](../sources/nvidia-isaac-ros-5-0-blog.md):

- **NITROS is gone.** Rebuilt natively on ROS 2 Lyrical's **`rosidl::Buffer`** with a **CUDA buffer backend** — standard ROS messages whose array fields can live in GPU memory. NVIDIA contributed the interface to ROS Lyrical through the Open Source Robotics Alliance as a vendor-neutral mechanism, with CUDA as the only backend so far. The NITROS packages are removed; code that calls NITROS APIs needs **a source-level migration**.
- **[Agent skills](../concepts/agents/agent-skills.md)** in the open format — `isaac-ros-activate`, an early-access `migrate-node-to-rosidl-buffer` skill (an agent to help with the NITROS migration the release itself forces), setup and manipulation skills, a **FoundationStereo fine-tuning skill**, and more in the `nvidia/skills` catalog under "Physical AI." Plus "agent-ready documentation."
- **FoundationPose** as an agent-ready inference library (*"up to 5.5x faster"*); **pick-and-place** as a standalone skill usable outside Isaac ROS.
- `isaac_ros_gpu_partitioning` (CUDA MPS SM shares per ROS process — compute only, no memory isolation); `isaac_ros_visual_slam` renamed `isaac_ros_cuvslam`.
- Known regressions: DNN image encoder slower than 4.6; RealSense only in Docker mode; nvblox + D455 produces empty maps.

> [!note] Positioning
> 5.0 is the first Isaac ROS release whose headline is **agents as users of the SDK**, not a new perception GEM. It lines up with the [NemoClaw](nemoclaw.md) / [Nemotron](nemotron.md) agent stack and with the community [AgenticROS](agenticros.md) bridge, which NVIDIA now presents as RealSense-sponsored. The more consequential change for anyone with existing code is the quiet one: NITROS removal.

## Release lineage

| Line | Platform | JetPack | Ubuntu / CUDA | ROS 2 |
|---|---|---|---|---|
| **5.0** (2026-09-21) | **Thor, Orin**, x86_64, DGX Spark | **7.2** | 24.04 / CUDA 13.2 | **Lyrical** |
| **4.x** (4.0 2025-10-24 → 4.6.0 2026-08-18) | **Thor**, x86_64, DGX Spark; **+ Orin from 4.6** | 7.0 → 7.1 → **7.2** (4.6) | 24.04 / CUDA 13 | **Jazzy** |
| 3.x (3.0 2024-05-30 → 3.2 Update 4) | **Orin**, x86_64 | 6.0 → **6.1/6.2** | 22.04 / CUDA 12.6 | Humble |
| 2.x (2023) | Orin, Xavier | 5.x | 20.04/22.04 | Humble |

Milestones: **4.0** added Thor + JetPack 7.0 (tested with Isaac Sim 5.1); **4.2** added [DGX Spark](dgx-spark.md), JetPack 7.1 and the Thor T4000 SKU; **4.4** refactored `isaac_manipulator` → `isaac_ros_manipulation` and added `isaac_ros_physical_ai` / `isaac_ros_robots`; **4.5** sun-set the GXF implementation inside NITROS and added an **MCAP-to-[LeRobot](lerobot.md) converter** and Unitree G1 [GR00T](nvidia-groot.md) deploy workflows; **4.6** re-added **Jetson Orin** with **JetPack 7.2**, made Isaac Sim 6.0 the recommended version, and added Unitree G1 cloud control; **5.0** moved to Lyrical and removed NITROS.

## Components seen in this wiki

- **[nvblox](nvblox.md)** — GPU 3D volumetric mapping from RGB-D/stereo depth. The wiki's exposure is via a Seeed [`jetson-examples`](jetson-examples.md) recipe pinned to **Orin + JetPack 6.x**, i.e. the 3.x line.
- `isaac_ros_physical_ai`, `isaac_ros_data_tools` (MCAP→LeRobot), `isaac_ros_teleop` — 4.x+; on Orin from 4.6 (JetPack 7.2).
- **FoundationPose**, **FoundationStereo**, **cuMotion**, **cuVSLAM** — the perception/planning GEMs partners cite (Intrinsic, Ekumen, ROBOTIS, Seeed reBot Arm) in the [5.0 announcement](../sources/nvidia-isaac-ros-5-0-blog.md).

## Related

- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) / [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — simulation + RL siblings.
- [ROS 2](ros2.md) — the middleware Isaac ROS extends.
- [JetPack](jetpack.md) — the Jetson software base Isaac ROS containers target.
- [Jetson Thor](jetson-thor.md) — the only Jetson on Isaac ROS 4.0–4.5; shares the table with Orin from 4.6.
- [AgenticROS](agenticros.md) — the community ROS↔agent bridge NVIDIA features alongside 5.0.

## Mentioned in

- [Isaac ROS — release notes and supported platforms](../sources/isaac-ros-release-notes-and-platforms.md)
- [Seeed jetson-examples — nvblox recipe (README)](../sources/seeed-jetson-examples-nvblox.md)
- [NVIDIA JetPack 7.2 with Jetson Linux 39.2](../sources/nvidia-jetpack-7-2-release.md)
- [NVIDIA Isaac ROS 5.0 blog](../sources/nvidia-isaac-ros-5-0-blog.md) — agentic skills, ROS Lyrical, partner roll-call.
