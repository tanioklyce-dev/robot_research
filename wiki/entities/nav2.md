---
title: Nav2
type: entity
subtype: software-framework
created: 2026-05-28
updated: 2026-08-04
sources: 7
tags: [nav2, navigation2, ros2, slam, navigation, behavior-tree, costmap, intel, samsung, open-navigation, mobile-robot]
---

**Nav2** (Navigation 2) — the **canonical [ROS 2](ros2.md) autonomous navigation stack**: SLAM, costmaps, behavior trees, path planning, local controllers, and recovery behaviors for mobile robots. Successor to ROS 1's **`move_base`**. Originally led at Intel + Samsung; now under the Open Navigation org. Apache 2.0. The default navigation framework for nearly every ROS 2 mobile platform in this wiki. Home: [docs.nav2.org](https://docs.nav2.org/).

## The behavior tree — Nav2's actual architecture (ingested 2026-08-04)

Nav2 is **architected around a [behavior tree](../concepts/robotics/behavior-trees.md)**, running [BehaviorTree.CPP](behaviortree-cpp.md) v4 (`BTCPP_format="4"`), with the **BT Navigator** as its primary action server ([docs](../sources/nav2-behavior-trees-docs.md)). The default tree, `navigate_to_pose_w_replanning_and_recovery.xml`, *"replans the global path periodically at 1 Hz and it also has recovery actions."*

**Nav2 had to invent control nodes the classical formalism lacks** — the strongest evidence available on where BTs fall short in practice:

- **PipelineSequence** — re-ticks *all prior* children when a later one is RUNNING, *"resembling the flow of water in a pipe."* This is what lets the planner keep replanning while the controller is still following.
- **RecoveryNode** — pairs a behavior with its remedy; bounded by `number_of_retries`.
- **RoundRobin** — cycles remedies, **retaining position across ticks**, so escalation tries something *new* each failure.
- **NonblockingSequence** — re-ticks succeeded children *"to ensure that successful nodes do not latch a stale state."*
- Rate decorators: `RateController` (Hz), `DistanceController` (per metre), `SpeedController` (speed-proportional).

Notably, **almost every addition is about *when* things tick, not about control flow** — the formalism's gap is temporal.

**Two-tier, cause-selected recovery.** Each primary behavior gets its own `RecoveryNode` whose remedy is gated by a `WouldA…RecoveryHelp` condition reading that behavior's error code; only when contextual recovery fails does the system-level subtree escalate (clear costmaps → Spin → Wait → BackUp), bounded at 6 retries. A `ReactiveFallback` with `<GoalUpdated/>` first means a new goal **preempts recovery immediately**.

**Runtime plugin selection.** `PlannerSelector` / `ControllerSelector` read a ROS topic and write the chosen plugin ID to the blackboard. The tree is the stable interface; algorithms are hot-swappable without editing it.

> [!note] Nav2 is a shipped execution rail
> The [guardrails synthesis](../syntheses/agents/guardrails-for-robot-agents.md) found the **execution rail ships empty** everywhere it looked. `ValidatePath`, `IsGoalNearby`, `WouldAControllerRecoveryHelp`, and `GoalUpdated` are **world-state preconditions gating actions**, with bounded retries and declared escalation, in diffable XML. Scoped to navigation and safety-*adjacent* rather than safety-*enforcing* — but the mechanism ships.

**No leaf in Nav2 contains a learned policy.** Every one is a classical planner, controller, or scripted behavior — which makes it the complete scaffolding for the [BT-over-VLA](../concepts/robotics/behavior-trees.md) architecture nobody has built.

## Why it matters in this wiki

- **The "house navigation is already solved" component.** When the [LeRobot on ROSOrin Pro synthesis](../syntheses/projects/lerobot-on-rosorin-pro.md) says "navigation is solved by Nav2 + LiDAR SLAM, LeRobot adds nothing here," **this is what is meant**. Nav2 handles map building, localization, global + local planning, costmap maintenance, and recovery — the entire autonomy loop for getting a wheeled robot from point A to point B around obstacles.
- **Used by every mobile platform here:**
  - [Stretch](stretch.md) — Stretch 3 ([source](../sources/hello-robot-stretch-docs.md)) and Stretch 4 ([source](../sources/hello-robot-stretch-4-launch.md), which references ROS 2 Jazzy + Nav2).
  - [ROSOrin Pro](rosorin-pro.md) — bundled SLAM + Nav2 curriculum ([source](../sources/hiwonder-rosorin-docs.md)).
  - [TurtleBot 4](turtlebot.md) — Nav2 is the default nav stack.

## Composition (high level)

| Layer | Role |
|---|---|
| **SLAM** (`slam_toolbox`) | Mapping + localization |
| **Costmaps** (`nav2_costmap_2d`) | Static + obstacle inflation layers |
| **Planner** (`nav2_planner`, e.g. NavFn / SmacPlanner) | Global path planning |
| **Controller** (`nav2_controller`, e.g. DWB / RPP) | Local trajectory following |
| **Behavior tree** (`nav2_bt_navigator`) | Mission orchestration + recovery |
| **Lifecycle nodes** | Configured / activated / cleaned via ROS 2 lifecycle states |

## Position vs other layers

| Stack | Role | Manipulator analogue |
|---|---|---|
| **Nav2** | Mobile-base autonomy | [MoveIt](moveit.md) is the closest analogue (planning + execution) |
| `ros2_control` | Real-time low-level control | Same on the arm side |
| [LeRobot](lerobot.md) policies | End-to-end **visuomotor** learned skills | Same — they're orthogonal to Nav2 |

The composition pattern in this wiki: **Nav2 handles "get to room X," LeRobot policy handles "pick up the object at the destination," LLM-agent orchestrator ([OpenClaw](openclaw.md) / [stretch_ai](stretch-ai.md)) sequences them.**

## Related

- [ROS 2](ros2.md) — middleware substrate.
- [MoveIt](moveit.md) — manipulation-side equivalent role.
- [Stretch](stretch.md), [ROSOrin Pro](rosorin-pro.md), [TurtleBot](turtlebot.md) — mobile platforms that bundle Nav2.
- [LeRobot](lerobot.md) — orthogonal; Nav2 + LeRobot policies compose, neither replaces the other.

## Mentioned in

- [Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md)
- [Stretch 4 launch](../sources/hello-robot-stretch-4-launch.md) — ROS 2 Jazzy + Nav2 on Stretch 4.
- [Hiwonder ROSOrin docs](../sources/hiwonder-rosorin-docs.md) — bundled Nav2 curriculum.

## Open questions / TBD

- **Direct ingest of [docs.nav2.org](https://docs.nav2.org/)** would let us cite the current planner / controller plugin landscape and ROS 2 Lifecycle integration.
- **Open Navigation** as an organization entity — Steve Macenski (Nav2 lead) — not yet a page.
- **Nav2 + a learned visuomotor policy at the home-tidy task level** — how does the orchestration actually look in [stretch_ai](stretch-ai.md) / [OpenClaw](openclaw.md)? Not surfaced in current sources.

- [Nav2 Behavior Trees documentation](../sources/nav2-behavior-trees-docs.md) — the BT architecture, Nav2-specific control nodes, and the default tree.
