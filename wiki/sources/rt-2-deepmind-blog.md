---
title: "RT-2: New model translates vision and language into action (DeepMind blog)"
type: source
url: https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/
author: Yevgen Chebotar, Tianhe Yu (with 40+ acknowledged contributors)
venue: Google DeepMind blog
published: 2023-07-28
ingested: 2026-08-04
format: html
tags: [rt-2, vla, google-deepmind, announcement, emergent-capabilities, vendor-communication]
---

# RT-2: New model translates vision and language into action (DeepMind blog)

The public announcement of [RT-2](rt-2-paper.md), published four days before the paper. Ingested alongside the paper mainly as a **communication artifact** — it is the document that put "vision-language-action model" into general circulation, and its numbers diverge from the paper's in one instructive way.

## Summary

Frames RT-2 as *"building upon Robotic Transformer 1"* — a VLM adapted to robot control that acquires capability *"beyond the robotic data it was exposed to."* The emphasis is squarely on **emergent semantic ability** rather than dexterity: a rock chosen as an improvised hammer, an energy drink for someone tired, and the widely-circulated *"move coke can to Taylor Swift."*

## Numbers as stated

| Claim | Blog | Paper |
|---|---|---|
| Evaluation scale | 6,000+ robotic trials | 6,000 (agrees) |
| **Generalization improvement** | **"3x… versus prior baselines"** | **"∼2x over the next two baselines"** (62 vs 32/35) |
| Emergent-skill average | ~60% | agrees (3× over next best) |
| Symbol understanding (PaLI-X) | 80%+ | agrees |
| Unseen-scenario performance | RT-1 32% → RT-2 62% | agrees (Table 4) |
| Language-Table (sim) | 90% | agrees (Table 1) |

> [!warning] Contradiction — the 3× generalization claim
> The blog's headline **3× generalization** figure does not appear in the paper, which reports **~2×** for generalization (62 vs 32/35 unseen average) and reserves **3×** for the separate *emergent-capability* evaluation. Every other number checks out against the paper. This looks like the emergent-eval figure being promoted into the generalization headline during write-up.
>
> **Use 2× for generalization, 3× for emergent skills**, and treat the blog as secondary wherever the two disagree. Recorded because the wiki cites vendor blogs often, and this is a clean, small, verifiable instance of the drift they introduce — the same care the [GR00T 1.7](nvidia-isaac-teleop-gr00t17-lerobot-blog.md) and [Gemini Robotics 2](gemini-robotics-2-blog.md) blog ingests required.

## What the blog omits

- **No inference-rate disclosure.** The paper's *"1–3 Hz… multi-TPU cloud service queried over the network"* — arguably the most consequential deployment fact about RT-2 — does not appear. A reader of the blog alone would not know the model cannot run on the robot.
- **No limitations section.** The paper states plainly that physical skills remain bounded by robot data; the blog does not.
- **No mention that nothing is released.**

This asymmetry is itself the reason the wiki prefers primary sources: the blog is accurate about what RT-2 *can do* and silent about what it *costs*.

## Entities mentioned
- [RT-2](../entities/rt-2.md) · [RT-1](../entities/rt-1.md) · [Google DeepMind](../entities/google-deepmind.md)

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md)
