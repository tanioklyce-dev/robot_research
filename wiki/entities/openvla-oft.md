---
title: OpenVLA-OFT
type: entity
subtype: model
created: 2026-07-17
updated: 2026-07-17
sources: 1
tags: [openvla-oft, vla, vision-language-action, custom-architecture, parallel-decoding, action-chunking, film, libero, baseline]
status: stub
---

# OpenVLA-OFT

**OpenVLA-OFT** ("**O**ptimized **F**ine-**T**uning"; Moo Jin Kim, [Chelsea Finn](chelsea-finn.md), Percy Liang, 2025 — *Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success*, arXiv 2502.19645) is the successor recipe to [OpenVLA](openvla.md) that swaps its slow autoregressive action-token decoding for a **custom, ACT-style action head with parallel decoding**. It sits in the **custom-architecture** family of the [VLA action-head taxonomy](../concepts/learning/vla-models.md) and is the **top-scoring model on [LIBERO](libero.md)** in the wiki's most complete cross-method table.

## Why it matters in this wiki

OpenVLA-OFT is the **benchmark to beat**: on LIBERO it is the single model that finishes above [VLA-0](vla-0.md) — the only pretrained VLA VLA-0 could not surpass ([VLA-0 paper](../sources/vla-0-paper.md), Table I). It also marks how far the OpenVLA line moved: plain OpenVLA (autoregressive discrete tokens) scores **76.5** avg on LIBERO, while OpenVLA-OFT's parallel-decoding redesign reaches **97.1** — a ~20-point jump from the *fine-tuning recipe alone*, on the same base model. That makes it the wiki's cleanest evidence that **action-head/decoding design, not just backbone or data, drives VLA success** — the same thesis [VLA-0](vla-0.md) argues from the opposite (minimalist) direction.

## Architecture

> [!note] Primary source not yet ingested
> Architecture details below are from the OpenVLA-OFT paper (arXiv 2502.19645), **not yet ingested** as a wiki source; benchmark numbers are cited from the [VLA-0 paper](../sources/vla-0-paper.md), which reproduces them. Deepen this page when 2502.19645 lands in `raw/`.

OFT keeps the [OpenVLA](openvla.md) VLM backbone but replaces the output stage with three changes ([VLA-0 paper](../sources/vla-0-paper.md), Fig. 2, classifies it as "Custom — VLM + parallel decoding + FiLM"):

- **Parallel decoding + action chunking** — emit a whole action chunk in one forward pass instead of autoregressively token-by-token; the large inference-speed win over vanilla OpenVLA.
- **Continuous action representation** (regression head) rather than discretized action tokens — removing the resolution/vocabulary tradeoff that discrete-token VLAs pay.
- **FiLM language conditioning** — feature-wise modulation to strengthen instruction grounding.

The specialized head is what the [VLA-0](vla-0.md) authors call OFT's "**ACT head**" — the [Action-Chunking-Transformer](act.md) lineage applied inside a VLA.

## LIBERO results (via [VLA-0 paper](../sources/vla-0-paper.md), Table I)

| Variant | Spatial | Object | Goal | Long | Avg | Rank |
|---|---|---|---|---|---|---|
| OpenVLA-OFT, **with** large-scale action pretraining | 97.6 | 98.4 | 97.9 | 94.5 | **97.1** | **1.5** (best) |
| OpenVLA-OFT, **no** action pretraining | 94.3 | 95.2 | 91.7 | 86.5 | 91.9 | 2.8 |

For comparison in the same table: [VLA-0](vla-0.md) 94.7 (no pretraining), π0.5-KI 94.3, π0 94.2, [GR00T-N1](nvidia-groot.md) 93.9, [SmolVLA](smolvla.md)-2.25B 88.8, plain [OpenVLA](openvla.md) 76.5.

## Related

- [OpenVLA](openvla.md) — the base model / predecessor; OFT is its optimized fine-tuning recipe.
- [VLA-0](vla-0.md) — the action-as-text VLA that OFT (pretrained) narrowly tops on LIBERO.
- [ACT](act.md) — the action-chunking lineage OFT's parallel-decoding head draws on.
- [VLA models](../concepts/learning/vla-models.md) — the concept; OFT is the "custom architecture" family exemplar.
- [Chelsea Finn](chelsea-finn.md) — co-author.

## Open questions

- **Primary source (arXiv 2502.19645) not ingested** — filing it would let this page carry OFT's own reported numbers (real-robot results, the exact speedup factor over autoregressive OpenVLA, ALOHA/bridge evaluations) rather than only the LIBERO figures relayed by VLA-0.
- How much of the 76.5 → 97.1 LIBERO gain is parallel decoding vs. continuous actions vs. FiLM? The ablation lives in the un-ingested paper.

## Mentioned in

- [VLA-0 paper](../sources/vla-0-paper.md) — the ingested source that reports OFT's LIBERO numbers and classifies it as a custom-architecture VLA.
