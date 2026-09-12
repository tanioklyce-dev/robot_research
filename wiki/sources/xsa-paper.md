---
title: Exclusive Self Attention (Zhai, Apple; 2026)
type: source
url: https://arxiv.org/abs/2603.09078
fetch_url: https://arxiv.org/pdf/2603.09078v1
author: Shuangfei Zhai
published: 2026-03-10
ingested: 2026-09-11
venue: arXiv technical report (v1; 7 pp.)
local_path: raw/2603.09078v1.pdf
sha256: 5a9b87ebda526d9562479e6ced017dd8b433551d9f7f938bf09aefcc5b592984
format: pdf
tags: [xsa, attention, transformer, language-modeling, architecture, apple, nanogpt, fineweb, lehome-challenge]
---

## Summary

A two-line change to self-attention, ingested because the [LeHome Challenge](../entities/lehome-challenge-2026.md) winner adopted it "on recent fashion" without ablation ([Larchenko](larchenko-learning-to-fold-tech-report.md)). The observation: in a trained 1.3B language model, attention output y_i has high cosine similarity with the token's own value vector v_i, rising with depth — value vectors are positively correlated within a sequence and the diagonal attention weight is large. Zhai calls this the **attention similarity bias** and argues it means attention is spending capacity on the point-wise transformation the FFN already handles through the residual path. **XSA** removes it: z_i = y_i − (y_iᵀv_i) v_i / ‖v_i‖², the projection of the attention output onto the self-value direction. On NanoGPT / FineWeb-100BT at 0.7B, 1.4B and 2.7B, XSA lowers training and validation loss throughout training, lifts the 8-task downstream average by **+0.26 / +1.03 / +1.36** points with the gap growing with size and with sequence length, holds across four learning rates, and costs almost nothing in time or memory. There is no theory; "we defer to empirical evaluations as the main justification."

## Key claims

- **Setup:** RoPE, an extra LayerNorm after embeddings, 2048 context, batch 0.5M tokens, 200K iterations ≈ 100B tokens, AdamW with cosine decay; learning rate grid-searched for the baseline and reused for XSA.
- **Downstream (Table 2, ARC-E / BoolQ / HellaSwag / LAMBADA / OBQA / PIQA / SocialIQA / WinoGrande):** averages 53.22 → 53.48 (0.7B), 56.16 → 57.19 (1.3B), 58.06 → 59.42 (2.7B). Individual tasks move both ways (OBQA −2.8 at 0.7B; BoolQ −3.2 at 1.3B; SocialIQA −1.5 at 2.7B).
- **Sequence length:** gains increase with context; robust to the presence of attention sinks (§4.2).
- **Overhead:** benchmarked on a B200 in bf16 across sequence lengths and widths — "minimal."

## Reading it against the wiki

- **It is a language-modeling result at ≤2.7B on text.** Nothing in the paper concerns policies, images, diffusion heads, or the ~100M-parameter regime a robot policy lives in. The LeHome winner's adoption is therefore an untested transfer — which the winner's own report acknowledges. The right reading is "harmless and cheap, unproven for control."
- **The mechanism is plausible and the evidence is one training run per size** — no seeds, no confidence intervals, single codebase. The [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) reflex applies to loss curves too: the 0.7B downstream gain (+0.26) is inside task-to-task noise; the 2.7B gain is the one that looks real.
- Belongs in the [sequence-model lineage](../syntheses/sequence-models/language-model-to-transformer-lineage.md) as a 2026 micro-modification, alongside attention sinks and QK-norm.

## Entities mentioned

- Apple (no page); the [LeHome Challenge](../entities/lehome-challenge-2026.md) winner as the wiki's only downstream user.

## Concepts touched

- [Language-model → transformer lineage](../syntheses/sequence-models/language-model-to-transformer-lineage.md).

## Open questions

- Any ablation of XSA inside a diffusion-policy or VLA transformer — none exists in the wiki.
- Whether the gain persists past 2.7B and 100B tokens; the author speculates yes.
