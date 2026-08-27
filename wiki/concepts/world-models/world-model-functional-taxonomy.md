---
title: World-model functional taxonomy (renderer / simulator / planner)
type: concept
created: 2026-08-07
updated: 2026-08-26
sources: 5
tags: [world-model, taxonomy, spatial-intelligence, policy, renderer, simulator, planner, pomdp]
---

**A functional taxonomy of world models**: sort them not by architecture but by **which output of the agent-world loop they produce**. Proposed by [World Labs](../../entities/world-labs.md) and [Fei-Fei Li](../../entities/fei-fei-li.md) in ["A Functional Taxonomy of World Models"](../../sources/world-labs-functional-taxonomy.md) (2026-06-03), and carried into policy — with additions — by the [HAI world-model brief](../../sources/hai-world-model-spatial-intelligence-brief.md).

> [!note] Two layers, kept apart
> This page separates **what the primary essay argues** from **what Stanford HAI added when it adopted the framework**. An earlier version of this page blended them, attributing the brief's governance apparatus to the taxonomy itself. The essay contains no governance content at all. Section headings below mark the provenance.

## The derivation (primary)

The taxonomy is not a list of three system types someone noticed. It falls out of the **POMDP loop** that RL textbooks — "including the canonical Sutton and Barto" — have drawn for decades, and which the essay says is where the term *world model* got its technical meaning:

> An agent takes **actions**. Actions change the **state** of the world. The agent never sees state directly; what reaches it are **observations**. New observations inform new actions.

Three quantities in the loop, therefore three things a "world model" can output:

| Category | Outputs | Contract |
|---|---|---|
| **Renderer** | **Observations** | Purely visual. "The model carries no explicit understanding of three-dimensional structure. It produces what a viewer would see, **not what is**." |
| **Simulator** | **State** | Structural. "Geometry that holds up under inspection, physics that respects Newton's laws." |
| **Planner** | **Actions** | Given an observation and a goal, decide what to do next. |

Two consequences the prose version of this taxonomy loses:

- **Renderer and planner are formal inverses.** A renderer takes actions in and puts observations out; a planner takes observations in and puts actions out. They close opposite halves of the same loop.
- **"State" is the roboticist's sense** — a complete description of every object, position, velocity and property, "complete in principle, but never directly visible to any agent inside it." Not solid/liquid/gas, and not "the current frame."

## The categories in practice

| Category | Primary outputs | Named exemplars | Applications | Maturity |
|---|---|---|---|---|
| **Renderer** | Images, video, interactive real-time views | [Genie 3](../../entities/genie-3.md), World Labs **RTFM**, Google **Nano Banana**, text-to-video; [Marble](../../entities/marble.md) and Tencent HY-World 2.0 for explorable scenes | Architecture/design visualization, film, digital content | **Most mature** — "renderer-quality image generation in the hands of potentially hundreds of millions of users" |
| **Simulator** | Environments obeying physics; geometry a program can compute on | [Marble](../../entities/marble.md) (Gaussian splats **+ collision meshes**), NVIDIA [Omniverse](../../entities/nvidia.md) | Crash test, digital twins, surgical practice, robot/AV training | Conventional simulation mature; ***learned* simulation early and data-limited** |
| **Planner** | Actions, trajectories, policies | [VLA models](../learning/vla-models.md), model-based systems, [world-action models](world-action-model.md) | Robotics, AVs, warehouses, healthcare logistics, defense | **Least mature** — see the candor quote below |

The simulator is the only one with **two classes of consumer at once**: human professionals who need accuracy beyond visual plausibility, and *programs* — RL agents, robot controllers, AVs — that use it as a training ground.

## Simulation is the linchpin (primary — and the essay's actual thesis)

The framework is usually cited for its three boxes. The essay's argument is the **ranking** inside them, and it is a claim about **dependency order**, not maturity:

> "If language is an abstraction of the world and pixels are a projection of it, then **geometry, physics, and dynamics are the world itself.**"

The simulator is therefore "the structural backbone from which both visual appearance (for renderers) and action consequences (for planners) can be derived." Hence the load-bearing sentence:

> **"A model that masters simulation can project its understanding into pixels for human consumption, and into action predictions for embodied agents. A model that masters only rendering, or only planning, cannot do either."**

And: *"Of the three categories, the simulator gets the least public attention, and is the most consequential of the three."*

> [!note] Read the incentive alongside the argument
> This is a company research-positioning essay, and the company's product is the one it names as dissolving the renderer/simulator boundary. The argument may still be right — but the wiki should note that "the underattended category is the most consequential one, and it is ours" is a self-serving shape. The [R2S2R results](../../sources/world-labs-r2s2r.md) seven weeks later are World Labs' own attempt to supply the missing evidence, and are explicitly framed as putting "that argument to the test."

**Why the ordering is the interesting part.** The maturity gradient runs exactly opposite to the value gradient. Renderers are commercially mature and optimized for **plausibility rather than underlying truth** — a renderer can produce a photorealistic hospital wing without capturing how people, materials or infrastructure would behave inside it. "Their outputs are beautiful, but they cannot be trusted to design a building or train a robot." Planners touch the physical world and are least mature. Everything in between — [sim-to-real](../learning/sim-to-real-transfer.md), the [visual plausibility trap](world-model-evaluation.md), the whole [robot-policy-evaluation](../robotics/robot-policy-evaluation.md) literature — lives in the gap between "looks right" and "acts right."

### The candor on planners

Unusually blunt for a vendor, and corroborating the wiki's own evaluation thread from the commercial side:

> "Almost all have been confined to heavily constrained laboratory setups, with narrow object sets and short task horizons. **None have been validated at the complexity, variability, or duration that real-world deployment demands.**" ([taxonomy essay](../../sources/world-labs-functional-taxonomy.md))

That is the same verdict as [robot policy evaluation](../robotics/robot-policy-evaluation.md) reaches from statistics, [LIBERO-PRO](../../sources/libero-pro-paper.md) from memorization, and [RoboLab](../../sources/nvidia-robolab-evaluation-blog.md) from benchmark saturation — reached instead by someone selling into the category.

### The four hard problems, all in the simulator row

1. **3D data scarcity** — geometry + material + physical annotations are "orders of magnitude scarcer than the internet video that renderers train on."
2. **[Sim-to-real gap](../learning/sim-to-real-transfer.md)** persists.
3. **Generative-geometry risk, new with learned simulators** — "AI-generated geometry can look correct while containing self-intersections or wrong scale that produce nonsensical physics." Note this is the *inverse* of the plausibility trap: not pixels that look right and aren't, but geometry that looks right and isn't.
4. **Multi-physics cost** — rigid + deformable + fluid + cloth interacting is "orders of magnitude more expensive than single-domain simulation."

## The categories are collapsing (primary)

"The knowledge required to render a world, simulate it, and act in it is largely the same." A model that truly understands how a cup sits on a table should be able to render it from any angle, simulate what happens when it is pushed, and plan a hand to pick it up. **"The three categories are three projections of a single underlying understanding."**

Two named mechanisms, and the wiki holds instances of both:

| Collapse | Essay's claim | Wiki's instances |
|---|---|---|
| **Renderer → planner** | "A pretrained video renderer can be used as the backbone for joint world-and-action prediction" (no citations given) | [Cosmos 3](../../sources/cosmos-3-technical-report.md) — one omnimodal model that is forward-dynamics, inverse-dynamics, VLM and policy at once; [Genie Envisioner](../../entities/genie-envisioner.md) / GE-Sim2, action as a first-class variable inside a video generator |
| **Renderer → simulator** | "[Marble](../../entities/marble.md) already outputs Gaussian splats and collision meshes from a single model" | [World-model simulators](world-model-simulators.md) |

Direction of travel across all three: **"Every level is moving from passive output to interactive system"** — renderers becoming action-conditioned, simulators more controllable and editable, planners deliberating rather than reacting.

**The endpoint** is "one foundation model that can render photorealistic views, produce physically accurate structure, and plan action sequences, switching between output modalities depending on what the downstream consumer needs." The [world-action model](world-action-model.md) page is the architectural name for this. The essay's stated open problem is the tension inside it: **"Optimizing for visual beauty can sacrifice the precision a robot or a high-fidelity simulation needs. Reconciling these tensions inside a single architecture is the defining open problem in world model research today."**

## What the HAI brief added (not in the primary)

The [brief](../../sources/hai-world-model-spatial-intelligence-brief.md) adopts the three categories and builds a policy apparatus on top that the essay does not contain.

**Interactivity as an emergent fourth thing.** When the three functions run together in a **real-time, action-conditioned loop**, a further capability emerges: people and machines act within a modeled world and use the feedback to guide action in the physical one — a surgeon rehearsing in responsive simulated anatomy, a warehouse robot practicing before entering the facility. The brief's claim is that interactivity "is thus a natural consequence of a capable world model and where its most valuable uses lie."

> [!warning] Do not build regulatory thresholds on these categories
> The brief is blunt about its framework's shelf life: renderers are becoming interactive, simulators more generative, planners more capable of reasoning, and "at the research frontier, unified models increasingly combine rendering, simulation, and control within a single network." Its conclusion — **"capability thresholds defined per category are easily gamed or outgrown; consequently, safeguards must attach to the deployment context rather than to the model class."**

So the taxonomy's durable use is **not** classification of systems. It is classification of **uses**, which is what determines how hard the system should be tested — see [world-model evaluation](world-model-evaluation.md), where the brief's evaluation ladder is keyed to exactly these three roles. The brief also calls for **public pools of shared action data**; the essay does not.

## World model as runtime verifier (neither source)

A function this taxonomy does not have. [FOREWARN](../../sources/forewarn-paper.md) uses a frozen **[DreamerV3](../../entities/dreamer.md)** RSSM not to plan and not to generate training data, but to **predict the outcomes of a separate policy's candidate action plans so a VLM can judge them**. The world model is the *foresight* half of a verifier; the VLM is the *forethought* half, reading predicted latents through a linear adapter into its token space.

- **The latents are more useful to the VLM than decoded images.** Narration accuracy 0.82 from predicted latents versus **0.52 for GPT-4o shown ground-truth future frames** — a world model's compressed state can be a *better* interface to a language model than pixels are, at least for fine-grained contact detail.
- **The world model is deliberately trained on the base policy's failures as well as its successes**, because a verifier must predict the outcomes of bad plans. That is a different data requirement from world models trained for planning or video prediction.

A fourth output — *a judgment about a proposed action* — is not one of the loop's three quantities, which is a real limit on the POMDP derivation's completeness.

## Related concepts

- [World model](world-model.md) — the architecture-first taxonomy (generative-video / JEPA / frozen-feature / MBRL / omnimodal) that this one cuts across.
- [World-model simulators](world-model-simulators.md) — the "simulator" row, as this wiki had already carved it.
- [Real-to-sim-to-real](../robotics/real-to-sim-to-real.md) — World Labs' own bid to make the linchpin claim true.
- [World-action model](world-action-model.md) — the unified endpoint.
- [Spatial intelligence](spatial-intelligence.md) — the capability the stack composes into.
- [World-model governance](../safety/world-model-governance.md) — why safeguards attach to deployment context instead.

## Mentioned in

- [A Functional Taxonomy of World Models](../../sources/world-labs-functional-taxonomy.md) — **the primary.**
- [Building Worlds That Train Robots (R2S2R)](../../sources/world-labs-r2s2r.md) — the same authors testing their own linchpin claim.
- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../../sources/hai-world-model-spatial-intelligence-brief.md) — the policy adoption, with additions.
- [FOREWARN paper](../../sources/forewarn-paper.md) — the verifier role the taxonomy lacks.
