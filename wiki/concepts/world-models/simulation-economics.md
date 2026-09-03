---
title: Simulation economics
type: concept
created: 2026-09-03
updated: 2026-09-03
sources: 1
tags: [simulation, synthetic-data, cost, gpu, rendering, isaac-sim, world-models, infrastructure, lambda, data-engineering]
---

**Simulation economics** — what it costs, in GPU-hours and dollars, to generate a unit of training data from a physics simulator, and how that cost varies with scene complexity and sensor stack. The wiki has argued from many directions that [synthetic data scales](../learning/synthetic-data-flywheel.md). This page holds the first source that **prices** it: Amir Zadeh's *Scaling GPU Infrastructure* talk at [Day 3 of the World Modeling Workshop](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md), from [Lambda](../../entities/lambda.md).

## The unit that matters: simulation-seconds per GPU-second

Not frames, not steps — **how much simulated world time you buy with one second of GPU time.** Zadeh's worked example fixes a plausible production-scale job and varies only the scene:

> 100,000 environments × 1,024 runs each × 90-second rollouts, on a **B200 at ~$6–7/hour**.

| Scene | Sim-seconds per GPU-second | Effect on cost |
|---|---|---|
| Static warehouse (shelving, pallets), one [Unitree G1](../../entities/unitree-g1.md) | **~100** | baseline, "decently manageable" |
| Same warehouse, **with articulation** | **~50** | **2×** |
| Rubble, or a forest | lower again | |
| **+ lidar and camera, RTX rendering** | **~1** | **experiment cost in the millions** |

Two structural facts sit under that table:

- **The last row changes hardware.** RTX rendering does not run on a B200 — *"B200 doesn't render"* — so the sensor-rich case moves to an **RTX PRO 6000 Blackwell** and is priced on a different GPU as well as a worse ratio.
- **~1:1 is a wall, not a slope.** At one simulated second per GPU-second you have lost the entire advantage of simulation over the real world *except* determinism, resettability and scenarios you cannot stage. Zadeh is pointed about how modest the ask was: *"G1 in a forest plus lidar plus camera — I'm not asking for too much."*

> [!warning] Read the dollar figure as an order of magnitude
> The transcript is machine ASR and gives both **$5M** and **$45M** for the sensor-rich cell within a minute of each other. The claim that survives is *millions of dollars per experiment*, and the target Zadeh sets — *"instead of $5 million, how can I break it down to 500,000?"* — is a **10×**, which is the useful number regardless of the base.

## The three unsolved problems

Zadeh presents these as community problems, explicitly not as things Lambda has solved.

**1. There is no way to tell a good simulation from a bad one.** Learning signal is high early and decays; *"the goal becomes how do I hunt down those fresh gradients that are hidden among increasingly [many] gradients that are no longer helpful."* And the metric is **task-dependent** — *"a robot that stands on its legs is going to be different than a robot that has propellers and flies"* — so there is no universal simulation-quality score to optimize a generation budget against. A backward pass producing "decent gradients" is not evidence: *"is that a good measure, or do we have other measures?"*

**2. Data logistics may bind before compute does.** Simulation output has to be **streamed** into training (not staged), and — the part usually forgotten — **indexed afterwards**, so that a *new* learning criterion can be applied to *existing* runs:

> *"I'm going to want to have an index where I can go on my database and say, give me all the instances where there's a cat crossing the street. You're not going to want to regenerate simulations… these have cost you a lot of money to generate."*

That is a specific, testable design requirement, and it is a **content-addressable query over simulated experience** — closer to a retrieval problem than a storage one. Nothing else in this wiki states it.

**3. Heterogeneous clusters have no playbook.** Render GPUs feed training GPUs, and *"there's no orchestration that is globally applicable"* — no general answer to which side throttles, how many GPUs per node, or how to configure the interconnect between two GPU types doing different jobs. Weight-update frequency becomes a network-bandwidth question rather than an optimization one.

## Why this belongs next to the flywheel argument

The wiki's [synthetic flywheel](../learning/synthetic-data-flywheel.md) page carries the strongest form of the pro-synthetic case — [Aleksandra Faust](../../entities/aleksandra-faust.md)'s Day 2 thesis that a synthetic environment should be a **superset of reality, not a replica**, evidenced across four domains. This page is the bill.

They are not in conflict; they are the two halves of one decision. Faust's argument says *what to simulate*; Zadeh's says *what you can afford to*. And the two together produce a specific research question he poses and does not answer:

> *"A G1 in a forest plus lidar and camera is going to give you really good learning signals. But remember, for one of those you could generate 100 more simple simulations. So do you want to come up with some sort of curriculum to make this better?"*

**A curriculum over simulation cost** — cheap scenes for coverage, expensive scenes for the gradients that only they provide — is the obvious construction and, as far as this wiki records, an unbuilt one. Compare the noise curriculum [Balestriero described the same morning](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) (cheap synthetic clean data restoring convergence rates on noisy data), which is the same shape of idea applied to a different axis.

> [!note] The cheap corner of the space is the one that has results
> [Sim2Reason](../../entities/sim2reason.md), from the same speaker, works because it **never renders anything** — it keeps forces, velocities and accelerations and throws the pixels away, then turns the traces into text. That is the sub-$100-per-experiment corner of this table, and it produced measurable gains on physics *and* mathematics benchmarks. The expensive corner is the one robotics needs, and the one nobody has priced down.

## Related concepts

- [The synthetic flywheel](../learning/synthetic-data-flywheel.md) — the thesis this prices.
- [Sim-to-real transfer](../learning/sim-to-real-transfer.md) — what the expensive rows are being bought for.
- [World-model simulators](world-model-simulators.md) — the alternative to paying this bill: learn the simulator instead of running one.
- [World-model evaluation](world-model-evaluation.md) — problem 1 above is the evaluation problem, one level upstream: judging the *data* rather than the model.
- [Actuator fidelity and sim2real](../learning/actuator-fidelity-sim2real.md) — where fidelity is worth paying for and where it is not.

## Mentioned in

- [Third World Modeling Workshop — Day 3](../../sources/chicago-booth-world-modeling-workshop-2026-day3.md) — **the sole source**; Amir Zadeh (Lambda), *Scaling GPU Infrastructure*.

> [!note] One source, one vendor, no independent check
> Every number on this page comes from a single talk by a GPU-cloud vendor with a disclosed interest in simulation being expensive-but-worth-it (he was asked about that directly; see [Lambda](../../entities/lambda.md)). The ratios are plausible and the qualitative claim — **sensors and rendering cost ~two orders of magnitude** — matches what anyone who has run Isaac Sim with cameras on would expect. But it is one measurement, on one hardware generation, with no ablation published. Treat the table as a shape, not as constants.
