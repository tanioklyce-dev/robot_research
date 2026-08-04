---
title: Behavior trees
type: concept
created: 2026-08-04
updated: 2026-08-04
sources: 1
tags: [behavior-trees, task-switching, modularity, reactivity, finite-state-machines, subsumption-architecture, action-representation, safety, ros2]
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
- Tooling is less mature than for FSMs (the book's 2018/2022 view; BehaviorTree.CPP and Nav2's BT navigator have since become ROS 2 standards, uncovered here).

## Where they're deployed

Computer games (the origin), autonomous vehicles, industrial robotics, the **Amazon Picking Challenge**, and the social robot **JIBO**.

## Related
- [Action representation languages](../../syntheses/agents/action-representation-languages.md) — BTs as the structural-readability row
- [Symbolic task planning](../agents/symbolic-task-planning.md) — PA-BT sits between planning and execution
- [Code as policy](../agents/code-as-policy.md) — the LLM-era alternative: generate the switching structure instead of authoring it
- [Control abstraction levels](control-abstraction-levels.md) — BTs live at the composition layer above primitives
- [AI guardrails](../safety/ai-guardrails.md) — the execution rail BTs could fill

## Mentioned in
- [Behavior Trees in Robotics and AI: An Introduction](../../sources/behavior-trees-book.md)
