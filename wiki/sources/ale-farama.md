---
title: Arcade Learning Environment — Farama Project Page
type: source
url: https://ale.farama.org/
author: Farama Foundation
affiliations: Farama Foundation
published: Unknown
ingested: 2026-05-09
tags: [ale, atari, rl, benchmark, farama, gymnasium]
---

## Summary
Documentation site for the [Arcade Learning Environment (ALE)](../entities/ale.md), Farama Foundation's Atari 2600 RL benchmark framework. ALE wraps the Stella emulator and exposes 100+ classic Atari games as Gymnasium-compatible RL environments. Foundational reference: "The Arcade Learning Environment: An Evaluation Platform for General Agents" (JAIR).

## Key claims

- ALE is a framework for developing AI agents against Atari 2600 ROMs via the Stella emulator.
- **100+ single-agent environments** covering classic games (Breakout, Pac-Man, Space Invaders, Donkey Kong, Frogger, etc.).
- **23 multi-agent environments** — competitive and cooperative (Basketball Pong, Joust, Warlords, etc.).
- Three interaction interfaces: **Gymnasium API** (recommended), Python, C++.
- Key design principle: separates emulation details from agent design.
- Additional features: vector environment support, customizable rendering modes, visualization tool.
- Maintained by the [Farama Foundation](../entities/farama-foundation.md); open-source.

## Entities mentioned
- [Farama Foundation](../entities/farama-foundation.md)
- [Gymnasium](../entities/gymnasium.md)

## Concepts touched
- RL evaluation benchmarks
- Atari 2600 as testbed for general agents

## Open questions
- License not stated on documentation page; Farama projects vary (MIT, Apache 2.0, GPL).
- Multi-agent API: PettingZoo-based or custom?
