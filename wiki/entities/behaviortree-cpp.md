---
title: BehaviorTree.CPP
type: entity
subtype: software
created: 2026-08-04
updated: 2026-08-04
sources: 2
tags: [behaviortree-cpp, behavior-trees, ros2, cpp, blackboard, ports, groot2, xml-dsl, mit-license]
---

**BehaviorTree.CPP** — the reference C++17 implementation of [behavior trees](../concepts/robotics/behavior-trees.md) in robotics. **MIT-licensed**, currently **v4.9**, maintained by Davide Faconti and contributors ([docs](../sources/behaviortree-cpp-docs.md)). Used by [Nav2](nav2.md) as its execution engine.

Positioned by its own documentation as *"a replacement for finite state machines"* — the book's argument, shipped.

## What it provides

| Feature | Note |
|---|---|
| **Asynchronous actions** | first-class, not bolted on — answers the [book](../sources/behavior-trees-book.md)'s warning that single-threaded engines can't give full BT semantics |
| **Reactive concurrent execution** | multiple actions running at once |
| **Runtime tree definition** | XML DSL, dynamically loaded — no hardcoded structure |
| **Plugins** | custom nodes as dynamically loadable libraries |
| **Type-safe dataflow** | ports + blackboard |
| **Logging / profiling** | visualization, recording, replay, analysis |
| **Groot2** | graphical tree editor (distributed separately; license unconfirmed) |

Build paths: colcon/ament (ROS 2), Conan, CMake, vcpkg.

## Ports and the blackboard

*"Custom TreeNodes… are not conceptually different from **functions**."* A **blackboard** is a key/value store shared across the tree; **input ports** read entries, **output ports** write them, and one node's outputs feed another's inputs — all type-safe. XML distinguishes literal from reference: `message="hello world"` vs `message="{greetings}"`.

> [!note] This is the interface a BT-over-VLA needs
> The [action-representation synthesis](../syntheses/agents/action-representation-languages.md) proposes a behavior tree with an opaque learned policy at an Action leaf. Ports make that mundane: a VLA node takes its instruction on an input port — a literal, or `{current_subtask}` written by an upstream planner — and writes results back for guard conditions to read. **A typed function-call boundary around a learned policy**, which is what the [guardrails thread](../syntheses/agents/guardrails-for-robot-agents.md) says an execution rail requires. See [latent action tokens](../concepts/learning/latent-action-tokens.md) for what would sit underneath.

## v3 → v4 (both post-date the book)

`NodeConfiguration`→`NodeConfig`, `SequenceStar`→**`SequenceWithMemory`**, `AsyncActionNode`→`ThreadedAction`, `Optional`→`Expected`; `<SubTreePlus>` became the default `<SubTree>`; `SetBlackboard`/`BlackboardCheck` replaced by a **scripting language plus pre/post conditions**; XML must declare `<root BTCPP_format="4">`. A `convert_v3_to_v4.py` script ships. Migration is described as incremental and mostly back-compatible.

The `SequenceStar → SequenceWithMemory` rename matches the book's Section 1.3.2 memory-node concept — v4 named the node after what it does.

## Caveats
- **Groot2's license is unconfirmed** here; the library is MIT, the editor is separate.
- **No performance characterization** found — tick overhead, practical tree size, and condition-checking cost are undocumented at ingest depth. Relevant at the rates on the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md).
- **`BehaviorTree.ROS2`** (ROS action/service node wrappers) not yet read — the natural next ingest for anyone building on this.
- The **v4 scripting language** moves logic into the XML, cutting against the "leaves are opaque code" model. Only skimmed.
- `behaviortree.dev` **403s unauthenticated fetchers**; use curl with a browser user-agent.

## Related
- [Behavior trees](../concepts/robotics/behavior-trees.md) — the formalism
- [Nav2](nav2.md) — the flagship consumer
- [ROS 2](ros2.md)

## Mentioned in
- [BehaviorTree.CPP documentation](../sources/behaviortree-cpp-docs.md)
- [Nav2 Behavior Trees documentation](../sources/nav2-behavior-trees-docs.md)
