---
title: Robot platforms — comparison
type: synthesis
created: 2026-05-08
updated: 2026-07-13
tags: [robots, hardware, comparison, list, manipulators, mobile-robots, aloha, mobile-aloha, xlerobot, yuri, bimanual]
---

# Robot platforms — comparison

A reference list of robot platforms with entity pages in this wiki, organized by tier and type, with comparison axes and "what each is used for in the wiki." Intended as a quick-lookup page when a paper says "we evaluate on X" and you want to know how X relates to other platforms ingested here.

## At a glance

| Robot                          | Tier        | Type                  | Compute                   | Arm DOF           | Mobility       | Primary use here                                                                         |
| ------------------------------ | ----------- | --------------------- | ------------------------- | ----------------- | -------------- | ---------------------------------------------------------------------------------------- |
| [Franka Panda](../../entities/franka-panda.md) | Research    | Tabletop manipulator  | External GPU              | 7                 | None           | DROID, V-JEPA 2, V-JEPA 2.1, JEPA-WMs, RUM cross-embodiment. The default real-robot arm. |
| [xArm 7](../../entities/xarm-7.md)             | Commercial  | Tabletop manipulator  | External                  | 7                 | None           | RUM cross-embodiment transfer target (~10pt drop vs Stretch).                            |
| [Stretch](../../entities/stretch.md)           | Research    | Mobile manipulator    | Onboard (NUC + RealSense) | 1 (telescoping)   | Diff-drive     | RUM zero-shot generalist policies; stretch_ai LLM agent.                                 |
| [Mobile ALOHA](../../entities/aloha.md)        | Research    | Bimanual mobile manip | Onboard (laptop + RTX 3070 Ti) | 2× 6 (ViperX 300) | Diff-drive (AgileX Tracer) | ACT + Diffusion Policy + VINN benchmarking on bimanual mobile manip; whole-body teleop; $32k. |
| [Yuri](../../entities/yuri.md) ([Sensori](../../entities/sensori-robotics.md)) | Research    | Bimanual manip (Desktop / Mobile) | Onboard (Jetson AGX Orin 64 GB) | 2× 7 (OpenArm+) | None (Desktop) / wheeled OpenBase (Mobile) | Integrated Physical-AI data-collection rig; bilateral force-feedback teleop out-of-box; LeRobot recording; GR00T/π0/X-VLA/SmolVLA support. Quote-only price. |
| [XLeRobot](../../entities/xlerobot.md)         | Educational | Bimanual mobile manip | External PC (or onboard [Jetson Orin Nano](../../entities/jetson-orin-nano.md)) | 2× (5+1) SO-101 + 2-DoF neck | Holonomic (LeKiwi omni) | **Cheapest bimanual mobile manipulator** ($660 tethered → $1.3k untethered); LeRobot/SO-101; onboard-Jetson untethered build + on-edge VLA benchmarks ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md)). |
| [ROSOrin Pro](../../entities/rosorin-pro.md)   | Educational | Mobile manipulator    | Jetson Orin Nano          | 6 (HX-12H servos) | Diff/Ackermann | OpenClaw LLM-agent (via Hiwonder's openclaw_controller ROS 2 bridge); LeWM-feasibility candidate.                                |
| [ROSOrin](../../entities/rosorin.md)           | Educational | Mobile robot (no arm) | Jetson Orin Nano          | 0                 | Diff/Ackermann | LLM-agent curriculum (cloud + offline).                                                  |
| [TurtleBot](../../entities/turtlebot.md)       | Educational | Mobile robot (no arm) | Raspberry Pi (gen 4)      | 0                 | Diff-drive     | Reference / comparison point — not used directly in any wiki source.                     |

## By tier

### Research-grade ($10k–$30k+)
- **[Franka Panda](../../entities/franka-panda.md)** (UFactory's commercial tier sits adjacent). 7-DOF torque-controlled arm, 1 kHz FCI control. Standard real-robot platform across the JEPA / VLA / DROID literature. Used in V-JEPA 2 (zero-shot pick-and-place), V-JEPA 2.1 (real-Franka grasping +20pt), JEPA-WMs (Franka unroll decode), RUM (transferred to via custom mount), DROID (single embodiment for entire dataset).
- **[xArm 7](../../entities/xarm-7.md)** (UFactory). Commercial alternative to Franka. Same 7-DOF tabletop class. Appears in this wiki only as RUM's cross-embodiment transfer target — but a useful data point for how BC policies generalize across hardware (~10pt drop).
- **[Stretch](../../entities/stretch.md)** (Hello Robot; Stretch 4 launched 2026-05-12). Mobile manipulation: telescoping arm + omnidirectional holonomic base + dual hemispherical 3D LiDAR (Stretch 4) + RealSense cameras. Anchor of the NYU + Hello Robot research line ([RUM](../../entities/robot-utility-models.md), [stretch_ai](../../entities/stretch-ai.md) LLM agent, [Dobb·E](../../entities/dobb-e.md)). The de-facto research-tier single-arm mobile manipulator for academic work in 2024–2026.
- **[Mobile ALOHA](../../entities/aloha.md)** (Stanford; Fu, Zhao, Finn 2024). Bimanual mobile manipulator with whole-body teleoperation. 4× [ViperX 300](../../entities/viperx-300.md) (2 leaders + 2 followers) + AgileX Tracer base + 3 webcams + RTX 3070 Ti laptop = **$32k**. Comparable in budget to a single Franka arm, ~6× cheaper than PR2/TIAGo. Anchors the [ACT](../../entities/act.md) + co-training-with-static-data IL pattern.
- **[Yuri](../../entities/yuri.md)** ([Sensori Robotics](../../entities/sensori-robotics.md), Southlake TX; 2026). **Integrated, supported** bimanual Physical-AI rig: 2× 7-DOF backdrivable **OpenArm+** arms + RealSense head + Jetson AGX Orin 64 GB, in Desktop (benchtop) or Mobile (wheeled **OpenBase**) form. Its differentiators are **out-of-the-box bilateral force-feedback teleoperation** (OpenLeader arms + Quest 3), a day-one [LeRobot](../../entities/lerobot.md)-recording + VLA-eval stack (GR00T / π0 / X-VLA / SmolVLA), and US-based support — "a complete robot, not a box of parts." Arms/base released as open hardware (OpenArm+ / OpenBase). Price is quote-only but the spec places it in the **research tier**, adjacent to Mobile ALOHA. The bimanual counterpart to Sensori's integrator role vs. the self-assembled [LeRobot](../../entities/lerobot.md) kits.

### Educational ($1k–$5k)
- **[XLeRobot](../../entities/xlerobot.md)** (open-source, LeRobot ecosystem). **Bimanual** mobile manipulator: 2× [SO-101](../../entities/so-arm101.md) arms (5+1 DoF each) + 2-DoF neck on a [LeKiwi](../../entities/lekiwi.md) holonomic omni base; 90% 3D-printed; **$660 tethered** (external PC) up to **~$1.3k untethered** with onboard [Jetson Orin Nano](../../entities/jetson-orin-nano.md). The educational-tier analog to [Mobile ALOHA](../../entities/aloha.md) at ~1/25th the cost — the wiki's **cheapest bimanual mobile manipulator**. The [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) build adds onboard compute, a Tri-Bus power topology, and the wiki's first on-edge VLA latency numbers; see [Jetson onboard compute for XLeRobot](jetson-onboard-compute-xlerobot.md).
- **[ROSOrin Pro](../../entities/rosorin-pro.md)** (Hiwonder). 6-DOF arm + mobile base + Jetson Orin Nano. Ships upstream [OpenClaw](../../entities/openclaw.md) as the LLM-agent brain plus Hiwonder's [`openclaw_controller`](../../entities/openclaw-controller.md) ROS 2 bridge module that wires it to the robot. Closest educational-tier analog to Stretch + stretch_ai, but with a real arm (vs Stretch's telescoping single-DOF arm).
- **[ROSOrin](../../entities/rosorin.md)** (Hiwonder). No-arm sibling of ROSOrin Pro. Mobile robot only; Jetson Orin Nano + cloud/offline LLM-agent curriculum.
- **[TurtleBot](../../entities/turtlebot.md)** (multiple vendors per generation; current: Open Robotics / Clearpath). Reference educational mobile robot since 2010. Lacks the agentic-AI bundling that ROSOrin / ROSOrin Pro now ship.

## By function

### Tabletop manipulators (no mobility)
[Franka Panda](../../entities/franka-panda.md), [xArm 7](../../entities/xarm-7.md).

### Mobile manipulators (arm + mobility)
**Single-arm:** [Stretch](../../entities/stretch.md) (research), [ROSOrin Pro](../../entities/rosorin-pro.md) (educational).
**Bimanual:** [Mobile ALOHA](../../entities/aloha.md) (research, $32k) and [XLeRobot](../../entities/xlerobot.md) (educational, $660–1.3k) — the two ingested bimanual *mobile* manipulators, ~25× apart in cost; plus [Yuri](../../entities/yuri.md) (Sensori; Desktop is bimanual tabletop, Mobile adds a wheeled base), the integrated force-feedback-teleop research-tier option.

### Mobile robots without arms
[ROSOrin](../../entities/rosorin.md), [TurtleBot](../../entities/turtlebot.md).

## Cross-tier observations

### "Research-grade" vs "educational" is a real boundary
- **Repeatability and torque** — Franka's 1 kHz torque control + research-grade servos vs ROSOrin Pro's HX-12H educational bus servos. Affects what kinds of policies can transfer cleanly. The RUM cross-embodiment story (~10pt drop, Stretch → xArm 7) is across two *commercial* arms; transferring to educational arms is a much larger gap.
- **Data availability** — every research-tier robot above has at least one large public dataset attached ([DROID](../../entities/droid.md) for Franka, [RUM](../../entities/robot-utility-models.md) for Stretch). Educational-tier robots don't yet.
- **Software stack maturity** — Franka has libfranka + frankx + ROS bindings + every major sim ([MuJoCo](../../entities/mujoco.md), [Isaac Sim](../../entities/nvidia-isaac-sim.md), Pinocchio). ROSOrin Pro has Hiwonder's stack + ROS 2 + Gazebo. Both functional; the research-tier ecosystems are deeper.

### Educational tier is converging on "Jetson + LLM agent + ROS 2"
The [ROSOrin](../../entities/rosorin.md) / [ROSOrin Pro](../../entities/rosorin-pro.md) / [OpenClaw](../../entities/openclaw.md) stack represents a generational update of the [TurtleBot](../../entities/turtlebot.md) educational role: same target audience (CS / robotics students learning ROS), but with **Jetson Orin Nano compute (~10× the Raspberry Pi)** and a **bundled agentic-AI / LLM-agent curriculum** that TurtleBot doesn't have. The interesting question is whether TurtleBot 5 (or whichever follows) will close that gap, or whether Hiwonder's lineage takes over the educational niche entirely.

### Research-tier mobile manipulation = Stretch (single-arm) or Mobile ALOHA (bimanual)
Two options in this wiki: **[Hello Robot Stretch](../../entities/stretch.md)** for single-arm + telescoping reach, and **[Mobile ALOHA](../../entities/aloha.md)** for bimanual + whole-body teleop. ROSOrin Pro (single-arm) and **[XLeRobot](../../entities/xlerobot.md) (bimanual)** are the educational-tier alternatives; Boston Dynamics Spot + Atlas would be the heavy-tier alternatives but aren't ingested here. When an academic paper says "real-robot mobile manipulation," **Stretch is implied for single-arm work, Mobile ALOHA for bimanual**. Both ship onboard compute and target the academic budget band ($20–32k).

> [!note] The educational-tier bimanual gap is now filled
> Until XLeRobot, bimanual mobile manipulation in this wiki meant **Mobile ALOHA at $32k** — research-tier only. [XLeRobot](../../entities/xlerobot.md) brings the same form factor (dual arms + mobile base) to **$660–1.3k** via 3D printing + [LeRobot](../../entities/lerobot.md)-ecosystem [SO-101](../../entities/so-arm101.md) arms, with an onboard-Jetson untethered path ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md)). The open question is capability: XLeRobot's 1 kg/arm payload + ~40 cm reach + hobby servos are a real step down from ViperX-300-class hardware — the cost collapse is genuine, the capability parity is not.

### Tabletop manipulation = Franka, with xArm 7 as second option
Same pattern — when a paper says "real-robot manipulation" without further qualification, **Franka is implied**. xArm 7 appears as a transfer target rather than a primary platform.

## What's missing from this wiki

Worth flagging robot platforms that show up in adjacent literature but don't have entity pages here yet:

- ~~**Boston Dynamics Spot** — quadruped reference platform (no entity page).~~ **Filed** as [Spot](../../entities/spot.md) (2026-05-09) alongside [Atlas](../../entities/atlas.md); [Unitree Go2](../../entities/unitree-go2.md) filed 2026-07-27 as the cheap-tier counterpart. Quadrupeds remain the **thinnest-sourced** platform tier here — neither entity is grounded in a primary technical source (Spot comes from a vendor blog, Go2 from an [Anthropic policy article](../../sources/anthropic-project-fetch-robot-dog.md) that never even names the model). No ingested paper uses a quadruped.
- **Pi (Physical Intelligence) hardware** — already in known gaps as needing a primary source.
- ~~**ALOHA / ViperX bimanual setup** — Stanford bimanual teleop platform; referenced indirectly via Chelsea Finn but no entity page.~~ **Filed 2026-05-25** as [ALOHA / Mobile ALOHA](../../entities/aloha.md) + [ViperX 300](../../entities/viperx-300.md) entities via the [Mobile ALOHA paper](../../sources/mobile-aloha-paper.md) ingest.
- **xArm 6** (UFactory's 6-DOF cousin to xArm 7) — sometimes cited as a cheaper alternative.
- **UR5 / UR10 / UR16** (Universal Robots) — collaborative arms common in industrial settings; not yet appearing in our literature.
- **Humanoids** — see the dedicated [Humanoid platforms survey](humanoid-platforms-survey.md) for that landscape; 10 humanoid entities filed there.

## Sources used in this synthesis

- Per-platform entity pages: [Franka Panda](../../entities/franka-panda.md), [xArm 7](../../entities/xarm-7.md), [Stretch](../../entities/stretch.md), [Mobile ALOHA](../../entities/aloha.md), [XLeRobot](../../entities/xlerobot.md), [ROSOrin Pro](../../entities/rosorin-pro.md), [ROSOrin](../../entities/rosorin.md), [TurtleBot](../../entities/turtlebot.md).
- [Cutting the Cord (Shaw et al., 2026)](../../sources/cutting-the-cord-untethered-xlerobot.md) — XLeRobot untethered build (cost, DoF, payload, onboard compute).
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
