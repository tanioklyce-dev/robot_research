---
title: BET Paper — Behavior Transformers (Shafiullah et al., NeurIPS 2022)
type: source
url: https://arxiv.org/abs/2206.11251
author: Nur Muhammad Mahi Shafiullah, Zichen Jeff Cui, Ariuntuya Altanzaya, Lerrel Pinto
affiliation: NYU (Pinto lab)
published: 2022-06-22 (arxiv v1); revised 2022-10-11 (v2); NeurIPS 2022
ingested: 2026-05-09
tags: [bet, behavior-transformer, action-discretization, k-means, transformer, multi-modal-bc, shafiullah-2022, pinto-lab, nyu]
---

> [!note] Ingest depth
> This source page is **based on the arxiv abstract page only** (paper PDF not in `raw/`). Mechanics are cross-cited from [Diffusion Policy Paper](diffusion-policy-paper.md) §VII (Related Work) and the Diffusion Policy ablation tables. To deepen this page, drop the BET PDF in `raw/` and re-ingest.

## Summary

**Behavior Transformers (BeT)** — Shafiullah, Cui, Altanzaya, Pinto (NYU, NeurIPS 2022). Behavior-cloning method that **discretizes the continuous action space via k-means clustering**, then trains a **transformer** to predict the cluster index *plus* a residual offset (offset prediction inspired by 2-stage object detectors). The headline contribution is handling **multi-modal demonstration data** that defeats unimodal regressive BC. Direct ancestor of [VQ-BeT](../entities/vq-bet.md) (which replaces k-means with end-to-end vector quantization). Co-authored by [Mahi Shafiullah](../entities/mahi-shafiullah.md) (first) and [Lerrel Pinto](../entities/lerrel-pinto.md) (senior) — both NYU figures who later co-authored [RUM](../sources/robot-utility-models-paper.md), [OK-Robot](../entities/ok-robot.md), [DINO-WM](../entities/dino-wm.md), and the broader NYU embodied-AI line.

## Abstract (verbatim opener)

> "While behavior learning has made impressive progress in recent times, it lags behind computer vision and natural language processing due to its inability to leverage large, human-generated datasets."

## Key claims (from abstract)

- **Action discretization + multi-task action correction** is the core trick: "uses action discretization coupled with a multi-task action correction inspired by offset prediction in object detection."
- **Transformer architecture** retrofitted with the action discretization scheme.
- **Multi-modal continuous-action prediction from unlabeled demonstration data** — no reward, no segmentation labels.
- Evaluated on **robotic manipulation and self-driving behavior datasets**; reports improvements over prior methods.

## Mechanics (cross-cited from Diffusion Policy paper)

From [Diffusion Policy Paper](diffusion-policy-paper.md) §V results and §VII related work:

- **Action quantization**: cluster the demo actions with k-means → fixed codebook of `k` action centroids. Policy predicts which cluster + a continuous offset for fine adjustment.
- **Transformer trunk**: predicts the cluster index given observation history; the offset head predicts the residual within the chosen cluster.
- **Multi-mode capture**: by selecting different cluster indices in similar contexts, the policy can express divergent action plans (e.g., "go around the T-block from the left" vs "from the right").
- **Hyperparameter sensitivity**: k (the number of clusters) must be specified; this is a known limitation that VQ-BeT later addresses by learning the codebook end-to-end.

### Performance in Diffusion Policy ablation

From [Diffusion Policy Paper](diffusion-policy-paper.md) Tables I, IV:
- Strong on **RoboMimic Lift / Can** (saturates at ~1.00 on simpler tasks).
- Strong on **BlockPush** (`p1=0.96 / p2=0.71`) — BET's home benchmark; the multi-modal block-pushing task was introduced or popularized via BET.
- Weaker on **Transport / ToolHang / Square** — drops sharply with task complexity.
- Weak on **Franka Kitchen multi-stage** (`p4=0.44`) vs Diffusion Policy `p4=0.99`.

## Why it matters in this wiki

- **Direct ancestor of [VQ-BeT](../entities/vq-bet.md)** — VQ-BeT is "BET with a learned vector-quantization codebook instead of k-means". Both methods solve the same problem (multi-modal BC) by discretizing actions into a learned vocabulary.
- **Pinto-line work** — NYU's Pinto lab has produced BET → VQ-BeT → DINO-WM → RUM → OK-Robot, all sharing authorship overlap. BET is one of the early markers of this line.
- **Standard baseline** — referenced as a baseline across [Diffusion Policy Paper](diffusion-policy-paper.md), [Robot Utility Models Paper](robot-utility-models-paper.md), and [DINO-WM Paper](dino-wm-paper.md). Defines "BC for multi-modal demonstrations" as a problem statement.

## Entities mentioned

- [BET](../entities/bet.md) — the method.
- [Mahi Shafiullah](../entities/mahi-shafiullah.md) — first author.
- [Lerrel Pinto](../entities/lerrel-pinto.md) — senior author (NYU).
- [VQ-BeT](../entities/vq-bet.md) — direct successor (Lee et al. 2024).
- [Diffusion Policy](../entities/diffusion-policy.md) — competitor with different (diffusion-based) multi-modal-BC solution.

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md) — BC variant with discrete action codebook.
- [Learned latent space](../concepts/world-models/latent-space.md) — BET's k-means clustering can be read as a *learned-frozen* discrete action space, sibling to VQ-BeT's end-to-end learned codebook and Diffusion Policy's continuous-latent diffusion.

## Open questions / TBD

- **Full paper not yet ingested** — abstract-level only.
- **k-selection methodology** — how is the cluster count k chosen per task? Not in abstract.
- **Self-driving evaluation** — the abstract claims self-driving evaluation; details not in abstract.
- **NYU embodied-AI lineage** — BET → VQ-BeT → DINO-WM → RUM is a clear line; would benefit from a synthesis page.
