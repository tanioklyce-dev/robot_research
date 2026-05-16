---
title: DINO-WM
type: entity
subtype: model
created: 2026-05-07
updated: 2026-05-16
sources: 16
tags: [dino-wm, dinov2, world-model, jepa-adjacent, lecun, pinto, nyu, meta-fair]
---

**DINO-WM** — "World Models on Pre-trained Visual Features enable Zero-shot Planning." From [FAIR](meta-fair.md) (LeCun) and NYU (Lerrel Pinto), introduced in [Zhou et al. (Nov 2024)](../sources/dino-wm-paper.md). Models visual dynamics in **DINOv2 patch-feature space** with a frozen pretrained encoder + learned predictor — JEPA-adjacent (predicts in latent space) but **not strictly JEPA** (encoder frozen, not co-trained).

## Approach
- Frozen DINOv2 encoder produces patch features.
- Learned dynamics model predicts next-step features given action.
- **Zero-shot planning** via action-sequence optimization against observational goals.
- "Without expert demonstrations, reward modeling, or pre-learned inverse models" (paper abstract).

## Environments
Six core environments per the project page (https://dino-wm.github.io/):

- **PushT** — 2D pushing benchmark.
- **Wall** — navigation in walled environments.
- **PointMaze** — point-mass maze navigation.
- **Rope** — deformable rope manipulation.
- **Granular** — multi-particle / granular media.
- **Reacher** — joint-space reaching.

Plus eval variants: **WallRandom, PushObj, GranularRandom, DM Control Reacher**, and **CLEVRER** (unconditioned world modeling).

> [!note] Physics engine
> Secondary research identifies underlying physics as **[MuJoCo](mujoco.md) 2.1**. Project page does not state this; treat as wiki-internal claim until confirmed against paper body.

## Why it matters
- **Lightweight-sim JEPA-adjacent baseline.** Cited as a baseline in both [LeWM](../sources/leworldmodel-paper.md) and [JEPA-WMs (Terver et al.)](../sources/jepa-wms-paper.md) — meaning DINO-WM is the comparison every later JEPA-style robotics paper has to beat.
- **Different design point from LeWM.** DINO-WM uses a frozen pretrained DINOv2 encoder; LeWM trains the encoder end-to-end with SIGReg. The two stake out the "frozen pretrained" vs "end-to-end" axis of the JEPA-style world-model design space.

## Related
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — JEPA-adjacent architecture.
- [Learned latent space](../concepts/world-models/latent-space.md) — DINO-WM models dynamics in *frozen DINOv2 patch-feature space*; the latent is inherited, not learned.
- [DINO-world](dino-world.md) — sibling DINOv2-feature world-model line from FAIR (Baldassarre et al. 2025).
- [LeWorldModel](leworldmodel.md) — end-to-end JEPA contrast.
- [V-JEPA 2](v-jepa-2.md) — full JEPA contrast.
- [Meta FAIR](meta-fair.md) — co-affiliation.
- [MuJoCo](mujoco.md) — likely physics backend.

## Mentioned in
- [DINO-WM Paper](../sources/dino-wm-paper.md)
- [LeWorldModel Paper](../sources/leworldmodel-paper.md) — cites DINO-WM as baseline
- [LeWorldModel GitHub](../sources/lewm-github.md) — DINO-WM listed as baseline
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md) — cites DINO-WM as baseline
- [DINO-world Paper](../sources/dino-world-paper.md) — sibling DINOv2-feature world-model line
- [VLA-JEPA Paper](../sources/vla-jepa-paper.md) — DINO-WM as comparator
