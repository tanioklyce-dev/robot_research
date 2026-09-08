---
title: "LeVJEPA: Efficient & Scalable Video Pretraining without the Heuristics (Kuhn et al., 2026)"
type: source
url: https://arxiv.org/abs/2608.27395
fetch_url: https://arxiv.org/pdf/2608.27395v1
local_path: raw/2608.27395v1.pdf
sha256: 047a945c5ccc7846269aa077fabce672f2b6c62b1aefba38ffa23004e63bad08
author: "Lukas Kuhn, Lucas Maes, Giuseppe Serra, Quentin Le Lidec, Yann LeCun, Randall Balestriero, Florian Buettner"
published: 2026-08-27
venue: "arXiv preprint (v1 only, no venue stated). 12 pp."
format: paper (PDF)
tags: [levjepa, lejepa, sigreg, jepa, video-pretraining, token-dropping, block-causal-attention, v-jepa-2, dinov2, videomae, compute-efficiency, streaming-perception, balestriero, lecun]
ingested: 2026-09-07
---

## Summary

**SIGReg carried to video — and the payoff is not stability, it is that video stops being expensive.** LeVJEPA trains a video encoder under [LeJEPA](lejepa-paper.md)'s collapse-free objective: a single encoder, an invariance loss over global and local views of a clip, regularized by [SIGReg](../concepts/world-models/sigreg.md), with **no EMA target encoder, no stop-gradient, no capacity-limited predictor, and no pixel reconstruction**. The architecture reduces to *encoder + projector*, and the objective to **one hyperparameter, untuned**.

Removing the asymmetry stack turns out to unlock two things that have nothing to do with collapse:

1. **Cost is governed by how many tokens the encoder sees — and dropping tokens *improves* accuracy.** Uniform random dropping at **95%** beats no dropping by **13.7 points**. Result: **matches or surpasses V-JEPA 2 at 5.6–20.8× less pretraining compute.**
2. **With no branch asymmetry to preserve, the encoder can be block-causal at no accuracy cost** — 51.2% vs 50.7% bidirectional. *"Temporal ordering becomes a property of the encoder itself."*

The paper's own conclusion is a claim about the field rather than the method: *"once its computational overhead is removed, **video becomes a viable and in several respects preferable substrate for general-purpose visual pretraining**."*

The wiki had an [entity page for this](../entities/levjepa.md) built from the abstract and tutorial narration, with the compute claim, the token-dropping ablation and the causal-attention result all flagged as needing the primary. All three hold, and the causal one is bigger than the entity page suggested.

## The numbers

**Epoch-matched** (same data, same 240 epochs, same effective batch 3,072; baselines *retrained by the authors* with official implementations on the identical 20% K710 subsample):

| | LeVJEPA vs V-JEPA 2 |
|---|---|
| ViT-S | comparable at **20.8×** less compute |
| ViT-B | within **1 point**, at **4.8 vs 36.4 ExaFLOPs** |
| ViT-L | **+1.9 points** at **5.6×** less compute |

And the line that lands hardest: **LeVJEPA's ViT-L consumes less than half the compute of V-JEPA 2's ViT-S.**

**FLOP-matched** (ViT-B, equal total budget — which buys LeVJEPA a 1,085-epoch schedule with V = 10):

| Method | IN1K | SSv2 | K400 |
|---|---|---|---|
| VideoMAEv2 | 53.4 | **43.6** | 37.4 |
| V-JEPA 2 | 51.6 | 42.5 | 40.7 |
| **LeVJEPA** | **61.0** | 40.4 | **44.6** |

**+7.6 points on ImageNet** over the strongest baseline, best on K400, and **−3.2 on Something-Something-v2** — it loses on the motion benchmark, which they state plainly and name as *"the axis with the most remaining headroom."*

**Against an image model at matched FLOPs** (ViT-B, DINOv2 trained on individual frames of the *same* videos):

| | IN1K | SSv2 |
|---|---|---|
| DINOv2 | **53.8** | 16.9 |
| LeVJEPA | 50.7 | **30.4** |

−3.1 on appearance, **~1.8× on motion**. Their claim for it: *"to our knowledge, this is the **first FLOP-matched comparison** in which video pretraining reaches near-parity with a state-of-the-art image method on appearance-centric evaluation while retaining a decisive advantage on motion-centric evaluation."*

**Data scaling**: ViT-L/16, 100 epochs on K710 + SSv2 + Walking Tours + PE Video → **69.5% IN1K, 55.0% SSv2** — **+9.5 IN1K** over the 20% subsample *in a shorter schedule*, with a corpus *"orders of magnitude below the internet-scale collections of V-JEPA 2, indicating **headroom rather than saturation**."*

## The four ablations, which are the interesting half

**1. Token dropping improves representations — monotonically.** IN1K frozen attentive probe against drop ratio ρ:

| ρ | 0% | 30% | 60% | **95%** |
|---|---|---|---|---|
| IN1K | 33.9 | 39.6 | 44.8 | **47.6** |

*"If token dropping constituted merely an approximation adopted for efficiency, downstream accuracy would be expected to degrade as ρ increases. We observe the opposite."* The mechanism they give is about *which* tokens: *"a tube pattern permanently occludes the majority of the scene across all frames, whereas **uniform random dropping yields a spatio-temporally distributed sample from which the content of the clip remains identifiable**."*

**2. Temporal patch aggregation is not required.** The conventional τ = 2 (pairing consecutive frames at input to halve tokens) *loses* to per-frame τ = 1 at a matched token budget — **50.7 / 30.4 against 47.4 / 28.8** — including on SSv2, the benchmark aggregation is usually motivated by.

**3. Block-causal attention is free.** Bidirectional 50.7, **block-causal 51.2**. Adopted as the default.

**4. Local-view budget is unexhausted.** V = 4 → 47.6, V = 10 → **50.2**, saturating at 12. **They use V = 4 for every headline comparison** and report the sweep to show the results *"do not exhaust the method."* Conservative, and stated.

> [!note] The result with the most reach for this wiki is the causal one
> Their discussion draws it out, and it is a direct hit on the [world-action model](../concepts/world-models/world-action-model.md) architecture:
>
> > Current systems obtain causal dynamics by **fitting a temporal model over the frozen outputs of a pretrained encoder**, an arrangement that has proven effective for planning and control but that **separates representation learning from temporal structure**. Our results show that the two need not be separated: causality can be established during pretraining, at no measurable cost… such that the encoder itself provides **per-frame state that respects temporal ordering and extends to incoming frames without re-encoding**. This positions a single pretrained encoder as a foundation for **streaming perception and autoregressive world modeling**.
>
> "Extends to incoming frames without re-encoding" is the property a robot needs and that a bidirectional video encoder cannot have. Note what it would change for [mimic-video](mimic-video-paper.md), which reads intermediate features out of a **bidirectional** diffusion backbone and pays a full forward pass per action chunk: a block-causal encoder amortizes across the stream instead.

## The view recipe, read in full (2026-09-07)

Checked because [the abstraction tax](../syntheses/world-models/abstraction-tax.md) turns on which axes a training procedure declares irrelevant.

**One global view + V local views**, `V = 4` for every headline result. Local views are *"obtained by **aggressive spatial cropping and photometric augmentation**"*, and the constraint that matters:

> All views **share the identical temporal window and differ only spatially and photometrically.**

The augmentation vocabulary is named but never itemized — *photometric* appears without a list, and **"jitter", "flip", "blur", "grayscale" and "solarize" appear zero times in the paper**. The construction is DINO's multi-crop, stated as such: *"LeVJEPA adopts the global–local view construction of this line, but none of its collapse-prevention machinery."*

Token dropping is a third declaration, and they say so: at ρ = 0.95 it *"simultaneously acts as a **stochastic augmentation** that requires the clip-level embedding to be inferable from sparse, randomly located observations of the clip."*

> [!note] The asymmetry comes from the views, not from a teacher
> > As the global view is the only view that remains **photometrically unaltered** and covers the largest spatial extent, it constitutes the prediction target **by construction of the views alone**.
>
> [The anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) shows branch asymmetry is the load-bearing ingredient and the EMA is one substitutable source of it. This is another: **augmentation asymmetry**. The teacher is the same encoder shown the least-corrupted view. `L = L_inv + λ·L_SIGReg` with λ = 0.02, untuned.

**So the declared axes are spatial position, photometric appearance, and which tokens you see — and nothing about time.** That is the wiki's explanation for why the results split the way they do: **+7.6 IN1K, −3.2 SSv2**. And the split appears inside the dropping sweep too, which this page had not recorded:

> On Something-Something-v2, **which primarily probes motion understanding, accuracy declines for dropping ratios beyond 0.3**, in contrast to the monotonic improvement observed on ImageNet.

Their interpretation is the same mechanism in their own words — sparse random observations render *"motion cues, which depend on correspondences across frames, less frequently recoverable within a single view."*

> [!warning] But the motion loss is partly bought back by compute
> *"With longer training, higher dropping ratios **recover** the accuracy of lower ones on Something-Something-v2 while retaining their lower per-iteration cost"* — *"additional iterations compensate for the reduced per-sample signal."*
>
> So this is a **sample-efficiency tax on the undeclared axis, not a hard representational limit** — an important qualification anywhere the wiki says an undeclared axis is *lost*. The FLOP-matched headline still loses SSv2 by 3.2 on a 1,085-epoch schedule, and *"dropping schemes that preserve motion information at high sparsity"* is named as unsolved.

**Tube dropping is the control**: retaining identical spatial locations in every frame drops ImageNet from **50.7% to 39.6%**, same ordering on SSv2 — the shortcut argument for why *uniform random* is the right sparsity pattern.

## Two more things worth keeping

**Consumer-hardware pretraining, with a number.** ViT-Tiny, **12 hours on a single RTX 5080 (16 GB)**, on **eight videos** of Walking Tours (~620k frames, ~5M clips) — *"unlabeled, uncurated egocentric footage."* ImageNet top-1 of the frozen encoder goes **8.9% → 25.2%**. The memory comparison is the sharper half: **LeVJEPA trains at batch 128 in under 8 GB; a V-JEPA configuration with an identically sized encoder saturates the same card at batch 28.**

**Emergent patch-level structure, for free.** The objective supervises **a single clip-level token**; patch tokens receive no loss at any point. Their PCA and cosine-similarity visualizations show the patch tokens nevertheless organize semantically and *spatially precisely* — *"a degree of visible organization that **V-JEPA 2 does not exhibit and that V-JEPA 2.1 obtains through an explicitly introduced auxiliary patch-level objective**."* If that holds, a competitor's added objective is here a side effect.

## Where to hold it at arm's length

- **v1, arXiv preprint, no venue.** Single version, no peer review recorded.
- **The baselines are the authors' retrainings.** Retraining V-JEPA 2 and VideoMAEv2 on identical data and schedule is the *right* way to remove confounds, and it means the comparison numbers are not the baselines' own published results. Official implementations and recommended hyperparameters are stated.
- **Frozen attentive probing throughout**, which is the [contested metric](../concepts/learning/representation-evaluation.md) — though consistent with how the JE line evaluates, and this paper's whole case is about frozen-encoder quality.
- **The 61.0 headline comes with a 1,085-epoch schedule.** FLOP-matching is fair, but a 4.5× longer schedule is a different training regime, not just a cheaper one.
- **It loses on motion at matched FLOPs** (−3.2 SSv2) and says so. Aggressive dropping is the suspected cause: *"dropping schemes that preserve temporal correlation"* is named as future work.

> [!note] It fits today's other ingest, and slightly complicates it
> [Joint-Embedding vs Reconstruction](joint-embedding-vs-reconstruction-paper.md) (same senior author, NeurIPS 2025) says joint-embedding wins when irrelevant features have high magnitude. LeVJEPA vs **VideoMAEv2** is exactly that contest on video — and at matched FLOPs the joint-embedding method wins IN1K by 7.6 and K400 by 7.2 while **losing SSv2 by 3.2**.
>
> So the crossover is visible *within a single comparison*: appearance-centric evaluation favours the joint-embedding encoder, motion-centric favours reconstruction. Neither paper cites the other and neither offers this reading; recorded here as an observation, not as their claim.

## Entities mentioned

- [LeVJEPA](../entities/levjepa.md) — the model; entity page now backed by the primary.
- [Randall Balestriero](../entities/randall-balestriero.md) · [Yann LeCun](../entities/yann-lecun.md) · [Lucas Maes](../entities/lucas-maes.md) — co-authors. **Lukas Kuhn**, **Giuseppe Serra**, **Quentin Le Lidec**, **Florian Buettner** — no pages.
- [V-JEPA 2](../entities/v-jepa-2.md) · [DINOv2](../entities/dinov2.md) — the baselines. VideoMAEv2 — no page.

## Concepts touched

- [SIGReg](../concepts/world-models/sigreg.md) · [JEPA](../concepts/world-models/jepa.md) — the objective, now demonstrated on video.
- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) — the asymmetry stack this removes is that page's whole subject.
- [World-action model](../concepts/world-models/world-action-model.md) — block-causal encoders vs temporal models fitted over frozen features.
- [Generative-video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md) — the compute column, substantially revised by 5.6–20.8×.
- [Representation evaluation](../concepts/learning/representation-evaluation.md) — frozen attentive probing throughout.
- [Scaling laws for VLAs](../concepts/learning/scaling-laws-vla.md) — "headroom rather than saturation" on a corpus orders of magnitude below internet scale.

## Open questions

- **Does the causal encoder actually help a robot?** The paper positions block-causal pretraining as *"a foundation for streaming perception and autoregressive world modeling"* and demonstrates it on ImageNet/SSv2/K400. **No robot, no control task, no latency measurement.** The claim this wiki most wants tested is the one furthest from the evidence.
- **What happens to [mimic-video](mimic-video-paper.md)'s architecture with a causal backbone?** It reads intermediate features from a bidirectional diffusion model at one forward pass per chunk. A causal encoder that *"extends to incoming frames without re-encoding"* is a different cost structure entirely, and nobody has tried it.
- **Does 95% token dropping survive contact-rich video?** Uniform random dropping works because *"the content of the clip remains identifiable."* In tight-tolerance manipulation the decisive information is small, local and occluded — the regime where a 95% sample is least obviously safe.
- **Is the motion gap the objective or the dropping?** They suspect dropping. A dropping scheme preserving temporal correlation would separate the two, and would decide whether the JE-vs-reconstruction crossover above is about the paradigm or about their efficiency trick.
