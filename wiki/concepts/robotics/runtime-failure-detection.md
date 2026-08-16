---
title: Runtime failure detection for generative policies
type: concept
created: 2026-08-16
updated: 2026-08-16
sources: 2
tags: [runtime-monitoring, failure-detection, out-of-distribution, conformal-prediction, diffusion-policy, generative-policies, temporal-consistency, vlm, epistemic-uncertainty, tri, stanford]
---

**Runtime failure detection** — deciding, *while a learned policy is executing*, whether it is going to fail, from the trajectory so far. Not evaluation (which happens after, over many rollouts) and not safety filtering (which prevents physical harm without knowing whether the task is going well). It is the third thing a deployed policy needs, and the one that answers *"is this rollout worth continuing?"*

The wiki has two ingested instances, published five months apart, and **the second one benchmarks against the first and disagrees with it**.

## Why the problem is not just OOD detection

The obvious framing — a policy is failing when its inputs are out of distribution — is wrong in a way both papers demonstrate:

> **State atypicality is not policy failure.** On out-of-distribution test cases, embedding-similarity detectors (CLIP, ResNet, the policy's own encoder) score **TNR = 0.00** in [Sentinel](../../sources/sentinel-paper.md)'s Close Box domain: they flag *every* OOD rollout, including the ones where the policy generalizes and succeeds. A detector whose real claim is "this looks unfamiliar" cannot distinguish generalization from failure — and generalization is the thing you deployed a generalist policy to get.

Two further complications specific to **generative** policies:

- **Multimodality breaks variance-based uncertainty.** In a genuinely multimodal domain both successes and failures produce high-variance action samples, so output variance detects almost nothing (0.26–0.33 TPR on Close Box).
- **Failure is closed-loop and time-correlated**, not a property of one input-output pair. It emerges from compounding errors along a rollout, so per-sample OOD scores miss it by construction.

And the failure *modes* are not enumerable. [FAIL-Detect](../../sources/fail-detect-paper.md) shows six qualitatively distinct failures from **one policy on one pick-and-place task** — slipped early, slipped late, tilted three different ways, never picked up. Any method requiring labelled failure data is fighting a combinatorial problem; **both methods here train on successes only.**

## The two approaches

| | [Sentinel](../../sources/sentinel-paper.md) (Stanford, CoRL 2024) | [FAIL-Detect](../../sources/fail-detect-paper.md) (TRI, RSS 2025) |
|---|---|---|
| Organizing idea | **Taxonomy**: split failures into erratic vs task-progression, one detector each | **Modularity**: any scalar score + a calibrated threshold |
| Signal | **STAC** — statistical distance between temporally overlapping action chunks; plus a **VLM** doing video QA | **`logpZO`** — normalizing-flow density, evaluated in latent noise space |
| Threshold | Constant, from the `1−δ` quantile of successful rollouts | **Time-varying conformal band** `μ_t + h_t` |
| Guarantee | Conformal bound on **false-alarm rate** (`FPR ≤ δ`) | Conformal FPR control at level `α` |
| Needs failure data | No | No |
| Cost | 256 policy samples per timestep | One forward pass |
| Headline | +18% over either detector alone; >97% of unknown failures | ~78% balanced accuracy (sim), ~72% (hardware) |

**The ideas are complementary, and nobody has combined them.** Sentinel's contribution is *what to measure* (a failure taxonomy, and a consistency signal that exploits action-chunk overlap); FAIL-Detect's is *how to threshold* (a time-varying band) and *a better score to threshold*. STAC as a score inside FAIL-Detect's stage-2 band is an experiment neither paper runs.

### STAC, because the mechanism is elegant

A chunked policy queried at `t` predicts actions for `t…t+h−1`; queried again at `t+k`, it predicts `t+k…t+h+k−1`. **The chunks overlap**, so you hold two distributions over the *same* future timesteps, produced from different observations. Their statistical distance (MMD, KL) is a direct measure of the policy changing its mind, it is well-posed under multimodality where comparing two *sampled* trajectories is not, and it needs no additional model. Cumulate over the rollout, threshold, done.

### `logpZO`, because the trick generalizes

Fit a continuous normalizing flow to successful-rollout observations. Rather than scoring likelihood in observation space (which needs the flow's divergence integrated along the ODE — badly behaved in high dimensions), run the **forward** ODE and check whether the resulting encoding looks like the Gaussian noise it should be: the score is just **`‖Z‖²`**. Push the sample through the flow and see if it lands where noise lives.

> [!warning] Contradiction — is a sampling-based score deployable?
> [Sentinel](../../sources/sentinel-paper.md) calls STAC's cost *"negligible."* [FAIL-Detect](../../sources/fail-detect-paper.md) measures **1.45 s per timestep** against 0.033–0.04 s for `logpZO` (**36–44×**), reports STAC's detection time as *"consistently exceed[ing] practical limits, surpassing the average success trajectory time,"* and **omits STAC from its hardware experiments** because it could not run in real time. It also drops Sentinel's VLM for the same reason.
>
> Reconcilable in principle — "negligible" against a diffusion policy's own denoising cost, with batch sampling parallelized on a GPU — but the deployment verdicts differ, and it is the industrial lab saying no. Caveat on the other side: FAIL-Detect reproduces STAC with **PushT hyperparameters** on other tasks and evaluates it without its VLM half, which is not the full system Sentinel proposes.

## What neither does

- **Detection is not recovery.** Both raise a flag and stop. What happens next — human handoff, retry, replan, safe park — is unaddressed, and it is the same [empty execution rail](../../syntheses/agents/guardrails-for-robot-agents.md) this wiki keeps finding on the agent side.
- **Neither predicts.** Sentinel says so explicitly: *"not targeted at predicting failures before they occur, but instead… detecting failures as they occur."* Contrast [predictive red-teaming](robot-policy-evaluation.md), which estimates degradation *before* deployment.
- **No detection guarantee, only a false-alarm guarantee.** Both bound the FPR by conformal prediction. Bounding the *miss* rate would require failure data — the assumption both are built to avoid. The guarantee runs in the direction that protects throughput, not the direction that protects people.
- **Neither runs on a generalist policy.** All experiments are single-task diffusion or flow-matching policies. [LBMs](../learning/large-behavior-models.md) and [VLAs](../learning/vla-models.md) are the obvious targets and are untested — and STAC in particular needs cheap batch sampling, which a large autoregressive VLA does not offer.

## Where it sits

Three distinct mechanisms, three distinct questions, and a deployed system needs all three:

| Layer | Question | Wiki page |
|---|---|---|
| **Safety filter** | Will this action hurt someone or break something? | [Safety filters](safety-filters.md) |
| **Runtime monitor** | Is this rollout going to succeed? | *this page* |
| **Offline evaluation** | Does this policy work, and how confidently do we know? | [Robot policy evaluation](robot-policy-evaluation.md) |

The filter cannot tell that the policy is confidently doing the wrong thing; the monitor cannot stop the arm from swinging through the table; the evaluation cannot say anything about the rollout currently in progress. They are not substitutes and nothing in this wiki's corpus runs more than one of them at once.

## Related concepts

- [Safety filters for learned policies](safety-filters.md) — prevention to this page's detection.
- [Robot policy evaluation](robot-policy-evaluation.md) — the offline counterpart, including the sample-size problem that governs how well any of this can be measured.
- [Imitation learning](../learning/imitation-learning.md) — OOD-state failure is the mechanism.
- [AI guardrails](../safety/ai-guardrails.md) — the semantic-harm analogue, still disjoint.

## Key references

- [Sentinel](../../sources/sentinel-paper.md) — Agia, Sinha, Yang, Cao, Antonova, [Pavone](../../entities/marco-pavone.md), Bohg; CoRL 2024. The taxonomy, STAC, and the VLM monitor.
- [FAIL-Detect](../../sources/fail-detect-paper.md) — Xu et al., **[TRI](../../entities/tri.md)**; RSS 2025. Nine scores compared under one calibration protocol, the `logpZO` flow score, and time-varying conformal bands.

## Mentioned in

- [Sentinel paper](../../sources/sentinel-paper.md)
- [FAIL-Detect paper](../../sources/fail-detect-paper.md)
