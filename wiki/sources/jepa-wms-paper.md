---
title: JEPA-WMs Paper (Terver et al. 2025)
type: source
url: https://arxiv.org/abs/2512.24497
code: https://github.com/facebookresearch/jepa-wms
dataset: https://huggingface.co/datasets/facebook/jepa-wms
local_path: null
author: Basile Terver, Tsung-Yen Yang, Jean Ponce, Adrien Bardes, Yann LeCun
affiliations: FAIR at Meta (inferred from senior authors and code namespace)
published: 2025-12-30
revised: 2026-01-08
ingested: 2026-05-07
tags: [jepa, world-model, jepa-wms, robocasa, metaworld, droid, franka, fair, meta-fair]
---

## Summary
"What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?" — preprint from [FAIR at Meta](../entities/meta-fair.md) investigating which architectural and training choices in [JEPA](../concepts/jepa.md)-style world models actually drive planning performance. Authors include **Adrien Bardes** and **Yann LeCun**, both senior authors on [V-JEPA 2](v-jepa-2-paper.md). The paper is the **first JEPA-for-robotics work this wiki has ingested that explicitly trains and evaluates inside [RoboCasa](../entities/robocasa.md)**, alongside Metaworld, Push-T, Wall, PointMaze, DROID, and a real Franka — and it directly contradicts the [earlier "JEPA skips heavy sim" synthesis](../syntheses/why-jepa-research-skips-the-simulator-stack.md) from this wiki.

## Key claims
- Investigates technical choices — model architecture, training objectives, planning algorithms — across JEPA-WMs.
- Proposed model **outperforms DINO-WM and V-JEPA 2-AC** on navigation and manipulation tasks (per abstract).
- Explicit experimental setup: "experiments using both simulated environments and real-world robotic data" (abstract).
- The repo README enumerates the actual environment list:
  - **42 Metaworld tasks** (100 episodes each)
  - **Push-T** trajectories
  - **PointMaze** navigation trajectories
  - **Wall** environment trajectories
  - **RoboCasa kitchen manipulation**
  - **[DROID](../entities/droid.md)** dataset (raw, stereo HD, 8.7 TB; or non-stereo HD, 5.6 TB)
  - **Franka** robot trajectories with "unroll decode evaluation"
- Optional pretraining video datasets: **Kinetics-400, Kinetics-710, Something-Something-v2, HowTo100M**.
- Pretrained weights provided per environment.
- Code: https://github.com/facebookresearch/jepa-wms
- HF dataset: https://huggingface.co/datasets/facebook/jepa-wms
- DOI: https://doi.org/10.48550/arXiv.2512.24497

> [!note] Affiliations not stated on arxiv abstract page
> Senior authors LeCun and Bardes are FAIR; the GitHub repo lives in `facebookresearch/`. Treating as FAIR work in the wiki, but the full author affiliation list is not on the abstract.

## Entities mentioned
- [Meta FAIR](../entities/meta-fair.md) — inferred lab.
- [JEPA-WMs](../entities/jepa-wms.md) — model family this paper introduces (entity created as a result of this ingest).
- [V-JEPA 2](../entities/v-jepa-2.md) — baseline.
- [DINO-WM](../entities/dino-wm.md) — baseline.
- [RoboCasa](../entities/robocasa.md) — manipulation eval.
- [DROID](../entities/droid.md) — real-robot dataset (raw stereo HD or non-stereo HD).
- [Metaworld](../entities/metaworld.md) — 42 tasks × 100 episodes used as eval data.
- [PushT](../entities/pusht.md) — included in env list.
- [Franka Panda](../entities/franka-panda.md) — real-robot eval platform (unroll decode evaluation).
- [DINOv2](../entities/dinov2.md) — likely frozen-feature substrate (continuation of DINO-world's design).
- [Yann LeCun](../entities/yann-lecun.md) — co-senior author.
- [Adrien Bardes](../entities/adrien-bardes.md) — co-senior author.
- [Basile Terver](../entities/basile-terver.md) — first author; bread-crumb from DINO-world.

## Concepts touched
- [Joint-Embedding Predictive Architecture](../concepts/jepa.md) — architecture family.
- [World model](../concepts/world-model.md) — physical-planning-with-world-model focus.
- [World-model simulators](../concepts/world-model-simulators.md) — latent-prediction paradigm.
- [Sim-to-real transfer](../concepts/sim-to-real-transfer.md) — sim + real-world robot evaluation in the same paper.

## Open questions
- The abstract is generic ("simulated environments and real-world robotic data") and does not enumerate environments — the specific list comes from the GitHub README. A full-paper read may surface additional environments or design rationale.
- No explicit reasoning given (in abstract) for why this paper *did* go into RoboCasa when prior FAIR JEPA work (V-JEPA 2) skipped sim entirely. The shift is observable but not justified in the abstract.
- Author affiliations are inferred — confirm with paper body.
- How the proposed JEPA-WM differs architecturally from V-JEPA 2-AC and DINO-WM — abstract gives outcomes, not specifics.

## Why this matters
This paper is the load-bearing evidence that **the FAIR JEPA research line is moving into heavy sim** — RoboCasa is the same household-manipulation benchmark used by [GR00T](../entities/nvidia-groot.md), [Robot Utility Models](../entities/robot-utility-models.md), and the broader VLA cohort. The pattern observed in [V-JEPA 2](v-jepa-2-paper.md) (no sim) and [LeWorldModel](leworldmodel-paper.md) (lightweight benches only) is breaking inside FAIR itself, within ~6 months of the V-JEPA 2 release. See [the revised synthesis](../syntheses/why-jepa-research-skips-the-simulator-stack.md) for the structural read.
