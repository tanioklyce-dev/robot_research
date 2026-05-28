---
title: Nav2
type: entity
subtype: software-framework
created: 2026-05-28
updated: 2026-05-28
sources: 3
tags: [nav2, navigation2, ros2, slam, navigation, behavior-tree, costmap, intel, samsung, open-navigation, mobile-robot]
---

**Nav2** (Navigation 2) — the **canonical [ROS 2](ros2.md) autonomous navigation stack**: SLAM, costmaps, behavior trees, path planning, local controllers, and recovery behaviors for mobile robots. Successor to ROS 1's **`move_base`**. Originally led at Intel + Samsung; now under the Open Navigation org. Apache 2.0. The default navigation framework for nearly every ROS 2 mobile platform in this wiki. Home: [docs.nav2.org](https://docs.nav2.org/).

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
