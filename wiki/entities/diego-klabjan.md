---
title: Diego Klabjan
type: entity
subtype: person
created: 2026-09-02
updated: 2026-09-02
sources: 1
tags: [person, klabjan, northwestern, time-series, hallucination, chronos, hidden-states, mechanistic-interpretability]
---

**Diego Klabjan** — Professor of Industrial Engineering and Management Sciences at **Northwestern**, founding director of its MS in Machine Learning & Data Science and of the **Center for Deep Learning**. Deep-dive speaker on time-series modelling at [Day 2 of the Chicago Booth world-modeling workshop](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) (2026-09-01), presenting work by his PhD student **Yifang Zhu** (NeurIPS).

His contribution is the question **"do time-series foundation models hallucinate?"** — and a definition of hallucination that does not depend on language at all. See [time-series foundation models](../concepts/learning/time-series-foundation-models.md).

## The result in one line

Hallucinated forecasts have **collapsed hidden states**: projected with UMAP, hallucinated samples cluster tightly while correct ones disperse, and the effect strengthens in later layers. Amplifying the per-neuron "signal" component (variance under real data) relative to "noise" (the same statistic under pure Gaussian input) at every layer reduces hallucination rates — *"it doesn't shake the boat... they are better."*

## Positions

- On the workshop's central argument, stated directly: *"I know Yann is a speaker here and he believes that LLMs are not going to lead to AGI. I'm on his side — I don't see how hallucinations can be got rid of."*
- On terminology, under audience pressure: he offers to swap the word out entirely. *"The concept is a model is inferring from training data something that is wrongly inferred."* Distinguished from *lying* (contradicting what is in the data).
- Candid about what the method needs: it is **white-box** — a black-box version is *"still an open problem."*

## Related
- [Time-series foundation models](../concepts/learning/time-series-foundation-models.md) — the concept page.
- [Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md) — the hidden-state method.
- [World models for financial markets](../syntheses/society/world-models-for-financial-markets.md).

## Mentioned in
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — deep-dive talk.

> [!note] The primary is not ingested
> The NeurIPS paper is the primary for everything on this page; the talk's slides are not legible in the stream. Chase it before quoting the four rules or the λ amplification as a method. Co-authors named in the talk, **spelled phonetically from auto-captions and not yet verified**: the lead student (Northwestern CS, "Yifang Zhu"), a Northwestern CS collaborator ("Han Liu"), and an external collaborator at the University of Sydney ("Zhenyang Wang").
