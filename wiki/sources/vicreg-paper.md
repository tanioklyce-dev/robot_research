---
title: "VICReg — Variance-Invariance-Covariance Regularization for Self-Supervised Learning (Bardes, Ponce, LeCun, ICLR 2022)"
type: source
url: https://arxiv.org/abs/2105.04906
local_path: raw/2105.04906v3.pdf
author: Adrien Bardes, Jean Ponce, Yann LeCun
affiliation: Facebook AI Research (Bardes, LeCun); Inria / École normale supérieure / NYU
published: 2021-05-11 (v1); 2022-01-28 (v3); ICLR 2022
ingested: 2026-05-12
created: 2026-05-12
updated: 2026-05-12
tags: [vicreg, ssl, variance, covariance, invariance, anti-collapse, bardes, lecun, ponce, joint-embedding, foundational]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/2105.04906v3.pdf`, 23 pages — main paper + appendices). Sections 1 (intro), 2 (intuition), 3 (related work), 4 (method — full loss derivation), 5 (results: ImageNet linear / semi-sup / transfer), 6 (analysis / multi-modal extension), 7 (conclusion) read in full. Appendices on optimization, expander-dim ablations, multi-modal pretraining skimmed.

## Summary

**VICReg** — Bardes, Ponce, LeCun (FAIR + Inria + NYU; ICLR 2022, arxiv 2105.04906). The **canonical regularized-SSL method** in the lineage that LeCun endorses in [A Path Towards Autonomous Machine Intelligence (2022)](lecun2022-path-towards-ami.md) as the JEPA-compatible anti-collapse mechanism. Three loss terms, applied **independently to the two branches** of a joint-embedding architecture:

1. **Variance (`v`)** — hinge loss enforcing per-dimension standard deviation ≥ a threshold (γ=1). Prevents *norm collapse* (all embeddings shrinking to zero).
2. **Invariance (`s`)** — mean-squared distance between embedding pairs of the same image's two views. The "make the same image's views agree" term.
3. **Covariance (`c`)** — push pairwise covariances between embedding dimensions toward zero. Prevents *informational collapse* (different dimensions encoding the same information). Borrowed conceptually from [Barlow Twins](barlow-twins-paper.md).

Total loss: `ℓ = λ·s + µ·[v(Z) + v(Z')] + ν·[c(Z) + c(Z')]`, with `λ = µ = 25`, `ν = 1` in the paper.

**Why it matters.** VICReg makes three structural commitments that distinguish it from prior SSL:

1. **Two branches can be fully independent.** No weight sharing required, no shared architecture, no shared input modality. This is the property that makes VICReg the **natural multi-modal SSL method** — pretrain image + text, image + audio, video + audio, etc.
2. **Each branch's collapse is prevented separately.** Variance + covariance are computed per-branch. Two branches can have independent collapse risks — VICReg handles them independently.
3. **No tricks.** No batch-norm, no feature-norm, no stop-gradient, no momentum encoder, no quantization, no memory bank, no predictor. Just three explicit loss terms.

**Headline empirical result:** ImageNet linear top-1 = **73.2%** (ResNet-50). Matches Barlow Twins and is competitive with BYOL / SwAV.

**More important**: VICReg's **variance term is shown to stabilize the training of other methods** when bolted on, including BYOL — which is the first empirical evidence that asymmetric methods (BYOL/SimSiam) can be replaced by explicit variance regularization.

## Abstract (verbatim)

> "Recent self-supervised methods for image representation learning maximize the agreement between embedding vectors produced by encoders fed with different views of the same image. The main challenge is to prevent a collapse in which the encoders produce constant or non-informative vectors. We introduce VICReg (Variance-Invariance-Covariance Regularization), a method that explicitly avoids the collapse problem with two regularizations terms applied to both embeddings separately: (1) a term that maintains the variance of each embedding dimension above a threshold, (2) a term that decorrelates each pair of variables. Unlike most other approaches to the same problem, VICReg does not require techniques such as: weight sharing between the branches, batch normalization, feature-wise normalization, output quantization, stop gradient, memory banks, etc., and achieves results on par with the state of the art on several downstream tasks. In addition, we show that our variance regularization term stabilizes the training of other methods and leads to performance improvements."

## The loss function (the core)

Let `Z = [z_1, ..., z_n] ∈ ℝ^{n×d}` be a batch of embeddings (one branch). Let `z^j` be the column vector of values at dimension `j` across the batch.

### Variance regularization
A hinge loss on per-dimension standard deviation:
```
v(Z) = (1/d) · Σ_j max(0, γ - S(z^j, ε))
```
where `S(x, ε) = √(Var(x) + ε)` (regularized standard deviation), `γ = 1` (target std), `ε = 10⁻⁴`.

> [!note] Why std, not variance?
> The paper points out: if you use raw variance instead of std in the hinge, the gradient becomes near-zero when `x` is near its mean → the embeddings collapse. Using `S = √(Var + ε)` keeps the gradient well-defined throughout training. This is the kind of subtle implementation detail that turns an "obvious" anti-collapse penalty into one that actually works.

### Covariance regularization
Compute the empirical covariance matrix `C(Z)` of the batch and penalize the off-diagonal entries:
```
C(Z) = (1/(n-1)) · Σ_i (z_i - z̄)(z_i - z̄)ᵀ
c(Z) = (1/d) · Σ_{i≠j} [C(Z)]²_{i,j}
```

This is **identical in spirit to Barlow Twins' redundancy-reduction term** — push off-diagonals toward zero. Difference: Barlow Twins applies to the cross-correlation between *the two branches' embeddings*; VICReg applies to the within-branch covariance separately for each branch.

### Invariance
Plain MSE between paired embeddings:
```
s(Z, Z') = (1/n) · Σ_i ||z_i - z'_i||²
```

### Total
```
ℓ(Z, Z') = λ·s(Z, Z')  +  µ·(v(Z) + v(Z'))  +  ν·(c(Z) + c(Z'))
```

Hyperparameters in the paper: `λ = µ = 25`, `ν = 1`.

## Architecture (Section 4 + Figure 1)

- **Encoder** `f_θ`: ResNet-50 backbone, 2048-dim output (= "representations" used downstream).
- **Expander** `h_φ`: 3-layer MLP (FC + BN + ReLU + FC + BN + ReLU + FC), all layers 8192-dim. Output of expander = "embeddings", fed to the loss.
- **Expander discarded after pretraining.** Same pattern as Barlow Twins / SimCLR.
- The expander's role per the paper: (1) eliminate information by which the two augmented representations differ, (2) expand dimension so decorrelating embedding dims reduces *dependencies* (not just correlations) between representation dims.
- Branches **may** be Siamese (shared weights) — most experiments are — but **don't have to be**. This is the key VICReg-vs-Barlow-Twins distinction.

## Anti-collapse story (Section 2)

The paper is explicit about which term prevents which collapse mode:

| Collapse mode | Failure | Prevented by |
|---|---|---|
| **Norm collapse** | Embeddings shrink toward `z = 0` for all inputs. | **Variance** term (hinge on std). |
| **Informational collapse** | Different dimensions encode redundant info. | **Covariance** term (decorrelate dimensions). |
| **Trivial agreement collapse** | Both branches output a constant (anywhere). | Variance prevents this — the constant has variance 0, hinge kicks in. |

This three-way decomposition is what makes the paper a **conceptual contribution beyond Barlow Twins**: it isolates the two failure modes (norm and information) and provides a separate explicit term for each, rather than relying on a single cross-correlation-identity loss to handle both implicitly.

## Headline results (ImageNet linear eval, ResNet-50)

| Method | Top-1 | Top-5 |
|---|---|---|
| Supervised | 76.5 | — |
| SimCLR | 69.3 | 89.0 |
| MoCo v2 | 71.1 | — |
| SimSiam | 71.3 | — |
| SwAV (w/o multi-crop) | 71.8 | — |
| BYOL | 74.3 | 91.6 |
| SwAV (w/ multi-crop) | 75.3 | — |
| Barlow Twins | 73.2 | 91.0 |
| **VICReg** | **73.2** | **91.1** |

Within 0.1% of Barlow Twins; competitive with BYOL / SwAV without their architectural tricks. Semi-supervised 1% Top-1 = 54.8% (Barlow Twins 55.0, BYOL 53.2).

Transfer tasks (frozen ResNet-50 features) on Places205, VOC07, iNaturalist18, VOC07+12 detection, COCO det/seg are all within ~0.5–1.0 of the best baselines — VICReg is **on par on transfer**, not state-of-the-art-by-a-mile.

## The variance term stabilizes other methods (Section 6)

A non-obvious empirical result: **bolting VICReg's variance term onto BYOL or SimSiam stabilizes their training and slightly improves their performance**. The paper interprets this as evidence that asymmetric methods (BYOL, SimSiam) are *implicitly* doing variance regularization through their architectural asymmetry — and an explicit variance term makes that mechanism less fragile.

This is part of why VICReg becomes the reference anti-collapse method in LeCun's [2022 Path-to-AMI](lecun2022-path-towards-ami.md): the variance term is portable across SSL methods, not coupled to a specific architecture.

## Multi-modal extension (Section 6.3)

The paper briefly demonstrates VICReg on **image-text pretraining** with MS-COCO 5K retrieval. Two encoders with completely different architectures (CNN for images, transformer for text), no shared weights, no shared parameters. Outperforms VSE++ contrastive baseline on image→text and text→image retrieval.

> [!note] This is the structural property that matters more than the ImageNet linear-probe number
> Contrastive methods (SimCLR, MoCo, BYOL) all require Siamese-style architectures with shared weights. VICReg removes that constraint, opening the door to multi-modal SSL with arbitrarily different encoders. For robotics — where action / proprioception / vision all live in different modalities — this is the consequential structural choice.

## Implementation details

- LARS optimizer, 1000 epochs, batch 2048 (smaller works), `lr = 0.2 × batch/256`, cosine decay, 10 warmup epochs, weight decay 10⁻⁶.
- Augmentations: same as BYOL.
- Code: https://github.com/facebookresearch/vicreg.

## Entities mentioned

- [Adrien Bardes](../entities/adrien-bardes.md) — lead author, now co-senior on [V-JEPA 2](v-jepa-2-paper.md), [V-JEPA 2.1](v-jepa-2-1-paper.md), [JEPA-WMs](jepa-wms-paper.md). VICReg is **Bardes's PhD-thesis-area paper** and the methodological precursor to his JEPA-program work.
- [Yann LeCun](../entities/yann-lecun.md) — senior author. VICReg is the regularizer LeCun endorses by name in [Path Towards AMI (2022)](lecun2022-path-towards-ami.md) as the JEPA-compatible anti-collapse method.
- **Jean Ponce** — co-author, Inria/ENS — not yet tracked as separate entity; senior figure in French CV/ML community.
- [Meta FAIR](../entities/meta-fair.md) (then "Facebook AI Research") — primary affiliation.

## Concepts touched
- [Siamese network](../concepts/world-models/siamese-network.md)

- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — VICReg defines the joint-embedding *without* predictor; JEPA adds the predictor on top. The encoder-side anti-collapse machinery is shared.
- **Representation collapse** — VICReg's three-term decomposition is the cleanest articulation of *which* collapse mode each term prevents.
- **Information maximization SSL** — the broader family Barlow Twins and VICReg belong to (vs. contrastive / clustering / distillation / quantization SSL).

## Position in the lineage

VICReg's contribution becomes most visible in the LeJEPA → SIGReg story 4 years later:

- **VICReg (2022)**: three explicit terms (variance, covariance, invariance), ~5 hyperparameters when tuned across all of `λ`, `µ`, `ν`, `γ`, `ε`.
- **PLDM (2025)** uses VICReg + inverse-dynamics + similarity — ~6 hyperparameters across the full pipeline.
- **LeJEPA (2025)** ([Balestriero & LeCun](lejepa-paper.md)) replaces this with **one regularizer (SIGReg) and one trade-off hyperparameter `λ`**, proving that an isotropic Gaussian is the unique optimal embedding distribution.
- **DINOv3 (2025)** ([Siméoni et al.](dinov3-paper.md)) goes the other way — keeps the DINO/iBOT heuristics-heavy paradigm and adds **Gram anchoring** as a fourth term.

VICReg is the **methodological anchor** of the regularized-SSL branch that LeJEPA and SIGReg eventually consolidate. Without VICReg's three-term decomposition, the "variance + covariance + invariance" vocabulary that subsequent JEPA papers rely on wouldn't exist.

## Open questions / TBD

- Why `λ = µ = 25` and `ν = 1`? Appendix D.4 has hyperparameter-selection guidance; not unpacked here.
- The expander-dim ablation (deep dependency of VICReg on D=8192-class expander) is a known SSL phenomenon — Barlow Twins shows the same pattern. Open question whether SIGReg shares it (the [LeJEPA paper](lejepa-paper.md) trains ViT-H at high D so likely yes).
- VICReg's variance term is the precursor to **SIGReg's** Epps-Pulley-test-based moment regularization. Direct theoretical relationship: SIGReg's per-direction sketch can be read as VICReg's variance term + a Gaussianity check on top. Worth a synthesis page if the curriculum modules ever go deeper into the regularizer-equivalence question.
