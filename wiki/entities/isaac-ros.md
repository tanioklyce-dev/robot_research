---
title: Isaac ROS
type: entity
subtype: software-framework
created: 2026-06-13
updated: 2026-06-13
sources: 4
tags: [isaac-ros, nvidia, ros2, perception, gpu, jetson, robotics]
---

**Isaac ROS** — NVIDIA's collection of **GPU-accelerated ROS 2 packages** ("GEMs") for robot perception and navigation, optimized to run on [Jetson](jetson-thor.md) edge hardware and discrete NVIDIA GPUs. It brings hardware-accelerated perception (3D mapping, stereo/depth, visual SLAM, AprilTag detection, DNN inference) into the ROS 2 ecosystem.

## In this wiki

So far the wiki touches Isaac ROS only through its **[nvblox](nvblox.md)** 3D-mapping component, packaged as a Seeed [reComputer](seeed-studio.md) [`jetson-examples`](../sources/seeed-jetson-examples-nvblox.md) recipe. Isaac ROS is the ROS 2 / edge-perception counterpart to NVIDIA's simulation-side stack ([Isaac Sim](nvidia-isaac-sim.md) + [Isaac Lab](nvidia-isaac-lab.md)) and physics work ([Newton](../sources/nvidia-newton-physics-engine-developer-page.md)).

## Components seen so far

- **[nvblox](nvblox.md)** — GPU 3D volumetric mapping from RGB-D/stereo depth.

## Related

- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) / [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — simulation + RL siblings.
- [ROS 2](ros2.md) — the middleware Isaac ROS extends.
- [JetPack](jetpack.md) — the Jetson software base Isaac ROS containers target.

## Mentioned in

- [Seeed jetson-examples — nvblox recipe (README)](../sources/seeed-jetson-examples-nvblox.md)
