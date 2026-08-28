---
title: SIGReg (Sketched Isotropic Gaussian Regularization)
type: concept
created: 2026-08-26
updated: 2026-08-26
sources: 10
tags: [sigreg, jepa, lejepa, anti-collapse, isotropic-gaussian, cramer-wold, epps-pulley, balestriero, lecun, latent-space, regularization]
---

**SIGReg (Sketched Isotropic Gaussian Regularization)** — the single-term anti-collapse regularizer that makes a [JEPA](jepa.md) trainable end-to-end without stop-gradients, EMA teachers, frozen encoders or schedulers. It works by **pushing the embedding distribution toward an isotropic Gaussian**, tested not directly but by *sketching* the high-dimensional normality test into many cheap 1-D tests along random directions.

Introduced by [Randall Balestriero](../../entities/randall-balestriero.md) & [Yann LeCun](../../entities/yann-lecun.md) in **[LeJEPA](../../sources/lejepa-paper.md)** (arXiv 2511.08544, Nov 2025). It is the load-bearing component of the wiki's whole "Le-" line — [LeWorldModel](../../entities/leworldmodel.md), [LeNEPA](../../sources/lenepa-paper.md) — and the baseline every subsequent anti-collapse proposal is measured against. See the short definition in the [glossary](../../glossary.md#sigreg) and the full derivation in [Curriculum Module 12](../../syntheses/curriculum/curriculum-12-lewm-deep-dive.md).

## Why an isotropic Gaussian, specifically

This is the part that distinguishes SIGReg from a heuristic. LeJEPA's Theorem 1 proves the isotropic Gaussian is the **unique** embedding distribution minimizing the **worst-case Integrated Square Bias** under k-NN and kernel regression, among distributions with a scalar covariance constraint.

The reading that makes it intuitive: **when you have no information about which downstream task you will need, isotropic Gaussian is the distribution to be in.** It is a minimax choice under task uncertainty, not an aesthetic preference for round point clouds.

## The mechanism: why "sketched"

Direct multivariate normality testing scales **at least quadratically** with sample size — unusable inside a training loop. SIGReg replaces it with a sketch:

1. **Project** embeddings onto `M` random unit-norm directions `a ∈ S^{K-1}`.
2. **Test** each 1-D projection for normality.
3. **Average** the test statistics and backprop the result as a loss term.

The justification is a **hyperspherical Cramér–Wold theorem** (Lemma 3): matching *all* 1-D marginals of a `d`-dimensional distribution is equivalent to matching the full joint. So testing along enough random directions is not an approximation of the right thing — asymptotically it *is* the right thing, with a directional-test consistency theorem (Theorem 2) to close the gap.

> [!note] Two details where the practice departs from the theory, both deliberate
> **Average, not max.** Theorem 2 is stated over the *maximum* across directions; SIGReg's practical Definition 2 uses the **mean**. The max is the sharper statistic; the mean is the one with usable gradients.
>
> **Epps–Pulley, and the reason is optimization, not statistics.** The per-direction normality test is the **Epps–Pulley** statistic, chosen over the obvious alternatives for concrete reasons: moment-based tests are numerically unstable; CDF-based tests (Kolmogorov–Smirnov, Anderson–Darling) require **sorting**, and `O(N log N)` sorting is synchronization-heavy across GPUs, breaking SGD parallelism. Characteristic-function-based tests are **differentiable, parallelizable, and consistent**. The regularizer's design is driven by what backpropagates cleanly at scale.
>
> *(An earlier version of this wiki described the test as "Anderson–Darling-style." That was wrong and was corrected in Module 12; Epps–Pulley is the statistic.)*

## What it buys

| | Prior end-to-end JEPAs ([PLDM](../../entities/pldm.md)) | LeJEPA / SIGReg |
|---|---|---|
| Loss hyperparameters | 4–6 | **1** (`λ`, default 0.1) |
| Stop-gradient | required | **none** |
| EMA / teacher–student | required | **none** |
| Schedulers | required | **none** |
| Time & memory | — | **linear** |
| Implementation | — | **~50 lines**, distributed-friendly |

Empirically it holds at scale: ImageNet-1k pretraining with linear eval on a **frozen ViT-H/14 reaches 79% top-1**, validated across **10+ datasets and 60+ architectures** (ResNets, ViTs, ConvNets) up to a **1.8B-parameter ViT-g** with stable loss curves.

**The practical diagnostic**, which is worth knowing if you ever train one: **the SIGReg loss descending alongside the prediction loss is the no-collapse signal.** If prediction loss falls while SIGReg loss does not, the encoder is buying prediction accuracy by degenerating the representation. An [independent reproduction](../../sources/onchain-ai-garage-lewm-reproduction.md) on a consumer RTX 3060 arrived at the same diagnostic unprompted, with SIGReg loss **28 → 1.4** against the paper's 40 → ~0.

## The theoretical upgrade

> [!note] From anti-collapse trick to load-bearing choice
> [When Does LeJEPA Learn a World Model?](../../sources/when-does-lejepa-learn-a-world-model-paper.md) (Klindt, LeCun & Balestriero, 2026) proves LeJEPA achieves **[linear identifiability](identifiability.md)** — the encoder recovers the true latents up to an orthogonal rotation — **and that the Gaussian latent distribution is *uniquely* the one for which this holds.**
>
> That is a second, independent argument arriving at the same target from a different direction. LeJEPA's Theorem 1 says Gaussian minimizes downstream prediction risk under task uncertainty; the identifiability converse says Gaussian is the only distribution under which every optimum is linear. SIGReg's specific target stops looking like a design choice and starts looking like the only available one.

## Where it is challenged

And then, within a year, three results pushed back — none of which refutes the theory, all of which bound it.

**1. Inverse dynamics beats it on the hardest task.** [SMWM](../../entities/smwm.md) ([paper](../../sources/sensorimotor-world-models-paper.md), Ivashkov, Balestriero, Schölkopf 2026) replaces the distributional regularizer with an **inverse-dynamics** one — predict the *action* from an embedding pair — and matches SIGReg on 2D while clearly winning in 3D:

| Task | SMWM | SIGReg |
|---|---:|---:|
| TwoRoom (2D nav) | **99** | 94 |
| Reacher | 66 | **67** |
| Push-T | 83 | **87** |
| **OGBench-Cube (3D tabletop)** | **84** | **59** |

The conceptual difference matters more than the numbers: SIGReg **prescribes a latent geometry**; inverse-dynamics regularization **anchors the representation to a task-grounded quantity** instead, biasing toward controllable degrees of freedom and filtering uncontrollable distractors. Whether the two are complementary or redundant is explicitly unanswered.

**2. A non-Gaussian target models dynamics better.** [LpWM](../../entities/lpwm.md) ([paper](../../sources/lpwm-paper.md)) swaps SIGReg for **RDMReg**, matching features to a *Rectified Generalized Gaussian* to get sparse non-negative codes, and reports **+24–57% over dense LeWM on PushT at intermediate predictor capacity**. No formal contradiction — the Gaussian theorems cover the **encoder**, while LpWM is about the **predictor's** job — but the practical implication is real: *the geometry that makes an encoder identifiable may not be the geometry that makes its dynamics cheap to predict.* See [gradient-based planning](gradient-based-planning.md), where this sits beside a third criterion (straightness).

**3. It does not deliver robustness.** [stable-worldmodel](../../sources/stable-worldmodel-paper.md) measured SIGReg-trained [LeWM](../../entities/leworldmodel.md) dropping from **50.8% to 6–26%** on Push-T under color/size/shape shift. Proved identifiability and proved anti-collapse have not produced an out-of-distribution-robust model; see [identifiability](identifiability.md) for why the two results are not reconciled by either paper.

> [!warning] The Two-Room case is where the isotropic-Gaussian assumption is most strained
> LeWM's Two-Room result is its **weakest** across the four environments and is **worse than PLDM**'s — the environment [Curriculum Module 12](../../syntheses/curriculum/curriculum-12-lewm-deep-dive.md) singles out as exposing a SIGReg limitation. Worth stating with the qualifier the [reproduction](../../sources/onchain-ai-garage-lewm-reproduction.md) adds, though: the "failure-mode" result is still **92%** on consumer hardware. **Weakest is not broken.**

## Implementation notes

- **`λ` is the single hyperparameter** — the SIGReg loss weight, default **0.1**.
- **The BN-after-CLS-token trick is load-bearing for optimizability** in [LeWM](../../entities/leworldmodel.md)'s architecture, per [Module 12](../../syntheses/curriculum/curriculum-12-lewm-deep-dive.md) — a detail easy to drop when reimplementing and expensive to debug.
- Runnable recipes: [LeWorldModel howto](../../syntheses/world-models/leworldmodel-howto.md), and the [RTX 3060 reproduction](../../sources/onchain-ai-garage-lewm-reproduction.md) for what the loss curves should look like on consumer hardware.

## Related concepts

- [JEPA](jepa.md) — the architecture; SIGReg is one rung on its [anti-collapse design space](jepa.md#common-training-challenges).
- [Identifiability](identifiability.md) — why the Gaussian target is uniquely right, and where that guarantee stops.
- [Learned latent space](latent-space.md) — the object SIGReg shapes; also covers the sparse and straight alternatives.
- [Gradient-based planning](gradient-based-planning.md) — three competing criteria for a good planning latent space, of which SIGReg's is one.
- [Spectral theory of SSL](../learning/spectral-theory-of-ssl.md) — the shared mathematical frame.

## Mentioned in

- [LeJEPA paper (Balestriero & LeCun, 2025)](../../sources/lejepa-paper.md) — **the primary**; Theorem 1, the Cramér–Wold sketch, Epps–Pulley.
- [LeWorldModel paper](../../sources/leworldmodel-paper.md) — SIGReg applied to action-conditioned world modeling.
- [When Does LeJEPA Learn a World Model?](../../sources/when-does-lejepa-learn-a-world-model-paper.md) — the uniqueness converse.
- [Sensorimotor World Models paper](../../sources/sensorimotor-world-models-paper.md) — inverse-dynamics regularization as the alternative; beats SIGReg 84 vs 59 on OGBench-Cube.
- [LpWM paper](../../sources/lpwm-paper.md) — a non-Gaussian sparse target for dynamics.
- [stable-worldmodel paper](../../sources/stable-worldmodel-paper.md) — the out-of-distribution collapse SIGReg does not prevent.
- [LeNEPA paper](../../sources/lenepa-paper.md) — SIGReg carried into time-series SSL.
- [PLDM paper](../../sources/pldm-paper.md) — the 4–6-hyperparameter baseline it replaces.
- [LeWM reproduction on an RTX 3060](../../sources/onchain-ai-garage-lewm-reproduction.md) — independent loss-curve confirmation and the no-collapse diagnostic.
