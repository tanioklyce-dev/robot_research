---
title: Isaac ROS — Release Notes and Supported Platforms (docs)
type: source
url: https://nvidia-isaac-ros.github.io/releases/index.html
author: NVIDIA Corporation
published: 2026-07-06 (Isaac ROS 4.5.0, latest entry at ingest)
ingested: 2026-08-17
venue: NVIDIA Isaac ROS documentation
tags: [isaac-ros, nvidia, ros2, jetson, thor, orin, jetpack, dgx-spark, jazzy, compatibility]
---

## Summary

The Isaac ROS documentation's **release-notes archive** plus the **Supported Platforms** table from its Getting Started page — together the primary for "what hardware and software does Isaac ROS actually run on." Ingested during the 2026-08-17 Jetson version sweep to settle a question the [JetPack 7.2 release page](nvidia-jetpack-7-2-release.md) could only half-answer.

The headline: **Isaac ROS 4.x is not an Orin product.** The supported-platform table lists Jetson Thor, x86_64, and DGX Spark — no Orin of any generation, on any JetPack. The last Orin-supporting line is **3.2 (December 2024, updated through Feb 2025)**. This is a considerably stronger statement than the "Isaac ROS: Coming soon" cell on the JetPack 7.2 release page, which reads as a scheduling note and is in fact a generational break.

## Key claims

### Supported Platforms table (Getting Started)

Prefaced with: "The platforms defined in this table are **the only hardware and software combinations that Isaac ROS tests and officially supports.** Users may be able to rely on backward and forward compatibility utilities like `cuda-compat` to use Isaac ROS on other platform versions."

| Platform | Hardware | Software | Storage |
|---|---|---|---|
| **Jetson** | **Jetson Thor (T5000 and T4000)** | **JetPack 7.1** | 128+ GB NVMe SSD |
| **x86_64** | Ampere or higher NVIDIA GPU, 8 GB+ RAM | Ubuntu 24.04, CUDA 13.0+, driver 580+ | 32+ GB |
| **DGX** | DGX Spark | DGX OS 7.2.3 | 32+ GB |

- **ROS support**: "All Isaac ROS packages are designed and tested to be compatible with **ROS 2 Jazzy**." (The 3.x line was Humble.)
- Install verification step: `cat /etc/nv_tegra_release` should report **`R38 (release), REVISION: 4.0`** — i.e. JetPack 7.1 = **Jetson Linux R38.4**, the Thor BSP line, not r39.2.

### Release timeline (release-notes archive)

| Release | Date | Platform-relevant contents |
|---|---|---|
| **4.5.0** | **2026-07-06** | Sun-setting GXF in NITROS; CUDA streaming for NITROS; cuMotion 1.1.0; **MCAP-to-LeRobot converter**; Unitree G1 recording + GR00T deploy workflows; Fast-FoundationStereo |
| 4.4.0 | 2026-04-30 | `isaac_manipulator` → `isaac_ros_manipulation`; new `isaac_ros_teleop` (XR headset); new `isaac_ros_physical_ai` and `isaac_ros_robots` repos |
| 4.3.0 | 2026-03-23 | `isaac_ros_sipl_camera` — SIPL integration for Camera-over-Ethernet |
| **4.2.0** | **2026-02-19** | **Support for DGX Spark; support for JetPack 7.1; support for Thor T4000 SKU** |
| 4.1.0 | 2026-02-02 | Docker-optional Virtual Environment and Bare Metal modes; nvblox Lidar dynamics |
| **4.0.0** | **2025-10-24** | **Support for Jetson AGX Thor; support for JetPack 7.0 / Ubuntu 24.04 on CUDA 13.0; tested with Isaac Sim 5.1** |
| 3.2 Update 1 | 2025-01-16 | **Support for JetPack 6.2 and Jetson Orin Nano Super** |
| 3.2 | 2024-12-10 | Support for JetPack 6.1 / Ubuntu 22.04 on CUDA 12.6 (only); Isaac Sim 4.2 |
| 3.1 | 2024-09-26 | — |
| 3.0.0 / 3.0.1 | 2024-05-30 / 2024-06-14 | JetPack 6.0 / Ubuntu 22.04 on CUDA 12.2 |

> [!warning] The Orin line ends at Isaac ROS 3.2
> No 4.x release note mentions Orin, and Orin appears nowhere in the supported-platform table. **An Orin robot's terminal supported Isaac ROS configuration is 3.2 (Update 4) on JetPack 6.1/6.2, Ubuntu 22.04, CUDA 12.6, ROS 2 Humble** — a stack frozen since early 2025. Everything in 4.x (cuMotion 1.1, the manipulation refactor, XR teleop, `isaac_ros_physical_ai`, the MCAP→LeRobot converter, GR00T deploy workflows) is Thor / x86 / DGX Spark only.

### Selected 4.5.0 limitations worth knowing before committing

- DNN stereo depth (ESS, FoundationStereo, Fast-FoundationStereo) "may intermittently fail to produce disparity or point cloud output, drop frames, or show no RViz output" with RealSense, ZED, or Isaac Sim, due to a synchronization issue in the decoder node.
- **Fast-FoundationStereo is a research model, not for commercial use**; use FoundationStereo for commercial applications.
- On **DGX Spark**, the H.264 encoder may fail to open the V4L2 encoder device.
- Stale TensorRT engine-cache failures on Thor were *fixed* in 4.5.0 (nvbugs/6032663).
- RealSense SDK stability on JetPack 7 was a 4.x issue addressed by following the RealSense setup tutorial.

## Entities mentioned

- [Jetson AGX Orin](../entities/jetson-agx-orin.md) — an Orin module, absent from the 4.x supported-platform table.
- [Jetson Orin NX](../entities/jetson-orin-nx.md) — an Orin module, and Orin is absent from the 4.x supported-platform table.
- [Isaac ROS](../entities/isaac-ros.md)
- [Isaac ROS NVBlox](../entities/nvblox.md)
- [Jetson Thor](../entities/jetson-thor.md)
- [JetPack](../entities/jetpack.md)
- [DGX Spark](../entities/dgx-spark.md)
- [Jetson Orin Nano](../entities/jetson-orin-nano.md)
- [LeRobot](../entities/lerobot.md) — via the MCAP-to-LeRobot converter in 4.5.0
- [Isaac GR00T](../entities/nvidia-groot.md) — via the G1 deploy workflow
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md)
- [ROS 2](../entities/ros2.md)

## Concepts touched

- Platform support matrices as a deployment constraint; the Humble → Jazzy distro break; GPU-accelerated ROS 2 perception.

## Open questions

- **Will Isaac ROS ever return to Orin under JetPack 7?** JetPack 7.2 brought Orin onto the JetPack 7 BSP, so the platform obstacle is gone; whether NVIDIA re-adds Orin to the tested matrix is a product decision with no public commitment found.
- **What breaks in practice if you run 4.x on an Orin anyway?** The table's `cuda-compat` sentence suggests it is not categorically impossible. Untested and unclaimed here.
- **Isaac Perceptor / Nova on Thor** — reported as not yet optimized for AGX Thor in a developer-forum thread about 4.1.0; not stated in the primary, so left as a secondary-sourced rumor.
