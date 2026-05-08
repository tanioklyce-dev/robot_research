---
title: MuJoCo
type: entity
subtype: physics-engine
created: 2026-05-07
updated: 2026-05-07
sources: 7
tags: [mujoco, physics-engine, deepmind, simulation]
---

**Multi-Joint dynamics with Contact** — physics engine optimized for articulated body dynamics with rich contact modelling. The default substrate for a large slice of the RL / robot-learning ecosystem (every Gymnasium-Robotics env, the original Adroit and Franka Kitchen benchmarks, DM Control, MuJoCo Playground, and many others). Now maintained as open-source by Google DeepMind.

## Variants and bindings
- **`mujoco`** (the maintained package) — the current Google DeepMind-maintained Python bindings + native engine. C++ core, Python via pybind11. What [[gymnasium-robotics|Gymnasium-Robotics]] and modern code uses ([[gymnasium-robotics-docs|Gymnasium-Robotics Documentation]]).
- **`mujoco-py`** — the legacy OpenAI bindings, deprecated. Older code (e.g. anything pinning `gym==0.21.0`'s `mujoco` extra) may still try to pull this; it builds against an old MuJoCo binary distribution.
- **MJX** — MuJoCo's JAX implementation. Same physics, GPU-vectorizable. The substrate for [[mujoco-playground|MuJoCo Playground]] ([[mujoco-playground-paper|MuJoCo Playground Paper]]).
- **MJCF** — MuJoCo's XML scene-description format. Sibling to URDF and USD ([[source-robotics-urdf-mjcf-usd-comparison|URDF vs MJCF vs USD comparison]]). Tightly coupled to the MuJoCo ecosystem; first-class actuators / sensors / tendons / equality constraints.

## Role in the ecosystem
- Physics backend under [[mujoco-playground|MuJoCo Playground]] (via MJX), [[gymnasium-robotics|Gymnasium-Robotics]] (via vanilla bindings), and Hello Robot's wrappers ([[hello-robot-stretch-docs|Hello Robot Stretch Documentation]]).
- Targeted as a **pluggable backend** by [[newton-physics-engine|Newton]] alongside Isaac/PhysX — Newton is positioned as compatible with both MuJoCo Playground and [[nvidia-isaac-lab|Isaac Lab]] ([[nvidia-newton-physics-engine-developer-page|NVIDIA Newton Physics Engine Developer Page]]).
- Compared against [[genesis|Genesis]], NVIDIA PhysX, and Newton across throughput / accuracy axes in multiple sources.

## History
- Originally developed by Roboti LLC (Emo Todorov).
- Acquired by DeepMind in October 2021 and open-sourced soon after.
- Continues active development under Google DeepMind, now also a co-developer of [[newton-physics-engine|Newton]].

## Why it matters here
- Effectively the lingua franca of contact-rich robot simulation. If a paper says "we evaluate on Fetch" or "we use the Adroit benchmark" or "our envs use the Gymnasium API," a MuJoCo backend is implied.
- The `mujoco` vs `mujoco-py` split is a real install-time hazard — see the `gym 0.21.0` saga in [[leworldmodel-howto|LeWM howto]]. The legacy bindings are the primary reason ancient Gym pins are painful to install.

## Related
- [[mujoco-playground|MuJoCo Playground]] — JAX-on-MJX learning framework on top.
- [[gymnasium-robotics|Gymnasium-Robotics]] — env library on top.
- [[newton-physics-engine|Newton physics engine]] — DeepMind co-developed; Newton targets compatibility with MJX-style workflows.

## Mentioned in
- [[mujoco-playground-paper|MuJoCo Playground Paper]]
- [[gymnasium-robotics-docs|Gymnasium-Robotics Documentation]]
- [[source-robotics-urdf-mjcf-usd-comparison|URDF vs MJCF vs USD comparison]]
- [[farama-projects-page|Farama Foundation Projects Page]]
- [[hello-robot-stretch-docs|Hello Robot Stretch Documentation]]
- [[genesis-project-page|Genesis Project Page]]
- [[leworldmodel-howto|LeWorldModel — train and run howto]] (legacy `mujoco-py` install hazard)
- [[dino-wm-paper|DINO-WM Paper]] — likely MuJoCo 2.1 backend per secondary research; project page silent on engine.
