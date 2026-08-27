---
title: DROID — A Large-Scale In-The-Wild Robot Manipulation Dataset (paper)
type: source
url: https://arxiv.org/abs/2403.12945
author: Alexander Khazatsky, Karl Pertsch, Chelsea Finn, Sergey Levine, et al. (101 authors)
published: 2024-04
ingested: 2026-05-16
tags: [droid, robot-manipulation, dataset, teleoperation, franka, scene-diversity]
---

## Summary
The primary [DROID](../entities/droid.md) paper — a **76k-trajectory / 350-hour** real-robot teleoperation manipulation dataset, deliberately optimized for **scene diversity over embodiment diversity**: every demonstration uses the **same standardized Franka Panda hardware** so the only varying axis is the scene/task. Collected across **564 scenes, 84 tasks, 50 data collectors in North America, Asia, and Europe over 12 months** by a 101-author, 13-institution consortium led by Alexander Khazatsky and Karl Pertsch (Chelsea Finn and Sergey Levine senior). Open-sourced under **CC BY 4.0** along with policy-learning code and a hardware-reproduction guide. The headline claim: training with DROID yields higher-performance, better-generalizing policies than non-DROID baselines.

## Key claims

### Abstract (verbatim)
"The creation of large, diverse, high-quality robot manipulation datasets is an important stepping stone on the path toward more capable and robust robotic manipulation policies. However, creating such datasets is challenging: collecting robot manipulation data in diverse environments poses logistical and safety challenges and requires substantial investments in hardware and human labour. As a result, even the most general robot manipulation policies today are mostly trained on data collected in a small number of environments with limited scene and task diversity. In this work, we introduce DROID (Distributed Robot Interaction Dataset), a diverse robot manipulation dataset with 76k demonstration trajectories or 350 hours of interaction data, collected across 564 scenes and 84 tasks by 50 data collectors in North America, Asia, and Europe over the course of 12 months. We demonstrate that training with DROID leads to policies with higher performance and improved generalization ability. We open source the full dataset, policy learning code, and a detailed guide for reproducing our robot hardware setup."

### Dataset stats
| Field | Value |
|---|---|
| Trajectories | 76,000 |
| Hours of interaction | 350 |
| Distinct scenes | 564 |
| Tasks | 84 |
| Data collectors | 50 |
| Continents | 3 (NA, Asia, Europe) |
| Collection window | 12 months |
| License | CC BY 4.0 |

### Design philosophy
- **Standardized hardware** across all collectors — Franka Panda manipulation platform — so the dataset's diversity axis is scenes/tasks rather than robot embodiments. Complementary to Open-X Embodiment's opposite choice (many platforms, narrower scene set).
- **Distributed collection**: 13 institutions, 50 collectors. The dataset's "in-the-wild" framing comes from non-lab scenes (offices, kitchens, homes, classrooms) on a globally-distributed footprint.

## Entities mentioned
- [DROID](../entities/droid.md)
- [Franka Panda](../entities/franka-panda.md)
- [Chelsea Finn](../entities/chelsea-finn.md), [Sergey Levine](../entities/sergey-levine.md), [Karl Pertsch](../entities/karl-pertsch.md) — senior / lead authors.
- [V-JEPA 2](../entities/v-jepa-2.md), [JEPA-WMs](../entities/jepa-wms.md) — downstream consumers of DROID footage in JEPA-line work.
- [Open X-Embodiment](../entities/open-x-embodiment.md) — co-cited dataset.

## Concepts touched
- [Imitation learning](../concepts/learning/imitation-learning.md) — DROID is the largest single-platform teleop corpus the wiki tracks for IL training.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — DROID's real-data scale is the counter-strategy to sim-pretrain-then-transfer.

## Open questions
- The abstract claims "higher performance and improved generalization" but the WebFetch summary did not surface specific benchmark numbers — the paper body has them. Worth pulling if DROID-pretrain-vs-baseline becomes a load-bearing wiki claim.
- Per-scene / per-task distribution: how skewed? 564 scenes × 84 tasks / 76k trajectories ≈ 134 trajectories per scene on average, but the actual distribution matters for evaluating long-tail tasks.
- Hardware-standardization details (gripper model, exact camera count and placement) not surfaced from abstract — body has them.
