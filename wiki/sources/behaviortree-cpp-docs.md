---
title: BehaviorTree.CPP documentation (v4)
type: source
url: https://www.behaviortree.dev/
author: Davide Faconti and contributors (BehaviorTree organization)
venue: Project documentation site + GitHub README
published: 2026-01-01
ingested: 2026-08-04
format: html
license: MIT
tags: [behaviortree-cpp, behavior-trees, ros2, cpp, blackboard, ports, groot2, xml-dsl, tooling]
---

# BehaviorTree.CPP documentation (v4)

The reference implementation of [behavior trees](../concepts/robotics/behavior-trees.md) in robotics — a **C++17 framework**, MIT-licensed, currently at **v4.9** (docs at 4.8; the 3.8 branch survives for bug fixes only). Ingested to close the gap the [book ingest](behavior-trees-book.md) left: the book is a 2018 volume whose stated disadvantage was that *"BT tools are less mature."* That is no longer true, and this is the source that retires it.

> [!note] Fetch note
> `behaviortree.dev` returns **403 to unauthenticated fetchers**; content here was retrieved via `curl` with a browser user-agent, plus the GitHub README. Worth recording for future ingests of this domain.

## What it is

*"A C++ 17 library that can be used to create very complex behavior trees… a replacement for finite state machines."* Distinguishing features as the project states them:

- **Asynchronous actions as a first-class concept**, not an afterthought — directly answering the book's warning that *"the tick's generation and traversal should be executed in parallel with the action execution"* and that single-threaded implementations don't give full BT semantics.
- **Reactive and concurrent execution** of multiple actions.
- **Trees defined at runtime** via an XML domain-specific language — *"dynamic loading without hardcoding tree structure."*
- **Plugin support** for custom nodes (dynamically loadable).
- **Type-safe dataflow** between nodes.
- **Logging and profiling infrastructure** — visualization, recording, replay, analysis.

Build paths: **colcon/ament for ROS 2**, Conan, plain CMake, vcpkg.

## Ports and the blackboard — the part that matters for composing with learned policies

> *"Custom TreeNodes… are not conceptually different from **functions**."*

That sentence is the book's two-way-control-transfer argument restated as an API. The mechanism:

- A **Blackboard** is a key/value store shared by all nodes in the tree; an **entry** is one key/value pair.
- An **input port** reads an entry; an **output port** writes one. **One node's outputs are another's inputs.**
- Ports are **type-safe**.
- XML syntax distinguishes a literal from a reference: `message="hello world"` passes the string; `message="{greetings}"` reads the blackboard entry `greetings`, whose value *"can (and probably will) change at run-time."*

> [!note] This is the missing piece for the BT-over-VLA architecture
> The [action-representation synthesis](../syntheses/agents/action-representation-languages.md) argues the answer to "readable *and* portable" is a behavior tree with an opaque policy at an Action leaf — and flagged that nobody has built it. Ports are the interface that makes it concrete and unexciting: a **VLA node takes an instruction on an input port** (literal string, or `{current_subtask}` written by an upstream planner node) and writes success/failure plus any state it produces to output ports. Guard conditions read the same blackboard.
>
> That is a **typed function-call boundary around a learned policy** — exactly the "argument-level predicates and world-state preconditions" the [guardrails synthesis](../syntheses/agents/guardrails-for-robot-agents.md) says a real execution rail needs. The plumbing has existed and been shipped for years.

## v3 → v4 changes (the book predates both)

| v3.8 | v4.x |
|---|---|
| `NodeConfiguration` | `NodeConfig` |
| `SequenceStar` | `SequenceWithMemory` |
| `AsyncActionNode` | `ThreadedAction` |
| `Optional` | `Expected` |
| `<SubTree>` | deprecated; `<SubTreePlus>` became the default `<SubTree>` |
| `SetBlackboard` / `BlackboardCheck` | replaced by a **scripting language** + **pre/post conditions** |

XML must now declare `<root BTCPP_format="4">`. A `convert_v3_to_v4.py` script ships in the repo. Migration is described as *"incremental and back compatible"* for most code.

The rename `SequenceStar → SequenceWithMemory` is worth noting against the book: memory nodes are the book's Section 1.3.2 escape hatch for turning a reactive BT feed-forward, and v4 renamed the node to say so plainly.

## Groot2

A **graphical editor** for behavior trees, complementing the XML. The book's "tooling is less mature" complaint had this in mind; a visual editor plus runtime logging/replay is a materially different maturity level than in 2018.

## Open questions

- **Licensing of Groot2** is not confirmed here — BehaviorTree.CPP itself is MIT (copyright 2014–2026), but Groot2 is distributed separately and may not be.
- **No performance characterization.** Tick overhead, maximum practical tree size, and the cost of the condition-checking the book warns about are undocumented at this depth. Relevant if a tree is ticked at the rates on the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md).
- **`BehaviorTree.ROS2`** — the wrapper providing ROS 2 action/service node types — was not fetched separately and is the natural next read for anyone building on this.
- **The scripting language and pre/post conditions are v4's largest semantic addition** and were only skimmed. They move logic *into* the XML, which cuts against the "leaves are opaque C++" model and deserves a closer look before leaning on it.

## Entities mentioned
- [BehaviorTree.CPP](../entities/behaviortree-cpp.md) · [ROS 2](../entities/ros2.md) · [Nav2](../entities/nav2.md)

## Concepts touched
- [Behavior trees](../concepts/robotics/behavior-trees.md) — the implementation of the formalism
- [Action representation languages](../syntheses/agents/action-representation-languages.md) — ports as the typed boundary around an opaque policy
- [AI guardrails](../concepts/safety/ai-guardrails.md) — a shipped candidate for the execution rail
