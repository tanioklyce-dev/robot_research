---
title: MarketOne
type: entity
subtype: dataset
created: 2026-09-02
updated: 2026-09-03
sources: 3
tags: [marketone, dataset, finance, self-supervised, lejepa, byol, scaling, chicago-booth, balestriero, benchmark, massive, market-jepa]
---

**MarketOne** — a permissively licensed dataset of **top-of-book aggregates and trade data for all US equities, 2008–2025: nearly one trillion observations**. Released in partnership with **Massive** (formerly Polygon) by **Humzah Merchant** with [Randall Balestriero](randall-balestriero.md) and Bradford Levy (Chicago Booth / Brown), presented as a lightning talk at [Day 2 of the Chicago Booth world-modeling workshop](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) (2026-09-01).

Motivation is a data-infrastructure complaint: financial ML datasets are *"extremely scattered"* — different periods, different frequencies, mostly daily or lower, often private, often carrying survivorship or look-ahead bias.

## The bake-off result

18 combinations of self-supervised objective ([LeJEPA](../sources/lejepa-paper.md), DINO, BYOL) and augmentation (time warping, same-stock crops, cross-stock same-time pairs) plus supervised baselines, ranked on three prediction tasks (change in return, volatility, spread — spread as a proxy for trading cost) and several **latent-organization** tasks (does it cluster by firm? by time? does it recover the statistical factor structure?).

> [!note] The finding is a trade-off, not a winner
> The three prediction tasks are **highly correlated with each other and negatively correlated with the economic-organization tasks** (one pair at ≈ −0.35). Some encoders learn representations useful for forecasting; others learn representations that are *economically meaningful*; these are largely different objectives.
>
> - **Pure forecasting** → multi-head supervised training on all three tasks with gradient normalization.
> - **Economically meaningful latent structure** → the **LeJEPA** setup, best in class.
> - **Efficient frontier between them** → LeJEPA and BYOL, both with time-warping augmentation.
> - **Generalist vs. specialist**: BYOL ranks ~4th on every task; same-stock crops is best at one task and worst at all others.

## Methodological point worth copying

**Regime shifts across the sample are large enough to invalidate single-period evaluation.** A single encoder trained across all months shows visible regime structure over time, and *"if you were to naively choose to only evaluate say on the last year of data 2023–2024 you get a very biased estimate of how this encoder performs."* Their protocol samples **32 random months** across the sample to span market regimes. Compare the wiki's [world-model evaluation](../concepts/world-models/world-model-evaluation.md) concerns about benchmark period selection.

## Day 3: the encoder shipped, and the dataset was handed to a room

[Day 3](../sources/chicago-booth-world-modeling-workshop-2026-day3.md) turns MarketOne from a bake-off result into a distributed artifact. Three things it settles:

- **[Market-JEPA](market-jepa.md) is public.** A **22.3M-parameter** encoder — 20×450 market-state tensor (9 top-of-book channels) → **384-dimensional** embedding, trained on **a single month of 2016**, **MIT licensed**, on Hugging Face, with the sample data **streamed rather than downloaded** (a few gigabytes, a few partitions, ~30 seconds). *"The performance of it doesn't decay super fast"* years out of sample.
- **The winning augmentation is time warping, and only time warping.** The shipped checkpoint uses it alone — see [financial time-series augmentations](../concepts/economics/financial-time-series-augmentations.md) for the derivation of why cross-stock is the *principled* choice and random resized crop provably cannot learn factor structure.
- **[Massive](massive.md) is a SIP-direct source**, not a reseller: UTP/CTA for equities, **OPRA** for options, plus a CME futures partnership. Presented by Steve Bravo, previously of OPRA. **Licensing terms for MarketOne itself were not stated** in either talk; the checkpoint is MIT.

Levy's own framing of what the encoder replaces is the part that generalizes: a trading day is **23,400 seconds**, and finance has always compressed it with **open/high/low/close** — a convention nobody chose on evidence. *"Maybe we can learn a different aggregation rule"*, one that does not treat every interval identically *"when clearly not all time intervals are created equal in terms of predictivity."*

Four challenge tasks were set on it, ordered most-promising to hardest: **risk-exposure probing**, an **event study** (COVID disclosure), **spoofing detection** (their paper reports an identifiable manipulation signature), and **return prediction** — deliberately last, on Grossman–Stiglitz grounds.

## Related
- [Asset embeddings](../concepts/economics/asset-embeddings.md) — the neighbouring representation-learning attempt, from holdings rather than prices.
- [World models for financial markets](../syntheses/society/world-models-for-financial-markets.md).
- [SIGReg](../concepts/world-models/sigreg.md) / [LeJEPA](../sources/lejepa-paper.md) — the objective that wins the interpretability half.
- [Market-JEPA](market-jepa.md) — the released encoder trained on it.
- [Massive](massive.md) — the data partner.
- [Financial time-series augmentations](../concepts/economics/financial-time-series-augmentations.md) — why time warping and not random crop.

## Mentioned in
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — lightning talk, session 3.
- [Third World Modeling Workshop — Day 3](../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — the encoder released and the challenge run on it; two participant results probing what the latent space retains.
