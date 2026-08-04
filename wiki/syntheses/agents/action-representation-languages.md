---
title: Action representation languages — can an LLM speak robot in human-readable words?
type: synthesis
created: 2026-08-04
updated: 2026-08-04
tags: [action-representation, controlled-natural-language, cross-embodiment, code-as-policy, control-abstraction-levels, latent-actions, rt-h, vla, interface-design]
---

# Action representation languages — can an LLM speak robot in human-readable words?

**The question.** Does a language exist for specifying robot actions that is a *subset of natural language* — human-readable, LLM-generatable, and interpretable onto any embodiment?

**The short answer.** Several things fit parts of the description; none has all three properties; and the two most desirable ones — **human-readability** and **embodiment-agnosticism** — are currently being pursued by two research programs that are *diverging*, not converging. There is no ratified standard: no ISO, no ROS specification, no cross-lab vocabulary.

**But the readable option is not merely a nicety, and that is the page's most useful finding.** Two independent experiments — [RT-H](../../sources/rt-h-paper.md) at 55B in 2024 and [TurboVLA](../../sources/turbovla-paper.md) at 0.2 B in 2026 — hold the underlying partition fixed, swap English phrases for opaque integer labels, and both lose accuracy. **The words earn their keep.** What has never been demonstrated is the other half: a readable vocabulary that survives a change of morphology.

> [!note] The term for what's being asked for
> In formal linguistics this is a **controlled natural language** (CNL) — a restricted grammar and closed lexicon that reads as English but parses deterministically. Working examples exist in other domains: Attempto Controlled English, and ASD **Simplified Technical English**, which is mandatory for civil-aviation maintenance documentation. **No robot-action CNL has been standardized.** That gap is the actual answer to the question; the rest of this page is why it persists.

## The spectrum

Every row is a real, used representation. Read the last two columns together — they are where the tension lives.

| Representation | Example | Human-readable | Embodiment-agnostic | Who does the grounding |
|---|---|---|---|---|
| **Free-form task language** | *"clean the kitchen"* | ✅ | ✅ | Everything below it |
| **Semantic subtask** ([π0.5](../../entities/pi-zero-5.md)) | *"pick up the cutting board"* | ✅ | ✅ | A learned VLA, per embodiment |
| **Language motions** ([RT-H](../../entities/rt-h.md)) | *"move arm forward and close gripper"* | ✅ | ❌ *grammar ports, lexicon doesn't* | A fixed extraction grammar over **this robot's 9 action dims** |
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

## Four measurements in this wiki that bear on it

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

### 4. …and the same result holds at 55B, from the opposite direction

[RT-H](../../sources/rt-h-paper.md)'s **OneHot ablation** is the cleanest version of this experiment anywhere, because it isolates the surface form perfectly: take RT-H's 2,500 language motions, **relabel each one as an integer**, change nothing else. The partition is identical; only the words are gone. Performance drops **substantially**. The authors' conclusion:

> *"while action hierarchy itself gets us part of the way, **the structure of language greatly improves language motion and action prediction**."*

A companion ablation sharpens it. RT-H-**Cluster** replaces the labeling procedure with K-means over raw actions — a *different, finer* partition with integer labels. It does slightly worse on average but **better on the hardest precision tasks**, because finer clusters give the action decoder more guidance while being harder for the upstream query to predict. That is the abstraction tradeoff, measured within one paper.

> [!note] Two independent confirmations, two years and 275× of scale apart
> RT-H-OneHot (2024, [PaLI-X](../../entities/pali-x.md) 55B, real mobile manipulator, in-house data) and TurboVLA's task-ID ablation (2026, 0.2 B, [LLM-free](../../concepts/learning/llm-free-vla.md), LIBERO) are **the same experiment on opposite ends of the scale and architecture spectrum**, and they agree: *a closed set of opaque labels over the same partition underperforms natural language.*
>
> **This is the strongest evidence on this page that a readable action vocabulary is not merely a convenience** — it earns its keep in accuracy. It also directly qualifies measurement 1: CaP-X says the *abstraction* carries the performance, but these two say the *words* carry some of it independently, presumably by reaching a pretrained model's compositional priors. Note the untested confound: RT-H's advantage may come from PaLI-X's internet-scale prior, and nobody has run the two designs head to head.

## Why 2026's cross-embodiment work went the other way

This is the update that should move a prior. The last year's cross-embodiment effort converged on **unified latent tokens**, explicitly trading away readability:

- [**UniT**](https://arxiv.org/pdf/2604.19734) — encodes heterogeneous cross-embodiment vision/action pairs into a shared **RQ-VAE codebook**, yielding embodiment-agnostic "unified latent action" tokens that capture physical intent without naming it.
- [**Universal action tokenization / action priors**](https://arxiv.org/abs/2606.26095) — one shared tokenizer so a single autoregressive VLA emits actions across morphologies.
- [**UniVLA**](../../entities/univla.md) (RSS 2025) — task-centric latent actions as the cross-embodiment interface; in this wiki as a stub via TurboVLA's table.

Every one of these is a **codebook index**. The field's best current answer to *"maps to any embodiment"* is deliberately unreadable, because the shared structure across a suction gripper, a parallel jaw, and a five-finger hand turned out not to be nameable in words — it is a learned manifold, and the tokens are coordinates on it.

**This is the crux.** The question asks for readability *and* portability. The 2026 evidence is that portability was purchased *with* readability.

## <a id="rt-h-the-closest-existing-thing"></a>RT-H — the closest existing thing

[**RT-H: Action Hierarchies Using Language**](../../sources/rt-h-paper.md) (Belkhale, …, [Sadigh](../../entities/dorsa-sadigh.md); DeepMind + Stanford, 2024) inserts precisely the layer the question describes. Between the high-level task and the motor action sits a vocabulary of short English phrases — *"move arm forward," "close gripper," "rotate arm right."* One [PaLI-X](../../entities/pali-x.md) 55B VLM predicts the **language motion** first, then the action conditioned on it, the task, and the image.

### <a id="what-the-rt-h-ingest-changed"></a>What the RT-H ingest changed

**Correction.** This page first said RT-H's vocabulary is "derived from the dataset, not specified in advance." That is wrong in an interesting way. The vocabulary is extracted **mechanically from proprioception** by a *fixed, hand-designed procedure*: map each of the robot's 9 action dimensions to a spatial word (position z → "up"/"down"), threshold out dimensions below a "small action" cutoff, and compose the survivors in order of magnitude → *"move arm forward and close gripper."* The combinatorics yield **2,500+ phrases with zero human annotation**, and the procedure is fixed across every task and dataset — *"designing this procedure is a one-time fixed cost for the developer."*

So RT-H is **a genuine controlled natural language**: a *specified generative grammar* (axis words × sign × composition order) over an *induced lexicon*. That is a far better fit to the original question than the abstract suggests — and it was reached by rejecting human labeling outright, because annotators produced *"language inconsistency across the dataset and even inaccuracy,"* mislabeling skill transitions and misjudging direction from camera angles.

**And it makes the embodiment coupling exact.** The 9 dimensions are *this* robot's: 3 arm-position deltas, 3 rotation deltas, **2 mobile-base**, 1 parallel gripper. A suction cup, a five-finger hand, or a fixed-base arm changes the dimension list, hence the extraction, hence the entire lexicon. **The grammar ports; the vocabulary cannot.** This is the sharpest illustration on the page of why readability and portability keep failing to co-occur — the readable names are *names for this robot's degrees of freedom*.

### What's worth stealing

1. **Data sharing at the motion layer — a data-efficiency argument, not an ergonomics one.** *"Pour a cup"* and *"pick up a coke can"* share no task-level semantics but **entirely overlap at the language motion level** until the object is picked. This is the strongest reason to want a readable middle layer, and it has nothing to do with humans reading it.
2. **Corrections are cheap to learn from.** A human types a replacement phrase mid-episode; afterward **only the motion query is retrained**, since the action query already executes the corrected phrase. **40% → 63% with 30 correction episodes per task** (p = 0.0036), versus teleop-corrected RT-2-IWR at 13%. Correcting in a compressed, readable space beats correcting in action space by 50 pp.
3. **The phrases are contextual, not primitives.** *"Move arm left"* means "move the packet above the bowl" in one scene and "latch the lid onto the jar" in another — different speeds, axes, and gripper poses. *"It would be immensely challenging to design a single 'move arm left' primitive to capture this contextuality."* A CNL whose terms are *interpreted by a learned policy* is strictly more expressive than the same terms bound to scripted primitives.
4. **The bottleneck is naming, not executing.** Offline action MSE using ground-truth motions is **40% lower** than end-to-end — the action query is much better than the system. Which is exactly why intervening at the language layer pays.

### The limits

Absolute success is **63%** after corrections. The hierarchy adds failure modes a flat model lacks (oscillation; getting stuck re-predicting *"close gripper"*). Correction quality is capped by the action query — when a phrase overshoots, the operator's only recourse is more phrases, and *"this can make the process slower than teleoperation."* The claimed object-generalization win (65% vs 55%, n=50) is a **statistical tie** (p = 0.31).

> [!warning] The cross-embodiment version was proposed here in 2024 and never executed
> RT-H's own Future Work names the exact question this page asks: language motions *"could even be used to help bridge datasets with many different embodiments like [OXE](../../entities/open-x-embodiment.md), or even to learn from human videos with actions described only in language."*
>
> The 2026 cross-embodiment literature went to **unified latent tokens** instead. Whether the language route was tried and failed, or simply not attempted, is unrecorded — and that gap is the single most interesting unknown on this page. The most relevant test is cheap and stated above: **re-run RT-H's extraction grammar on a different morphology and see whether the induced lexicons are compatible.**

## What actually deploys today

The layer that is genuinely readable, genuinely portable, and genuinely in production is **semantic subtask text**: plain English at the granularity of *"pick up the cutting board."* [π0.5](../../entities/pi-zero-5.md) runs exactly this internally — predict the semantic subtask, then the action chunk conditioned on it, one model, two levels. [Helix](../../sources/helix-blog.md) and [GR00T](../../entities/nvidia-groot.md) split the same way across their System 2 / System 1 tiers, and [TurboVLA](../../entities/turbovla.md)'s conclusion proposes it again with a much cheaper executor.

It is **not a specified language.** It is free-form English, and it works because a learned policy underneath grounds it — per embodiment, at training time. Which is the same conclusion the spectrum table reaches from the other end.

## A design sketch, if you wanted to build one

Two layers, and be explicit about which is portable:

- **Semantic layer — specified, portable, version-controllable.** A closed verb set × object reference × constraint clause: `GRASP(obj, approach=top, force=light)`. Readable, LLM-generatable, diffable in git, reviewable by a human before execution. This is the CNL.
> [!note] The design move RT-H suggests: **specify the grammar, induce the lexicon**
> RT-H's vocabulary is not written by hand and not learned — it is *generated* by a fixed procedure from the robot's own action dimensions. Port that idea rather than the word list: **the portable artifact is the extraction grammar** (axis → word, threshold, magnitude-ordered composition), and each embodiment induces its own lexicon by running it. You get readability everywhere and consistency within an embodiment, without pretending "close gripper" means anything to a suction cup. Whether two induced lexicons are *mutually* interpretable is the open question above — and the cheapest experiment on this page.

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

- ~~RT-H — un-ingested~~ → **[primary-ingested 2026-08-04](../../sources/rt-h-paper.md)**. Closed. It also exposed that **[RT-2](../../entities/rt-2.md) and RT-1 have no pages** despite being the most-referenced un-ingested models in the wiki's VLA thread; RT-2 now has a stub built secondhand from RT-H.
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
