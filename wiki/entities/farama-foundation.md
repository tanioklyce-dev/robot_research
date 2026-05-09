---
title: Farama Foundation
type: entity
subtype: organization
created: 2026-05-07
updated: 2026-05-09
sources: 3
tags: [farama, gymnasium, pettingzoo, rl, organization]
---

Non-profit that took over stewardship of OpenAI's `gym` library and rebuilt it as **[Gymnasium](gymnasium.md)**, then expanded into a broader ecosystem of standardized RL APIs and reference environments. Maintains 19+ projects spanning single-agent RL, multi-agent RL, offline RL, multi-objective RL, and game-based benchmarks ([Farama Foundation Projects Page](../sources/farama-projects-page.md)).

## Role
- Owns the **API standards** the open-source RL community reuses. Other projects (in and out of Farama) implement those APIs rather than each rolling their own env interface.
- Operates as the de-facto successor to OpenAI's RL infrastructure work — OpenAI deprecated `gym` and Farama forked it as `gymnasium` to continue maintenance.

## Project tiers
- **Core (standards)**: [Gymnasium](gymnasium.md), [PettingZoo](pettingzoo.md), Minari.
- **Mature**: [Gymnasium-Robotics](gymnasium-robotics.md), Metaworld, MAgent2, Minigrid, MiniWoB++, MOMAland, MO-Gymnasium, Shimmy, ViZDoom, Jumpy.
- **Incubating**: [Arcade Learning Environment](ale.md), HighwayEnv, MPE2, Procgen2, Stable-Retro.

## Why it matters here
- **The `gym` 0.21.0 install pain in [the LeWM howto](../syntheses/leworldmodel-howto.md) is a Farama-era artifact** — `stable-worldmodel[env]` still pins the legacy OpenAI `gym` 0.21.0 transitively, while also pulling Farama's modern `gymnasium`. The two coexist in the same dep tree, which is why the install hit both PEP 440 metadata bugs (in old gym) and SWIG/box2d-py issues (in `gymnasium[all]`).
- Farama is the gravitational center of "RL env API" decisions across the broader robotics-learning ecosystem — anything claiming to be a "drop-in" RL env library is almost certainly implementing the Gymnasium API.

## Mentioned in
- [Farama Foundation Projects Page](../sources/farama-projects-page.md)
- [Gymnasium-Robotics Documentation](../sources/gymnasium-robotics-docs.md)
- [LeWorldModel — train and run howto](../syntheses/leworldmodel-howto.md) (indirectly, via `gymnasium[all]` dep chain)
- [Arcade Learning Environment — Farama Project Page](../sources/ale-farama.md)
