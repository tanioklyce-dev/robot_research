---
title: DINO-WM Paper
type: source
url: https://arxiv.org/abs/2411.04983
project_page: https://dino-wm.github.io/
local_path: null
author: Gaoyue Zhou, Hengkai Pan, Yann LeCun, Lerrel Pinto
affiliations: NYU (Pinto lab), Meta FAIR (LeCun)
published: 2024-11-07
revised: 2025-02-01
ingested: 2026-05-07
tags: [dino-wm, world-model, dinov2, jepa-adjacent, zero-shot-planning, lecun, pinto, mujoco]
---

## Summary
**DINO-WM** — "World Models on Pre-trained Visual Features enable Zero-shot Planning." From [FAIR](../entities/meta-fair.md) (LeCun) and NYU (Pinto). Models visual dynamics in **DINOv2 patch-feature space** rather than reconstructing pixels — JEPA-adjacent in spirit (predict in latent space) but uses a **frozen pre-trained encoder** rather than the end-to-end training [LeWorldModel](../entities/leworldmodel.md) later argued for. Cited as a baseline in both [LeWM](leworldmodel-paper.md) and [JEPA-WMs (Terver et al.)](jepa-wms-paper.md).

## Key claims
- Models visual dynamics **without reconstructing the visual world** by leveraging pretrained DINOv2 patch features.
- Enables **zero-shot planning on observational goals** through action sequence optimization.
- "Without expert demonstrations, reward modeling, or pre-learned inverse models" (abstract).
- Six environments per project page: **PushT, Wall, PointMaze, Rope, Granular, Reacher**.
- Additional eval environments: **WallRandom, PushObj, GranularRandom, DM Control Reacher, CLEVRER** (unconditioned world modeling).
- DOI: https://doi.org/10.48550/arXiv.2411.04983

> [!note] Physics engine not confirmed on project page
> Secondary research from the agent's pass identifies the underlying physics as **MuJoCo 2.1**. The official project page does not state this; treat as a wiki-internal claim until confirmed against the paper body.

## Entities mentioned
- [DINO-WM](../entities/dino-wm.md) — model itself (entity created with this ingest).
- [Meta FAIR](../entities/meta-fair.md) — co-affiliation.
- [MuJoCo](../entities/mujoco.md) — likely physics backend.
- [DINOv2](../entities/dinov2.md) — frozen encoder used as patch-feature substrate.
- [PushT](../entities/pusht.md) — one of the six core eval environments.
- [Yann LeCun](../entities/yann-lecun.md) — co-senior author.
- [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) — referenced as platform context (no direct training there).

## Concepts touched
- [Joint-Embedding Predictive Architecture](../concepts/jepa.md) — JEPA-adjacent: predicts in DINOv2 latent space, but uses a frozen encoder rather than learning the encoder end-to-end.
- [World model](../concepts/world-model.md) — frozen-foundation-feature design point.
- [World-model simulators](../concepts/world-model-simulators.md) — latent-prediction paradigm.

## Open questions
- Exact physics-engine confirmation needed.
- Code repository link not surfaced on project page; check for `gaoyuezhou/dino_wm` or similar on GitHub.
- How the pretrained-DINOv2 design point compares quantitatively to LeWM's end-to-end + SIGReg approach (LeWM claims ~48× faster planning; DINO-WM does not give a comparable number).

## Why this matters
DINO-WM is a **lightweight-sim** JEPA-adjacent world model — fits the original "JEPA skips heavy sim" pattern. PushT/Wall/PointMaze/Rope/Granular/Reacher are classic 2D/3D control benches, not [RoboCasa](../entities/robocasa.md)/[ManiSkill](../entities/maniskill.md)/[Isaac Lab](../entities/nvidia-isaac-lab.md). So DINO-WM **supports the lightweight-sim half** of the original synthesis even as Terver et al. break the no-sim half.
