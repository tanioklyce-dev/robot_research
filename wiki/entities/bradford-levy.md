---
title: Bradford Levy
type: entity
subtype: person
created: 2026-09-03
updated: 2026-09-03
sources: 1
tags: [person, bradford-levy, chicago-booth, finance, accounting, applied-ai, marketone, market-jepa, self-supervised, time-series, workshop-organizer]
---

**Bradford Levy** — Assistant Professor of **Accounting and Applied AI** at the University of Chicago Booth School of Business; co-organizer of the [World Modeling Workshop](../sources/chicago-booth-world-modeling-workshop-2026.md) with [Randall Balestriero](randall-balestriero.md), [Kawin Ethayarajh](kawin-ethayarajh.md) and XY Han. An engineer before he was an economist — *"I made the questionable decision of getting a PhD in an econ field… and as a result was forced to learn the lingo of economics. I saw a lot of basically common math but different English words around that math."*

In this wiki he is the person **carrying [JEPA](../concepts/world-models/jepa.md) machinery into markets** and reporting honestly about where it does not fit. He is a co-author on [MarketOne](marketone.md) and the releaser of [Market-JEPA](market-jepa.md); his PhD student **Humzah Merchant** presented the dataset bake-off on Day 2.

## The translation work

His [Day 3 tutorial](../sources/chicago-booth-world-modeling-workshop-2026-day3.md) is the wiki's clearest bridge between the two vocabularies, and it turns on one measurement and two theorems.

**The measurement.** Push consecutive periods of a time series through a [time-series foundation model](../concepts/learning/time-series-foundation-models.md), extract representations, estimate **mutual information** between them (SMILE estimator), and repeat across domains. Electricity demand, weather, traffic and dynamical systems come out high; **finance comes out markedly lower than all of them, and non-zero.** Prompted by XY Han asking *"surely we can empirically measure this, right?"*

**The two results that explain it.** *Rational expectations equilibrium* — after trading, price is a sufficient statistic for the private signals, so the ex-post value of your signal is nil. *Grossman–Stiglitz (1980)* — but information is costly, so only a fraction of agents become informed, so price **cannot** fully reveal, and the market is **"efficiently inefficient."** Predictability lives in pockets (post-earnings-announcement drift is his most robust example); *"this is what people mean when they say financial data are noisy"* — strong-signal periods are rare, not absent.

**The image that lands it**, and the reason this page matters to a robotics wiki:

> *"Imagine if the friction coefficient in [Push-T] was adversarially changing to try to mess with the robot. That's more of the type of environment that we're dealing with in financial markets."*

## The methodological contribution

Two things he says that generalize past finance:

- **[Financial time-series augmentations](../concepts/economics/financial-time-series-augmentations.md).** He does not present augmentations as a list of tricks; he derives from the factor model *which ones cannot possibly work*. Random resized crop draws its two views from different time periods, so the learned invariance must be time-independent and therefore **cannot be the latent factor structure**. Cross-stock sampling (same window, different tickers) fixes it. **Time warping won on return prediction and he expected it to lose.**
- **Aggregation is a learnable choice.** A trading day is 23,400 seconds and finance has always compressed it with open/high/low/close — a convention nobody chose on evidence. *"It seems a little goofy to me… maybe we can learn a different aggregation rule"*, one that is not identical across intervals *"when clearly not all time intervals are created equal in terms of predictivity."* This is the [SSL](../concepts/learning/spectral-theory-of-ssl.md) argument aimed at a 60-year-old convention.

He is also candid about the reflexive objection to his own release: asked whether a public checkpoint destroys the edge it finds, he answers with Grossman–Stiglitz rather than a denial — the market gets more efficient, never perfectly efficient, because *"you've got to run this on a GPU, you've got to purchase the data."*

## Related

- [Market-JEPA](market-jepa.md) — the released encoder.
- [MarketOne](marketone.md) — the dataset.
- [Massive](massive.md) — the data partner, *"since back when they were called Polygon."*
- [World models for financial markets](../syntheses/society/world-models-for-financial-markets.md) — the wiki's synthesis his material feeds.
- [Randall Balestriero](randall-balestriero.md) · [Kawin Ethayarajh](kawin-ethayarajh.md) — co-organizers.

## Mentioned in

- [Third World Modeling Workshop — Day 3](../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — Tutorial 2, *Financial Data: Challenges, Evaluation, and Training*.
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — organizer; co-author on the MarketOne lightning talk.
- [Third World Modeling Workshop, Chicago Booth 2026](../sources/chicago-booth-world-modeling-workshop-2026.md) — organizer.
