---
title: World-model evaluation
type: concept
created: 2026-08-07
updated: 2026-08-07
sources: 1
tags: [world-model, evaluation, benchmark, physical-validity, policy, vbench, worldscore]
---

**World-model evaluation** — establishing whether a learned environment is **valid for the use it is being put to**. Distinct from measuring how good its outputs look, and distinct from measuring whether a policy trained inside it scores well.

The [HAI world-model brief](../../sources/hai-world-model-spatial-intelligence-brief.md) frames this as the third governance object, after content (what a system generates) and authority to act (what a system may do): **the validity of the learned environment itself.** Its verdict on the current state is unambiguous — evaluation "remains a research patchwork rather than a settled standard," and "none gives policymakers an adequate basis to assess a world model for safety-critical deployment."

## Two failure modes that look identical from the outside

**1. The visual plausibility trap.** A renderer produces a persuasive depiction without modeling the geometry, dynamics, or physical constraints needed for safety. AI-generated video shows fire or flowing water that doesn't obey physics; a generated building looks sound with no stable underlying structure. The system looks competent **to a human observer**.

**2. The simulation-to-reality gap.** The system performs well *inside* the generated environment and fails outside it — sensor noise, lighting, weather, wear, unexpected human behavior, edge-case physics. Here nobody is fooled by appearances; the model is simply wrong about a world it was never shown. See [sim-to-real transfer](../learning/sim-to-real-transfer.md).

**And the compound of the two, which is specific to world models: teaching to a flawed test.** When a learned model is used both to *train* a system and to *judge* it, the model's errors become invisible. The brief's example: if the model understates the risk of skidding in rain, a vehicle trained inside it learns to drive too fast — and still scores well when the same flawed model tests it. "The score would reflect an error in the model, not readiness for a real road."

> [!warning] This is the one the wiki should watch for
> Learned-simulator evaluation is arriving in exactly this shape. [Veo](../../entities/veo.md) is a video foundation model specialized as a **policy-evaluation simulator**; the Dream* line generates training data for the policies it neighbors. Any pipeline where the generator of training data and the arbiter of success share weights, architecture, or training corpus inherits this failure. Nothing in the wiki currently measures the size of that effect.

## Each architecture fails differently

The brief's sharpest technical observation, and it maps cleanly onto this wiki's existing families:

| Design | Characteristic failure | Wiki page |
|---|---|---|
| Video generators **without a persistent scene representation** | Lose consistency over time; objects drift, flicker, vanish | [generative-video vs JEPA](../../syntheses/world-models/generative-video-vs-jepa-world-models.md) |
| **3D-native** systems (explicit geometry) | Spatially consistent, but "still fail to capture how a world *changes*" | [world-model simulators](world-model-simulators.md) |
| **Latent state-space** models (compressed internal representation) | Prioritize predicting change over visual detail — so visual metrics score them wrongly in both directions | [JEPA](jepa.md), [latent space](latent-space.md) |

The consequence: **each demands a different evaluation.** A single leaderboard across these families is measuring three different things.

## Evaluation should match function

Keyed to the [functional taxonomy](world-model-functional-taxonomy.md):

- **Renderer** used for concept art → judge by how convincing it looks. Plausibility *is* the product.
- **Simulator** used for infrastructure planning → higher bar: is its geometry and physics **actually correct**?
- **Planner** embedded in a robot → tested repeatedly across varied real-world conditions.
- **Interactive** systems add one more: do skills practiced in simulation, by a person or a robot, **transfer to the real task**?

The principle: *the closer a system comes to real-world actions, the more its evaluation should weigh physical validity, robustness, and transfer beyond the test setting.*

## The benchmark landscape as of mid-2026

Named by the brief; none has a primary source in this wiki yet, which makes this list a standing ingest backlog.

| Benchmark | What it measures |
|---|---|
| **VBench** | Visual quality, prompt alignment, temporal smoothness — explicitly **not** whether scenes obey physical law |
| **VideoPhy** | Physical commonsense in generated video |
| **PhyGenBench** | Physical commonsense in generated video |
| **WorldScore** | Controllability, quality, and dynamics in world *generation* |
| **WorldModelBench** | Judges video models specifically **as world models** |
| **WorldArena** | Perceptual quality **plus usefulness in training, testing, and planning robot behavior** |
| **[LIBERO](../../entities/libero.md)** | Simulated manipulation task completion — the robotics anchor of the list |

The progression VBench → VideoPhy/PhyGenBench → WorldScore/WorldModelBench → WorldArena is a progression from *how it looks* toward *what it is good for*. **WorldArena is the only one scored on downstream utility**, which makes it the most interesting and the least documented here.

Even so: "leading models still fail to maintain basic physical consistency, and high benchmark scores can conceal weaknesses in physical reasoning or robustness to changing conditions."

## The wiki's own instrument agrees, from the policy side's blind spot

[Robot policy evaluation](../robotics/robot-policy-evaluation.md) reaches the same verdict about *policies* that the brief reaches about *world models*, with numbers the brief doesn't have: **±2 pp confidence requires ≈1,030 rollouts against the ~70 typically run**; scores saturate above 90%; and [LIBERO-PRO](../../sources/libero-pro-paper.md) drops >90% policies to **0.0%** under perturbations that preserve the task. That last result is the empirical form of the brief's "high benchmark scores can conceal weaknesses."

So the two literatures converge and neither cites the other. The policy brief says no benchmark supports safety-critical deployment decisions; the robotics measurement literature says the benchmarks in use don't even support ranking two policies against each other.

## Related concepts

- [Robot policy evaluation](../robotics/robot-policy-evaluation.md) — the statistical case, from inside robotics.
- [Instruction leakage](instruction-leakage.md) — a concrete, diagnosed world-model evaluation confound.
- [Sim-to-real transfer](../learning/sim-to-real-transfer.md) — the older name for half of this problem.
- [World-model governance](../safety/world-model-governance.md) — what to do about it.
- [Robot safety standards](../robotics/robot-safety-standards.md) — the certification regimes this would have to plug into.

## Mentioned in

- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../../sources/hai-world-model-spatial-intelligence-brief.md)
