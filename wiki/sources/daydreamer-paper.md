---
title: "DayDreamer — World Models for Physical Robot Learning"
type: source
url: https://arxiv.org/abs/2206.14176
author: Philipp Wu*, Alejandro Escontrela*, Danijar Hafner*, Ken Goldberg, Pieter Abbeel (UC Berkeley)
published: 2022-06 (arXiv); CoRL 2022
ingested: 2026-07-09
venue: CoRL 2022
local_path: raw/DayDreamer_2206.14176v1.pdf
sha256: 2ee10ae0961bef97ca522bb7ee5b7514e7a918a637dedad569b572b18bccb35e
format: paper PDF (15 pp)
tags: [daydreamer, dreamer, mbrl, real-robot, no-simulator, quadruped, manipulation, online-learning, berkeley, hafner]
---

# DayDreamer — World Models for Physical Robot Learning

## Summary

**Dreamer on real robots, no simulator** — the wiki's most-wanted MBRL ingest (flagged in the [awesome-physical-ai gap analysis](awesome-physical-ai-github.md) and as [EAWM](eawm-paper.md)'s natural robot testbed). [Hafner](../entities/danijar-hafner.md) + Berkeley apply [Dreamer](../entities/dreamer.md) to **4 physical robots learning online, directly in the real world**: an **A1 quadruped learns to roll off its back, stand, and walk in 1 hour from scratch, without resets** — and adapts to pushes within 10 minutes (rolls over, stands back up); UR5 and XArm learn **visual pick-and-place**; a Sphero learns navigation. The thesis: the world model's imagination provides the cheap trials that everyone else gets from simulators — **sample-efficient enough to skip sim-to-real entirely**.

## Key claims

- Same Dreamer algorithm across 4 robots/tasks/observation types (proprio + visual), learning *online in the physical world* — no simulator, no demonstrations, no resets (A1).
- **A1: 1 hour to walking**, from lying on its back; perturbation recovery emerges with ~10 min more experience.
- UR5/XArm visual pick-place and Sphero navigation learned directly on hardware — manipulation and navigation, not just locomotion.
- Positioned explicitly against the sim-to-real orthodoxy: simulators miss real-world complexity and behaviors don't adapt; online world-model RL adapts continuously.
- Infrastructure released (async actor/learner for real-time robot RL) — pitched as groundwork for world-model robot learning.

## Entities mentioned

- [Dreamer](../entities/dreamer.md) — the algorithm; [Danijar Hafner](../entities/danijar-hafner.md) co-first author.
- Unitree A1 (predecessor of the wiki's [Unitree G1](../entities/unitree-g1.md)/Go2 coverage), UR5, XArm, Sphero. Berkeley (Goldberg, Abbeel).

## Concepts touched

- [World model](../concepts/world-models/world-model.md) — the real-robot existence proof for imagination-based MBRL.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — the explicit *alternative* to it.
- [Imitation learning](../concepts/learning/imitation-learning.md) — contrast: no demonstrations at all.

## Open questions

- Why didn't this line take over robot learning? → filed as [Why online MBRL lost to imitation/VLAs (2022–2026)](../syntheses/rl/online-mbrl-vs-imitation-robot-learning.md).
- EAWM×DayDreamer-style test (event-aware WM on hardware) — the open question filed on [EAWM](eawm-paper.md).
