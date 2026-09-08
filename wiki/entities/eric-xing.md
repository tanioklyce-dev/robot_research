---
title: Eric Xing
type: entity
subtype: person
created: 2026-09-07
updated: 2026-09-07
sources: 3
tags: [person, mbzuai, cmu, world-model, glp, pan, critique]
---

**Eric P. Xing** — President of [MBZUAI](mbzuai.md) and professor at Carnegie Mellon's School of Computer Science; first author of [Critique of World Model](../sources/critique-of-world-model-paper.md), the essay that coins **Generative Latent Prediction (GLP)** and previews the [PAN](pan-world-model.md) world model. In this wiki he is the named counter-party to [Yann LeCun](yann-lecun.md) on the question of whether a world model should reconstruct observations.

## Position, in one paragraph

A world model is *"a generative model that simulates the possibilities in diverse scenarios"* for purposeful reasoning; it is not a video generator and not an open-loop latent predictor. Representations must be **stateful**, which he argues favours discrete tokens as the backbone with continuous embeddings for nuance. Learning should be **grounded in observation** through a decoder, because a lossy encoder cannot be diagnosed from inside its own latent space (Theorem 2 of the essay: the latent loss is an upper-bounded surrogate of the generative one). Decision-making should use **RL from simulated experience** rather than MPC. The LLM is a first-class component of the reasoning backbone, not something to route around ([source](../sources/critique-of-world-model-paper.md)).

## Debates and lineage

- **[LeCun–Xing debate](../sources/lecun-xing-jepa-glp-debate-2026.md)**, Spring School AI for Impact, UM6P Benguerir, March 2026 — ingested. His rebuttal opens with *"I fundamentally agree with Yann that the prediction needs to happen in abstract space"* and narrows the disagreement to where prediction is *checked*; concedes GLP *"can strictly subsume JEPA if you turn off the generative function."* Also presents a "system three" agent model (a configurator choosing between reactive policy and world-model planning).
- Earlier programme: *Toward a standard model of machine learning* (Hu & Xing 2021), SimuRA (LLM-based world model for goal-oriented agents, 2025), Pandora (natural-language actions + video states, 2024), all cited as antecedents of PAN.
- A companion essay, *Critiques of Agents*, is listed as in preparation.

## Mentioned in

- [Critique of World Model](../sources/critique-of-world-model-paper.md) — first author.
- [PAN technical report](../sources/pan-world-model-paper.md) — conception, design and leadership.
- [LeCun & Xing debate](../sources/lecun-xing-jepa-glp-debate-2026.md) — speaker.
