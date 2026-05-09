---
title: MuJoCo
type: entity
subtype: physics-engine
created: 2026-05-07
updated: 2026-05-08
sources: 9
tags: [mujoco, physics-engine, deepmind, simulation, biomechanics]
---

**Multi-Joint dynamics with Contact** — physics engine optimized for articulated body dynamics with rich contact modelling. The default substrate for a large slice of the RL / robot-learning ecosystem (every Gymnasium-Robotics env, the original Adroit and Franka Kitchen benchmarks, DM Control, MuJoCo Playground, and many others). Now maintained as open-source by Google DeepMind.

## Variants and bindings
- **`mujoco`** (the maintained package) — the current Google DeepMind-maintained Python bindings + native engine. C++ core, Python via pybind11. What [Gymnasium-Robotics](gymnasium-robotics.md) and modern code uses ([Gymnasium-Robotics Documentation](../sources/gymnasium-robotics-docs.md)).
- **`mujoco-py`** — the legacy OpenAI bindings, deprecated. Older code (e.g. anything pinning `gym==0.21.0`'s `mujoco` extra) may still try to pull this; it builds against an old MuJoCo binary distribution.
- **MJX** — MuJoCo's JAX implementation. Same physics, GPU-vectorizable. The substrate for [MuJoCo Playground](mujoco-playground.md) ([MuJoCo Playground Paper](../sources/mujoco-playground-paper.md)).
- **MJCF** — MuJoCo's XML scene-description format. Sibling to URDF and USD ([URDF vs MJCF vs USD comparison](../sources/source-robotics-urdf-mjcf-usd-comparison.md)). Tightly coupled to the MuJoCo ecosystem; first-class actuators / sensors / tendons / equality constraints.

## Role in the ecosystem
- Physics backend under [MuJoCo Playground](mujoco-playground.md) (via MJX), [Gymnasium-Robotics](gymnasium-robotics.md) (via vanilla bindings), and Hello Robot's wrappers ([Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md)).
- Targeted as a **pluggable backend** by [Newton](newton-physics-engine.md) alongside Isaac/PhysX — Newton is positioned as compatible with both MuJoCo Playground and [Isaac Lab](nvidia-isaac-lab.md) ([NVIDIA Newton Physics Engine Developer Page](../sources/nvidia-newton-physics-engine-developer-page.md)).
- Compared against [Genesis](genesis.md), NVIDIA PhysX, and Newton across throughput / accuracy axes in multiple sources.
- **Biomechanical-simulation carrier.** [flybody](flybody.md) (Vaxenburg et al. 2025, *Nature*) builds an anatomically detailed *Drosophila melanogaster* in vanilla MuJoCo with phenomenological fluid + adhesion forces — extending MuJoCo's reach beyond rigid-robot bodies into [biomechanical animal simulation](../concepts/biomechanical-simulation.md). Same pattern as DeepMind's earlier virtual rodent.

## History
- Originally developed by Roboti LLC (Emo Todorov).
- Acquired by DeepMind in October 2021 and open-sourced soon after.
- Continues active development under Google DeepMind, now also a co-developer of [Newton](newton-physics-engine.md).

## Why it matters here
- Effectively the lingua franca of contact-rich robot simulation. If a paper says "we evaluate on Fetch" or "we use the Adroit benchmark" or "our envs use the Gymnasium API," a MuJoCo backend is implied.
- The `mujoco` vs `mujoco-py` split is a real install-time hazard — see the `gym 0.21.0` saga in [LeWM howto](../syntheses/leworldmodel-howto.md). The legacy bindings are the primary reason ancient Gym pins are painful to install.

## Related
- [MuJoCo Playground](mujoco-playground.md) — JAX-on-MJX learning framework on top.
- [Gymnasium-Robotics](gymnasium-robotics.md) — env library on top.
- [Newton physics engine](newton-physics-engine.md) — DeepMind co-developed; Newton targets compatibility with MJX-style workflows.

## Mentioned in
- [MuJoCo Playground Paper](../sources/mujoco-playground-paper.md)
- [Gymnasium-Robotics Documentation](../sources/gymnasium-robotics-docs.md)
- [URDF vs MJCF vs USD comparison](../sources/source-robotics-urdf-mjcf-usd-comparison.md)
- [Farama Foundation Projects Page](../sources/farama-projects-page.md)
- [Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md)
- [Genesis Project Page](../sources/genesis-project-page.md)
- [LeWorldModel — train and run howto](../syntheses/leworldmodel-howto.md) (legacy `mujoco-py` install hazard)
- [DINO-WM Paper](../sources/dino-wm-paper.md) — likely MuJoCo 2.1 backend per secondary research; project page silent on engine.
- [flybody Paper](../sources/flybody-paper.md) — fly biomechanical sim built on vanilla MuJoCo.
- [flybody GitHub](../sources/flybody-github.md)
