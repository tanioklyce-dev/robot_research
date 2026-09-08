---
title: Test-time adaptation
type: concept
created: 2026-08-26
updated: 2026-09-07
sources: 9
tags: [test-time-adaptation, test-time-training, distribution-shift, world-model, mpc, planning, robustness, self-supervised]
---

**Test-time adaptation (TTA)** — updating a pretrained model *during deployment*, using a self-supervised signal available from the deployment stream itself, with no labels and no expert demonstrations. Distinct from fine-tuning (offline, labeled, before deployment) and from in-context adaptation (no weight change).

The wiki's entry point is [AdaJEPA](../../entities/adajepa.md), which applies it to a **latent world model inside the MPC loop** — and that closed-loop framing is what makes TTA interesting for robotics rather than a generic robustness trick.


## The extreme-low-data end: 1–10 gradient steps

[GEN-1.5](../../sources/generalist-gen-1-5-blog.md) ([Generalist AI](../../entities/generalist-ai.md), 2026) invokes test-time training explicitly for a regime below the one this page usually covers: *"Test-time training commonly uses tens of gradient steps; GEN-1.5 learns a new physical task in **1–10 steps on 5 minutes of data**."* One step on one minute of data reportedly gives **66.5%** on a held-out task; ten steps on five minutes gives **83% ± 9%**.

The number worth keeping is the one about *where the change lands*: **ten steps move the weights on held-out tasks by less than 0.15%**, which they read as *"fine-tuning slightly reconfigures knowledge already present rather than building new representations."* Adaptation as **retrieval rather than learning** — *"closer to reminding the model of something it nearly knows."*

> [!note] And a trade-off this page has no other instance of
> Generalist report that **improvisation strengthens as the number of adaptation steps decreases** — *"lightly adapted models stay closer to their pretrained priors and can draw on a broader repertoire of behaviors when the situation departs from the demonstrations."* If that holds, adaptation is not free even at 10 steps: it buys task competence by narrowing the behavioral repertoire, and the right amount of test-time training is **as little as the task tolerates**, not as much as fits.
>
> Vendor blog, no ablation, no counts. Recorded as a hypothesis with a mechanism.

## Why control is the natural home for it

In classification, TTA has to invent a proxy objective — entropy minimization, an auxiliary task — because no ground truth arrives at test time. **In closed-loop control, the ground truth arrives for free and immediately.** The agent predicts what will happen, acts, and observes what actually happened. That transition is exactly the training signal the world model was pretrained on:

> "Each execution leads to the next observation, which serves as a self-supervised prediction target for adaptation." ([AdaJEPA](../../sources/adajepa-paper.md))

So a world model in a control loop is in the unusual position of generating labeled training data about its own errors, continuously, at no cost. **One gradient step per replanning step** is reported as sufficient.

## What it fixes, and what it cannot

From [AdaJEPA](../../sources/adajepa-paper.md)'s shift taxonomy — the most useful part of the result, because the failures are as informative as the successes:

| Shift type | Adaptation helps? | Why |
|---|---|---|
| **Unseen object shape** | **Strongly** — "nearly doubles" planning success | Dynamics of the new shape are observable from the transitions being generated |
| **In-distribution** | Yes where the frozen model is suboptimal (>20%); **no harm** where it is already near-optimal | Adaptation specializes a broadly-trained model to the current instance |
| **Blur / noise / lighting** | Clearly | The task-relevant signal survives the corruption; the model just needs recalibrating to it |
| **Recoloring the block or the anchor** | **Only modestly** | The model used color to tell the fixed anchor from the manipulated object — **the identity signal itself is destroyed**, and no amount of transition data restores information that is no longer in the observation |
| **Dynamics change** | Some, on top of an already-strong frozen baseline | Attributed to *in-context* adaptation over the history window — the model was partly handling this without weight updates |

> [!note] The generalizable rule
> **Test-time adaptation repairs a model whose predictions are miscalibrated; it cannot repair observations that no longer carry the needed information.** Recoloring the anchor is not a harder version of blur — it is a different failure, and the fix is offline (augmentation, invariance regularization), not online. Any claim that TTA "handles distribution shift" should be read against which of these two it is facing.

## Relation to the wiki's other uses of prediction error

[Runtime failure detection](../robotics/runtime-failure-detection.md) consumes the same quantity — the mismatch between predicted and observed — but **as an alarm**: [Sentinel](../../sources/sentinel-paper.md) and [FAIL-Detect](../../sources/fail-detect-paper.md) train on successful data only and flag deviation so a rollout can be stopped. TTA consumes it **as a gradient**. The same signal is either evidence that the policy is failing or evidence that the model needs correcting, and nothing in the signal distinguishes those two readings.

That matters, because the wiki already records the failure mode this creates in the detection direction: embedding-similarity OOD detectors score **TNR = 0.00** — they flag every unfamiliar rollout including the ones where the policy generalizes and succeeds. A TTA system makes the opposite error available: it will happily adapt toward a transition that was anomalous because the *policy* did something wrong, not because the *model* was wrong.

## The circularity it introduces

> [!warning] An adapted world model cannot evaluate the episode it adapted to
> The wiki's [train-and-judge](sim-to-real-transfer.md#the-learned-simulator-failure-mode-teaching-to-a-flawed-test) warning — using one learned model to both train and score a system means "the score would reflect an error in the model, not readiness" — acquires a sharper form under TTA. A world model fitted online to the current trajectory has been fitted to the very rollout under test. AdaJEPA measures planning success in the real environment, so its own results are clean; but an adaptive world model used as a [policy-evaluation harness](../robotics/robot-policy-evaluation.md) would be uninterpretable.

## Open questions

- ~~**Cost.** No source here reports the latency or compute of a gradient step inside a replanning step.~~ **Answered 2026-09-02** — presenting AdaJEPA at the [Chicago Booth workshop](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md), Ying Wang gives **~0.3 s added per replanning step**, *"very small compared to the planning time."* Latent world models' appeal is partly [48× faster planning](../../entities/leworldmodel.md), and 0.3 s does not obviously spend that — but the figure comes from a talk, covers only the 2D simulation settings, and has no real-robot counterpart.
- **Stability.** [AdaJEPA](../../entities/adajepa.md) uses stop-gradient as an anti-collapse stabilizer during online updates and reports no case where adaptation hurts — but a single-sample online objective on a JEPA is exactly the regime where collapse is plausible, and no adversarial case is shown.
- **No real-robot instance in this wiki.** Both environments are 2D simulation.

## Related concepts

- [JEPA](../world-models/jepa.md) — the architecture; its self-supervised loss is what makes online adaptation free.
- [Identifiability](../world-models/identifiability.md) — the gap between proved recovery and practical robustness that TTA attacks empirically.
- [Sim-to-real transfer](sim-to-real-transfer.md) — the offline family of answers to the same problem.
- [Runtime failure detection](../robotics/runtime-failure-detection.md) — the same signal used as an alarm.
- [Robot policy evaluation](../robotics/robot-policy-evaluation.md) — what adaptation breaks if the model is also the judge.

## Mentioned in

- [GEN-1.5](../../sources/generalist-gen-1-5-blog.md) — test-time training at 1–10 steps; the <0.15% weight-change number; adaptation-vs-improvisation trade-off.

- [AdaJEPA paper](../../sources/adajepa-paper.md)
- [stable-worldmodel paper](../../sources/stable-worldmodel-paper.md) — the collapse TTA is responding to.
- [Third World Modeling Workshop — Day 2](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md) — AdaJEPA presented; the ~0.3 s/step latency figure.
- [Embodied AI — AI House Davos 2026 (LeCun)](../../sources/ai-house-davos-2026-lecun-embodied-ai.md) — the cerebellum argument: adaptation in milliseconds from prediction error alone, *"not reinforcement learning, absolutely not."*
- [Entropy-SGD (2017)](../../sources/chaudhari2017-entropy-sgd.md) — a Gibbs distribution with a *moving prior* centred on the current iterate; noted on the source page as structurally akin to online adaptation, not developed.
