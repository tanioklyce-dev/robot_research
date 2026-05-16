---
title: Curriculum Module 4 — Self-supervised learning and embeddings
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-4, ssl, self-supervised-learning, embeddings, representation-collapse, vicreg, byol, dino, mae, simclr, moco, contrastive-learning, sigreg]
prereqs: [curriculum-01, curriculum-02, curriculum-03]
status: draft
---

> [!note] Curriculum context
> This is **Module 4** of the [Robot-learning curriculum](robot-learning-curriculum.md). Tier 1 — final module. Prerequisites: [Module 1](curriculum-01-neural-networks.md) (NN basics), [Module 2](curriculum-02-cnns.md) (CNN as a visual encoder), [Module 3](curriculum-03-attention-and-transformers.md) (ViT — modern SSL uses ViT encoders).
>
> Module 4 is the module that turns [LeWM](../../entities/leworldmodel.md)'s abstract from word-soup into a sensible engineering claim. **Without this module, "single SIGReg regularizer vs 4–6 anti-collapse hyperparameters" doesn't mean anything.** With it, you have the full taxonomy of anti-collapse mechanisms ready to read [Module 11 §"collapse-prevention zoo"](curriculum-11-jepa-deep.md).
>
> Acronyms used here are also in the [Glossary](../../glossary.md). First-mention links go there.

## Prereq diagnostic

Can you answer these without notes?

1. What's the difference between supervised learning, self-supervised learning, and unsupervised learning?
2. Name three pretext tasks for image SSL and explain what each one learns.
3. What's representation collapse? Why is it a first-order failure mode for non-contrastive SSL specifically?
4. Walk through how [VICReg](../../glossary.md#vicreg) prevents collapse using variance + covariance penalties.
5. What's the connection between SSL and JEPA?

If yes to all five, skim and do the anchor exercise. If no to any, read the relevant section.

## What this module is

The SSL landscape circa 2024–2026 — contrastive vs predictive methods, the central problem of representation collapse, and the family of anti-collapse mechanisms that [Module 11](curriculum-11-jepa-deep.md) zooms into. By the end you should be able to:

1. Define SSL precisely and distinguish it from supervised + unsupervised learning.
2. Place each major SSL method ([SimCLR](../../glossary.md#simclr), [MoCo](../../glossary.md#moco), [BYOL](../../glossary.md#byol), [DINO](../../glossary.md#dino), [MAE](../../glossary.md#mae), VICReg, Barlow Twins, [SIGReg](../../glossary.md#sigreg)) on the contrastive-vs-predictive axis.
3. Articulate representation collapse mathematically: why it's an attractor for unconstrained predictive SSL, and which mechanisms prevent it.
4. Walk through VICReg's three loss terms and predict what failure modes each prevents.
5. Read any new SSL paper's "method" section and identify which anti-collapse strategy it uses.
6. Place [LeWM](../../entities/leworldmodel.md)'s SIGReg as one specific point in this design space.

## §1 — What SSL is

**Self-supervised learning (SSL)** is supervised learning where the labels are *generated from the input itself* — by augmenting, masking, perturbing, or otherwise transforming the input to create a self-defined prediction task.

The point: SSL gets supervised-learning's training signal *without needing human labels*. This makes it the right move when:

- You have lots of unlabeled data (videos, web images, robot teleop recordings) and few labels.
- The downstream task (whatever it is) benefits from generic visual / sequence features.
- You want a foundation encoder you can then fine-tune or use frozen for many downstream tasks.

### SSL vs unsupervised vs supervised

| Paradigm | Labels | Training signal |
| --- | --- | --- |
| **Supervised** | human-provided `(x, y)` | match prediction to `y` |
| **Unsupervised** | none | density estimation, clustering, dimensionality reduction |
| **Self-supervised** | auto-generated from `x` | match prediction to an auto-defined target |

Older terminology lumped SSL into unsupervised. Modern usage distinguishes them: SSL is *labeled* training where the labels come from a pretext task derived from `x` itself.

### Pretext tasks

A pretext task is a fake supervised task whose labels come from the input. Examples:

- **Predict the next pixel** — autoregressive image generation (PixelCNN, GPT-image).
- **Reconstruct masked patches** — MAE (Masked Autoencoder).
- **Match two augmented views of the same image** — SimCLR, MoCo, BYOL, DINO.
- **Predict the next embedding** — JEPA. (Module 11.)
- **Predict the relative pose of two crops** — Doersch et al. 2015 (early CV SSL).

The pretext task is a means, not an end. The encoder learned by solving the pretext task is what you actually use downstream. **The pretext task should be hard enough that solving it requires learning useful features.**

## §2 — Contrastive vs predictive SSL — the two families

The dominant axis in 2024–2026 SSL.

### Contrastive SSL

**Idea.** Define positive pairs (different augmentations of the same image) and negative pairs (different images). Train the encoder so positive pairs are *close* in embedding space and negative pairs are *far*.

**Loss family:** InfoNCE (a.k.a. NT-Xent for "normalized temperature-scaled cross-entropy"):

```
L_NCE = - (1/N) · Σ_i  log  exp(s(z_i, z_i^+) / τ)
                              ─────────────────────────────
                              Σ_j  exp(s(z_i, z_j) / τ)
```

where `z_i^+` is a positive sample for `z_i`, the sum in the denominator includes negatives, `s` is a similarity function (cosine), and `τ` is a temperature.

**Examples:**
- **[SimCLR](../../glossary.md#simclr)** (Chen et al. 2020) — minibatch contrastive learning with strong data augmentations and a projection head. Needs **large batches** (typically 4K+) for enough negatives.
- **[MoCo](../../glossary.md#moco)** (He et al. 2020) — maintains a *queue* of negatives from previous batches + a momentum encoder. Decouples batch size from negative count. Works at smaller batch sizes.

**Cons:** sensitivity to negative sampling; usually needs careful augmentation tuning.

### Predictive (non-contrastive) SSL

**Idea.** Predict one view from another without explicit negatives. The encoder learns to align positive views; some anti-collapse mechanism prevents trivial solutions.

**Examples:**
- **[BYOL](../../glossary.md#byol)** (Grill et al. 2020) — predict the *target encoder*'s embedding from the *online encoder*'s embedding. Target encoder is an EMA copy of the online encoder. **No negatives.** A landmark result: showed that contrastive learning's negatives aren't strictly necessary.
- **[DINO](../../glossary.md#dino)** (Caron et al. 2021) — self-distillation with EMA target + cross-entropy loss between student and (centered, sharpened) teacher distributions. The DINOv2 successor is the dominant frozen-feature encoder in 2024–2026 robotics ([DINO-WM](../../entities/dino-wm.md), [JEPA-WMs](../../entities/jepa-wms.md)).
- **[MAE](../../glossary.md#mae)** (He et al. 2021) — mask 75% of image patches; ViT reconstructs the missing patches. Pixel-space prediction. The "predict missing patches" pretext task at scale.
- **[JEPA](../../concepts/world-models/jepa.md)** — predict the next-state *embedding*, not pixels. Module 11's family.

**Cons:** **collapse is a first-order failure mode** — the network can degenerate to a constant. The whole game becomes preventing collapse.

## §3 — The latent space as object

Both contrastive and predictive SSL produce an **embedding space** — a learned vector space where positions encode meaningful structure. The embedding is the artifact.

### Why the embedding is the right object

A trained classifier head is task-specific; the encoder learns general features. **The encoder transfers; the head doesn't.** Once you have a good encoder, you can:

- **Linear probe** — freeze the encoder, train a small linear classifier on top. Tests feature quality.
- **Frozen encoder + downstream MLP** — use the encoder's features as inputs to a more complex downstream model. [DINO-WM](../../entities/dino-wm.md)'s frozen-feature approach.
- **Fine-tune** — start from pretrained weights and tune the encoder for the specific task. Module 2's standard recipe.
- **Use for retrieval / similarity** — embedding distance proxies for semantic similarity.

### Linear-probe evaluation

The standard SSL benchmark. Freeze the encoder; train a linear layer on top with supervised labels (e.g., ImageNet-1k); measure top-1 accuracy. **Higher accuracy → better features.** [LeJEPA](../../sources/lejepa-paper.md)'s 79% on ViT-H/14 with linear probe is the headline empirical result of the SIGReg / LeJEPA recipe.

This evaluation is preferred over fine-tuning because it isolates feature quality from downstream-model capacity.

## §4 — Representation collapse — the central failure

The most important failure mode in non-contrastive SSL.

### What collapse looks like

The encoder degenerates to a near-constant function: `g_φ(x) ≈ c` for all `x`. Then:

- The prediction loss (e.g., `‖predictor(z_t, a_t) − z_{t+1}‖²`) becomes trivially 0, because both sides are the constant `c`.
- The model achieves "great training loss" but has learned nothing useful — the embedding has no information.
- Linear probe accuracy is near-random.

**Why this is a *first-order* failure.** In contrastive SSL, collapse is prevented by negatives: if all embeddings collapsed to a constant, positive-negative similarity scores would all be equal, and the InfoNCE loss would be high. So collapse and good loss are incompatible. In predictive SSL, there are no negatives — collapse and zero loss are compatible.

### Why collapse is an attractor

For predictive SSL with a flexible enough encoder, *the constant solution is reachable*. The loss landscape has trivial-collapse as a low-loss region; gradient descent finds it unless something stops you.

**This is the entire engineering problem in non-contrastive SSL.** Every method in §5 below is a different answer to "how do you prevent collapse?"

### Beyond constant collapse: dimensional collapse

A subtler failure: the encoder doesn't collapse to a constant, but it collapses to a *low-dimensional subspace*. Embeddings span only a few dimensions even though `d_model = 256`. Information is lost but not zeroed.

Module 11's terminology distinguishes:
- **Complete collapse**: `g_φ(x) ≈ c` for all `x`.
- **Dimensional collapse**: `g_φ(x)` spans a `k`-dimensional subspace with `k ≪ d_model`.

Both are bad. Both must be prevented.

## §5 — The collapse-prevention zoo

The collection of mechanisms used by different SSL methods. **Module 11's central content; Module 4 introduces the families.**

### Family 1: EMA target + stop-gradient (BYOL-line)

Maintain a **target encoder** `g̃_φ` whose weights are an exponential moving average (EMA) of the main encoder `g_φ`:

```
g̃_φ.weights  ←  τ · g̃_φ.weights  +  (1 - τ) · g_φ.weights         (typically τ = 0.99)
```

At training time:
- The **online** encoder `g_φ` produces a prediction.
- The **target** encoder `g̃_φ` produces the prediction target. **Stop gradient through `g̃_φ`** — its weights are not updated by backprop, only by the EMA update.

The asymmetry between online and target prevents collapse: the main encoder can't trivially match the target by setting both to a constant, because the target encoder lags. Empirically: BYOL, DINO, V-JEPA-line all use this trick.

**Hyperparameter:** the EMA decay `τ`. Typical 0.99–0.9999.

### Family 2: Variance + covariance regularization (VICReg-line)

Add explicit loss terms that *prevent* trivial solutions:

- **Variance term** — penalize embeddings with low variance across the batch. Forces the encoder to produce diverse embeddings.
- **Covariance term** — penalize off-diagonal entries of the embedding covariance matrix. Forces feature dimensions to be decorrelated (rules out dimensional collapse).
- **Invariance term** — the prediction loss itself (the standard SSL objective).

[VICReg](../../glossary.md#vicreg) (Bardes, Ponce, LeCun 2022):

```
L = λ_inv · L_invariance  +  λ_var · L_variance  +  λ_cov · L_covariance
```

Three hyperparameters. **Hard to collapse to a constant** — the variance term explicitly punishes low variance. **Hard to suffer dimensional collapse** — the covariance term punishes correlations.

[Barlow Twins](../../glossary.md#barlow-twins) is a variant: enforce the cross-correlation matrix between two augmented views' embeddings to be the identity. Similar effect, different formulation.

### Family 3: Frozen pretrained encoder (DINO-WM-line)

Don't train the encoder at all. **Load a strong pretrained encoder ([DINOv2](../../entities/dinov2.md) is the canonical choice) and freeze it.** Train only the downstream model.

The encoder *can't* collapse because it's not being trained. No hyperparameters. Simplest possible solution.

**Cost:** stuck with the pretrained encoder's representational choices. If DINOv2 wasn't trained on your task distribution, its features may not be optimal. [LeWM vs DINO-WM](curriculum-12-lewm-deep-dive.md) is exactly this trade-off.

### Family 4: Multi-fix soup (PLDM-line)

Combine several mechanisms — variance/covariance regularization + similarity loss + inverse-dynamics auxiliary + maybe EMA — and tune their relative weights. [PLDM](../../sources/pldm-paper.md) is the canonical example.

**4–6 anti-collapse hyperparameters per design.** Layered defense, but tuning hell. This is what [LeWM](../../entities/leworldmodel.md) explicitly responds to.

### Family 5: Distribution-matching (SIGReg / LeJEPA-line)

The newest entry. [LeJEPA (Balestriero & LeCun 2025)](../../sources/lejepa-paper.md) proves that an **isotropic Gaussian** is the optimal distribution for SSL embeddings (minimizes downstream prediction risk), and proposes **SIGReg** as a single regularizer that enforces this distribution.

```
SIGReg(Z) = (1/M) · Σ_m  T( a_m^T f_θ(x_n) )
```

where `T` is the [Epps-Pulley](https://en.wikipedia.org/wiki/Goodness_of_fit) univariate normality test statistic, `a_m` are random unit-norm directions on the hypersphere, justified by the hyperspherical Cramér-Wold theorem. **One hyperparameter** (the SIGReg loss weight); provable anti-collapse guarantee.

[Module 11 §"collapse-prevention zoo"](curriculum-11-jepa-deep.md) walks through this in detail. [Module 12 §2](curriculum-12-lewm-deep-dive.md) does the full math. For now: **SIGReg is the newest anti-collapse mechanism, and it's the one [LeWM](../../entities/leworldmodel.md) uses.**

### Side-by-side summary

| Family | Mechanism | Hyperparameters | Examples |
| --- | --- | --- | --- |
| EMA + stop-grad | slow-updating teacher | 1 (τ) | BYOL, DINO, V-JEPA |
| Variance + covariance | explicit non-degeneracy penalty | 3 (λ_inv, λ_var, λ_cov) | VICReg, Barlow Twins |
| Frozen encoder | no encoder training | 0 | DINO-WM, JEPA-WMs |
| Multi-fix soup | layered combination | 4–6 | PLDM |
| Distribution-matching | match isotropic Gaussian | 1 (λ) | LeJEPA, LeWM |

## §6 — Where this lands for the curriculum

The SSL design space is the **superset** of what [Module 11](curriculum-11-jepa-deep.md) zooms into. Module 11 covers families 1, 2, 3, 4, 5 specifically in the JEPA / world-model context. Module 4 introduces the same families at the SSL-in-general level, so Module 11's specific framing makes sense.

**Why this matters for LeWM.** LeWM's contribution (per [Module 12](curriculum-12-lewm-deep-dive.md)) is methodological: simplest possible end-to-end JEPA with a single anti-collapse mechanism. This claim only parses if you understand the alternatives — and the alternatives are this module's collapse-prevention families.

**Why this matters for everything else.**

- [Module 5](curriculum-05-generative-models.md) DDPM is not SSL in the strict sense (it's generative), but score-matching shares mathematical structure with SSL.
- [Module 11](curriculum-11-jepa-deep.md) JEPA is the SSL family Module 4 most directly enables.
- [Module 12](curriculum-12-lewm-deep-dive.md) LeWM is one specific point in the design space.
- Frozen pretrained encoders (Family 3) appear throughout the wiki — [Module 2](curriculum-02-cnns.md) covered the workflow at the CNN level; here we cover the SSL pretraining side.

## §7 — A taxonomy you should be able to draw

A mental picture: SSL methods are points in a 2D space.

```
       contrastive  ←─────────────────────→  predictive
                              │
                              │
       large batches  ─────────────────────  small batches (with EMA / queues)
                              │
                              │
       moment / cov-based  ←─────→  distribution-matching  (SIGReg)
                              │
                              │
       end-to-end encoder  ────────────────  frozen encoder  (DINO-WM)
```

Most methods are characterized by their position on these axes:

- **SimCLR**: contrastive, large batches, no anti-collapse needed (negatives handle it).
- **MoCo**: contrastive, small batches (with queue), no anti-collapse needed.
- **BYOL / DINO**: predictive, end-to-end, EMA + stop-grad.
- **VICReg / Barlow Twins**: predictive, end-to-end, variance/covariance regularization.
- **MAE**: predictive (pixel-reconstruction), end-to-end, no collapse problem (pixels are fixed targets).
- **PLDM**: predictive, end-to-end, multi-fix soup.
- **LeJEPA / LeWM**: predictive, end-to-end, distribution-matching.
- **DINO-WM / JEPA-WMs**: predictive, frozen DINOv2 encoder, no anti-collapse needed.

## Anchor exercise

> **Reproduce VICReg on CIFAR with and without the regularizer. Observe collapse to constant.**

Concrete:

1. **Setup.** CIFAR-10 (60k 32×32 RGB images). Pretrain an SSL model on the training set (ignore labels); evaluate on the test set via linear probe.
2. **Model.** ResNet-18 encoder (Module 2) producing 512-dim features. Apply two random augmentations (crop, color jitter, horizontal flip) to each image to get two views; encode both.
3. **Loss A — VICReg.** Apply the three loss terms (variance, covariance, invariance) with paper-default weights (λ_inv = 25, λ_var = 25, λ_cov = 1). Train ~10 epochs.
4. **Loss B — invariance only.** Drop the variance and covariance terms. Just minimize the similarity between the two views' embeddings. Train the same way.
5. **Linear probe.** Freeze each encoder; train a linear classifier on top with the actual CIFAR-10 labels. Compare test accuracy.
6. **Inspect embeddings.** For each model, look at the *variance* of each embedding dimension across the test set. For VICReg, all 512 dimensions should have similar variance. For invariance-only, **most dimensions should have collapsed to near-zero variance** (or even to a constant); the embedding has effectively zero rank.

The point: feel that **without explicit anti-collapse, the encoder collapses**. Linear probe accuracy on the invariance-only model should be near-random. The variance-covariance penalty is what makes VICReg work.

Deeper variant: try VICReg with just the variance term (no covariance). Some dimensions will have high variance but they'll all be highly correlated — dimensional collapse without complete collapse. This isolates which term handles which failure mode.

## Recommended reading

In order:

1. **Lilian Weng — [Self-Supervised Representation Learning](https://lilianweng.github.io/posts/2019-11-10-self-supervised/)** — the canonical online survey. Covers contrastive and predictive families with pseudocode.
2. **Grill et al. 2020 — BYOL paper** (arxiv 2006.07733) — the landmark "no negatives needed" result. Read §3 (method).
3. **Bardes, Ponce, LeCun 2022 — VICReg paper** (arxiv 2105.04906) — the variance-covariance recipe. Read §3 (method).
4. **He et al. 2021 — MAE paper** (arxiv 2111.06377) — the masked-autoencoder pretext task. Read §3 (method).
5. **Caron et al. 2021 — DINO paper** (arxiv 2104.14294) — self-distillation. Read §3.
6. **[LeJEPA Paper](../../sources/lejepa-paper.md) (Balestriero & LeCun 2025)** — the SIGReg foundation. Already in the wiki. Read §3 (Why Gaussian?) and §4 (SIGReg).

## What you should now be able to do

- Read any SSL paper and place it on the contrastive-vs-predictive axis and identify which anti-collapse family it uses.
- Predict the failure modes of a hypothetical SSL method given its loss formulation.
- Recognize the JEPA framing as a specific instance of predictive SSL where the prediction target is a *future* embedding (in time).
- Write the VICReg loss formulation from memory.
- Distinguish complete collapse from dimensional collapse.
- Articulate the difference between BYOL's EMA + stop-grad trick and VICReg's explicit variance/covariance penalties.

## Hand-off

Module 4 is the prerequisite for:

- **[Module 11](curriculum-11-jepa-deep.md) — JEPA in depth** — the family of "predictive SSL in time" specifically. The collapse-prevention zoo there is a refinement of this module's families 1–5.
- **[Module 12](curriculum-12-lewm-deep-dive.md) — LeWM deep-dive** — derives SIGReg in detail; Module 4's family-5 setup is what makes Module 12's math motivated rather than abstract.

It also touches:

- **[Module 7](curriculum-07-bc-lineage-pusht.md) — BC lineage** — some BC methods use SSL-pretrained encoders ([R3M](../../glossary.md#r3m), DINOv2).
- **[Module 9](curriculum-09-vla.md) — VLA** — VLA backbones are typically pretrained via SSL (CLIP, DINOv2, V-JEPA).

## Related curriculum modules

- **[Module 1](curriculum-01-neural-networks.md), [Module 2](curriculum-02-cnns.md), [Module 3](curriculum-03-attention-and-transformers.md)** — prerequisites.
- **[Module 5](curriculum-05-generative-models.md)** — sibling (generative modeling; score matching connects to predictive SSL).
- **[Module 11](curriculum-11-jepa-deep.md), [Module 12](curriculum-12-lewm-deep-dive.md)** — direct successors.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../../index.md)

## Open questions / TBD

- **BYOL, VICReg, SimCLR, MoCo, DINO source pages** — none of these have wiki source pages yet. Module 4 leans on the secondary surveys. Could be filed if curriculum-internal pointers become heavy.
- **MAE source page** (He et al. 2021) — pixel-reconstruction SSL; appears in some V-JEPA-line comparisons.
- **A "common SSL failure modes" page** — collapse (complete + dimensional) + augmentation overfitting + linear-probe vs k-NN-probe gaps — would help downstream module readers.
- **DINOv2 source page** — the encoder behind [DINO-WM](../../entities/dino-wm.md), [JEPA-WMs](../../entities/jepa-wms.md), and others; foundational and not yet ingested.
