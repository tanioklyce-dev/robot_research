---
title: Behavior trees
type: concept
created: 2026-08-04
updated: 2026-08-04
sources: 3
tags: [behavior-trees, task-switching, modularity, reactivity, finite-state-machines, subsumption-architecture, action-representation, safety, ros2, nav2, behaviortree-cpp]
---

# Behavior trees

A **behavior tree (BT)** is a directed rooted tree that structures the switching between tasks in an autonomous agent. Internal nodes are **control flow nodes**; leaves are **execution nodes**. The root emits **ticks** at a fixed frequency, a node runs *iff* it is ticked, and every node returns **Running**, **Success**, or **Failure** to its parent ([Colledanchise & Ögren](../../sources/behavior-trees-book.md)).

The dominant *deployed* action-composition formalism in robotics and computer games — and, until 2026-08-04, entirely absent from this wiki despite being older and more widely shipped than anything in its [VLA](../learning/vla-models.md) thread.

## The whole vocabulary

| Node | Symbol | Semantics |
|---|---|---|
| **Sequence** | `→` | "and-then" — Failure/Running at the first child returning it; Success iff *all* succeed |
| **Fallback** | `?` | "or-else" — Success/Running at the first child returning it; Failure iff *all* fail |
| **Parallel** | `⇉` | tick all; succeed on M of N |
| **Decorator** | — | transform a child's return (invert, retry, timeout) |
| **Action** | box | do something; Running while under way |
| **Condition** | oval | check something; never Running |

Six node types. The expressive power comes from the **tick model**: the tree re-evaluates continuously, so a condition that becomes false *while an action is running* preempts it on the next tick. **Memory nodes** suppress re-ticking of succeeded children, deliberately trading reactivity for cheaper condition checks.

## Why they displaced FSMs

The argument is about **control transfer**. An FSM transition is a **one-way** transfer — a `goto` — so adding a state requires reasoning about every transition into and out of it, and subtrees can't be lifted between projects. A BT's tick/return is a **two-way** transfer, like a function call, making any subtree independently composable.

BTs are formally shown to **generalize** finite state machines, hierarchical FSMs, the **subsumption architecture**, **teleo-reactive programs**, **decision trees**, and sequential behavior compositions ([book Ch. 2 and Ch. 6](../../sources/behavior-trees-book.md)).

## The readability claim, and why it's a different claim

> *"BTs are human readable due to their tree structure and modularity."*

This is **structural** readability, not action readability — a distinction nothing else in [action representation languages](../../syntheses/agents/action-representation-languages.md) separates cleanly. A BT leaf can be any opaque thing, including a learned policy. What the tree makes legible is the **composition**: what runs, in what order, under what guard, with what fallback.

> [!note] The obvious 2026 architecture that nobody in this wiki has built
> A BT is the natural *container* for unreadable action representations. A [UniT](../../entities/unit.md) token predictor or a [TurboVLA](../../entities/turbovla.md) policy sits at a leaf; the tree above it stays auditable, guarded, and diffable. That composes the [latent-action](../learning/latent-action-tokens.md) line's portability with the readability the language-motion line was chasing — and **no ingested source does it**. [Waddle](../../entities/waddle-labs.md)'s "VLA-as-tool" stance and the [code-as-policy](../agents/code-as-policy.md) lineage both point here without naming BTs.
>
> **As of the 2026-08-04 implementation ingest this is no longer hand-waving.** [BehaviorTree.CPP](../../entities/behaviortree-cpp.md) ports give the exact interface: a VLA node takes its instruction on a typed **input port** — a literal, or `{current_subtask}` written by an upstream planner node — and writes results back for guard conditions to read. Nav2 already demonstrates every surrounding piece: cause-selected recovery, bounded retries, preemption on goal change, runtime plugin swap. **Nothing in Nav2 contains a learned policy at any leaf** — that substitution is the entire unbuilt experiment.

## Safety — a candidate for the rail that ships empty

The book gives **safety by construction** (guard conditions placed ahead of the actions they protect, Ch. 3.4), a state-space formulation supporting **proofs** about safety, robustness, and efficiency (Ch. 5), and **stochastic BTs** that convert to a discrete-time Markov chain to yield **success probability and expected time to completion** analytically (Ch. 9).

The [guardrails for robot agents](../../syntheses/agents/guardrails-for-robot-agents.md) synthesis found the **execution rail ships empty** in every stack examined. BTs are a 20-year-old, formally analyzed candidate for exactly that layer, with a shipped ROS ecosystem — and no ingested robot stack in this wiki uses one for it. That is a gap worth closing, not a settled tradeoff.

## Planning and learning

- **PA-BT** — grows a BT by **backchaining** from unmet conditions and refines it during execution; stated reactiveness, safety, and fault-tolerance properties. Structurally close to [PDDL-style](../agents/symbolic-task-planning.md) goal regression, but producing a *reactive executable* rather than a plan.
- **GP-BT** — genetic programming synthesizes BT subtrees, with pruning of ineffective ones.
- **RL-BT** — Q-learning inside BT nodes.
- **Learning from demonstration** applied to BT structure.

## Honest limitations (from the authors)

- The **engine is complex to implement** correctly — ticking must run in parallel with action execution.
- **Checking all conditions can be expensive** or infeasible.
- *"In applications where the robot operates in a very structured environment, predictable in space and time, BTs do not have any advantages over simpler architectures."*
- They **require a new mindset** — switching is tick-driven, not event-driven.
- ~~Tooling is less mature than for FSMs~~ — **the book's 2018/2022 view, now retired.** See the implementations section below.

## The implementations (ingested 2026-08-04)

The book predates both of these, and its stated disadvantage — *"BT tools are less mature"* — no longer holds.

### [BehaviorTree.CPP](../../entities/behaviortree-cpp.md) v4 — the engine

MIT-licensed C++17, **asynchronous actions as a first-class concept** (answering the book's own warning that single-threaded engines can't give full BT semantics), runtime XML tree definition, dynamically-loaded node plugins, **type-safe dataflow via ports and a blackboard**, logging/profiling/replay, and the **Groot2** graphical editor.

The dataflow model is the load-bearing part: *"custom TreeNodes… are not conceptually different from **functions**."* A blackboard is a shared key/value store; input ports read entries, output ports write them, one node's outputs feed another's. XML separates literal from reference — `message="hello world"` vs `message="{greetings}"`.

### [Nav2](../../entities/nav2.md) — the production instance

The ROS 2 navigation stack is architected around a BT and ships `navigate_to_pose_w_replanning_and_recovery.xml`, running on a very large number of real robots. Three things it teaches that the formalism alone does not:

**1. Nav2 had to add control nodes.** The classical vocabulary was insufficient in practice:

| Node | Semantics |
|---|---|
| **PipelineSequence** | re-ticks *all prior* children when a later one returns RUNNING — *"resembling the flow of water in a pipe"*; lets the planner keep replanning while the controller is still following |
| **RecoveryNode** | two children; succeeds iff the first does; on failure ticks the remedy and retries, bounded by `number_of_retries` |
| **RoundRobin** | cycles children until one succeeds, **retaining position across ticks** — so escalating recovery tries a *different* remedy each time |
| **NonblockingSequence** | re-ticks even already-successful children *"to ensure that successful nodes do not latch a stale state"* |

Plus rate decorators: `RateController` (fixed Hz), `DistanceController` (per metre travelled), `SpeedController` (proportional to speed).

> [!note] The formalism's gap is temporal, not structural
> Almost every Nav2 addition is about *when* things get ticked, not about control flow. The classical BT assumes one global tick; real robots need per-subtree rates and staleness control. That is the operational form of the book's own "checking all conditions can be expensive" caveat.

**2. Two-tier recovery, cause-selected.** Each primary behavior is wrapped in its own `RecoveryNode` whose remedy is gated by a `WouldA…RecoveryHelp` condition reading that behavior's error code — **the remedy is chosen by the failure's cause, and only attempted if it could plausibly help**. Only when contextual recovery fails does the system-level subtree run, escalating via `RoundRobin` through clear-costmaps → Spin → Wait → BackUp, bounded at 6 retries. A `ReactiveFallback` with `<GoalUpdated/>` first means a new goal **preempts recovery immediately**.

**3. Runtime plugin selection.** `PlannerSelector` / `ControllerSelector` and friends read a ROS topic and write the chosen plugin ID to the blackboard. **The tree is the stable interface; implementations are hot-swappable without editing it.**

> [!note] Nav2 *is* a shipped execution rail — which qualifies a standing wiki finding
> The [guardrails synthesis](../../syntheses/agents/guardrails-for-robot-agents.md) concluded the **execution rail ships empty** everywhere it looked. Nav2's default tree is a counterexample in plain sight: `ValidatePath`, `IsGoalNearby`, `WouldAControllerRecoveryHelp`, and `GoalUpdated` are **world-state preconditions gating actions**, with bounded retries and a declared escalation path, in diffable XML.
>
> Caveats that keep the original finding mostly intact: it is scoped to navigation, not general manipulation, and it is safety-*adjacent* (recover from failure) rather than safety-*enforcing* (refuse unsafe actions). But *"nothing ships at this layer"* needs qualifying to *"the mechanism ships, applied to a different problem."*


## Where they're deployed

Computer games (the origin), autonomous vehicles, industrial robotics, the **Amazon Picking Challenge**, and the social robot **JIBO**.

## Related
- [Action representation languages](../../syntheses/agents/action-representation-languages.md) — BTs as the structural-readability row
- [Symbolic task planning](../agents/symbolic-task-planning.md) — PA-BT sits between planning and execution
- [Code as policy](../agents/code-as-policy.md) — the LLM-era alternative: generate the switching structure instead of authoring it
- [Control abstraction levels](control-abstraction-levels.md) — BTs live at the composition layer above primitives
- [AI guardrails](../safety/ai-guardrails.md) — the execution rail BTs could fill

## Mentioned in
- [Behavior Trees in Robotics and AI: An Introduction](../../sources/behavior-trees-book.md) — the formalism
- [BehaviorTree.CPP documentation](../../sources/behaviortree-cpp-docs.md) — the engine
- [Nav2 Behavior Trees documentation](../../sources/nav2-behavior-trees-docs.md) — the production instance
