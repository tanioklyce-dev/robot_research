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

| Robot | Tier | Type | Compute | Arm DOF | Mobility | Primary use here |
|---|---|---|---|---|---|---|
| [[franka-panda\|Franka Panda]] | Research | Tabletop manipulator | External GPU | 7 | None | DROID, V-JEPA 2, V-JEPA 2.1, JEPA-WMs, RUM cross-embodiment. The default real-robot arm. |
| [[xarm-7\|xArm 7]] | Commercial | Tabletop manipulator | External | 7 | None | RUM cross-embodiment transfer target (~10pt drop vs Stretch). |
| [[stretch\|Stretch]] | Research | Mobile manipulator | Onboard (NUC + RealSense) | 1 (telescoping) | Diff-drive | RUM zero-shot generalist policies; stretch_ai LLM agent. |
| [[rosorin-pro\|ROSOrin Pro]] | Educational | Mobile manipulator | Jetson Orin Nano | 6 (HX-12H servos) | Diff/Ackermann | OpenClaw LLM-agent framework; LeWM-feasibility candidate. |
| [[rosorin\|ROSOrin]] | Educational | Mobile robot (no arm) | Jetson Orin Nano | 0 | Diff/Ackermann | LLM-agent curriculum (cloud + offline). |
| [[turtlebot\|TurtleBot]] | Educational | Mobile robot (no arm) | Raspberry Pi (gen 4) | 0 | Diff-drive | Reference / comparison point — not used directly in any wiki source. |

## By tier

### Research-grade ($10k–$30k+)
- **[[franka-panda|Franka Panda]]** (UFactory's commercial tier sits adjacent). 7-DOF torque-controlled arm, 1 kHz FCI control. Standard real-robot platform across the JEPA / VLA / DROID literature. Used in V-JEPA 2 (zero-shot pick-and-place), V-JEPA 2.1 (real-Franka grasping +20pt), JEPA-WMs (Franka unroll decode), RUM (transferred to via custom mount), DROID (single embodiment for entire dataset).
- **[[xarm-7|xArm 7]]** (UFactory). Commercial alternative to Franka. Same 7-DOF tabletop class. Appears in this wiki only as RUM's cross-embodiment transfer target — but a useful data point for how BC policies generalize across hardware (~10pt drop).
- **[[stretch|Stretch]]** (Hello Robot, Stretch 3). Mobile manipulation: telescoping arm + differential-drive base + RealSense cameras + LiDAR. Anchor of the NYU + Hello Robot research line ([[robot-utility-models|RUM]], [[stretch-ai|stretch_ai]] LLM agent, [[dobb-e|Dobb·E]]). The de-facto research-tier mobile manipulator for academic work in 2024–2026.

### Educational ($1k–$5k)
- **[[rosorin-pro|ROSOrin Pro]]** (Hiwonder). 6-DOF arm + mobile base + Jetson Orin Nano. Ships with [[openclaw|OpenClaw]] LLM-agent framework. Closest educational-tier analog to Stretch + stretch_ai, but with a real arm (vs Stretch's telescoping single-DOF arm).
- **[[rosorin|ROSOrin]]** (Hiwonder). No-arm sibling of ROSOrin Pro. Mobile robot only; Jetson Orin Nano + cloud/offline LLM-agent curriculum.
- **[[turtlebot|TurtleBot]]** (multiple vendors per generation; current: Open Robotics / Clearpath). Reference educational mobile robot since 2010. Lacks the agentic-AI bundling that ROSOrin / ROSOrin Pro now ship.

## By function

### Tabletop manipulators (no mobility)
[[franka-panda|Franka Panda]], [[xarm-7|xArm 7]].

### Mobile manipulators (arm + mobility)
[[stretch|Stretch]] (research), [[rosorin-pro|ROSOrin Pro]] (educational).

### Mobile robots without arms
[[rosorin|ROSOrin]], [[turtlebot|TurtleBot]].

## Cross-tier observations

### "Research-grade" vs "educational" is a real boundary
- **Repeatability and torque** — Franka's 1 kHz torque control + research-grade servos vs ROSOrin Pro's HX-12H educational bus servos. Affects what kinds of policies can transfer cleanly. The RUM cross-embodiment story (~10pt drop, Stretch → xArm 7) is across two *commercial* arms; transferring to educational arms is a much larger gap.
- **Data availability** — every research-tier robot above has at least one large public dataset attached ([[droid|DROID]] for Franka, [[robot-utility-models|RUM]] for Stretch). Educational-tier robots don't yet.
- **Software stack maturity** — Franka has libfranka + frankx + ROS bindings + every major sim ([[mujoco|MuJoCo]], [[nvidia-isaac-sim|Isaac Sim]], Pinocchio). ROSOrin Pro has Hiwonder's stack + ROS 2 + Gazebo. Both functional; the research-tier ecosystems are deeper.

### Educational tier is converging on "Jetson + LLM agent + ROS 2"
The [[rosorin|ROSOrin]] / [[rosorin-pro|ROSOrin Pro]] / [[openclaw|OpenClaw]] stack represents a generational update of the [[turtlebot|TurtleBot]] educational role: same target audience (CS / robotics students learning ROS), but with **Jetson Orin Nano compute (~10× the Raspberry Pi)** and a **bundled agentic-AI / LLM-agent curriculum** that TurtleBot doesn't have. The interesting question is whether TurtleBot 5 (or whichever follows) will close that gap, or whether Hiwonder's lineage takes over the educational niche entirely.

### Research-tier mobile manipulation = Stretch
There's basically one option in this wiki: **Hello Robot Stretch.** ROSOrin Pro is the educational-tier alternative; Boston Dynamics Spot + Atlas would be the heavy-tier alternatives but aren't ingested here. So when an academic paper says "real-robot mobile manipulation," **Stretch is implied**.

### Tabletop manipulation = Franka, with xArm 7 as second option
Same pattern — when a paper says "real-robot manipulation" without further qualification, **Franka is implied**. xArm 7 appears as a transfer target rather than a primary platform.

## What's missing from this wiki

Worth flagging robot platforms that show up in adjacent literature but don't have entity pages here yet:

- **iRobot Create 3** — base of TurtleBot 4; no entity page.
- **Boston Dynamics Atlas / Spot** — humanoid / quadruped reference platforms; no entity pages (they're occasionally referenced via [[nvidia-groot|GR00T]] and humanoid-VLA context but not directly).
- **Unitree H1 / G1, Tesla Optimus, AGIBOT humanoid line** — humanoid platforms that VLA papers like [[nvidia-groot|GR00T]] target; not yet ingested.
- **Pi (Physical Intelligence) hardware** — already in known gaps as needing a primary source.
- **ALOHA / ViperX bimanual setup** — Stanford bimanual teleop platform; referenced indirectly via Chelsea Finn but no entity page.
- **xArm 6** (UFactory's 6-DOF cousin to xArm 7) — sometimes cited as a cheaper alternative.
- **UR5 / UR10 / UR16** (Universal Robots) — collaborative arms common in industrial settings; not yet appearing in our literature.

## Sources used in this synthesis

- Per-platform entity pages: [[franka-panda|Franka Panda]], [[xarm-7|xArm 7]], [[stretch|Stretch]], [[rosorin-pro|ROSOrin Pro]], [[rosorin|ROSOrin]], [[turtlebot|TurtleBot]].
- Companion source pages: [[robot-utility-models-paper|RUM Paper]] (cross-embodiment data), [[droid|DROID]] entity (Franka data scale), [[hiwonder-rosorin-pro-user-manual|ROSOrin Pro User Manual]] (educational-tier specs).

## Related

- [[index|index.md]] — Robot platforms section (the live list).
- [[lewm-on-rosorin-pro-feasibility|LeWM on ROSOrin Pro — feasibility analysis]] — uses the research-vs-educational tier distinction extensively.
- [[llm-agent-architecture-across-stacks|LLM-agent architecture across stacks]] — compares stretch_ai (Stretch) vs ROSOrin (cloud/offline) vs OpenClaw (ROSOrin Pro).
- [[sim-heavy-vs-real-data-paths|Sim-heavy vs real-data paths]] — anchors the "what robot underpins each path" question.

## Open questions / TBD

> [!note] Tier boundary in cross-embodiment transfer
> RUM measures Stretch → xArm 7 (~10pt drop). The research-tier-to-educational-tier drop is **not measured anywhere in this wiki**. Whether a Stretch-trained policy transfers to ROSOrin Pro is the obvious next question; nobody has published on it yet.

> [!note] Humanoids absent
> Humanoid platforms (Atlas, Optimus, Unitree, AGIBOT) drive a lot of 2026 industry attention but are underrepresented in this wiki because the ingested sources skew academic + tabletop / mobile-manipulation. If humanoid VLA papers get ingested, this comparison page should grow a humanoid section.
