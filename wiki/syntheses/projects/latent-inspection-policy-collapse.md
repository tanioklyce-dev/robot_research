---
title: "Proposed experiment — does latent-space inspection predict policy collapse before you run the perturbed benchmark?"
type: synthesis
created: 2026-08-30
updated: 2026-08-30
tags: [experiment-design, robot-policy-evaluation, libero-pro, interpretability, neural-geometry, latent-space, generalization, project-scoping]
status: proposal
---

> [!note] What this is
> A concrete, runnable experimental design for the question left open on [mechanistic interpretability](../../concepts/safety/mechanistic-interpretability.md), [neural geometry](../../concepts/safety/neural-geometry.md) and the [Goodfire Silico page](../../sources/goodfire-silico-robotics-vision.md). Nothing here has been run. It is scoped for a single workstation with one GPU and entirely open checkpoints.

## The question

**Can you predict which robot policies will collapse under perturbation by inspecting their latent representations — without running the perturbed benchmark?**

## Why it is worth answering

[LIBERO-PRO](../../sources/libero-pro-paper.md) established the problem: policies scoring **>90%** on LIBERO drop to **0.0%** under perturbation. Benchmark success does not distinguish generalization from memorization. The wiki's [VLA success-rate audit](../platforms/vla-success-rate-audit.md) sharpens it — ten models within **1.2 percentage points** on LIBERO, a tier that a perturbation axis would presumably shred, in unknown order.

Today the only way to know is to **build a perturbed benchmark for every task and rerun everything**. That is expensive, it does not transfer to a new task or a new robot, and it tells you nothing until after the policy is trained.

[Goodfire](../../entities/goodfire.md) markets exactly this capability — *"catch generalization failure before deployment"* by evaluating the latent space — with [no published evidence](../../sources/goodfire-silico-robotics-vision.md). Either it works, which changes evaluation practice, or it does not, which is worth knowing about a shipping product.

**A negative result is publishable and useful.** That is unusual enough to be part of the case for running it.

## The design

### Ground truth (`y`)

For each policy `p` and task suite: `collapse(p) = success_standard(p) − success_perturbed(p)`, from LIBERO and [LIBERO-PRO](../../sources/libero-pro-paper.md). Report the ratio as a secondary measure; the difference is better behaved when standard success is near-ceiling, which it is for this tier.

### Candidate predictors (`x`) — computed without the perturbed benchmark

Five, ordered from cheapest to most informative. All operate on the policy's **visual/observation encoder output** over a held-out set of standard-condition rollouts.

1. **Effective dimensionality** — participation ratio or intrinsic-dimension estimate of the latent across the task distribution. *Hypothesis: memorizing policies compress to fewer effective dimensions, one cluster per demonstration.*
2. **Episode-identity probe** — train a linear classifier to predict *which demonstration* a latent came from. *This is the sharpest memorization signature available: if episode identity is linearly decodable from a mid-policy representation, the policy has learned to index demonstrations rather than to perceive state.*
3. **Task-variable recoverability** — linear probe for ground-truth physical quantities the simulator provides free: object pose, gripper–object distance, gripper aperture. *A policy that does not linearly encode the object's position is not solving the task by seeing the object.*
4. **Manifold vs cluster structure** — for a continuous task variable (object x-position), is the latent a **smooth 1-D manifold** or **discrete per-demonstration clusters**? Method from [Engels et al.](../../sources/engels2024-not-all-features-one-dimensionally-linear.md) and [neural geometry](../../concepts/safety/neural-geometry.md). *A policy whose latent fragments a continuous variable has, by construction, no interpolation capacity between the fragments.*
5. **Latent nuisance-to-signal ratio (NSR)** — the proposed primary metric. Apply a **task-irrelevant** perturbation to the observation and measure how far the latent moves; divide by how far it moves under a **task-relevant** change of the same magnitude.

```
NSR(p) = E[ d(z(o), z(o + Δ_nuisance)) ] / E[ d(z(o), z(o + Δ_task)) ]
```

`d` = cosine or normalized L2. Cost is **one forward pass per observation** — no rollouts, no scoring, no simulator stepping beyond what you already recorded. **Prediction: high NSR → collapse.**

### The trap, and how to avoid it

> [!warning] The design's central failure mode
> If `Δ_nuisance` is drawn from the same perturbation families LIBERO-PRO applies, **you have not predicted the benchmark — you have run a cheap version of it.** The result would be trivially positive and worthless.
>
> Two escapes, and a serious version of this experiment uses both:
>
> **(a) Held-out perturbation families.** Fit the latent metric using family A (e.g. lighting, texture); evaluate collapse prediction on family B (e.g. object-position and distractor perturbations). Cross-family transfer is the actual claim.
>
> **(b) Perturbation-free predictors.** Metrics 1–4 use **no perturbation at all**. If an intrinsic metric — especially the **episode-identity probe** — predicts collapse, that is a much stronger and more useful result than anything NSR can give, because it needs no perturbation design for a new task.

### Controls that must be beaten

A predictor is only interesting if it beats what you already have for free:

- **Standard benchmark success** — LIBERO-PRO's whole finding is that this does *not* predict collapse, so it should be a weak baseline. Confirming that is a sanity check on the setup.
- **Model size**, **pretraining data volume**, **validation loss / action MSE on held-out demos**.
- **Training-set size per task.**

If NSR does not beat validation loss, there is no result.

### Statistical design — the part that decides feasibility

Cross-sectional power is the problem: there are maybe **8–12** open checkpoints (OpenVLA, OpenVLA-OFT, [π0](../../entities/pi-zero.md), GR00T N1.x, [TurboVLA](../../entities/turbovla.md), [VQ-BeT](../../entities/vq-bet.md), [Diffusion Policy](../../entities/diffusion-policy.md), [ACT](../../entities/act.md)). Ten points is not enough to fit anything.

**The fix, and the best idea in this design: go longitudinal.** Train **one** policy, checkpoint **frequently**, and track the latent metric and the collapse metric together across training.

- Turns ~10 cross-sectional points into ~50–100 points on a controlled axis.
- Directly tests the interesting mechanism: **does memorization form gradually, and is it visible in the representation before it is visible in the perturbed score?**
- Removes architecture as a confound entirely.
- The predictive claim becomes sharp and falsifiable: *at checkpoint `t`, does the latent metric forecast the collapse score at checkpoint `t`?*

Then use the 8–12 open checkpoints as a **smaller cross-architecture validation set**, not as the primary evidence.

### Cost

| Item | Estimate |
|---|---|
| Ground truth: LIBERO + LIBERO-PRO on ~10 checkpoints | the dominant cost; simulator rollouts, days of GPU |
| Ground truth: perturbed eval on ~50 training checkpoints of one policy | larger, but parallelizable and the same code |
| Latent metrics 1–5 | **hours** — forward passes plus linear probes |
| Training one policy with dense checkpointing | one standard LIBERO training run |

Everything is open: LIBERO, LIBERO-PRO, LeRobot, and the checkpoints. **No robot hardware.** The asymmetry is the point — the ground truth is expensive and the proposed predictor is nearly free, which is exactly why a positive result would matter.

## A cheaper pilot, with no robot at all

If the full design is too much, [EchoJEPA-L](../../entities/echojepa.md) is an **open JEPA checkpoint with a published, physics-informed, severity-swept perturbation benchmark already attached** ([paper](../../sources/echojepa-paper.md)). Its baselines (VideoMAE, EchoFM, PanEcho, EchoPrime) span a **2.3% → 16.8%** degradation range — a genuine spread in perturbation robustness across models on a shared benchmark, which is precisely the `y` axis LIBERO-PRO gives for only two points.

Run metrics 1–5 across those models and ask whether they rank the degradation. **Same question, same method, existing ground truth, no simulator.** If the latent metrics cannot rank a five-model spread with published robustness numbers, they will not rank robot policies either — and that is a one-week negative result rather than a two-month one.

## Design lessons borrowed from EchoJEPA

Their [robustness protocol](../../sources/echojepa-paper.md) §3.5 is better built than anything in the robot-evaluation literature this wiki tracks, and three choices transfer directly:

1. **Derive perturbations from sensor physics**, not a generic corruption library. For manipulation: lighting change, occlusion by the arm itself, specular surfaces, calibration drift, gripper wear — not Gaussian pixel noise.
2. **Sweep severity** to get a degradation *curve*. LIBERO-PRO reports a cliff; a swept axis says where the cliff is, which is what a deployment decision needs.
3. **Apply perturbations consistently across a whole episode**, not per-frame — a real acquisition failure persists.

Their population argument transfers too, and stings: *"patients most likely to benefit from automated analysis… are precisely those whose images deviate most from training distributions."* The manipulation tasks worth automating are the awkward ones nobody collected fifty clean demonstrations of.

## What each outcome would mean

| Result | Consequence |
|---|---|
| **Intrinsic metric (esp. episode-identity probe) predicts collapse** | The strongest outcome. A cheap, task-general memorization detector; changes how policies are evaluated and validates [Goodfire's](../../entities/goodfire.md) "Validate" claim from outside. |
| **Only NSR predicts, and only within perturbation family** | Weak. You have built a cheap proxy benchmark, useful operationally, not a generalization insight. |
| **Nothing predicts collapse** | Genuinely informative: latent inspection does not substitute for perturbed evaluation, and a shipping product's central robotics claim is unsupported. Publishable. |
| **Latent metric predicts collapse *earlier in training* than the perturbed score does** | The most interesting possible result — memorization is visible in the representation before it is visible in behaviour, which would make it an early-stopping signal, not just a diagnostic. |

## Related

- [LIBERO-PRO](../../sources/libero-pro-paper.md) · [VLA success-rate audit](../platforms/vla-success-rate-audit.md) · [robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md)
- [Neural geometry](../../concepts/safety/neural-geometry.md) · [Engels et al.](../../sources/engels2024-not-all-features-one-dimensionally-linear.md) · [mechanistic interpretability](../../concepts/safety/mechanistic-interpretability.md)
- [Goodfire](../../entities/goodfire.md) · [Silico for Robotics & Vision](../../sources/goodfire-silico-robotics-vision.md)
- [EchoJEPA](../../entities/echojepa.md) · [its paper](../../sources/echojepa-paper.md) — the pilot testbed
- [Latent space](../../concepts/world-models/latent-space.md) · [inductive bias](../../concepts/learning/inductive-bias.md)

## Open questions in the design itself

- **Which layer?** Metrics are specified on "the observation encoder output," but a [VLA](../../concepts/learning/vla-models.md) has several plausible taps — frozen vision backbone, post-fusion trunk, pre-action-head. The answer probably differs across them and that is itself a finding. Sweep it.
- **Frozen pretrained backbones confound the episode-identity probe.** If the vision encoder is a frozen [DINOv2](../../entities/dinov2.md), it cannot have memorized *these* demonstrations, so the probe must be run on representations downstream of fine-tuning.
- **`Δ_task` is hard to define.** "A task-relevant change of the same magnitude" needs an operational definition; simulator ground-truth state gives one, but the normalization is a judgement call and should be reported as a sensitivity analysis.
- **Success is binary and sparse**, so collapse scores are noisy at 50 episodes/task. The [LIBERO protocol](../../entities/libero.md) is 50 episodes per task, 500 per suite — probably adequate aggregated, marginal per task.
