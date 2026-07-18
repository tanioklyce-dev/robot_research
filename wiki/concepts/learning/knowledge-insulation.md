---
title: Knowledge Insulation (KI)
type: concept
created: 2026-07-17
updated: 2026-07-17
sources: 3
tags: [knowledge-insulation, vla, flow-matching, fast-tokens, stop-gradient, physical-intelligence, training-recipe]
---

# Knowledge Insulation (KI)

**Knowledge Insulation (KI)** is a [VLA](vla-models.md) training recipe from [Physical Intelligence](../../entities/physical-intelligence.md) (Driess et al., 2025 — *Knowledge Insulating Vision-Language-Action Models: Train fast, run fast, generalize better*, arXiv 2505.23705) that stops a continuous action head from **corrupting the pretrained knowledge of the VLM backbone** while still training the whole system end-to-end.

## Definition

The problem KI solves: when you bolt a **[flow-matching](flow-matching.md)** (or diffusion) action expert onto a pretrained VLM and train end-to-end, gradients from the freshly-initialized action head flow back into the VLM and **degrade its language/vision grounding** — the same failure the [VLA-0 paper](../../sources/vla-0-paper.md) cites as the downside of generative-action-head VLAs. KI "insulates" the backbone with two coupled tricks ([π0.7 paper](../../sources/pi07-paper.md), [π*0.6 paper](../../sources/pistar06-paper.md)):

1. **Supervise the VLM with discrete [FAST](../../entities/fast-action-tokenization.md) action tokens** via next-token prediction — so the backbone keeps learning to *predict actions* in its native (text-like) objective, staying stable and well-grounded.
2. **Stop-gradient between the action expert and the VLM** — the continuous flow-matching action expert attends to VLM activations but its gradients **do not flow back** into the backbone, so the non-pretrained head can't corrupt it.

The net effect (per the paper's title): **train fast, run fast, generalize better** — the backbone retains its VLM knowledge, the action expert provides high-fidelity continuous control, and the two are trained jointly without one wrecking the other.

## Key references

- [π0.7 paper](../../sources/pi07-paper.md) — uses KI as its core training recipe (VLM supervised via FAST tokens; action expert with stop-gradient); the wiki's most detailed downstream description.
- [π*0.6 paper](../../sources/pistar06-paper.md) — same KI recipe under the RECAP RL pipeline.
- [VLA-0 paper](../../sources/vla-0-paper.md) — reports **π0.5-KI** (π0.5 trained with knowledge insulation) as a LIBERO baseline: **94.3** avg with large-scale action pretraining (93.3 without) — beaten by [VLA-0](../../entities/vla-0.md).

> [!note] Primary source not yet ingested
> The KI paper itself (Driess et al., arXiv 2505.23705) is **not yet ingested**; this page is built from the ingested [π0.7](../../sources/pi07-paper.md) / [π*0.6](../../sources/pistar06-paper.md) papers that use the recipe, plus [VLA-0](../../sources/vla-0-paper.md)'s benchmark row. **π0.5-KI** = π0.5 ([lineage](../../entities/pi-zero-6.md)) trained with KI — the model that names the recipe.

## Related concepts

- [FAST (action tokenization)](../../entities/fast-action-tokenization.md) — the discrete-token scheme KI uses to supervise the VLM.
- [Flow matching](flow-matching.md) — the continuous action-expert technique KI insulates the VLM from.
- [VLA models](vla-models.md) — KI is a generative-action-head training recipe; [π0.7](../../entities/pi07.md) and [π*0.6](../../entities/pistar06.md) are its instances.

## Mentioned in

- [π0.7 paper](../../sources/pi07-paper.md)
- [π*0.6 paper](../../sources/pistar06-paper.md)
- [VLA-0 paper](../../sources/vla-0-paper.md)
