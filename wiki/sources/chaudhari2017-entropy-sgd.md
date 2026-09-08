---
title: "Entropy-SGD: Biasing Gradient Descent Into Wide Valleys (Chaudhari, Choromanska, Soatto, LeCun, Baldassi, Borgs, Chayes, Sagun & Zecchina, ICLR 2017)"
type: source
url: https://arxiv.org/abs/1611.01838
fetch_url: https://arxiv.org/pdf/1611.01838v5
local_path: raw/1611.01838v5.pdf
sha256: 0bdf8b99236a1892809db3ac6774372f04a9265d15cb328de717680279f34d39
author: "Pratik Chaudhari, Anna Choromanska, Stefano Soatto, Yann LeCun, Carlo Baldassi, Christian Borgs, Jennifer Chayes, Levent Sagun, Riccardo Zecchina (UCLA, NYU, Facebook AI Research, Politecnico di Torino, Microsoft Research New England)"
venue: "ICLR 2017; arXiv v5, 2017-04-21"
published: 2016-11-06
ingested: 2026-09-07
format: "paper, 12 pp. + appendices (SGLD, proofs, variational-inference connection, SGLD comparison); code at github.com/ucla-vision/entropy-sgd"
tags: [loss-landscape, flat-minima, wide-valleys, local-entropy, free-entropy, langevin-dynamics, sgld, hessian-spectrum, generalization, uniform-stability, statistical-physics, gibbs-distribution, lecun, choromanska, primary-source, foundational]
---

## Summary

**Turn the free energy of statistical physics into a training objective, so that optimization seeks wide valleys instead of deep points.** The paper starts from a measurement: at the minima SGD and Adam actually find, the Hessian is **almost entirely flat** — about **94%** of eigenvalues within 10⁻⁴ of zero on a 47k-parameter LeNet, ~90–95% on a fully-connected net, a char-LSTM and a 1.6M-weight All-CNN — with a **long positive tail** (largest eigenvalue ~40) and a **short negative tail** (largest negative −0.46). Minima that generalize sit in wide, almost-flat regions. So instead of minimizing the loss `f(x)`, Entropy-SGD *maximizes* the **local entropy**

`F(x, γ) = log ∫ exp(−f(x′) − (γ/2)‖x − x′‖²) dx′`

— the log-partition function of a Gibbs distribution focused around `x` by a quadratic "scope" `γ`. It measures depth *and* width at once, and its gradient is `γ(x − ⟨x′⟩)`, the pull toward the *mean* of nearby low-loss configurations, which for two neighbouring minima of equal loss points toward the wider one. The expectation is estimated by **stochastic gradient Langevin dynamics** in an inner loop: the algorithm is *"SGD inside SGD."*

The result on the benchmarks of the day is **parity in error and a speed-up on recurrent nets** — 2× fewer effective epochs on Penn Treebank and War-and-Peace char-LSTMs — plus a generalization bound via uniform stability that says the smoothed objective generalizes better for the same number of passes. The number the wiki should carry is not any of those. It is the **Hessian spectrum**, which was new, held across every architecture they tried, and became the empirical anchor of the flat-minima literature.

The paper is here for the same reason as its [2015 sibling](choromanska2015-loss-surfaces-multilayer-networks.md): it is the second of the three LeCun-coauthored statistical-physics papers the [physics essay](jepa-vs-physics-moudrkat.md) surfaced, and it is the optimization-side twin of the regularized-EBM principle in the [Les Houches notes](dawid-lecun-lvebm-lecture-notes.md) — *bound the volume of the low-energy region.* Read against the wiki's JEPA thread it also poses a sharp question: **an objective that seeks the widest low-loss valley would, on a joint-embedding loss, seek collapse.** See [loss-landscape geometry](../concepts/learning/loss-landscape-geometry.md).

## Key claims

### The observation (§1, §5.1) — universality of the Hessian at SGD's minima

Exact Hessians (autograd) at the end of training, or the diagonal Fisher as a proxy for the large net:

| Network | Params | Near-zero eigenvalues | Notes |
|---|---|---|---|
| small-LeNet, MNIST | 47,658 | **≈ 94%** (|λ| < 10⁻⁴) | largest +40, largest negative −0.46 |
| small-mnistfc | 50,890 | ≈ 90% (|λ| ≤ 10⁻²) | |
| char-LSTM | 32,640 | ≈ 95% (|λ| < 10⁻⁵) | |
| All-CNN-BN, CIFAR-10 | ~1.6M | ≈ 95% (Fisher diag) | |

*"For a wide variety of network architectures, sizes and datasets, optima obtained by SGD are mostly flat… they always have a few directions with large positive curvature… A very small fraction of directions have negative curvature, and the magnitude of this curvature is extremely small."* The novel part, in their words: *"the directions of descent that SGD misses do not have a large curvature."*

### The objective (§3)

- **Local entropy** `F(x, γ)` is the log-partition function of the modified Gibbs distribution `P(x′; x, β, γ) ∝ exp(−β f(x′) − βγ/2 ‖x − x′‖²)`, with β set to 1 because γ gives the same control. Called *"local entropy in analogy to the free entropy used in statistical physics"*; it extends Baldassi et al.'s (2015–16) discrete-weight results to continuous weights.
- **Scope γ**: large γ → mass near `x` regardless of loss (objective ≈ original); small γ → landscape much smoother, global minimum moves to the wide valley (Fig. 2, `x_robust` vs `x_non-robust`); γ → 0 → nearly uniform.
- **Not classical entropy**: classical entropy would favour any flat region, including flat high-loss plateaus (`x_candidate`); local free entropy weighs flatness *and* depth.
- **Not smoothing**: homotopy/continuation methods convolve the loss and can invent a false minimum between two sharp ones; local entropy *"places more weight on wide local minima even if they are much shallower than the global minimum,"* which smoothing cannot do.

### The algorithm (§4)

- **Gradient**: `−∇F = γ(x − ⟨x′⟩)`, the expectation over the locally focused Gibbs distribution (Eq. 7–8).
- **Estimation by SGLD**: L inner steps of noisy SGD with a forcing term `−γ(x − x′)` and thermal noise ε ∈ [10⁻⁴, 10⁻³]; exponential averaging (α = 0.75) of the inner iterates gives `µ ≈ ⟨x′⟩`; outer step `x ← x − ηγ(x − µ)`. L ∈ [5, 20].
- **Scoping**: *reverse-annealing* γ upward as training proceeds — `γ(t) = γ₀(1 + γ₁)ᵗ` — explores coarse to fine. Interferes with learning-rate annealing, so in practice the update is rescaled to `x ← x − η(x − µ)`.
- **Interpretations offered**: the inner loop resembles one large step along the noisy average gradient, i.e. **averaged SGD** (Polyak–Juditsky); and the "moving prior" `exp(−γ/2‖x − z‖²)` makes it *not* variational inference — Appendix C shows local entropy equals an ELBO only for a "flat variational family" with an `x`-dependent prior, which is not a prior.

### Theory (§4.4)

- Lemma 2: `F` is `α/(1 + γ⁻¹c)`-Lipschitz and `β/(1 + γ⁻¹c)`-smooth — smoother than `f` by the same factor — **if no Hessian eigenvalue lies in [−2γ − c, c]**.
- Via Hardt–Recht–Singer uniform stability: `ε_Entropy-SGD ≲ α T^{−(1 − 1/(1+γ⁻¹c))^β} ε_SGD` (Eq. 9) — better generalization for all T > α at equal passes.
- Remark 4, the authors' own caveat: the eigenvalue assumption *"is admittedly unrealistic"* — Fig. 1 shows most eigenvalues near zero, i.e. inside the excluded set. A bound without it *"would require a dynamical analysis of SGD and seems out of reach currently."*

### Results (§5, Table 1)

| Model | Entropy-SGD | Epochs×L | SGD / Adam | Epochs |
|---|---|---|---|---|
| mnistfc | 1.37 ± 0.03% | 120 | 1.39 ± 0.03% | 100 |
| LeNet (BN) | 0.50 ± 0.01% | 80 | 0.51 ± 0.01% | 100 |
| All-CNN-BN, CIFAR-10 (no aug.) | 7.81 ± 0.09% | 160 | 7.71 ± 0.19% | 200 |
| PTB-LSTM (66M) | 77.656 ± 0.171 ppl | **25** | 78.6 ± 0.26 | 55 |
| char-LSTM (War and Peace) | 1.217 ± 0.005 ppl | **25** | 1.226 ± 0.01 | 50 |

- **CNNs: parity**, marginal wall-clock gain at best. **RNNs: half the effective epochs and slightly better perplexity.** Their reading: the local-entropy gradient's angle to the SGD gradient changes far faster for RNNs, *"which suggests a more rugged energy landscape for the former."*
- **Always lower training cross-entropy than SGD at equal generalization** (§6) — hence the claim that wide valleys sit *deeper*, against the "equivalent minima" models of §2 including Choromanska et al.
- **Momentum was decisive on RNNs** (0.5 vs the baseline's none); CNNs used 0.9 throughout.
- **Appendix C.1, vanilla SGLD**: LeNet 0.63 ± 0.1% after 300 epochs, All-CNN 9.89 ± 0.11% after 500 — *"much worse"* than Entropy-SGD; PTB 94.03 vs 77.656 for prior SGLD work. Their explanation: temperature trades energy for entropy globally and *"does not help with narrow minima"*; local entropy uses the landscape's geometry directly.

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md) — fourth author (NYU + Facebook AI Research); the second of his three statistical-physics papers here.
- [Anna Choromanska](../entities/anna-choromanska.md) — second author; first author of the 2015 sibling.
- Pratik Chaudhari, Stefano Soatto (UCLA); Carlo Baldassi, Riccardo Zecchina (Torino — the discrete-weight local-entropy line this extends); Christian Borgs, Jennifer Chayes (MSR); Levent Sagun (NYU; *Singularity of the Hessian in Deep Learning*, the parallel spectrum paper) — no entity pages.

## Concepts touched

- [Loss-landscape geometry](../concepts/learning/loss-landscape-geometry.md) — the flat-minima half of the concept page.
- [Energy-based models](../concepts/learning/energy-based-models.md) — Gibbs distribution, partition function, free entropy used as a *training objective*; the "bound the volume of the low-energy region" principle from the optimizer's side.
- [JEPA](../concepts/world-models/jepa.md) — the collapse question: the trivial solution is the widest valley.
- [Test-time adaptation](../concepts/learning/test-time-adaptation.md) — a moving prior around the current iterate is also what online adaptation does; noted, not developed.

## Open questions

- **The widest valley of a joint-embedding loss is the collapsed one.** Entropy-SGD's whole mechanism — pull toward the mean of nearby low-loss configurations — would, applied to a JEPA prediction loss without a regularizer, accelerate collapse. Does [SIGReg](../concepts/world-models/sigreg.md) or VICReg change the *width* of the collapsed basin, or remove it? Nobody in the wiki has measured the Hessian at a JEPA solution.
- **Did the RNN speed-up survive?** 2017 RNN baselines; the claim has not been checked against later optimizers or transformers here.
- **Sharp-vs-flat was contested a few months later** (Dinh et al. 2017, *Sharp Minima Can Generalize*, via reparameterization). Not ingested; the concept page carries the caveat without a source.
- **Levent Sagun's parallel Hessian work** (Sagun, Bottou, LeCun 2016) is cited as the companion measurement and is not filed.
