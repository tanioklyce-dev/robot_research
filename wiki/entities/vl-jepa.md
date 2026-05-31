---
title: VL-JEPA
type: entity
subtype: model
created: 2026-05-31
updated: 2026-05-31
sources: 1
tags: [vl-jepa, jepa, vlm, vision-language, meta, lecun, gqa, embedding-prediction]
---

> [!warning] Name collision — not the same as [VLA-JEPA](vla-jepa.md)
> **VL-JEPA** (this page) is a *Meta / LeCun* **vision-language** JEPA — it reframes the whole VLM by predicting **text embeddings** instead of generating tokens (Chen et al., arXiv **2512.10942**, Dec 2025). **[VLA-JEPA](vla-jepa.md)** is a separate USTC paper (Sun et al., arXiv 2602.10098, Feb 2026) that adds a JEPA *auxiliary* objective inside a vision-language-**action** robot policy. Different groups, different ideas; the near-identical names are an unfortunate coincidence.

**VL-JEPA** — "VL-JEPA: Joint Embedding Predictive Architecture for Vision-language" ([Chen, Shukor, Moutakanni, Chung, Yu, Kasarla, Bang, Bolourchi, **LeCun**, Fung — arXiv 2512.10942](https://arxiv.org/abs/2512.10942), v1 Dec 11 2025 / v2 Feb 2 2026). Applies the [JEPA](../concepts/world-models/jepa.md) recipe to a full **vision-language model**: rather than autoregressively generating output text, it encodes the target text and trains a predictor to hit that text's **embedding**, conditioned on the image + prompt. The first JEPA reframing of the *entire* VLM (not just the vision encoder, as in [V-JEPA 2](v-jepa-2.md)). Surfaced in the wiki via the [Welch Labs Part 2 explainer](../sources/welchlabs-lecun-1b-bet-against-llms-part2.md).

## Approach
- Standard VLM: vision encoder → embeddings → LLM → output **tokens**.
- VL-JEPA: vision encoder → embeddings → **predictor** (the LLM's structural role) → predicted **embedding of the output text**. Prompt is passed in as predictor conditioning.
- Abstracts away irrelevant phrasing of correct answers (multiple correct paraphrases map to similar target embeddings), so the model isn't penalized for semantically-correct rewordings — the same "don't waste capacity on unpredictable surface detail" argument JEPA makes against pixel reconstruction.
- **Not generative by default.** Two workarounds: (1) multiple-choice via embedding similarity (encode all candidate answers, pick the nearest to the prediction); (2) train a **text decoder** to map predicted embeddings back to text for generative-style inference.
- Uses a **SONAR encoder/decoder** operating at the **sentence level** (not token level) for the controlled VLM-vs-JEPA comparisons (per the video's technical note).

## Headline results
- **Efficiency**: reaches **35% video-classification accuracy after 5M examples vs 20%** for a matched standard VLM (same vision encoder, data, config) — per the [Welch Labs explainer](../sources/welchlabs-lecun-1b-bet-against-llms-part2.md).
- **Punching above weight**: a **1.6B-param** VL-JEPA outperforms **7B-param** models on the **GQA** compositional-reasoning benchmark (video framing).
- Paper abstract framing: **50% fewer trainable parameters** and **2.85× fewer decoding operations** vs token-space VLM training; **comparable to InstructBLIP / QwenVL** on GQA, TallyQA, POPE, POPEv2; **surpasses CLIP / SigLIP2 / Perception Encoder** on 8 video-classification + 8 video-retrieval datasets.

> [!note] Two numbers, two sources
> The "35% vs 20%" and "1.6B beats 7B" figures are the video's framing; the paper's own abstract leads with the parameter/decoding-efficiency and parity-with-InstructBLIP/QwenVL claims. Reconcile against the paper body when it's ingested as a primary source.

## Why it matters
- **Fills the middle rung of the "alternative stack."** The [Welch Labs Part 2](../sources/welchlabs-lecun-1b-bet-against-llms-part2.md) framing: [V-JEPA 2](v-jepa-2.md) is the JEPA *vision encoder*, VL-JEPA is the JEPA *VLM*, [LeWorldModel](leworldmodel.md) is the JEPA *robot controller*. VL-JEPA is the layer that shows JEPA can interface with — and improve on — the language stack, not just the perception stack.
- **Evidence JEPA is "not incompatible" with mainstream LLM-driven AI**, countering the assumption that the JEPA program is a wholesale replacement rather than a reusable training objective.

## Related
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — architecture family.
- [V-JEPA 2](v-jepa-2.md) — JEPA at the vision-encoder layer (VL-JEPA can sit on top of it).
- [VLA-JEPA](vla-jepa.md) — **different paper, similar name** (see warning above).
- [Yann LeCun](yann-lecun.md) — co-author.
- [VLA models](../concepts/learning/vla-models.md) — the generative-stack counterpart VL-JEPA reframes.

## Mentioned in
- [Welch Labs — Yann LeCun's $1B Bet Against LLMs Part 2 (video)](../sources/welchlabs-lecun-1b-bet-against-llms-part2.md)
