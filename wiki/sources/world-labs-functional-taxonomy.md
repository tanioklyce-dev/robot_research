---
title: "A Functional Taxonomy of World Models"
type: source
url: https://www.worldlabs.ai/blog/taxonomy-of-world-models
author: World Labs team and Fei-Fei Li
published: 2026-06-03
ingested: 2026-08-26
venue: World Labs blog
format: blog post
tags: [world-model, taxonomy, renderer, simulator, planner, spatial-intelligence, pomdp, world-labs]
---

# A Functional Taxonomy of World Models

Subtitle: *"Renderers, Simulators, Planners, and the Loop That Connects Them."*

> [!note] This is the primary the wiki had been citing second-hand
> The **renderer / simulator / planner** framework entered this wiki through the [HAI world-model brief](hai-world-model-spatial-intelligence-brief.md), which borrows it. The [functional-taxonomy concept page](../concepts/world-models/world-model-functional-taxonomy.md) was built from that borrowing and, until this ingest, attributed brief-only material to the taxonomy itself. See [what the primary does *not* contain](#what-the-brief-added-that-this-post-does-not-contain).

## Summary

Positions itself as the sequel to World Labs' earlier "spatial intelligence is AI's next frontier" essay, going "one level deeper": of the many things now called world models, which functional pieces actually compose that capacity, and what is each one for? The answer is derived from the **POMDP loop** — an agent takes **actions**, actions change the world's **state**, the agent perceives **observations**, observations inform new actions. Each thing called a world model is a different **projection of that same loop**, distinguished by which of the three quantities it outputs. From that, three categories: **renderers** output observations, **simulators** output state, **planners** output actions. The essay's actual thesis is not the taxonomy but a ranking within it: **the simulator is the linchpin**, because geometry/physics/dynamics is the substrate from which both visual appearance and action consequences can be derived, and the categories are already collapsing toward a unified model.

## Key claims

### The generative rule

- The taxonomy is not a list of three system types; it is the **three outputs of the POMDP loop**. "The different things now being called world models are in fact different projections of this same loop. Each one outputs a different piece of it."
- **State** is used in the physicist's/roboticist's sense — "a complete description of what is happening in the world at a given moment, including every object, every position, every velocity, every property" — explicitly *not* the chemist's sense (solid/liquid/gas). State is "complete in principle, but never directly visible to any agent inside it."
- **Renderer and planner are formal inverses.** "Where a renderer takes actions as input and produces observations, a planner takes observations as input and produces actions, closing the perception-action loop."

### The three categories

| | Outputs | Contract | Consumers | Named examples |
|---|---|---|---|---|
| **Renderer** | Observations (pixels for human eyes) | Purely **visual** — visual fidelity is "the quality that matters most" | Human viewers | Google [Genie 3](../entities/genie-3.md); World Labs **RTFM**; Google **Nano Banana**; text-to-video "cinematic drone shot" models |
| **Simulator** | State — "geometrically, physically or dynamically faithful" | **Structural** — "geometry that holds up under inspection, physics that respects Newton's laws" | *Two at once*: human professionals (architects, designers, filmmakers, game devs) **and** computer programs (RL agents, robot controllers, AVs) | World Labs **[Marble](../entities/marble.md)**; NVIDIA **Omniverse** |
| **Planner** | Actions — "given an observation and a goal… what the agent should do next" | Decide what to do in an unstructured world | Embodied agents | [VLA models](../concepts/learning/vla-models.md); model-based systems; "the new wave of [World Action Models](../concepts/world-models/world-action-model.md)" |

- On renderers: **"The model carries no explicit understanding of three-dimensional structure. It produces what a viewer would see, not what is."** The illustration: "The buildings in the drone shot may look flawless from above, but try to drive through the city below and they fall apart."

### Simulation is the linchpin — the essay's actual argument

- **"Of the three categories, the simulator gets the least public attention, and is the most consequential of the three. This essay addresses this asymmetry."**
- The claim is a **dependency ordering**, not a maturity observation: *"If language is an abstraction of the world and pixels are a projection of it, then geometry, physics, and dynamics are the world itself."* The simulator is "the structural backbone from which both visual appearance (for renderers) and action consequences (for planners) can be derived."
- Therefore: **"A model that masters simulation can project its understanding into pixels for human consumption, and into action predictions for embodied agents. A model that masters only rendering, or only planning, cannot do either."**
- **Renderers are the most commercially mature** — Nano Banana "has put renderer-quality image generation in the hands of potentially hundreds of millions of users." But "renderers optimize for visual plausibility rather than physical accuracy, and that ceiling matters. Their outputs are beautiful, but they cannot be trusted to design a building or train a robot."
- Market sizing, attributed to NVIDIA: **Omniverse "alone targets what the company estimates as more than a trillion dollars of addressable market in factories, warehouses, supply chains, and digital twins."**

### The candor on planners

> "The field has produced robotic demos in the last two years that look impressive in videos, but candor is required about what those demos actually show. **Almost all have been confined to heavily constrained laboratory setups, with narrow object sets and short task horizons. None have been validated at the complexity, variability, or duration that real-world deployment demands.** The gap between a compelling demo reel and a robot that reliably works in a kitchen, a warehouse, or an operating room remains vast."

Immediately followed by: "The commercial bets are nonetheless substantial. A wave of well-funded entrants is racing to ship general-purpose planning systems, while the largest infrastructure players are positioning planning atop broader simulation stacks."

### The four hard problems in simulation

1. **3D data scarcity** — "Three-dimensional data with explicit geometry, material properties, and physical annotations is orders of magnitude scarcer than the internet video that renderers train on."
2. **The [sim-to-real gap](../concepts/learning/sim-to-real-transfer.md)** persists.
3. **A new generative-simulator risk** — "AI-generated geometry can look correct while containing self-intersections or wrong scale that produce nonsensical physics."
4. **Multi-physics cost** — rigid bodies + deformables + fluids + cloth interacting "remains orders of magnitude more expensive than single-domain simulation."

### Convergence and the unified endpoint

- "The same underlying knowledge of how the world works — geometry, physics, dynamics — sits beneath all of them." The cup example, used twice: a model that truly understands how a cup sits on a table "should be able to render that cup from any angle, simulate what happens when the cup is pushed, and plan for a hand to pick the cup up. **The three categories are three projections of a single underlying understanding.**"
- Two concrete collapse mechanisms named:
  - **Renderer → planner.** "A small but growing number of recent work from various robotics labs have demonstrated that — at least conceptually — a pretrained video renderer can be used as the backbone for joint world-and-action prediction."
  - **Renderer → simulator.** "World Labs' Marble already outputs Gaussian splats and collision meshes from a single model, dissolving the boundary between the renderer and the simulator."
- The direction of travel across all three: **"Every level is moving from passive output to interactive system, with renderers becoming action-conditioned, simulators generating worlds that are more controllable and editable, and planners deliberating rather than just reacting."**
- **The endpoint**: "one foundation model that can render photorealistic views, produce physically accurate structure, and plan action sequences, **switching between output modalities depending on what the downstream consumer needs.**"
- **The stated open problem**: "The data picture is uneven, with renderers awash in internet video while simulators and planners face acute shortages of 3D assets and robot demonstrations. Optimizing for visual beauty can sacrifice the precision a robot or a high-fidelity simulation needs. **Reconciling these tensions inside a single architecture is the defining open problem in world model research today,** and this is what World Labs sets out to do as we continue to evolve Marble."

### Marble, as described here

Takes **multimodal prompts — text, image, video, or spatial sketch** — and generates explorable 3D environments, outputting **Gaussian splats** for visual exploration **alongside collision meshes a physics engine can operate on**. Framed as "our first move into this territory… only the first chapter."

### Lineage

- **Kenneth Craik, 1943** — minds reason by running "small-scale models" of reality.
- Carried into neural networks "by the late 1980s and early 1990s."
- The POMDP picture is credited to RL textbooks "including the canonical Sutton and Barto," and the essay states that **"the original definition of the term 'world model' belongs to that tradition."**
- The framing device: the ancient Greeks never agreed whether the world was fire, water, or atoms, because "'world' was never a single thing. It was always a stand-in for whatever totality a given thinker needed to reason about. AI has inherited the same problem, at exactly the moment when the field needs precision."

## What the brief added that this post does not contain

Recording this explicitly, because the wiki previously blended the two.

| Claim | In this post? | Source |
|---|---|---|
| Renderer / simulator / planner categories | **Yes** | This post |
| POMDP derivation; renderer–planner inverse | **Yes** | This post — *absent from the brief's presentation* |
| Simulator-as-linchpin dependency argument | **Yes** | This post — *absent from the brief* |
| Maturity ordering (renderers ≫ simulators ≫ planners) | **Yes** | Both |
| **Interactivity as an emergent fourth capability** | **No** | [HAI brief](hai-world-model-spatial-intelligence-brief.md) only |
| **"Capability thresholds per category are easily gamed or outgrown"** / safeguards attach to deployment context | **No** | [HAI brief](hai-world-model-spatial-intelligence-brief.md) only |
| Evaluation ladder keyed to the three roles | **No** | [HAI brief](hai-world-model-spatial-intelligence-brief.md) only |
| Public pools of shared action data | **No** | [HAI brief](hai-world-model-spatial-intelligence-brief.md) only |

The post has **no governance content at all**. It is a company research-positioning essay; the policy apparatus around the taxonomy is Stanford HAI's addition.

> [!note] Provenance correction
> The wiki previously described this as a *Substack post by Fei-Fei Li*. It is a post on the **World Labs company blog**, bylined **"the World Labs team and I"** — a corporate research statement co-signed by the CEO, not a personal essay. The distinction matters for how much of it reads as positioning: the essay argues the simulator is the most consequential category, and World Labs' product is the one it names as dissolving the renderer/simulator boundary.

## Entities mentioned

- [World Labs](../entities/world-labs.md) — author.
- [Fei-Fei Li](../entities/fei-fei-li.md) — co-author, CEO.
- [Marble](../entities/marble.md) — World Labs' product; splats + collision meshes.
- [Genie 3](../entities/genie-3.md) — named as a renderer.
- [Google DeepMind](../entities/google-deepmind.md) — Genie 3, Nano Banana.
- [NVIDIA](../entities/nvidia.md) — Omniverse, the >$1T TAM claim.
- **RTFM** — World Labs' real-time interactive renderer. No page; no technical detail given here beyond "generates frames in real time conditioned on user input."
- **Nano Banana** — Google image-generation model. No page.

## Concepts touched

- [World-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md) — the primary for it.
- [World model](../concepts/world-models/world-model.md) / [world-model simulators](../concepts/world-models/world-model-simulators.md).
- [World-action model](../concepts/world-models/world-action-model.md) — named in the post as "the new wave of World Action Models."
- [Spatial intelligence](../concepts/world-models/spatial-intelligence.md).
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md).
- [VLA models](../concepts/learning/vla-models.md).
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — the planner-candor paragraph.

## Open questions

- **RTFM has no technical documentation in the wiki.** Named as World Labs' real-time renderer and nothing else. Real-time frame generation conditioned on user input is the same claimed capability as [Genie 3](../entities/genie-3.md) and [Ctrl-World](../entities/ctrl-world.md); no comparison is possible from this source.
- **The linchpin claim is asserted, not demonstrated, here.** The post gives no evidence that a simulator-mastering model can in fact project into pixels and actions. World Labs' own [R2S2R results](world-labs-r2s2r.md), seven weeks later, are the attempt to supply it — and the wiki should read that post as this essay's evidence section, with the incentive that implies.
- **"A pretrained video renderer as the backbone for joint world-and-action prediction"** is cited as "a small but growing number of recent work" with **no citations**. The wiki holds the specific instances — [Cosmos 3](cosmos-3-technical-report.md), [Genie Envisioner](../entities/genie-envisioner.md) / GE-Sim2 — so this is a case where the wiki is more concrete than its source.
- **The trillion-dollar Omniverse TAM is a vendor estimate quoted by a second vendor.** Not independently sourced here.
