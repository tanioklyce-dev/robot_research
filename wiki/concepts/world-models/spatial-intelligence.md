---
title: Spatial intelligence
type: concept
created: 2026-08-07
updated: 2026-08-07
sources: 1
tags: [spatial-intelligence, world-model, embodied-ai, policy, stanford-hai]
---

**Spatial intelligence** — the capacity "to understand a physical environment and use that information to guide action" ([HAI world-model brief](../../sources/hai-world-model-spatial-intelligence-brief.md)).

The term is doing a specific piece of work: it names the **capability**, where [world model](world-model.md) names one **technical pathway** toward it. The brief is explicit — "world models are one technical pathway toward achieving that capability." Keeping the two apart matters, because a policy or benchmark written against "world models" binds to an architecture that is already dissolving into unified networks, whereas one written against spatial intelligence binds to what the system can do.

## The contrast it is drawn against

The framing is deliberately generational. The systems defining the current AI era operate through **language**; multimodal systems extend that to images, audio and video, "but most still cannot track a coherent environment over time." Spatial intelligence is the claimed next axis: maintain a coherent representation of an environment *over time* and predict how it changes *in response to action*.

The operational distinction from a language model is action-conditioning, not modality. A language model predicts the next token in text. A spatially intelligent system predicts what happens if an object is moved or a door is opened — including, per the brief's central technical ambition, **counterfactual** actions the model was never explicitly trained on.

## The informal progress test

The brief offers a concrete probe that is worth remembering because it is cheap to run and hard to fake: can an agent **move an object, leave the scene, and return to find it where it was left**?

What makes this a test of spatial intelligence rather than of video quality is that in a world model the persistence is *learned from observation*, while in a game engine or authored simulator every object is placed in advance and persistence is free. The same probe is the failure mode behind the brief's [Genie 3](../../entities/genie-3.md) datapoint — coherent for only a few minutes at its 2025 release before objects "shift or vanish."

> [!note] This is the same claim the wiki's JEPA thread makes from the other direction
> The [instruction-leakage](instruction-leakage.md) concept and the [identifiability](identifiability.md) work are both about whether a learned latent actually tracks the world's state or merely reproduces something that scores well. "Leave and return" is the behavioral version of the same question.

## Lineage

Older than the term. Kenneth Craik proposed in **1943** that humans carry a "small-scale model" of reality to test actions internally before acting — reasoning through a bridge design in the mind before building it. Early AI researchers took the idea up in the 1960s with explicit structured internal models, which stayed confined to narrow rule-governed environments for decades.

Two recent developments unlocked it, per the brief: reinforcement learning showing that agents can learn to act through **internal simulation** (reducing reliance on costly real-world trial and error), and multimodal AI making it possible to ground systems in how the physical world **actually looks, moves, and sounds**.

## Related concepts

- [World model](world-model.md) — the pathway; the umbrella architecture concept.
- [World-model functional taxonomy](world-model-functional-taxonomy.md) — renderer / simulator / planner, the stack that composes into spatial intelligence.
- [World-model evaluation](world-model-evaluation.md) — how you would ever measure this.
- [World-action model](world-action-model.md) — the unified-network endpoint the taxonomy is dissolving into.
- [Latent space](latent-space.md) / [identifiability](identifiability.md) — whether the internal representation tracks the real world.

## Current state

A marketing term and a research program at the same time, which is a reason to handle it carefully. As of mid-2026 the wiki holds strong technical evidence for the **rendering** end (generative-video world models producing minute-scale coherent rollouts) and much weaker evidence for the **acting** end — see [robot policy evaluation](../robotics/robot-policy-evaluation.md), which argues the published manipulation numbers do not support their own rankings. The [HAI brief](../../sources/hai-world-model-spatial-intelligence-brief.md)'s maturity ordering (renderers ≫ simulators ≫ planners) is consistent with that.

## Mentioned in

- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../../sources/hai-world-model-spatial-intelligence-brief.md)
