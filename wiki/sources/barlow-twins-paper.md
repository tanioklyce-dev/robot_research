---
title: "Barlow Twins — Self-Supervised Learning via Redundancy Reduction (Zbontar, Jing, Misra, LeCun, Deny, 2021)"
type: source
url: https://arxiv.org/abs/2103.03230
local_path: raw/2103.03230v3.pdf
author: Jure Zbontar, Li Jing, Ishan Misra, Yann LeCun, Stéphane Deny
affiliation: Facebook AI Research (+ NYU for LeCun)
published: 2021-03-04 (v1); 2021-06-14 (v3); ICML 2021 (PMLR 139)
ingested: 2026-05-12
created: 2026-05-12
updated: 2026-05-12
tags: [barlow-twins, ssl, redundancy-reduction, anti-collapse, cross-correlation, lecun, zbontar, jing, misra, deny, information-bottleneck, foundational]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/2103.03230v3.pdf`, 13 pages — main paper + appendix outline). Sections 1 (intro), 2 (method, loss formula), 3 (ImageNet linear + transfer results), 4 (ablations), and 5 (discussion / comparison with infoNCE and BYOL / SimSiam) read in full. Appendix A (Information-Bottleneck derivation) referenced but not unpacked.

## Summary

**Barlow Twins** — Zbontar, Jing, Misra, LeCun, Deny (FAIR + NYU; ICML 2021, arxiv 2103.03230). A **non-contrastive, non-asymmetric** SSL method whose loss makes the **cross-correlation matrix between the embeddings of two augmented views as close to the identity as possible**.

Two terms in the loss:

1. **Invariance term** — push diagonal entries `C_ii` toward 1 (the two views of the same image should produce correlated representations on every component).
2. **Redundancy-reduction term** — push off-diagonal entries `C_ij` (i≠j) toward 0 (different components should encode different information).

**Why it matters.** Barlow Twins is the **first SSL method to prevent representation collapse without asymmetry**:

- No momentum encoder (vs. MoCo).
- No predictor network (vs. BYOL).
- No stop-gradient (vs. SimSiam).
- No large negative-sample batches (vs. SimCLR / InfoNCE).
- Works with batches as small as 256.
- **Benefits from very high-dimensional embeddings** (D=8192 in the paper) — the opposite of contrastive methods, which suffer in high dimensions.

The method is named after neuroscientist **Horace Barlow**, whose [1961 "Possible Principles Underlying the Transformation of Sensory Messages"](barlow1961-sensory-messages.md) introduced the **redundancy-reduction principle** for sensory coding. Barlow Twins applies the same principle to a Siamese-network pair — hence "Twins."

**Headline result:** ImageNet top-1 linear-probe accuracy **73.2%** with ResNet-50 (state-of-the-art among non-asymmetric methods at the time; on par with SimCLR-class, slightly below BYOL/SwAV).

## Abstract (verbatim)

> "Self-supervised learning (SSL) is rapidly closing the gap with supervised methods on large computer vision benchmarks. A successful approach to SSL is to learn embeddings which are invariant to distortions of the input sample. However, a recurring issue with this approach is the existence of trivial constant solutions. Most current methods avoid such solutions by careful implementation details. We propose an objective function that naturally avoids collapse by measuring the cross-correlation matrix between the outputs of two identical networks fed with distorted versions of a sample, and making it as close to the identity matrix as possible. This causes the embedding vectors of distorted versions of a sample to be similar, while minimizing the redundancy between the components of these vectors. The method is called BARLOW TWINS, owing to neuroscientist H. Barlow's redundancy-reduction principle applied to a pair of identical networks. BARLOW TWINS does not require large batches nor asymmetry between the network twins such as a predictor network, gradient stopping, or a moving average on the weight updates. Intriguingly it benefits from very high-dimensional output vectors."

## The loss function (the core)

Let `Z^A, Z^B ∈ ℝ^{N×D}` be the batches of embeddings from two augmented views, **mean-centered along the batch dimension**. The cross-correlation matrix:

```
C_ij = Σ_b z^A_{b,i} · z^B_{b,j}  /  ( ||z^A_{·,i}||_2 · ||z^B_{·,j}||_2 )
```

(`i, j` index embedding dimensions; `b` indexes batch.) `C` is a `D × D` matrix with entries in [-1, 1].

The Barlow Twins loss:

```
L_BT = Σ_i (1 - C_ii)²    +    λ · Σ_i Σ_{j≠i} C_ij²
       ─────────────────         ────────────────────────
       invariance term            redundancy-reduction term
```

Best hyperparameter: `λ = 5·10⁻³`.

### Information-theoretic interpretation (Appendix A)

The paper derives Barlow Twins as an **instantiation of the Information Bottleneck (IB) principle** under a Gaussian assumption on the embedding distribution. Reading: Barlow Twins is the SSL specialization of "preserve maximum information about `x` while being least informative about the distortions applied." The `λ` parameter is the IB trade-off parameter. This is what gives the method its theoretical grounding beyond "the trick happens to work."

### PyTorch-style pseudocode (Algorithm 1)

```python
for x in loader:
    y_a, y_b = augment(x)             # two augmented views
    z_a, z_b = f(y_a), f(y_b)         # N x D embeddings
    z_a = (z_a - z_a.mean(0)) / z_a.std(0)
    z_b = (z_b - z_b.mean(0)) / z_b.std(0)
    c = (z_a.T @ z_b) / N             # D x D cross-correlation
    c_diff = (c - eye(D)).pow(2)
    off_diagonal(c_diff).mul_(lambda)
    loss = c_diff.sum()
    loss.backward(); optimizer.step()
```

About 20 lines. The simplicity is the point.

## Implementation details (Section 2.2)

- **Encoder**: ResNet-50, 2048-dim output (no final classifier).
- **Projector**: 3 linear layers, each 8192-dim, BN + ReLU on the first two.
- **Embeddings** (fed to the loss) = projector output; **representations** (used downstream) = encoder output.
- **Optimization**: LARS, 1000 epochs, batch size 2048 (but 256 also works), LR 0.2 weights / 0.0048 BN+bias, cosine decay, 10-epoch warm-up.
- **Augmentations**: same as BYOL — random crop, resize 224×224, horizontal flip, color jitter, grayscale, Gaussian blur, solarization.
- **Compute**: 124 hours on 32 V100 GPUs. (BYOL takes 113 hours on the same hardware at batch 4096 — Barlow Twins is comparable but with smaller batches.)

## Headline results (ImageNet linear eval, ResNet-50)

| Method | Top-1 | Top-5 |
|---|---|---|
| Supervised | 76.5 | — |
| MoCo | 60.6 | — |
| SimCLR | 69.3 | 89.0 |
| MoCo v2 | 71.1 | 90.1 |
| SimSiam | 71.3 | — |
| SwAV (w/o multi-crop) | 71.8 | — |
| BYOL | 74.3 | 91.6 |
| SwAV (w/ multi-crop) | 75.3 | — |
| **Barlow Twins** | **73.2** | **91.0** |

In semi-supervised 1% Top-1, Barlow Twins reached 55.0%, slightly better than BYOL (53.2) and SimCLR (48.3).

## Comparison with prior art (Section 5.1)

### vs. InfoNCE / SimCLR
- Both have an invariance term + a "spread" term.
- **InfoNCE spreads by repelling samples** (contrastive); **Barlow Twins spreads by decorrelating dimensions** (information-content maximization).
- InfoNCE's spread term is non-parametric entropy estimation → suffers curse of dimensionality → needs many negatives, large batches, low-D embeddings.
- Barlow Twins' spread term is a Gaussian-parametric proxy → handles high-D embeddings → works with small batches.
- Barlow Twins normalizes along the **batch** dimension; InfoNCE normalizes along the **feature** dimension. This is a deep structural difference between contrastive and information-maximization methods.

### vs. BYOL / SimSiam
- BYOL and SimSiam use **only a cosine similarity** between twin embeddings.
- They avoid collapse via **architectural asymmetry** (predictor network in BYOL, stop-gradient in SimSiam, EMA target encoder in BYOL).
- "The dynamics of learning in these methods, and how they avoid collapse, is not fully understood." This is the key motivation for Barlow Twins: an SSL method whose anti-collapse mechanism is **explicit and analytically grounded**, not an empirical observation about asymmetry.

### vs. Whitening-MSE (Ermolov 2020)
- Both decorrelate embedding dimensions to prevent collapse.
- W-MSE does **hard whitening** (zero off-diagonals exactly).
- Barlow Twins does **soft whitening** (push off-diagonals toward zero via `λ` trade-off).
- Barlow Twins outperforms W-MSE.

## Robustness properties (ablations)

The paper reports two non-obvious empirical findings:

1. **Robust to small batches.** Barlow Twins works at batch=256 with ~1% top-1 drop. SimCLR's performance falls off a cliff at small batches.
2. **Benefits from large embedding dimension.** Going from D=1024 → D=8192 → D=16384 *continues to improve* Barlow Twins. InfoNCE-based methods plateau or degrade at high D. This is the strongest empirical signal that the method is doing something structurally different from contrastive learning.

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md) — senior author. Marks Barlow Twins as the FAIR-internal precursor to [VICReg](vicreg-paper.md) (with Bardes a year later) and to the regularized-SSL strand of LeCun's broader [Path-Towards-AMI](lecun2022-path-towards-ami.md) vision.
- [Meta FAIR](../entities/meta-fair.md) (then "Facebook AI Research") — primary affiliation.
- **Horace Barlow** — the eponymous neuroscientist. His [1961 paper](barlow1961-sensory-messages.md) introduced the redundancy-reduction principle that Barlow Twins applies to neural networks.
- Stéphane Deny, Jure Zbontar, Li Jing, Ishan Misra — co-authors not yet tracked as separate entities; worth filing if they recur.

## Concepts touched
- [Siamese network](../concepts/world-models/siamese-network.md)

- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — Barlow Twins is one of the canonical Joint-Embedding *non-predictive* architectures (no predictor on top of the embedding). It informs the encoder-side design of JEPA but does not itself predict a future.
- **Representation collapse** — the central problem Barlow Twins solves; its anti-collapse mechanism is one of the "regularized methods" that LeCun (2022) explicitly endorses over contrastive methods.
- **Redundancy reduction** — Horace Barlow's principle, formalized here as the cross-correlation-identity loss.
- **Information Bottleneck** — the framework the loss derives from; ties Barlow Twins to a broader information-theoretic foundation for SSL.

## Position in the lineage

Barlow Twins sits in the SSL anti-collapse lineage that anchors most of the wiki's JEPA / world-model coverage:

```
Barlow 1961 (neuroscience)
   ↓ (decorrelate → factorial code)
Barlow Twins 2021 (cross-corr → I)
   ↓ (decompose into variance + covariance + invariance)
VICReg 2021/2022 (explicit hinge variance + covariance + L2 invariance)
   ↓ (used as JEPA regularizer in LeCun's 2022 vision)
LeCun 2022 — Path Towards AMI (endorses VICReg-class regularized methods for JEPA)
   ↓ (instantiated end-to-end at small scale)
PLDM 2025 (VICReg + inverse-dynamics + similarity, ~6 hyperparameters)
   ↓ (replaced by SIGReg's single regularizer with proofs)
LeJEPA 2025 (SIGReg — Sketched Isotropic Gaussian Regularization)
   ↓ (applied to world modeling)
LeWM 2026 (first stable end-to-end JEPA WM)
```

In parallel: the DINO branch (DINO 2021 → DINOv2 2023 → DINOv3 2025 with Gram anchoring) uses different anti-collapse machinery (EMA teacher + stop-gradient + Koleo regularization), but solves the same problem. The two branches converge on "regularized SSL is the path forward; contrastive methods don't scale well to high-D embeddings."

## Open questions / TBD

- Stéphane Deny's affiliation and current work — co-corresponding on Barlow Twins, not on later LeCun-line papers. Has he stayed in the SSL space?
- The Information-Bottleneck derivation in Appendix A is non-trivial. A future deepening pass could unpack it; useful for understanding why the loss is theoretically grounded rather than empirically lucky.
- Direct application of Barlow Twins to **video / temporal SSL** is not reported in the paper. The natural extension (correlate embeddings across time instead of across augmentations) is one possible bridge from Barlow Twins to JEPA — worth checking the literature.
