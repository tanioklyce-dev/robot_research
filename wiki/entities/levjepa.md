---
title: LeVJEPA
type: entity
subtype: model
created: 2026-09-03
updated: 2026-09-03
sources: 1
tags: [levjepa, jepa, lejepa, sigreg, video, self-supervised, pretraining, balestriero, lecun, lucas-maes, encoder, flop-efficiency]
---

**LeVJEPA** — the video member of the "Le-" family: a **video encoder** trained with an invariance loss over temporal views plus [SIGReg](../concepts/world-models/sigreg.md), with **no EMA teacher and no stop-gradient**. arXiv **2608.27395**, *"LeVJEPA: Efficient & Scalable Video Pretraining without the Heuristics"*, submitted **2026-08-27** — Lukas Kuhn, [Lucas Maes](lucas-maes.md), Giuseppe Serra, Quentin Le Lidec, [Yann LeCun](yann-lecun.md), [Randall Balestriero](randall-balestriero.md), Florian Buettner. Code at `MLO-lab/LeVJEPA`.

## What it is, and what it is not

Structurally it is [LeJEPA](../sources/lejepa-paper.md) with more frames. Encode global and local views of a clip (masking patches, augmentation, or both), predict one view's embedding from the other, and regularize with SIGReg so the embedding distribution stays isotropic Gaussian. The only change from the image case is that the views now span time.

> [!note] It is the encoder half, not a world model — its author says so
> Asked directly at the [Day 3 tutorial](../sources/chicago-booth-world-modeling-workshop-2026-day3.md), Balestriero: *"it is a video encoder that gives you a very strong embedding Z on which you can learn an action-conditioned predictor to do world modeling."* The family sorts cleanly:
>
> | Model | Encoder | Action-conditioned predictor |
> |---|---|---|
> | [LeJEPA](../sources/lejepa-paper.md) | images | — |
> | **LeVJEPA** | video | — |
> | [LeWM](leworldmodel.md) | learned jointly | **yes** |
>
> *"The common denominator among all of these is basically SIGReg and the prediction loss, and then it's a matter of: do you have actions or not?"*

## The claim

Comparable or better than **V-JEPA 2** at **5.6–20.8× less pretraining compute** across ViT scales, from **random token dropping** during training — which *"reduces computational cost while improving downstream performance."* It supports block-causal attention with no accuracy loss, and holds motion-recognition performance while staying competitive on appearance recognition against image-pretrained models.

The reason to care beyond the number: SIGReg's entire pitch is that stability removes the tuning tax. **A FLOP-efficiency win on video is the first result where that pitch pays a compute dividend rather than a convenience one.** Balestriero's framing at the workshop: *"this is really the very beginning of us starting to have reliable pre-training solutions where we can finally become more sample efficient, more FLOP efficient."*

Emergent-property demo shown live: PCA over patch embeddings, top three components as RGB, gives **zero-shot segmentation** of a video (dog cleanly separated from background) with no segmentation training — the standard [DINO](dinov2.md)-style visualization, applied to a model whose pretraining objective is *"seemingly simple."*

## Independently exercised at the workshop, within hours

At the Day 3 hackathon a participant (one of the paper's own promoters) trained a **DINO-WM-style action-conditioned predictor on frozen LeVJEPA features** over the MineRL navigate dataset — an interactive imagined rollout beside ground truth, learned *"in a very small amount of time on top of the frozen features."* Blurry, at 64×64, and honest about it. **It is the fastest demonstration in the wiki of the frozen-encoder + learned-predictor recipe**, and it validates the division of labour the model is designed around.

## Related

- [SIGReg](../concepts/world-models/sigreg.md) — the anti-collapse term; LeVJEPA is its video-scale validation.
- [LeWorldModel](leworldmodel.md) — the action-conditioned sibling.
- [V-JEPA 2](v-jepa-2.md) — the baseline it undercuts on compute.
- [DINO-WM](dino-wm.md) — the frozen-encoder-plus-predictor pattern the hackathon demo used on it.
- [JEPA](../concepts/world-models/jepa.md) · [Randall Balestriero](randall-balestriero.md) · [Lucas Maes](lucas-maes.md) · [Yann LeCun](yann-lecun.md).

## Mentioned in

- [Third World Modeling Workshop — Day 3](../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — announced in the tutorial; demoed on frozen features at the hackathon the same afternoon.

> [!note] The paper itself is not ingested
> This page is built from the arXiv abstract and the Day 3 tutorial's narration. The compute-efficiency comparison, the token-dropping ablation, and the block-causal-attention result all need the primary before they are quoted in anything load-bearing.
