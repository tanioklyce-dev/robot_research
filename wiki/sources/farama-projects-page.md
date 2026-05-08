---
title: Farama Foundation Projects Page
type: source
url: https://farama.org/projects
author: Farama Foundation
ingested: 2026-05-07
tags: [farama, gymnasium, pettingzoo, rl, multi-agent, offline-rl, robotics]
---

## Summary
Index page for projects maintained by the [[farama-foundation|Farama Foundation]] — the non-profit that took stewardship of OpenAI's `gym` and rebuilt the surrounding ecosystem of standardized RL APIs and reference environments. The page splits 19 projects into three tiers: Core (the standards), Mature (production-ready), Incubating (newer or transitioning).

The foundation's stated role: maintain "standard APIs that are reused by other projects within Farama and the community." The pattern is consistent — Gymnasium and PettingZoo are positioned as **APIs first**, with reference environments shipped alongside; downstream projects (e.g. [[gymnasium-robotics|Gymnasium-Robotics]]) implement those APIs for specific domains.

## Key claims
- **Three core projects (the standards)**:
  - [[gymnasium|Gymnasium]] — standard API for single-agent RL environments. The successor to OpenAI gym.
  - [[pettingzoo|PettingZoo]] — standard API for multi-agent RL environments.
  - **Minari** — standard format for offline RL datasets.
- **Mature** (11 projects):
  - [[gymnasium-robotics|Gymnasium-Robotics]] — robotics simulation environments built on the Gymnasium API.
  - **Metaworld** — multi-task / meta-RL benchmark.
  - **MAgent2** — engine for very-large-population multi-agent envs.
  - **Minigrid** — configurable gridworld envs.
  - **MiniWoB++** — web interaction tasks.
  - **MOMAland** / **MO-Gymnasium** — multi-objective (multi-agent / single-agent) extensions.
  - **Shimmy** — bindings that bring non-Farama envs (e.g. DM Control, OpenSpiel) into the Gymnasium / PettingZoo APIs.
  - **ViZDoom** — Doom (1993) environments.
  - **Jumpy** — JAX↔NumPy tensor conversion utility.
- **Incubating** (5 projects): Arcade Learning Environment (Atari), HighwayEnv (autonomous driving), MPE2 (communication-oriented multi-agent), Procgen2 (procedurally generated games), Stable-Retro (gym-retro fork).

## Entities mentioned
- [[farama-foundation|Farama Foundation]]
- [[gymnasium|Gymnasium]]
- [[pettingzoo|PettingZoo]]
- [[gymnasium-robotics|Gymnasium-Robotics]]

## Concepts touched
- Multi-agent RL — referenced via PettingZoo, MAgent2, MOMAland, MPE2.
- Offline RL — referenced via Minari.
- Multi-objective RL — referenced via MO-Gymnasium, MOMAland.
- Meta-RL — referenced via Metaworld.

## Open questions
- How active is each tier? Page positions Gymnasium / PettingZoo / Minari as standards, but doesn't say which "Mature" projects are still on a release cadence vs. archived-but-functional.
- Does Gymnasium-Robotics overlap with or compete against [[nvidia-isaac-lab|Isaac Lab]] / [[mujoco-playground|MuJoCo Playground]]? Likely a different niche (Gymnasium API on top of vanilla [[mujoco|MuJoCo]]) but the page doesn't address it.
- Is **Shimmy** the canonical bridge for using e.g. DM Control envs through a Gymnasium API? If so, it deserves its own page next time it comes up.
