---
title: "OLMo: Accelerating the Science of Language Models (Groeneveld et al. 2024)"
type: source
url: https://arxiv.org/abs/2402.00838
local_path: raw/2402.00838.pdf
author: Dirk Groeneveld, Iz Beltagy, Pete Walsh, … (Allen Institute for AI / Ai2, ~40 authors)
published: 2024-02-01
ingested: 2026-07-24
venue: arXiv:2402.00838 (v4 2024-06-07); Ai2
tags: [olmo, open-source-llm, language-model, ai2, dolma, reproducibility, open-data, apache-2]
---

# OLMo: Accelerating the Science of Language Models

## Summary

OLMo (Ai2) is a **"truly open" language model** built to make LMs *scientifically* studiable rather than just usable. Its argument: most "open" releases give you weights + inference code and stop there, so the community never gets to study *how* a performant LM is actually made. OLMo instead releases **the whole pipeline** — weights, the **full pretraining corpus (Dolma)**, training and evaluation code, hundreds of **intermediate checkpoints**, and the **training logs** — all under **Apache 2.0**. It's the foundational "open-everything" LM whose **OLMo-7B** is a [Molmo](../entities/molmo.md) backbone and whose openness thesis Molmo's own PixMo work extends to the vision-language setting.

## Key claims

- **"Truly open" = the whole framework, not just weights.** The release includes: **open weights**, the **full training data (Dolma; Soldaini et al. 2024)** plus the code that produces it and tools to analyze it, **training + evaluation code**, **hundreds of intermediate checkpoints** (as HuggingFace revisions), and **the complete Weights & Biases training-metric logs**. Adaptation uses **Open Instruct**. This is a strict superset of the Pythia/BLOOM "most open" tier and far beyond Llama/Mixtral (weights + report).
- **Model sizes.** **OLMo-1B** (trained on **2T tokens**) and **OLMo-7B** (**2.46T tokens**), plus a 65B in progress; AdamW, ~4M-token batches (Table 1).
- **Architecture (decoder-only, LLaMA-lineage choices).** **No biases** anywhere, **non-parametric LayerNorm** (OLMo-7B), **SwiGLU** activation, **RoPE** positional embeddings, full attention, 32 layers, ~8/3 MLP ratio — the modern stable-training recipe, chosen explicitly for reproducibility.
- **Competitive at its scale.** Benchmarked against **LLaMA-7B, Llama-2-7B, MPT-7B, Pythia-6.9B, Falcon-7B, RPJ-INCITE-7B** — a genuine peer, not a toy, which is what makes the full-transparency release scientifically useful.
- **NVIDIA *and* AMD.** The codebase was verified to train on **both NVIDIA and AMD GPUs without loss** — a portability/reproducibility point most releases can't make.
- **Why open the whole thing.** To catalyze research into "as-yet poorly understood aspects" (data↔capability relationships, training dynamics), and to cut duplicated pretraining emissions by letting others build on checkpoints rather than pretrain from scratch.

## Entities mentioned

- [OLMo](../entities/olmo.md) — the model family (this source's subject).
- [Molmo](../entities/molmo.md) — the VLM whose **OLMo-7B** backbone comes from here; the reason OLMo entered this wiki.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — OLMo is the open **LLM decoder** side of the VLM/VLA stack (the "L" that a vision encoder is bolted onto in [Molmo](../entities/molmo.md)).

## Open questions

- **Dolma** (the ~3T-token open corpus, Soldaini et al. 2024) and **Ai2 / Allen Institute for AI** (recurs across [Molmo](../entities/molmo.md), [MolmoAct](../entities/molmoact.md), and even the [YOLO](yolo-you-only-look-once-2016.md) authorship) both lack wiki entities — candidates if the open-model thread deepens.
- **OLMoE** (the MoE sibling, Muennighoff et al. 2024, arXiv 2409.02060) — the other Molmo backbone — is a separate release still un-ingested. Same for **OLMo 2** (2025), the successor.
