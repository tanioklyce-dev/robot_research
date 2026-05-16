---
title: Robot Simulation File Formats — URDF vs MJCF vs USD (Source Robotics)
type: source
url: https://source-robotics.com/blogs/blog/robot-simulation-files-urdf-vs-mjcf-vs-usd
author: Source Robotics
published: 2026-03-13
ingested: 2026-05-07
tags: [openusd, urdf, mjcf, comparison, robot-description, format]
---

## Summary
Practical practitioner-oriented comparison of the three dominant robot description formats — **URDF**, **MJCF**, and **USD** — with explicit use-case recommendations. Useful as a survey-level baseline; less authoritative than the [UsdPhysics whitepaper](openusd-rigid-body-physics-proposal.md) but more direct about practical positioning.

## Key claims

### Format positioning

| | URDF | MJCF | USD |
|---|---|---|---|
| Origin | ROS | [MuJoCo](../entities/mujoco.md) physics engine | Pixar / NVIDIA Omniverse |
| Technology | XML | XML | Scene graph |
| Core purpose | Robot kinematics description | Physics simulation | General scene representation |

### Strengths and weaknesses

**URDF** — widely supported in ROS; simple link/joint structure; **but**: contact modeling is limited, actuator modeling is basic, **cannot represent closed kinematic chains**.

**MJCF** — precise physics, advanced contact handling, first-class actuators / sensors / tendons / equality constraints; **but**: tightly coupled to the MuJoCo ecosystem.

**USD** — scales to extremely large scenes via layered composition; integrates rendering + physics + assets comprehensively; **but**: more complex than alternatives; steeper learning curve.

### Recommendations (paraphrased)
- **ROS workflows / motion planning / kinematic description** → URDF.
- **MuJoCo research / RL / precise contact** → MJCF.
- **Large environments / Omniverse-modern simulators / collaborative assets** → USD.

### Conversion paths
The article notes URDF "is often converted into simulator-specific formats" but does **not** detail specific tools or bidirectional paths.

## Entities mentioned
- [OpenUSD](../entities/openusd.md)
- [MuJoCo](../entities/mujoco.md)
- (URDF, MJCF — concepts not yet stubbed in this wiki)

## Concepts touched
- Robot description format trade-offs.

## Open questions
- The article treats USD as primarily an Omniverse-native format and doesn't cover [MuJoCo Playground](../entities/mujoco-playground.md)'s OpenUSD adoption — a 2026-relevant fact. Suggests the article's center of gravity is still ROS/MuJoCo with USD as an outsider, even though the substrate convergence story (covered in [Newton + OpenUSD synthesis](../syntheses/simulators/newton-openusd-substrate-convergence.md)) implies USD is moving inside the MuJoCo stack too.
- No mention of UsdPhysics-specific features (articulations, joint drives) — treats USD as a scene format rather than a physics-schema format.
