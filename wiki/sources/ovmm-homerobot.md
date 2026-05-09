---
title: HomeRobot — Open Vocabulary Mobile Manipulation (OVMM)
type: source
url: https://ovmm.github.io/
author: Yenamandra, Ramachandran, Yadav et al.
affiliations: Georgia Tech, Meta AI, CMU, Simon Fraser University
published: 2024
ingested: 2026-05-09
tags: [ovmm, homerobot, mobile-manipulation, stretch, zero-shot, sim-to-real]
---

## Summary
HomeRobot is the benchmark and software platform for Open Vocabulary Mobile Manipulation (OVMM) — picking any object in any unseen environment and placing it in a commanded location. Runs on [Hello Robot Stretch](../entities/stretch.md). OK-Robot (2024) reports 1.8× improvement over HomeRobot baselines.

## Key claims

- OVMM framed as "a foundational challenge for robots to be useful assistants in human environments" requiring simultaneous perception, language, navigation, and manipulation.
- Task format: "Move the [object] from the [start receptacle] to the [goal receptacle]."
- Baseline real-world result: **20% success rate** on Hello Robot Stretch.
- Demonstrates sim-to-real transfer via both RL and heuristic model-based approaches.
- Simulation benchmark: 50 scenes, thousands of episodes, multi-room home environments, seen vs. unseen objects.

## Entities mentioned
- [Stretch](../entities/stretch.md) — hardware platform
- [Hello Robot](../entities/hello-robot.md) — robot manufacturer
- [Meta FAIR](../entities/meta-fair.md) — contributing institution

## Open questions
- Exact date of the HomeRobot paper not confirmed from project page.
- Current SOTA on the OVMM benchmark after OK-Robot.
