---
title: MetaOthello
type: entity
subtype: benchmark
created: 2026-09-02
updated: 2026-09-02
sources: 1
tags: [metaothello, othello-gpt, world-model, interpretability, linear-probe, steering, belief-state, ambiguity, toy-model]
---

**MetaOthello** — *"A Controlled Study of Multiple World Models in Transformers."* **Aviral Chawla, Galen Hall and Juniper L. Lovato** (University of Vermont); presented at [Day 2 of the Chicago Booth world-modeling workshop](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) (2026-09-01) by a collaborator who introduced himself as presenting *"from the University of Michigan,"* on behalf of *"my co-author Avi back there and his adviser Juniper"* — i.e. Chawla and Lovato. On the poster author list the presenter is **Galen Hall**.

## The question

An input sequence can be **compatible with more than one world** — more than one underlying state, or even more than one set of dynamics that generated it. The talk's motivating example is an instruction ambiguous between worlds in which a given strategy is or is not acceptable. How is that represented inside the model, and how does the model decide which world's rules to apply?

Foundation models are the wrong place to ask, because *"we don't actually know what the correct model of the underlying world is."* So: **Othello-GPT with variants.** Take the established setup (train on random legal move sequences, nothing about the game; the board state turns out to be linearly decodable from the residual stream), then **alter the rules** — e.g. a variant where only the *outermost* flanked pieces flip — producing games with the same board, same syntax, same legality rules, but **different latent board updates**, whose sequences partially overlap with classic Othello. Train 8-layer GPT-style transformers on ~**40M sequences** mixed from both.

## Three results

1. **Capability is unaffected.** Every model — classic-only, variant-only, mixed — predicts legal next moves about equally well.
2. **Both hypotheses are represented, and they share a substrate.** A linear probe recovers **both** candidate board states from an ambiguous sequence. But interventions on either representation *"work the same regardless of whether the sequence is sampled from one game or the other"* — the representations are **causally equivalent**, evidence of one base board representation with **game-specific perturbations on top** rather than two parallel world models.
3. **The disambiguation is localized and abrupt.** The optimal posterior probability that a sequence came from one dynamics or the other is *"only properly represented after the fifth layer"* — it emerges suddenly — and **the same direction can be used to steer** which rule set the model applies to generate next tokens. But only at layer 5.

## Why it matters here

> [!note] This is the belief-state question, made experimental
> Day 1's panel argued whether to **represent the full belief** ([Hafner](danijar-hafner.md): tried it, sampling worked better) or **discard what you can't predict** ([LeCun](yann-lecun.md): the JEPA argument) — an argument the wiki notes is Blackwell's mixed state under another name. MetaOthello asks the *empirical* version: given genuine ambiguity, what does a trained transformer actually do? The answer is neither of the two positions — it maintains a **shared representation plus a low-dimensional world-selector**, and the selector is a single steerable direction at one layer.
>
> Compare [Vafa et al.](../sources/vafa-world-model-implicit.md), where a model can score 1.00 on next-token legality and 0.10 on world-model compression. MetaOthello's models are also perfect on legality — and here the underlying structure *is* recovered. The difference is that the true world is known and small.

Also relevant to the wiki's [linear-probe caution](../concepts/safety/mechanistic-interpretability.md): the same workshop's poster session carried *"Is a Linear Probe Evidence of a Linear Representation?"* (Internò, Kutluozen, [Klindt](david-klindt.md)), which is the methodological objection to exactly this technique.

## Related
- [Belief states and mixed states](../concepts/world-models/belief-states-and-mixed-states.md).
- [Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md) — probes and steering.
- [Vafa et al. — Evaluating the World Model Implicit in a Generative Model](../sources/vafa-world-model-implicit.md) — the Othello-GPT lineage.

## Mentioned in
- [Third World Modeling Workshop — Day 2](../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — lightning talk, session 3.

> [!note] Thin entity
> Five-minute talk, no paper ingested. Author names were recovered from the workshop's archived poster list, not from the auto-captions, which rendered "Juniper" as a first name with no surname.
