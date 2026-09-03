---
title: Ralph Koijen
type: entity
subtype: person
created: 2026-09-02
updated: 2026-09-02
sources: 1
tags: [person, koijen, chicago-booth, finance, asset-embeddings, demand-system, representation-learning, transformers, holdings-data]
---

**Ralph Koijen** — **AQR Capital Management Distinguished Service Professor of Finance and Applied AI at [Chicago Booth](../sources/chicago-booth-world-modeling-workshop-2026-day2.md)**, and Director of Advanced Research at LSV. Keynote at Day 2 of the 2026 world-modeling workshop, *"Learning Representations of Assets and Investors with Applications to Financial Markets"* (joint with Xavier Gabaix, Rob Richmond and Motohiro Yogo).

Known in finance for the **asset demand system** programme — modelling prices as the market-clearing outcome of investors' portfolio choices, rather than as a function of firm characteristics directly. His contribution to this wiki is the bridge from that programme to representation learning: see [asset embeddings](../concepts/economics/asset-embeddings.md).

## The two claims

**1. Holdings data are sufficient.** Substituting market-clearing prices back into demand gives a *reduced-form demand system* in which observed holdings already reflect every characteristic that matters for pricing. Therefore *"if you want to start learning representations of financial assets, then holdings data contain all the information that's relevant for prices."*

**2. Portfolios are sentences.** Mask a position in an investor's portfolio and predict it from the rest; rotate the matrix and mask investors in a firm's ownership list to get investor embeddings. Off-the-shelf architectures, applied to holdings rather than text, take masked-holdings prediction from **~20% of variation (observed characteristics, and linear recommender systems) to ~60% (BERT-style transformer)**.

## Findings worth keeping

- **Text embeddings cannot explain holdings**, and neither can 150 standard accounting/asset-pricing characteristics. He reports AI labs telling him not to bother because their firm embeddings already contain everything; the data says otherwise.
- **Rank beats weight** — whether a stock is held and where it ranks carries almost all the information; the exact percentage adds little.
- **Investor similarity is cleaner than firm similarity.** Nearest neighbours of a small-cap value ETF are all small-cap value funds; nearest neighbours of an arbitrage fund are all special-situations funds. Firm similarity is harder to eyeball because covariances matter, not just sectors.
- **Credit application**: embeddings explain yield dispersion *within* rating buckets and predict IG→junk downgrades; re-rating insurers on them would shift required equity by **~16 percentage points** on average while preserving rating stability.

## The question he asked the room and did not get answered

Counterfactuals need **elasticities**, not just demand prediction: for every forced seller there is a buyer, so you must know how far prices move to clear. *"I would love to know if there's a JEPA-style equivalent to that."* No world-model architecture in this wiki represents an equilibrium response.

## Related
- [Asset embeddings](../concepts/economics/asset-embeddings.md) — the concept page.
- [World models for financial markets](../syntheses/society/world-models-for-financial-markets.md).
- [Distributed representations](../concepts/learning/distributed-representations.md) — the word2vec lineage he transplants.

## Mentioned in
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — keynote.
