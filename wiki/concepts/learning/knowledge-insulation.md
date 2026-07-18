---
title: Knowledge Insulation (KI)
type: concept
created: 2026-07-17
updated: 2026-07-17
sources: 4
tags: [knowledge-insulation, vla, flow-matching, fast-tokens, stop-gradient, co-training, physical-intelligence, training-recipe]
---

# Knowledge Insulation (KI)

**Knowledge Insulation (KI)** is a [VLA](vla-models.md) training recipe from [Physical Intelligence](../../entities/physical-intelligence.md) ([Driess et al., 2025](../../sources/knowledge-insulation-paper.md), arXiv 2505.23705) that lets you attach a continuous [flow-matching](flow-matching.md) action expert to a pretrained VLM **without the action expert corrupting the VLM's pretrained knowledge** — while still training the whole system in a single stage.

## Definition

The problem KI solves ([KI paper](../../sources/knowledge-insulation-paper.md) §4): when you graft a **randomly-initialized** flow-matching (or diffusion) action expert onto a pretrained VLM and train end-to-end (the [π0](../../entities/pi-zero.md) recipe), the expert's gradients flow back into the backbone and **degrade its language/vision grounding** and **slow training** — the same downside the [VLA-0 paper](../../sources/vla-0-paper.md) cites for generative-action-head VLAs. Naïve fixes fail: **freezing** the backbone gives ~0% performance (VLMs aren't pretrained on robotics data, so frozen features are insufficient).

KI's fix is **three coupled measures**:

1. **Joint discrete + continuous action training.** Train the VLM backbone with an autoregressive next-token loss on **[FAST](../../entities/fast-action-tokenization.md)-tokenized discrete actions** *as a representation-learning objective*, while a smaller action expert simultaneously learns continuous actions via flow matching. **Discrete tokens are a training-time-only learning signal**; at inference you use the fast continuous expert. Having *both* action representations at training time is the crucial ingredient.
2. **VLM-data co-training.** Co-train on general vision-language data (VQA, captioning, bounding-box prediction, robot planning) so the model retains web-scale knowledge — most important for out-of-distribution semantic generalization.
3. **Stop-gradient.** Block gradients from the action expert into the backbone (via a modified attention where the expert attends to *stop-gradiented* backbone keys/values). This is only safe *because* measure 1 already trains the backbone on actions — so insulating it costs nothing, and the flow-matching loss weight can be set to `α = 1`.

A further detail: the attention mask keeps **discrete FAST action tokens and continuous action tokens from attending to each other**, so the two representations coexist without interference. KI is a **single-stage** recipe that formalizes and extends [π0.5](../../entities/pi-zero-6.md)'s earlier two-stage (FAST-first, then add expert) procedure.

## Why it works (results)

- **Train fast:** converges as fast as π0-FAST; plain π0 needs **~7.5× more training steps** for comparable performance.
- **Run fast:** inference uses the small continuous action expert (π0-class ~10 Hz), not slow autoregressive token decoding (~1.3 Hz).
- **Generalize better:** best language-following and OOD object generalization among the paper's baselines; SOTA on **LIBERO-90 (96.0)** and **LIBERO-Spatial (98.0)**; DROID 0.55 vs π0 0.49.
- **Cost:** ~20% more compute per step, offset by faster convergence.

## Key references

- [Knowledge Insulation paper (Driess et al. 2025)](../../sources/knowledge-insulation-paper.md) — **primary source**; introduces and ablates the recipe.
- [π0.7 paper](../../sources/pi07-paper.md) / [π*0.6 paper](../../sources/pistar06-paper.md) — the wiki's two strongest VLAs, both trained with KI.
- [VLA-0 paper](../../sources/vla-0-paper.md) — reports **π0.5-KI** (π0.5 + KI) as a LIBERO baseline (94.3 avg); its number matches the KI paper's "from generalist" row, confirming the identity.

## Related concepts

- [FAST (action tokenization)](../../entities/fast-action-tokenization.md) — the discrete-token scheme KI uses to supervise the VLM.
- [Flow matching](flow-matching.md) — the continuous action-expert technique KI insulates the VLM from.
- [VLA models](vla-models.md) — KI is a generative-action-head training recipe; [π0.7](../../entities/pi07.md) and [π*0.6](../../entities/pistar06.md) are its instances.

## Mentioned in

- [Knowledge Insulation paper](../../sources/knowledge-insulation-paper.md)
- [π0.7 paper](../../sources/pi07-paper.md)
- [π*0.6 paper](../../sources/pistar06-paper.md)
- [VLA-0 paper](../../sources/vla-0-paper.md)
