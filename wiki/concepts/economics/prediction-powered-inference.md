---
title: Prediction-powered inference (PPI)
type: concept
created: 2026-05-29
updated: 2026-05-29
sources: 1
tags: [economics-of-ml, inference, uncertainty-quantification, foundation-models, debiasing, conformal, michael-jordan]
---

**Prediction-powered inference (PPI)** — an inferential algorithm that produces **provably-valid confidence intervals** for an estimand by combining a foundation model's (possibly biased) predictions with a smaller set of **local ground-truth measurements** (Angelopoulos, Bates, Fannjiang, Jordan & Zrnic, *Science* 2023). In [Jordan 2025](../../sources/jordan-collectivist-economic-ai.md) it is the worked example of correcting foundation-model bias using **local knowledge**.

## The problem it solves
Foundation models make "high-quality predictions" — but only *on average over past data*. They can be **badly miscalibrated at the edge of knowledge**, where little ground truth exists. Example from [Jordan 2025](../../sources/jordan-collectivist-economic-ai.md): **AlphaFold** (Jumper et al. 2019) gives **overly narrow confidence intervals that fail to cover the truth** for proteins exhibiting quantum fluctuations (few ground-truth measurements). Angelopoulos et al. (2023) showed such biased intervals arise across many scientific domains.

## How it works (conceptually)
A **local agent** holds ground-truth measurements not available when the foundation model was trained (or reflecting a desirable local bias). PPI uses these to **adjust the uncertainty assessment** derived from the global model, yielding intervals that **provably cover the ground-truth estimand** under standard statistical assumptions. It is in the family of distribution-free / model-agnostic uncertainty quantification (cf. conformal prediction, Angelopoulos & Bates 2023).

## The economic reinterpretation
[Jordan 2025](../../sources/jordan-collectivist-economic-ai.md) reframes PPI as **more than a debiasing technique** in a multi-agent / strategic setting:
- If the agent supplying data or the foundation model **knows** the receiver will check against local ground truth, it is **disincentivized from supplying significantly biased data**.
- It is also **incentivized to expand** the scope of its data/model to meet the receiver's needs (to keep the interaction going).

So PPI functions as an **implicit incentive mechanism** — a bridge between the inferential and economic legs of the [three thinking styles](three-thinking-styles.md). The broader point: "correct response" is often ambiguous because knowledge is **local, contextual, and fleeting**; good answers blend outside-source information with locally-available information.

## Related concepts
- [Three thinking styles](three-thinking-styles.md) — PPI as an inference⊕economics blend.
- [Mechanism design & statistical contract theory](mechanism-design.md) — the incentive lens PPI is reinterpreted through.
- [Collectivist AI / AI-as-market](collectivist-ai.md) — PPI as how a market participant safely queries a foundation model.

## Mentioned in
- [A Collectivist, Economic Perspective on AI (Jordan, 2025)](../../sources/jordan-collectivist-economic-ai.md)
