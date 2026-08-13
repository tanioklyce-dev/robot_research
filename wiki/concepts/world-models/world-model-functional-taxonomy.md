---
title: World-model functional taxonomy (renderer / simulator / planner)
type: concept
created: 2026-08-07
updated: 2026-08-07
sources: 2
tags: [world-model, taxonomy, spatial-intelligence, policy, renderer, simulator, planner]
---

**A functional taxonomy of world models**: sort them not by architecture but by **the role they play** in perceiving, understanding, and acting — **renderers** help us see, **simulators** help us understand, **planners** help machines act. Proposed by [Fei-Fei Li](../../entities/fei-fei-li.md) in a June 3, 2026 [World Labs](../../entities/world-labs.md) Substack post and carried into policy by the [HAI world-model brief](../../sources/hai-world-model-spatial-intelligence-brief.md).

This is a **capability stack**, not a partition — rendering what a world looks like, simulating how it behaves, planning how to act within it.

| Category | Core task | Primary outputs | Example applications | Maturity |
|---|---|---|---|---|
| **Renderer** | Generate observations of a world from a viewpoint, prompt, or scene description | Images, video, visual sequences, interactive views | Architecture and design visualization; animated film; digital content | **Most mature** — Marble, Tencent HY-World 2.0 already ship explorable scenes from text/image |
| **Simulator** | Model underlying state, geometry, and dynamics; show the effect of changes | Digital environments that behave according to physics and biological properties | Crash-test simulation; digital twins; surgical practice; military training across domains | Conventional simulation mature ([Omniverse](../../entities/nvidia-isaac-sim.md)-class), *learned* simulation early and data-limited |
| **Planner** | Determine what action an agent should take given a state or goal | Actions, trajectories, policies, intervention choices | Robotics, AVs, warehouse systems, healthcare logistics, disaster response, defense | **Least mature** — reliable only in bounded domains; most demos are "short, narrow tasks in controlled labs" |

## Why the ordering is the interesting part

The maturity gradient runs exactly opposite to the value gradient. Renderers are commercially mature and optimized for **plausibility rather than underlying truth** — a renderer can produce a photorealistic hospital wing without capturing how people, materials, or infrastructure would behave inside it. Planners are the ones that touch the physical world, and they are the least mature. Everything in between — the [sim-to-real](../learning/sim-to-real-transfer.md) problem, the [visual plausibility trap](world-model-evaluation.md), the whole robot-policy-evaluation literature — lives in the gap between "looks right" and "acts right."

## Interactivity as the emergent fourth thing

When the three functions run together in a **real-time, action-conditioned loop**, the brief says a further capability emerges: **interactivity** — people and machines act within a modeled world and use the resulting feedback to guide action in the physical one. A surgeon rehearsing in simulated anatomy that responds to each movement; a warehouse robot practicing unfamiliar objects in a digital twin before entering the facility. The brief's claim is that interactivity "is thus a natural consequence of a capable world model and where its most valuable uses lie."

## The taxonomy is already dissolving — and that is the policy point

> [!warning] Do not build thresholds on these categories
> The brief is blunt about the shelf life of its own framework: renderers are becoming interactive, simulators more generative, and planners more capable of reasoning, and "at the research frontier, unified models increasingly combine rendering, simulation, and control within a single network." Its conclusion — **"capability thresholds defined per category are easily gamed or outgrown; consequently, safeguards must attach to the deployment context rather than to the model class."**

This wiki already holds the counterexamples. [Cosmos 3](../../sources/cosmos-3-technical-report.md) is simultaneously a forward-dynamics model, an inverse-dynamics model, a VLM, and a video-action policy — renderer, simulator, and planner in one dual-tower network. [Genie Envisioner](../../entities/genie-envisioner.md) / GE-Sim2 makes action a first-class variable inside a video generator. The [world-action model](world-action-model.md) concept page is the architectural name for this collapse. The brief notes it independently: recent unified world-action models learn rendering, dynamics and control jointly, "with planning capability emerging directly from learned visual dynamics rather than from an intermediate simulator."

So the taxonomy's durable use is **not** classification of systems. It is classification of **uses**, which is what determines how hard the system should be tested — see [world-model evaluation](world-model-evaluation.md), where the brief's evaluation ladder is keyed to exactly these three roles.

## Related concepts

- [World model](world-model.md) — the architecture-first taxonomy (generative-video / JEPA / frozen-feature / MBRL / omnimodal) that this one cuts across.
- [World-model simulators](world-model-simulators.md) — the "simulator" row, as this wiki had already carved it.
- [World-action model](world-action-model.md) — the unified endpoint.
- [Spatial intelligence](spatial-intelligence.md) — the capability the stack composes into.
- [World-model governance](../safety/world-model-governance.md) — why safeguards attach to deployment context instead.

## Mentioned in

- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../../sources/hai-world-model-spatial-intelligence-brief.md)
