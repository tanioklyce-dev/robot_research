---
title: Isaac ROS NVBlox (nvblox)
type: entity
subtype: software-framework
created: 2026-06-13
updated: 2026-08-17
sources: 2
tags: [nvblox, isaac-ros, nvidia, 3d-mapping, perception, gpu, robotics, navigation]
---

**Isaac ROS NVBlox** — NVIDIA's high-performance, **GPU-accelerated 3D mapping framework** for real-time robotic perception. It ingests **depth from RGB-D or stereo cameras** and fuses it into a volumetric 3D scene representation, rather than relying on monocular depth estimation ([Seeed jetson-examples nvblox README](../sources/seeed-jetson-examples-nvblox.md)). It is part of the [Isaac ROS](isaac-ros.md) perception stack and is upstreamed at [NVIDIA-ISAAC-ROS/isaac_ros_nvblox](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox).

## What it does

- Builds a real-time **volumetric map** (TSDF-class reconstruction → mesh + occupancy/ESDF outputs) on the GPU, designed to feed downstream **navigation** (e.g. Nav2 cost-maps) and obstacle avoidance.
- Depth-driven: requires an **RGB-D or stereo** sensor. The Seeed recipe wires it to an **[Orbbec Gemini2](orbbec.md)** camera ([Seeed jetson-examples nvblox README](../sources/seeed-jetson-examples-nvblox.md)).

## Deployment (Seeed reComputer recipe)

Seeed packages nvblox as a one-command [`jetson-examples`](../sources/seeed-jetson-examples-nvblox.md) recipe on its [reComputer](seeed-studio.md) Jetson carriers:

- Requirements: **Jetson Orin**, Ubuntu 22.04, [JetPack 6.x](jetpack.md), Docker + NVIDIA Container Runtime, Orbbec Gemini2, ~60 GB storage.

> [!note] Those requirements pin this recipe to the Isaac ROS **3.x** line
> Orin + Ubuntu 22.04 + JetPack 6.x is the [Isaac ROS](isaac-ros.md) 3.2 configuration. **Isaac ROS 4.x (current: 4.5.0) dropped Orin from its supported-platform list entirely** — nvblox in 4.x is Thor / x86_64 / DGX Spark only, on Ubuntu 24.04 and ROS 2 Jazzy ([release notes and platforms](../sources/isaac-ros-release-notes-and-platforms.md)). The Seeed recipe still works on the stack it targets; it is simply no longer on the current line, and moving that Orin to [JetPack 7.2](jetpack.md) removes Isaac ROS rather than upgrading it.
- `reComputer run nvblox` (full), with `NVBLOX_MODE=prepare` / `NVBLOX_MODE=run` to split image-build from demo-launch, and `reComputer clean nvblox` to tear down.
- A deeper manual guide exists for **AGX Orin** at the [Seeed Wiki deploy page](https://wiki.seeedstudio.com/deploy_nvblox_jetson_agx_orin/).

## Related

- [Isaac ROS](isaac-ros.md) — parent perception stack.
- [Orbbec](orbbec.md) — the RGB-D camera used in the Seeed demo.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) / [Isaac Lab](nvidia-isaac-lab.md) — sibling NVIDIA robotics platforms (sim side).
- [Seeed Studio](seeed-studio.md) — reComputer carrier vendor that packages the recipe.

## Mentioned in

- [Seeed jetson-examples — nvblox recipe (README)](../sources/seeed-jetson-examples-nvblox.md)
