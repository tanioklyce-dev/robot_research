---
title: Prediction markets as calibrated world models
type: concept
created: 2026-09-02
updated: 2026-09-02
sources: 1
tags: [prediction-markets, event-contracts, arrow-debreu, calibration, brier-score, forecasting, incentive-compatibility, world-model-evaluation, kalshi]
---

**A prediction market** trades **event contracts** — Arrow–Debreu securities that pay a fixed amount if one unambiguously specified proposition resolves true and nothing otherwise. Under no-arbitrage the **price is a probability by construction**, not a quantity you must decode from a price.

The claim that puts this page in a world-models wiki, from [Kalshi](../../entities/kalshi.md)'s head of research at [Day 2 of the Chicago Booth workshop](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md):

> *"World models are at their core a system that takes some partially observed environment and then produces some compact updatable representation that's sufficient to predict what happens next in it. And what I want to argue today is that actually such a system already exists, at scale, and it exists **outside of any machine learning representation or neural network**."*

## Why a stock price is not a probability and an event contract is

A share price is a **compound object**: a claim on uncertain future cash flows, discounted by a rate reflecting risk preferences, time value and assorted frictions, all bundled. Recovering a clean probability for any single proposition means unwinding all of that, and the components shift over time.

An event contract collapses that. *"It's difficult to know if Tesla's share price should be $500 or $600. It's difficult to know what a somewhat arbitrary PE multiple should be. What is less difficult to know is what a Fed decision should be next month."*

## Two mechanisms make it work

1. **Arbitrage as an error-correcting force.** If a market's implied probability is inconsistent with a logically related market's, the inconsistency is *extractable profit* — so someone is paid to collapse it. Calibration is enforced by a bound that is not a loss function.
2. **Incentive compatibility against polling.** A poll respondent *"might tell you what they think you want to hear or what they idealistically would love to happen. What they're unlikely to tell you is what they think will actually happen."* Under proper scoring rules, misreporting your belief is costly. See [mechanism design](mechanism-design.md).

## The calibration evidence

From a study over **2.2 million resolved markets** spanning 2021–2026 — the full operating history of a CFTC-regulated exchange, and described as the first such study on any US regulated exchange:

| Measure | Result |
|---|---|
| Brier score, 3-month horizon → market close | **0.08 → 0.02** |
| Uninformative-forecaster benchmark | 0.25 |
| Reliability diagram | tracks the 45° line closely, across categories |
| Depth effect | calibration improves near-monotonically with volume and unique traders |
| **Volume threshold** | **~$10,000 at the event level** → Brier ≈ 0.1, comparable to the best forecasting models in fields like meteorology |

The threshold is the surprise. Institutions had assumed tens of millions of dollars of volume were required before a market price could be trusted; the curve plateaus four orders of magnitude earlier.

Categories reveal information at different times, which is itself usable: macroeconomic outcomes are discussed and priced well in advance, while *"what somebody might say in a speech"* resolves close to or during the event.

## Why this is an evaluation instrument, not just a data feed

> [!note] It answers a problem posed on the same panel and nobody connected them
> [Bayan Bruss](../../entities/bayan-bruss.md) argued world-model evaluation is circular: you need a simulator to test a policy, and you need a world model to have a simulator. [Edoardo Airoldi](../../entities/edoardo-airoldi.md) asked for benchmarks with known ground truth, proposing to manufacture it in agent-based simulators.
>
> A resolved prediction market needs neither. It is a **forecast with a realized outcome, adjudicated externally, made by participants who paid to be right** — the world already ran the experiment. 2.2M of them, free through a public API. Any learned world model that emits probabilities over near-term real-world events can be scored against this directly.
>
> As far as this wiki knows, **nobody has done it.** See [world-model evaluation](../world-models/world-model-evaluation.md).

Two further affordances offered explicitly to researchers: the marginal cost of listing a contract is ~zero, so markets can be listed **on request**; and **conditional** markets (*"if this person wins, will this policy pass"*) are the closest thing available to a **priced counterfactual** — a probabilistic estimate of a state of the world that did not happen, elicited from people with money on it rather than from a survey.

## Limits

- **Volume concentrates in sports**, so the deepest and best-calibrated markets are not the economically load-bearing ones. Kagan declines to treat this as a defect — a fan who has followed a team across 28 World Cups is not obviously less informed than a hedge-fund researcher on short rates — but for a benchmark builder it constrains coverage.
- The reported Brier-vs-volume curve **declines monotonically past roughly $10,000**, raised from the audience and not fully explained.
- **Not a substitute for a learned world model**, by the presenter's own statement. It produces calibrated marginals over pre-specified propositions; it does not produce a state representation you can plan in, and it can only answer questions someone thought to list.
- It is a market, so it inherits the reflexivity every other market has: a widely-read probability may change the outcome it prices. Anecdotally reported to lead polling on political momentum.

## Related concepts
- [Mechanism design](mechanism-design.md) — incentive compatibility and proper scoring rules are what make the price informative.
- [World-model evaluation](../world-models/world-model-evaluation.md) — the problem this is an instrument for.
- [Collectivist AI](collectivist-ai.md) — markets as computation over dispersed private information.
- [Prediction-powered inference](prediction-powered-inference.md) — the other place this wiki treats a market-like incentive as a statistical guarantee.

## Mentioned in
- [Third World Modeling Workshop — Day 2](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — Nicole Kagan, Finance & Markets panel.
