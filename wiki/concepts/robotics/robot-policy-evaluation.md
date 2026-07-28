---
title: Robot policy evaluation
type: concept
created: 2026-07-27
updated: 2026-07-27
sources: 2
tags: [evaluation, benchmark, statistics, clopper-pearson, sparc, robolab, methodology, vla, reproducibility]
---

**Robot policy evaluation** — how you establish that one policy is better than another, and how much of the published record actually supports the rankings it reports. The wiki has flagged this as a gap for months (rliable, robomimic, RoboArena all named and unfiled). [NVIDIA SRL's RoboLab work](../../sources/nvidia-robolab-evaluation-blog.md) is the first ingested source that treats it as the subject rather than the plumbing.

## The four failure modes

From the [RoboLab methodology blog](../../sources/nvidia-robolab-evaluation-blog.md):

1. **Visual domain overlap** — train and eval data drawn from the same visual sources, so models memorize rather than generalize. The standard fix (real2sim via Gaussian Splatting) costs **>1 hour per scene**, pricing out large-scale testing.
2. **Saturation** — fixed task suites plateau above **90%** success, at which point the benchmark no longer discriminates. "Almost every model paper reports results on this benchmark."
3. **The diagnostic gap** — binary success/failure says nothing about *why*. Color confusion, instruction phrasing, and camera placement all produce the same `0`.
4. **Statistical untrustworthiness** — see below. This is the one that generalizes furthest.

## The sample-size problem

Using **Clopper-Pearson** exact binomial confidence intervals, achieving a **±2 percentage-point** band on a success rate requires roughly **1,030 rollouts**. Typical published evaluations run about **70** — roughly **15× short**.

> [!warning] This indicts most success rates in this wiki
> The wiki's VLA tables report real-robot success rates at small N and treat differences between them as meaningful: MolmoAct2's real YAM **50.1%** as "+15 over OpenVLA-OFT," GR00T N1.5's G1 **98.8%**, π0-vs-SmolVLA at **78.3 vs 61.7**. At ~70 rollouts a ±2 pp claim is unsupportable, and differences of a few points are inside the noise.
>
> What survives: **large** gaps (a 30-point spread is robust to this critique), and **LIBERO-style simulation** results where trial counts are high and cheap. What does not: fine-grained rankings among close competitors on real hardware, which is exactly the comparison the [VLA deployability landscape](../../syntheses/platforms/vla-deployability-landscape.md) and the wiki's LIBERO table invite readers to make.
>
> This is a limitation of the *published field*, not of the wiki's reading of it — but the wiki has been repeating point estimates without their uncertainty, and should stop treating small gaps as real.

## Metrics beyond binary success

| Metric | What it captures |
|---|---|
| **Graded task score** | Partial credit for subtasks completed within a multi-step instruction — turns a 0 into a diagnostic |
| **SPARC (Spectral Arc-Length)** | Trajectory smoothness from the Fourier spectrum of the velocity profile; imported from human-movement analysis |
| **End-effector velocity** | Execution speed as a human-aligned *preference* signal, not a correctness measure |
| **Failure-event logs** | Frame-level automated detection of wrong-object grasps, drops, gripper collisions |

**Competency tagging** is the structural counterpart: RoboLab splits tasks into **visual** (color, size, semantics), **procedural** (stacking, reorientation, tool affordances), and **relational** (spatial logic, counting, conjunctions) so that a failure localizes to a capability rather than a task.

## Robustness axes that turn out to matter

- **Language complexity** — each task issued as **vague / default / specific**. Finding: *vague instructions consistently lead to failures.* Instruction phrasing is a policy capability, not a prompt-engineering detail, and single-phrasing benchmarks hide it entirely.
- **Scene complexity** — distractors and clutter.
- **Task horizon** — the blunt result: **no policy managed more than four complex subtasks.** Set against the wiki's ~97% LIBERO scores, this is the sharpest available statement that benchmark saturation is hiding a real ceiling.

## Sensitivity analysis without ablation

**Neural Posterior Estimation (NPE)** infers a posterior `p(θ|x)` over environment variables conditioned on observed outcomes, surfacing which conditions correlate with success or failure **without running exhaustive one-variable-at-a-time ablations**. It converts intuitions ("camera placement matters") into quantified associations. This is a simulation-based-inference technique arriving in robot evaluation; the wiki has no other source using it.

## What is still missing

- **No real-world validation.** RoboLab is simulation-only, and whether its scores predict deployment success is precisely the question it exists to answer.
- **The ~1,030-rollout bar is proposed, not met** — including by NVIDIA's own published numbers.
- **rliable / robomimic remain unfiled**, and **[RoboArena](../../entities/nvidia-cosmos.md)** (the real-world leaderboard) has no page. RoboLab is the sim half of a methodology story whose real half is still uncovered here.
- **SPARC's transfer from human-movement analysis to manipulation is unjustified** in the source.

## Related concepts
- [Sim-to-real transfer](../learning/sim-to-real-transfer.md) — RoboLab runs the real-to-sim *evaluation* direction.
- [VLA models](../learning/vla-models.md) — the policies under test and the tables this page qualifies.
- [Control abstraction levels](control-abstraction-levels.md) — an evaluation result is under-specified without its abstraction level; this page adds *and without its confidence interval*.
- [Detection evaluation metrics](detection-evaluation-metrics.md) — the perception-side analogue (mAP/IoU) the wiki already covers.

## Mentioned in
- [How to Evaluate General-Purpose Robot Policies for Real-World Deployment](../../sources/nvidia-robolab-evaluation-blog.md)
- [RoboLab project page](../../sources/nvidia-robolab-project.md)
