---
title: OpenVLA
type: entity
subtype: model
created: 2026-05-25
updated: 2026-07-17
sources: 1
tags: [openvla, vla, vision-language-action, open-weights, llama-2, autoregressive-action-tokens, baseline]
status: stub
---

> [!note] Stub entity
> Filed 2026-05-25 during lint as the most-mentioned undocumented entity (49 mentions across 23 wiki files). Primary source — Kim et al. 2024 — **not yet ingested**; deepen when filed.

**OpenVLA** — **7B-parameter open-weights VLA** by Kim et al. (Stanford / TRI / UC Berkeley / Google DeepMind / MIT, June 2024; arXiv 2406.09246). The reference open-baseline that every subsequent VLA paper benchmarks against. Built on a **Llama-2 7B** backbone with vision encoders; emits **autoregressive action tokens** (actions discretized into bins, predicted as next-token sequences).

## What we know via the wiki's existing references

- **Action head**: **autoregressive action tokens** — the contrast point against [π0](pi-zero.md)'s flow-matching, [Diffusion Policy](diffusion-policy.md)'s DDPM, and [SmolVLA](smolvla.md)'s flow-matching action expert. See [VLA action-head taxonomy](../concepts/learning/vla-models.md).
- **Open-weights baseline** — the first credible open-source 7B VLA; cited as the comparison VLA across [π0](pi-zero.md), [SmolVLA](smolvla.md), [JEPA-WMs](jepa-wms.md), [EgoScale](../sources/egoscale-paper.md), and the [LeRobot tutorial](../sources/lerobot-robot-learning-tutorial.md).
- **Beaten on every wiki-tracked benchmark by 2025-era successors**: π0-3.3B beats OpenVLA-7B on bussing tasks ([π0 paper](../sources/pi-zero-paper.md)); SmolVLA-0.45B beats OpenVLA-7B on LIBERO + Meta-World ([SmolVLA paper](../sources/smolvla-paper.md), Table 2).
- **The 7B size is now considered large** for VLA work — SmolVLA at 0.45B is ~16× smaller and wins on real-world SO-100.

## Why it matters in this wiki

- **The default 2024 open-VLA baseline.** Practically every VLA primary source in this wiki cites OpenVLA as the comparison point — filing this stub closes 49 mentions × 23 files from "text mention" to "live entity reference."
- **The autoregressive-action-tokens family representative.** Without OpenVLA, the action-head taxonomy chart in [VLA models](../concepts/learning/vla-models.md) has a blank in the AR-tokens row; this entity anchors it.

## Related

- [VLA models](../concepts/learning/vla-models.md) — broader concept.
- [π0](pi-zero.md), [SmolVLA](smolvla.md), [NVIDIA GR00T](nvidia-groot.md), [π0.7](pi07.md) — VLA contemporaries / successors.
- [Diffusion Policy](diffusion-policy.md) — DDPM-action-head contrast.
- [Flow matching](../concepts/learning/flow-matching.md) — alternative continuous-action head; OpenVLA's autoregressive approach is the discrete-action contrast.
- [Sergey Levine](sergey-levine.md), [Chelsea Finn](chelsea-finn.md) — OpenVLA authors (Levine + Finn-affiliated work; not yet ingested as a primary source on either page).
- [Karl Pertsch](karl-pertsch.md) — DROID co-lead; also affiliated with the OpenVLA team.

## Code & weights

- Project page: https://openvla.github.io
- Repo: https://github.com/openvla/openvla
- Weights on Hugging Face: `openvla/openvla-7b`

## Open questions

- **Primary source not yet ingested.** When the Kim et al. 2024 paper lands in `raw/`, deepen this entity with architecture details (vision encoder, action-bin scheme, training data mixture, exact LIBERO/SimplerEnv numbers).
- **[OpenVLA-OFT](openvla-oft.md) / OpenVLA v2** — successor work (own entity + [ingested primary](../sources/openvla-oft-paper.md), Kim/Finn/Liang, RSS 2025); the OFT "optimized fine-tuning" recipe (**parallel decoding + action chunking + continuous L1 head**, +FiLM for ALOHA) fine-tunes *this same base model* to lift LIBERO **76.5 → 97.1** avg with **26× faster** action generation. **OpenVLA-OFT is the *only* model above [VLA-0](vla-0.md) on LIBERO** (rank 1.5 vs 2.8; [VLA-0 paper](../sources/vla-0-paper.md)).
- **Author entity pages** — Moo Jin Kim (first author) doesn't have a page. Karl Pertsch + Levine + Finn do.
