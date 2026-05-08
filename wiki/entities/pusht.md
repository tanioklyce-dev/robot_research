---
title: PushT
type: entity
subtype: benchmark
created: 2026-05-07
updated: 2026-05-08
sources: 3
tags: [pusht, push-t, manipulation-benchmark, ibc, diffusion-policy, lightweight-sim]
---

**PushT** (sometimes "Push-T") — **2D manipulation benchmark**: an end-effector must precisely **push a T-shaped block into a target region**, then move to an end-zone to terminate the episode. Originally introduced in **Implicit Behavior Cloning** (IBC, Florence et al., Google Research, CoRL 2021) and popularized further by [[diffusion-policy|Diffusion Policy]] (Chi et al., 2023). Now functions as a **default lightweight benchmark** across the world-model and imitation-learning literature.

## Task structure (from the diffusion-policy project page)
> "the robot needs to precisely push the T-shaped block into the target region, and move the end-effector to the end-zone which terminates the episode."

Two sequential subgoals:
1. Precise T-block alignment with target.
2. End-effector retreat to terminate.

The task is **2D**, **dense-contact** (the T-block geometry creates non-trivial pushing dynamics), and **goal-conditioned** (target position varies). It rewards policies that handle **multi-step, contact-rich, position-precise** manipulation while staying small enough to train on a single GPU in hours.

## Concrete mechanics

What you actually see when a PushT episode runs.

### Visual scene
Top-down 2D view of a square workspace. Three things on screen:

- **Gray T-shaped block** — the object being pushed. Asymmetric (the T has a long stem and a wide cap), so its rotation matters.
- **Green T-shaped outline** — the target pose for the gray block to match (position + orientation).
- **Blue circle** — the end-effector. A point-mass agent, no gripper, no grasping. It can only push by making contact.

Image resolution is typically 96×96 (canonical [[diffusion-policy|Diffusion Policy]] / IBC variant) or 224×224 (some world-model variants). The `stable-worldmodel` PushT shipped with [[leworldmodel|LeWM]] uses image observations.

### Observation space
- **Image variant** — RGB rendering of the scene. Used by world-model papers ([[leworldmodel-paper|LeWM]], [[dino-wm|DINO-WM]]).
- **State variant** — end-effector xy + T-block xy + T-block orientation angle. Used by some BC baselines.
- **Goal** — for [[jepa|JEPA]]-style image-goal planning, the goal is itself an *image* of the T at the target pose; the planner minimizes latent prediction error against this goal embedding.

### Action space
2D continuous: the agent commands a target xy position for the end-effector. A low-level controller drives the blue circle toward that position; physics (Box2D / pymunk in the canonical implementation) handles contact with the T-block. **No grasping primitive** — the only way to move the block is to push it through contact.

### Episode structure
- Max steps per episode: typically 200–300.
- Success criterion: T-block intersection-over-union with the target T pose exceeds a threshold (commonly **IoU > 0.95** in the IBC variant).
- Some variants additionally require the agent to retreat to an end-zone after alignment ("two-phase" termination); others terminate on IoU alone. **Identify the variant when citing numbers** — see callout below.

### Why it's hard (despite being 2D)
- **Rotational asymmetry** — pushing the wrong edge of the T induces unwanted rotation. Naive "push toward goal" fails because contact dynamics depend on where on the T you push.
- **No regrasping** — once the block is misaligned, you have to *circle around* and push from a different angle. This forces multi-step planning rather than reactive behavior.
- **Position-precise** — sub-pixel alignment matters because IoU thresholds are tight.

This is exactly the bundle of properties that makes it a good **world-model benchmark**: greedy / reactive policies plateau, so improvements come from better lookahead (what a learned dynamics model is supposed to give you).

### Dataset
- IBC and Diffusion Policy ship ~200 human-teleop demonstration trajectories. These are the canonical training set.
- `stable-worldmodel`'s PushT dataset (the one [[leworldmodel-howto|LeWM howto]] downloads) is HDF5-archived; trajectories are `(image, action, next_image)` tuples suitable for action-conditioned JEPA training.

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
