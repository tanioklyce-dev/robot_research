---
title: "A Careful Examination of Large Behavior Models for Multitask Dexterous Manipulation (TRI LBM paper)"
type: source
url: https://toyotaresearchinstitute.github.io/lbm1/
author: TRI LBM Team (82 authors; leadership incl. Rares Ambrus, Ben Burchfiel, Hadas Kress-Gazit, Siyuan Feng, Russ Tedrake)
published: 2025-07-07 (arXiv 2507.05331); Science Robotics 2026
ingested: 2026-07-08
venue: Science Robotics (2026); arXiv cs.RO
format: web (project page + arXiv abstract; PDF not ingested)
tags: [lbm, tri, diffusion-policy, multitask, manipulation, evaluation, statistics, franka, drake, pretraining]
---

# A Careful Examination of Large Behavior Models for Multitask Dexterous Manipulation (TRI LBM paper)

## Summary

The primary source for [TRI](../entities/tri.md)'s **[Large Behavior Model](../concepts/learning/large-behavior-models.md)** program — the wiki's most-flagged missing ingest since the [TRI website page](tri-website.md). An 82-author, [Tedrake](../entities/russ-tedrake.md)-led study that **extends the [Diffusion Policy](../entities/diffusion-policy.md) paradigm to multitask scale** (~1,700 h of mixed robot data) and — the actual headline — builds a **statistically rigorous evaluation pipeline** (blind randomized A/B trials, sequential hypothesis testing, Clopper-Pearson CIs; 1,800 real + 47,000+ sim rollouts) to measure what pretraining buys. Findings: multitask pretraining makes policies **more successful and robust** and teaches new tasks with **3–5× less fine-tuning data**; performance improves **smoothly and predictably** with pretraining scale ("no discontinuities"); **zero-shot (un-fine-tuned) performance is weak**, attributed partly to language steerability; and **subtle choices like data normalization often dominate architecture/algorithm changes**.

## Key claims

**Model & data**
- Architecture: diffusion transformer — multimodal ViT vision-language encoders + transformer denoising head with **AdaLN conditioning**; inputs = wrist cameras (2/arm), scene cameras, proprioception, language prompt; output = **16-timestep action chunks (1.6 s)**. Notably **not a VLA** (no uptrained VLM backbone) — consistent with Tedrake's [LBM ⊃ VLA taxonomy](../concepts/learning/large-behavior-models.md).
- Pretraining corpus ~**1,695 h**: 468 h internal bimanual teleop + 45 h sim teleop + **32 h [UMI](../entities/umi.md)** + ~1,150 h [Open X-Embodiment](../entities/open-x-embodiment.md) internet data.
- Hardware: bimanual **Franka Panda FR3** stations, up to 6 cameras; sim = **Drake** ([Tedrake](../entities/russ-tedrake.md)'s library — the model-based stack underwriting the learning study).

**Evaluation methodology (the paper's core contribution)**
- 29 tasks / 4,200+ rollouts headline eval: 16 sim seen + 3 real seen + 5 sim unseen long-horizon + 5 real unseen long-horizon; ≥50 rollouts per real task, ≥200 per sim task.
- **Blind, randomized A/B testing** in the real world with controlled/synchronized initial conditions across sim and real; sequential hypothesis testing; Clopper-Pearson intervals.
- Sobering calibration for the whole field: **with 50 rollouts, the CI width is generally 20–30% absolute success rate** — i.e. most robot-learning papers' eval sample sizes cannot statistically distinguish the methods they rank.

**Findings**
- Multitask pretraining → more successful and robust single-task performance, and novel long-horizon tasks learnable with **3–5× less data** than single-task-from-scratch baselines.
- Smooth, predictable improvement with pretraining scale and diversity — the "initial scaling laws" [Tedrake described on the podcast](automated-podcast-tedrake-rocket-ship.md); no phase transitions observed at this scale.
- Zero-shot (pretrained, un-fine-tuned) results mixed/weak — language steerability named as a partial cause.
- "Subtle design choices like data normalization can have large effects on performance, often dominating architectural or algorithmic changes."
- Demo tasks include apple coring/cutting, bike-rotor installation, breakfast-table setup.

## Entities mentioned

- [TRI](../entities/tri.md) — sole affiliation (82 authors). [Russ Tedrake](../entities/russ-tedrake.md) — senior author; also [Diffusion Policy](../entities/diffusion-policy.md)-cohort names (Cousineau, Burchfiel, Feng).
- [UMI](../entities/umi.md) — 32 h of its data in the pretraining mix; [Open X-Embodiment](../entities/open-x-embodiment.md) — bulk of corpus hours.
- Franka Panda FR3 (no entity page); Drake (anchored on [Tedrake](../entities/russ-tedrake.md)).

## Concepts touched

- [Large behavior models](../concepts/learning/large-behavior-models.md) — **primary source**.
- [VLA models](../concepts/learning/vla-models.md) — contrast case: an LBM that is not a VLA.
- [Imitation learning](../concepts/learning/imitation-learning.md), [Scaling laws — VLAs](../concepts/learning/scaling-laws-vla.md) — smooth-scaling evidence from a non-VLA generalist policy.

## Open questions

- Full PDF not ingested (project page + abstract only) — per-task success tables, ablations, and the sequential-testing math would reward a deep read.
- How LBM 1.0's non-VLA architecture relates to whatever [Tedrake's stealth startup](../entities/russ-tedrake.md) builds (he now argues video backbones win for long context — a shift from this paper's ViT-encoder design?).
- Whether the 20–30%-CI-at-50-rollouts point has changed evaluation practice elsewhere (cf. [RoboCasa365](robocasa365-paper.md)'s large-N sim eval, which cites TRI LBM as a baseline).
- "LBM 1" naming implies an LBM 2 — unannounced as of ingest.
