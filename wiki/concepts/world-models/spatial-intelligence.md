---
title: Spatial intelligence
type: concept
created: 2026-08-07
updated: 2026-08-26
sources: 6
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

> [!note] Independently arrived at, at manipulation timescale
> [Yunzhu Li](../../entities/yunzhu-li.md) gives the same probe when asked why R2S2R differs from the video-model approach: consistency must hold "over space, over time, over different viewpoints, and over different types of interactions," and the failure is concrete — *"imagine if a robot pushes an object forwards. **The object just magically disappears**, which has been a problem of many of the existing video prediction models. This won't provide good enough signal for the robot to know what is the right thing to do"* ([a16z conversation](../../sources/a16z-worldlabs-scenix-conversation.md)). The brief's version is a person leaving a room; this one is an object under contact, seconds apart. Same test, and the shorter horizon is the harder one to excuse.

> [!note] This is the same claim the wiki's JEPA thread makes from the other direction
> The [instruction-leakage](instruction-leakage.md) concept and the [identifiability](identifiability.md) work are both about whether a learned latent actually tracks the world's state or merely reproduces something that scores well. "Leave and return" is the behavioral version of the same question.

## Lineage

Older than the term. Kenneth Craik proposed in **1943** that humans carry a "small-scale model" of reality to test actions internally before acting — reasoning through a bridge design in the mind before building it. Early AI researchers took the idea up in the 1960s with explicit structured internal models, which stayed confined to narrow rule-governed environments for decades.

Two recent developments unlocked it, per the brief: reinforcement learning showing that agents can learn to act through **internal simulation** (reducing reliance on costly real-world trial and error), and multimodal AI making it possible to ground systems in how the physical world **actually looks, moves, and sounds**.

## The substrate argument

The [taxonomy essay](../../sources/world-labs-functional-taxonomy.md) states the language/space contrast more sharply than the brief does, and grounds it in what is being *modeled* rather than what is being *predicted*:

> "Where language models learn the statistical structure of text, world models learn the statistical structure of space and time: how light falls on a surface, how a garden looks from an angle no camera has captured, how objects respond to force and follow the laws of physics."

And its ordering claim — **"If language is an abstraction of the world and pixels are a projection of it, then geometry, physics, and dynamics are the world itself."** That is the essay's basis for calling the simulator the linchpin, and it is a claim about which representation the others can be *derived from*, not about which is more mature.

The essay also names the term's own problem: "world" has always been "a stand-in for whatever totality a given thinker needed to reason about," which is why computer vision, robotics, RL and generative AI can each claim to build world models and each mean something different. Spatial intelligence is the attempt to name the capability instead — the same move this page opens with.

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
- [A Functional Taxonomy of World Models](../../sources/world-labs-functional-taxonomy.md) — the primary for the renderer/simulator/planner stack and the substrate argument above.
- [Building Worlds That Train Robots (R2S2R)](../../sources/world-labs-r2s2r.md) — "robotics is where spatial intelligence becomes physical."
- [Fei-Fei Li is Solving the Hardest Problem in Robotics (a16z × World Labs)](../../sources/a16z-worldlabs-scenix-conversation.md) — object permanence under contact; "robotics is where spatial intelligence becomes physical."
