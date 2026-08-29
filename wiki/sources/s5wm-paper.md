---
title: "Accelerating Model-Based RL with State-Space World Models (S5WM)"
type: source
url: https://arxiv.org/abs/2502.20168
author: Maria Krinner*, Elie Aljalbout*, Angel Romero, Davide Scaramuzza (Robotics and Perception Group, University of Zurich)
published: 2025-02-27 (arXiv v1, cs.RO)
ingested: 2026-07-09
venue: arXiv (UZH RPG)
local_path: raw/RLMB_2502.20168v1.pdf
sha256: 4fa4b7816efcef433e86bd98b98225c48868164973b0e4681788e27c275ea64b
format: paper PDF (16 pp)
tags: [mbrl, world-model, state-space-models, s5, dreamer, drone-racing, quadrotor, sim-to-real, uav, sample-efficiency]
---

# Accelerating Model-Based RL with State-Space World Models (S5WM)

## Summary

Scaramuzza's UZH drone lab attacks MBRL's practical bottleneck: the world model makes training **slow** (even when sample-efficient), because [Dreamer](../entities/dreamer.md)-family methods use a recurrent RSSM that trains sequentially. **S5WM** swaps the RSSM for a modern **parallelizable state-space model (S5)** — adapted to reset at episode boundaries — cutting **world-model training time up to 10× and overall MBRL wall-clock up to 4×** at equal sample efficiency and reward. Second contribution: an **asymmetric world model** that reconstructs low-dimensional *privileged state* (not pixels) while conditioning on images, easing vision-based POMDP training and sim-to-real. Validated where it counts for this lab: **real-world agile quadrotor flight / drone racing**, with both state- and image-based policies flown on hardware.

## Key claims

- **Bottleneck diagnosis**: in Dreamer-class MBRL the sequential RSSM dominates compute; SSMs parallelize the sequence dimension of dynamics training (same motivation family as S4/S5 for long sequences).
- **S5WM**: S5 backbone as the world-model sequence model, with episode-boundary **resettability** added; actor-critic in imagination on top (Dreamer-family recipe otherwise).
- **Speedups**: up to **10× WM-training**, **4× end-to-end MBRL** wall-clock vs RSSM baselines, at comparable sample efficiency/reward vs SOTA MBRL and model-free baselines (drone-racing environment).
- **Asymmetric/privileged reconstruction**: during sim training, the WM reconstructs **privileged low-dim state `s_t`** instead of high-dim images — cheaper, and a sim-to-real device for vision-based policies (train perception-conditioned, supervise on state).
- **Real-world demonstration**: agile quadrotor tasks (state obs + image obs variants) flown on real hardware — MBRL at racing-grade dynamics, not just DMC.
- Honest limitation: less robust to hyperparameter changes than mature MBRL baselines; actor-critic training remains unaccelerated (future work).

## Entities mentioned

- [Dreamer / DreamerV3](../entities/dreamer.md) — the family being accelerated (RSSM replaced).
- UZH Robotics & Perception Group / Davide Scaramuzza — the wiki's canonical agile-flight lab ([agentic UAVs](../concepts/robotics/agentic-uavs.md)); no entity page yet.
- Adjacent: [TD-MPC2](../entities/td-mpc.md) (decoder-free MBRL sibling).

## Concepts touched

- [World model](../concepts/world-models/world-model.md) — MBRL facet: a systems-level (wall-clock) datapoint, orthogonal to the sample-efficiency axis the page tracks.
- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — MBRL reaching real racing quadrotors.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — privileged-state asymmetry as transfer device.

## Open questions

- Venue/camera-ready status (arXiv v1 only in the raw copy); any follow-up flight results.
- Whether SSM world models displace RSSMs upstream (in Dreamer-line releases) — this is an existence proof, not adoption evidence.
- How the privileged-asymmetric trick compares to the teacher-student distillation standard in locomotion.
