---
title: ACT (Action Chunking Transformer)
type: entity
subtype: method
created: 2026-05-25
updated: 2026-05-25
sources: 1
tags: [act, action-chunking, transformer, imitation-learning, behavior-cloning, aloha, mobile-aloha, tony-zhao, stanford]
---

**ACT (Action Chunking Transformer)** — imitation-learning method introduced by **Tony Z. Zhao et al. (Stanford, RSS 2023)** as the default policy for [ALOHA](aloha.md). Predicts a **chunk** (sequence) of future actions per timestep from observation history, instead of one action at a time. The "chunking" formulation is the contribution: it improves trajectory coherence, reduces per-step inference latency, and is now near-default across 2024–2026 BC and [VLA models](../concepts/learning/vla-models.md).

## Approach (per the [Mobile ALOHA paper](../sources/mobile-aloha-paper.md) reference)

- Transformer-based encoder-decoder over a fixed observation window.
- Predicts an action chunk of length **k** (typically 50–100 timesteps).
- Executes the first k action steps before re-predicting (vs Diffusion Policy's `T_a < T_p` receding-horizon approach).
- **Action chunking** as a primitive: predicting longer sequences helps with non-Markovian / multi-modal demonstrations and absorbs per-step jitter.
- Compatible with **co-training over heterogeneous bimanual datasets**: Mobile ALOHA uses ACT as the default and shows co-training gains of up to +95% absolute success on hard mobile-manipulation tasks ([source](../sources/mobile-aloha-paper.md), Table 1).

## Why it matters

- **The default policy class for the [ALOHA](aloha.md) / [Mobile ALOHA](aloha.md) platform line** — and increasingly for the broader bimanual-teleop ecosystem ([LeRobot](lerobot.md) docs surface ACT as a reference policy as well).
- **Popularized action chunking** as an IL primitive. The 2023 result that predicting a sequence outperforms per-step prediction is now baseline assumption across [Diffusion Policy](diffusion-policy.md), the Pi VLAs, and [RUMs](robot-utility-models.md).
- **Method-agnostic co-training compatibility** — Mobile ALOHA shows ACT + co-training beats no-co-train in 5/7 tasks, with average +34% absolute improvement; Diffusion Policy + co-train also benefits (+30/+20 on Wipe Wine / Push Chairs) but less than ACT; VINN+chunking gets mixed results.

## Open questions

- The original 2023 ACT paper is **not yet ingested** in this wiki — the wiki's view of ACT comes via the Mobile ALOHA paper (which uses it as a baseline and describes its mechanics in passing) plus references on [chelsea-finn.md](chelsea-finn.md) and [imitation-learning.md](../concepts/learning/imitation-learning.md). A direct ACT paper ingest would refine architectural details (encoder depth, action-chunk length k, training tricks, the VAE-style action distribution model).
- **Multi-task / language-conditioned ACT** — the wiki has no coverage of multi-task extensions; the published 2023/2024 work is single-task.

## Related
- [ALOHA / Mobile ALOHA](aloha.md) — the platform ACT was introduced with.
- [Diffusion Policy](diffusion-policy.md) — contemporary BC method; both use action chunking.
- [Tony Z. Zhao](tony-zhao.md) — first author.
- [Chelsea Finn](chelsea-finn.md) — senior author.
- [Imitation learning](../concepts/learning/imitation-learning.md) — concept; ACT is the canonical action-chunked BC reference.
- [LeRobot](lerobot.md) — surfaces ACT as a reference policy.

## Mentioned in
- [Mobile ALOHA Paper](../sources/mobile-aloha-paper.md)
