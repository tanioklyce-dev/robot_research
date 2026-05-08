---
title: Gymnasium-Robotics Documentation
type: source
url: https://robotics.farama.org/
author: Farama Foundation
ingested: 2026-05-07
tags: [farama, gymnasium, gymnasium-robotics, mujoco, rl, robotics]
---

## Summary
Landing page / documentation root for **[[gymnasium-robotics|Gymnasium-Robotics]]** — the [[farama-foundation|Farama Foundation]]'s collection of [[mujoco|MuJoCo]]-based robotics RL environments exposing the [[gymnasium|Gymnasium]] API. Six environment families covering reaching/picking, dexterous manipulation, navigation/mazes, kitchen multi-task, and multi-agent locomotion.

## Key claims
- Single sentence pitch: "Gymnasium-Robotics is a collection of robotics simulation environments for Reinforcement Learning."
- Built on **[[mujoco|MuJoCo]]** via the "maintained mujoco python bindings" (i.e. google-deepmind/mujoco, not the legacy `mujoco-py`).
- Conforms to the Gymnasium env interface — drop-in for any RL trainer that already targets Gymnasium.
- Six environment families:
  - **Fetch** — Pick-and-Place, Push, Reach, Slide. Single-arm tabletop manipulation.
  - **Shadow Dexterous Hand** — 7 tasks (blocks, eggs, pens), with optional touch sensors.
  - **Maze** — Ant Maze, Point Maze. Navigation.
  - **Adroit Hand** — Door, Hammer, Pen, Relocate. Dexterous manipulation (originally Vikash Kumar's Adroit benchmark; also a staple in D4RL offline-RL evaluations).
  - **Franka Kitchen** — Multi-task kitchen manipulation benchmark (microwave, kettle, light switch, slide cabinet, hinge cabinet, top burner, bottom burner).
  - **MaMuJoCo** — Multi-Agent MuJoCo. Decomposes classic locomotion (Ant, Humanoid, Walker2d, etc.) into per-joint agents for cooperative multi-agent RL.
- Install / register pattern (Python):
  ```python
  import gymnasium as gym
  import gymnasium_robotics
  gym.register_envs(gymnasium_robotics)
  ```
- Footer: "Copyright © 2026 Farama Foundation" — actively maintained.

## Entities mentioned
- [[gymnasium-robotics|Gymnasium-Robotics]]
- [[gymnasium|Gymnasium]]
- [[mujoco|MuJoCo]]
- [[farama-foundation|Farama Foundation]]

## Concepts touched
- Dexterous manipulation (Shadow Hand, Adroit).
- Multi-task RL (Franka Kitchen — explicitly multi-task).
- Multi-agent RL (MaMuJoCo) — uses the [[pettingzoo|PettingZoo]] API.
- Offline RL evaluation — Adroit envs are the standard eval suite for D4RL-style offline RL papers.

## Open questions
- The page didn't surface a current version number — pin awareness matters in practice (the LeWM dep tree pulls `gymnasium[all]==1.3.0`).
- MaMuJoCo presumably exposes a [[pettingzoo|PettingZoo]] API rather than Gymnasium — but the docs root didn't make that explicit.
- Does Gymnasium-Robotics include a HER (Hindsight Experience Replay) example/baseline? Fetch envs are the canonical HER benchmark, but the doc root doesn't say.
