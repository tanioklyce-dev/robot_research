---
title: Robot platforms — comparison
type: synthesis
created: 2026-05-08
updated: 2026-05-08
tags: [robots, hardware, comparison, list, manipulators, mobile-robots]
---

# Robot platforms — comparison

A reference list of robot platforms with entity pages in this wiki, organized by tier and type, with comparison axes and "what each is used for in the wiki." Intended as a quick-lookup page when a paper says "we evaluate on X" and you want to know how X relates to other platforms ingested here.

## At a glance

| Robot                          | Tier        | Type                  | Compute                   | Arm DOF           | Mobility       | Primary use here                                                                         |
| ------------------------------ | ----------- | --------------------- | ------------------------- | ----------------- | -------------- | ---------------------------------------------------------------------------------------- |
| [Franka Panda](../../entities/franka-panda.md) | Research    | Tabletop manipulator  | External GPU              | 7                 | None           | DROID, V-JEPA 2, V-JEPA 2.1, JEPA-WMs, RUM cross-embodiment. The default real-robot arm. |
| [xArm 7](../../entities/xarm-7.md)             | Commercial  | Tabletop manipulator  | External                  | 7                 | None           | RUM cross-embodiment transfer target (~10pt drop vs Stretch).                            |
| [Stretch](../../entities/stretch.md)           | Research    | Mobile manipulator    | Onboard (NUC + RealSense) | 1 (telescoping)   | Diff-drive     | RUM zero-shot generalist policies; stretch_ai LLM agent.                                 |
| [ROSOrin Pro](../../entities/rosorin-pro.md)   | Educational | Mobile manipulator    | Jetson Orin Nano          | 6 (HX-12H servos) | Diff/Ackermann | OpenClaw LLM-agent framework; LeWM-feasibility candidate.                                |
| [ROSOrin](../../entities/rosorin.md)           | Educational | Mobile robot (no arm) | Jetson Orin Nano          | 0                 | Diff/Ackermann | LLM-agent curriculum (cloud + offline).                                                  |
| [TurtleBot](../../entities/turtlebot.md)       | Educational | Mobile robot (no arm) | Raspberry Pi (gen 4)      | 0                 | Diff-drive     | Reference / comparison point — not used directly in any wiki source.                     |

## By tier

### Research-grade ($10k–$30k+)
- **[Franka Panda](../../entities/franka-panda.md)** (UFactory's commercial tier sits adjacent). 7-DOF torque-controlled arm, 1 kHz FCI control. Standard real-robot platform across the JEPA / VLA / DROID literature. Used in V-JEPA 2 (zero-shot pick-and-place), V-JEPA 2.1 (real-Franka grasping +20pt), JEPA-WMs (Franka unroll decode), RUM (transferred to via custom mount), DROID (single embodiment for entire dataset).
- **[xArm 7](../../entities/xarm-7.md)** (UFactory). Commercial alternative to Franka. Same 7-DOF tabletop class. Appears in this wiki only as RUM's cross-embodiment transfer target — but a useful data point for how BC policies generalize across hardware (~10pt drop).
- **[Stretch](../../entities/stretch.md)** (Hello Robot, Stretch 3). Mobile manipulation: telescoping arm + differential-drive base + RealSense cameras + LiDAR. Anchor of the NYU + Hello Robot research line ([RUM](../../entities/robot-utility-models.md), [stretch_ai](../../entities/stretch-ai.md) LLM agent, [Dobb·E](../../entities/dobb-e.md)). The de-facto research-tier mobile manipulator for academic work in 2024–2026.

### Educational ($1k–$5k)
- **[ROSOrin Pro](../../entities/rosorin-pro.md)** (Hiwonder). 6-DOF arm + mobile base + Jetson Orin Nano. Ships with [OpenClaw](../../entities/openclaw.md) LLM-agent framework. Closest educational-tier analog to Stretch + stretch_ai, but with a real arm (vs Stretch's telescoping single-DOF arm).
- **[ROSOrin](../../entities/rosorin.md)** (Hiwonder). No-arm sibling of ROSOrin Pro. Mobile robot only; Jetson Orin Nano + cloud/offline LLM-agent curriculum.
- **[TurtleBot](../../entities/turtlebot.md)** (multiple vendors per generation; current: Open Robotics / Clearpath). Reference educational mobile robot since 2010. Lacks the agentic-AI bundling that ROSOrin / ROSOrin Pro now ship.

## By function

### Tabletop manipulators (no mobility)
[Franka Panda](../../entities/franka-panda.md), [xArm 7](../../entities/xarm-7.md).

### Mobile manipulators (arm + mobility)
[Stretch](../../entities/stretch.md) (research), [ROSOrin Pro](../../entities/rosorin-pro.md) (educational).

### Mobile robots without arms
[ROSOrin](../../entities/rosorin.md), [TurtleBot](../../entities/turtlebot.md).

## Cross-tier observations

### "Research-grade" vs "educational" is a real boundary
- **Repeatability and torque** — Franka's 1 kHz torque control + research-grade servos vs ROSOrin Pro's HX-12H educational bus servos. Affects what kinds of policies can transfer cleanly. The RUM cross-embodiment story (~10pt drop, Stretch → xArm 7) is across two *commercial* arms; transferring to educational arms is a much larger gap.
- **Data availability** — every research-tier robot above has at least one large public dataset attached ([DROID](../../entities/droid.md) for Franka, [RUM](../../entities/robot-utility-models.md) for Stretch). Educational-tier robots don't yet.
- **Software stack maturity** — Franka has libfranka + frankx + ROS bindings + every major sim ([MuJoCo](../../entities/mujoco.md), [Isaac Sim](../../entities/nvidia-isaac-sim.md), Pinocchio). ROSOrin Pro has Hiwonder's stack + ROS 2 + Gazebo. Both functional; the research-tier ecosystems are deeper.

### Educational tier is converging on "Jetson + LLM agent + ROS 2"
The [ROSOrin](../../entities/rosorin.md) / [ROSOrin Pro](../../entities/rosorin-pro.md) / [OpenClaw](../../entities/openclaw.md) stack represents a generational update of the [TurtleBot](../../entities/turtlebot.md) educational role: same target audience (CS / robotics students learning ROS), but with **Jetson Orin Nano compute (~10× the Raspberry Pi)** and a **bundled agentic-AI / LLM-agent curriculum** that TurtleBot doesn't have. The interesting question is whether TurtleBot 5 (or whichever follows) will close that gap, or whether Hiwonder's lineage takes over the educational niche entirely.

### Research-tier mobile manipulation = Stretch
There's basically one option in this wiki: **Hello Robot Stretch.** ROSOrin Pro is the educational-tier alternative; Boston Dynamics Spot + Atlas would be the heavy-tier alternatives but aren't ingested here. So when an academic paper says "real-robot mobile manipulation," **Stretch is implied**.

### Tabletop manipulation = Franka, with xArm 7 as second option
Same pattern — when a paper says "real-robot manipulation" without further qualification, **Franka is implied**. xArm 7 appears as a transfer target rather than a primary platform.

## What's missing from this wiki

Worth flagging robot platforms that show up in adjacent literature but don't have entity pages here yet:

- **Boston Dynamics Spot** — quadruped reference platform (no entity page; [Atlas](../../entities/atlas.md) is filed).
- **Pi (Physical Intelligence) hardware** — already in known gaps as needing a primary source.
- **ALOHA / ViperX bimanual setup** — Stanford bimanual teleop platform; referenced indirectly via Chelsea Finn but no entity page.
- **xArm 6** (UFactory's 6-DOF cousin to xArm 7) — sometimes cited as a cheaper alternative.
- **UR5 / UR10 / UR16** (Universal Robots) — collaborative arms common in industrial settings; not yet appearing in our literature.
- **Humanoids** — see the dedicated [Humanoid platforms survey](humanoid-platforms-survey.md) for that landscape; 10 humanoid entities filed there.

## Sources used in this synthesis

- Per-platform entity pages: [Franka Panda](../../entities/franka-panda.md), [xArm 7](../../entities/xarm-7.md), [Stretch](../../entities/stretch.md), [ROSOrin Pro](../../entities/rosorin-pro.md), [ROSOrin](../../entities/rosorin.md), [TurtleBot](../../entities/turtlebot.md).
- Companion source pages: [RUM Paper](../../sources/robot-utility-models-paper.md) (cross-embodiment data), [DROID](../../entities/droid.md) entity (Franka data scale), [ROSOrin Pro User Manual](../../sources/hiwonder-rosorin-pro-user-manual.md) (educational-tier specs).

## Related

- [index.md](../../index.md) — Robot platforms section (the live list).
- [LeWM on ROSOrin Pro — feasibility analysis](../projects/lewm-on-rosorin-pro-feasibility.md) — uses the research-vs-educational tier distinction extensively.
- [LLM-agent architecture across stacks](../agents/llm-agent-architecture-across-stacks.md) — compares stretch_ai (Stretch) vs ROSOrin (cloud/offline) vs OpenClaw (ROSOrin Pro).
- [Sim-heavy vs real-data paths](../simulators/sim-heavy-vs-real-data-paths.md) — anchors the "what robot underpins each path" question.

## Open questions / TBD

> [!note] Tier boundary in cross-embodiment transfer
> RUM measures Stretch → xArm 7 (~10pt drop). The research-tier-to-educational-tier drop is **not measured anywhere in this wiki**. Whether a Stretch-trained policy transfers to ROSOrin Pro is the obvious next question; nobody has published on it yet.

> [!note] Humanoids absent
> Humanoid platforms (Atlas, Optimus, Unitree, AGIBOT) drive a lot of 2026 industry attention but are underrepresented in this wiki because the ingested sources skew academic + tabletop / mobile-manipulation. If humanoid VLA papers get ingested, this comparison page should grow a humanoid section.
