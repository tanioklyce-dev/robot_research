---
title: PettingZoo
type: entity
subtype: api-standard
created: 2026-05-07
updated: 2026-05-07
sources: 2
tags: [farama, pettingzoo, multi-agent-rl, api-standard]
---

Standard API for **multi-agent reinforcement learning environments**, with reference environments. The multi-agent counterpart to [[gymnasium|Gymnasium]] from the [[farama-foundation|Farama Foundation]] ([[farama-projects-page|Farama Foundation Projects Page]]).

## Role
- API analogue of Gymnasium for the multi-agent case: defines turn-taking (AEC) and parallel (Parallel API) interfaces so multi-agent envs across different research groups present a uniform surface.
- Bundles reference envs (classic games, MPE-style, Atari multiplayer wrappers).
- Cross-references **MAgent2** (large-population engine) and **MPE2** (communication-oriented multi-agent), both also under Farama.

## Why it matters here
- The robotics wiki is currently single-agent-centric, but multi-robot coordination work (humanoid teams, fleet manipulation, multi-arm tasks) lands on PettingZoo when it surfaces. Worth knowing the Farama branding before encountering it in a paper.

## Related
- [[gymnasium|Gymnasium]] — single-agent counterpart.
- [[farama-foundation|Farama Foundation]] — maintainer.

## Mentioned in
- [[farama-projects-page|Farama Foundation Projects Page]]
- [[gymnasium-robotics-docs|Gymnasium-Robotics Documentation]] — MaMuJoCo (multi-agent MuJoCo) uses the PettingZoo API.
