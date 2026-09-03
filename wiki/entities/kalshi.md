---
title: Kalshi
type: entity
subtype: company
created: 2026-09-02
updated: 2026-09-02
sources: 1
tags: [kalshi, prediction-markets, event-contracts, calibration, brier-score, forecasting, benchmark, dataset, cftc, finance]
---

**Kalshi** — a **CFTC-regulated designated contract market** (the same regulatory category as the Chicago Mercantile Exchange), approved November 2020, operating since 2021. The world's largest prediction market: **8,000+ live events** and hundreds of thousands of live markets covering elections, macroeconomic indicators, weather, corporate KPIs, entertainment and sports.

In this wiki it is not a finance entity — it is an **evaluation surface**. Presented by **Nicole Kagan**, head of research, at [Day 2 of the Chicago Booth world-modeling workshop](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) (2026-09-01).

## The claim

> *"World models are at their core a system that takes some partially observed environment and then produces some compact updatable representation that's sufficient to predict what happens next in it. And what I want to argue today is that actually such a system already exists, at scale, and it exists **outside of any machine learning representation or neural network**."*

The mechanism: an equity price is a **compound object** (uncertain cash flows × discount rate × risk preferences × frictions), so recovering a probability from it means unwinding all of that. An **event contract** is an Arrow–Debreu security — a fixed payout on one unambiguously specified proposition — so under no-arbitrage **the price *is* the probability**, and any inconsistency is directly extractable profit. Against polling, the incentive structure differs in kind: respondents *"might tell you what they think you want to hear... What they're unlikely to tell you is what they think will actually happen."*

## The calibration study

Over **2.2 million resolved markets**, the full 2021–2026 operating history — described as the first calibration study on the complete resolved history of any US regulated exchange. Published at `kalshi.com/research`.

| Measure | Result |
|---|---|
| Brier score, 3-month horizon → close | **0.08 → 0.02** |
| Uninformative-forecaster benchmark | 0.25 |
| Reliability diagram | tracks the 45° line closely, **across categories** — a 70¢ contract resolves yes ~70% of the time |
| Calibration vs. depth | improves near-monotonically with volume and unique traders |
| **Volume threshold** | **~$10,000 at event level** already gives Brier ≈ 0.1 — *"up with the best forecasting models across fields like meteorology"* |
| Non-trading users | ~**75%** come only to read the probabilities |

The $10,000 figure is the counterintuitive one: institutions had assumed tens of millions of dollars of volume were needed before a market price could be trusted.

## Why the wiki should care

> [!note] An evaluation surface that needs no simulator
> On the same panel, [Bayan Bruss](bayan-bruss.md) argued world-model evaluation is circular without a simulator, and [Edoardo Airoldi](edoardo-airoldi.md) asked for benchmarks with known ground truth. Kalshi's resolved history is **2.2M incentive-disciplined, externally adjudicated forecasting instances with realized outcomes** — the world already ran the experiment. Kagan's explicit pitch was that this is *"a real-time, adjudicated and incentive-disciplined dataset against which forecasting competence of any learned world model is able to be directly benchmarked."* Nobody on the panel picked it up.

Two practical affordances she offered:
- **All data is free** through a public API.
- **The marginal cost of listing a contract is ~zero**, so she will list markets — including **conditional** markets (*"if this person wins, will this policy pass"*) — on researcher request. Conditional contracts are the closest thing on offer to a priced counterfactual.

## Limits to record

- Volume is dominated by sports. Kagan does not concede this is a defect — a fan tracking a team across 28 World Cups is not obviously less informed than a hedge-fund researcher on short rates — but it does mean the well-capitalized markets are not the economically load-bearing ones.
- Brier score improves with volume up to a plateau, then **declines monotonically past roughly $10,000** on the reported curve, a pattern raised from the audience and not fully explained.
- Prediction markets are **not a substitute for a learned world model**, by her own statement — they are a benchmark and an input stream.

## Related
- [Prediction markets](../concepts/economics/prediction-markets.md) — the concept page.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — the problem this partly answers.
- [World models for financial markets](../syntheses/society/world-models-for-financial-markets.md).
- [Mechanism design](../concepts/economics/mechanism-design.md) — incentive compatibility as the mechanism doing the work.

## Mentioned in
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — Finance & Markets panel.
