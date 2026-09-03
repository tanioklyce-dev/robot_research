---
title: Financial time-series augmentations
type: concept
created: 2026-09-03
updated: 2026-09-03
sources: 2
tags: [augmentation, self-supervised, jepa, lejepa, finance, market-microstructure, factor-model, invariance, time-warping, marketone, market-jepa]
---

**Financial time-series augmentations** — the design problem of saying what *"two views of the same thing"* means when the thing is a limit order book, so that a [JEPA](../world-models/jepa.md)-style invariance loss has something to be invariant to.

In vision this question is settled by convention: crop, flip, colour-jitter, solarize. Nobody derives them; they work. **In markets there is no convention, and the wrong choice provably cannot learn what you want** — which makes this the clearest worked example in the wiki of *deriving* an augmentation from the structure of the domain instead of copying one. The material is [Bradford Levy](../../entities/bradford-levy.md)'s [Day 3 tutorial](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md), with the empirical ranking from the [MarketOne](../../entities/marketone.md) bake-off the day before.

## The target: latent factor structure

Standard asset pricing writes a return as `r = βᵀf + ε` — asset-specific **loadings** `β` on a small set of **latent risk factors** `f`, plus noise. The factors are stochastic and time-specific; the loadings are properties of the asset. Most of the field's factors ([CAPM](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md)'s market factor, Fama–French size and value, momentum) were **hypothesized and then tested**, and Levy is blunt that the micro-foundations are thin: *"there aren't necessarily super super strong micro-foundations for why those would exist."*

So the SSL pitch is: **learn `f` from data instead of guessing it.** Everything below follows from asking whether a given augmentation *can* let that happen.

## The derivation that kills the obvious choice

**Random resized crop** is the vision default: take two crops of one series, rescale, call them the same thing.

It cannot work, and the argument is two lines. The crops come from **different time periods**. Under the factor model the factor realizations at those two times are *different draws*. So whatever invariance the encoder learns must be **time-independent** — and the latent factor structure is, by construction, exactly the time-dependent part.

What it *does* learn is real but unwanted: time-stable characteristics of the asset — typical bid-ask spread, typical order-size distribution. Levy's account of finding this is worth keeping as a research anecdote:

> *"Indeed, while we were messing around with it we saw this sort of — it's sort of obvious ex post — oh, of course you're not going to be able to learn a latent factor structure this way."*

## The fix, and the surprise

| Augmentation | Construction | Verdict |
|---|---|---|
| **Random resized crop** | Two crops of one stock's series, different times | **Cannot learn factors** — invariance is forced to be time-independent. Learns spread/size characteristics instead |
| **Cross-stock** | **Same time window**, two different tickers (e.g. Apple and NVIDIA at 10:00–11:45 Tuesday) | **The principled fix.** Whatever is common to both at that instant *is* a common factor, so the invariance loss can carry factor structure |
| **Time warping** | Same window, same stock, but the **clock runs faster or slower through the day** — squeeze and stretch | **Won on return prediction**, against expectation. Interpretability suggests it pushes the model **toward volume** and smooths price noise. The shipped [Market-JEPA](../../entities/market-jepa.md) uses this alone |
| **Gaussian noise on prices** | Add noise to the series | **Naive and mostly wrong.** If perturbed bid and ask cross, you have created a **locked book** — a state where two participants should have traded and did not. It destroys the defining structure of a market |
| **Volume noise** | Same, applied to sizes | Weaker version of the same objection |
| **Price jitter** | Deliberately gentler than Gaussian noise | Compromise attempt |
| **Channel dropout** | Drop whole feature channels (price, size, …) — the analogue of dropping RGB planes | Sound; stops the model leaning on a single channel for the invariance |

> [!note] The time-warping result is the one to be suspicious of, and Levy says so first
> He expected it to fail: markets have *"some economic structure even though it's noisy"* — orders are submitted when they are submitted, for reasons — and warping the clock ought to destroy that. It won anyway, **measured on return prediction specifically**, and he is explicit that he has not checked other downstream tasks: *"perhaps it is tilting it toward one thing or another."* Read the result as *time warping is good for return prediction*, not as *time warping is good*.

## The augmentation nobody has built yet: tick time

Raised by a high-frequency practitioner in the room and immediately adopted by Levy as the interesting next one. Clock time in markets is mostly empty — the overnight and pre-market stretches contain nothing. **Tick time** advances only when something actually happens (a trade, a change in the order book), so it is time reparameterized by *events* rather than by seconds.

Which makes it a **principled** version of time warping rather than an arbitrary one — the same squeeze-and-stretch, with the warp determined by market activity instead of a drift process. Levy confirms the shipped warp is *"purely a drift process right now."*

> [!note] This generalizes past finance, and the wiki has the other half
> Reparameterizing a sequence by "when something happened" instead of by clock ticks is exactly what [EAWM](../../sources/eawm-paper.md) does in a Dreamer-style world model, segmenting on **events** rather than frames and reporting +10–45%. Two independent domains arriving at the same reparameterization is a stronger signal than either alone — and neither, as far as this wiki records, cites the other.

## Why a robotics wiki holds this page

Because the reasoning transfers and the augmentations do not. The template is:

1. **Write down what you want the latent to encode** (here, `f`).
2. **Ask what invariance each candidate augmentation forces.**
3. **Discard the ones whose invariance is provably orthogonal to the target** — before running anything.

Robot learning uses vision augmentations by inheritance, on data where the equivalent question is rarely asked. What does colour jitter force a manipulation policy's latent to be invariant to, and is that invariance compatible with the task? [Balestriero](../../entities/randall-balestriero.md) makes the general version of the point in the same day's tutorial: *"as soon as you say you want to be invariant to something, someone can come and say, well, I can design a downstream task that lives exactly in this invariant subspace and for which you will have random performance."* The craft is choosing which tasks to sacrifice.

## Related concepts

- [Asset embeddings](asset-embeddings.md) — the other route to a learned representation of an asset, from **holdings** rather than prices.
- [JEPA](../world-models/jepa.md) · [SIGReg](../world-models/sigreg.md) — the objective these augmentations feed.
- [Spectral theory of SSL](../learning/spectral-theory-of-ssl.md) — the frame in which "choose an augmentation" becomes "choose a graph over samples."
- [Time-series foundation models](../learning/time-series-foundation-models.md) — the alternative approach these are competing with.
- [Generative data augmentation](../learning/generative-data-augmentation.md) — augmentation by synthesis rather than by transformation.

## Mentioned in

- [Third World Modeling Workshop — Day 3](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — **the primary**; Levy's tutorial, with the derivation and the whole list.
- [Third World Modeling Workshop — Day 2](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — the [MarketOne](../../entities/marketone.md) bake-off ranking time warping, same-stock crops and cross-stock pairs against each other across 18 objective × augmentation combinations.
