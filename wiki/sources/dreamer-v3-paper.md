---
title: DreamerV3 Paper — Mastering Diverse Domains through World Models (Hafner et al., 2023)
type: source
url: https://arxiv.org/abs/2301.04104
author: Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap
affiliation: Not stated on the arxiv abstract page (Hafner-line work; DeepMind / Toronto / collaborators)
published: 2023-01-10 (arxiv v1); 2024-04-17 (v2)
ingested: 2026-05-10
created: 2026-05-10
updated: 2026-05-10
tags: [dreamer, dreamer-v3, world-model, model-based-rl, imagination, hafner, foundational, mbrl]
---

> [!note] Ingest depth
> This source page is **based on the arxiv abstract page only** (paper PDF not in `raw/`). Filed as part of the curriculum-driven backfill of LeWM baselines (Module 8 RL vocab + Module 10 world models). To deepen, drop the PDF in `raw/` and re-ingest; the [authors' project page](https://danijar.com/dreamerv3) likely has additional detail.

## Summary

**DreamerV3** — Hafner, Pasukonis, Ba, Lillicrap (2023). General model-based RL algorithm built around a learned world model and an actor-critic trained "in imagination" (i.e. on rollouts produced by the world model rather than the environment). Headline contribution per the abstract: **a single fixed configuration** outperforms specialized methods across **150+ diverse tasks**, and DreamerV3 is "the first algorithm to collect diamonds in Minecraft from scratch without human data or curricula." Stability across domains attributed to "robustness techniques based on normalization, balancing, and transformations" — the symlog / two-hot / exponential moving-average tricks the paper introduces. Canonical example of the **generative-style world model** family: predicts environment state and reward, with a recurrent dynamics core.

## Abstract (verbatim opener)

> "DreamerV3 outperforms specialized methods across over 150 diverse tasks, with a single configuration."
>
> "DreamerV3 is the first algorithm to collect diamonds in Minecraft from scratch without human data or curricula."

## Key claims

- **Generality with a single hyperparameter set.** 150+ tasks across "continuous and discrete actions, visual and low-dimensional inputs, 2D and 3D worlds, different data budgets, reward frequencies, and reward scales" (paraphrased from the abstract; exact range to be re-verified against the PDF).
- **Minecraft diamond from scratch.** First algorithm to do so without human demonstrations or curricula — long held up as a hard MBRL benchmark.
- **Method = world-model + actor-critic in imagination.** The world model learns environment dynamics; the actor and critic train on synthetic rollouts produced by the world model rather than (only) on real environment interactions.
- **Stability via normalization tricks.** The paper's robustness story attributes cross-domain consistency to specific techniques (symlog squashing, two-hot reward representation, percentile-based return normalization, etc.) — exact list to be confirmed on PDF ingest.

## Why it matters in this wiki

- **The Dreamer baseline column.** Dreamer / DreamerV3 is one of the four world-model baselines in [LeWM](../entities/leworldmodel.md); the entity now exists so curriculum [Module 10](../syntheses/robot-learning-curriculum.md) can talk about MBRL coherently.
- **Generative-WM family exemplar.** DreamerV3 predicts environment state (and reward) — the *opposite end* of the world-model design axis from JEPA, which sidesteps generation entirely. The DreamerV3 vs LeWM contrast is one of the cleanest framings in the [generative-video vs JEPA synthesis](../syntheses/generative-video-vs-jepa-world-models.md).
- **MBRL canon.** With Dreamer, [TD-MPC](td-mpc2-paper.md), and [LeWM](leworldmodel-paper.md) all on the wiki, the model-based-RL family is no longer a referenced-but-unbacked stub.

## Entities mentioned

- [Dreamer](../entities/dreamer.md) — the algorithm/family entity.
- [LeWorldModel](../entities/leworldmodel.md) — uses DreamerV3 as a baseline column.

## Concepts touched

- [World model](../concepts/world-model.md) — DreamerV3 is a Reward-conditioned MBRL exemplar.
- [Imitation learning](../concepts/imitation-learning.md) — orthogonal but useful contrast (BC ≠ MBRL).

## Open questions / TBD

- **Full paper not yet ingested** — abstract-level only. The paper's exact stability tricks, ablations, and Minecraft training details are referenced but not quoted verbatim here.
- **Affiliations** — arxiv abstract page didn't list them. Hafner has been associated with DeepMind / U Toronto across the Dreamer line; verify on PDF.
- **Nature publication.** DreamerV3 was reportedly accepted to Nature in 2025; confirm and add the published version reference.
- **Author entity page for Danijar Hafner** — would anchor the Dreamer line (PlaNet → DreamerV1 → V2 → V3) end to end.
