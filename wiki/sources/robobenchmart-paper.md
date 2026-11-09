---
title: "RoboBenchMart: Benchmarking Robots in Retail Environment"
type: source
url: https://arxiv.org/abs/2511.10276
fetch_url: https://arxiv.org/pdf/2511.10276v1
local_path: raw/robobenchmart-2511.10276v1.pdf
sha256: a7562fcfad94f24e270b3341de91c9522daa6c1831eab8e5d51420ebe7773917
author: Soshin, Krapukhin, Spiridonov, Shepelev, Bukhtuev, Kuznetsov, Shakhuro (FusionBrain Lab)
published: 2025-11-13
ingested: 2026-11-08
tags: [retail, grocery, benchmark, simulation, maniskill, fetch, vla-models, pi-zero]
---

# RoboBenchMart: Benchmarking Robots in Retail Environment

## Summary

An open simulated benchmark for dark stores, built on [ManiSkill3](../entities/maniskill.md) with a Fetch mobile manipulator. Generalist policies were fine-tuned on 2,480 generated demonstrations. **Multi-step tasks scored zero for every model, and single steps collapsed when the scene or items changed.** Treat it as evidence of fragility under little training data, because the authors deliberately limited the demonstrations.

## Key claims

- **Generators.** Procedural store layouts and shelf arrangements, 370 product assets across 21 categories, and trajectories from motion planning and RL. The RL pipeline produces feasible trajectories about 60% of the time.
- **Tasks.** Pick to basket, pick from floor, board to board, open fridge, close fridge, plus composite "pick 3 items" and "pick from fridge."
- **Success rates in Table 2 (%), 50 trials per task, item and fixture:**

| Model | Scenario | Pick to basket | Pick from floor | Board to board | Open fridge | Close fridge | Composite tasks |
|---|---|---|---|---|---|---|---|
| Octo | In-domain | 17 | 2 | 13 | 32 | 41 | 0 |
| Octo | Unseen scenes | 1 | 0 | 2 | 10 | 37 | 0 |
| [π0](../entities/pi-zero.md) | In-domain | 22 | 29 | 15 | 48 | 83 | 0 |
| π0 | Unseen scenes | 1 | 12 | 5 | 25 | 75 | 0 |
| [π0.5](../entities/pi-zero-5.md) | In-domain | 63 | 44 | 55 | 50 | 85 | 0 |
| π0.5 | Unseen scenes | 38 | 11 | 22 | 37 | 77 | 0 |
| π0.5 | Unseen scenes and items | 10 | 0 | 23 | n/a | n/a | 0 |

- **Authors' reading.** Pretrained generalist models are fragile to minor changes and may need retail-specific pretraining.
- **Stated limits.** Parallel-jaw gripper only, no suction or dexterous hands. Rigid packages only. Relatively large gaps between items, which the authors note may suit future standardized dark stores.

> [!note] Limits on what the zeros mean
> Models were fine-tuned only on single steps, and composites were run by chaining those steps. Only 2–3 training objects per task were used, with no real-robot test. The zeros say a chained, lightly trained policy fails. They don't establish the ceiling of a well-trained one.

## Entities mentioned

- [RoboBenchMart](../entities/robobenchmart.md)
- [ManiSkill](../entities/maniskill.md)
- [Octo](../entities/octo.md)
- [π0](../entities/pi-zero.md)
- [π0.5](../entities/pi-zero-5.md)

## Concepts touched

- [Retail and grocery robotics](../concepts/robotics/retail-and-grocery-robotics.md)
- [VLA models](../concepts/learning/vla-models.md)

## Open questions

- How do the results change with far more demonstrations, or a suction gripper?
- Does simulated rank predict real-store performance?
