---
title: Asset & investor embeddings (portfolios as sentences)
type: concept
created: 2026-09-02
updated: 2026-09-02
sources: 1
tags: [asset-embeddings, investor-embeddings, holdings-data, demand-system, representation-learning, word2vec, transformers, masked-modeling, finance]
---

**Asset embeddings** are learned vector representations of firms, recovered from **portfolio holdings** rather than from accounting data or price histories. **Investor embeddings** are the dual, recovered by transposing the same matrix. Developed by [Ralph Koijen](../../entities/ralph-koijen.md) with Xavier Gabaix, Rob Richmond and Motohiro Yogo; presented at [Day 2 of the Chicago Booth world-modeling workshop](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md).

The idea in one line: **treat a portfolio the way NLP treats a sentence.**

## Why holdings, and not something else

The traditional representation of a firm in finance is a hand-chosen characteristic vector — industry code plus ~150 accounting and asset-pricing features. Two known problems: standardized accounting data misses what matters *when the environment changes* (which firms are exposed to remote work, or to AI displacement), and for **investors** the observed characteristics are so thin — institution type, fund size, turnover — that they explain very little of portfolio choice.

The theoretical argument for holdings is short and general. Investors choose portfolios given prices and characteristics; supply is fixed by issuance; markets clear, so prices become a function of the characteristics. **Substitute prices back into demand** and you get the *reduced-form demand system* — holdings alone, already reflecting everything that matters for pricing.

> *"If you want to start learning representations of financial assets, then holdings data contain all the information that's relevant for prices."*

The result is architecture-agnostic; what changes with the demand model is *which method* efficiently extracts it. Under the standard linear specification used in empirical finance — investors like expected return and dislike variance, returns follow a factor model, loadings are affine in characteristics — the demand shifter is **bilinear** (investor taste × firm representation), and the optimal estimator is exactly a **linear recommender system**.

## The ladder of methods

Evaluated on masked-holdings prediction (share of variation in what investors hold that is explained):

| Method | NLP analogue | Result |
|---|---|---|
| 150 observed characteristics | hand-crafted features | ~20% |
| Linear recommender system | matrix factorization | ~same |
| word2vec-style shallow model | mask one position, predict from the rest of the portfolio | significantly better |
| **BERT-style transformer** + contrastive fine-tune | masked asset modelling; sentence-transformer aggregation over odd/even position splits | **~60%** |

The transformer's advantage is **contextualization**, and the economic reading is exactly the polysemy argument:

> *"If I hold Apple in a portfolio with all large-cap stocks I'm going to get a different representation compared to when I hold Apple in a portfolio of all technology firms. You may think of Tesla as kind of a car company. I think of Tesla more as an AI company."*

The only architectural change needed was the **tokenizer** — stocks are the tokens.

## Findings worth carrying

- **Rank beats weight.** Information in holdings sits at three levels: *do I hold it* / *where does it rank* / *what exact percentage*. The first two carry almost everything.
- **Regularization is forced by the data.** The median investor holds only **50–60 stocks**, so higher-dimensional models overfit immediately.
- **Text embeddings cannot explain holdings**, and neither can the observed characteristics — and holdings cannot explain them either. Three partially disjoint information sets. Koijen reports AI labs telling him not to bother because their firm embeddings already contain everything; the data disagrees.
- **Investor similarity is cleaner than firm similarity.** Nearest neighbours of a small-cap value ETF are all small-cap value funds; of an arbitrage fund, all special-situations funds. Firm similarity is harder to eyeball because covariance structure matters, not just sector.
- **Dimensionality is task-dependent.** Low-dimensional holdings embeddings *underperform* observed characteristics on return co-movement; they only win at high dimension — because it is not clear which leading components correspond to expected return, risk, downside risk, or ESG preference.
- **Credit markets.** Within a rating bucket, yields vary by ~75–100 bp. Embeddings explain that dispersion, explain credit-spread volatility, and predict investment-grade→junk downgrades. Applying them to insurance regulation (while preserving rating-transition stability, so the comparison is fair) would move required equity by **~16 percentage points** on average.
- Live at **market-gen.ai**, which also uses an LLM over firm- and investor-level text to *interpret* what a given embedding neighbourhood has in common.

## The open problem: prediction is not counterfactual

The limitation Koijen states himself, and the sharpest unanswered question of the day:

> *"It's not enough to predict who's going to buy or sell, because for every buyer there's a seller. You need to know what the elasticities are — if some investor is forced to sell because they are constrained, how much do prices need to move for other investors to buy the stocks from that investor... I would love to know if there's a JEPA-style equivalent to that."*

Substituting out the price is what makes the embeddings estimable; it is also what deletes the **equilibrium response**, which is precisely what a stress test or a policy counterfactual needs. No world-model architecture in this wiki represents one.

A second gap: the estimation is done **cross-section by cross-section, with no time-series component at all** — holdings are quarterly, and *"a big question we have for all of you is if you think about world models, whether the time series dimension is even something we can do here."*

## Related concepts
- [Distributed representations](../learning/distributed-representations.md) — the word2vec lineage being transplanted.
- [World models for financial markets](../../syntheses/society/world-models-for-financial-markets.md) — the cross-talk synthesis.
- [MarketOne](../../entities/marketone.md) — the neighbouring attempt, from prices rather than holdings, with a similar prediction-vs-interpretability trade-off.
- [Collectivist AI](collectivist-ai.md) / [mechanism design](mechanism-design.md).

## Mentioned in
- [Third World Modeling Workshop — Day 2](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — Ralph Koijen keynote.
