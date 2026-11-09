---
title: "Practice Makes Precise: At CoRL, NVIDIA and Partners Reveal How Robots Rehearse Delicate Work in Simulation"
type: source
url: https://blogs.nvidia.com/blog/robotics-simulation-advancements-corl/
author: "Sasa Docca (NVIDIA)"
published: 2026-11-09
format: vendor blog post
tags: [nvidia, corl-2026, gr00t-2, isaac-lab, newton, isaac-lab-arena, dexbench, vabar, alphanist, steel, agentic-robotics]
ingested: 2026-11-09
---

# Practice Makes Precise: At CoRL, NVIDIA and Partners Reveal How Robots Rehearse Delicate Work in Simulation

## Summary

NVIDIA's announcement post for CoRL 2026 in Austin. It introduces [GR00T 2](gr00t-2-whitepaper.md), new Isaac Lab, Newton and Arena releases, two industrial benchmarks and [Graph-as-Policy](gap-graph-as-policy-paper.md).

Its GR00T 2 and GaP claims are summaries of primary documents, and those are the pages to cite. **Everything else here rests on this post alone**, and the numbers are vendor-reported.

## Key claims

**Conference.** Two NVIDIA papers are among six Best Paper finalists: GRAIL (Generating Humanoid Loco-Manipulation from World Models) and [RoboTTT](robottt-paper.md).

**GR00T 2.** It is described as an open world-action model on [Cosmos](../entities/nvidia-cosmos.md). The post repeats 40 of 50 tasks, 71% and 95%, without the [selection condition](gr00t-2-whitepaper.md) stated in the report. Named users:

- Nexuni is testing laundry handling.
- Foxconn is applying it to server manufacturing.
- Siemens is evaluating industrial use cases.
- MicroAGI post-trains it with RL for Ethernet cable swapping on a [YAM](../entities/yam.md).

**Data tools.** An open Video to Data workflow turns human video into simulated robot demonstrations. The EgoHand open model reconstructs 3D hand motion and has over 40,000 Hugging Face downloads in two weeks.

**[Isaac Lab](../entities/nvidia-isaac-lab.md) 3.0 and [Newton](../entities/newton-physics-engine.md).**

- Agents can set up training environments.
- Researchers can switch between PhysX and Newton, and choose renderers.
- A new RL post-training library applies to foundation models like GR00T.
- Newton adds deformable objects and complex articulated hands.
- **Up to 2.5× the training throughput of Isaac Lab 2.3 with PhysX** on a vision-based dexterous benchmark.

**Partners using the stack.**

- Skild AI's STEEL is a rigid-body solver built on Newton.
- Flexion trains its Reflect model with Isaac Lab and Newton.
- FieldAI trains and validates policies with Newton, Isaac Lab and Isaac Sim.
- Dyna Robotics trains whole-body controllers for its Taku robot.
- Walden Robotics uses Isaac Sim rendering.
- Dexmate is exploring coding agents that rehearse in Isaac Sim before running on Vega.

**AlphaNIST.** One policy learns all 20 NIST Assembly Task Board tasks from a success signal alone, with over 98% training success. Separate per-task policies reach 81%, and it uses about 39× less GPU time. Its method, Success-Guided Sampling (University of Washington and NVIDIA), focuses practice on tasks succeeding about half the time. Training success isn't real-robot success, and the post gives no transfer result.

**[Isaac Lab-Arena](../entities/isaac-lab-arena.md) 0.4** arrives as a developer preview.

**Benchmarks.**

- **DexBench** (RLWRLD with NVIDIA): 15 tasks across four scenes in retail, logistics, manufacturing and hospitality.
- **VABAR** (UC Berkeley and NVIDIA): the Variational Automation Benchmark for Agentic Robotics, six industrial tasks with standard variations, difficulty tiers and metrics.

**GaP.** Ken Goldberg calls agentic robotics *"the most exciting technological development since the internet in 1995."* Ambi Robotics, Bosch Research and Siemens are exploring GaP.

## Entities mentioned

- [NVIDIA](../entities/nvidia.md), [NVIDIA GR00T](../entities/nvidia-groot.md), [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md), [Newton](../entities/newton-physics-engine.md), [Isaac Lab-Arena](../entities/isaac-lab-arena.md), [NVIDIA Cosmos](../entities/nvidia-cosmos.md)
- [Graph-as-Policy](../entities/graph-as-policy.md), [Ken Goldberg](../entities/ken-goldberg.md), [Skild AI](../entities/skild-ai.md), [YAM](../entities/yam.md)

## Concepts touched

- [Variational automation](../concepts/robotics/variational-automation.md) — VABAR gives the term a benchmark.
- [Code as policy](../concepts/agents/code-as-policy.md) — marketed here as "agentic robotics."

## Open questions

- **DexBench, VABAR and AlphaNIST need their own primaries** before their numbers feed any decision.
- **GRAIL** is a Best Paper finalist and not yet in this wiki.
- **Is the 2.5× a fair comparison?** It compares two major Isaac Lab versions as well as two solvers, on a benchmark the post doesn't name.

## Cited by
- [NVIDIA GEAR Lab](../entities/nvidia-gear.md)
