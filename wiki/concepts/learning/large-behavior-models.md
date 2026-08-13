---
title: Large Behavior Models (LBMs)
type: concept
created: 2026-07-08
updated: 2026-07-15
sources: 5
tags: [lbm, large-behavior-model, tri, vla, diffusion-policy, multitask, foundation-model, manipulation, walden-robotics]
---

# Large Behavior Models (LBMs)

**Large Behavior Model** — [TRI](../../entities/tri.md)'s term (by analogy to LLMs) for **any large model that takes sequences of images in and outputs robot actions**. On [Russ Tedrake](../../entities/russ-tedrake.md)'s definition, LBM is the *superclass* and a [VLA](vla-models.md) is one architectural choice within it — the choice of uptraining a vision-language model into a robot model. Starting from a **video / world-model backbone** instead is the other main choice, which he argues wins "if you want longer context lengths" ([Automated Podcast, 2026-07](../../sources/automated-podcast-tedrake-rocket-ship.md)).

## Lineage

"Large behavior models was the **multitask version of [Diffusion Policy](../../entities/diffusion-policy.md)**, in my vernacular" ([Tedrake](../../sources/automated-podcast-tedrake-rocket-ship.md)) — i.e. the LBM program extended the single-task diffusion-policy recipe across a large corpus of simulated and real robot data, with TRI's contribution framed as the **"science of LBMs"**: initial scaling laws and rigorous, statistically-grounded evaluation at an experiment scale neither startups nor academia would fund.

The [primary paper](../../sources/tri-lbm-paper.md) (82 authors, Science Robotics 2026) delivers exactly that: a **diffusion transformer** (ViT VL encoders + AdaLN denoising head, 16-step/1.6 s action chunks — notably **not a VLA**) pretrained on ~1,695 h of mixed data (bimanual Franka teleop + sim + [UMI](../../entities/umi.md) + Open X-Embodiment), evaluated over 1,800 real + 47,000+ sim rollouts with blind randomized A/B trials and Clopper-Pearson CIs. Findings: **multitask pretraining improves success and robustness and cuts fine-tuning data 3–5×**; scaling is **smooth and predictable** (no discontinuities); **zero-shot is weak** (language steerability); **data-normalization-level choices often dominate architecture changes**. Its methodological warning shot: at 50 rollouts per task, success-rate CIs are **20–30 percentage points wide** — most published robot-learning comparisons are statistically underpowered.

## Key references

- **[TRI LBM paper](../../sources/tri-lbm-paper.md)** ("A Careful Examination of Large Behavior Models for Multitask Dexterous Manipulation", arXiv 2025-07 / Science Robotics 2026) — **the primary source** (ingested 2026-07-08). Referenced as a baseline in [RoboCasa365](../../sources/robocasa365-paper.md).
- [Automated Podcast interview](../../sources/automated-podcast-tedrake-rocket-ship.md) — the definitional/taxonomic source.
- [Diffusion Policy paper](../../sources/diffusion-policy-paper.md) — the single-task ancestor.

## Commercialization

As of **2026-07-15**, the LBM program has a named commercial vehicle: **[Walden Robotics](../../entities/walden-robotics.md)**, spun out of [TRI](../../entities/tri.md) and led by [Russ Tedrake](../../entities/russ-tedrake.md), with the TRI LBM leadership ([Ben Burchfiel](../../entities/ben-burchfiel.md), [Siyuan Feng](../../entities/siyuan-feng.md), et al.). Walden markets **LBMs + [Diffusion Policy](../../entities/diffusion-policy.md)** for manufacturing/logistics, pairing autonomy with a human-remote-assist fallback so policies keep improving from real-world practice ([Walden launch](../../sources/walden-robotics-launch.md)). This is the concept's academic-to-industrial bridge.

## Related concepts

- [VLA models](vla-models.md) — the dominant LBM subtype; the wiki's main page for concrete systems (GR00T, π-line, SmolVLA…).
- [World-action models](../world-models/world-action-model.md) — the video-backbone LBM path made concrete ([Cosmos 3](../../entities/nvidia-cosmos.md)'s policy mode is the wiki's clearest instance).
- [Imitation learning](imitation-learning.md), [Scaling laws — VLAs](scaling-laws-vla.md).

## Current state

The term is TRI-house vocabulary that is escaping into general use (RoboCasa365 uses "large behavior models" for multitask manipulation policies generally; [Tedrake's stealth startup](../../entities/russ-tedrake.md) apparently carries it in its name). In practice the field's public systems are almost all the VLA subtype — and notably **LBM 1.0 itself is not a VLA** (ViT-encoder diffusion transformer, no VLM backbone — [paper](../../sources/tri-lbm-paper.md)), while the video-backbone alternative Tedrake now advocates is best evidenced by [Cosmos 3's](../../entities/nvidia-cosmos.md) policy mode topping RoboArena. Whether "LBM" displaces "VLA" as the umbrella term likely depends on his startup's visibility.

## Mentioned in

- [TRI LBM paper](../../sources/tri-lbm-paper.md) — **primary source**.
- [Automated Podcast — Tedrake](../../sources/automated-podcast-tedrake-rocket-ship.md)
- [TRI Website](../../sources/tri-website.md)
- [RoboCasa365 Paper](../../sources/robocasa365-paper.md) — LBM as baseline class.
