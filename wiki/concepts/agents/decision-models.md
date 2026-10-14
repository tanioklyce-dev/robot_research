---
title: Decision models
type: concept
created: 2026-10-13
updated: 2026-10-13
sources: 2
tags: [decision-model, classification, calibration, single-forward-pass, routing, success-detection, llm-agent, d1, mediapipe]
---

# Decision models

A **decision model** answers a fixed-form question about an input (yes/no, one label of many, a point on a scale) by returning **a probability for each possible answer from one forward pass**, instead of generating an answer as text. The term comes from [Liquid AI](../../entities/liquid-ai.md)'s [d1](../../entities/liquid-d1.md) launch ([d1 blog](../../sources/liquid-ai-d1-decision-model-blog.md)). The underlying idea is old: it is a classifier head on a pretrained encoder, or reading the logits of the answer tokens. The new part is packaging it as a **general-purpose, prompt-specified, multimodal service**: the classes are defined in natural language at call time instead of at training time.

## Why the shape matters for agents and robots

- **Most agent sub-calls are decisions.** Did the grasp succeed? Is a person in the workspace? Which tool or skill? Keep or drop this context? Using a generative model for each is slow, costly (d1 is listed at 19–200× cheaper) and needs output parsing.
- **A probability can be thresholded; a sampled string can't.** A safety monitor, a guardrail or a success detector wants `p(person present) = 0.93` so it can pick an operating point. DeepMind's [GR 2 safety report](../../sources/gemini-robotics-2-safety-report.md) frames human-proximity detection as exactly that FPR/FNR trade-off, and found no model reaching the good quadrant. A decision-model interface makes the operating point a parameter.
- **Latency fits inside a control-loop tier.** 200–300 ms per decision is too slow for servoing but fits the 1–5 Hz supervisory tier on the [control-rate ladder](../../syntheses/platforms/control-rate-ladder.md), where routing and success checks live.

## The property that matters, and nobody reports
**Calibration.** A decision model is only better than parsing a chat model's "yes" if its 0.9 really means 90%. Neither ingested source shows a reliability diagram or ECE. Until one does, "returns probabilities" is an interface claim, not a quality claim.

## Instances
- **[d1](../../entities/liquid-d1.md)** (Liquid AI, 2026-10): API, text + vision, noul/choice/score question types.
- **MediaPipe Decision Task API** (Google): "classification, routing, and predictive capabilities" built on [EmbeddingGemma 2](../../entities/embeddinggemma-2.md) embeddings, on-device ([EmbeddingGemma 2 blog](../../sources/embeddinggemma-2-blog.md)). Mentioned only; the API was not ingested.

## Related concepts
- [LLM-agent architecture](llm-agent-architecture.md) — the loop these sub-calls live inside.
- [Semantic safety](../safety/semantic-safety.md) — hazard judgments as a classification problem.
- [AI guardrails](../safety/ai-guardrails.md) — runtime classifiers on inputs and outputs are decision models under another name.
- [On-device and on-robot agents](../../syntheses/agents/on-device-and-on-robot-agents.md).

## Current state (2026-10)
One commercial API (d1, closed weights, open weights promised) and one on-device Google API exist. The single public evaluation is the vendor's n = 1 comparison, in which d1 is near frontier quality on simple decisions and clearly behind on multi-step search. No robotics use is documented yet.

## Mentioned in
- [Introducing d1 (Liquid AI blog)](../../sources/liquid-ai-d1-decision-model-blog.md)
- [EmbeddingGemma 2 launch blog](../../sources/embeddinggemma-2-blog.md)
