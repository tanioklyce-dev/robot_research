---
title: "Gemini Robotics On-Device 2 — model card"
type: source
url: https://deepmind.google/models/model-cards/gemini-robotics-on-device-2/
author: Google DeepMind
affiliation: Google DeepMind
published: 2026-07-30
ingested: 2026-08-03
venue: deepmind.google model card
format: model card
tags: [gemini-robotics, on-device, vla, edge-inference, model-card, gemma, so-arm101, vendor-source]
---

## Summary

The official model card for **[Gemini Robotics On-Device 2](../entities/gemini-robotics.md)** — partially closing the backlog's "highest-value single fact" item. It supplies **architecture lineage, v1→v2 success numbers (including on [SO101](../entities/so-arm101.md)), and a stated limitation**, but still **no parameter count, memory footprint, hardware spec, or control rate**.

## Key claims

- **Architecture:** built on "Gemini Robotics 1.5 technology and our on-device **Gemma** models." Inputs: text, images, robot proprioception; outputs: robot actions as numerical values. Trained on TPUs.
- **v1 → v2 evaluation** (the card's one results table):

| Platform | GRoD v1 | **GRoD v2** |
|---|---:|---:|
| **SO101** | 6.7% | **53.3%** |
| **Dexmate** | 33.3% | **75.6%** |

- **Stated limitation:** "Limited in its ability to generalise to out of distribution tasks as well as **controlling high-degree-of-freedom robots**" — i.e. the on-device tier is explicitly *not* the whole-body-humanoid tier.
- Distribution: **Trusted Testers only**. Adaptation claim (from the [product page](deepmind-gemini-robotics-model-page.md)/[blog](gemini-robotics-2-blog.md)): new embodiments in a few hours, typically **<200 examples**.

> [!note] The v1 baseline confirms the wiki's one prior data point
> The wiki's only earlier GRoD number was **0.09 Franka visual-gen** (vs GR 1.5's 0.77) from the [1.5 report](gemini-robotics-1-5-report.md) — the on-device tier generalized very poorly. The card's own v1 numbers (6.7% SO101, 33.3% Dexmate) are consistent with that picture, and v2's jump (+46.6 pp on SO101) is the real story: **the on-device tier went from unusable to plausibly useful on the low-cost arm class in one generation.** No trial counts published, per the usual [audit](../syntheses/platforms/vla-success-rate-audit.md) caveat.

> [!note] The ~0.25 s latency figure is third-party, not official
> A hands-on tutorial (binaryverseai.com) reports closed-loop latency "around a quarter of a second" (~4 Hz) — a plausible [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) Band-C figure, but it appears **nowhere in the model card or product page**. Recorded here as unofficial; not added to the ladder table.

## Entities mentioned
- [Google DeepMind](../entities/google-deepmind.md) · [Gemini Robotics](../entities/gemini-robotics.md) · [SO-ARM101](../entities/so-arm101.md) (SO101) · [Gemma 4](../entities/gemma4.md) (the on-device Gemma line)

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) · [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md)

## Open questions
- **Parameter count, memory footprint, target compute, and control rate remain unpublished** — the envelope is still not placeable on the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) or the [Jetson ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md). "On-device Gemma" suggests the [Gemma 4 edge](nvidia-gemma-4-edge-blog.md) size class (E2B/E4B), but that is inference, not fact.
- What robot is "Dexmate", and at what trial counts were 53.3%/75.6% measured? Neither stated.

## Related sources
- [Gemini Robotics 2 blog](gemini-robotics-2-blog.md) · [model page](deepmind-gemini-robotics-model-page.md) — the announcement tier.
- [Gemini Robotics 1.5 report](gemini-robotics-1-5-report.md) — source of the v1 GRoD baseline picture.
