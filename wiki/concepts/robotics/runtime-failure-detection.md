---
title: Runtime failure detection for generative policies
type: concept
created: 2026-08-16
updated: 2026-08-16
sources: 4
tags: [runtime-monitoring, failure-detection, out-of-distribution, conformal-prediction, diffusion-policy, generative-policies, temporal-consistency, vlm, epistemic-uncertainty, tri, stanford]
---

**Runtime failure detection** — deciding, *while a learned policy is executing*, whether it is going to fail, from the trajectory so far. Not evaluation (which happens after, over many rollouts) and not safety filtering (which prevents physical harm without knowing whether the task is going well). It is the third thing a deployed policy needs, and the one that answers *"is this rollout worth continuing?"*

The wiki has **four** ingested instances spanning the full arc — two monitors that detect ([Sentinel](../../sources/sentinel-paper.md), [FAIL-Detect](../../sources/fail-detect-paper.md), where the second benchmarks the first and disagrees with it), one predictor that anticipates ([FIPER](../../sources/fiper-paper.md)), and one that intervenes ([FOREWARN](../../sources/forewarn-paper.md)).

## Why the problem is not just OOD detection

The obvious framing — a policy is failing when its inputs are out of distribution — is wrong in a way both papers demonstrate:

> **State atypicality is not policy failure.** On out-of-distribution test cases, embedding-similarity detectors (CLIP, ResNet, the policy's own encoder) score **TNR = 0.00** in [Sentinel](../../sources/sentinel-paper.md)'s Close Box domain: they flag *every* OOD rollout, including the ones where the policy generalizes and succeeds. A detector whose real claim is "this looks unfamiliar" cannot distinguish generalization from failure — and generalization is the thing you deployed a generalist policy to get.

Two further complications specific to **generative** policies:

- **Multimodality breaks variance-based uncertainty.** In a genuinely multimodal domain both successes and failures produce high-variance action samples, so output variance detects almost nothing (0.26–0.33 TPR on Close Box).
- **Failure is closed-loop and time-correlated**, not a property of one input-output pair. It emerges from compounding errors along a rollout, so per-sample OOD scores miss it by construction.

And the failure *modes* are not enumerable. [FAIL-Detect](../../sources/fail-detect-paper.md) shows six qualitatively distinct failures from **one policy on one pick-and-place task** — slipped early, slipped late, tilted three different ways, never picked up. Any method requiring labelled failure data is fighting a combinatorial problem; **both methods here train on successes only.**

## The two monitors

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
- **Neither *monitor* predicts.** Sentinel says so explicitly: *"not targeted at predicting failures before they occur, but instead… detecting failures as they occur."* Contrast [predictive red-teaming](robot-policy-evaluation.md), which estimates degradation *before deployment*, and [FIPER](../../sources/fiper-paper.md) below, which predicts *within a rollout*.
- **No detection guarantee, only a false-alarm guarantee.** Both bound the FPR by conformal prediction. Bounding the *miss* rate would require failure data — the assumption both are built to avoid. The guarantee runs in the direction that protects throughput, not the direction that protects people.
- **Neither runs on a generalist policy.** All experiments are single-task diffusion or flow-matching policies. [LBMs](../learning/large-behavior-models.md) and [VLAs](../learning/vla-models.md) are the obvious targets and are untested — and STAC in particular needs cheap batch sampling, which a large autoregressive VLA does not offer.

## Prediction, not detection: [FIPER](../../sources/fiper-paper.md)

Monitors *"only raise alarms after errors manifest, providing no foresight."* FIPER (TUM, NeurIPS 2025) predicts, on the insight that a real failure shows **two** signals at once: **consecutive OOD observations** — random network distillation run **inside the policy's own observation embedding space** (RND-OE) — **and** **prolonged high uncertainty in the generated actions** — a novel **action-chunk entropy** (ACE) score. Both conformally calibrated on a few successful rollouts; the alarm needs **both** over a sliding window.

**That AND is the structural inverse of Sentinel's OR.** Sentinel unions complementary detectors to raise recall; FIPER conjoins two indicators to *suppress* alarms on situations the policy can handle. Same underlying observation — OOD ≠ failure — two opposite architectural responses.

- **Entropy, not variance, and the reasoning is the good part**: IL multimodality is *discrete* (pick A, B or C; grasp from the side or above), so a successful policy legitimately emits very different actions for one observation and variance says nothing. What distinguishes trouble is whether the modes are **sharp** — which is entropy. No tractable likelihood for diffusion/flow policies, so ACE samples chunks and bins dimension-wise.
- **A second critique of STAC.** FIPER argues STAC *"typically associates timesteps at which the policy **decides on a behavior mode** with high uncertainty"* — divergence between consecutive chunk distributions spikes when a multimodal policy *commits*, which is healthy. After [FAIL-Detect](../../sources/fail-detect-paper.md)'s speed measurement, this is the second successor paper going after Sentinel's signal.
- **Results**: average **TWA 0.65 / accuracy 0.78 / DT 0.30** across five environments, against `logpZO` 0.69 and STAC 0.68 accuracy. Larger margins on the two real tasks (PushChair **0.96**).
- **And a metric contribution the wiki should keep regardless**: standard metrics do not reward *prediction* — waiting until the last timestep scores high accuracy, flagging everything at t=0 scores a perfect detection time. **Timestep-wise accuracy (TWA)** credits a true positive with `1 − DT`, folding accuracy and earliness into one number.
- **The evaluation protocol is the sharpest formalization of this page's opening claim**: split rollouts into **Success-ID / Success-OOD / Fail-ID / Fail-OOD** and require scores to order `Success ID ≤ Success OOD < Fail ID ≤ Fail OOD`. The **Success-OOD vs Fail-ID gap** *is* the measurement of "can this score tell generalization from failure."

## From detection to intervention: policy steering

Both methods above stop at a flag. [FOREWARN](../../sources/forewarn-paper.md) (CMU) acts, and its premise reframes the problem: most runtime failures are **mode-selection failures, not capability failures** — *"the base policy may already contain the 'right' behavior mode within its distribution… but due to putting too much probability mass on an undesired mode, the robot does not reliably choose the correct action plan at runtime."*

So: sample `K` candidate plans from the policy, predict each outcome with a **latent world model** ([DreamerV3](../../entities/dreamer.md)), have a **VLM narrate those predicted latents in natural language**, and pick the best plan against the task description. Base-policy success **0.30/0.20/0.10 → 0.80/0.70/0.70** on three real Franka tasks.

> [!note] The structural constraint two independent lines arrived at: intervene by *choosing*, not by *correcting*
> [PACS](../../sources/pacs-paper.md) showed that editing a policy's action pushes it off the demonstration manifold and destroys task success (0.04 vs 0.72). FOREWARN never edits — it selects among samples **the policy itself drew**, so the executed action is in-distribution by construction. One paper came from safety, the other from intent-alignment; neither states the rule in general form, and the wiki should: **a runtime intervention that stays inside the policy's own output distribution costs nothing; one that leaves it costs almost everything.**

Two results from it worth carrying independently:

- **Predicted latents beat ground-truth images as VLM input.** FOREWARN scores 0.82 narration accuracy against 0.52 for GPT-4o shown the *actual* future frames. Frontier VLMs do not reliably extract fine-grained contact detail (handle vs rim vs interior) from video.
- **Natural language is the representation in which generalization survives.** A transformer classifier over the same predicted latents *ties* FOREWARN on trained task descriptions (0.80/0.70/0.70) and **collapses to 0.00/0.10/0.20** on novel ones. Routing the decision through narration — rather than asking the VLM for a category — is what preserves open-world reasoning.

FOREWARN's own three-way taxonomy locates everything on this page, and its criticism of the middle row is the one this wiki reached independently:

| Category | What it does | Instances here |
|---|---|---|
| Post-hoc detection | Find and explain failures in offline data | none ingested |
| **Runtime monitoring** | Detect failures *as they happen* | [Sentinel](../../sources/sentinel-paper.md), [FAIL-Detect](../../sources/fail-detect-paper.md) |
| **Failure prediction** | Anticipate *before* they occur, enabling preemptive correction | [FOREWARN](../../sources/forewarn-paper.md) |

> *"[Monitoring strategies] fundamentally require the robot to start failing for the runtime monitor to activate."*

**And the two halves do not yet compose.** FOREWARN assumes a good plan is among the K samples and names detecting *"if none of the policy's generated action plans are suitable"* as future work — which is exactly what a monitor does. Monitors assume something has already gone wrong. Nobody has built the system where the monitor escalates because steering has run out of options.

## Where it sits

Three distinct mechanisms, three distinct questions, and a deployed system needs all three:

| Layer | Question | Wiki page |
|---|---|---|
| **Safety filter** | Will this action hurt someone or break something? | [Safety filters](safety-filters.md) |
| **Runtime monitor** | Is this rollout going to succeed? | *this page* |
| **Runtime intervention** | Which of the policy's own options should it take? | [FOREWARN](../../sources/forewarn-paper.md), above |
| **Offline evaluation** | Does this policy work, and how confidently do we know? | [Robot policy evaluation](robot-policy-evaluation.md) |

The filter cannot tell that the policy is confidently doing the wrong thing; the monitor cannot stop the arm from swinging through the table; the evaluation cannot say anything about the rollout currently in progress. They are not substitutes and nothing in this wiki's corpus runs more than one of them at once.

## The synthesis

All of this now sits inside a three-layer argument — **prevention → detection → intervention** — with the design rule that spans it, the four things wrong with every layer, and the hazard that the layers can be mistaken for each other's failure modes: [Prevention, detection, intervention](../../syntheses/platforms/prevention-detection-intervention.md).

## Related concepts

- [Safety filters for learned policies](safety-filters.md) — prevention to this page's detection.
- [Robot policy evaluation](robot-policy-evaluation.md) — the offline counterpart, including the sample-size problem that governs how well any of this can be measured.
- [Imitation learning](../learning/imitation-learning.md) — OOD-state failure is the mechanism.
- [AI guardrails](../safety/ai-guardrails.md) — the semantic-harm analogue, still disjoint.

## Key references

- [Sentinel](../../sources/sentinel-paper.md) — Agia, Sinha, Yang, Cao, Antonova, [Pavone](../../entities/marco-pavone.md), Bohg; CoRL 2024. The taxonomy, STAC, and the VLM monitor.
- [FAIL-Detect](../../sources/fail-detect-paper.md) — Xu et al., **[TRI](../../entities/tri.md)**; RSS 2025. Nine scores compared under one calibration protocol, the `logpZO` flow score, and time-varying conformal bands.
- [FIPER](../../sources/fiper-paper.md) — Römer, Kobras, Worbis & Schoellig; TUM, NeurIPS 2025. Prediction via OOD ∧ action entropy, plus the **TWA** metric and the ID/OOD × success/failure protocol.
- [FOREWARN](../../sources/forewarn-paper.md) — Wu, Tian, Swamy & Bajcsy; CMU 2025. Prediction *and* intervention: world model for foresight, latent-aligned VLM for forethought, steering by selection.

## Mentioned in

- [Sentinel paper](../../sources/sentinel-paper.md)
- [FAIL-Detect paper](../../sources/fail-detect-paper.md)
- [FIPER paper](../../sources/fiper-paper.md)
- [FOREWARN paper](../../sources/forewarn-paper.md)
