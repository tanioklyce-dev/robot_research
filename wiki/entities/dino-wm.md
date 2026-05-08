---
title: DINO-WM
type: entity
subtype: model
created: 2026-05-07
updated: 2026-05-07
sources: 1
tags: [dino-wm, dinov2, world-model, jepa-adjacent, lecun, pinto, nyu, meta-fair]
---

**DINO-WM** — "World Models on Pre-trained Visual Features enable Zero-shot Planning." From [[meta-fair|FAIR]] (LeCun) and NYU (Lerrel Pinto), introduced in [[dino-wm-paper|Zhou et al. (Nov 2024)]]. Models visual dynamics in **DINOv2 patch-feature space** with a frozen pretrained encoder + learned predictor — JEPA-adjacent (predicts in latent space) but **not strictly JEPA** (encoder frozen, not co-trained).

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
> Secondary research identifies underlying physics as **[[mujoco|MuJoCo]] 2.1**. Project page does not state this; treat as wiki-internal claim until confirmed against paper body.

## Why it matters
- **Lightweight-sim JEPA-adjacent baseline.** Cited as a baseline in both [[leworldmodel-paper|LeWM]] and [[jepa-wms-paper|JEPA-WMs (Terver et al.)]] — meaning DINO-WM is the comparison every later JEPA-style robotics paper has to beat.
- **Different design point from LeWM.** DINO-WM uses a frozen pretrained DINOv2 encoder; LeWM trains the encoder end-to-end with SIGReg. The two stake out the "frozen pretrained" vs "end-to-end" axis of the JEPA-style world-model design space.

## Related
- [[jepa|Joint-Embedding Predictive Architecture]] — JEPA-adjacent architecture.
- [[dino-world|DINO-world]] — sibling DINOv2-feature world-model line from FAIR (Baldassarre et al. 2025).
- [[leworldmodel|LeWorldModel]] — end-to-end JEPA contrast.
- [[v-jepa-2|V-JEPA 2]] — full JEPA contrast.
- [[meta-fair|Meta FAIR]] — co-affiliation.
- [[mujoco|MuJoCo]] — likely physics backend.

## Mentioned in
- [[dino-wm-paper|DINO-WM Paper]]
