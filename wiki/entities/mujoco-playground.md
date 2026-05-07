---
title: MuJoCo Playground
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-07
sources: 3
tags: [mujoco, mjx, jax, robot-learning, deepmind, sim-to-real]
---

Google DeepMind's open-source robot-learning framework built on MuJoCo MJX (the JAX-accelerated MuJoCo). Designed to streamline simulation, training, and sim-to-real transfer on a single GPU.

## Capabilities
- JAX-based GPU vectorization (MJX); optional Warp / [[newton-physics-engine|Newton]] backends.
- Robot platforms: quadrupeds, humanoids, dexterous hands, robotic arms.
- Vision-based RL via the Madrona batch GPU renderer.
- Demonstrated zero-shot sim-to-real from both state and pixel inputs.
- `pip install playground` install path; minutes to first trained policy.

## 2026 status
Presented at RSS 2025; widely cited for [[sim-to-real-transfer|Sim-to-real transfer]] research. Now interoperates with [[newton-physics-engine|Newton physics engine]] alongside its native MJX backend.

## Related
- [[google-deepmind|Google DeepMind]] — maintainer.
- [[newton-physics-engine|Newton physics engine]] — alternative backend.
- [[nvidia-isaac-lab|NVIDIA Isaac Lab]] — competing/parallel learning framework.

## Mentioned in
- [[mujoco-playground-paper|MuJoCo Playground Paper]]
- [[nvidia-newton-physics-engine-developer-page|NVIDIA Newton Physics Engine Developer Page]]
