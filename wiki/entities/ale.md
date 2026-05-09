---
title: Arcade Learning Environment (ALE)
type: entity
subtype: simulator
created: 2026-05-09
updated: 2026-05-09
sources: 1
tags: [ale, atari, rl, benchmark, farama, gymnasium]
---

The **Arcade Learning Environment (ALE)** is a framework for developing and evaluating AI agents on Atari 2600 games. Built on the Stella emulator, it exposes 100+ classic games as RL environments. The foundational paper ("The Arcade Learning Environment: An Evaluation Platform for General Agents," JAIR) established Atari as the canonical benchmark for deep RL — the basis for DQN (Mnih et al. 2015) and most subsequent deep RL work through ~2020.

## Environments
- **100+ single-agent games**: Breakout, Pac-Man, Space Invaders, Donkey Kong, Frogger, etc.
- **23 multi-agent environments**: Basketball Pong, Joust, Warlords, etc. — competitive and cooperative.

## API
- **Gymnasium** (recommended modern interface) — [Gymnasium](gymnasium.md)-compatible.
- Python interface.
- C++ interface.
- Visualization tool for debugging.

## Key design principle
Separates emulation details from agent design — agents interact via a fixed observation/action API without needing to know Stella internals.

## Status in the field
ALE / Atari was the dominant deep RL benchmark from ~2013 through ~2020. It has since been largely superseded in the robot-learning community by continuous-control benchmarks ([DM Control Suite](dm-control.md), [Gymnasium-Robotics](gymnasium-robotics.md), [MuJoCo Playground](mujoco-playground.md)) and manipulation benchmarks ([RoboCasa](robocasa.md), [ManiSkill](maniskill.md)). ALE remains relevant for general RL and multi-agent RL research.

## Organization
Maintained by the [Farama Foundation](farama-foundation.md). Listed as "Incubating" tier within Farama's project hierarchy. Open-source.

## Related
- [Farama Foundation](farama-foundation.md) — maintainer.
- [Gymnasium](gymnasium.md) — the API ALE implements.

## Mentioned in
- [Arcade Learning Environment — Farama Project Page](../sources/ale-farama.md)
