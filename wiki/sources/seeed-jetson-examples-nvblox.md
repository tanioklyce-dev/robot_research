---
title: Seeed jetson-examples — nvblox recipe (README)
type: source
url: https://github.com/Seeed-Projects/jetson-examples/blob/main/reComputer/scripts/nvblox/README.md
author: Seeed Studio (Seeed-Projects)
published: 2025
ingested: 2026-06-13
local_path: null
venue: GitHub (Seeed-Projects/jetson-examples)
license: (repo) — see jetson-examples
format: README.md
tags: [seeed-studio, jetson, nvblox, isaac-ros, 3d-mapping, perception, orbbec, docker, recomputer, robotics]
---

## Summary

A one-command recipe in Seeed's **[`jetson-examples`](seeed-jetson-examples.md)** repo (the [`reComputer` example runner](../entities/jetson-examples.md)) for standing up **[Isaac ROS NVBlox](../entities/nvblox.md)** — NVIDIA's GPU-accelerated real-time 3D mapping framework — on a Jetson Orin device. The recipe wraps the heavy Isaac ROS / nvblox container setup behind `reComputer run nvblox`: it downloads a base Docker image archive, loads it, builds a derived image, prepares the ROS workspaces, and launches a **static [Orbbec Gemini2](../entities/orbbec.md) RGB-D mapping demo**. It is the "buy-the-carrier, run-one-command" path to a working volumetric-mapping demo on Seeed [reComputer](../entities/seeed-studio.md) hardware.

## Key claims

- **What nvblox is.** "[Isaac ROS NVBlox](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox) is a high-performance GPU-accelerated 3D mapping framework developed by NVIDIA for real-time robotic perception." It consumes **depth from RGB-D or stereo cameras** to build 3D scene representations, rather than relying on monocular depth estimation.
- **Hardware requirements:** NVIDIA **Jetson Orin** processor; **[Orbbec Gemini2](../entities/orbbec.md)** camera (or compatible Orbbec RGB-D device); ~**60 GB** free storage.
- **Software requirements:** **Ubuntu 22.04**; **[JetPack 6.x](../entities/jetpack.md)**; **Docker** with **NVIDIA Container Runtime**.
- **Install + run (full):**
  ```sh
  cd jetson-example/
  pip install .
  reComputer run nvblox
  ```
- **Two-phase mode** via the `NVBLOX_MODE` env var — separates the slow image build from the demo launch:
  - `NVBLOX_MODE=prepare reComputer run nvblox` — preparation only (download/load/build image, set up workspaces).
  - `NVBLOX_MODE=run reComputer run nvblox` — launch the demo after a prior prepare.
- **Cleanup:** `reComputer clean nvblox`.
- **Workflow internals:** downloads a base Docker image archive → loads it → constructs a derived image → prepares workspaces → launches a static Gemini2 mapping demonstration.
- **Connectivity debugger:** `bash reComputer/scripts/nvblox/scripts/debug_runtime_connectivity.sh`.
- **Deeper setup guide:** the [Seeed Wiki "deploy nvblox on Jetson AGX Orin" page](https://wiki.seeedstudio.com/deploy_nvblox_jetson_agx_orin/).

> [!note] Camera is Orbbec, not RealSense
> Upstream NVIDIA Isaac ROS nvblox examples commonly use Intel RealSense; this Seeed recipe is wired for the **Orbbec Gemini2** RGB-D camera. That matters for anyone cross-referencing the [XLeRobot low-light camera options](../syntheses/projects/xlerobot-camera-options-low-light.md) work — Orbbec is the assumed depth source here.

## Entities mentioned

- [jetson-examples / reComputer runner](../entities/jetson-examples.md) (parent repo: [source page](seeed-jetson-examples.md))
- [Isaac ROS NVBlox (nvblox)](../entities/nvblox.md)
- [Isaac ROS](../entities/isaac-ros.md)
- [Orbbec / Gemini2](../entities/orbbec.md)
- [Seeed Studio](../entities/seeed-studio.md) (reComputer)
- [JetPack](../entities/jetpack.md)
- [Jetson Thor](../entities/jetson-thor.md) / [Jetson Orin Nano](../entities/jetson-orin-nano.md) (Orin family context)

## Concepts touched

- GPU-accelerated **volumetric 3D mapping** (TSDF / occupancy / ESDF-class reconstruction for navigation) — depth-driven, not monocular.
- Container-packaged robot-perception deployment on edge (Docker + NVIDIA Container Runtime on JetPack).

## Open questions

- Which nvblox outputs does the demo expose (mesh / TSDF / ESDF cost-map for Nav2)? The README describes a "static mapping demo" but not the downstream navigation hook.
- Compute footprint: which Orin tier is the practical minimum (Orin Nano 8 GB vs NX 16 GB vs AGX) for real-time nvblox at usable resolution? The Seeed deep-dive page targets **AGX Orin** specifically.
- Does the recipe support RealSense as a drop-in, or is it Orbbec-only?
