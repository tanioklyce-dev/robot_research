---
title: Action representation languages — can an LLM speak robot in human-readable words?
type: synthesis
created: 2026-08-04
updated: 2026-08-04
tags: [action-representation, controlled-natural-language, cross-embodiment, code-as-policy, control-abstraction-levels, latent-actions, rt-h, rt-2, pddl, behavior-trees, unit, vla, interface-design]
---

# Action representation languages — can an LLM speak robot in human-readable words?

**The question.** Does a language exist for specifying robot actions that is a *subset of natural language* — human-readable, LLM-generatable, and interpretable onto any embodiment?

**The short answer.** Several things fit parts of the description; none has all three properties; and the two most desirable ones — **human-readability** and **embodiment-agnosticism** — are currently being pursued by two research programs that are *diverging*, not converging. There is no ratified standard: no ISO, no ROS specification, no cross-lab vocabulary.

**But the readable option is not merely a nicety, and that is the page's most useful finding.** Three independent experiments — [RT-H](../../sources/rt-h-paper.md) at 55B on a real robot, [TurboVLA](../../sources/turbovla-paper.md) at 0.2 B on LIBERO, and [PDDL generalized planning](../../sources/generalized-planning-pddl-llm-paper.md) with no robot at all — hold the underlying structure fixed, swap human-meaningful names for opaque labels, and all three lose accuracy. In the PDDL case performance **collapses to near zero**, in a formalism where the names are *provably* unnecessary for the solver. **The words earn their keep.**

**And the question turns out to be two questions.** [Behavior trees](../../concepts/robotics/behavior-trees.md) make the *composition* readable while staying agnostic about the *action* — the only place on this page where readability and portability co-occur, because a BT never tried to name the robot's degrees of freedom. The architecture that would satisfy the original request is a BT with latent-token policies at its leaves. **Nobody has built it.**

> [!note] The term for what's being asked for
> In formal linguistics this is a **controlled natural language** (CNL) — a restricted grammar and closed lexicon that reads as English but parses deterministically. Working examples exist in other domains: Attempto Controlled English, and ASD **Simplified Technical English**, which is mandatory for civil-aviation maintenance documentation. **No robot-action CNL has been standardized.** That gap is the actual answer to the question; the rest of this page is why it persists.

## The spectrum

Every row is a real, used representation. Read the last two columns together — they are where the tension lives.

| Representation | Example | Human-readable | Embodiment-agnostic | Who does the grounding |
|---|---|---|---|---|
| **Free-form task language** | *"clean the kitchen"* | ✅ | ✅ | Everything below it |
| **Semantic subtask** ([π0.5](../../entities/pi-zero-5.md)) | *"pick up the cutting board"* | ✅ | ✅ | A learned VLA, per embodiment |
| **Language motions** ([RT-H](../../entities/rt-h.md)) | *"move arm forward and close gripper"* | ✅ | ❌ *grammar ports, lexicon doesn't* | A fixed extraction grammar over **this robot's 9 action dims** |
| **Formal task language** ([PDDL](../../concepts/agents/symbolic-task-planning.md)) | `(on block-a block-b)` | ✅ | ✅ symbolically | A planner + hand-written operators; **says nothing about motion** |
| **[Behavior trees](../../concepts/robotics/behavior-trees.md)** | `→[ ?[HasBall, Grasp], Lift ]` | ✅ **composition, not action** | ✅ tree / ❌ leaves | The leaf — which can be *any* policy, readable or not |
| **Code + API** ([code-as-policy](../../concepts/agents/code-as-policy.md)) | `stack_objs_in_order([...])` | ✅ | ❌ | **The API designer** — see [CaP-X](../../sources/cap-x-paper.md) below |
| **Visual trace** ([MolmoAct](../../entities/molmoact.md)) | a 2D polyline drawn on the image | ✅ *visually* | ◐ | The policy; **beat language for steering** |
| **Action-as-text** ([RT-2](../../entities/rt-2.md), [VLA-0](../../entities/vla-0.md)) | `"142 87 201 …"` | ◐ legible, not meaningful | ❌ joint-space | Nothing — it *is* the action |
| **[FAST](../../entities/fast-action-tokenization.md) tokens** | DCT coefficients → tokens | ❌ | ❌ | — |
| **[Unified latent tokens](../../concepts/learning/latent-action-tokens.md)** ([UniT](../../entities/unit.md), [UniVLA](../../entities/univla.md)) | codebook index `#4471` | ❌ **by construction** | ✅ **the point** | A shared RQ-VAE codebook, visually anchored |
| **Raw joint values** | `[0.21, −1.07, …]` | ❌ | ❌ | — |

## The central tension

Reading down the table, a pattern falls out that is stronger than any single row:

**Readability and portability are both cheap at the top and both expensive at the bottom — but usefulness runs the other way.** *"Clean the kitchen"* is perfectly readable and perfectly portable and specifies nothing. A joint vector specifies everything and transfers to no other robot. Every representation in between is a choice about **where the grounding work lives**, and the grounding work does not disappear — it relocates.

That reframes the original question. The surface syntax is not the hard part; almost any reasonable subset of English would serve. **The interpreter is the hard part**, and an interpreter is per-embodiment by definition.

## The measurements that bear on it

### 1. The abstraction does the work, not the model — and not the language

[CaP-X](../../sources/cap-x-paper.md) (ICML 2026) built an eight-rung ladder from human-written macros (`stack_objs_in_order()`, plus privileged state) down to bare signatures (`solve_ik()`, docstrings only). **Success falls monotonically as the macros are stripped away.** Their own conclusion is that much of a decade of code-as-policy results "belonged to the API designer rather than the model."

Applied here: **the more useful your action vocabulary, the more of the problem was solved by whoever chose the verbs.** A rich, readable action language is a human-authored controller wearing a vocabulary costume. That is not a criticism — it is a correct and reusable engineering move — but it means the artifact of value is the *grounding of each term*, not the term list, and the term list is what looks like a language.

One consolation from the same paper: **test-time compute substitutes for abstraction.** Multi-turn reasoning over low-level primitives (M4) reaches parity with multi-turn over human macros. You can buy back the abstraction penalty at runtime instead of hard-coding it — so a *thin* vocabulary plus an iterating agent is a viable point on the curve.

### 2. Language may be the wrong modality for spatial action

[MolmoAct](../../sources/molmoact-paper.md) emits a decodable 2D trajectory over the image and lets you redirect the robot by **editing that trace**. Ai2 report this is *"more reliable than language commands, which can suffer from ambiguity."*

This is a head-to-head between two human-readable intermediate representations — one linguistic, one visual — and **the picture won**. *"Move the arm a bit left"* has no metric referent; a dragged polyline does. Any proposal for a natural-language action layer has to answer this directly, because for the spatial subset of actions there is now evidence the readable-but-non-linguistic option is better.

### 3. A closed vocabulary has a measurable cost — the TurboVLA numbers

The [TurboVLA](../../sources/turbovla-paper.md) ablation (n = 2,000, so this separates) is the cleanest existing datapoint on how much *linguistic* content a robot policy actually uses:

| Instruction encoding | LIBERO avg |
|---|---|
| None | 70.8 (Goal suite collapses 97.4 → **11.6**) |
| **Learned task-ID embedding** (a maximally closed vocabulary) | **95.4** |
| Semantic natural language | **97.7** |

A task ID is the degenerate CNL — a closed set of opaque symbols. It recovers most of the gap but stays a **statistically real 2.3 pp short** (p = 0.0001). So natural language carries something past task identity even at execution level: compositional structure over objects, attributes, and spatial relations. **Constraining the grammar risks throwing exactly that away** — and this experiment shows the cost is measurable.

This turns out to be one instance of a pattern that shows up three times.

### 4. The names result — three independent confirmations

[RT-H](../../sources/rt-h-paper.md)'s **OneHot ablation** is the cleanest version of this experiment anywhere, because it isolates the surface form perfectly: take RT-H's 2,500 language motions, **relabel each one as an integer**, change nothing else. The partition is identical; only the words are gone. Performance drops **substantially**. The authors' conclusion:

> *"while action hierarchy itself gets us part of the way, **the structure of language greatly improves language motion and action prediction**."*

A companion ablation sharpens it. RT-H-**Cluster** replaces the labeling procedure with K-means over raw actions — a *different, finer* partition with integer labels. It does slightly worse on average but **better on the hardest precision tasks**, because finer clusters give the action decoder more guidance while being harder for the upstream query to predict. That is the abstraction tradeoff, measured within one paper.

And a **third**, from a paradigm with no robot in it at all. [Silver et al.](../../sources/generalized-planning-pddl-llm-paper.md)'s **No Names** ablation renames every identifier in a [PDDL](../../concepts/agents/symbolic-task-planning.md) domain — predicates, operators, types, objects — to `predicate1`, `operator2`. GPT-4 is asked to synthesize a generalized planner as before. Performance **collapses**:

| Domain | With names | No names |
|---|---:|---:|
| Delivery | 0.90 | **0.10** |
| Forest | 1.00 | **0.11** |
| Gripper | 0.90 | **0.10** |
| Ferry | 0.80 | **0.00** |
| Heavy | 0.60 | **0.00** |

> [!note] Three independent confirmations, across paradigms that share nothing
> | | Year | Setting | Structure held fixed, names removed | Result |
> |---|---|---|---|---|
> | [RT-H-OneHot](../../sources/rt-h-paper.md) | 2024 | [PaLI-X](../../entities/pali-x.md) 55B VLA, real mobile manipulator | 2,500 language motions → integers | drops **substantially** |
> | [TurboVLA task-ID](../../sources/turbovla-paper.md) | 2026 | 0.2 B [LLM-free](../../concepts/learning/llm-free-vla.md) policy, LIBERO | instructions → learned task IDs | 97.7 → **95.4** (p=0.0001) |
> | [PDDL No-Names](../../sources/generalized-planning-pddl-llm-paper.md) | 2023 | GPT-4 program synthesis, **no robot, no perception** | identifiers → `predicate1` | 0.90 → **0.10** |
>
> A 55B VLA, a 0.2 B LLM-free policy, and a symbolic planner with no perception at all. **275× of scale, three architectures, and one shared finding: semantic names beat opaque labels over identical structure.**
>
> **PDDL is the sharpest case for two reasons.** The loss is not degradation but *collapse to near zero*. And PDDL is the one representation of the three that is **formally complete without names** — a classical planner solves the renamed domain exactly as well, reading only structure. The names exist purely for humans, and a language model needs them for the same reason a human does.
>
> **This is the strongest evidence on the page that a readable action vocabulary is not merely a convenience** — it earns its keep in accuracy. It also qualifies measurement 1: CaP-X says the *abstraction* carries the performance; these three say the *words* carry some of it independently, by reaching a pretrained model's compositional priors. Untested confound: all three consume models pretrained on human text, so this measures what such models need, not what is intrinsically necessary. A policy trained from scratch on robot data alone might not care.

## The axis the spectrum was hiding: composition vs. action

The [behavior trees](../../concepts/robotics/behavior-trees.md) ingest ([Colledanchise & Ögren](../../sources/behavior-trees-book.md)) exposes a distinction every other row on this page conflates.

The authors claim BTs are *"human readable due to their tree structure and modularity."* But that is **structural** readability, not action readability. A BT's whole vocabulary is six node types — Sequence (`→`, "and-then"), Fallback (`?`, "or-else"), Parallel, Decorator, Action, Condition — ticked continuously from the root, each returning Running / Success / Failure. What the tree makes legible is **what runs, in what order, under what guard, with what fallback**. It says nothing about what a leaf *is*.

**So the question splits in two, and the answers differ:**

| Question | Best available answer | Readable? | Portable? |
|---|---|---|---|
| Is the **action** readable? | [RT-H](../../entities/rt-h.md) language motions | ✅ | ❌ lexicon is per-embodiment |
| Is the **composition** readable? | [Behavior trees](../../concepts/robotics/behavior-trees.md) | ✅ | ✅ **tree ports; leaves don't** |

That second row is the only place on this page where readability and portability actually co-occur — because the BT never tried to name the robot's degrees of freedom in the first place.

> [!note] The architecture that would answer the original question, which nobody has built
> Put the unreadable representation at the leaves and the readable structure above it. A [UniT](../../entities/unit.md) token predictor or a [TurboVLA](../../entities/turbovla.md) policy sits at an Action node; the tree above stays auditable, guarded, diffable in git, and generatable by an LLM. You get the [latent-action](../../concepts/learning/latent-action-tokens.md) line's cross-embodiment portability *and* a human-legible control surface — without pretending "close gripper" means anything to a suction cup.
>
> **No source in this wiki does this.** BTs are twenty years old, formally analyzed (state-space safety proofs; stochastic BTs reduce to Markov chains yielding success probability and expected completion time), and shipped in ROS 2 via BehaviorTree.CPP and Nav2. The [guardrails synthesis](guardrails-for-robot-agents.md) separately found the **execution rail ships empty** in every stack examined. These two facts belong together and currently sit in different literatures.

The book is also honest about when BTs are *not* worth it: *"In applications where the robot operates in a very structured environment, predictable in space and time, BTs do not have any advantages over simpler architectures."* Checking all conditions every tick can be expensive; the engine is hard to implement correctly; and the mindset is tick-driven rather than event-driven.

## Why 2026's cross-embodiment work went the other way

This is the update that should move a prior. The last year's cross-embodiment effort converged on **unified latent tokens**, explicitly trading away readability:

- **[UniT](../../sources/unit-paper.md)** ([XPENG Robotics](../../entities/xpeng-robotics.md) + Tsinghua + HKU, 2026) — **primary-ingested 2026-08-04**, and it calls its codebook *"a unified physical language."* Three branches (visual, action, fusion) quantized by a **shared RQ-VAE codebook**, where every token must decode **both** the visual transition and the action chunk. **Visual anchoring** is the thesis: *"while human and humanoid kinematics differ in structural DoFs, the physical outcomes of their intents share a consistent visual representation."*
- [**Universal action tokenization / action priors**](https://arxiv.org/abs/2606.26095) — one shared tokenizer so a single autoregressive VLA emits actions across morphologies. Un-ingested.
- [**UniVLA**](../../entities/univla.md) (RSS 2025) — vision-only latent actions; UniT's own taxonomy files it as the design that *"entangles low-level appearance confounders."* Stub.

**What the latent route actually buys**, from UniT's numbers: **+18.9 pp** from the token-prediction objective alone (66.7 vs 47.8 for an architecturally identical GR00T baseline, n=1,200); **~10× data efficiency**; **0% → 60% zero-shot** on a task present only in human video, with emergent waist rotation copied from the human demonstrations; and **denoising** — at σ=0.2 injected noise [FAST](../../entities/fast-action-tokenization.md) degrades 10.7× and UniT only 1.7×, because kinematic variation with no visual correspondence gets discarded. t-SNE shows human and humanoid distributions *overlapping* under UniT and cleanly *separated* under raw-action conditioning — and the alignment propagates into the downstream VLA's and world model's internals.

One honest negative worth keeping: as a world-model conditioning interface UniT ≈ raw actions on **single-embodiment** DROID, and only pulls ahead under human-humanoid co-training. **The unified interface pays only when embodiments are actually mixed** — which is the precise scope of the claim.

Every one of these is a **codebook index**. The field's best current answer to *"maps to any embodiment"* is deliberately unreadable, because the shared structure across a suction gripper, a parallel jaw, and a five-finger hand turned out not to be nameable in words — it is a learned manifold, and the tokens are coordinates on it.

**This is the crux.** The question asks for readability *and* portability. The 2026 evidence is that portability was purchased *with* readability.

And the cost is specific, not abstract: a codebook index cannot be read, logged in human terms, or **corrected by an operator mid-episode** — the last of which took [RT-H](../../entities/rt-h.md) from 40% to 63% with 30 typed corrections per task. UniT does not cite RT-H. RT-H's own proposal to bridge [OXE](../../entities/open-x-embodiment.md) embodiments *using language motions* was never executed. **The two traditions are answering the same question and not talking to each other** — which remains the single clearest open question on this page.

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

Six sources ingested 2026-08-04 closed every gap this page originally listed. What replaced them:

- ~~RT-H un-ingested~~ → **[ingested](../../sources/rt-h-paper.md)**.
- ~~PDDL / LTL uncovered~~ → **[symbolic task planning](../../concepts/agents/symbolic-task-planning.md)** founded on [Silver et al.](../../sources/generalized-planning-pddl-llm-paper.md). **LTL and temporal-logic specification remain uncovered.**
- ~~Behavior trees uncovered~~ → **[behavior trees](../../concepts/robotics/behavior-trees.md)** founded on [Colledanchise & Ögren](../../sources/behavior-trees-book.md). **BehaviorTree.CPP and Nav2's BT navigator — the actual ROS 2 implementations — are not covered.**
- ~~UniT un-ingested~~ → **[latent action tokens](../../concepts/learning/latent-action-tokens.md)** founded on [UniT](../../sources/unit-paper.md). Universal action tokenization and UniVLA remain secondhand.
- ~~RT-2/RT-1 secondhand~~ → both **[primary](../../sources/rt-1-paper.md)**-**[ingested](../../sources/rt-2-paper.md)**.
- **Controlled natural languages** generally — still no page; the transferable prior art is in aerospace documentation (ASD Simplified Technical English), not robotics.
- **Task-and-motion planning (TAMP)** — newly exposed by the PDDL ingest and *not* closed. TAMP is the tradition that explicitly bridges symbolic action specifications to continuous motion, which is exactly the "says nothing about motion" limitation this page keeps hitting. [Kaelbling](../../entities/leslie-kaelbling.md) is a co-author on the ingested PDDL paper and a founder of that line.
- **The BT-over-VLA architecture** — no source, and the most valuable thing on this list.

## Related
- [Behavior trees](../../concepts/robotics/behavior-trees.md) — the composition layer, and the only readable-*and*-portable row here.
- [Symbolic task planning (PDDL)](../../concepts/agents/symbolic-task-planning.md) — the 50-year-old formal answer; complete without names, and an LLM still needs them.
- [Latent action tokens](../../concepts/learning/latent-action-tokens.md) — the unreadable answer that actually ports across morphologies.
- [Control abstraction levels](../../concepts/robotics/control-abstraction-levels.md) — *where* a controller acts; this page is about *what it says* at that level.
- [Code as policy](../../concepts/agents/code-as-policy.md) — the action vocabulary as arbitrary code; the winning representation so far, and the least portable.
- [LLM-agent architecture](../../concepts/agents/llm-agent-architecture.md) — the parent pattern, where the action vocabulary is a discrete tool schema.
- [LLM-free VLA](../../concepts/learning/llm-free-vla.md) — the counterpart finding: language *semantics* are load-bearing while language *models* may not be.
- [VLA models](../../concepts/learning/vla-models.md) — the action-head taxonomy, which is the bottom three rows of the spectrum table.
- [Control-rate ladder](../../syntheses/platforms/control-rate-ladder.md) — why the hierarchy exists at all: nothing readable runs at 83 Hz.
