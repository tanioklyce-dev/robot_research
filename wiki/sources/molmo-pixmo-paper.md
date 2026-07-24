---
title: "Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Vision-Language Models (Deitke et al. 2024)"
type: source
url: https://arxiv.org/abs/2409.17146
local_path: raw/2409.17146.pdf
author: Matt Deitke, Christopher Clark, Sangho Lee, Rohun Tripathi, … (Allen Institute for AI / Ai2, ~50 authors)
published: 2024-09-25
ingested: 2026-07-24
venue: arXiv:2409.17146 (v2 2024-12-05); Ai2
tags: [molmo, pixmo, vlm, vision-language-model, open-data, open-weights, pointing, visual-grounding, ai2, clip]
---

# Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Vision-Language Models

## Summary

Molmo (Ai2) is a family of **[vision-language models](../concepts/learning/vla-models.md)** whose thesis is a rebuke of how "open" VLMs are usually built: the strong open-weight models of 2024 lean heavily on **synthetic data distilled from proprietary VLMs** (GPT-4V etc.), so the community never learned how to build a performant VLM *from scratch*. Molmo's key contribution is therefore **not the model but the data** — **PixMo**, a suite of datasets collected **without any external VLM in the loop** — plus the careful modeling/training recipe that turns it into a state-of-the-art result. The 72B model **tops academic benchmarks** in its openness class and ranks **second only to GPT-4o** by human preference, beating Claude 3.5 Sonnet and Gemini 1.5 Pro/Flash.

## Key claims

- **The distillation problem it avoids.** "The strongest open-weight models rely heavily on synthetic data from proprietary VLMs … effectively distilling these closed VLMs into open ones." Molmo refuses this and collects human data instead — the whole point.
- **PixMo-Cap (pre-training captions) via a speech "trick".** Rather than have annotators *type* (slow, terse) or a VLM generate (distillation), annotators **describe each image aloud for 60–90 seconds**; audio is transcribed by a standard speech-to-text system, then a **language-only LLM** summarizes multiple raw transcripts into the final caption. Yield: **712k images, 1.3M captions**, averaging **196 words** vs **11** for COCO captions and **37** for localized narratives — far denser.
- **PixMo-AskModelAnything (fine-tuning Q&A).** Human annotators author diverse free-form image Q&A: **162k question-answer pairs over 73k images**.
- **PixMo-Points (the innovative 2D pointing dataset).** Pointing data collected to (1) **point to items named by text**, (2) **count by pointing**, and (3) use pointing as a **natural grounding output**. Notably, pointing is **evaluated with optimal (Jonker-Volgenant) assignment** between predicted and ground-truth points — a Hungarian min-cost matching, the same machinery the wiki's [detection-evaluation-metrics](../concepts/robotics/detection-evaluation-metrics.md) page contrasts with greedy matching.
- **Architecture (deliberately standard).** A **preprocessor** (multiscale, multi-crop) → a **ViT image encoder** → a **connector** that pools + projects patch features into the LLM embedding space → a **decoder-only LLM**. Default vision encoder is **OpenAI CLIP ViT-L/14@336**; a **100% fully-open variant** swaps in a **MetaCLIP** encoder + **[OLMo](../entities/olmo.md)** LLM so every training bit is public.
- **The model family + where each lands:**
  - **MolmoE-1B** — on the **OLMoE-1B-7B** mixture-of-experts LLM; **~GPT-4V** on academics and user preference.
  - **Molmo-7B-O** (OLMo-7B) and **Molmo-7B-D** (Qwen2-7B; "D" = demo) — **between GPT-4V and GPT-4o**.
  - **Molmo-72B** (Qwen2-72B) — **highest academic benchmark**, **2nd by human preference behind GPT-4o**; beats Claude 3.5 Sonnet, Gemini 1.5 Pro/Flash.
- **Fully open release.** Model **weights**, the **PixMo datasets**, and **source code** all released (molmo.allenai.org) — the differentiator from open-weights-but-closed-data peers.

## Entities mentioned

- [Molmo](../entities/molmo.md) — the model family (this source is its primary reference).
- [MolmoAct](../entities/molmoact.md) — the VLA built on Molmo (the reason Molmo entered this wiki).
- [Qwen](../entities/qwen.md) — Qwen2-7B/72B are two of the four backbones.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — Molmo is a VLM backbone; its pointing capability is the action-grounding hook MolmoAct builds on.
- [Detection evaluation metrics](../concepts/robotics/detection-evaluation-metrics.md) — PixMo-Points' Hungarian/optimal point-matching evaluation is a concrete instance of the greedy-vs-optimal-assignment distinction.

## Open questions

- **OLMo / OLMoE** (the fully-open LLM backbones) still have no wiki entity or source — Molmo's "100% open" claim rests on them; the OLMo papers are the obvious next ingest.
- Does the **pointing → counting → grounding** capability feed [MolmoAct](../entities/molmoact.md)'s action grounding *directly* (point = action target) or only as a pretraining prior? Resolvable when the MolmoAct paper (2508.07917) is filed.
- Exact per-benchmark numbers and the PixMo license terms live in the (very large) appendix, not extracted here.
