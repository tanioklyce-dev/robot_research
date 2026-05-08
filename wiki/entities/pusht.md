---
title: PushT
type: entity
subtype: benchmark
created: 2026-05-07
updated: 2026-05-07
sources: 3
tags: [pusht, push-t, manipulation-benchmark, ibc, diffusion-policy, lightweight-sim]
---

**PushT** (sometimes "Push-T") — **2D manipulation benchmark**: an end-effector must precisely **push a T-shaped block into a target region**, then move to an end-zone to terminate the episode. Originally introduced in **Implicit Behavior Cloning** (IBC, Florence et al., Google Research, CoRL 2021) and popularized further by **Diffusion Policy** (Chi et al., 2023). Now functions as a **default lightweight benchmark** across the world-model and imitation-learning literature.

## Task structure (from the diffusion-policy project page)
> "the robot needs to precisely push the T-shaped block into the target region, and move the end-effector to the end-zone which terminates the episode."

Two sequential subgoals:
1. Precise T-block alignment with target.
2. End-effector retreat to terminate.

The task is **2D**, **dense-contact** (the T-block geometry creates non-trivial pushing dynamics), and **goal-conditioned** (target position varies). It rewards policies that handle **multi-step, contact-rich, position-precise** manipulation while staying small enough to train on a single GPU in hours.

## Why PushT shows up everywhere
- **Cheap to run** — 2D, fast contact simulation, small observation/action spaces. A single GPU can train hundreds of seeds.
- **Hard enough to discriminate** — purely reactive policies fail; policies need some lookahead. Diffusion Policy used PushT to demonstrate robustness to occlusion, physical perturbation, and visual distractors.
- **Standard across benchmarks** — by 2026 it has become a near-default lightweight testbed across world-model and imitation-learning papers.

## Cross-references in this wiki
- **[[leworldmodel-paper|LeWorldModel]]** — one of the four task datasets shipped with the `stable-worldmodel` package (`pusht`, `cube`, `tworooms`, `reacher`). Default fast eval bench.
- **[[dino-wm-paper|DINO-WM]]** — listed among the six core environments (PushT, Wall, PointMaze, Rope, Granular, Reacher).
- **[[jepa-wms-paper|JEPA-WMs]] (Terver et al., FAIR)** — included in the env list alongside Metaworld, RoboCasa, Wall, PointMaze, DROID.
- Implicit / pre-2024 references in earlier IBC and Diffusion Policy lines (those papers themselves not yet ingested).

## Position vs cousins
- **Versus [[metaworld|Metaworld]]** — PushT is one task with one well-tuned dynamic; Metaworld is 50 distinct tasks. Different testing surface (depth on one task vs breadth across tasks).
- **Versus [[robocasa|RoboCasa]] / [[maniskill|ManiSkill]]** — PushT is 2D, no scene clutter, no embodiment realism. RoboCasa has scenes; ManiSkill has 3D physics. PushT is for *training-method validation*, not realism.

## Origin
- **IBC**: Pete Florence, Corey Lynch, Andy Zeng, et al., Google Research, CoRL 2021.
- **Diffusion Policy**: Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, Shuran Song, Columbia / TRI / MIT, 2023.

> [!note] Code lineage
> PushT-style tasks now ship in many packages (LeRobot, `stable-worldmodel`, robomimic, diffusion-policy repo). Variants exist with mild differences in reward shaping, observation modality (state vs pixel), and termination criteria. When citing a specific number, identify which variant.

## Related
- [[leworldmodel|LeWorldModel]] — uses PushT as one of four `stable-worldmodel` task datasets.
- [[dino-wm|DINO-WM]] / [[jepa-wms|JEPA-WMs]] — JEPA-family consumers.

## Mentioned in
- [[leworldmodel-paper|LeWorldModel Paper]]
- [[leworldmodel-howto|LeWorldModel — train and run howto]]
- [[dino-wm-paper|DINO-WM Paper]]
- [[jepa-wms-paper|JEPA-WMs Paper]]

## Open questions / TBD
- IBC paper (Florence et al., CoRL 2021) and Diffusion Policy paper (Chi et al., 2023) not yet source pages — would let us cite PushT design rationale directly.
- Reward variants and observation modalities differ across packages; full taxonomy not yet documented.
