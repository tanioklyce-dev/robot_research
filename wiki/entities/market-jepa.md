---
title: Market-JEPA
type: entity
subtype: model
created: 2026-09-03
updated: 2026-09-03
sources: 2
tags: [market-jepa, jepa, lejepa, sigreg, finance, encoder, marketone, bradford-levy, balestriero, mit-license, time-series]
---

**Market-JEPA** — a **22.3M-parameter [LeJEPA](../sources/lejepa-paper.md)-trained encoder for equity market microstructure**, released under **MIT licence** on Hugging Face by [Bradford Levy](bradford-levy.md) and [Randall Balestriero](randall-balestriero.md) with PhD student **Humzah Merchant**, and handed to the room as the substrate for the [Day 3 modeling challenge](../sources/chicago-booth-world-modeling-workshop-2026-day3.md).

## Shape

| | |
|---|---|
| Input | a **20 × 450** market-state tensor — **9 channels** of top-of-book data (bid price, ask price, bid size, ask size, volume, …) |
| Output | a **384-dimensional** embedding |
| Parameters | **22.3M** |
| Training data | **a single month of 2016**, from [MarketOne](marketone.md) / [Massive](massive.md) |
| Augmentation | **time warping only** |
| Licence | **MIT** — *"I mean, it's your checkpoint as well, Randall"* |

The compression is the pitch: a regular trading day is **23,400 seconds** across nine features — well over 100,000 numbers — reduced to 384 dimensions. Levy's framing is that this replaces a convention rather than a model: finance has always compressed the day with **open / high / low / close**, a rule chosen by tradition. *"It seems a little goofy to me… maybe we can learn a different aggregation rule"*, one that does not treat every interval identically *"when clearly not all time intervals are created equal in terms of predictivity."*

Trained on one month of 2016 and still useful on 2019–2020 data: *"the performance of it doesn't decay super fast."* Scaling studies (bigger model, more data) are in the paper, unsurprising in direction.

## What it is not

An encoder, not a world model. Asked directly whether this is *"the JEPA in action"*, Levy: *"this is purely an encoder, I would say."* The action-conditioned extension — conditioning on **events** — is described as work at the end of the paper. Same division of labour as [LeVJEPA](levjepa.md) versus [LeWM](leworldmodel.md).

## What it was shown to encode

Two independent results, hours apart, both about **what survives in the latent space**:

- **Levy's own** (via the released paper): latent structure carries **risk exposure**, and there is an identifiable **signature of spoofing** — placing orders to move other participants without intending to execute — which is one of the four challenge tasks he set.
- **A participant's, in 45 minutes** ([Janing](../sources/chicago-booth-world-modeling-workshop-2026-day3.md)): does latent proximity predict similar futures? Retrieve the 10 nearest source states to a held-out query, compare their realized returns/volatility/liquidity against random controls anchored at the same intraday time, block-bootstrap the confidence intervals. **Neighbour advantage is positive and decaying**, and **Market-JEPA beats a 32-dimensional PCA baseline** — with a proposed **"representation half-life"** as the summary statistic.

> [!note] The half-life idea is the more valuable output
> Measuring how long latent neighbours stay predictive needs **no decoder, no planner and no labels** — precisely the evaluation gap Balestriero named that same morning (*"how can you assess if you learned a good Z without having to reconstruct?"*). It happens to be tested on markets, where signal decays fast enough to see, but nothing about it is finance-specific. Presented as exploratory, with the right caveats: three horizons, one seed, PCA-32 not claimed optimal.

## The four challenge tasks it was released for

Ordered by Levy from most promising to hardest: **(1)** probe the embedding for asset risk exposure; **(2)** run an event study (COVID disclosure — Starbucks was among the first firms to warn); **(3)** detect **market manipulation / spoofing**; **(4)** find persistent predictability and trade it — deliberately last, on Grossman–Stiglitz grounds.

## Related

- [MarketOne](marketone.md) — the dataset; the Day 2 bake-off that chose the recipe.
- [Financial time-series augmentations](../concepts/economics/financial-time-series-augmentations.md) — why time warping and not random crop.
- [SIGReg](../concepts/world-models/sigreg.md) · [LeJEPA](../sources/lejepa-paper.md) — the objective.
- [Asset embeddings](../concepts/economics/asset-embeddings.md) — the neighbouring approach, from holdings rather than prices.
- [World models for financial markets](../syntheses/society/world-models-for-financial-markets.md).

## Mentioned in

- [Third World Modeling Workshop — Day 3](../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — released in Tutorial 2; used by two challenge presentations.
