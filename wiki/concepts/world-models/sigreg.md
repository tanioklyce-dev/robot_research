---
title: SIGReg (Sketched Isotropic Gaussian Regularization)
type: concept
created: 2026-08-26
updated: 2026-09-03
sources: 19
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

## VISReg — decomposing the regularizer (2026-09-01)

**VISReg** (Haiyu Wu, [Balestriero](../../entities/randall-balestriero.md), Morgan Levine; Altos Labs) keeps SIGReg's theorem and **splits the regularization into three separately re-weightable components — scale, shape and centre** ([Day 2 lightning talk](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md)). More hyperparameters, in exchange for three claimed properties:

- **A stronger anti-collapse gradient** — the signal grows sharply as the embedding starts to collapse, rather than degrading gracefully.
- **Robustness to skewed data**, via re-weighting the three terms: reported as a modest improvement when pretraining on long-tailed ImageNet.
- **Out-of-domain performance**: DINOv2-comparable results scaling to ImageNet-22k on **~10% of the data**.

Swapped into a LeWM-style world model on the same benchmarks, it beats end-to-end methods on four datasets except against VICReg, which the presenter attributes to VICReg's own instability rather than a clean win.

> [!warning] The batch-size dependence is a real constraint, and it is disclosed
> VISReg only outperforms the SIGReg-based world model at **large batch size** — because the shape term is built on a **sliced-Wasserstein distance**, which is sensitive to batch size (a larger batch gives a better distributional target). At matched small batch, the SIGReg baseline is the more stable of the two. That inverts SIGReg's own selling point: LeJEPA's pitch is that it trains stably without tuning, and a variant that needs a large batch to win has spent part of that.

Two honest negatives from the same talk: it remains **sensitive to noise**, and **open-loop long-horizon planning still degrades badly** from 25 → 75 steps — *"this is a fundamental problem of the world model, not just the regularization. We need to design probably new prediction losses or the model design."* The wiki's [gradient-based planning](gradient-based-planning.md) and [stable-worldmodel](../../sources/stable-worldmodel-paper.md) pages record the same ceiling.

## What the shipped code says that the paper does not

Ingesting the [`lejepa` package](../../sources/lejepa-github.md) and the [lab's tutorial repo](../../sources/wm-booth-lejepa-lewm-tutorial-repo.md) changes three things on this page.

### 1. SIGReg is one configuration of a normality-test library

The package does not export "SIGReg". It exports a **family of distributional tests** you compose:

| `lejepa.univariate` | `lejepa.multivariate` |
|---|---|
| `EppsPulley` (SIGReg's choice), `AndersonDarling`, `CramerVonMises`, `ShapiroWilk`, `Watson`, `Entropy`, `NLL`, `Moments`, `ExtendedJarqueBera`, **`VCReg`** | `SlicingUnivariateTest`, `BHEP`, `HZ` (Henze–Zirkler), `HV` |

SIGReg = `SlicingUnivariateTest(EppsPulley(num_points=17), num_slices=1024)`. Each alternative has its own unit-test file, so these are maintained, not sketched. **Nine drop-in alternatives; one is used, and no ablation is published** (though `scripts/launch_epps_ablation.md` exists, so one was run).

### 2. VICReg is a *low-order-moment* member of the same family

> [!note] This reframes the "Where it is challenged" section above
> `VCReg` ships inside `univariate/jarque_bera.py`, re-exported alongside `ExtendedJarqueBera`. Jarque–Bera is built from **skewness and kurtosis** — third and fourth moments — and VICReg's variance-covariance term is the second-moment fragment of the same construction.
>
> So SIGReg and VICReg are not competing heuristics. They are **points on one axis: how many moments of the Gaussian you insist on.** VICReg constrains second moments and is blind above them; Epps–Pulley matches the entire characteristic function. That is a much better account of *why* VICReg collapses where it does — and it is asserted here by a module layout rather than by any paper the wiki has ingested.

### 3. A quadrature trick that is not in the paper

`MINIMAL.md` flags the deviation explicitly: exploit the symmetry of the empirical characteristic function to **integrate over `[0, t_max]` and double, instead of `[-t_max, t_max]`** — *"improved quadrature for free."* The shipped module uses **17 knots over `t ∈ [0,3]`**, trapezoidal weights doubled except at the endpoints, a Gaussian window `exp(-t²/2)`, and **256 unit slice directions resampled every call**. Anyone reimplementing from the paper integrates twice the domain for the same answer.

### And an unverified claim worth chasing

The repo asserts **"94%+ Spearman correlation between training loss and downstream performance"**, i.e. *"you can finally do model selection without labeled validation data."* No plot, dataset list or protocol accompanies it.

> [!note] There is an independent method making the same offer, and it has a table
> **RankMe** — the effective rank of the embeddings — does label-free model selection and recovers essentially all of a labelled ImageNet oracle's hyperparameter-selection quality across VICReg, SimCLR and DINO ([Cookbook](../../sources/ssl-cookbook.md) Table 3; see [representation evaluation](../learning/representation-evaluation.md)). It predates the repo claim by three years and is recommended in a survey Balestriero first-authored. **Whether SIGReg loss and RankMe agree on the same checkpoints is an unrun, cheap experiment** — and it is the natural way to verify the 94% claim without labels. If true it matters far more in robotics than in vision, because there the labeled validation set is a [real-robot rollout](../robotics/robot-policy-evaluation.md).

## What its author says when teaching it (2026-09-02)

Balestriero's [Day 3 tutorial](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) is the only source here where he explains SIGReg live rather than in a paper. Five additions:

**1. The DINO critique is sharper than the papers make it.** EMA doubles model memory, adds a hyperparameter, and **makes the loss uninterpretable** — *"you can see the loss actually increase but the quality of your model become better and better."* Hyperparameter changes move ImageNet-1k accuracy *"from almost state-of-the-art to completely random."* That instability, he argues, is why people refuse to train JEPAs at all — which is the market SIGReg is for.

**2. Epps–Pulley's one implementation gotcha, stated aloud:** the random projection directions must be **identical across GPUs**. Seed carefully; everything else *"falls back in very easily."*

**3. Architecture-agnosticism is the pitch to non-vision domains.** **50 architectures** thrown at ImageNet-10 out of the box, all training to within a small delta of each other, with no per-architecture tuning. *"When you want to do JEPA on new domains with new architecture, you need this stability."* Aimed at the finance half of the room, and the reason [Market-JEPA](../../entities/market-jepa.md) and [LeNEPA](../../sources/lenepa-paper.md) exist.

**4. The detached-decoder diagnostic — stated as a rule, not a tip.**

> *"This is something that you should always do when you train a world model. Always plug a detached online decoder and see what it reconstructs, because this is quite informative to see if you have a collapsed Z, or if you have a Z that actually did not collapse enough and the reconstruction is very crisp."*

Trained **post-hoc and gradient-detached**, so it never touches training dynamics. On his cube example, arm motion and joint configuration decode correctly from actions alone while **cube rotation and gripper rotation do not** — a visible, cheap map of what the latent kept. Note the *two-sided* reading: crisp reconstruction is a warning too, meaning the latent retained detail it should have discarded.

**5. SIGReg + IDM is the direction, and the ablation explains why.** [SMWM](../../entities/smwm.md)'s inverse-dynamics regularizer is the rival on this page; the tutorial makes both bounds concrete. In IDM's favour: if the inverse model is weak (linear), then a linear combination of `z_t` and `z_{t+1}` must recover `a_t` — *"a very very strong geometric constraint on how you put your Z embedding, which you don't have with SIGReg"* — and the resulting space is *"much easier to optimize for at planning time."* Against it: its anti-collapse power is **bounded by the richness of the action space**, shown by ablation — no actions loses position and shape; XY-only control preserves position but goes **shape-invariant**; only XY *plus* rotation retains enough to reconstruct the object. Since *"in practice we never observe all the actions,"* **combining the two is the promising path**, and he says the latest work does.

> [!note] A free ablation of the Gaussian target, from the hackathon
> A team with two hours swapped SIGReg's isotropic Gaussian for **multivariate Laplace** and **Student-t** on MNIST (and tried it on UrbanSound audio): **Gaussian beat both, by a clear margin.** No tuning, small scale, one dataset — it settles nothing against [LpWM](../../entities/lpwm.md)'s +24–57% with a sparse Rectified Generalized Gaussian on Push-T. But it is the first attempt in this wiki at the ablation the tutorial explicitly invited, and it went the theory's way. Balestriero's own live position is that the target matters less than the mechanism: *"in terms of performance it does not seem to matter so much as long as you feed the distribution in a nice way."*

> [!note] What the heuristic stack actually was — now sourced
> SIGReg is pitched against "the stop-gradient / EMA / frozen-encoder heuristic stack." Ingesting the primaries ([BYOL](../../sources/byol-paper.md), [DINO](../../sources/dino-paper.md), [CPC](../../sources/cpc-paper.md), [MAE](../../sources/mae-paper.md)) shows that stack is **not one thing**: BYOL needs an asymmetric predictor *and* an EMA (either alone scores 0.2–0.3%); DINO needs an EMA *and* centering/sharpening, and BYOL's predictor does nothing for it. See [the anti-collapse lineage](../../syntheses/world-models/ssl-anti-collapse-lineage.md).
>
> Two things that reading them adds to the case here, one in each direction. **For SIGReg:** BYOL's authors state plainly that *"there is no loss such that BYOL's dynamics is a gradient descent on L jointly over θ, ξ"* — which is precisely why the loss is uninterpretable, and exactly the defect a single provable term removes. **Against the pitch, not the theorems:** BYOL's own headline claim was already **robustness to augmentation choice and batch size** (−9.1 points under colour-removal against SimCLR's −22.2; flat from batch 4096 to 256). Insensitivity-without-tuning is a 2020 claim as well as a 2025 one, and the [MarketOne](../../entities/marketone.md) bake-off puts BYOL and LeJEPA **together** on the efficient frontier.

## Carried to video: [LeVJEPA](../../entities/levjepa.md) (2026-08-27)

SIGReg's first result at video scale, and the first where its stability pitch buys **compute** rather than convenience: [LeVJEPA](../../entities/levjepa.md) (arXiv 2608.27395) trains a video encoder with an invariance loss over temporal views plus SIGReg — no EMA, no stop-gradient — and reports V-JEPA-2-comparable or better results at **5.6–20.8× less pretraining compute**, largely from random token dropping. Zero-shot segmentation emerges from PCA over patch embeddings, with no segmentation supervision.

## Where to put SIGReg in a *temporal* model — an open question with four candidate answers

The paper and this page both treat the embedding distribution as one static thing. In an action-conditioned world model there are several distributions to choose from, and the lab's own [tutorial code](../../sources/wm-booth-lejepa-lewm-tutorial-repo.md) exposes the choice as a flag with **no published comparison**:

| `sigreg_mode` | Constrains | Note |
|---|---|---|
| **`pooled`** (default) | all `(N×T)` latents as one distribution | permits the time-marginal to be isotropic Gaussian while individual timesteps are not |
| `per_time` | one SIGReg per timestep, averaged | stricter; the per-step distribution must itself be Gaussian |
| `both` | mean of the two | |
| `pooled_pred` | pooled over encoded latents **and** the predicted rollout | the only mode constraining the **predictor's own output** — where rollout collapse would surface |

Given that open-loop degradation from 25 → 75 steps is the standing failure ([VISReg](#visreg--decomposing-the-regularizer-2026-09-01) above; [stable-worldmodel](../../sources/stable-worldmodel-paper.md)), the fact that the default mode is the one *not* constraining the predictor's outputs is at least worth an experiment.

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
- [galilai-group/lejepa](../../sources/lejepa-github.md) — **the reference implementation**; the test family, the VICReg relationship, the quadrature trick.
- [galilai-group/tutorial](../../sources/wm-booth-lejepa-lewm-tutorial-repo.md) — a 60-line LeWM and the four temporal SIGReg modes.
- [Third World Modeling Workshop — Day 2](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — VISReg, the scale/shape/centre decomposition.
- [BYOL paper (Grill et al., 2020)](../../sources/byol-paper.md) · [DINO paper (Caron et al., 2021)](../../sources/dino-paper.md) — the two heuristic stacks SIGReg replaces, read from their primaries.
- [MAE paper (He et al., 2021)](../../sources/mae-paper.md) — the reconstruction alternative that needs no anti-collapse term, and rejects linear probing as the metric.
- [Third World Modeling Workshop — Day 3](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — **its author teaching it**: the DINO instability case, the cross-GPU seeding gotcha, 50 architectures out of the box, the detached-decoder rule, the SIGReg+IDM argument, and a hackathon ablation where Gaussian beat Laplace and Student-t.
