---
title: Yunzhu Li
type: entity
subtype: person
created: 2026-08-26
updated: 2026-08-26
sources: 4
tags: [person, robotics, world-model, manipulation, simulation, real-to-sim, code-as-policy, scenix, columbia]
---

**Yunzhu Li** — **co-founder of [SceniX](scenix.md)** and **Assistant Professor of Computer Science at Columbia University**. PhD at **MIT**; postdoc at the **Stanford Vision and Learning Lab with [Fei-Fei Li](fei-fei-li.md)** (one year — he already held a faculty offer). In this wiki he also appears as a co-author on [VoxPoser](../sources/voxposer-paper.md) and [CodeAct](../sources/codeact-paper.md). Since 2026-07-21 at [World Labs](world-labs.md), and relocating to San Francisco.

Fei-Fei Li's description: "a full-stack researcher in robotics, from modeling to hardware" ([a16z conversation](../sources/a16z-worldlabs-scenix-conversation.md)).

## The stated north star

Asked whether he has a philosophical position comparable to Fei-Fei Li's spatial-intelligence framing, he declines one:

> **"My north star is to make robots work. In the real environment. I'm a very practical person. I want the robot to work."**

That pragmatism is what Fei-Fei Li names as the reason for the acquisition — SceniX's "first instinct is work with design partners and customers in real industry," which she calls "a refreshing way of approaching robotics" for a team out of academia.

## Positions worth recording

- **Simulation and real data are not opposed.** Against [Sergey Levine](sergey-levine.md)'s position that simulation always deviates and real collection is essential: *"they don't contradict with each other."* A simulator "doesn't necessarily have to be pure physics — it can be a combination between both physics and also learning," physics-weighted early and learning-weighted as deployment data accumulates.
- **Fidelity should be judged by essential structure, not realism.** Quadrupeds walk on snow and bushes without a simulator that models snow or bushes precisely; you need "a simulation that captures the essential structure of the problem" plus randomization. He leaves *what level of fidelity is needed* explicitly open.
- **Semi-structured before unstructured.** Robotics has moved structured (factories) → semi-structured (warehouses, restaurants, hotels) → unstructured (homes, "the grand challenge"), and the tractable target now is the middle. Casado characterizes his view as humanoid predictions being "a little bit aggressive."
- **Robots have no human-in-the-loop grace period.** You don't blindly trust an LLM to book a flight — a person reads the output. *"But for robotic models, out of the box, the robot has to work reliably in the real environment."*
- **Human-level power efficiency "will take a very long time"** — because a working robot is a *system*, down to "the friction coefficient of your fingers."
- **Video world models fail at object permanence.** "Imagine if a robot pushes an object forwards. The object just magically disappears" — the manipulation-timescale version of the [spatial intelligence](../concepts/world-models/spatial-intelligence.md) leave-and-return probe.

## In this wiki

- **[VoxPoser](../sources/voxposer-paper.md)** (CoRL 2023) — co-author; LLM-composed 3D value maps for manipulation.
- **[CodeAct](../sources/codeact-paper.md)** — co-author.
- **[SceniX / R2S2R](../concepts/robotics/real-to-sim-to-real.md)** — the [results post](../sources/world-labs-r2s2r.md) and the [a16z conversation](../sources/a16z-worldlabs-scenix-conversation.md) that explains it.
- He also worked on the **[BEHAVIOR-1K](behavior-benchmark.md)** survey during the Stanford postdoc, and supplies the datapoint that **one-third of the thousand surveyed tasks are cleaning**.

## Related

- [Fei-Fei Li](fei-fei-li.md) — postdoc advisor, VoxPoser senior author, now acquirer.
- [Changxi Zheng](changxi-zheng.md) — SceniX co-founder; the simulation half.
- [Wenlong Huang](wenlong-huang.md) — VoxPoser first author.
- [SceniX](scenix.md) / [World Labs](world-labs.md) / [real-to-sim-to-real](../concepts/robotics/real-to-sim-to-real.md).

## Mentioned in

- [VoxPoser paper](../sources/voxposer-paper.md)
- [CodeAct paper](../sources/codeact-paper.md)
- [Building Worlds That Train Robots (R2S2R)](../sources/world-labs-r2s2r.md)
- [Fei-Fei Li is Solving the Hardest Problem in Robotics (a16z × World Labs)](../sources/a16z-worldlabs-scenix-conversation.md)
- [World Labs Acquires SceniX](../sources/world-labs-scenix-acquisition.md)
