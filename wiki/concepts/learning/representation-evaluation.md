---
title: Representation evaluation (k-NN, linear, MLP, fine-tuning, RankMe)
type: concept
created: 2026-09-03
updated: 2026-09-03
sources: 1
tags: [evaluation, linear-probing, knn, fine-tuning, rankme, dimensional-collapse, effective-rank, ssl, model-selection, label-free]
---

**Representation evaluation** — how you decide whether a self-supervised encoder learned anything useful, given that its training loss is not comparable across methods and its downstream task may not exist yet. The wiki needed this page because a **live dispute on [JEPA](../world-models/jepa.md), [MAE](../../entities/mae.md) and [the anti-collapse lineage](../../syntheses/world-models/ssl-anti-collapse-lineage.md) turns entirely on which protocol you believe**, and because the label-free option that would settle a lot of it has existed since 2022 and is not in use here.

Primary source: [A Cookbook of Self-Supervised Learning](../../sources/ssl-cookbook.md) §3.7.

## The four protocols that use labels

Ranked by cost, and they do **not** agree with each other.

| Protocol | What it does | Cost | Notes |
|---|---|---|---|
| **k-NN** | freeze features, classify by weighted nearest-neighbour vote | trivial | No hyperparameters to tune, no domain adaptation. [DINO](../../entities/dino.md) weights votes by `exp(xᵀx′/T)`. Its **78.3%** ImageNet k-NN is the result that made frozen features credible |
| **Linear probe** | one linear layer on frozen features | cheap | The default for a decade. Low discriminative power *by design*, so it reflects the representation. Can run **online** during pretraining |
| **MLP probe** | 2–3 layer head on frozen features | cheap | Rarely reported. Reveals information that is present but not linearly accessible |
| **Full fine-tuning** | retrain everything | very expensive | Re-introduced as the headline metric by [MAE](../../sources/mae-paper.md) |

Two practical findings worth knowing before running any of them:

- **An online linear probe tracks the offline one closely and never overfits** ([Cookbook](../../sources/ssl-cookbook.md) Fig. 13). It reuses the pretraining forward pass, so it is nearly free — which retroactively justifies the detached online probe in the [Booth tutorial code](../../sources/wm-booth-lejepa-lewm-tutorial-repo.md).
- **MLP probes *do* overfit.** *"The best MLP head might not be the ones you get after 100 epochs."* Non-linear probing needs early stopping, which is a caveat on both sides of the dispute below.

## The dispute, stated precisely

> [!warning] Linear probing and fine-tuning are uncorrelated, and the field split on what to do about it
> **[MAE](../../sources/mae-paper.md)'s position (2021):** linear probing *"misses the opportunity of pursuing strong but non-linear features."* Its evidence is **partial fine-tuning** — tuning **one** transformer block takes ViT-L from **73.5 → 81.0**, and MAE beats MoCo v3 at every partial-fine-tuning depth *despite MoCo v3's higher linear probe*.
>
> **[Balestriero's position (2026)](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md):** two autoencoders with identical train *and* test MSE differ by ~20 points of downstream accuracy **under linear and nonlinear probes alike** — so reconstruction loss carries no information about representation quality, and the probe is the right instrument.
>
> **What the [Cookbook](../../sources/ssl-cookbook.md) records (2023), with Balestriero as first author:** the field went MAE's way. *"The majority of works that followed focused on this type of evaluation (and sometimes do not report linear/MLP results). It has been shown that contrastive methods show inferior performance than masked image modeling with regards to fine-tuning, because they are **less 'optimization friendly'**."*
>
> Nothing in this wiki bridges the 2023 survey and the 2026 tutorial. Treat "which probe" as **an open methodological question with a stated field consensus that one of its participants later argued against**, not as settled either way.

## Evaluation without labels

The part the wiki was missing, and the reason to read the Cookbook.

### RankMe — effective rank as a model-selection signal

**RankMe** (Garrido et al. 2022) is the exponentiated entropy of the embeddings' singular-value distribution:

`RankMe(Z) = exp(−Σₖ pₖ log pₖ)`,  `pₖ = σₖ(Z) / ‖σ(Z)‖₁ + ε`

**No labels, no optimization, no hyperparameters.** Against an ImageNet-labelled oracle for hyperparameter selection across VICReg / SimCLR / DINO, on ImageNet and a 10-dataset OOD average, it recovers essentially all of the oracle's selection quality — e.g. DINO teacher-temperature: oracle **72.3**, RankMe **72.2**; SimCLR temperature: oracle 68.5, RankMe 67.1, α-ReQ 63.5.

Its limits are stated by the source and matter:

- **Full rank is necessary, not sufficient.** A random Gaussian matrix is full-rank and useless.
- **It selects hyperparameters within a method; it does not rank methods against each other.**

### Dimensional collapse

The failure mode between "collapsed" and "fine": the embedding is **rank-deficient**, with information duplicated across dimensions. Distinct from the total collapse the [anti-collapse mechanisms](../world-models/jepa.md#common-training-challenges) prevent — a model can train stably, post a reasonable loss, and still be quietly using a fraction of its dimensions.

The finding that localizes it: **dimensional collapse occurs after the projector, not before it**, at different severities for DINO, SimCLR and VICReg ([Cookbook](../../sources/ssl-cookbook.md) Fig. 9). Several works find it a **good proxy for downstream performance**. Measures: singular-value entropy (RankMe), classical rank estimators, power-law fits to the spectrum, spectrum AUC. Alternative label-free metric: **α-ReQ**, from the eigenspectrum decay of representations *before* the projector.

## Why this matters outside vision

Three places the wiki has already run into this without the vocabulary:

1. **[Balestriero asked the question on Day 3 and called it open](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md)** — *"how can you assess if you learned a good Z without having to reconstruct?"* His own answer was a **detached online decoder** for visual inspection, plus probing `Z` for known object properties. RankMe is a quantitative answer that predates the question by four years.
2. **The [LeJEPA repo claims 94%+ Spearman correlation between training loss and downstream performance](../../sources/lejepa-github.md)** — "model selection without labeled validation data" — with no plot or protocol. That is the same claim RankMe makes by a different route, and the two have never been compared here.
3. **A hackathon participant reinvented a version of it in 45 minutes.** The ["representation half-life"](../../entities/market-jepa.md) — how long latent neighbours stay predictive against matched random controls — is label-free, decoder-free and planner-free, like RankMe, but measures *temporal* rather than *spectral* structure. Whether they agree is untested.

In robotics the argument for label-free evaluation is stronger than in vision, because there the labelled validation set is a **[real-robot rollout](../robotics/robot-policy-evaluation.md)** — slow, expensive, and noisy enough that [Balestriero warns against using it as a research signal](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) at all.

## Related concepts

- [World-model evaluation](../world-models/world-model-evaluation.md) — the same problem one level up: judging a *dynamics* model rather than an encoder.
- [Robot policy evaluation](../robotics/robot-policy-evaluation.md) — where the labelled validation set is a physical rollout.
- [SIGReg](../world-models/sigreg.md) — whose diagnostic (SIGReg loss falling alongside prediction loss) is a hand-rolled version of the same idea.
- [Contrastive learning and InfoNCE](contrastive-learning.md) · [spectral theory of SSL](spectral-theory-of-ssl.md) — the spectrum these metrics read is the same one the spectral framework predicts.

## Mentioned in

- [A Cookbook of Self-Supervised Learning](../../sources/ssl-cookbook.md) — **the primary**; §3.7, plus §2.6.2 on dimensional collapse.
- [MAE paper (He et al., 2021)](../../sources/mae-paper.md) — the partial-fine-tuning argument.
- [DINO paper (Caron et al., 2021)](../../sources/dino-paper.md) — the k-NN protocol and the result that made it credible.
- [Third World Modeling Workshop — Day 3](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — the question restated as open, and the decoder-based practical answer.
