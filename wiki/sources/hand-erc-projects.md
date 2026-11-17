---
title: "HAND ERC project list and project pages (retrieved 2026-11-17)"
type: source
url: https://hand-erc.org/project-pages-landing-page/
local_path: raw/2026-11-17-hand-erc-projects.md
sha256: a4c69d758d94c8d99ba973ab4715ee8b4a462cf0e38728b1684b7a6129a14aaa
capture: bundle
author: NSF HAND Engineering Research Center (headquartered at Northwestern University)
published: Unknown (projects labelled 2025 and 2026; retrieved 2026-11-17)
ingested: 2026-11-17
format: text extracted from the project list and 15 project pages
tags: [hand-erc, dexterous-manipulation, robot-hands, tactile-sensing, artificial-muscle, soft-robotics, diffusion-policy, drake, teleoperation, haptics, skill-library, benchmark, policy-steering, dexnex]
---

# HAND ERC project list and project pages

## Summary

The [HAND ERC](../entities/hand-erc.md)'s list of 31 projects, with one-paragraph descriptions of 15 of them. It shows what the center is actually doing under its three thrusts. The pages describe plans and aims in a sentence or two each, with project leads. No results, numbers or hardware specifications are given.

## Key claims

**Shape of the portfolio** (project list)
- 31 projects: 4 in Thrust 1 (Hands), 6 in Thrust 2 (Intelligent Dexterity), 5 in Thrust 3 (Human Interface), 7 in System Integration and Testbeds, and 9 in outreach, workforce development and the innovation ecosystem.
- Project codes carry a year. Most are 2025. Five system-integration projects are 2026: mechanical design, soft sensing skin, electrical integration, software infrastructure and **benchmarking dexterity**.

**Thrust 1: Hands**
- **Artificial muscle fibers** (Truby, Ware): electrostatically actuated fibers that are cheap, replaceable and bundled to scale, able to switch between high force and fast actuation in the manner of slow- and fast-twitch muscle.
- **Tactile sensing underlayer** (Fedder, Majidi): a stretchable, fine-grained sensor layer anchored to the hand's skeleton, mated to a glove-like skin from a companion project.
- **Textile sensing glove** (Cao, Fedder, Pollard): a glove with a dense network of sensing yarns that produces characteristic signals as hand joints move, for tracking dexterous motion.
- **Durable skin and tissue** (Hipwell, Krick): soft inner tissue for contact area and stable grip, a harder outer layer for low friction and wear resistance.

**Thrust 2: Intelligent Dexterity**
- **Grasp-affordance taxonomy and levels-of-dexterity benchmarks** (Argall): the canonical grasp-posture taxonomy is judged too thin for evaluating dexterity. The project adds what is done with each posture, then defines metrics, benchmark tasks and simulation environments for each combination.
- **Defining dexterous skills** (Kroemer): a general representation of manipulation skills, how they take sensor input, how human input adapts them, and how they combine into a hierarchy. This is the basis of the skill library.
- **DexNex Drake Sim** (Lynch, Tedrake): a high-fidelity simulation of DexNex, *"the bimanual dexterous teleoperation system at Northwestern"*, in [Drake](../entities/drake.md).
- **DexNex Diffusion Policies** (Tedrake): behavior cloning with [Diffusion Policy](../entities/diffusion-policy.md) from teleoperation, later augmented with reinforcement learning in the Drake simulation. The page states the design rule: *"The teleoperator has no privileged information: they see only what the robot sees and feel only what the robot feels."*
- **Self-supervised models of soft hands** (Sitzmann): learning dynamics and kinematics models for robots where hand-built models are hard to obtain.
- **Soft hand dexterity learning** (Murphey, Truby): data-efficient learning co-developed with soft grippers, aiming at *"near real-time learning of dexterous skills without simulation or demonstration."*

**Thrust 3: Human Interface**
- **Essential haptic cues** (Friesen, Orta-Martinez): which skin-deformation cues, at what resolution, are needed for dexterous tasks.
- **Haptic glove with miniature continuously variable transmissions** (Moore, Orta-Martinez): kinesthetic feedback across several degrees of freedom, and a study of how degrees of freedom relate to manipulation performance.
- **Mapping dexterous action to interface elements** (Mutlu, with Argall): how people express intent in a task such as opening a jar of peanut butter and spreading it, and interfaces that map instructions to dexterous primitives.
- **Inference-time steering of diffusion policies** (Shah): extends the group's Inference-Time Policy Steering framework so a person can guide a pre-trained policy at deployment without retraining.

**System integration**
- **Bones, joints and tendons** (Colgate): a precursor to the hand design. A lightweight, durable, high-degree-of-freedom hand with **remotized actuators**, tested on finger and tendon rigs against established benchmarks (NIST) and new ones (admittance, cycle life).

## Analysis

- **The center is still before its first hand.** The hand project is described as a "precursor to hand design", and mechanical design, skin, electrical integration and software are 2026 projects. Two years into the first five-year term, the public record is plans.
- **The learning stack is conventional; the hardware is not.** Policies are Diffusion Policy from teleoperation plus simulation-based reinforcement learning, the same recipe found across this wiki. The new work is in muscles, skins and tendons.
- **The no-privileged-information rule matters for data quality.** If the operator sees and feels only what the robot does, the demonstrations contain no information the policy cannot access. That addresses a known weakness of teleoperated data, where the operator's direct view of the scene leaks into the demonstrations ([imitation learning](../concepts/learning/imitation-learning.md)).
- **Benchmarks before hardware.** A dexterity taxonomy with benchmark tasks, and a separate benchmarking project, would give the field something it lacks: a shared way to say how dexterous a hand is. That may be the center's most reusable output, and it would be worth ingesting when published.
- **Two different bets on learning sit side by side.** One project learns from demonstration and simulation; another aims to learn *"without simulation or demonstration."*
- **Evidence weight.** Project descriptions only. Sixteen listed projects have no page, including the benchmarking project and all outreach and workforce items.

## Entities mentioned

- [HAND ERC](../entities/hand-erc.md)
- [argallab](../entities/argallab.md) — its director leads the taxonomy and benchmark project
- [Russ Tedrake](../entities/russ-tedrake.md) — leads the diffusion-policy project, co-leads the simulation
- [Drake](../entities/drake.md) — the simulation engine
- [Diffusion Policy](../entities/diffusion-policy.md) — the behavior-cloning method

## Concepts touched

- [Tactile sensing](../concepts/robotics/tactile-sensing.md)
- [Dexterous tool manipulation](../concepts/robotics/dexterous-tool-manipulation.md)
- [Imitation learning](../concepts/learning/imitation-learning.md)

## Open questions

- What are the hand's specifications: degrees of freedom, actuator count, mass, payload?
- Has the grasp-affordance taxonomy or any benchmark been published?
- What hardware does DexNex use today, before the center's own hand exists?
