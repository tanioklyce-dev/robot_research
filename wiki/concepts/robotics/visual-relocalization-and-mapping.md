---
title: Visual relocalization and mapping
type: concept
created: 2026-08-13
updated: 2026-08-13
sources: 4
tags: [slam, visual-relocalization, scene-coordinate-regression, gaussian-splatting, 3d-reconstruction, feed-forward, drift, loop-closure, rtab-map, gtsam]
---

**Visual relocalization and mapping** — building a geometric representation of a real place from camera (and sometimes LiDAR) data, and later recovering where the camera is *within* that representation. The two halves are separable and the second is usually the harder one to make robust.

## Why this page exists

**This wiki covered world models extensively and had no page for any of this.** [Generative-video](../world-models/world-model-simulators.md) world models predict what happens next; [JEPA](../world-models/jepa.md) predicts in latent space; both are asked *"what will the world do?"* This tradition asks a different question — ***"where am I, and what is the shape of this actual room?"*** — and answers it geometrically.

The gap was invisible until the [Niantic Spatial](../../sources/niantic-spatial-research.md) and [LingBot-Map](../../sources/lingbot-map-github.md) ingests, even though the wiki already depended on the answer: the [XLeRobot bring-up plan](../../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md)'s entire navigation leg is [RTAB-Map](../../entities/rtab-map.md) + [Nav2](../../entities/nav2.md), and [DimOS](../../entities/dimos.md) ships a voxel map with [GTSAM](../../entities/gtsam.md) pose-graph optimization.

## The three problems

| Problem | What it means | Classical answer |
|---|---|---|
| **Mapping** | build a representation from a stream | occupancy grid / voxel / point cloud / mesh / **Gaussian splat** |
| **Localization** | find the camera pose in an existing map | feature matching + PnP, or **scene coordinate regression** |
| **Drift** | small per-frame errors compound over a long trajectory | **loop closure** + back-end optimization over a factor graph |

**Drift is the one that decides whether a system works over minutes rather than seconds**, and it is where the approaches most visibly differ.

## Two ways to do it, and the field is moving between them

### Optimization-based (classical SLAM)

Estimate structure and pose by solving an optimization problem, usually a factor graph. [RTAB-Map](../../entities/rtab-map.md) with an appearance-based loop-closure detector and a [GTSAM](../../entities/gtsam.md)-class back end is the reference instance, and the wiki's only *measured* deployment on a cheap robot ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md): RealSense D435 + RTAB-Map localization-only + Nav2 on an Orin Nano Super).

**Localization-only mode** is the practical trick: map once offline, run pose-graph optimization there, then at runtime localize against the frozen map. Cheap, and it removes runtime drift accumulation entirely.

### Feed-forward (learned, amortized)

Train a model that outputs geometry and pose directly, with no per-scene optimization. **[LingBot-Map](../../entities/lingbot-map.md)** folds *"long-range drift correction"* into a transformer via trajectory memory and a pose-reference window — no loop-closure detector, no map to re-solve — and demonstrates a 25,000-frame walkthrough.

> [!note] The same arc, arrived at independently from AR and from robotics
> [Niantic Spatial](../../entities/niantic-spatial.md)'s own publication line runs **ACE** (CVPR 2023 — train a small per-scene network *in minutes*) → **Scene Coordinate Reconstruction** (ECCV 2024) → **feed-forward** localization and view synthesis by ICLR/CVPR 2026. [LingBot-Map](../../entities/lingbot-map.md) reaches the same place from the robotics side in 2026.
>
> **Per-instance optimization giving way to an amortized model once enough data exists** is a pattern this wiki has recorded repeatedly — in [RoboTwin 2.0](../../entities/robotwin.md) replacing hand-written task programs with an MLLM that writes them, and in the [world-model](../world-models/world-model.md) line's drift from planning-in-a-model toward direct policies.

## Representations

- **Occupancy / voxel** — what a planner consumes. [DimOS](../../entities/dimos.md)'s "column-carving" voxel map replaces each region wholesale from the newest LiDAR frame, trading map memory for reactivity.
- **Mesh** — geometry for rendering and collision.
- **Gaussian splats** — the 2023+ photorealistic representation, now produced **on-device on a phone in real time** ([Scaniverse](../../entities/niantic-spatial.md)). Niantic publishes **SPZ**, an open splat format claiming 90% size reduction.
- **Scene coordinate regression** — no explicit map at all; a network memorizes the scene by regressing 3D coordinates from pixels, and pose falls out of PnP. The ACE line.

## The benchmarks measure agreement with an algorithm, not accuracy

> [!warning] Every number in this area inherits a pseudo-ground-truth problem
> Poses for thousands of benchmark images cannot be human-annotated, so they are generated by a **reference algorithm** (SfM, or depth SLAM). **[On the Limits of Pseudo Ground Truth](../../sources/pseudo-ground-truth-paper.md)** (ICCV 2021) shows the consequence: swap the reference and **Active Search moves from last to first (+29.8 pts)** on 7Scenes while the depth-based leaders fall to the bottom.
>
> The mechanism is bias, not noise — **methods whose cost function resembles the reference's replicate its *imperfections* and are rewarded for it.** The authors call the issue *"fundamental"* and say they *"do not see a solution,"* offering four mitigations: multiple pGT versions per dataset, grouping methods by similarity to the reference, coarser thresholds, or **task-specific evaluation** (AR, robotic navigation).
>
> Practical consequence for this wiki: **hold rankings in this area loosely and capabilities firmly.** [LingBot-Map](../../entities/lingbot-map.md)'s KITTI and Oxford Spires SOTA claim inherits this and does not name its reference algorithm.

## Gaussian splats as a training environment, not just a viewer

[Niantic + Flexion + NVIDIA](../../sources/niantic-flexion-nvidia-sim2real.md) use a 3DGS reconstruction as **the renderer inside an RL loop** — fast enough for massively parallel training on a single GPU, with the **collision mesh derived from the same reconstruction so the two agree by construction**. The failure mode that design removes is worth remembering generally: *"a small mismatch between a rendered wall and a collision wall can teach a humanoid to slide through obstacles it can see."*

An RGB policy trained this way **beat a depth baseline and transferred zero-shot** to a real office. That is a different requirement from mapping — throughput and viewpoint generalisation matter more than fidelity to any one view — and it is the strongest robotics argument for this whole representation.

## What this wiki still lacks here

> [!warning] Uncovered adjacent territory, named honestly
> **NeRF**, **Gaussian splatting** as a method (rather than a Niantic product feature), **ORB-SLAM / visual-inertial odometry**, **factor graphs** as a formalism, and **Frank Dellaert**'s lineage all have **no pages**. [GTSAM](../../entities/gtsam.md) and [RTAB-Map](../../entities/rtab-map.md) are stubs written from other papers' methods sections, with **no primary source ingested for either**.
>
> That is a real hole for a wiki whose active project plans depend on this layer. It is recorded rather than quietly filled because filling it properly means ingesting primaries, not paraphrasing.

## Relation to world models

Both build a model of the environment; they differ in what the model is *for*.

| | Visual relocalization / mapping | [World models](../world-models/world-model.md) |
|---|---|---|
| Question | where am I, what shape is this place | what happens if I act |
| Output | geometry + pose | predicted future observations or latents |
| Evaluated on | reconstruction error, pose accuracy | [rollout fidelity, action-following](../world-models/world-model-evaluation.md) |
| Fails by | drift, loop-closure failure | compounding prediction error, hallucination |

They are complementary rather than competing — a robot plausibly wants both — and this wiki has essentially no source that uses them together.

## Key references

- [Niantic Spatial research page](../../sources/niantic-spatial-research.md) — the ACE → feed-forward relocalization arc
- [LingBot-Map GitHub](../../sources/lingbot-map-github.md) — feed-forward streaming reconstruction
- [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) — the wiki's only measured cheap-robot SLAM deployment

## Related concepts

- [Motion planning](motion-planning.md) · [Task and motion planning](task-and-motion-planning.md) · [Control abstraction levels](control-abstraction-levels.md)
- [World models](../world-models/world-model.md) — the adjacent tradition

## Mentioned in

- [Niantic Spatial research page](../../sources/niantic-spatial-research.md)
- [LingBot-Map GitHub repository](../../sources/lingbot-map-github.md)
