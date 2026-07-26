---
title: LeJEPA Paper — Provable and Scalable Self-Supervised Learning Without the Heuristics (Balestriero & LeCun, 2025)
type: source
url: https://arxiv.org/abs/2511.08544
local_path: raw/2511.08544v3.pdf
author: Randall Balestriero, Yann LeCun
affiliation: Brown University + Meta-FAIR (Balestriero, equal contribution); New York University + Meta-FAIR (LeCun, equal contribution)
published: 2025-11-11 (v1); 2025-11-14 (v3)
ingested: 2026-05-10 (deepened from PDF)
tags: [lejepa, sigreg, jepa, ssl, anti-collapse, isotropic-gaussian, balestriero, lecun, foundational, sketched-regularization, cramer-wold, epps-pulley, characteristic-function]
---

> [!note] Ingest depth
> Deepened ingest based on the **full PDF** (`raw/2511.08544v3.pdf`, 50 pages — main paper sections 1–6 + extensive appendices). Sections 1–4 (intro, background, why-Gaussian, SIGReg) are unpacked here; sections 5 (LeJEPA = JEPA + SIGReg combined training procedure) and 6 (experiments at scale) are summarized at headline-result depth. Appendices A–F have additional theory + ablations + implementation details and are noted but not exhaustively read.

## Summary

**LeJEPA** — Balestriero & LeCun (Brown + NYU/Meta-FAIR; arxiv 2511.08544; Nov 2025). The **foundational paper for [SIGReg](../glossary.md#sigreg)** (Sketched Isotropic Gaussian Regularization). Two intertwined contributions:

1. **Theoretical:** prove that an **isotropic Gaussian** is the *unique* optimal embedding distribution for JEPA — formally, the distribution that minimizes the worst-case Integrated Square Bias (ISB) under k-NN regression and kernel regression among distributions with a scalar covariance constraint (Theorem 1).
2. **Methodological:** propose **SIGReg** — a regularizer that enforces this distribution by sketching multivariate normality testing into 1-D directional tests, justified by a *hyperspherical* Cramér-Wold theorem (Lemma 3) and a directional-test consistency theorem (Theorem 2). Use the **Epps-Pulley test statistic** for the per-direction normality test, justified rigorously: moment-based tests are unstable, CDF-based tests break gradient-based optimization, and characteristic-function-based tests (specifically Epps-Pulley) are differentiable, parallelizable, and consistent.

Combining the JEPA predictive loss with SIGReg yields **LeJEPA**: a "lean, scalable, and theoretically grounded training objective" with **a single hyperparameter** (the SIGReg loss weight `λ`), **linear time and memory complexity**, **no stop-gradient**, **no teacher-student / EMA**, **no hyperparameter schedulers**. Implementation: ~50 lines of code; distributed-training-friendly.

**Headline empirical claim:** ImageNet-1k pretraining + linear-eval on a frozen ViT-H/14 backbone reaches **79% top-1**. Validation across **10+ datasets, 60+ architectures** including ResNets, ViTs, ConvNets at scales up to **1.8B-parameter ViT-g** (which the paper specifically demonstrates trains with stable loss curves). Galaxy10 in-domain pretraining beats DINOv2/v3 transfer (frontier foundation models trained on natural images) across data regimes from 1-shot to full supervision.

LeJEPA is the **methodological precursor to [LeWM](leworldmodel-paper.md)** (Maes et al. 2026): same SIGReg, but LeWM applies it to action-conditioned world modeling for offline RL.

## Abstract (verbatim)

> "Learning manipulable representations of the world and its dynamics is central to AI. Joint-Embedding Predictive Architectures (JEPAs) offer a promising blueprint, but lack of practical guidance and theory has led to ad-hoc R&D. We present a comprehensive theory of JEPAs and instantiate it in LeJEPA, a lean, scalable, and theoretically grounded training objective. First, we identify the isotropic Gaussian as the optimal distribution that JEPAs' embeddings should follow to minimize downstream prediction risk. Second, we introduce a novel objective–Sketched Isotropic Gaussian Regularization (SIGReg)–to constrain embeddings to reach that ideal distribution. Combining the JEPA predictive loss with SIGReg yields LeJEPA with numerous theoretical and practical benefits: (i) single trade-off hyperparameter, (ii) linear time and memory complexity, (iii) stability across hyper-parameters, architectures (ResNets, ViTs, ConvNets) and domains, (iv) heuristics-free, e.g., no stop-gradient, no teacher–student, no hyper-parameter schedulers, and (v) distributed training-friendly implementation requiring only ≈50 lines of code. Our empirical validation covers 10+ datasets, 60+ architectures, all with varying scales and domains. As an example, using imagenet-1k for pretraining and linear evaluation with frozen backbone, LeJEPA reaches 79% with a ViT-H/14."

## Section 3 — Why isotropic Gaussian? (§3)

### Setup

The paper assumes a JEPA forward pass `f_θ: 𝒳 → ℝ^d` followed by a downstream task. Two regression regimes are analyzed:

- **k-NN regression** on the embeddings.
- **Kernel regression** with bandwidth `h`.

For each, the paper computes the **Integrated Square Bias (ISB)** — the expected squared bias of the regression estimator integrated over query points.

### Theorem 1 — Isotropic Gaussian Optimality

> "The integrated square bias (ISB) over query points is given by `ISB_{k-NN} = r₀⁴ / (K+2)² · τ²_g · J(p) + O(r₀⁴)`, `ISB_{kernel} ≤ h² · μ²(K)/(2²) · 2B² + 8L² · J(p) + o(h⁴)`, and among distributions with a scalar-based covariance constraint, **the isotropic Gaussian is the unique minimizer of the integrated square bias.**" *(Proof in §B.4 and §B.7.)*

Reading: under the regularity conditions stated in §A, when you have *no information about which downstream task you'll need*, you should make your embeddings isotropic Gaussian. This is the formal justification for SIGReg's distributional target.

### Geometric intuition (§3.3)

The paper validates the optimality empirically via lemma 1 (bias under Tikhonov regularization) and lemma 2 (variance of the OLS / logistic-regression estimator):

- **Anisotropic embeddings** → cosine similarity between estimated and ground-truth parameters is < 1 (linear regression bias).
- **Anisotropic embeddings** → higher-variance learned parameters across training samples (Figure 3: 2D classification with isotropic vs anisotropic data, learned boundary variance differs by ~14×).

So an anisotropic latent hurts *both* bias and variance of the downstream task — a clean argument for matching a specific isotropic distribution rather than just "any non-collapsed shape."

## Section 4 — SIGReg derivation (§4)

The mathematical heart of the paper. Three building blocks.

### §4.1 Hyperspherical Cramér-Wold + sketching

Direct multivariate normality testing scales at least **quadratically** with sample size. So SIGReg sketches the high-dimensional test into many 1-D tests.

For each unit-norm direction `a ∈ S^{K-1}`, define the push-forward distribution `P_θ^(a) ≜ (a^⊤)_# P_θ` and the directional null hypothesis:

```
H_0(a) : P_θ^(a) = Q^(a)        // 1-D distribution match
H_1(a) : P_θ^(a) ≠ Q^(a)
```

The directional test statistic is `T({a^⊤ f_θ(x_n)}_{n=1..N})`. The **global test statistic** in the original paper formulation (Theorem 2) is the **maximum** over directions in a finite set `A = {a_1, ..., a_M}`:

```
T_A({f_θ(x_n)}_{n=1..N}) ≜ max_{a ∈ A} T({a^⊤ f_θ(x_n)}_{n=1..N})        (eq. 4)
```

> **Lemma 3 — Hyperspherical Cramér-Wold.** Let `X, Y` be `ℝ^d`-valued random vectors. Then `⟨u, X⟩ =_d ⟨u, Y⟩ ∀u ∈ S^{d-1}` ⟺ `X =_d Y`. *(Convergence in distribution also holds. Proof in §B.8.)*

This is the formal tool — matching all 1D marginals along directions on the hypersphere is equivalent to matching the joint distribution.

> **Theorem 2 — Sufficiency of directional tests.** Equation (4) is a valid statistical test, with both **level** (Type-I error bounded by `α`) and **power** (Type-II error → 0 as `n → ∞`) holding under appropriate consistency conditions on `T`. *(Proof in §B.9.)*

### §4.2 SIGReg: average, not max (definition 2)

The paper's **practical** SIGReg definition departs from Theorem 2's max in one important way:

> **Definition 2 — SIGReg.**
> `SIGReg_T(A, {f_θ(x_n)}_{n=1..N}) ≜ (1/|A|) Σ_{a ∈ A} T({a^⊤ f_θ(x_n)}_{n=1..N})`
> *(Average, not max.)*
> *Recommend the **Epps-Pulley test** for `T` (§4.2.3).*

The paper notes the departure explicitly: "We replace the maximum over `a ∈ A` in [Theorem 2] by an **average** [...] to avoid sparse gradient over the directions in `A`." Max is the formally consistent statistic; average is the one that backprops well. This is the same kind of practical-vs-formal trade-off as VICReg's variance penalty (which approximates a hard non-degeneracy constraint with a soft penalty).

### §4.2.1 Why not moments? Theorem 3 — insufficiency of K moments

> "Minimizing `Σ_{k=1..K} c_k (m_k(P_θ^(a)) − m_k(Q^(a)))²` for finite `K` does not imply `P_θ^(a) = Q^(a)`." *(Proof in §B.11.)*

You need *all* moments to determine the distribution (under Carleman's condition for well-behaved densities). But:

- The gradient of the `k`-th moment scales as `O(k)`.
- The Monte-Carlo gradient variance scales as `O(k² · m_{2(k-1)})`.

So as `K → ∞` (which is what identifiability requires), gradient-based optimization becomes unstable. **Moment-based tests give you a stability-vs-identifiability conundrum** that can't be resolved.

### §4.2.2 Why not CDF-based? (Cramér-von Mises, Anderson-Darling, Watson)

CDF-based tests use sorting (rank statistics):

- **Cramér-von Mises:** `T_w = N ∫ (F_N(x) − F(x))² w(x) dF(x)` with `w(x) = 1`.
- **Anderson-Darling:** same form with `w(x) = [F(x)(1 − F(x))]⁻¹`.
- **Watson:** `U² = T_w − N(F̄ − 1/2)²`.

The paper explicitly rejects these for SIGReg because:

1. **Sorting breaks SGD parallelism** — `O(N log N)` quicksort is fast but synchronization-heavy on multi-GPU.
2. **Non-differentiable operations** — sorting and order statistics aren't smooth; require relaxations that introduce more hyperparameters.
3. **Kolmogorov-Smirnov** is *also* rejected: uses `ℓ_∞` instead of `ℓ_2`, producing **sparse gradients**.
4. **Shapiro-Wilk** found unstable in practice (per §E).

### §4.2.3 Why Epps-Pulley specifically — characteristic functions

The empirical characteristic function (ECF) is `φ̂_X(t) = (1/n) Σ_j exp(i · t · X_j)` — the Fourier transform of the empirical density.

The **Epps-Pulley test** (Epps & Pulley 1983) compares the ECF against the target characteristic function in weighted ℓ² norm:

```
EP = N · ∫_{−∞}^{∞} |φ̂_X(t) − φ(t)|² · w(t) · dt
```

with `w(t) = exp(−t² / σ²)`, `σ ≈ 1` (Gaussian weight).

**Why this is the right choice:**

1. **Differentiable.** The ECF is a sum of complex exponentials. Each exponential is smooth; the gradient is just `(i · t / n) · exp(i · t · X_j)`, available via standard autodiff.
2. **Parallelizable.** ECF is an **average** of complex exponentials — perfect for distributed training via `all_reduce`.
3. **Bounded loss, gradient, and curvature.** The paper explicitly establishes this in §4.2.3 — Epps-Pulley has well-behaved derivatives at all orders.
4. **Tests the full distribution.** Unlike moment-based tests (which truncate), the ECF captures all distributional information.
5. **No sparse-gradient pathology.** Unlike KS / Watson / sorted-CDF methods, the integral is smooth in `X`.

### Summary: the SIGReg recipe

```
1. Sample M random unit-norm directions a_1, ..., a_M ∈ S^{K-1}.
2. For each direction, project: h^(m) = {a_m^⊤ f_θ(x_n)}_{n=1..N}.
3. Compute the Epps-Pulley statistic T(h^(m)) per direction (against std Gaussian).
4. Average: SIGReg = (1/M) Σ_m T(h^(m)).
5. Backprop SIGReg through the projections + encoder.
```

Recommended `M = 1024` projections; weight function `w(t) = exp(−t² / σ²)` with `σ = 1`. Linear `O(N · M)` time, embarrassingly parallel.

## Section 5 — LeJEPA (§5, summarized)

LeJEPA combines the JEPA predictive loss with SIGReg:

```
L_LeJEPA = L_JEPA + λ · SIGReg(Z)
```

Single hyperparameter `λ`. No stop-gradient, no teacher-student, no EMA target encoder, no hyperparameter schedulers. ~50 lines of PyTorch (algorithm 1 in §5).

## Section 6 — Experiments (§6, headline results)

- **ImageNet-1k linear-eval, ViT-H/14, frozen backbone: 79%.**
- **Validation breadth:** 10+ datasets, 60+ architectures (ResNets, ViTs, ConvNets including ConvNeXt-V2 Nano).
- **Scale stability:** 1.8B-parameter ViT-g trained without stop-gradient, with stable loss curves (Figure 1, top-right).
- **Galaxy10 in-domain:** LeJEPA in-domain pretraining beats DINOv2 ViT-S/16 and DINOv3 ViT-S/16 transfer learning across regimes (1-shot, full supervision; full FT, frozen).
- **Loss → linear-probe correlation:** Spearman 94.52% on ViT-base / ImageNet-1k. The training loss is a usable model-selection signal *without* requiring a labeled probing run — a practical win for SSL workflows.

## How LeJEPA relates to LeWM

[LeWM](leworldmodel-paper.md) (Maes et al. 2026) takes the LeJEPA recipe and applies it to action-conditioned world modeling for offline RL. Same SIGReg formulation; same single-hyperparameter recipe. What LeWM adds:

- Action conditioning in the predictor (causal AR transformer with AdaLN action input).
- Planning protocol: CEM-MPC against the learned dynamics.
- Robotics-relevant evaluation on PushT, Reacher, OGBench-Cube, Two-Room.
- The BN-after-CLS engineering trick (LeJEPA's pure-SSL setting can use LayerNorm on the encoder output; LeWM's offline-RL setting needs Batch Norm in the projection MLP because LayerNorm pre-normalizes away the batch distribution SIGReg operates on — see [Module 12 §3.1](../syntheses/curriculum/curriculum-12-lewm-deep-dive.md)).

The relationship is the same as VICReg → V-JEPA: a paper introduces an anti-collapse regularizer in a pure-SSL setting, and a successor paper uses the same regularizer for world modeling with actions.

## Why it matters in this wiki

- **The foundational reference for SIGReg.** [Module 12 §2](../syntheses/curriculum/curriculum-12-lewm-deep-dive.md) re-derives SIGReg from the LeWM paper's exposition; the LeJEPA paper itself is now the source for the rigorous version with formal theorems (Theorem 1 isotropic-Gaussian optimality; Lemma 3 hyperspherical Cramér-Wold; Theorem 2 directional-test sufficiency).
- **Resolves a hedge in [Module 12 §2](../syntheses/curriculum/curriculum-12-lewm-deep-dive.md):** the curriculum module says SIGReg "averages" the test statistic across projections. The LeJEPA paper's Theorem 2 actually defines the consistent statistic as the **max**, with the practical SIGReg using **average** for gradient flow. Module 12 has been updated to flag this distinction.
- **Validation breadth (10+ datasets / 60+ architectures)** is what makes LeWM's "single hyperparameter" claim credible at small scale. Without LeJEPA's broad pretraining-side validation, LeWM's four-environment robotics-side results could be hand-tuned. With LeJEPA's results in hand, LeWM is more naturally read as a confirmation that the LeJEPA recipe holds when extended to the action-conditioned setting.
- **Scaling evidence:** the 1.8B ViT-g stable training run is the strongest published evidence that SIGReg-only training works at scale. Module 11's collapse-prevention zoo can now state this with primary-source backing.

## The follow-up: when does this recipe recover the world?

**[When Does LeJEPA Learn a World Model? (Klindt, LeCun, Balestriero, 2026-05-25)](when-does-lejepa-learn-a-world-model-paper.md)** answers the question this paper leaves open — whether SIGReg's isotropic-Gaussian target buys anything beyond anti-collapse. It proves LeJEPA achieves **[linear identifiability](../concepts/world-models/identifiability.md)** of the true latents (recovery up to an orthogonal rotation), and that **the Gaussian is uniquely the distribution for which this holds** — retroactively justifying SIGReg's specific target rather than any anti-collapse regularizer.

Two caveats the follow-up itself supplies: **VICReg and InfoNCE also achieve identifiability** under the theory's assumptions (SIGReg's edge is robustness when they're violated, an empirical claim), and the theorems cover the **encoder only** — not action-conditioned dynamics.

## Entities mentioned

- [LeWorldModel](../entities/leworldmodel.md) — the action-conditioned application of this paper's methodology.
- [Yann LeCun](../entities/yann-lecun.md) — co-author.
- [Randall Balestriero](../entities/randall-balestriero.md) — co-first author.
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — the architecture family this paper provides theory for.

## Concepts touched

- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — LeJEPA is "JEPA done correctly" (per the paper's framing).
- [Self-Supervised Learning](../glossary.md#ssl) — LeJEPA is positioned as a heuristics-free SSL method.
- [Learned latent space](../concepts/world-models/latent-space.md) — the isotropic-Gaussian-target framing.
- [VICReg](../glossary.md#vicreg) — implicit comparison: VICReg targets variance + covariance + invariance separately; LeJEPA targets the *full distribution* (isotropic Gaussian) via SIGReg.

## Open questions / TBD

- ~~**Author entity page for Randall Balestriero**~~ — **done (2026-07-26):** [Randall Balestriero](../entities/randall-balestriero.md), anchoring the SIGReg-line thread across [PLDM](pldm-paper.md), this paper, [LeWM](leworldmodel-paper.md), and the two May 2026 papers.
- **§B.4, §B.7, §B.8, §B.9, §B.11 detailed proofs** — referenced but not unpacked here. Worth re-reading if [Module 12](../syntheses/curriculum/curriculum-12-lewm-deep-dive.md) needs to defend the SIGReg derivation against pushback.
- **Sobolev smoothness coefficient framework (§4.1, Theorem 5)** — alluded to in Figure 4 caption ("the greater α is, the more global will be the impact of SIGReg for a given M"). Connects SIGReg's effective coverage of the hypersphere to the smoothness of the embedding distribution. Not surfaced in this ingest; would deepen the "SIGReg is immune to the curse of dimensionality" claim.
- **PyTorch reference implementation (algorithm 1, §5)** — the ~50-line code snippet. Re-read if the curriculum needs a reproducible reference for capstone-style work.
- **Empirical comparison vs DINOv2 / V-JEPA 2 at matched compute** — the paper reports 79% on ViT-H/14 but the head-to-head against DINOv2 / V-JEPA 2 at the same compute budget is in §6 / appendix tables not surfaced here.
