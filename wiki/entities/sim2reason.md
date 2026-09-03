---
title: Sim2Reason
type: entity
subtype: system
created: 2026-09-03
updated: 2026-09-03
sources: 1
tags: [sim2reason, synthetic-data, mujoco, physics, llm, reasoning, lambda, cmu, icml-2026, simulation, transfer]
---

**Sim2Reason** — an **ICML 2026** result from [Lambda](lambda.md) and Carnegie Mellon asking whether an LLM can learn to solve **International Physics Olympiad** problems from **synthetic data alone**. Presented at [Day 3 of the World Modeling Workshop](../sources/chicago-booth-world-modeling-workshop-2026-day3.md) by Amir Zadeh as the opening argument for taking simulators seriously as data engines.

## The pipeline

Fully machine-generated, with no human annotation in the loop:

1. A domain-specific language procedurally generates physical scenarios in **[MuJoCo](mujoco.md)** — a ball on a ramp, a pulley system, a charged particle in a field — with an **LLM writing the scene descriptions**.
2. The simulator runs them and emits complete traces: forces, velocities, accelerations, energy flows.
3. The traces are turned into **verified question–answer pairs** in three modes — numeric, reverse, and symbolic.
4. A second model fine-tunes on those pairs.

Zadeh's framing of the loop is *"an LLM controlling MuJoCo and an LLM learning"* — the simulator is the only thing in it that knows any physics, and it is the arbiter.

## The results, and the one that matters

- **IPhO mechanics: +5–10 percentage points zero-shot, across 3B to 72B parameters.** The gain being roughly stable across an order of magnitude of model size is what makes it a data result rather than a capacity result: *"the knowledge that these data points are creating for us is generalizable across these models."*
- **JEEBench: +17.9%** at 32B.
- Their fine-tuned models land close to frontier models that (as far as the authors know) used **curated human expert data** — which is the claim Zadeh actually cares about: *"this gap … this human-level expert data could be closed with a simulator."*
- **It transfers to mathematics** (AIME 2025, MATH 500). *"A physics simulator generating data that makes you do better in math, right? Despite the fact that it was never meant as a math thing."*

> [!note] "Correlated frontiers" is the idea worth taking
> Zadeh's name for the transfer effect. If simulator-derived physics data improves an unrelated symbolic-reasoning benchmark, then the value of a simulation run is not bounded by the task it was generated for — which changes the arithmetic on whether a given simulation budget is worth spending. It also **sits directly against the cost model in the rest of his talk**: [simulation economics](../concepts/world-models/simulation-economics.md) says rendered, sensor-rich robotics simulation is brutally expensive, while Sim2Reason's physics-trace generation is cheap because it never renders anything. **The affordable case is the one where you keep the state and throw away the pixels.**

## Where it sits in this wiki

It is a **[synthetic flywheel](../concepts/learning/synthetic-data-flywheel.md)** result from an unexpected direction: not synthetic environments for embodied policies, but a physics engine used as a *verifier* generating reasoning supervision for a language model. Compare [Aleksandra Faust](aleksandra-faust.md)'s Day 2 thesis that synthetic data should be a **superset of reality rather than a replica** — Sim2Reason is a clean instance, since scenes like the ones it generates *"can be really difficult to make in the real world … but ultimately very straightforward in a simulator."*

## Related

- [Lambda](lambda.md) — the lab; also the source of the cost model.
- [Simulation economics](../concepts/world-models/simulation-economics.md) — why the no-rendering case is the affordable one.
- [The synthetic flywheel](../concepts/learning/synthetic-data-flywheel.md) · [generative data augmentation](../concepts/learning/generative-data-augmentation.md).
- [MuJoCo](mujoco.md) — the simulator.
- [Aleksandra Faust](aleksandra-faust.md) — the superset-of-reality thesis it instantiates.

## Mentioned in

- [Third World Modeling Workshop — Day 3](../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — opening result of the Lambda talk.

> [!note] Built from the talk plus Lambda's own blog post, not the paper
> The ICML paper is not ingested. Benchmark numbers here come from Lambda's write-up (the primary for its own result); the transcript's live figures are lower and less specific, and were not used.
