---
title: "galilai-group/lejepa — the LeJEPA reference implementation and normality-test library"
type: source
url: https://github.com/galilai-group/lejepa
author: "Randall Balestriero, Yann LeCun (GalilAI group / Brown University, NYU)"
published: 2026-01-25
ingested: 2026-09-02
venue: GitHub repository (pip package `lejepa`)
format: code + MINIMAL.md walkthrough
tags: [lejepa, sigreg, epps-pulley, normality-test, vicreg, ssl, balestriero, lecun, implementation, model-selection]
---

# galilai-group/lejepa

## Summary

The reference implementation behind [LeJEPA](lejepa-paper.md) (arXiv 2511.08544). Two things the paper does not give you: a **130-line runnable ViT/ImageNette example** (`MINIMAL.md`, authored by Balestriero and LeCun, dated 2025-11-20), and — more interesting for this wiki — the discovery that the shipped package is not "SIGReg" at all but a **general library of distributional normality tests**, of which SIGReg is one configuration.

Last commit `c293d29`, **2026-01-25** — the repo has been static for seven months while the surrounding work moved on. Installable as `pip install lejepa`.

> [!warning] Repository moved: `rbalestr-lab` → `galilai-group`
> Both `rbalestr-lab/lejepa` and `rbalestr-lab/stable-worldmodel` now **301-redirect** to `galilai-group/*`. The org is **GalilAI-group** — *"Foundation Models, Theory, World Models, Everything AI"*, created 2024-05-25, 14 public repos. This wiki's [stable-worldmodel entity](../entities/stable-worldmodel.md) previously described galilai-group as a *mirror*; it is the canonical home, and rbalestr-lab is the redirect. The repo's own README still points readers at the old URL.

## SIGReg is one member of a test family

The package exposes normality tests as interchangeable components, which reframes what [SIGReg](../concepts/world-models/sigreg.md) is:

| `lejepa.univariate` | `lejepa.multivariate` |
|---|---|
| `EppsPulley` (SIGReg's choice), `AndersonDarling`, `CramerVonMises`, `ShapiroWilk`, `Watson`, `Entropy`, `NLL`, `Moments`, `ExtendedJarqueBera`, **`VCReg`** | `SlicingUnivariateTest`, `BHEP`, `HZ` (Henze–Zirkler), `HV`, `comb` |

Composition is explicit — pick a univariate test, wrap it in the slicing operator, choose a slice count:

```python
loss_fn = lejepa.multivariate.SlicingUnivariateTest(
    univariate_test=lejepa.univariate.EppsPulley(num_points=17),
    num_slices=1024)
loss = loss_fn(embeddings); loss.backward()
```

Each test has its own unit-test file (`tests/test_epps_pulley.py`, `test_shapiro_wilk.py`, `test_hz.py`, …), so these are maintained implementations rather than sketches.

> [!note] **VICReg is exported as a special case of a moment-based normality test**
> `VCReg` sits in `univariate/jarque_bera.py` alongside `ExtendedJarqueBera`, both re-exported from the same module. The Jarque–Bera statistic is built from **skewness and kurtosis** — the third and fourth moments — and VICReg's variance-covariance term is the second-moment fragment of the same family.
>
> The wiki's [SIGReg page](../concepts/world-models/sigreg.md) treats SIGReg and VICReg as competing anti-collapse proposals. This code says they are **points on one axis: how many moments of the Gaussian you insist on**. VICReg constrains second moments and is blind to everything above; Epps–Pulley matches the whole characteristic function. That is a cleaner account of why VICReg collapses in the regimes it does than "it is a different heuristic," and it is asserted by a module layout rather than by a paper.

## The implementation detail that differs from the paper

`MINIMAL.md` flags a deliberate deviation, and explains the reasoning:

> *"We leverage the symmetric property of the ECF/CF to improve the quadrature efficiency (integrate on `[0, t_max]` and doubling, instead of integrating on `[-t_max, t_max]`) — **improved quadrature for free**."*

The shipped 24-line `SIGReg` module: **17 knots** over `t ∈ [0, 3]`, trapezoidal weights doubled except at the endpoints, a Gaussian window `exp(-t²/2)`, **256 random unit slice directions** resampled every call, and the statistic scaled by the sample count. The empirical characteristic function is compared to the Gaussian one in both real (`cos`) and imaginary (`sin`) parts. Anyone reimplementing SIGReg from the paper alone would integrate over twice the domain for the same answer.

## Claims made by the repo, not all of them in the wiki yet

- **~50 lines of core code**; the complete worked example is 130. Single hyperparameter λ. No stop-gradient, teacher–student, register tokens or schedulers.
- Works out of the box across **60+ architectures** and **10+ datasets**, scaling to **1.8B parameters**.
- **The training loss is informative** — *"94%+ Spearman correlation between training loss and downstream performance."*

> [!note] The model-selection claim is the one worth chasing
> *"You can finally do model selection without labeled validation data."* If a 94% Spearman correlation between an unsupervised training loss and downstream accuracy holds up, it removes the labeled validation set from the SSL loop — which matters far more for robotics than for ImageNet, since [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) is the wiki's most expensive recurring problem and a real-world rollout is the labeled validation set. **This wiki has not verified the number, and no ingested source reproduces it.**

The README's benchmark table is the parameter-efficiency argument: **LeJEPA ViT-L (304M, IN-1K, 100 epochs)** against **I-JEPA ViT-H (632M, 300 epochs)** across eight transfer datasets — LeJEPA leads the average at 1-shot (31.58 for the ConvNeXtV2-H variant vs 30.20), 10-shot (60.95 vs 60.51) and full (79.48 vs 78.50), at roughly half the parameters and a third of the epochs. Margins are thin and per-dataset results are mixed (I-JEPA wins CIFAR-10/100 nearly everywhere); the honest reading is **parity at a third of the compute**, not a sweep.

## Caveats

- **Static since January 2026.** Meanwhile [`stable-pretraining`](wm-booth-lejepa-lewm-tutorial-repo.md) carries the SIGReg implementation the lab's own tutorials import (`stable_pretraining.methods.lejepa.SlicedEppsPulley`), not this package. Two live implementations of the same objective, and this is not the one the authors reach for.
- Benchmarks are IN-1K pretraining and image transfer only. Nothing about world models, control, or temporal data.
- The 94% Spearman claim carries no plot, dataset list, or protocol in the README.

## Entities mentioned
- [Randall Balestriero](../entities/randall-balestriero.md), [Yann LeCun](../entities/yann-lecun.md). **GalilAI-group** — the org, no page.

## Concepts touched
- [SIGReg](../concepts/world-models/sigreg.md) — **the primary implementation reference**, and the test-family reframing.
- [JEPA](../concepts/world-models/jepa.md) · [spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) · [latent space](../concepts/world-models/latent-space.md).

## Open questions
- **Has anyone swept the univariate test?** Ten drop-in alternatives with unit tests, one used. `scripts/launch_epps_ablation.md` exists in the repo, so the authors ran something — the results are not in the README.
- **Does the loss↔performance correlation survive into world models?** In [LeWM](../entities/leworldmodel.md) the loss has a prediction term as well as SIGReg, and the wiki's [stable-worldmodel](stable-worldmodel-paper.md) results show planning success collapsing under perturbation with no obvious loss signature.
- **Is the VICReg-as-low-order-moments framing published anywhere**, or only implied by this module layout? It is a cleaner story than the wiki currently tells and deserves a citation.
