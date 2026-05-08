---
title: Google DeepMind
type: entity
subtype: company
created: 2026-05-06
updated: 2026-05-07
sources: 3
tags: [google-deepmind, mujoco, newton, mjcphysics, openusd, robotics-research]
---

Google's AI research lab. Maintains MuJoCo and [[mujoco-playground|MuJoCo Playground]], co-developed the [[newton-physics-engine|Newton physics engine]] with [[nvidia|NVIDIA]] and [[disney-research|Disney Research]] under the Linux Foundation, and ships **`MjcPhysics`** — a USD schema plugin that brings MuJoCo solver parameters into [[openusd|OpenUSD]] scenes.

## Robotics simulation contributions
- **MuJoCo** — the open-source physics engine (acquired and open-sourced by DeepMind in 2021).
- **[[mujoco-playground|MuJoCo Playground]]** — robot-learning framework on MJX, presented at RSS 2025.
- **[[newton-physics-engine|Newton physics engine]]** co-development under Linux Foundation governance.
- **`MjcPhysics` USD schema plugin** — MuJoCo-specific solver attributes (integrator, constraint solver algorithm, tolerance, contact settings) authored as USD prims. Concrete evidence that DeepMind is invested in [[openusd|OpenUSD]] as a cross-stack substrate, not just consuming it ([[nvidia-openusd-for-robotic-simulation|NVIDIA OpenUSD-for-robotic-simulation blog]]).
- **`mujoco-usd-converter`** — MuJoCo-to-USD bridge tool hosted in the `newton-physics` GitHub org, used alongside `MjcPhysics` schemas.

## Mentioned in
- [[mujoco-playground-paper|MuJoCo Playground Paper]]
- [[nvidia-newton-physics-engine-developer-page|NVIDIA Newton Physics Engine Developer Page]]
- [[nvidia-openusd-for-robotic-simulation|Using OpenUSD for Modular and Scalable Robotic Simulation]]
