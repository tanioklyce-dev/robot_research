---
title: Robot policy evaluation
type: concept
created: 2026-07-27
updated: 2026-08-13
sources: 18
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
>
> **Applied 2026-07-27:** the [success-rate audit](../../syntheses/platforms/vla-success-rate-audit.md) works through every headline comparison in the wiki. Result — the **entire top of the LIBERO table (96.5–98.1) is one statistical tie**, while every conclusion the wiki actually reasons from rests on a gap large enough to survive.

## The second failure mode: memorization

Sample size is not the only way a benchmark can fail to measure what it claims. [LIBERO-PRO](../../sources/libero-pro-paper.md) reports that models scoring **>90% on standard [LIBERO](../../entities/libero.md) collapse to 0.0%** when objects, initial states, instructions, or environments are perturbed — because the **evaluation tasks *are* the training tasks**, differing only by imperceptible initial-state variation. Models keep grasping when the target object is swapped and emit unchanged actions under corrupted instructions: the language and object channels are largely inert.

This sharpens RoboLab's **saturation** critique from *"the benchmark stopped discriminating above 90%"* to *"**above 90% it may be measuring recall.**"* Two independent groups reached the conclusion that the field's most-reported robot-learning benchmark is broken, by different routes and in the same year.

**The two failure modes need different fixes.** Small-N is fixed by more rollouts (or by [pairwise preference](#the-real-world-pole-pairwise-preference), below). Memorization is fixed by **held-out** tasks, objects, phrasings, and scenes — more rollouts on a memorized benchmark just measures the memorization more precisely.

## The real-world pole: pairwise preference

[RoboArena](../../entities/roboarena.md) ([paper](../../sources/roboarena-paper.md), CoRL 2025) takes the opposite route from RoboLab: rather than pinning absolute rates with more rollouts, it **stops estimating absolute rates**. Evaluators at seven institutions freely choose tasks and environments but run **double-blind pairwise A/B comparisons** on a shared [DROID](../../entities/droid.md) platform; an extended **Bradley-Terry** model (per-policy ability θ, per-task difficulty τ, policy×task offset ψ, fit by EM) turns preferences into a ranking.

| | Conventional centralized success-rate eval | RoboArena pairwise |
|---|---|---|
| Pearson r with oracle ranking | **≈ 0.60** | **≈ 0.95** |
| Comparisons to converge | — | **~100** |

**Why it works with so few episodes:** a pairwise preference is a richer unit of evidence than a binary success flag, because both policies face the *identical* scene, so scene difficulty cancels — the standard argument for paired experimental designs. **The cost is magnitude**: you get an ordering, never "72% success," and deployment decisions often need the number. RoboLab and RoboArena are complements, not rivals — *collect far more rollouts* vs *measure something else*.

## Metrics beyond binary success

| Metric | What it captures |
|---|---|
| **Graded task score** | Partial credit for subtasks completed within a multi-step instruction — turns a 0 into a diagnostic |
| **SPARC (Spectral Arc-Length)** | Trajectory smoothness from the Fourier spectrum of the velocity profile; imported from human-movement analysis |
| **End-effector velocity** | Execution speed as a human-aligned *preference* signal, not a correctness measure |
| **Failure-event logs** | Frame-level automated detection of wrong-object grasps, drops, gripper collisions |
| **Safe success** | Fraction of rollouts completing the task **while never violating a safety constraint** ([PACS](../../sources/pacs-paper.md)) |

> [!warning] Safe success is the one in that table that can be zero while task success is 0.79
> [PACS](../../sources/pacs-paper.md) ran diffusion policies and a [SmolVLA](../../entities/smolvla.md) on three human-robot-interaction tasks with **no safety filter**: average task success **0.79**, average **safe** success **0.00**, with constraints violated in **56% of all timesteps** and in *every* rollout. Adding a path-consistent filter moved safe success to **0.80** at unchanged task success.
>
> The implication for the rest of this page is uncomfortable and worth stating plainly: **every success rate in this wiki was measured without a safety constraint being checked**, so none of them distinguishes a policy that does the task from one that does the task while repeatedly entering states that would injure a person standing there. Where humans are in the workspace, task success on its own is not a deployment-relevant number.

**Competency tagging** is the structural counterpart: RoboLab splits tasks into **visual** (color, size, semantics), **procedural** (stacking, reorientation, tool affordances), and **relational** (spatial logic, counting, conjunctions) so that a failure localizes to a capability rather than a task.

## Robustness axes that turn out to matter

- **Language complexity** — each task issued as **vague / default / specific**. Finding: *vague instructions consistently lead to failures.* Instruction phrasing is a policy capability, not a prompt-engineering detail, and single-phrasing benchmarks hide it entirely.
- **Scene complexity** — distractors and clutter.
- **Task horizon** — the blunt result: **no policy managed more than four complex subtasks.** Set against the wiki's ~97% LIBERO scores, this is the sharpest available statement that benchmark saturation is hiding a real ceiling.

## Sensitivity analysis without ablation

**Neural Posterior Estimation (NPE)** infers a posterior `p(θ|x)` over environment variables conditioned on observed outcomes, surfacing which conditions correlate with success or failure **without running exhaustive one-variable-at-a-time ablations**. It converts intuitions ("camera placement matters") into quantified associations. This is a simulation-based-inference technique arriving in robot evaluation; the wiki has no other source using it.

## Two protocols worth knowing by number

The wiki now has confirmed protocols for its two most-cited manipulation benchmarks, which makes their numbers directly comparable in a way most reporting elides:

| Benchmark | Rollouts per model per condition | Base rate | Separating gap |
|---|---:|---:|---|
| [LIBERO](../../entities/libero.md) (4-suite avg) | 2,000 (50/task × 10 tasks × 4) | ~97% | >1.0 pp — and **ten models sit inside 1.2 pp** |
| [RoboTwin 2.0](../../entities/robotwin.md) | **5,000** (100/task × 50 tasks) | ~40% | ~2 pp |

RoboTwin's protocol is confirmed from its [primary source](../../sources/robotwin2-paper.md): 50 clean expert demonstrations per task for training, **100 rollouts per task across all 50 tasks**, Aloha-AgileX, single-task finetuning from released weights. **RoboTwin is the better instrument** — more rollouts *and* a base rate near 50% where the binomial variance is worst but the field's headroom is largest. LIBERO's tie is now wide enough that it discriminates nothing at the top.

> [!warning] Dataset papers routinely report n = 10, and it is not a ranking
> [RoboMIND](../../entities/robomind.md) ([paper](../../sources/robomind-paper.md)) evaluates every model on every task at **ten trials** — *"each model was tested ten times."* At n=10 per cell, a 95% CI spans roughly ±30 points; its reported ACT 55.3% (AgileX) vs 30.7% (Franka) cannot support "AgileX is easier," and its ACT-vs-DP-vs-BAKU ordering cannot support anything.
>
> This is not a criticism of the paper — a dataset paper needs to show the data trains policies at all, and n=10 across 45 tasks does that. It **is** a criticism of citing those tables as comparisons, which is the error to avoid. Read dataset-paper baselines as smoke tests; read benchmark-paper tables as measurements, after checking their n.

## What is still missing

- **No real-world validation.** RoboLab is simulation-only, and whether its scores predict deployment success is precisely the question it exists to answer.
- **The ~1,030-rollout bar is proposed, not met** — including by NVIDIA's own published numbers.
- **rliable / robomimic remain unfiled.** (~~RoboArena has no page~~ — [filed 2026-07-27](../../entities/roboarena.md).) These are the *statistical-reporting* tools (bootstrap CIs, stratified metrics) that would let the wiki report intervals rather than point estimates.
- **No 2026-class model has been run through LIBERO-PRO** — MolmoAct2, OpenVLA-OFT, GR00T N1.7 were not tested. Whether newer models are less memorization-bound is the most consequential open question in this area.
- **SPARC's transfer from human-movement analysis to manipulation is unjustified** in the source.

## Related concepts
- [RoboArena](../../entities/roboarena.md) — the real-world pole.
- [Success-rate audit](../../syntheses/platforms/vla-success-rate-audit.md) — **this page's standard, applied to the wiki's own tables**. Also corrects how the bar is usually quoted: 1,030 rollouts is the requirement at a *90%* success rate; at 50% it is ~2,450.
- [Sim-to-real transfer](../learning/sim-to-real-transfer.md) — RoboLab runs the real-to-sim *evaluation* direction.
- [VLA models](../learning/vla-models.md) — the policies under test and the tables this page qualifies.
- [Control abstraction levels](control-abstraction-levels.md) — an evaluation result is under-specified without its abstraction level; this page adds *and without its confidence interval*.
- [Detection evaluation metrics](detection-evaluation-metrics.md) — the perception-side analogue (mAP/IoU) the wiki already covers.

## Mentioned in
- [RoboArena paper (CoRL 2025)](../../sources/roboarena-paper.md) — the distributed pairwise-preference protocol
- [LIBERO-PRO paper](../../sources/libero-pro-paper.md) — the memorization critique
- [How to Evaluate General-Purpose Robot Policies for Real-World Deployment](../../sources/nvidia-robolab-evaluation-blog.md)
- [RoboLab project page](../../sources/nvidia-robolab-project.md)
- [CaP-X paper](../../sources/cap-x-paper.md) — 100 trials/task across 8 independently controllable tiers; makes the case that a code-as-policy result is uninterpretable without its abstraction tier.
- [ASPIRE paper](../../sources/aspire-paper.md) — **disjoint debug/eval seeds** and one-program-per-task evaluation, a protocol that handicaps the paper's own method relative to its baseline.
- [Evaluating Gemini Robotics Policies in a Veo World Simulator](../../sources/veo-robotics-policy-evaluation-paper.md) — a **third evaluation paradigm**: a video world model as the harness. Pearson 0.88 / MMRV 0.03 against 1600+ real evaluations, but absolute predicted rates run **low**, so it ranks rather than measures — the same trade [RoboArena](../../sources/roboarena-paper.md) makes.
- [Predictive Red Teaming](../../sources/predictive-red-teaming-paper.md) — a fourth: predict degradation per environmental factor without hardware, then use the prediction to target data collection.
- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../../sources/hai-world-model-spatial-intelligence-brief.md) — the same verdict reached from the policy side about *world models* rather than policies: evaluation is "a research patchwork rather than a settled standard," and none of it supports safety-critical deployment decisions. See [world-model evaluation](../world-models/world-model-evaluation.md) and the [scoring synthesis](../../syntheses/society/world-model-policy-vs-wiki-evidence.md).
- [vla-evaluation-harness](../../sources/vla-evaluation-harness-github.md) — Ai2's 18-benchmark, any-VLA evaluation infrastructure (47× throughput; 2,000 LIBERO episodes in ~18 min/H100). Supports LIBERO-Pro with MolmoAct2/GR00T N1.7/π0.5 — the wiki's most consequential open question is no longer blocked on tooling. Its reproduction reports independently verify four LeRobot checkpoints at 96–100% of published LIBERO scores.
- [WorldArena paper](../../sources/worldarena-paper.md) — the **fifth** evaluation paradigm question, turned on the harness itself: when a *world model* is the evaluator, ranking correlates at r = 0.986 (Ctrl-World) or r = 0.483 (Cosmos), and **both inflate absolute success rates** — "partial overfitting to successful trajectories."
