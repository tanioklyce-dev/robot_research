---
title: "Scaling Language-Free Visual Representation Learning (Web-SSL)"
type: source
url: https://arxiv.org/abs/2504.01017
local_path: raw/webssl_2504.01017.pdf
sha256: bca24285ea5432d63db6112512f906d2a3ba68bd7f0e95b0d149633a7ac0fc6d
author: David Fan, Shengbang Tong, Jiachen Zhu, Koustuv Sinha, Zhuang Liu, Xinlei Chen, Michael Rabbat, Nicolas Ballas, Yann LeCun, Amir Bar, Saining Xie
published: 2025-04-01
ingested: 2026-08-26
venue: arXiv (FAIR Meta + NYU + Princeton)
format: paper (21 pp)
tags: [webssl, web-dino, self-supervised, vision-encoder, clip, metaclip, scaling, vqa, mllm, lecun, saining-xie]
---

# Scaling Language-Free Visual Representation Learning

Project page: `davidfan.io/webssl`. Code: `github.com/facebookresearch/webssl`.

## Summary

Asks a controlled question the field had been answering by assumption: **"Do visual self-supervised approaches lag behind CLIP due to the lack of language supervision, or differences in the training data?"** The confound is that visual SSL and CLIP models are almost never trained on the same corpus. So this trains both on **the same data** — 2 billion MetaCLIP web images (**MC-2B**) — and evaluates via **VQA inside an MLLM** as a diverse testbed. Result: visual SSL scales *better* than CLIP in both data and model capacity, **does not saturate at 7B parameters**, and reaches CLIP-level performance across VQA and classic vision — **including OCR & Chart**, the category assumed to require language supervision.

> [!warning] This resolves an identity the wiki did not know it had
> The model family here is **Web-SSL**, and its DINOv2-style member is **Web-DINO**. The wiki has been discussing *both names on different pages without connecting them* — [WebSSL](../entities/webssl.md) as the backbone [Patch Policy](patch-policy-paper.md) recommends for robot learning, and **Web-DINO** as the image-SSL encoder that [action-relevant latents](action-relevant-latents-paper.md) measures at **0.16 action R²** with *negative* rotation. **They are the same models.** See [the entity page](../entities/webssl.md) for what that does to both claims.

## Key claims

### The controlled setup, which is the contribution

- **Same data for both arms**: 2B samples from MetaCLIP (MC-2B), images only for the SSL arm.
- **Model scale**: ViTs at **1B, 2B, 3B, 5B, 7B** parameters.
- **Evaluation**: **16 tasks across 4 VQA categories** — General, Knowledge, **OCR & Chart**, Vision-Centric — under a fixed visual-instruction-tuning setup with **Llama-3 8B Instruct** held constant, mostly at 224×224 for comparability. Plus classic vision: ImageNet-1k linear probe, ADE20K, NYU Depth v2, following the DINOv2 protocol.
- Deliberately *not* an MLLM SOTA attempt: no unfrozen vision encoder, no resolution tiling, no spatial visual aggregator. "The primary motivation is still to provide controlled insights."

### The four findings

1. **Visual SSL can match and even surpass language-supervised pretraining on VQA — including OCR & Chart**, the language-adjacent category where CLIP was assumed to be structurally advantaged.
2. **It scales well in both model capacity and data**, and **performance does not saturate even at 7B parameters** — "indicating that SSL has significant untapped potential."
3. **Classic vision performance stays competitive** (classification, segmentation) *while* VQA improves — the two do not trade off.
4. **Data composition matters more than expected**: training on a **higher ratio of images containing text** is especially effective for OCR & Chart. "Exploring data composition is a promising direction."

**Head-to-head**: Web-DINO outperforms off-the-shelf MetaCLIP on both VQA and classic vision, and **matches SigLIP and SigLIP 2 on VQA despite seeing 5× less data.**

### The framing

Explicitly a "bitter lesson" argument: *"imposing less supervision — including language — remains a promising direction."* Positioned as "a compelling vision-centric alternative to the recent CLIP-dominated trend."

## Limitations, as stated

- **No zero-shot classification out of the box** — the structural cost of dropping language. The paper's answer is that instruction tuning inside an MLLM recovers downstream performance; LiT-style adaptation is named and declared out of scope.
- **One LLM backbone** (Llama-3 8B Instruct) held fixed; other backbones "hypothesized" to behave similarly, untested.
- **Only curated data** — MetaCLIP is a curated corpus; larger or uncurated datasets are left to future work.

## How this lands against the wiki

- **It supplies the primary for a recommendation the wiki was already carrying.** [Patch Policy](patch-policy-paper.md) recommends WebSSL as a robot-learning backbone with no citation the wiki had ingested. Now the model family, scale range, training corpus and objective are documented.
- **It sharpens the [SigLIP](../entities/siglip.md) story.** Web-DINO matching SigLIP 2 on VQA *at 5× less data*, then beating it as a policy backbone, is consistent with the wiki's reading that language-image alignment buys semantics at the cost of dense geometry.
- **[Yann LeCun](../entities/yann-lecun.md) is a co-author**, which places this alongside the [JEPA](../concepts/world-models/jepa.md) program rather than opposite it — both are language-free representation-learning bets, differing in whether the predictive structure is temporal.

## Entities mentioned

- [WebSSL / Web-DINO](../entities/webssl.md) — the model family.
- [Yann LeCun](../entities/yann-lecun.md), Saining Xie, Nicolas Ballas — FAIR/NYU.
- [SigLIP](../entities/siglip.md) / [SigLIP 2](../entities/siglip-2.md), [DINOv2](../entities/dinov2.md) — comparison encoders.
- **MetaCLIP / MC-2B**, **Llama-3 8B Instruct** — no pages.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — the downstream consumer of these encoders.
- [JEPA](../concepts/world-models/jepa.md) — the sibling language-free program.

## Open questions

- **No control or robotics evaluation anywhere in the paper.** Every claim is VQA or classic vision. Its use as a *policy* backbone is entirely [Patch Policy](patch-policy-paper.md)'s finding, and its *action-relevance* is measured — badly — by [action-relevant latents](action-relevant-latents-paper.md). Nothing here anticipates either.
- **Which Web-SSL variant do downstream users take?** The family spans 1B–7B and DINO-style vs other objectives; neither [Patch Policy](patch-policy-paper.md) nor the wiki records which checkpoint was used.
- **Zero-shot classification is genuinely lost**, which matters for any open-vocabulary perception pipeline — a real cost the robot-learning framing tends to skip.
