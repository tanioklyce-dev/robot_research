---
title: π0 Paper — A Vision-Language-Action Flow Model for General Robot Control (Black et al., Physical Intelligence, 2024)
type: source
url: https://arxiv.org/abs/2410.24164
html: https://arxiv.org/html/2410.24164v1
blog: https://physicalintelligence.company/blog/pi0
author: "Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, Lachy Groom, Karol Hausman, Brian Ichter, Szymon Jakubczak, Tim Jones, Liyiming Ke, Sergey Levine, Adrian Li-Bell, Mohith Mothukuri, Suraj Nair, Karl Pertsch, Lucy Xiaoyang Shi, James Tanner, Quan Vuong, Anna Walling, Haohuan Wang, Ury Zhilinsky"
affiliation: Physical Intelligence
published: 2024-10-31 (arxiv v1); 2026-01-08 (last revised)
ingested: 2026-05-10 (abstract); 2026-05-25 (full HTML deepening)
created: 2026-05-10
updated: 2026-05-25
tags: [pi-zero, pi0, vla, flow-matching, vision-language-action, physical-intelligence, generalist-policy, paligemma, action-expert, cross-embodiment, levine, primary-source]
---

## Summary

**π0** ("pi-zero") — [Physical Intelligence](../entities/physical-intelligence.md)'s flagship vision-language-action model (24 authors including Black, Brown, Driess, Finn, Hausman, Ichter, Levine, Pertsch; October 2024). The architecture: take a **pretrained 3 B-parameter PaliGemma VLM** and bolt on a **flow-matching "action expert"** that turns VLM features + a noisy action chunk into continuous joint commands. Train end-to-end on **~10,000 hours of in-house cross-embodiment teleop data** across 7 robot configurations and 68 tasks, plus OXE + DROID + Bridge. Result: one model that performs **laundry folding, table bussing, microwave dish loading, egg-carton stacking, box assembly, and grocery bagging** on single-arm, dual-arm, and mobile-manipulator embodiments without per-platform retraining.

Full HTML ingested 2026-05-25 — supersedes the prior abstract-only ingest. The wiki now also has a [dedicated π0 entity](../entities/pi-zero.md) and a separate ingest of the **[SmolVLA paper](smolvla-paper.md)** (Shukor et al., HF, June 2025), which uses π0 as its primary VLA baseline.

## Architecture (paper §IV)

- **Base VLM**: **PaliGemma 3 B** ([Beyer et al., 2024](https://arxiv.org/abs/2407.07726)) — chosen for "convenient tradeoff between size and performance" and **suitability for real-time control**. The framework is VLM-agnostic.
- **Action expert**: a transformer module added to the VLM that emits flow-based outputs. **Total params: 3.3 B** (PaliGemma 3 B + ~0.3 B action expert).
- **Attention pattern**: the action expert uses a **full bidirectional attention mask** — all action tokens within a chunk attend to each other. (Contrast with [SmolVLA](../entities/smolvla.md), which interleaves cross-attention and **causal** self-attention.)
- **Inputs**: 3 RGB images + sensorimotor state + a natural-language task instruction.
- **Outputs**: action chunks; flow-matching head trained to predict the vector field that denoises actions from Gaussian noise toward the demonstration action distribution, with the flow-matching time variable `τ` sampled from a **Beta distribution**.

## Training data (paper §V)

- **~10,000 hours of dexterous manipulation** collected in-house by Physical Intelligence.
- Across **7 robot configurations and 68 tasks** (single-arm, dual-arm, mobile manipulator).
- Augmented with **OXE** ([Open X-Embodiment](../entities/droid.md)), **[DROID](../entities/droid.md)**, **Bridge**, and other open robot datasets.

## Training recipe (paper §V)

- **Pre-training** on the full mixture → broad coverage.
- **Post-training** (fine-tuning) on task-specific data → dexterity for laundry, bussing, etc.
- Pre-training corresponds to the "robot-foundation-model" framing: one model, many tasks; fine-tune for specialization.
- High-level VLM policy is used to **direct π0 with sub-task language commands** in the multi-stage experiments (the "human-VLA-VLM stack").

## Results (paper §VI)

### Tasks demonstrated
Laundry folding (long-horizon, dual-arm, deformable), table bussing (combinatorial — many dishes, utensils, trash), dishes in microwave, eggs-into-carton stacking, box assembly, grocery bagging.

### Baselines
- **OpenVLA** (autoregressive action tokens) — trained for 160k steps for fair comparison.
- **Octo** (transformer-from-scratch on demonstration data) — trained for 320k steps and additionally on the same data mixture as π0.
- Plus a **cross-embodiment-fine-tuned OpenVLA** on UR5e to give the baseline its strongest shot.

### Headline finding (§VI-D)
π0 **substantially beats both baselines** on the bussing-task family — paper reports "large improvements over all baselines, including prior VLA models and models designed specifically for dexterous manipulation." The bussing task evaluates the fraction of objects correctly placed in receptacles; harder variants stack utensils on trash and include objects not seen in pre-training.

### Cross-embodiment finding (§VI-B)
A single π0 checkpoint follows language commands across single-arm, dual-arm, and mobile-manipulator platforms — "zero shot after pre-training."

### Language-following finding (§VI-B)
The model **follows commands from a high-level VLM policy** as well as from a human — opening the door to hierarchical VLM-as-planner + π0-as-controller stacks.

## Discussion / Limitations (paper §VII)

- π0 is presented as **a prototype**, not the final word — Physical Intelligence has since iterated to π0.5 / π0.6 ([referenced via Physical Intelligence entity](../entities/physical-intelligence.md); not separately ingested).
- The **flow-matching head + bidirectional action attention** is one design point; SmolVLA's contrast (causal self-attention + interleaved cross-attention, with a smaller base VLM) shows the architectural space isn't settled.
- **Data scale and curation are load-bearing**: 10k hours of in-house teleop is the kind of investment that's hard for academic labs to match — which is why subsequent work like [SmolVLA](smolvla-paper.md) (22.9k episodes ≈ 0.6k hours equivalent, from 481 community datasets) and [EgoScale](egoscale-paper.md) (egocentric human video) have been exploring alternative data regimes.

## Entities mentioned

- [Physical Intelligence](../entities/physical-intelligence.md) — the company.
- [π0](../entities/pi-zero.md) — model entity (new, filed by this ingest).
- [Sergey Levine](../entities/sergey-levine.md), [Chelsea Finn](../entities/chelsea-finn.md), [Karl Pertsch](../entities/karl-pertsch.md) — author overlaps with DROID / Metaworld lineage.
- [Franka Panda](../entities/franka-panda.md), UR5e — referenced platforms.
- [DROID](../entities/droid.md) — training-data component.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — π0 is a defining instance; the flow-matching action head is contrasted there with DDPM (Diffusion Policy) and autoregressive tokens (OpenVLA).
- [Imitation learning](../concepts/learning/imitation-learning.md) — π0 is BC-flavored at training time (with a flow-matching head).

## Open questions / TBD

- **Flow matching concept page** still not filed. With both π0 and [SmolVLA](smolvla-paper.md) using it, plus [DDPM](../entities/ddpm.md) as the substrate the LeRobot tutorial introduces it through, it's now load-bearing enough to deserve its own concept page in `concepts/learning/flow-matching.md`.
- **π0.5 / π0.6 primary sources** — referenced in [Physical Intelligence](../entities/physical-intelligence.md) and [Stanford HAI AI Index 2026](stanford-hai-ai-index-2026.md); not yet ingested. The π series is one of the wiki's known-active gaps.
- **Quantitative results table** — the paper presents head-to-head numbers per task; this ingest captures the structure but not the per-task percentages (paper PDF would supplement the HTML for exact values).
