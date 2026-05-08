---
title: Gymnasium-Robotics
type: entity
subtype: env-library
created: 2026-05-07
updated: 2026-05-07
sources: 2
tags: [farama, gymnasium, robotics, rl, env-library]
---

Collection of **robotics simulation environments for RL**, exposing the [Gymnasium](gymnasium.md) API and built on **MuJoCo** (via the maintained `mujoco` Python bindings, not the legacy `mujoco-py`). Maintained by the [Farama Foundation](farama-foundation.md) ([Gymnasium-Robotics Documentation](../sources/gymnasium-robotics-docs.md), [Farama Foundation Projects Page](../sources/farama-projects-page.md)).

## Role
- The "Farama-native" robotics env library — counterpart to NVIDIA's [Isaac Lab](nvidia-isaac-lab.md) and DeepMind's [MuJoCo Playground](mujoco-playground.md), but built around the canonical Gymnasium API rather than a vendor-specific wrapper.
- Continuation of the original `gym` Fetch / Hand envs (originally OpenAI Robotics envs), now under Farama maintenance.

> [!note] CPU vs GPU backend not stated
> The `mujoco` Python bindings default to single-process CPU stepping, and Gymnasium-Robotics positions itself alongside (not under) [MuJoCo Playground](mujoco-playground.md) (which is the JAX/GPU one). Strong implication: Gymnasium-Robotics is the single-process CPU path. The docs root doesn't say so explicitly — verify before benchmarking throughput.

## Environment families
Six families ([Gymnasium-Robotics Documentation](../sources/gymnasium-robotics-docs.md)):

- **Fetch** — single-arm tabletop manipulation. Pick-and-Place, Push, Reach, Slide. Canonical Hindsight Experience Replay (HER) benchmark.
- **Shadow Dexterous Hand** — 7 in-hand manipulation tasks (blocks, eggs, pens), with optional touch sensors.
- **Maze** — Ant Maze and Point Maze. Navigation tasks.
- **Adroit Hand** — Door, Hammer, Pen, Relocate. Originally Vikash Kumar's Adroit benchmark; the standard eval suite for D4RL-style offline RL papers.
- **Franka Kitchen** — Multi-task kitchen manipulation (microwave, kettle, light switch, slide cabinet, hinge cabinet, top/bottom burner).
- **MaMuJoCo** — Multi-Agent MuJoCo. Classic locomotion envs (Ant, Humanoid, Walker2d) decomposed into per-joint agents for cooperative multi-agent RL; uses the [PettingZoo](pettingzoo.md) API rather than the single-agent Gymnasium API.

## Install / register
```python
import gymnasium as gym
import gymnasium_robotics
gym.register_envs(gymnasium_robotics)
```

## How it relates to other robotics sim stacks
- vs. [Isaac Lab](nvidia-isaac-lab.md): Isaac Lab is GPU-parallel ([Newton](newton-physics-engine.md) / PhysX), full Omniverse stack, much heavier; Gymnasium-Robotics rides on vanilla [MuJoCo](mujoco.md) bindings.
- vs. [MuJoCo Playground](mujoco-playground.md): both [MuJoCo](mujoco.md), but Playground uses MJX (JAX) for GPU vectorization; Gymnasium-Robotics is the classical single-env interface.
- vs. [ManiSkill](maniskill.md): ManiSkill uses [SAPIEN](sapien.md) and emphasizes large-batch GPU rollouts; Gymnasium-Robotics is benchmark-canon for "give me a Fetch reach env, fast."

## Why it matters here
- For research papers from 2018–2023 that say "we evaluate on Fetch / Hand / Maze envs," this is the package being imported.
- Useful sanity-check baseline before committing to a heavier sim stack.

## Related
- [Gymnasium](gymnasium.md) — API it implements.
- [Farama Foundation](farama-foundation.md) — maintainer.

## Mentioned in
- [Gymnasium-Robotics Documentation](../sources/gymnasium-robotics-docs.md)
- [Farama Foundation Projects Page](../sources/farama-projects-page.md)
