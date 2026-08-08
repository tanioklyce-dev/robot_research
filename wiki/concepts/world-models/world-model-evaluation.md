---
title: World-model evaluation
type: concept
created: 2026-08-07
updated: 2026-08-08
sources: 4
tags: [world-model, evaluation, benchmark, physical-validity, policy, vbench, worldscore]
---

**World-model evaluation** — establishing whether a learned environment is **valid for the use it is being put to**. Distinct from measuring how good its outputs look, and distinct from measuring whether a policy trained inside it scores well.

The [HAI world-model brief](../../sources/hai-world-model-spatial-intelligence-brief.md) frames this as the third governance object, after content (what a system generates) and authority to act (what a system may do): **the validity of the learned environment itself.** Its verdict on the current state is unambiguous — evaluation "remains a research patchwork rather than a settled standard," and "none gives policymakers an adequate basis to assess a world model for safety-critical deployment."

## Two failure modes that look identical from the outside

**1. The visual plausibility trap.** A renderer produces a persuasive depiction without modeling the geometry, dynamics, or physical constraints needed for safety. AI-generated video shows fire or flowing water that doesn't obey physics; a generated building looks sound with no stable underlying structure. The system looks competent **to a human observer**.

**2. The simulation-to-reality gap.** The system performs well *inside* the generated environment and fails outside it — sensor noise, lighting, weather, wear, unexpected human behavior, edge-case physics. Here nobody is fooled by appearances; the model is simply wrong about a world it was never shown. See [sim-to-real transfer](../learning/sim-to-real-transfer.md).

**And the compound of the two, which is specific to world models: teaching to a flawed test.** When a learned model is used both to *train* a system and to *judge* it, the model's errors become invisible. The brief's example: if the model understates the risk of skidding in rain, a vehicle trained inside it learns to drive too fast — and still scores well when the same flawed model tests it. "The score would reflect an error in the model, not readiness for a real road."

> [!warning] Now measured — and the bias has a direction
> [WorldArena](../../sources/worldarena-paper.md) ran two world models as policy evaluators against the RoboTwin simulator's own verdict and found that **both "have consistently higher success rates than those measured in the simulator, suggesting partial overfitting to successful trajectories."** A learned evaluator *flatters* the policies it evaluates.
>
> What survives is **ranking**, not level: Ctrl-World correlates at **r = 0.986** with the simulator's ordering while reporting inflated absolute rates; Cosmos-Predict 2.5 manages only **r = 0.483**. So a learned evaluator can be a usable comparator and an unusable measurement at the same time.
>
> One complication before treating this as settled: [Veo](../../entities/veo.md) reports the **opposite sign** — Pearson 0.88 against 1,600+ real evaluations with absolute predicted rates running *low*. Both papers agree ranking beats level; they disagree on which way the level moves. Different substrates (RoboTwin sim vs real Gemini Robotics evaluations), so the disagreement may be about what the model was compared against rather than about the models.

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

| Benchmark | What it measures | Primary source |
|---|---|---|
| **VBench** | Visual quality, prompt alignment, temporal smoothness — explicitly **not** whether scenes obey physical law | not ingested |
| **VideoPhy** / **PhyGenBench** | Physical commonsense in generated video | not ingested |
| **WorldScore** | Controllability, quality, and dynamics in world *generation* (Duan, Yu, Chen, [Fei-Fei Li](../../entities/fei-fei-li.md), Wu — arXiv 2504.00983) | not ingested |
| **WorldModelBench** | Judges video models specifically **as world models** | not ingested |
| **[WorldArena](../../entities/worldarena.md)** | Perceptual quality **plus functional utility** as data engine / policy evaluator / action planner — extended in 2.0 to visuotactile, RL environments, and real robots | **[ingested](../../sources/worldarena-paper.md)** · **[2.0](../../sources/worldarena-2-paper.md)** |
| **[WorldRoamBench](../../entities/worldroambench.md)** | **Long-horizon stability** of interactive world models: per-frame action, visual drift, interaction physics, memory | **[ingested](../../sources/worldroambench-paper.md)** |
| **[LIBERO](../../entities/libero.md)** | Simulated manipulation task completion — the robotics anchor of the list | [ingested](../../sources/libero-pro-paper.md) |

The progression VBench → VideoPhy/PhyGenBench → WorldScore/WorldModelBench → WorldArena runs from *how it looks* toward *what it is good for*. WorldArena and WorldRoamBench sit at that far end and now have primary sources here.

Note a small closed loop in the policy record: **WorldScore was co-authored by two of the HAI brief's own authors** (Fei-Fei Li, Jiajun Wu), and its first author Haoyi Duan appears on WorldArena 2.0. The brief presents the benchmark landscape as external evidence without noting the overlap.

### What the measurements actually say

Two independent labs, two task domains, one result.

**[WorldArena](../../entities/worldarena.md)** (manipulation) quantifies the gap directly. Its EWMScore — the unweighted mean of 16 video-quality metrics — correlates with:

| Against | Pearson r |
|---|---:|
| Human judgment | **0.825** |
| Data-engine utility | 0.600 |
| **Action-planning performance** | **0.360** |

**[WorldRoamBench](../../entities/worldroambench.md)** (open-world roaming) finds the same thing without measuring the same quantity: "high visual quality ≠ good action following" — the two are **"largely independent."** It adds that **trajectory-level action scores above 85 can hide below-65% per-frame accuracy**, so even the *action* metric everyone reports was measuring the wrong thing.

Concrete performance, from WorldArena:

- **As a data engine** — no world model matches real demonstration data (best: WoW 45%/71% vs real 77%/66%), and the gap *widens* from simulation to a real robot.
- **As an action planner** — every world model loses to a [π0.5](../../entities/pi-zero-5.md) policy by **3–4×** (best 20%/21% vs 77%/66%).
- **As an RL environment** — this one works. Policies trained inside a learned world model close roughly two-thirds of the gap to simulator-based RL and beat SFT across the board ([WorldArena 2.0](../../sources/worldarena-2-paper.md)).

> [!note] The role distinction is the finding
> Learned dynamics are good enough to **shape** a policy and not good enough to **be** one. Neither paper states it this way, and it is the most decision-relevant thing in the cluster — see [what world models are measurably good for](../../syntheses/world-models/what-world-models-are-measurably-good-for.md).

The brief's summary judgment holds: "leading models still fail to maintain basic physical consistency, and high benchmark scores can conceal weaknesses in physical reasoning or robustness to changing conditions."

### A tension the metrics create

WorldRoamBench: **stricter physics adherence may compromise action following.** A model that refuses to clip through a wall must deviate from the keystroke-prescribed trajectory — so correct behavior is scored as error, and an aggregate that averages action and physics penalizes it twice. Nobody has proposed the right scoring rule. Worth remembering whenever a world-model leaderboard reports a single number.

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

- [WorldArena paper](../../sources/worldarena-paper.md) — the perception–functionality gap, measured.
- [WorldArena 2.0 paper](../../sources/worldarena-2-paper.md) — visuotactile, world-model-as-RL-environment, and the sim-to-real usability gap.
- [WorldRoamBench paper](../../sources/worldroambench-paper.md) — long-horizon stability; per-frame action, visual drift, interaction physics, action-decoupled memory.

- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../../sources/hai-world-model-spatial-intelligence-brief.md)
