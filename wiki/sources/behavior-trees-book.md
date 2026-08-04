---
title: "Behavior Trees in Robotics and AI: An Introduction"
type: source
url: https://arxiv.org/abs/1709.00084
local_path: raw/1709.00084.pdf
author: Michele Colledanchise, Petter Ögren
venue: Chapman & Hall/CRC Artificial Intelligence and Robotics Series (2018); arXiv 1709.00084v6, 198 pp.
published: 2022-10-25
ingested: 2026-08-04
format: pdf
license: arXiv (book preprint)
tags: [behavior-trees, task-switching, modularity, reactivity, finite-state-machines, subsumption-architecture, formal-analysis, automated-planning, action-representation]
---

# Behavior Trees in Robotics and AI: An Introduction

**[Colledanchise](../entities/michele-colledanchise.md) & [Ögren](../entities/petter-ogren.md)** — a 198-page book (arXiv preprint of the Chapman & Hall/CRC volume; v1 2017, v6 2022). The wiki's primary source on **[behavior trees](../concepts/robotics/behavior-trees.md)**, the dominant *deployed* action-composition formalism in robotics and games — and, until this ingest, entirely absent here.

> [!note] Scope of this ingest
> Read structurally: full treatment of Chapters 1–3 (formulation, generalization, design principles) and the framing of Chapters 5–9. The formal proofs (Ch. 6), the planning algorithms (Ch. 7), and the stochastic-BT reliability calculus (Ch. 9) are summarized, not verified line by line.

## Summary

A **Behavior Tree** structures the switching between tasks in an autonomous agent. It is a directed rooted tree whose internal nodes are **control flow nodes** and whose leaves are **execution nodes**. The root emits **ticks** at a fixed frequency; a node executes *if and only if* it is ticked, and returns **Running**, **Success**, or **Failure** to its parent.

The book's central claim is that BTs are simultaneously **modular** and **reactive** — properties that the earlier alternatives (FSMs, subsumption, decision trees, teleo-reactive programs) each achieve only partially — and Chapter 6 proves BTs *generalize* all of them.

## The formalism (Ch. 1.3)

Four control-flow node types and two execution node types:

| Node | Symbol | Returns |
|---|---|---|
| **Sequence** | `→` | ticks children left to right; returns **Failure**/**Running** at the first child returning it; **Success** only if *all* children succeed |
| **Fallback** (selector / priority selector) | `?` | ticks children left to right; returns **Success**/**Running** at the first child returning it; **Failure** only if *all* children fail |
| **Parallel** | `⇉` | ticks all children; succeeds on a threshold M of N |
| **Decorator** | custom | transforms a child's return (invert, retry, timeout, …) |
| **Action** | box | does something; Running while under way |
| **Condition** | oval | checks something; Success/Failure, never Running |

That is the whole vocabulary. Sequence is "and-then," Fallback is "or-else," and the tick model makes the whole tree re-evaluate continuously — which is where reactivity comes from: a condition that becomes false *while an action runs* is re-checked on the next tick and can preempt.

**Memory nodes** (Ch. 1.3.2) suppress re-ticking of already-succeeded children, converting a reactive BT into a feed-forward one — the explicit escape hatch when re-checking conditions is too expensive.

## Why it matters here

### The readability claim, stated by the authors

> *"BTs are human readable due to their tree structure and modularity."*

This is a **structural** readability argument, and it is different in kind from every other claim in the [action-representation-languages](../syntheses/agents/action-representation-languages.md) spectrum. BTs don't make the *primitives* readable — a leaf can be any opaque policy, including a VLA. They make the **composition** readable: what runs, in what order, under what conditions, with what fallback. The leaves stay embodiment-specific; the tree does not.

> [!note] The one row in the spectrum that separates the two questions
> Everything else on that page conflates "is the action readable?" with "is the composition readable?" BTs answer **yes** to the second while remaining agnostic on the first. That makes them the natural *container* for the unreadable representations — a [UniT](unit-paper.md) token predictor or a [TurboVLA](turbovla-paper.md) policy can sit at a leaf while the tree above it stays auditable. **No source in this wiki does this**, which is a conspicuous gap rather than a settled question.

### What BTs generalize (Ch. 2, formally in Ch. 6)

- **Finite state machines** and **hierarchical FSMs** — the book shows constructions in both directions (a BT that behaves like an FSM; an FSM that behaves like a BT).
- **Subsumption architecture** (Brooks).
- **Teleo-reactive programs** (Nilsson).
- **Decision trees** — a decision tree is a BT with only conditions and actions.
- **Sequential behavior compositions.**

The modularity argument against FSMs: an FSM transition is a **one-way** control transfer — a `goto` — so adding a state means reasoning about every transition into and out of it, and subtrees cannot be moved between projects. A BT's tick/return is a **two-way** transfer, like a function call, so any subtree is independently composable.

### Honest disadvantages (Ch. 2.6.2)

The book is unusually candid, which is worth recording:

- **The engine is complex to implement.** Ticking must run in parallel with action execution; single-threaded sequential implementations don't give full BT semantics. (Mitigated: implement once, reuse — C++, ROS, and Python libraries exist.)
- **Checking all conditions can be expensive** or infeasible. Closed-loop task execution has a cost in any architecture; memory nodes give an open-loop fallback.
- **Sometimes feed-forward is fine.** *"In applications where the robot operates in a very structured environment, predictable in space and time, BTs do not have any advantages over simpler architectures."*
- **BTs require a new mindset** — execution is not state-focused; switching is **tick-driven, not event-driven**.
- **Tooling is less mature** than for FSMs.

### Beyond the basics

- **Ch. 3 — design principles:** explicit success conditions for readability; implicit sequences for reactivity; sequences for **safety** (guard conditions ahead of the action they protect); **backchaining** to build deliberative BTs from goal conditions; memory nodes to *remove* reactivity deliberately; and choosing granularity.
- **Ch. 5 — formal analysis:** a state-space formulation supporting proofs about **efficiency, robustness, and safety**.
- **Ch. 7 — planning:** **PA-BT** (Planning and Acting with BTs) grows a BT by backchaining from unmet conditions and refines it during execution, with stated reactiveness, safety, and fault-tolerance properties. Also **ABL**, used for a StarCraft agent.
- **Ch. 8 — machine learning:** **GP-BT** (genetic programming synthesizes BT subtrees, with pruning of ineffective ones), **RL-BT** (Q-learning inside BT nodes), and learning from demonstration.
- **Ch. 9 — stochastic BTs:** actions with probabilistic outcomes; an SBT transforms into a **discrete-time Markov chain**, yielding **success probability** and **expected time to completion** analytically.

### Deployment record (Ch. 1.6)

Autonomous vehicles (DARPA-lineage stacks), industrial robotics, the **Amazon Picking Challenge**, and the social robot **JIBO** — plus the origin in the computer-game industry, which is where BTs were invented and remain standard.

## Open questions

- **No BT + learned-policy integration in this wiki.** Ch. 8 covers *learning a BT*; nothing covers *a BT orchestrating VLAs*, which is the obvious 2026 architecture and the one [Waddle](../entities/waddle-labs.md)'s "VLA-as-tool" stance and the [guardrails](../syntheses/agents/guardrails-for-robot-agents.md) thread both point at without naming.
- **BTs as a safety rail.** Ch. 3.4 and Ch. 5.3 give safety-by-construction via sequence guards, and Ch. 9 gives failure probabilities. The wiki's [guardrails synthesis](../syntheses/agents/guardrails-for-robot-agents.md) found the **execution rail ships empty** in every stack examined — BTs are a 20-year-old, formally analyzed candidate for exactly that layer, and no ingested robot stack uses one for it.
- **Book is a preprint of a 2018 volume**, last revised 2022. BehaviorTree.CPP and Nav2's BT navigator are now the de-facto ROS 2 implementations and are not covered here.

## Entities mentioned
- [Michele Colledanchise](../entities/michele-colledanchise.md) · [Petter Ögren](../entities/petter-ogren.md)

## Concepts touched
- [Behavior trees](../concepts/robotics/behavior-trees.md) — the concept this source founds
- [Action representation languages](../syntheses/agents/action-representation-languages.md) — structural readability, distinct from action readability
- [Symbolic task planning](../concepts/agents/symbolic-task-planning.md) — PA-BT backchains like a planner
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — the modern alternative to a hand-designed switching structure
- [AI guardrails](../concepts/safety/ai-guardrails.md) — safety by construction at the composition layer
