---
title: d1 (Liquid AI decision model)
type: entity
subtype: model
created: 2026-10-13
updated: 2026-10-13
sources: 1
tags: [d1, liquid-ai, decision-model, classification, vision, api, single-forward-pass]
---

**d1** is [Liquid AI](liquid-ai.md)'s **decision model**, launched with vision on 2026-10-05. Its input is text and/or images plus questions. Its output is **a probability per possible answer from a single forward pass, with no generated tokens** ([d1 blog](../sources/liquid-ai-d1-decision-model-blog.md)).

## Interface
- Question types: **noul** (yes/no → p), **choice** (distribution over labels), **score** (probability-weighted scale position). Several questions per request.
- **200–300 ms** per text decision (API). **$0.04 / M input tokens**, no output billing; images cost 1.5 tokens per 32×32 patch.
- Available on the Liquid API (vision), Vercel and OpenRouter (text only for now). Not open-weight yet. No size or architecture disclosed.

## Results (vendor, n = 1 per app)
Ties or beats GPT-6.1 Sol on 4/6 applications. Against Claude Opus 5.5 it **ties 2 and loses 4**, worst on Code Search (80 vs 100). Cost is 19–200× lower. Zero-shot VisA defect sorting scores 85–97% with a good-part reference shown. Full table and caveats are on the [source page](../sources/liquid-ai-d1-decision-model-blog.md#the-comparison-chart-as-data).

## Why it matters in this wiki
Robot agent loops contain many cheap classification sub-decisions: success detection, routing, hazard yes/no, context pruning. A model that returns probabilities directly could do those in place of a chat model, if the probabilities are calibrated, and that is not measured. See [decision models](../concepts/agents/decision-models.md).

## Mentioned in
- [Introducing d1 (Liquid AI blog)](../sources/liquid-ai-d1-decision-model-blog.md)
