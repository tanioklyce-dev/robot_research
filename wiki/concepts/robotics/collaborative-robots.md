---
title: Collaborative robots (cobots)
type: concept
created: 2026-07-16
updated: 2026-07-16
sources: 4
tags: [cobots, collaborative-robots, industrial-robotics, safety, machine-vision, human-robot-collaboration]
---

# Collaborative robots (cobots)

## Definition

A **collaborative robot (cobot)** is an industrial robot arm designed to work **in a shared workspace alongside humans without safety fencing**, using force/torque limiting, compliant control, and collision detection so contact with a person is inherently safe. Cobots trade peak speed and payload for **safety, ease of programming (lead-through / drag teaching), and fast redeployment** — the qualities that let non-experts set them up on a factory line.

The category is distinct from the wiki's usual **learned-policy / VLA** center of gravity: classical cobots are programmed by demonstration or waypoint teaching and run deterministic motion, not neural policies. They represent the **industrial-automation lineage** of "AI robotics" that predates and runs parallel to the imitation-learning wave.

## Key vendors

- **[Techman Robot](../../entities/techman-robot.md)** — Taiwan; the first cobots with a **built-in vision system**; world's #2 cobot brand behind Universal Robots (~10% vs ~50% share, 2021) ([Techman profile](../../sources/techman-robot-about.md)).
- **Universal Robots** (Denmark) — the category-defining market leader (~50% share); not yet a standalone entity here.
- **[Standard Bots](../../entities/standard-bots.md)** — US 6-axis cobot (RO1) with a self-serve learn-by-demonstration platform; the point where classical cobots start reaching toward imitation learning.

## Relation to humanoids

Industrial humanoids increasingly borrow cobot safety framing: **[Agile ONE](../../entities/agile-one.md)** is explicitly pitched as a **co-working** humanoid with proximity sensors and per-joint force-torque sensing for safe operation alongside people ([Agile ONE launch](../../sources/agile-robots-agile-one-launch.md)) — a humanoid inheriting the cobot's "safe near humans" contract.

## Related concepts

- [Robot safety standards (ISO 13482)](robot-safety-standards.md) — the machinery-safety framework cobots operate under (ISO 10218 / 15066 specifically cover collaborative operation)
- [End-user robot programming](end-user-robot-programming.md) — lead-through teaching is the cobot's non-expert programming model
- [Whole-body control](whole-body-control.md) — where co-working extends from arms to full humanoids

## Mentioned in

- [Techman Robot — Company Profile](../../sources/techman-robot-about.md)
- [Agile Robots launches Agile ONE](../../sources/agile-robots-agile-one-launch.md)
