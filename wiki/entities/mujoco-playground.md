---
title: MuJoCo Playground
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-07
sources: 4
tags: [mujoco, mjx, jax, robot-learning, deepmind, sim-to-real]
---

Google DeepMind's open-source robot-learning framework built on MuJoCo MJX (the JAX-accelerated MuJoCo). Designed to streamline simulation, training, and sim-to-real transfer on a single GPU.

## Capabilities
- JAX-based GPU vectorization (MJX); optional Warp / [Newton](newton-physics-engine.md) backends.
- Robot platforms: quadrupeds, humanoids, dexterous hands, robotic arms.
- Vision-based RL via the Madrona batch GPU renderer.
- Demonstrated zero-shot sim-to-real from both state and pixel inputs.
- `pip install playground` install path; minutes to first trained policy.

## 2026 status
Presented at RSS 2025; widely cited for [Sim-to-real transfer](../concepts/sim-to-real-transfer.md) research. Now interoperates with [Newton physics engine](newton-physics-engine.md) alongside its native MJX backend.

## Related
- [Google DeepMind](google-deepmind.md) — maintainer.
- [Newton physics engine](newton-physics-engine.md) — alternative backend.
- [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — competing/parallel learning framework.

## Mentioned in
- [MuJoCo Playground Paper](../sources/mujoco-playground-paper.md)
- [NVIDIA Newton Physics Engine Developer Page](../sources/nvidia-newton-physics-engine-developer-page.md)
- [Farama Foundation Projects Page](../sources/farama-projects-page.md)
- [URDF vs MJCF vs USD comparison](../sources/source-robotics-urdf-mjcf-usd-comparison.md)
