---
title: π0.5
type: entity
subtype: model
created: 2026-08-03
updated: 2026-08-03
sources: 8
tags: [pi-zero-5, physical-intelligence, vla, co-training, open-world, mobile-manipulation, hierarchical-inference, baseline]
---

**π0.5** ("pi oh five") — [Physical Intelligence](physical-intelligence.md)'s open-world-generalization VLA (Apr 2025), built on [π0](pi-zero.md) via **co-training on heterogeneous data** ([paper](../sources/pi-zero-5-paper.md), now ingested — previously the wiki's most-cited secondhand model). The first end-to-end learned system demonstrated **cleaning kitchens and bedrooms in entirely unseen homes**, on 10–15-minute tasks from high-level prompts.

## What it is

- **Recipe, not architecture:** ~400 hr mobile-manipulation data across ~100 homes is only **2.4%** of first-phase training; the rest is other robots (ME/CE), high-level subtask prediction (HL), web data (WD), and verbal instructions (VI). Removing any cross-embodiment source significantly degrades performance; web data is what buys **out-of-distribution object vocabulary**.
- **Hierarchical inference in one model:** predict the semantic subtask ("pick up the cutting board"), then the action chunk conditioned on it.
- **Hybrid training** — discrete [FAST](fast-action-tokenization.md) tokens in pre-training, a 300M flow-matching expert attached in post-training. This recipe became the template for [π0.5-KI](../concepts/learning/knowledge-insulation.md) and [MolmoAct2](molmoact2.md).
- **Scaling result:** at **104 training locations**, matches a control model trained directly on the test homes — the environment-generalization gap closed.

## Role in the wiki: the standing 2026 baseline

π0.5 is the model the 2026 record is measured against, and the record is two-sided:

| Where | What π0.5 shows |
|---|---|
| [π0.5 paper](../sources/pi-zero-5-paper.md) (2025) | Real scene-level generalization: cleans unseen homes; beats π0 and π0-FAST+Flow |
| [LIBERO-PRO](../sources/libero-pro-paper.md) (2026) | Most robust of the three VLAs tested under **position** perturbation (0.17–0.38) — and **~0.00 under instruction paraphrase** |
| [CaP-X](../sources/cap-x-paper.md) (2026) | Beats training-free CaP-Agent0 on position perturbation in 2 of 3 suites; loses decisively on paraphrase |
| [ASPIRE](../sources/aspire-paper.md) (2026) | "Largely collapses under task paraphrases" vs the coding agent |
| [MolmoAct2](../sources/molmoact2-paper.md) (2026) | Runner-up on RoboEval (44.3 vs 40.5); in-house π0-SO100/101 beaten by 11.4 on SO-100 |
| [Knowledge Insulation](../sources/knowledge-insulation-paper.md) | The π0.5-KI variant; LIBERO-90 + Spatial SOTA claims |

> [!note] The two records are about different axes — keep them apart
> π0.5's demonstrated generalization is **environment- and object-level**; the 2026 collapses are **instruction-level** (paraphrase), on benchmark-finetuned variants. Both are real. The honest one-line summary: **the co-training recipe bought scene generalization but not instruction generalization** — which the paper's own "relatively simple prompts" limitation anticipated.

## Related
- [Physical Intelligence](physical-intelligence.md) — lab · [π0](pi-zero.md) — base · [π0.6 stub](pi-zero-6.md) / [π0.7](pi07.md) / [π*0.6](pistar06.md) — successors
- [MolmoAct2](molmoact2.md) — adopts the hybrid recipe; the open-everything counterpart
- [VLA models](../concepts/learning/vla-models.md) · [Knowledge insulation](../concepts/learning/knowledge-insulation.md)

## Mentioned in
- [π0.5 paper](../sources/pi-zero-5-paper.md) — primary source.
- [Knowledge Insulation paper](../sources/knowledge-insulation-paper.md) — π0.5-KI.
- [LIBERO-PRO paper](../sources/libero-pro-paper.md) · [CaP-X paper](../sources/cap-x-paper.md) · [ASPIRE paper](../sources/aspire-paper.md) · [MolmoAct2 paper](../sources/molmoact2-paper.md) — the 2026 comparisons.
- [π0.7 paper](../sources/pi07-paper.md) · [π*0.6 paper](../sources/pistar06-paper.md) — successor lineage references.
