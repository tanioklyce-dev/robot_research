---
title: MarketOne
type: entity
subtype: dataset
created: 2026-09-02
updated: 2026-09-02
sources: 2
tags: [marketone, dataset, finance, self-supervised, lejepa, byol, scaling, chicago-booth, balestriero, benchmark]
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

> [!note] Massive presented separately on Day 3
> The data partner has its own slot in the workshop programme — **Day 3, 11:00–11:20am, *"Institutional-Grade Market Data,"* Steve Bravo, Massive.** Not ingested; the Day 3 stream had no captions as of 2026-09-02. If the dataset's provenance and licensing terms ever become load-bearing, that is the talk to find.

## Related
- [Asset embeddings](../concepts/economics/asset-embeddings.md) — the neighbouring representation-learning attempt, from holdings rather than prices.
- [World models for financial markets](../syntheses/society/world-models-for-financial-markets.md).
- [SIGReg](../concepts/world-models/sigreg.md) / [LeJEPA](../sources/lejepa-paper.md) — the objective that wins the interpretability half.

## Mentioned in
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — lightning talk, session 3.
