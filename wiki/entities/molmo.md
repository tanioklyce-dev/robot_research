---
title: Molmo
type: entity
subtype: vlm
created: 2026-07-17
updated: 2026-07-24
sources: 2
tags: [molmo, vlm, allen-institute, ai2, pixmo, open-weights, open-data, pointing, vla-backbone]
---

# Molmo

**Molmo** (*Multimodal Open Language MOdel*) is a family of **[vision-language models](../concepts/learning/vla-models.md)** from the **Allen Institute for AI (Ai2)** ([Deitke et al. 2024](../sources/molmo-pixmo-paper.md)), distinguished by being **fully open** — open *weights and* open training *data* (the PixMo datasets) — rather than open-weights-but-closed-data. It is the VLM backbone under **[MolmoAct](molmoact.md)**.

## Why it matters in this wiki

Molmo appears here as the **backbone of [MolmoAct](molmoact.md)**, the Allen Institute VLA baseline in the wiki's [LIBERO](libero.md) table. Two properties make Molmo a natural VLA backbone:

- **Pointing.** Molmo's signature capability is **pointing to pixels** — outputting 2D image coordinates to reference objects. That is directly action-grounding-relevant: a VLM that can point at "the mug" is a short step from a policy that can act on it, which is the lineage MolmoAct's "reason in space" framing builds on.
- **Fully-open provenance.** PixMo training data is **human-collected, not distilled from proprietary VLMs** (dense captions via speech, free-form Q&A, 2D point annotations). This puts Molmo in the same "open-data" spirit as the wiki's other reproducibility-first VLA work ([SmolVLA](smolvla.md), [LeRobot](lerobot.md)), and contrasts with the closed-data backbones (PaliGemma, Gemma3) used by π0 / π0.7.

Among the wiki's [VLM backbones for VLAs](../concepts/learning/vla-models.md), Molmo is the **Allen-Institute open-data** option, sitting alongside NVIDIA's [Eagle](eagle-vlm.md), Google's [PaliGemma](paligemma.md)/[Gemma3](gemma3.md), and Hugging Face's [SmolVLM-2](smolvlm.md).

The distillation-free data recipe pays off: the **Molmo-72B** model **tops academic benchmarks** in its openness class and ranks **2nd by human preference behind GPT-4o**, beating Claude 3.5 Sonnet and Gemini 1.5 Pro/Flash ([Deitke et al. 2024](../sources/molmo-pixmo-paper.md)).

## Family

- **MolmoE-1B** — **OLMoE-1B-7B** mixture-of-experts backbone; ~GPT-4V.
- **Molmo-7B-O** — **[OLMo-7B](olmo.md)** backbone (the fully-open one).
- **Molmo-7B-D** — **Qwen2-7B** backbone (the "demo" model); 7B-O/7B-D land between GPT-4V and GPT-4o.
- **Molmo-72B** — **Qwen2-72B** backbone; the flagship / top scorer.
- Common design: **preprocessor (multi-crop) → ViT vision encoder → connector (pool + project) → decoder LLM**. Default encoder is **OpenAI CLIP ViT-L/14@336**; a 100%-open variant swaps in **MetaCLIP + OLMo**. Trained on the **PixMo** data suite.

## Related

- [MolmoAct](molmoact.md) — the VLA built on Molmo; the reason this entity exists.
- [VLA models](../concepts/learning/vla-models.md) — Molmo is a VLM backbone in the VLA taxonomy.
- [PaliGemma](paligemma.md) / [Gemma3](gemma3.md) / [SmolVLM-2](smolvlm.md) / [Eagle](eagle-vlm.md) — the other VLA VLM backbones tracked in the wiki.

## Open questions

- **[OLMo](olmo.md)** (the fully-open backbone) is now filed; **OLMoE** (the MoE backbone behind MolmoE-1B, arXiv 2409.02060) is still un-ingested.
- Does Molmo's pointing capability feed MolmoAct's action grounding directly (point → act), or only indirectly? Resolvable when the [MolmoAct](molmoact.md) paper (2508.07917) is filed.

## Mentioned in

- [Molmo and PixMo paper (Deitke et al. 2024)](../sources/molmo-pixmo-paper.md) — the primary source.
- [MolmoAct](molmoact.md) — the VLA that uses Molmo as its backbone.
