---
title: Robot policy evaluation
type: concept
created: 2026-07-27
updated: 2026-08-26
sources: 22
tags: [evaluation, benchmark, statistics, clopper-pearson, sparc, robolab, methodology, vla, reproducibility, real-to-sim, r2s2r]
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

## The sixth paradigm: a task-reconstructed simulator as the screening layer

[R2S2R](real-to-sim-to-real.md) ([World Labs / SceniX](../../sources/world-labs-r2s2r.md)) proposes reconstructing each real task as an aligned interactive world and using it to **screen checkpoints before hardware evaluation** — "screen out a significant portion of checkpoints before real-world testing, and reserve costly hardware evaluation for the most promising policies."

Its stated standard is the one this page has been converging on from every other direction:

> "A useful simulation need not match real-world success rates exactly. It must support the same decisions as reality: identify where policies succeed and fail, **rank** which policies are better, and predict whether improvements during training will carry over to hardware."

> [!note] Five paradigms, one conclusion
> [RoboArena](../../sources/roboarena-paper.md) (pairwise preference, r ≈ 0.95 vs ≈ 0.60), the [Veo world simulator](../../sources/veo-robotics-policy-evaluation-paper.md) (r = 0.88, absolute rates low), [WorldArena](../../sources/worldarena-paper.md) (r = 0.986 for [Ctrl-World](../../entities/ctrl-world.md), absolute rates *inflated*), and now R2S2R all land on the same trade: **ranking transfers, magnitude does not.** Three of the four report the correlation; R2S2R does not. The convergence is the finding — asking a surrogate evaluator for a deployment success rate is asking it for the one thing none of them delivers.

**The bar, restated by a practitioner as a wall-clock question.** In the [companion interview](../../sources/a16z-worldlabs-scenix-conversation.md), Yunzhu Li defines evaluation not as a rate but as a discrimination time: *"the key criterion people use in industry is **how long in wall-clock time does it take for you to distinguish between a checkpoint that is 90% from a checkpoint that is 92%.**"* That 2-point discrimination is precisely the **±2 pp band** this page prices at ≈1,030 rollouts. The statistics and the industry requirement were derived independently and landed on the same number — which is the strongest evidence available that the Clopper-Pearson bar is not an academic nicety but the actual thing that gates robot iteration speed.

**The protocol number, and where it sits against this page's bar.** Each checkpoint is evaluated on **2,000 simulated trials** (1,000 ID + 1,000 OOD) versus **100 real trials** (50 ID + 50 OOD), on an ALOHA bimanual cube-handover task.

- The **simulated** side clears the [~1,030-rollout Clopper-Pearson bar](#the-sample-size-problem) comfortably — which is the entire point of moving evaluation into simulation.
- The **real** side does not: at n=50 per cell the 95% band is roughly ±10 pp, so every sim-vs-real comparison in that post is bounded by the precision of its real half.

That asymmetry is structural, not a flaw in this particular study. **Making simulated evaluation cheap does not make the ground truth it is validated against any cheaper** — so surrogate evaluators will keep being validated at small real-world N, and will therefore keep being defensible as rankers and indefensible as measurers. It also explains why R2S2R's ordinal framing is not merely principled: at n=50 per cell it is forced.

R2S2R also attacks **failure mode #1** on this page at its root. Visual domain overlap's standard fix is real2sim via Gaussian splatting at **>1 hour per scene**, which [RoboLab](../../sources/nvidia-robolab-evaluation-blog.md) says prices out large-scale testing; industrializing that pipeline is exactly what R2S2R claims to do. Whether it does is unverifiable from a blog post with no numbers.

## The runtime pole: detecting failure inside a rollout

Everything above measures a policy **across** rollouts, after the fact. [Runtime failure detection](runtime-failure-detection.md) measures it **during** one, and the wiki's two ingested instances ([Sentinel](../../sources/sentinel-paper.md), [FAIL-Detect](../../sources/fail-detect-paper.md)) both train on **successful data only**, because failure modes are not enumerable — one policy on one pick-and-place task produced six qualitatively different failures.

Two of their findings bear directly on this page:

- **State atypicality is not policy failure.** Embedding-similarity OOD detectors score **TNR = 0.00** on out-of-distribution test cases — they flag every unfamiliar rollout, including the ones where the policy *generalizes and succeeds*. Any evaluation that treats "OOD" as a proxy for "will fail" inherits that error.
- **Conformal calibration bounds false alarms, not misses.** Both methods guarantee `FPR ≤ δ` from successful rollouts alone; guaranteeing detection would need failure data. The statistical guarantee available at runtime protects throughput, not people.

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
- [Real-to-sim-to-real](real-to-sim-to-real.md) — the reconstruct-the-task-then-screen-in-it paradigm, and the sample-size asymmetry it makes structural.
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
- [Building Worlds That Train Robots (R2S2R)](../../sources/world-labs-r2s2r.md) — a **sixth** paradigm: a per-task reconstructed simulator as a high-throughput checkpoint-screening layer. Reports its protocol (2,000 sim / 100 real trials per checkpoint) but **no success rates and no correlation coefficient**, so it cannot be placed next to WorldArena's 0.986 or Veo's 0.88.
- [A Functional Taxonomy of World Models](../../sources/world-labs-functional-taxonomy.md) — the same verdict from a vendor selling into the category: robot demos are "confined to heavily constrained laboratory setups, with narrow object sets and short task horizons" and **"none have been validated at the complexity, variability, or duration that real-world deployment demands."**
- [Fei-Fei Li is Solving the Hardest Problem in Robotics (a16z × World Labs)](../../sources/a16z-worldlabs-scenix-conversation.md) — evaluation as a wall-clock discrimination problem (90% vs 92%), and the reliability asymmetry against LLMs: an LLM's output has a human reading it, *"but for robotic models, out of the box, the robot has to work reliably in the real environment."*
- [Patch Policy paper](../../sources/patch-policy-paper.md) — two textbook instances of this page's failure modes in one paper: **LIBERO Goal sits at 0.93–0.98 for every method** (saturation, discriminating nothing), and the real-robot comparison runs **n = 20 per cell** (~±20 pp), where the headline 0.70-vs-0.30 gap survives and the 0.90-vs-0.70 ones do not. No confidence intervals reported. Its simulated protocol is better than most: **100 trajectories per seed × 3 seeds**.
