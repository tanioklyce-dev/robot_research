---
title: Curriculum Module 14 — Capstone (paper-first, hardware-second)
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-14, capstone, lewm, pusht, stretch, experiment-design, hello-world]
prereqs: [curriculum-12, curriculum-13]
status: draft
---

> [!note] Curriculum context
> This is **Module 14** of the [Robot-learning curriculum](robot-learning-curriculum.md) — the **capstone**. Prerequisites: [Module 12](curriculum-12-lewm-deep-dive.md) (LeWM deep-dive — you need to actually understand SIGReg + the architecture + planning) and [Module 13](curriculum-13-home-robotics-deployment.md) (deployment reality — you need to know where the experiment fits and what it would teach).
>
> The capstone has two phases. **Phase A (paper / sim — required)** is fully completable on a single GPU; everything you need is already in the wiki. **Phase B (real Stretch — gated)** is the hardware execution; the curriculum is "completable" on phase A alone.
>
> The capstone *is* the anchor exercise. There's no separate "anchor exercise" section here — the entire module is the exercise.

## What the capstone is

You've read 13 modules of the curriculum. You can read the LeWM paper. You can write the SIGReg derivation on paper. You can sketch the data flow for a VLA, a BC method, and a WM-MPC system on the same task. The only step left is **train the thing**.

The capstone is a real-but-bounded research project structured to take a careful reader from "I understand LeWM on paper" to "I trained LeWM, observed where it works, observed where it breaks, and wrote down what I learned." Then, gated on hardware availability, "I tried it on a real robot."

By the end of the capstone you should have produced:

- **(Phase A, required)** A working PushT-LeWM training run on a single GPU, with success rate within a few points of the paper.
- **(Phase A, required)** A 5–10 page **experiment-design memo** for the smallest credible LeWM-on-Stretch or DINO-WM-on-Stretch experiment — the one you defended in [Module 13](curriculum-13-home-robotics-deployment.md)'s anchor exercise.
- **(Phase B, gated on hardware)** That experiment, executed on a real Stretch. With a Diffusion Policy baseline. Compared honestly.

## Phase A — paper / sim (required)

Three sub-deliverables. Each leans on an existing wiki artifact.

### A.1 — Reproduce LeWM PushT from scratch

The first concrete experiment in the curriculum. The goal is to *train it yourself* and see the LeWM training curves with your own eyes.

**Existing artifact:** [LeWM hello world — Project 1 detailed scope](lewm-hello-world-project-scope.md). Phase-by-phase plan:
- Install [`stable-worldmodel`](../entities/stable-worldmodel.md) per [the howto](leworldmodel-howto.md).
- Download the canonical PushT dataset.
- Train LeWM from scratch on a single GPU. Expect a few hours of training.
- Evaluate planning success rate. Expected ≈90%; target ≈96% per the paper.
- Reproduce by also pulling the `quentinll/lewm-pusht` HF checkpoint and verifying your numbers.

**One-knob ablation** — flip the `λ` SIGReg weight by an order of magnitude in either direction. Watch the training collapse (low `λ`) or the prediction loss fail to converge (high `λ`). Confirm the "λ is the only effective hyperparameter" claim in your own training runs.

**What you'll learn from this exercise that paper-reading didn't give you.**

- How long training actually takes.
- What the training curves *look like* — the sharp early SIGReg drop followed by plateau, with prediction loss falling steadily underneath.
- How SIGReg interacts with the BN-after-CLS engineering trick from [Module 12](curriculum-12-lewm-deep-dive.md): if you accidentally leave the original ViT LayerNorm at the end, SIGReg won't optimize. This is *the* engineering footgun and it's worth landing on once with your own code rather than reading about it.
- How the planner's CEM hyperparameters interact with the predictor's horizon. (Try varying `H` and watch success rate peak then decline — this is the optimal-horizon plot from [Module 10](curriculum-10-world-models.md)'s anchor exercise made concrete.)

### A.2 — SIGReg gradient derivation on paper

Module 12's anchor exercise Part B. Re-do it as a capstone deliverable: derive `∂T/∂h_k → ∂T/∂Z` with the Epps–Pulley test statistic, including the empirical-characteristic-function chain rule. Two pages of math. Verify it matches the LeWM repo implementation in `lucas-maes/le-wm`.

### A.3 — The experiment-design memo

The phase-A capstone deliverable. **5–10 pages.**

**Existing artifacts to lean on:**

- [LeWM-on-Stretch feasibility](lewm-on-stretch-feasibility.md) — the LeWM-side sketch.
- [DINO-WM-on-Stretch experiment plan](dino-wm-on-stretch-experiment.md) — the DINO-WM-side sketch.
- [Module 13](curriculum-13-home-robotics-deployment.md)'s anchor exercise — pick one, defend it.

**The memo should cover:**

1. **The task.** A single Stretch task narrow enough to evaluate quantitatively. Recommended: medication-fetcher subtasks per [Module 13](curriculum-13-home-robotics-deployment.md), or a [RUM](../entities/robot-utility-models.md)-style pick-and-drop on a defined object.
2. **The architecture.** Which world model (LeWM vs DINO-WM), which encoder, which predictor, action conditioning specifics. Cite [Module 11](curriculum-11-jepa-deep.md)'s LeWM-vs-V-JEPA-2 axis-by-axis to position your choice.
3. **The data.** Use [RUM](../entities/robot-utility-models.md)'s open dataset to bootstrap action-conditioning data. Be honest about sample size.
4. **Baselines.** Diffusion Policy on the same data. (You drafted DP's data flow in [Module 9](curriculum-09-vla.md)'s anchor exercise; fold that in.) RUM (BC) as a third comparison if scope allows.
5. **Metrics.** Success rate; latency per control tick; planning failure modes (compounding error in WM rollouts; mode-averaging in BC; etc.); user-relevant metrics (does it complete the task in a reasonable time?).
6. **Risk register.** Where could this go wrong? The Two-Room failure case from [Module 12](curriculum-12-lewm-deep-dive.md) — Stretch's tasks may have low intrinsic dimensionality similar to Two-Room; if so, a Gaussian-prior latent over-regularizes. The 3D failure case from PushT vs OGBench-Cube — Stretch is 3D. Etc.
7. **What you'd learn.** Phrase as "the experiment is designed to answer: question X, with answer being clearly distinguishable success/failure based on metrics Y."
8. **Phase-B gating.** What hardware, time, and budget are required to execute. What's the minimum-viable scope.

The memo *is* the deliverable. Whether you ever execute phase B is a function of hardware access; the memo stands on its own as the curriculum's culminating artifact.

## Phase B — hardware execution (gated on Stretch availability)

If you can borrow, rent, or buy a Stretch, execute your phase-A memo. Honestly. Including the comparison to a Diffusion Policy baseline.

**Hardware logistics.**

- A Stretch RE3 is ~$25K to buy. A few research labs (NYU, UW HCR, Hello Robot) have units that can be shared; ask. Your local university's robotics lab may have one.
- Phase-B execution is **40–80+ hours** of work, often more for first-time hardware setup. The curriculum-effort estimate ([curriculum hub](robot-learning-curriculum.md)) lists this explicitly.

**What "honestly" means.**

- Report the numbers you actually got, not the numbers you wanted.
- If LeWM (or DINO-WM) doesn't beat Diffusion Policy on your task, **say so**. The deployment-reality framing from [Module 13](curriculum-13-home-robotics-deployment.md) — "the strongest 2026 home-robotics results are BC, not WM" — may apply to your experiment too.
- Document failure modes specifically — were rollouts compounding errors past horizon `H`? Was the latent collapsing in some scene configurations? Was Stretch hardware producing data that didn't match the dataset distribution?

The phase-B deliverable: a follow-up memo (or short paper) reporting what happened, including a comparison-to-baseline table and a list of "things that didn't work" — the latter often more valuable than the former for the next researcher.

## Beyond the capstone

If phase B succeeds — *and* it's worth doing if it does — the result is the wiki's first real data point on whether LeWM-class WMs can move home-robotics deployment metrics. That's a meaningful contribution. Two follow-on questions worth flagging:

- **Does SIGReg scale to Stretch hardware data?** Module 12 §5.3 documents the Two-Room failure case — SIGReg over-regularizes when intrinsic task dimensionality is low. Does Stretch real-world data trigger the same failure mode? If yes, that's a real limitation of the technique. If no, that's strong evidence SIGReg is robust.
- **Does WM + planning beat or lose to BC + scaled data?** [Module 13](curriculum-13-home-robotics-deployment.md) flagged this as an open empirical question. Your phase-B result is one data point on it.

## Recommended reading

The capstone *uses* the following — re-read them now:

1. **[Module 12](curriculum-12-lewm-deep-dive.md)** — for the SIGReg derivation, architecture details, and CEM-MPC mechanics you'll re-implement.
2. **[Module 13](curriculum-13-home-robotics-deployment.md)** — for the deployment framing and the choice between LeWM-on-Stretch and DINO-WM-on-Stretch.
3. **[LeWM hello-world scope](lewm-hello-world-project-scope.md)** — phase-by-phase plan for A.1.
4. **[LeWM-on-Stretch feasibility](lewm-on-stretch-feasibility.md)** — hardware-side scoping for A.3 and phase B.
5. **[DINO-WM-on-Stretch experiment plan](dino-wm-on-stretch-experiment.md)** — the alternative phase-B candidate.
6. **[LeWM howto](leworldmodel-howto.md)** — the install / train / eval recipe.
7. **[Robot Utility Models paper](../sources/robot-utility-models-paper.md)** — your baseline comparison and your action-conditioning data source.
8. **[Diffusion Policy paper](../sources/diffusion-policy-paper.md)** — your other baseline.

## What you should now be able to do

- Train LeWM on PushT yourself, hit ≈90% success rate, and explain what failed at each prior attempt.
- Defend a specific Stretch experiment in writing in 5–10 pages.
- (Phase B) Execute that experiment on real hardware, report honest numbers, and identify which deployment-reality barriers from [Module 13](curriculum-13-home-robotics-deployment.md) you actually moved.
- Tell the difference between "interesting research finding" and "noise / setup error" in your own results — and have the discipline to flag the latter when it shows up.

## Closing the curriculum

Module 14 is the end. By here you should be able to:

- Read any 2026+ paper in the LeWM neighborhood (JEPA, world models, latent prediction, end-to-end training, robot policies) and place it in the curriculum's design space.
- Reason quantitatively about which technical innovations matter for which deployment problems.
- Know what you don't know — which research questions remain open, which deployment problems remain unsolved, and which curriculum modules glossed over things you'll still need to chase down for any specific application.
- Have hands-on experience training a LeWM-class model and (gated on hardware) running one on a real robot.

The curriculum's destination was always **deployment-relevant understanding of LeWM-class techniques**. Module 14 is where understanding becomes capability.

## Related curriculum modules

- **All of Modules 1–13.** The capstone integrates everything.
- **[Module 12 — LeWM deep-dive](curriculum-12-lewm-deep-dive.md)** — most directly the source of the architecture you'll be running.
- **[Module 13 — Home robotics deployment](curriculum-13-home-robotics-deployment.md)** — most directly the framing for what the experiment is supposed to teach.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../index.md)

## Open questions / TBD

- **The phase-B result itself.** No published LeWM-on-Stretch or DINO-WM-on-Stretch result exists in the wiki at curriculum-draft time. The capstone is designed to *be* that result.
- **A reusable phase-A training-run notebook.** The [hello-world scope](lewm-hello-world-project-scope.md) is prose; an executable notebook reproducing the PushT result would be a useful capstone artifact for future curriculum readers.
- **A "what went wrong" library.** A community-curated list of failure modes encountered when reproducing LeWM (e.g. forgetting to swap the BN-after-CLS, SIGReg projection counts that conflict with batch sizes, etc.) would compound across capstone-runners over time.
