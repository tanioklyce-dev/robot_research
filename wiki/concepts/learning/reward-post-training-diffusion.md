---
title: Reward post-training of diffusion and flow models
type: concept
created: 2026-08-28
updated: 2026-08-28
sources: 1
tags: [rl-post-training, diffusion, rectified-flow, flow-matching, reward-model, credit-assignment, reward-hacking, alignment, vla]
---

**Reward post-training** of a diffusion or flow model is the problem of improving a multi-step generative policy against a scalar reward observed **only at the endpoint**. It is a credit-assignment problem with an unusual shape: the sample is produced by a sequence of interdependent denoising predictions, but reward exists only after the final state is decoded, so *nothing in the reward says how any individual intermediate prediction should change*.

> [!note] Sourced from image generation; the robotics case is prospective
> The one ingested instance ([DiffusionOPSD](../../entities/diffusionopsd.md)) is an image-generation paper. This page is filed because the wiki's dominant action-head family — [flow matching](flow-matching.md) in [π0](../../entities/pi-zero.md), [SmolVLA](../../entities/smolvla.md), [GR00T N1](../../sources/groot-n1-paper.md) — is the same mathematical object, and because RL-finetuning those heads from task reward is the same problem. No robot result is claimed by anything here.

## Why it is not ordinary RL

A diffusion policy's "episode" is a denoising trajectory of 4–50 steps whose intermediate states are **not** environment states — they are latents on a noise schedule. Three consequences:

- **The action space is the prediction itself.** There is no environment transition to credit; the same network is queried repeatedly at different noise levels, so fitting a target at one query moves predictions at many others.
- **Reward is a function of the decoded endpoint**, which for images is a learned preference model and for robots is a task outcome.
- **Likelihood is awkward.** Reverse-process likelihood ratios are approximate and sensitive to sampler and discretization, which is where the policy-gradient family spends its variance budget.

## The four reward-to-target paradigms

The useful taxonomy, from [DiffusionOPSD](../../sources/diffusionopsd-paper.md) Fig. 3. What separates these methods is **where reward information enters and what it is converted into**:

| Paradigm | How reward becomes an update | Named weakness |
|---|---|---|
| **Trajectory credit** — FlowGRPO, DanceGRPO | group-relative advantages over sampled trajectories via reverse-process likelihood ratios | sensitive to sample budget, likelihood estimation, discretization, rollout choice; no explicit local target |
| **Direct reward backprop** — ReFL, DRaFT, AlignProp | differentiate a reward through one late-state clean-output prediction | couples reward evaluation to optimization; the suffix is never executed and the endpoint never decoded during training |
| **Endpoint supervision** — DiffusionNFT | reweight rollout endpoints under a supervised diffusion objective | efficient, but the target is *an endpoint*, not a statement about how the current prediction should improve |
| **On-policy self-distillation** — DiffusionOPSD | build an explicit bounded local target from reward gradients, fit it detached, rebuild it as the policy moves | needs a **differentiable** reward on the decoded output |

The last column is the design axis: the first three leave the desired intermediate change **implicit** — in advantage weights, in parameter gradients, or in an endpoint — while the fourth makes it an object you can inspect.

## Construction is not realization

The most transferable idea here, and it survives independent of any method winning. Split the reward change at a query into two stages:

```
G_realized = G_construct − G_fit
```

where `G_construct` is the reward gain of the *target you built* and `G_fit` is a **signed** gap covering under-realization, rotation, or overshoot by the actual parameter update.

The empirical finding is that **the two do not track each other**. In controlled same-query experiments, a target with a *larger* construction gain produced a *smaller* realized gain after one update — with the ordering reversing on **62.3%** of prompts for one reward and **29.5%** for another ([DiffusionOPSD](../../sources/diffusionopsd-paper.md)). The reversal is reward-dependent and persists with cross-query interference excluded.

Two practical consequences:

- **A single-update probe can rank methods backwards.** ReFL achieved the largest isolated one-step gain and still lost the training run.
- **"Better reward signal" and "better optimizer step" are separable failure modes**, and diagnosing which one broke requires instrumenting them apart. Most post-training work reports only the end-to-end curve.

## Step distillation breaks endpoint supervision

The result with the clearest robotics implication. On a **9-step distilled** backbone, endpoint-supervision post-training (DiffusionNFT) drove the model *below its own unadapted starting point on 8 of 10 objectives*. The stated mechanism: distillation compresses the trajectory into native transitions that **need not correspond one-to-one with teacher trajectories**, so an endpoint-conditioned target is mismatched to the states the distilled policy actually visits.

This matters here because **the wiki's action heads are already few-step** — [GR00T N1](../../sources/groot-n1-paper.md) runs **K=4** Euler steps at inference, and the whole [flow-matching](flow-matching.md) case for VLAs rests on needing few integration steps. If endpoint supervision degrades with step count, the cheap post-training methods degrade exactly where robot policies live. **Untested on any robot.**

## Reward hacking is the standing hazard

Post-training against a learned reward model optimizes the model, not the thing it stands for. The ingested source shows it plainly without naming it: an Aesthetic-specialist checkpoint scores **12.08** where every reference model sits at **5.1–5.7**, while the *same method's* generalist checkpoint scores **6.03**. The gap between those two numbers is the size of the over-optimization.

The methodological rule this suggests: **a reward-specific checkpoint evaluated on its own training reward is not a held-out measurement**, even on held-out prompts. Held-out *prompts* and held-out *evaluators* are different controls, and only the second speaks to whether quality improved. Compare the wiki's [world-model evaluation](../world-models/world-model-evaluation.md) coverage of the same trap and [AI safety and alignment](../safety/ai-safety-alignment.md) on Goodharting generally.

## What would make this a robotics topic

The blocker is specific. Self-distillation needs `∇_y R(D(y), c)` — a differentiable reward on the decoded output. Image preference models are differentiable by construction. Robot task rewards are typically **sparse, environment-evaluated and non-differentiable**, so the reward-gradient step (which ablations show *is* the method) has no direct analogue. Candidate bridges, none demonstrated: a learned differentiable critic, a VLM preference model over rendered rollouts, or restricting to differentiable proxy objectives.

The parts that port without modification are the **diagnosis** (endpoint reward under-specifies intermediate change), the **decomposition** (construction vs realization), and the **clean-output identity** — given a noised action chunk and the action expert's velocity output, `A₀ = A_τ − τ·v_θ` recovers the predicted clean chunk, which is what a target would be built around.

## Related concepts

- [Flow matching](flow-matching.md) — the substrate for both the image models here and the wiki's VLA action heads
- [Diffusion Policy](../../entities/diffusion-policy.md) — the robot-side object with the same structure
- [Real-world robot RL](real-world-robot-rl.md) — where robot-side reward post-training currently lives (RLPD/HIL-SERL lineage, not diffusion-native)
- [AI safety and alignment](../safety/ai-safety-alignment.md) — reward-model over-optimization

## Current state

**One ingested source, image-only, not peer-reviewed, no replication.** The taxonomy and the construction/realization decomposition are worth keeping regardless of whether DiffusionOPSD holds up; the numbers are about images and should not be quoted as evidence about robots. The open question the wiki should track: **has anyone RL-post-trained a flow-matching VLA action head against a task reward at all?** Nothing ingested so far does.

## Mentioned in

- [On-Policy Self-Distillation in Diffusion Models](../../sources/diffusionopsd-paper.md) — the paradigm table, the reversal experiments, and the step-distillation collapse.
