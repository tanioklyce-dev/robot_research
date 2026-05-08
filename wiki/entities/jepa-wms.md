---
title: JEPA-WMs
type: entity
subtype: model
created: 2026-05-07
updated: 2026-05-07
sources: 1
tags: [jepa-wms, jepa, world-model, fair, meta-fair, robocasa, metaworld, droid, lecun, bardes]
---

**JEPA-WMs** — a family of [JEPA](../concepts/jepa.md)-style world models for physical planning, introduced by [FAIR](meta-fair.md) in [Terver et al. (Dec 2025)](../sources/jepa-wms-paper.md) ("What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?"). Authors include **Adrien Bardes** and **Yann LeCun** — both senior on [V-JEPA 2](v-jepa-2.md). The work is the **first JEPA-for-robotics paper this wiki has ingested that explicitly uses heavy sim** ([RoboCasa](robocasa.md) kitchen manipulation).

## Approach
- Investigates which architectural and training choices in JEPA-WMs drive planning performance.
- Compares against **DINO-WM** ([entity](dino-wm.md)) and **V-JEPA 2-AC** ([entity](v-jepa-2.md)) as baselines on navigation and manipulation tasks.
- Per the abstract: "experiments using both simulated environments and real-world robotic data."

## Environments and datasets
From the official `facebookresearch/jepa-wms` README:

- **42 Metaworld tasks** (100 episodes each).
- **Push-T**, **PointMaze**, **Wall** — classic 2D/3D control benches.
- **[RoboCasa](robocasa.md) kitchen manipulation** — the heavy-sim entry that breaks the "JEPA skips sim" pattern.
- **DROID** dataset (raw stereo HD, 8.7 TB; or non-stereo HD, 5.6 TB).
- **Franka** robot trajectories with "unroll decode evaluation."
- Optional video pretraining: **Kinetics-400, Kinetics-710, Something-Something-v2, HowTo100M**.

Pretrained weights ship per environment; HF dataset at https://huggingface.co/datasets/facebook/jepa-wms.

## Why it matters
JEPA-WMs is the load-bearing source for the [revised "JEPA + sim" synthesis](../syntheses/why-jepa-research-skips-the-simulator-stack.md). The same FAIR group that produced V-JEPA 2 (no simulator) and the broader JEPA push moved into RoboCasa within ~6 months. The original "JEPA skips heavy sim" generalization broke before this wiki was even one ingest old.

## Related
- [Joint-Embedding Predictive Architecture](../concepts/jepa.md) — architecture family.
- [V-JEPA 2](v-jepa-2.md) — predecessor + baseline.
- [DINO-WM](dino-wm.md) — baseline.
- [RoboCasa](robocasa.md) — heavy-sim manipulation benchmark.
- [Meta FAIR](meta-fair.md) — primary lab.
- [Why JEPA research skips the simulator stack](../syntheses/why-jepa-research-skips-the-simulator-stack.md) — revised synthesis citing this paper as the contradicting evidence.

## Code
- Repo: https://github.com/facebookresearch/jepa-wms
- Dataset: https://huggingface.co/datasets/facebook/jepa-wms

## Mentioned in
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)
