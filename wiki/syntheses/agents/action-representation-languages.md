---
title: Action representation languages — can an LLM speak robot in human-readable words?
type: synthesis
created: 2026-08-04
updated: 2026-08-04
tags: [action-representation, controlled-natural-language, cross-embodiment, code-as-policy, control-abstraction-levels, latent-actions, rt-h, vla, interface-design]
---

# Action representation languages — can an LLM speak robot in human-readable words?

**The question.** Does a language exist for specifying robot actions that is a *subset of natural language* — human-readable, LLM-generatable, and interpretable onto any embodiment?

**The short answer.** Several things fit parts of the description; none has all three properties; and the two most desirable ones — **human-readability** and **embodiment-agnosticism** — are currently being pursued by two research programs that are *diverging*, not converging. There is no ratified standard: no ISO, no ROS specification, no cross-lab vocabulary. Everything below is learned per-paper and non-portable.

> [!note] The term for what's being asked for
> In formal linguistics this is a **controlled natural language** (CNL) — a restricted grammar and closed lexicon that reads as English but parses deterministically. Working examples exist in other domains: Attempto Controlled English, and ASD **Simplified Technical English**, which is mandatory for civil-aviation maintenance documentation. **No robot-action CNL has been standardized.** That gap is the actual answer to the question; the rest of this page is why it persists.

## The spectrum

Every row is a real, used representation. Read the last two columns together — they are where the tension lives.

| Representation | Example | Human-readable | Embodiment-agnostic | Who does the grounding |
|---|---|---|---|---|
| **Free-form task language** | *"clean the kitchen"* | ✅ | ✅ | Everything below it |
| **Semantic subtask** ([π0.5](../../entities/pi-zero-5.md)) | *"pick up the cutting board"* | ✅ | ✅ | A learned VLA, per embodiment |
| **Language motions** ([RT-H](#rt-h-the-closest-existing-thing)) | *"move arm forward," "close gripper"* | ✅ | ◐ arm-shaped | A learned VLA + the dataset's verb inventory |
| **Formal task language** (PDDL, LTL) | `(on block-a block-b)` | ✅ | ✅ symbolically | A planner + hand-written action models; says nothing about motion |
| **Behavior trees** | `Sequence[Approach, Grasp, Lift]` | ✅ structure | ❌ at the leaves | The human who wrote the leaf nodes |
| **Code + API** ([code-as-policy](../../concepts/agents/code-as-policy.md)) | `stack_objs_in_order([...])` | ✅ | ❌ | **The API designer** — see [CaP-X](../../sources/cap-x-paper.md) below |
| **Visual trace** ([MolmoAct](../../entities/molmoact.md)) | a 2D polyline drawn on the image | ✅ *visually* | ◐ | The policy; **beat language for steering** |
| **Action-as-text** ([VLA-0](../../entities/vla-0.md)) | `"142 87 201 …"` | ◐ legible, not meaningful | ❌ joint-space | Nothing — it *is* the action |
| **[FAST](../../entities/fast-action-tokenization.md) tokens** | DCT coefficients → tokens | ❌ | ❌ | — |
| **Unified latent tokens** (UniT, UniVLA) | codebook index `#4471` | ❌ **by construction** | ✅ **the point** | A shared RQ-VAE codebook |
| **Raw joint values** | `[0.21, −1.07, …]` | ❌ | ❌ | — |

## The central tension

Reading down the table, a pattern falls out that is stronger than any single row:

**Readability and portability are both cheap at the top and both expensive at the bottom — but usefulness runs the other way.** *"Clean the kitchen"* is perfectly readable and perfectly portable and specifies nothing. A joint vector specifies everything and transfers to no other robot. Every representation in between is a choice about **where the grounding work lives**, and the grounding work does not disappear — it relocates.

That reframes the original question. The surface syntax is not the hard part; almost any reasonable subset of English would serve. **The interpreter is the hard part**, and an interpreter is per-embodiment by definition.

## Three measurements in this wiki that bear on it

### 1. The abstraction does the work, not the model — and not the language

[CaP-X](../../sources/cap-x-paper.md) (ICML 2026) built an eight-rung ladder from human-written macros (`stack_objs_in_order()`, plus privileged state) down to bare signatures (`solve_ik()`, docstrings only). **Success falls monotonically as the macros are stripped away.** Their own conclusion is that much of a decade of code-as-policy results "belonged to the API designer rather than the model."

Applied here: **the more useful your action vocabulary, the more of the problem was solved by whoever chose the verbs.** A rich, readable action language is a human-authored controller wearing a vocabulary costume. That is not a criticism — it is a correct and reusable engineering move — but it means the artifact of value is the *grounding of each term*, not the term list, and the term list is what looks like a language.

One consolation from the same paper: **test-time compute substitutes for abstraction.** Multi-turn reasoning over low-level primitives (M4) reaches parity with multi-turn over human macros. You can buy back the abstraction penalty at runtime instead of hard-coding it — so a *thin* vocabulary plus an iterating agent is a viable point on the curve.

### 2. Language may be the wrong modality for spatial action

[MolmoAct](../../sources/molmoact-paper.md) emits a decodable 2D trajectory over the image and lets you redirect the robot by **editing that trace**. Ai2 report this is *"more reliable than language commands, which can suffer from ambiguity."*

This is a head-to-head between two human-readable intermediate representations — one linguistic, one visual — and **the picture won**. *"Move the arm a bit left"* has no metric referent; a dragged polyline does. Any proposal for a natural-language action layer has to answer this directly, because for the spatial subset of actions there is now evidence the readable-but-non-linguistic option is better.

### 3. Semantic English beats a closed vocabulary — measurably

The [TurboVLA](../../sources/turbovla-paper.md) ablation (n = 2,000, so this separates) is the cleanest existing datapoint on how much *linguistic* content a robot policy actually uses:

| Instruction encoding | LIBERO avg |
|---|---|
| None | 70.8 (Goal suite collapses 97.4 → **11.6**) |
| **Learned task-ID embedding** (a maximally closed vocabulary) | **95.4** |
| Semantic natural language | **97.7** |

A task ID is the degenerate CNL — a closed set of opaque symbols. It recovers most of the gap but stays a **statistically real 2.3 pp short** (p = 0.0001). So natural language carries something past task identity even at execution level: compositional structure over objects, attributes, and spatial relations. **Constraining the grammar risks throwing exactly that away** — and this experiment shows the cost is measurable.

## Why 2026's cross-embodiment work went the other way

This is the update that should move a prior. The last year's cross-embodiment effort converged on **unified latent tokens**, explicitly trading away readability:

- [**UniT**](https://arxiv.org/pdf/2604.19734) — encodes heterogeneous cross-embodiment vision/action pairs into a shared **RQ-VAE codebook**, yielding embodiment-agnostic "unified latent action" tokens that capture physical intent without naming it.
- [**Universal action tokenization / action priors**](https://arxiv.org/abs/2606.26095) — one shared tokenizer so a single autoregressive VLA emits actions across morphologies.
- [**UniVLA**](../../entities/univla.md) (RSS 2025) — task-centric latent actions as the cross-embodiment interface; in this wiki as a stub via TurboVLA's table.

Every one of these is a **codebook index**. The field's best current answer to *"maps to any embodiment"* is deliberately unreadable, because the shared structure across a suction gripper, a parallel jaw, and a five-finger hand turned out not to be nameable in words — it is a learned manifold, and the tokens are coordinates on it.

**This is the crux.** The question asks for readability *and* portability. The 2026 evidence is that portability was purchased *with* readability.

## <a id="rt-h-the-closest-existing-thing"></a>RT-H — the closest existing thing

[**RT-H: Action Hierarchies Using Language**](https://arxiv.org/abs/2403.01823) (Belkhale et al., DeepMind + Stanford, 2024; [project page](https://rt-hierarchy.github.io/)) inserts precisely the layer the question describes. Between the high-level task and the motor action sits a vocabulary of short English phrases — *"move arm forward," "close gripper," "rotate arm right."* The policy predicts the **language motion** first, then the action conditioned on it and the task, with visual context at every stage.

Two properties worth stealing:

1. **Shared structure across disparate tasks.** "Move arm forward" is the same motion whether wiping a plate or opening a drawer, so data pools across tasks that otherwise share no supervision. This is the strongest argument for a linguistic middle layer that isn't about human convenience at all — it's a **data-efficiency** argument.
2. **Correction at the layer the policy was trained on.** A human can say "no, move left" mid-episode and the policy consumes it natively — a flexible-policy paradigm that raw action prediction cannot offer. (Read against MolmoAct's finding above: language correction *works*, it just lost to trace editing on reliability.)

The limits: the vocabulary is **derived from the dataset rather than specified**, and it is arm-shaped — *"close gripper"* does not survive transfer to a suction cup or a five-finger hand. It is a learned dialect, not a language.

> [!warning] Not ingested
> RT-H is cited here from its abstract and project page, not a full read. It is the **top ingest candidate** this page generates — the wiki has no coverage of it, and it is the single most relevant prior work to this question.

## What actually deploys today

The layer that is genuinely readable, genuinely portable, and genuinely in production is **semantic subtask text**: plain English at the granularity of *"pick up the cutting board."* [π0.5](../../entities/pi-zero-5.md) runs exactly this internally — predict the semantic subtask, then the action chunk conditioned on it, one model, two levels. [Helix](../../sources/helix-blog.md) and [GR00T](../../entities/nvidia-groot.md) split the same way across their System 2 / System 1 tiers, and [TurboVLA](../../entities/turbovla.md)'s conclusion proposes it again with a much cheaper executor.

It is **not a specified language.** It is free-form English, and it works because a learned policy underneath grounds it — per embodiment, at training time. Which is the same conclusion the spectrum table reaches from the other end.

## A design sketch, if you wanted to build one

Two layers, and be explicit about which is portable:

- **Semantic layer — specified, portable, version-controllable.** A closed verb set × object reference × constraint clause: `GRASP(obj, approach=top, force=light)`. Readable, LLM-generatable, diffable in git, reviewable by a human before execution. This is the CNL.
- **Grounding contract — declarative, per-embodiment, not portable.** A map from each verb to that robot's primitive, with its own preconditions and failure modes. [Rosetta](../../sources/rosetta-github.md) already has this shape for ROS 2 — YAML contracts mapping topics to [LeRobot](../../entities/lerobot.md) features declaratively, no Python driver class required. It is aimed at *data* rather than *actions*, but it is the closest existing artifact in this wiki to the interface being described, and the pattern transfers.

The honest accounting: layer one is the part that looks like a language and is nearly free. Layer two is the part that costs, does not transfer, and is where CaP-X says the performance actually comes from. **A new robot means a new grounding contract, always.** What the CNL buys is that the *planner* above it, the *logs*, and the *human review surface* stay unchanged — which is a real and underrated win, just not the win the original question was reaching for.

## The experiment worth running first

Cheap, decisive, and it reuses an existing design. **Replicate TurboVLA's instruction-encoding ablation with a third condition.**

| Condition | Expected role |
|---|---|
| Free-form natural language | 97.7 — the baseline |
| **Your controlled vocabulary (CNL)** | **the measurement** |
| Learned task-ID embedding | 95.4 — the closed-vocabulary floor |

At n = 2,000 on [LIBERO](../../entities/libero.md), ~1 pp separates. If CNL lands at parity with free-form English, **readability is free** and you should take it everywhere. If it lands near the task-ID floor, the constrained grammar has discarded the compositional semantics that were doing the work — and you have learned that in one training run, on four consumer GPUs, before building any infrastructure on top of it.

A second, harder run settles the portability half: train the grounding contract on one embodiment, swap the arm, and measure how much of the CNL survives. That is the experiment nobody in the cited literature has published.

## Open gaps in this wiki

This page is built partly on external references because the wiki lacks coverage of an entire relevant tradition:

- **[RT-H](https://arxiv.org/abs/2403.01823)** — un-ingested; the most directly relevant prior work.
- **PDDL / LTL / temporal-logic task specification** — no page. The classical AI-planning answer to "human-readable, embodiment-agnostic action specification," 50 years old, and the wiki has nothing on it.
- **Behavior trees** — no page, despite being the dominant *deployed* action-composition formalism in industrial and game robotics.
- **UniT / universal action tokenization** — un-ingested; would anchor a `latent-action-tokens` concept page that [UniVLA](../../entities/univla.md) also points at.
- **Controlled natural languages** generally — no page; the transferable prior art is in aerospace documentation, not robotics.

## Related
- [Control abstraction levels](../../concepts/robotics/control-abstraction-levels.md) — *where* a controller acts; this page is about *what it says* at that level.
- [Code as policy](../../concepts/agents/code-as-policy.md) — the action vocabulary as arbitrary code; the winning representation so far, and the least portable.
- [LLM-agent architecture](../../concepts/agents/llm-agent-architecture.md) — the parent pattern, where the action vocabulary is a discrete tool schema.
- [LLM-free VLA](../../concepts/learning/llm-free-vla.md) — the counterpart finding: language *semantics* are load-bearing while language *models* may not be.
- [VLA models](../../concepts/learning/vla-models.md) — the action-head taxonomy, which is the bottom three rows of the spectrum table.
- [Control-rate ladder](../../syntheses/platforms/control-rate-ladder.md) — why the hierarchy exists at all: nothing readable runs at 83 Hz.
