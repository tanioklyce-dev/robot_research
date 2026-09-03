---
title: "Representation Learning with Contrastive Predictive Coding (van den Oord, Li & Vinyals, 2018)"
type: source
url: https://arxiv.org/abs/1807.03748
fetch_url: https://arxiv.org/pdf/1807.03748v2
local_path: raw/1807.03748v2.pdf
sha256: 5ef5e1ab47d2273f418f01f66fb8eb1431ba9b185b7cba45e9955f0fee36427d
author: "Aaron van den Oord, Yazhe Li, Oriol Vinyals (DeepMind)"
published: 2018-07-10
venue: "arXiv preprint (v2, 2019-01-22)"
format: paper (PDF, 13 pp.)
tags: [cpc, infonce, contrastive-learning, self-supervised, mutual-information, predictive-coding, representation-learning, speech, foundational]
ingested: 2026-09-03
---

## Summary

**The paper that named InfoNCE and gave it a mutual-information justification.** CPC proposes one recipe for unsupervised representation learning across every modality: **compress observations into a latent space, predict several steps into the future *in that latent space*, and train the prediction with a probabilistic contrastive loss instead of a reconstruction loss.** Demonstrated on speech, images, text and reinforcement learning with the same mechanism.

Read in 2026 it is startling how much of the current world-model argument is already here, eight years early. The central move — *do not predict the observation, predict its representation, and use a loss that does not require generating anything* — is [JEPA](../concepts/world-models/jepa.md)'s move. CPC makes it with negatives; [LeJEPA](lejepa-paper.md) makes it with a distributional regularizer. The disagreement is about the anti-collapse term, not the architecture.

## Key claims

**The objection to reconstruction, stated in 2018** (§2.1). Unimodal losses like MSE and cross-entropy *"are not very useful"* for high-dimensional prediction, and the generative models that would be needed *"waste capacity at modeling the complex relationships in the data x, often ignoring the context c."* The arithmetic they give is the memorable part: *"images may contain thousands of bits of information while the high-level latent variables such as the class label contain much less information (10 bits for 1,024 categories). This suggests that modeling p(x|c) directly may not be optimal."*

**The architecture** (§2.2). A non-linear encoder `g_enc` maps observations `x_t` to latents `z_t`; an autoregressive model `g_ar` summarizes `z_≤t` into a context `c_t`. Rather than predicting `x_{t+k}`, CPC models a **density ratio** `f_k(x_{t+k}, c_t) ∝ p(x_{t+k}|c_t) / p(x_{t+k})`, implemented as a log-bilinear score `exp(z_{t+k}ᵀ W_k c_t)` with a separate `W_k` per prediction step. Either `z_t` or `c_t` can serve as the downstream representation — `c_t` when past context helps (speech), `z_t` otherwise.

> [!warning] Correction — CPC coined the *name*, not the loss form
> This page originally called CPC "the origin of InfoNCE." [A Cookbook of Self-Supervised Learning](ssl-cookbook.md) (Fig. 2) traces the lineage, and the loss arrived in stages before this paper: [Bromley et al. 1993](bromley1993-siamese-signature-verification.md) (contrastive loss) → Goldberger et al. 2004 (Neighbourhood Component Analysis, the softmax-over-distances form) → Chopra 2005 / Hadsell 2006 (margin) → Weinberger & Saul 2009, Chechik 2010 (triplet) → **Sohn 2016** ((N+1)-tuple: inner products, negatives from other samples in the batch) → **Wu et al. 2018** (the "non-parametric softmax," which introduces **explicit normalization, the temperature τ, and the momentum-encoder idea** via proximal optimization) → **CPC**, which *"coins the name infoNCE by removing the proximal constraint and using positive pairs."*
>
> So the temperature and the momentum encoder both predate CPC **and MoCo**. What is genuinely CPC's: the **name**, the **mutual-information framing**, and the **`I ≥ log N − L_N` bound**.

**The InfoNCE loss** (§2.3). Given `N` samples containing one positive from `p(x_{t+k}|c_t)` and `N−1` negatives from `p(x_{t+k})`:

`L_N = −E[ log ( f_k(x_{t+k}, c_t) / Σ_j f_k(x_j, c_t) ) ]`

This is categorical cross-entropy for "which of these N is the real future." Two properties they prove:

- **The optimum is the density ratio**, and it is **independent of `N`**.
- **`I(x_{t+k}; c_t) ≥ log N − L_N`** — minimizing InfoNCE maximizes a lower bound on mutual information, and the bound tightens as `N` grows. *This is the origin of the "more negatives is better" folklore.* Whether it is a real engineering constraint is a separate question, and the answer turns out to be **mostly no** — see [contrastive learning](../concepts/learning/contrastive-learning.md).

**Predicting several steps ahead is load-bearing** (§3.1, Table 2). On LibriSpeech phone classification, predicting 2 steps gives 28.5% accuracy; 12 steps gives 64.6%; 16 steps gives 63.8%. The motivation is stated in terms of **slow features**: near-term prediction exploits local smoothness, while *"when predicting further in the future, the amount of shared information becomes much lower, and the model needs to infer more global structure."*

**Results, all with a linear probe on frozen features:**

| Domain | Result |
|---|---|
| LibriSpeech phone classification | **64.6%** (MFCC 39.7, random init 27.6, fully supervised 74.6) — and **72.5%** with a single hidden layer instead of linear |
| LibriSpeech speaker ID (251-way) | **97.4%** (supervised 98.5) |
| ImageNet top-1, ResNet-v2-101 encoder | **48.7%**, vs the previous best 39.6% (Colorization) — **+9 points absolute** |
| ImageNet top-5 | **73.6%**, vs 69.3% for a *combination* of four prior pretext tasks |
| NLP transfer (MR/CR/Subj/MPQA/TREC) | on par with skip-thought vectors; **96.8 on TREC** |
| DeepMind Lab RL (5 tasks) | CPC as an **auxiliary loss** on a batched A2C agent improves 4 of 5 after 1B frames |

**The one negative result is diagnostic.** The RL task where CPC does not help is `lasertag_three_opponents_small`, and their explanation is that it *"does not require memory and thus yields a purely reactive policy."* A predictive representation buys nothing where nothing needs to be predicted.

## Why this source matters to this wiki

> [!note] The wiki has cited InfoNCE on 21 pages without ever reading its origin
> Before this ingest, "InfoNCE" appeared across the wiki as a named loss with no source page — a term inherited from downstream papers. Three things the primary supplies that the paraphrases do not:
>
> 1. **The MI lower bound is why negatives were *thought* to scale.** `I ≥ log N − L_N` tightens with N, and every subsequent complaint about large batches, memory banks and mining strategies ([BYOL](byol-paper.md) §1) traces to this inequality. The [Cookbook](ssl-cookbook.md) §3.5.1 then calls the practical conclusion **"misleading"** — with square-root LR scaling, SimCLR trains on ImageNet on a single GPU, and DCL reaches top performance at batch 256.
> 2. **The image formulation is patch-to-patch, not view-to-view.** CPC on images predicts *lower rows of a 7×7 grid of overlapping 64×64 crops from upper rows*, with a PixelCNN-style autoregressive model — spatial-autoregressive, not two-augmented-views. The modern contrastive setup ([SimCLR](byol-paper.md), MoCo) is a *simplification* of CPC, not its direct form.
> 3. **CPC is action-free but explicitly temporal.** The `z_t → c_t → predict z_{t+k}` structure is [LeWM](../entities/leworldmodel.md)'s structure minus the action conditioning. See [world model](../concepts/world-models/world-model.md)'s periodization: this sits right on the 2012– boundary of the third era.

The **auxiliary-loss** result is the one closest to this wiki's robotics work: CPC bolted onto an existing A2C agent with *"minimal overhead"* — only linear prediction heads added — improved 4 of 5 3D navigation tasks. That is structurally the same play as [FLARE](../concepts/world-models/flare.md) adding a latent-prediction auxiliary loss to a VLA policy, eight years earlier.

## Entities mentioned

- [DeepMind](../entities/google-deepmind.md) — all three authors (van den Oord, Li, Vinyals).

## Concepts touched

- [Contrastive learning and InfoNCE](../concepts/learning/contrastive-learning.md) — where the corrected lineage lives.
- [JEPA](../concepts/world-models/jepa.md) — the latent-prediction architecture CPC prefigures.
- [Spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) — where contrastive methods land as *global* spectral embeddings.
- [World model](../concepts/world-models/world-model.md) · [latent space](../concepts/world-models/latent-space.md).

## Open questions

- ~~**Is the MI bound the right story?**~~ **Partly answered 2026-09-03** by the [Cookbook](ssl-cookbook.md) §2.6.1, which cites Tschannen et al. 2020 for the finding that *"the performance of InfoNCE cannot be explained only in terms of mutual information"* — the feature extractor and the choice of MI estimator matter more. Competing accounts it names: InfoNCE as balancing **alignment and uniformity** (Wang & Isola), as an **HSIC** bound, and as **nonlinear ICA**-style latent identification under strong assumptions. Also: contrastive learning with a **deep linear** network is equivalent to **PCA** (Tian 2022). None of those primaries is ingested; the critique now rests on a survey's summary rather than on nothing.
- **Nobody re-ran CPC's multi-step ablation in the modern setting.** Table 2's finding — 12 steps ≫ 2 steps — is the ancestor of [LeWM](../entities/leworldmodel.md)'s multi-horizon prediction term and of the rollout-penalty in the [Booth tutorial code](wm-booth-lejepa-lewm-tutorial-repo.md). Whether the optimum is a property of the objective or of the domain is untested here.
- **The negative-sampling ablation is under-appreciated.** Table 2 shows same-speaker negatives (65.5) beating mixed-speaker (64.6) — i.e. *harder negatives helped*, on a 1-point margin, in 2018. The hard-negative-mining literature that followed is not represented in this wiki.
