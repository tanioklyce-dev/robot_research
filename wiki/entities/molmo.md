---
title: Molmo
type: entity
subtype: vlm
created: 2026-07-17
updated: 2026-07-17
sources: 1
tags: [molmo, vlm, allen-institute, ai2, pixmo, open-weights, open-data, pointing, vla-backbone]
status: stub
---

# Molmo

**Molmo** (*Multimodal Open Language Model*; Deitke et al., 2024 — *Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Multimodal Models*, arXiv 2409.17146) is a family of **[vision-language models](../concepts/learning/vla-models.md)** from the **Allen Institute for AI (Ai2)**, distinguished by being **fully open** — open *weights and* open training *data* (the PixMo datasets) — rather than open-weights-but-closed-data. It is the VLM backbone under **[MolmoAct](molmoact.md)**.

## Why it matters in this wiki

Molmo appears here as the **backbone of [MolmoAct](molmoact.md)**, the Allen Institute VLA baseline in the wiki's [LIBERO](libero.md) table. Two properties make Molmo a natural VLA backbone:

- **Pointing.** Molmo's signature capability is **pointing to pixels** — outputting 2D image coordinates to reference objects. That is directly action-grounding-relevant: a VLM that can point at "the mug" is a short step from a policy that can act on it, which is the lineage MolmoAct's "reason in space" framing builds on.
- **Fully-open provenance.** PixMo training data is **human-collected, not distilled from proprietary VLMs** (dense captions via speech, free-form Q&A, 2D point annotations). This puts Molmo in the same "open-data" spirit as the wiki's other reproducibility-first VLA work ([SmolVLA](smolvla.md), [LeRobot](lerobot.md)), and contrasts with the closed-data backbones (PaliGemma, Gemma3) used by π0 / π0.7.

Among the wiki's [VLM backbones for VLAs](../concepts/learning/vla-models.md), Molmo is the **Allen-Institute open-data** option, sitting alongside NVIDIA's [Eagle](eagle-vlm.md), Google's [PaliGemma](paligemma.md)/[Gemma3](gemma3.md), and Hugging Face's [SmolVLM-2](smolvlm.md).

> [!note] Primary source not yet ingested
> This page is grounded in Molmo's role as the [MolmoAct](molmoact.md) backbone; the Molmo/PixMo paper (arXiv 2409.17146) is **not yet ingested**. Variant list and architecture below are from general knowledge of the release and should be confirmed against the paper when it's filed.

## Family (per the 2024 release — confirm on ingest)

- **MolmoE-1B** — Mixture-of-Experts (OLMoE backbone).
- **Molmo-7B-O** — OLMo-7B backbone.
- **Molmo-7B-D** — Qwen2-7B backbone (the "demo" model).
- **Molmo-72B** — Qwen2-72B backbone; the flagship.
- Common design: a **CLIP ViT** vision encoder projected into an open LLM (OLMo / OLMoE / Qwen2), trained on the **PixMo** data suite.

## Related

- [MolmoAct](molmoact.md) — the VLA built on Molmo; the reason this entity exists.
- [VLA models](../concepts/learning/vla-models.md) — Molmo is a VLM backbone in the VLA taxonomy.
- [PaliGemma](paligemma.md) / [Gemma3](gemma3.md) / [SmolVLM-2](smolvlm.md) / [Eagle](eagle-vlm.md) — the other VLA VLM backbones tracked in the wiki.

## Open questions

- **Primary source (arXiv 2409.17146) not ingested** — needed for the exact PixMo data recipe, the pointing-supervision method, benchmark numbers, and licensing. The **OLMo / OLMoE** open LLMs it builds on also have no wiki entity.
- Does Molmo's pointing capability feed MolmoAct's action grounding directly (point → act), or only indirectly? Resolvable when the [MolmoAct](molmoact.md) paper (2508.07917) is filed.

## Mentioned in

- [MolmoAct](molmoact.md) — the VLA that uses Molmo as its backbone.
