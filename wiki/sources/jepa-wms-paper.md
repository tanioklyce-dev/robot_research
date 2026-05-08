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
"What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?" — preprint from [[meta-fair|FAIR at Meta]] investigating which architectural and training choices in [[jepa|JEPA]]-style world models actually drive planning performance. Authors include **Adrien Bardes** and **Yann LeCun**, both senior authors on [[v-jepa-2-paper|V-JEPA 2]]. The paper is the **first JEPA-for-robotics work this wiki has ingested that explicitly trains and evaluates inside [[robocasa|RoboCasa]]**, alongside Metaworld, Push-T, Wall, PointMaze, DROID, and a real Franka — and it directly contradicts the [[why-jepa-research-skips-the-simulator-stack|earlier "JEPA skips heavy sim" synthesis]] from this wiki.

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
  - **[[droid|DROID]]** dataset (raw, stereo HD, 8.7 TB; or non-stereo HD, 5.6 TB)
  - **Franka** robot trajectories with "unroll decode evaluation"
- Optional pretraining video datasets: **Kinetics-400, Kinetics-710, Something-Something-v2, HowTo100M**.
- Pretrained weights provided per environment.
- Code: https://github.com/facebookresearch/jepa-wms
- HF dataset: https://huggingface.co/datasets/facebook/jepa-wms
- DOI: https://doi.org/10.48550/arXiv.2512.24497

> [!note] Affiliations not stated on arxiv abstract page
> Senior authors LeCun and Bardes are FAIR; the GitHub repo lives in `facebookresearch/`. Treating as FAIR work in the wiki, but the full author affiliation list is not on the abstract.

## Entities mentioned
- [[meta-fair|Meta FAIR]] — inferred lab.
- [[jepa-wms|JEPA-WMs]] — model family this paper introduces (entity created as a result of this ingest).
- [[v-jepa-2|V-JEPA 2]] — baseline.
- [[dino-wm|DINO-WM]] — baseline.
- [[robocasa|RoboCasa]] — manipulation eval.
- [[droid|DROID]] — real-robot dataset (raw stereo HD or non-stereo HD).
- [[metaworld|Metaworld]] — 42 tasks × 100 episodes used as eval data.
- [[pusht|PushT]] — included in env list.
- [[franka-panda|Franka Panda]] — real-robot eval platform (unroll decode evaluation).
- [[dinov2|DINOv2]] — likely frozen-feature substrate (continuation of DINO-world's design).
- [[yann-lecun|Yann LeCun]] — co-senior author.
- [[adrien-bardes|Adrien Bardes]] — co-senior author.
- [[basile-terver|Basile Terver]] — first author; bread-crumb from DINO-world.

## Concepts touched
- [[jepa|Joint-Embedding Predictive Architecture]] — architecture family.
- [[world-model|World model]] — physical-planning-with-world-model focus.
- [[world-model-simulators|World-model simulators]] — latent-prediction paradigm.
- [[sim-to-real-transfer|Sim-to-real transfer]] — sim + real-world robot evaluation in the same paper.

## Open questions
- The abstract is generic ("simulated environments and real-world robotic data") and does not enumerate environments — the specific list comes from the GitHub README. A full-paper read may surface additional environments or design rationale.
- No explicit reasoning given (in abstract) for why this paper *did* go into RoboCasa when prior FAIR JEPA work (V-JEPA 2) skipped sim entirely. The shift is observable but not justified in the abstract.
- Author affiliations are inferred — confirm with paper body.
- How the proposed JEPA-WM differs architecturally from V-JEPA 2-AC and DINO-WM — abstract gives outcomes, not specifics.

## Why this matters
This paper is the load-bearing evidence that **the FAIR JEPA research line is moving into heavy sim** — RoboCasa is the same household-manipulation benchmark used by [[nvidia-groot|GR00T]], [[robot-utility-models|Robot Utility Models]], and the broader VLA cohort. The pattern observed in [[v-jepa-2-paper|V-JEPA 2]] (no sim) and [[leworldmodel-paper|LeWorldModel]] (lightweight benches only) is breaking inside FAIR itself, within ~6 months of the V-JEPA 2 release. See [[why-jepa-research-skips-the-simulator-stack|the revised synthesis]] for the structural read.
