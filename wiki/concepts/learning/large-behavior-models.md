---
title: Large Behavior Models (LBMs)
type: concept
created: 2026-07-08
updated: 2026-07-08
sources: 3
tags: [lbm, large-behavior-model, tri, vla, diffusion-policy, multitask, foundation-model, manipulation]
---

# Large Behavior Models (LBMs)

**Large Behavior Model** — [TRI](../../entities/tri.md)'s term (by analogy to LLMs) for **any large model that takes sequences of images in and outputs robot actions**. On [Russ Tedrake](../../entities/russ-tedrake.md)'s definition, LBM is the *superclass* and a [VLA](vla-models.md) is one architectural choice within it — the choice of uptraining a vision-language model into a robot model. Starting from a **video / world-model backbone** instead is the other main choice, which he argues wins "if you want longer context lengths" ([Automated Podcast, 2026-07](../../sources/automated-podcast-tedrake-rocket-ship.md)).

## Lineage

"Large behavior models was the **multitask version of [Diffusion Policy](../../entities/diffusion-policy.md)**, in my vernacular" ([Tedrake](../../sources/automated-podcast-tedrake-rocket-ship.md)) — i.e. the LBM program extended the single-task diffusion-policy recipe across a large corpus of simulated and real robot data, with TRI's contribution framed as the **"science of LBMs"**: initial scaling laws and rigorous, statistically-grounded evaluation at an experiment scale neither startups nor academia would fund. The headline empirical finding: **multitask pre-training substantively improves robustness on individual tasks** — capabilities transfer in from other tasks ([podcast](../../sources/automated-podcast-tedrake-rocket-ship.md); primary paper at toyotaresearchinstitute.github.io/lbm1, **not yet ingested**).

## Key references

- **TRI LBM paper** ("A Careful Examination of Large Behavior Models…", 2025) — the primary source; still a wanted ingest (flagged since the [TRI website](../../sources/tri-website.md) page). Referenced as a baseline in [RoboCasa365](../../sources/robocasa365-paper.md).
- [Automated Podcast interview](../../sources/automated-podcast-tedrake-rocket-ship.md) — the definitional/taxonomic source.
- [Diffusion Policy paper](../../sources/diffusion-policy-paper.md) — the single-task ancestor.

## Related concepts

- [VLA models](vla-models.md) — the dominant LBM subtype; the wiki's main page for concrete systems (GR00T, π-line, SmolVLA…).
- [World-action models](../world-models/world-action-model.md) — the video-backbone LBM path made concrete ([Cosmos 3](../../entities/nvidia-cosmos.md)'s policy mode is the wiki's clearest instance).
- [Imitation learning](imitation-learning.md), [Scaling laws — VLAs](scaling-laws-vla.md).

## Current state

The term is TRI-house vocabulary that is escaping into general use (RoboCasa365 uses "large behavior models" for multitask manipulation policies generally; [Tedrake's stealth startup](../../entities/russ-tedrake.md) apparently carries it in its name). In practice the field's public systems are almost all the VLA subtype; the video-backbone alternative Tedrake advocates is so far best evidenced by [Cosmos 3's](../../entities/nvidia-cosmos.md) policy mode topping RoboArena. Whether "LBM" displaces "VLA" as the umbrella term likely depends on his startup's visibility.

## Mentioned in

- [Automated Podcast — Tedrake](../../sources/automated-podcast-tedrake-rocket-ship.md)
- [TRI Website](../../sources/tri-website.md)
- [RoboCasa365 Paper](../../sources/robocasa365-paper.md) — LBM as baseline class.
