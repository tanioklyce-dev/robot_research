---
title: Google DeepMind
type: entity
subtype: company
created: 2026-05-06
updated: 2026-05-07
sources: 3
tags: [google-deepmind, mujoco, newton, mjcphysics, openusd, robotics-research]
---

Google's AI research lab. Maintains MuJoCo and [MuJoCo Playground](mujoco-playground.md), co-developed the [Newton physics engine](newton-physics-engine.md) with [NVIDIA](nvidia.md) and [Disney Research](disney-research.md) under the Linux Foundation, and ships **`MjcPhysics`** — a USD schema plugin that brings MuJoCo solver parameters into [OpenUSD](openusd.md) scenes.

## Robotics simulation contributions
- **MuJoCo** — the open-source physics engine (acquired and open-sourced by DeepMind in 2021).
- **[MuJoCo Playground](mujoco-playground.md)** — robot-learning framework on MJX, presented at RSS 2025.
- **[Newton physics engine](newton-physics-engine.md)** co-development under Linux Foundation governance.
- **`MjcPhysics` USD schema plugin** — MuJoCo-specific solver attributes (integrator, constraint solver algorithm, tolerance, contact settings) authored as USD prims. Concrete evidence that DeepMind is invested in [OpenUSD](openusd.md) as a cross-stack substrate, not just consuming it ([NVIDIA OpenUSD-for-robotic-simulation blog](../sources/nvidia-openusd-for-robotic-simulation.md)).
- **`mujoco-usd-converter`** — MuJoCo-to-USD bridge tool hosted in the `newton-physics` GitHub org, used alongside `MjcPhysics` schemas.

## Mentioned in
- [MuJoCo Playground Paper](../sources/mujoco-playground-paper.md)
- [NVIDIA Newton Physics Engine Developer Page](../sources/nvidia-newton-physics-engine-developer-page.md)
- [Using OpenUSD for Modular and Scalable Robotic Simulation](../sources/nvidia-openusd-for-robotic-simulation.md)
