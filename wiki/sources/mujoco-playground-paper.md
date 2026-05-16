---
title: MuJoCo Playground Paper
type: source
url: https://arxiv.org/abs/2502.08844
author: Google DeepMind (multiple authors)
published: 2025-02
ingested: 2026-05-06
tags: [mujoco, mjx, sim-to-real, gpu, robot-learning]
---

## Summary
ArXiv paper introducing [MuJoCo Playground](../entities/mujoco-playground.md), an open-source framework for robot learning built on [MuJoCo](../entities/mujoco.md) MJX, with end-to-end support for vision-based policy training and sim-to-real transfer. Demonstrated at RSS 2025.

## Key claims
- Built on MJX ([MuJoCo](../entities/mujoco.md)'s JAX-based GPU implementation).
- Supports quadrupeds, humanoids, dexterous hands, and robotic arms in a unified API.
- Achieves zero-shot sim-to-real transfer from both state and pixel inputs.
- Integrates the open-source Madrona batch GPU renderer for vision-based RL on a single GPU.
- `pip install playground` — single-GPU training in minutes.
- Optionally backends to [Newton](../entities/newton-physics-engine.md) in 2026.

## Entities mentioned
- [MuJoCo Playground](../entities/mujoco-playground.md)
- [MuJoCo](../entities/mujoco.md)
- [Google DeepMind](../entities/google-deepmind.md)
- [Newton physics engine](../entities/newton-physics-engine.md)

## Concepts touched
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md)
- GPU-accelerated RL
- Vision-based policy learning

## Open questions
- How does Playground's throughput compare to Isaac Lab on identical tasks?
- Does Madrona renderer match Omniverse photorealism enough for [VLA](../concepts/learning/vla-models.md) training?
