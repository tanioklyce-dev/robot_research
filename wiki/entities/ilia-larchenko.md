---
title: Ilia Larchenko
type: entity
subtype: person
created: 2026-09-07
updated: 2026-09-07
sources: 2
tags: [person, practitioner, competition, lehome, behavior-1k, rl, vla, pi0.5, so-arm101]
---

**Ilia Larchenko** — independent robot-learning practitioner and YouTube educator; winner of the simulation round (1st of 62) and runner-up in the real-world final of the [LeHome Challenge 2026](lehome-challenge-2026.md), and first author, with G. Zarin and A. Karnatak, of the **1st-place solution to the BEHAVIOR-1K Challenge 2025** (arXiv 2512.06951) (the source of the wiki's [12.4 % full-task](behavior-benchmark.md) figure). He open-sources everything: code, tech reports, checkpoints, and hour-long explanations of *why* each choice was made.

## Why he is in this wiki

He is the wiki's first **competition practitioner** voice: someone who takes a frontier recipe ([π0.5](physical-intelligence.md) + [RECAP](pistar06.md)), rebuilds it on a single H200 and a consumer GPU, and reports what mattered and what he never ablated. The [LeHome Part 1 video](../sources/larchenko-lehome-part1-rl-for-vlas.md) is the wiki's only first-person account of RL-post-training a flow-matching VLA, and it runs on the [SO-ARM101](so-arm101.md) stack this wiki already tracks.

## Recurring ideas across his solutions

- **The policy is its own value function** — auxiliary heads on the VLA replace a separate value model.
- **Task-defined world models** — predict the quantities the success criterion is built from (keypoint distances), not pixels or latents.
- **Asynchronous training and rollout through the Hugging Face Hub** — no process waits for another.
- **Image augmentation is underused in robotics** — his own 2019 augmentation tool article is still his reference.
- **A small "System 2" at episode start** (garment type in LeHome; task decomposition in BEHAVIOR) fed back as conditioning.

## Primaries not yet ingested

- BEHAVIOR-1K Challenge 2025 solution — arXiv 2512.06951; video `J4wpO0EdCZs`.
- Parts 2 and 3 of the LeHome series (reward/advantage/inference; sim-to-real/DAgger/ICRA final).

## Mentioned in

- [LeHome deep dive, Part 1](../sources/larchenko-lehome-part1-rl-for-vlas.md)
- [Learning to Fold — tech report](../sources/larchenko-learning-to-fold-tech-report.md) — the primary; includes the self-reported CUPED error and the units bug.
