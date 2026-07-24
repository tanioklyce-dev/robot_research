---
title: Gemma3
type: entity
subtype: model
created: 2026-05-25
updated: 2026-05-25
sources: 1
tags: [gemma3, vlm, google, vision-language-model, vla-backbone]
status: stub
---

> [!note] Stub entity
> Filed 2026-05-25 during lint (20 mentions across 8 wiki files). Primary source — Google Gemma3 release ([arXiv 2503.19786](https://arxiv.org/abs/2503.19786), Mar 2025) — **not yet ingested**; deepen when filed.

**Gemma3** — Google's 2025 VLM family; successor to [Gemma](paligemma.md) / Gemma2. **Multi-modal-from-the-start** design with a built-in 400M-parameter vision encoder, multiple param-count variants (1B / 4B / 12B / 27B), and 128K-token context. The default backbone for [π0.7](pi07.md) (which uses the **4 B variant**).

## What we know via the wiki's existing references

- **Architecture**: VLM with **built-in 400M-parameter vision encoder** (vs PaliGemma's separate SigLIP encoder).
- **Variants**: 1B, 4B, 12B, 27B (the 4B is used in π0.7).
- **128K-token context** — enabling MEM-style video history encoding in π0.7.
- **The backbone for [π0.7](pi07.md)** ([paper](../sources/pi07-paper.md)) — Gemma3 4B + 860 M flow-matching action expert + MEM video-history encoder = 5 B total params. The vision encoder is also initialized from Gemma3 and follows the **MEM video history encoder design** (temporal + spatial compression).

## Why it matters in this wiki

- **Backbone of the wiki's strongest 2025 VLA** ([π0.7](pi07.md)). Filing closes 20 mentions across 8 files.
- **Architectural inflection from PaliGemma → Gemma3**: separate-vision-encoder → built-in-vision-encoder. Worth noting as a design-pattern shift in VLA backbones.

## Related

- [Gemma 4](gemma4.md) — successor (2026); first MoE variant + multimodal E2B/E4B edge variants.
- [π0.7](pi07.md), [π*0.6](pistar06.md) — primary downstream users.
- [PaliGemma](paligemma.md) — predecessor; backbone of π0.
- [SmolVLM-2](smolvlm.md) — Hugging Face's smaller alternative for SmolVLA.
- [VLA models](../concepts/learning/vla-models.md) — broader concept.

## Code & weights

- Project page: https://ai.google.dev/gemma
- HF: `google/gemma-3-1b-it`, `google/gemma-3-4b-it`, `google/gemma-3-12b-it`, `google/gemma-3-27b-it`.

## Open questions

- **Primary source not yet ingested.** When it lands, deepen with architecture diagram, vision-encoder specifics, multi-modal training-data mixture, and benchmark numbers.
- **Gemma3 vs PaliGemma 2/3** — relationship and naming clarity needed.
- **Multimodal capabilities specifics** — input modalities, video, audio: not in this wiki yet.
