---
title: Knowledge Insulating Vision-Language-Action Models (Driess et al. 2025)
type: source
url: https://arxiv.org/abs/2505.23705
author: Danny Driess, Jost Tobias Springenberg, Brian Ichter, Lili Yu, Adrian Li-Bell, Karl Pertsch, Allen Z. Ren, Homer Walke, Quan Vuong, Lucy Xiaoyang Shi, Sergey Levine (Physical Intelligence)
published: 2025-05-29
ingested: 2026-07-17
local_path: raw/2505.23705v1.pdf
venue: arXiv preprint (cs.LG), 2505.23705v1 ("Preprint. Under review.")
license: null
format: PDF (18 pages)
tags: [knowledge-insulation, vla, flow-matching, fast-tokens, stop-gradient, co-training, physical-intelligence, pi-zero, libero, droid]
---

# Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better

## Summary

The [Physical Intelligence](../entities/physical-intelligence.md) paper that names and formalizes **[Knowledge Insulation (KI)](../concepts/learning/knowledge-insulation.md)** — the training recipe now used by [π0.7](../entities/pi07.md) and [π*0.6](../entities/pistar06.md). Its core finding: **naïvely bolting a randomly-initialized [flow-matching](../concepts/learning/flow-matching.md) action expert onto a pretrained VLM (the [π0](../entities/pi-zero.md) recipe) significantly hurts both training speed and the VLM's retained knowledge** — the fresh action-expert gradients corrupt the backbone, degrading language following. KI fixes this with three coupled measures — **joint discrete+continuous action training**, **VLM-data co-training**, and a **stop-gradient** from the action expert into the backbone — giving "the best of both worlds": FAST-token representation learning trains fast and preserves knowledge, while the continuous action expert gives fast, precise inference. The **π0.5-KI** model referenced across the wiki is this paper's "Ours (from generalist model)."

## Key claims

- **The problem with standard recipes (§4).**
  - **Autoregressive VLAs are slow** — π0-FAST takes ~750 ms to decode a 1-second action chunk on an RTX 4090 (~1.3 Hz control), too slow for high-frequency/dynamic tasks and causing dynamics mismatch.
  - **Grafting a flow-matching action expert (π0-style) degrades the backbone** — the randomly-initialized expert's gradients interfere with pretrained VLM weights, harming **language following** and slowing convergence.
  - **Freezing the backbone doesn't work** — VLMs aren't pretrained on robotics data, so frozen representations are insufficient → **0% performance** (Fig. 4a, Fig. 8).
- **Knowledge Insulation = three measures (§5).**
  1. **Joint discrete + continuous action training** — the VLM backbone is trained with an autoregressive next-token loss on **[FAST](../entities/fast-action-tokenization.md)-tokenized discrete actions** *as a representation-learning objective*, while a smaller action expert is simultaneously trained with flow matching on continuous actions. **Discrete actions are used only at training time**; the continuous expert is used at inference. Loss `L_CO-VLA` (Eq. 4) = AR language/action token loss + α·flow-matching loss.
  2. **VLM-data co-training** — co-train on general vision-language data (VQA, captioning, bounding-box prediction, robot planning) to prevent knowledge loss; especially important for OOD semantic generalization to novel objects (Fig. 7).
  3. **Stop-gradient** — block gradient flow from the action expert into the backbone, implemented by modifying the attention so action-expert→backbone attention applies **stop-gradient** to the backbone's keys/values (Eqs. 5–6). Because the backbone is *also* trained on discrete actions, its activations still carry action information — so insulating it loses nothing. A side benefit: the flow-matching loss multiplier can simply be `α = 1`.
- **Attention-mask detail** — discrete FAST action tokens and continuous flow-matching action tokens are masked so **neither attends to the other**; the two action representations coexist without interference.
- **Single-stage, formalizing π0.5** — π0.5 used a *two-stage* procedure (FAST-tokens first, then add an action expert for post-training). KI **formalizes and extends this into a single-stage recipe** where backbone-adaptation and expert-training happen simultaneously. Built on the [π0](../entities/pi-zero.md) architecture (PaliGemma init, 3B backbone + ~300M action expert).
- **Results.**
  - **Convergence:** trains **as fast as π0-FAST**; plain **π0 needs ~7.5× as many training steps** to reach comparable performance (Fig. 6b).
  - **LIBERO (Table 1):** new SOTA on **LIBERO-90 (96.0)** and **LIBERO-Spatial (98.0)** — "Ours (from generalist)" = Spatial 98.0 / Object 97.8 / Goal 95.6 / Long 85.8 (avg **94.3**); "from scratch" = 96.6 / 97.2 / 94.6 / 84.8 (avg 93.3). Beats π0-FAST badly on LIBERO-10/Long (85.8 vs 60.2).
  - **DROID:** 0.55 ± 0.09 vs π0 0.49 vs π0-FAST 0.45.
  - **Language following:** stop-gradient markedly improves it over π0 / joint-training-without-stop-gradient; VLM co-training can recover it too.
  - Consistently best across real-world dexterous tasks: table bussing, shirt folding, items-in-drawer (held-out scenes), and 4 mobile-manipulation tasks.
- **Cost/limits (§7).** ~**20% more compute per training step** (dual objectives), offset by much faster wall-clock convergence. Language following is improved but "still far from perfect."

> [!note] Consistency check
> This paper's "Ours (from generalist model)" LIBERO average of **94.3** exactly matches the "π0.5-KI 94.3" figure the [VLA-0 paper](vla-0-paper.md) relays — confirming **π0.5-KI = π0.5 trained with this KI recipe**.

## Entities mentioned

- [Physical Intelligence](../entities/physical-intelligence.md) — the lab; all authors.
- [π0](../entities/pi-zero.md) — the base architecture KI builds on (and the degraded baseline).
- [FAST / π0-FAST](../entities/fast-action-tokenization.md) — the DCT tokenizer KI uses for its discrete representation-learning objective; π0-FAST is a baseline.
- [OpenVLA-OFT](../entities/openvla-oft.md), [GR00T N1](../entities/nvidia-groot.md) — baselines / related continuous-action VLAs.
- [PaliGemma](../entities/paligemma.md) — the VLM the backbone is initialized from.
- [LIBERO](../entities/libero.md), [DROID](../entities/droid.md) — open benchmarks evaluated.
- [Sergey Levine](../entities/sergey-levine.md), [Karl Pertsch](../entities/karl-pertsch.md) — authors; [Chelsea Finn](../entities/chelsea-finn.md) — acknowledged (initial language-following experiments).
- [π0.5 (lineage)](../entities/pi-zero-6.md) — π0.5-KI = π0.5 + this recipe.

## Concepts touched

- [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) — the recipe this paper introduces (primary source).
- [Flow matching](../concepts/learning/flow-matching.md) — the continuous action-expert technique KI insulates the VLM from.
- [VLA models](../concepts/learning/vla-models.md) — a generative-action-head training recipe.

## Open questions

- KI raises training compute ~20% per step; the paper argues wall-clock still wins, but doesn't fully characterize the tradeoff at very large scale.
- Language following is "still far from perfect" — data correlations still let the model ignore instructions sometimes; an open robustness gap.
