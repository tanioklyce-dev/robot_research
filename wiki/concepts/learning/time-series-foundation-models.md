---
title: Time-series foundation models (and whether they hallucinate)
type: concept
created: 2026-09-02
updated: 2026-09-02
sources: 1
tags: [time-series, foundation-models, chronos, hallucination, zero-shot-forecasting, hidden-states, signal-noise, interpretability, non-stationarity]
---

**Time-series foundation models** are pretrained transformers for **zero-shot forecasting**: given a context window of a series it has never seen, emit the next *q* values without fitting anything. Some are adapted from text foundation models, some are transformers with time-series-specific modifications; all are trained on very large heterogeneous collections of series. **Chronos** (Amazon) is the best-known.

The wiki's entry point is [Diego Klabjan](../../entities/diego-klabjan.md)'s deep-dive at [Day 2 of the Chicago Booth workshop](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md), which asks whether they **hallucinate**, and answers yes.

## Hallucination without language

The motivating example needs no LLM framing: a clean alternating 0-1-0-1 series, forecast as a **constant 1**. The pattern is unambiguous, both values are equally frequent in the context, and every human gets it right.

The working definition offered, after audience pushback on the word:

> *"A model is inferring from training data something that is wrongly inferred."*

Distinguished from **lying** (contradicting what is in the data — "the capital of the US is Paris"). Offered as terminology-agnostic — *"you can replace hallucination with your favorite word"* — and, importantly, **the detection rules below apply to classical models too**: ARMA and friends can be flagged by them; statisticians simply never used the word.

Asked whether a hallucinating model is just a **bad** model, he declines the collapse: Chronos is state of the art, and *"I would not call Opus 4.8 a bad model even though it hallucinates. It increases my productivity a lot."*

## Four detection rules

All built the same way — compute a statistic over sliding windows of the context, compute it on the forecast, flag a large gap. Zero-shot, no ground truth needed.

| Rule | Statistic on windows vs. forecast | Firing rate |
|---|---|---|
| **R1 trend** | slope of a univariate regression | low |
| **R2 frequency** | frequency of y-values | low |
| **R3 relative absolute error** | window vs. forecast | — |
| **R4 ARMA(1,1) coefficients** | AR and MA coefficient pair | **fires far more often than the others** |

The set is explicitly extensible (seasonality, R²) and the mitigation method does not depend on which rules are used. A sample is "hallucinated" if **any** rule fires. Sanity check: samples flagged by the rules have significantly lower R² than unflagged ones, across six hard public datasets and three foundation models.

## The mechanistic finding

Project last-layer hidden states with UMAP and colour by whether the rules fired:

> **Hallucinated samples cluster tightly; correct ones disperse.** And the effect **strengthens in higher layers** — lower layers show it weakly, later layers strongly.

So *homogeneity of hidden state* is a signature of hallucination. That inverts the usual intuition about representation collapse: here the collapse is not a training failure, it is a **runtime indicator** available before you see the ground truth.

## The mitigation: amplify signal, not noise

Decompose each layer's hidden state into **signal** and **noise**, defined operationally rather than theoretically:

- **Signal** — the per-neuron standard deviation of activations across real inputs.
- **Noise** — the same statistic computed when the model is fed **pure Gaussian noise** as input. *"For those of you familiar with diffusion models... here it's similar — we just assume pure noise to capture noise."* Deliberately the simplest thing that could work.

Then at every layer: centre the hidden state, project onto the signal subspace, **add (λ−1)× the signal component** with λ > 1, restore the mean. λ is computed dynamically rather than fixed. A separate **contrastive** statistic (signal minus noise at the neuron with the largest gap, last layer) serves as a hidden-state-based hallucination detector complementing the four statistical rules.

> [!note] Honest about the effect size, which is rare enough to record
> *"It doesn't shake the boat... they are better."* Against vanilla Chronos the improvement in hallucination rate and Pearson correlation is clear; against the other two models it is small. Carry this as **a mechanism with a modest effect**, not a fix.

## Limitations, stated by the author

- **White-box only.** It needs access to hidden states. *"Completely black box — that's still an open problem."*
- **Relationship to causality unexplored**, offered to the room as an open question.
- More models and more datasets needed.

## The comparison that should temper the whole area

An audience member reports unpublished work comparing foundation-model forecasters against traditional statistical models on standard public datasets, reaching *"the same conclusion... the standard statistical models often outperform LLM and deep learning models."* Klabjan does not dispute it. He also relays a consulting engagement where a Fortune 500 firm wanted financial foundation models for forecasting while doing no sophisticated classical modelling — *"they are just following buzzwords."*

> [!warning] Read alongside the wiki's other transfer-of-hype warnings
> This is the same shape as the [visual plausibility trap](../world-models/world-model-evaluation.md): a model whose outputs look like the right kind of object, evaluated by people who want it to work, against baselines that were never run.

## Related concepts
- [Mechanistic interpretability](../safety/mechanistic-interpretability.md) — hidden-state geometry as the diagnostic.
- [Neural geometry](../safety/neural-geometry.md) — representation collapse as a measurable property.
- [World-model evaluation](../world-models/world-model-evaluation.md) — the same detect-without-ground-truth problem.
- [Runtime failure detection](../robotics/runtime-failure-detection.md) — the robotics analogue: flag a bad rollout before the outcome is known.
- [World models for financial markets](../../syntheses/society/world-models-for-financial-markets.md).
- [LeNEPA](../../sources/lenepa-paper.md) — the wiki's other time-series line, from the SSL side.

## Mentioned in
- [Third World Modeling Workshop — Day 2](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — Diego Klabjan deep-dive.
