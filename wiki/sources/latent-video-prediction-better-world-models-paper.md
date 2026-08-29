---
title: "Latent Video Prediction Learns Better World Models (Alrasheed et al., 2026)"
type: source
url: https://arxiv.org/abs/2605.15618
local_path: raw/2605.15618.pdf
sha256: 2a1c60ffa31afed52797922de3a31f8432916e29b32c88ae800ec17d166ee306
author: Ali J Alrasheed, Aryan Yazdan Parast, Basim Azam, James Bailey, Naveed Akhtar
affiliations: The University of Melbourne; Monash University
venue: Preprint (arXiv 2605.15618v1)
published: 2026-05-15
ingested: 2026-08-08
license: CC BY 4.0
tags: [jepa, v-jepa-2, world-model, evaluation, robustness, occlusion, corruption, arrow-of-time, ssv2, latent-prediction]
---

## Summary

**States the JEPA evaluation gap outright and fills part of it.** Self-supervised video models are increasingly framed as world models, "yet their evaluation remains largely confined to a single top-1 accuracy score on clean benchmarks" — which says nothing about the properties a deployed world model actually needs. This is "the first systematic study addressing this gap": four **matched-capacity ViT-L** frontier video models, frozen, read out through a unified attentive probe, across **five robustness axes**. Over **1,000 A100 GPU-hours**.

The models span the three dominant self-supervised paradigms: **latent prediction** (V-JEPA 2.1, V-JEPA 2), **contrastive + masked prediction** (VideoPrism), **pixel reconstruction** (VideoMAEv2). Capacity, readout protocol, and data distribution are held fixed so that only the pretraining objective varies.

Finding: across all five axes, latent-prediction models form "a distinct and consistent profile."

> [!warning] Scope this carefully — it is not robot control
> Everything is measured on **Something-Something v2** action classification (220k+ videos, 174 fine-grained human-object interaction classes), not on planning or manipulation success. This is a *representation-quality* argument for latent prediction, not a demonstration that JEPA world models plan better. The wiki's planning evidence still comes from [DINO-WM](../entities/dino-wm.md), [LeWorldModel](../entities/leworldmodel.md), [JEPA-WMs](jepa-wms-paper.md), and [stable-worldmodel](stable-worldmodel-paper.md).

## Key claims

### The five axes

| Axis | Protocol |
|---|---|
| **Feature discriminability** | 600 videos / 30 classes, stratified by semantic difficulty (different-verb → same-verb → pretend-vs-real) |
| **Corruption robustness** | Six ImageNet-C corruptions (motion blur, snow, pixelation, impulse noise, brightness, elastic) × 3 severities, 500 balanced videos |
| **Fine-grained action discrimination** | The "pretending" subset — 1,992 videos, 22 classes, where real vs simulated interaction differs only in fine spatiotemporal contact cues |
| **Occlusion robustness** | Three spatiotemporal occlusion paradigms × 3 severities, 1,740 videos / 174 classes |
| **Temporal robustness** | Frame shuffling, reversal, static replacement, noise injection — 1,740 videos / 174 classes |

### The result that should change how the wiki reads representation metrics

> **Under the most severe spatiotemporal patch dropout, VideoPrism maintains representational similarity above 0.98 while collapsing to 2.7% top-1 accuracy. V-JEPA 2.1 retains 46.1% on the same clips.**

"Stable features are not the same as usable features." A representation can look almost perfectly preserved by cosine similarity and carry nothing you can act on — **cosine similarity alone is a misleading measure of representational stability.**

This is the latent-space twin of the [WorldArena](worldarena-paper.md) finding. There, a video that *looks* right scores 0.360 against planning utility. Here, an embedding that *looks* stable scores 2.7% against the task. Both are the same error: mistaking a surface-level similarity metric for functional adequacy.

### The other four findings

- **Corruption**: V-JEPA 2.1 leads on **five of six** corruption types and shows the slowest degradation across severities — "consistent with the joint-embedding predictive objective discarding surface-level visual variation in favour of higher-order semantic structure."
- **Fine-grained contact cues without pixels**: V-JEPA beats the pixel-reconstruction baseline on virtually every "pretend action" class, with the **largest margins precisely on the classes whose discriminative signal is the absence of actual physical contact**. A model that never reconstructs pixels detects that a hand didn't quite touch the object better than one trained to reproduce pixels.
- **Arrow of time**: under video reversal, V-JEPA models "flip predictions coherently to semantically antonymous classes" — pushing ↔ pulling — scoring a **Directional Semantic Coherence Score several times higher** than VideoMAEv2 and VideoPrism. The latent predictors have internalized temporal direction; the others largely haven't.
- **Frozen beats fine-tuned**: a frozen V-JEPA 2 with a lightweight attentive probe **outperforms an end-to-end fine-tuned VideoMAE and a fully supervised TimeSformer** on corruption and occlusion robustness. Task-specific optimization does not buy back the robustness the pretraining objective confers.

### Supporting prior work the paper surfaces

- **Garrido et al.** — V-JEPA acquires intuitive physics understanding through representation-space masked prediction alone, while **pixel-reconstruction models perform near chance** on the same benchmarks.
- **Joseph et al.** — first interpretability study of physics representations inside V-JEPA 2 vs VideoMAEv2; latent prediction produces "qualitatively different internal organisation." (Independently corroborated by the per-layer profile in [action-relevant latents](action-relevant-latents-paper.md).)

## Entities mentioned

- [V-JEPA 2](../entities/v-jepa-2.md) (and V-JEPA 2.1) · [DINO-WM](../entities/dino-wm.md) · [NVIDIA Cosmos](../entities/nvidia-cosmos.md) · [Genie](../entities/genie-3.md) (Genie 2, in related work)
- VideoPrism, VideoMAEv2, TimeSformer, Something-Something v2 — no wiki pages

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — the strongest single collection of evidence in the wiki for the latent-prediction bet, on representation quality rather than planning.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) · [latent space](../concepts/world-models/latent-space.md)
- [Generative-video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md)

## Open questions

- **SSv2 classification is not world modeling.** The paper argues from action recognition to world-model suitability. That inference is plausible and explicitly framed as being about deployment-relevant *properties*, but no planning, control, or robot task appears anywhere in it.
- **Public checkpoints only.** Capacity, protocol, and data are matched; pretraining data volume, recipe, and compute are not, and "cannot be equalised without retraining from scratch under a shared compute budget." V-JEPA 2 saw 1M+ hours of internet video — some of the advantage may be corpus, not objective. The companion paper [action-relevant latents](action-relevant-latents-paper.md) attributes most of the gain to temporal video pretraining rather than the JEPA objective specifically, which is consistent with that worry.
- **VideoPrism's 0.98-similarity / 2.7%-accuracy result deserves replication.** It is the paper's most striking number and rests on one model under one occlusion paradigm.
- **No error bars on the headline comparisons** in the abstract or introduction; per-axis variance is reported only in figures.
