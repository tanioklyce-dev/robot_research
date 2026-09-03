---
title: Bayan Bruss
type: entity
subtype: person
created: 2026-09-02
updated: 2026-09-02
sources: 1
tags: [person, bruss, capital-one, consumer-finance, world-model-evaluation, back-testing, counterfactuals, reflexivity, graph-ml, benchmarks]
---

**Bayan Bruss** — applied AI research lead at **Capital One**; panelist on the Finance & Markets panel at [Day 2 of the Chicago Booth world-modeling workshop](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) (2026-09-01), on world models for **consumer** finance (retail banking, credit cards, mortgages) as distinct from the high finance the other speakers covered.

## Why he matters to this wiki

He states the **world-model evaluation circularity** more cleanly than any other source here:

> *"If I had a good world model, I could simulate the economy and I could test any policy — but how do I know if my world model is good if I don't have a simulator? And there's no way out of it."*

The route in: world-model evaluation has only two families, **reconstruction** and **task-based**. Reconstruction is not useful in his domain; task-based needs a simulator he does not have. So the field uses **back-testing** — replay history, swap in the new policy, aggregate realized outcomes — which *"assumes that the state didn't change under the new policy. But that's exactly what we're trying to ask."* His partial escape is deliberate off-policy data collection, with the sting that *"you have to have done it years ago."* See [world-model evaluation](../concepts/world-models/world-model-evaluation.md).

## His spec for a consumer-finance world model

**Two-level correctness**: accurate per-person prediction *and* recovery of known macroeconomic dynamics when individual models are aggregated. Plus horizons ML does not think in — *"a mortgage... 30 years. That is a time scale that machine learning doesn't typically think about."*

Five challenges, four of which he calls tractable:

1. **Representation** — tabular + temporal + semi-structured clickstream + unstructured documents jointly.
2. **Partial observability twice over** — you cannot see inside a person, and no single institution sees all participants.
3. **Non-stationarity with reflexivity** — *"they know that they are being modeled... and they change depending on what they think of your own beliefs about them."*
4. **Steerability** — including changing the environment's *rules*: *"how would my policy operate under a financial crisis?"*
5. **Evaluation** — *"the hardest problem here."*

Plus the **time-travel problem**: *"very very subtle choices you make in how you do the evaluation end up vastly inflating what you think the quality of your decisions are."*

## Also on record

- On money: *"a system of mutual trust... a complete figment of our collective imaginations,"* created from nothing whenever a bank makes a loan.
- On benchmarks: no ImageNet exists for this domain. His team released **PersonalLedger** — NVIDIA's 100,000 census-matched personas expanded by an LLM into grounded transaction histories — and found **longitudinal fidelity of the synthetic generation was the hard part**. Standing offer to the research community: *"I will tell you what the benchmark needs to have if it's going to unlock more research."*
- On graph ML: relational models help *"where the signal is heavily relational, which tends to be in fraud"*; where the signal is a person's own behavior over time, sequence models win.
- On monitoring: *"the only thing you can fully count on is that an assumption you made will turn out to be wrong"* — and *"the real trick is to not be so wrong that it's your last trade or your last loan."*

## Related
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — the circularity.
- [World models for financial markets](../syntheses/society/world-models-for-financial-markets.md).
- [Kalshi](kalshi.md) — the evaluation surface offered on the same panel that would partly answer him.

## Mentioned in
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — Finance & Markets panel.
