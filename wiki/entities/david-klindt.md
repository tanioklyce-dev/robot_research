---
title: David Klindt
type: entity
subtype: person
created: 2026-07-26
updated: 2026-09-02
sources: 3
tags: [person, klindt, cold-spring-harbor, identifiability, jepa, lejepa, theory, representation-learning]
---

**David Klindt** — researcher at **Cold Spring Harbor Laboratory**; lead author of **[When Does LeJEPA Learn a World Model?](../sources/when-does-lejepa-learn-a-world-model-paper.md)** (2026-05-25, with [LeCun](yann-lecun.md) and [Balestriero](randall-balestriero.md)).

His contribution to this wiki is the import of **[identifiability theory](../concepts/world-models/identifiability.md)** — a line from causal representation learning and nonlinear ICA — into the JEPA program, which until then argued for latent prediction on architectural and empirical grounds rather than recovery guarantees.

> [!note] Thin entity
> Two sources, both about the same paper. His prior work in identifiability / neuroscience-adjacent representation learning is not yet ingested and is the obvious gap if this thread is pursued.

## The latent-learning argument (2026-09-01)

Presenting the paper at the [Chicago Booth workshop](../sources/chicago-booth-world-modeling-workshop-2026-day2.md), Klindt draws a **behavioral prediction out of the theory** that is not in the paper, and it is the most actionable thing he has said in this wiki.

He cites **Tolman & Honzik's 1930s latent-learning experiments**: rats run repeatedly to a food goal in a maze, versus rats that simply explore it with no reward. Move the food, and the *explorers* find it almost immediately while the goal-trained rats struggle. The theory's requirement of an unbiased random walk through latent space says the same thing about representation learning: **goal-biased training data produces a worse map.**

Demonstrated on a robot reaching task — a model trained on exploratory random-walk data plans a near-optimal arc that *"follows the shadow of the correct solution"*, while the goal-focused model overshoots and has to correct.

> [!note] This cuts directly against the wiki's teleoperation orthodoxy
> Almost every robot dataset here is **successful demonstrations only**. This is a second, independent argument for the same conclusion as [Vafa et al.](../sources/vafa-world-model-implicit.md)'s finding that models trained on random data recover more structure than models trained on expert data — and as [Jeannette Bohg](jeannette-bohg.md)'s Day 1 point that failures supply the counterfactuals a world model needs. Three routes, one destination, and no ingested source builds a dataset that way.

He also concedes the standard objection to his own theorem before the audience raises it: a Gaussian world *"is a world void of structure — it's maximum entropy, so it's boring,"* which is why ICA looks for the opposite. His answer is the latent-learning argument above: the assumptions are not fairyland if they tell you how to collect data.

## Related
- [Identifiability](../concepts/world-models/identifiability.md) — the concept he brings to the JEPA thread.
- [Yann LeCun](yann-lecun.md) / [Randall Balestriero](randall-balestriero.md) — co-authors.
- [MetaOthello](metaothello.md) — a probe-and-steer result presented in the same session that his own poster ("Is a Linear Probe Evidence of a Linear Representation?") is the methodological objection to.

## Mentioned in
- [When Does LeJEPA Learn a World Model?](../sources/when-does-lejepa-learn-a-world-model-paper.md) — lead author.
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — lightning talk; the Tolman & Honzik latent-learning argument.
