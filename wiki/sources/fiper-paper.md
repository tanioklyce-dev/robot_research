---
title: "FIPER — Failure Prediction at Runtime for Generative Robot Policies"
type: source
url: https://arxiv.org/abs/2510.09459
local_path: raw/FIPER_FailurePredictionAtRuntime_2510.09459.pdf
sha256: df815e61dc535ff248b020b151c7b94d7921fa8cca21e5041899a7a165e8a597
project_page: https://tum-lsy.github.io/fiper_website/
author: "Ralf Römer*, Adrian Kobras*, Luca Worbis, Angela P. Schoellig (TU Munich, Learning Systems and Robotics Lab / MIRMI)"
published: 2025-10-10
ingested: 2026-08-16
venue: arXiv 2510.09459 (v2, 2025-10-13); NeurIPS 2025
format: pdf
tags: [failure-prediction, runtime-monitoring, out-of-distribution, random-network-distillation, action-chunk-entropy, conformal-prediction, diffusion-policy, flow-matching, timestep-wise-accuracy, tum]
---

# FIPER — Failure Prediction at Runtime

## Summary

The third TUM/Schoellig-lab entry in this thread (after [PACS](pacs-paper.md)), and the one that **turns the wiki's recurring observation into a measurement**. Both [Sentinel](sentinel-paper.md) and [FAIL-Detect](fail-detect-paper.md) noted that OOD ≠ failure; FIPER makes *distinguishing them* the evaluation axis and designs against it.

The insight is a conjunction: a real failure shows **both** (i) **consecutive OOD observations** — detected by random network distillation in the **policy's own embedding space** (RND-OE) — **and** (ii) **prolonged high uncertainty in the generated actions** — measured by a novel **action-chunk entropy** (ACE) score. Both are calibrated by conformal prediction on a handful of successful rollouts, aggregated over sliding windows, and an alarm fires only when **both** exceed threshold.

That AND is the structural difference from Sentinel, which ORs complementary detectors to raise recall. FIPER conjoins two indicators to **suppress false alarms on situations the policy can actually handle**.

> [!note] Why "predict" rather than "detect", and why the distinction has teeth
> Monitors *"only raise alarms after errors manifest, providing no foresight about impending failure."* Prediction is what buys time for the thing that comes next — *"timely intervention or safe fallbacks or [asking] human experts to demonstrate the task."*
>
> But the paper's sharper contribution is noticing that **the standard metrics do not reward prediction at all**: waiting until the last timestep to "predict" the outcome scores high accuracy, and flagging everything at t=0 scores a perfect detection time. So they propose **timestep-wise accuracy (TWA)**, which credits a true positive with `1 − DT` instead of 1 — accuracy and earliness in one number. A benchmark-design contribution that this wiki's [evaluation thread](../concepts/robotics/robot-policy-evaluation.md) should carry regardless of what happens to FIPER.

## The two signals

**RND-OE — novelty, in the space the policy actually conditions on.** Random network distillation: a frozen random target network `g` and a predictor `f_θ` trained to match it on in-distribution data; they agree on familiar inputs and diverge on novel ones. The design choice that matters is **reusing the policy's own frozen observation encoder** inside both networks, so anomalies are measured **in the policy's embedding space** rather than in raw pixels — *"more indicative of failures than OOD raw observations"* — and the RND model can be trained from a small dataset. Scores are summed over a sliding window, because *"multiple consecutive OOD observations are likely to cause compounding errors… from which the policy cannot recover"* while brief excursions are survivable.

**ACE — entropy, not variance, and the argument for it is the best paragraph in the paper.** Imitation data is multimodal, so a policy can emit very different actions for the same observation *in a successful rollout*; variance therefore says nothing. But *"action multimodality in IL is usually of a **discrete** nature"* — pick object A, B or C; grasp from the side or above; go left or right — so each sample should land cleanly in *some* mode. Sharpness of modes is **entropy**, and entropy is the right uncertainty measure here. Diffusion and flow policies have no tractable likelihood, so ACE samples `B` chunks, treats each prediction timestep separately (the joint over an `H`-step chunk needs an infeasible batch), and estimates entropy by **dimension-wise binning** — chosen as *"more computationally efficient, robust, and easier to tune"* than alternatives. Computed in Cartesian end-effector space for interpretability.

> [!warning] A direct technical criticism of Sentinel's STAC
> FIPER's Figure 3(d): STAC *"typically associates timesteps at which the policy **decides on a behavior mode** with high uncertainty."* Divergence between consecutive action-chunk distributions spikes exactly when a multimodal policy **commits** — which is normal, healthy behavior, not a failure. ACE is designed to be indifferent to *which* mode is chosen and sensitive only to whether the distribution is sharp.
>
> This is the second substantive critique of STAC in two ingested papers, after [FAIL-Detect](fail-detect-paper.md)'s speed measurement. The signal that reads most elegantly on paper is the one both successor works go after.

## Key claims

**Five environments — SORTING, STACKING, PUSHT (sim), PRETZEL (rope-folding), PUSHCHAIR (mobile manipulator, reusing Sentinel's data)** — across diffusion (U-Net) and flow-matching (ACT transformer) policies. Calibration: **M = 50** successful rollouts in sim, **M = 10** real. Averaged over quantiles 0.90–0.99 and five seeds.

| Method | TWA ↑ | Accuracy ↑ | Detection time ↓ |
|---|---|---|---|
| PCA-kmeans | 0.57 | 0.61 | (0.09) |
| **`logpZO`** ([FAIL-Detect](fail-detect-paper.md)) | 0.60 | 0.69 | 0.35 |
| RND-A (ReDiffuser-style) | 0.56 | 0.62 | 0.34 |
| **STAC** ([Sentinel](sentinel-paper.md)) | 0.57 | 0.68 | 0.42 |
| RND-OE (ours, obs only) | 0.59 | 0.67 | **0.18** |
| ACE (ours, actions only) | 0.63 | 0.74 | 0.25 |
| **FIPER (both)** | **0.65** | **0.78** | 0.30 |

- **The conjunction earns its keep**, but modestly: 0.78 average accuracy against 0.74 for ACE alone and 0.69 for the best prior method. On the two real-world tasks the margin is larger (PUSHCHAIR **0.96** accuracy vs 0.88–0.92; PRETZEL 0.85 vs 0.65–0.82).
- **Observation-only and action-only detectors are individually mediocre and fail differently** — RND-OE is fastest (DT 0.18) but less accurate; ACE is more accurate but slower. The paper's framing of prior work is that it *"aim[s] to detect failures either only from the policy inputs **or** outputs"*, and both halves are needed.
- **The four-way rollout split is the evaluation idea to steal**: group rollouts into **Success-ID / Success-OOD / Fail-ID / Fail-OOD** and require scores to order as `Success ID ≤ Success OOD < Fail ID ≤ Fail OOD`. *"The gap between Success OOD and Fail ID provides information about a score's ability to distinguish between OOD and failure."* That is the wiki's "state atypicality is not policy failure" note, converted into a protocol.
- **Honest about the ceiling.** Average accuracy 0.78 and TWA 0.65 — across three papers now, runtime failure prediction on real tasks sits in the 0.7–0.8 band. Nobody is close to solving this.

## Limitations, as stated

- **A separate model to train and rollouts to collect.** *"While we use only a few successful rollouts for calibration, the need to collect them and train an RND-OE model that is separate from the policy is still a limitation."*
- **Runtime cost may not survive high-dimensional action spaces** — humanoids named explicitly. ACE needs a batch of action chunks per timestep, which is the same sampling cost [FAIL-Detect](fail-detect-paper.md) measured as prohibitive for STAC.
- **Single-task vision-based IL policies only.** Adapting to large VLAs is future work — the *third* paper in this cluster to say so.

## Entities mentioned

- **Angela P. Schoellig** (TUM LSR / MIRMI) — senior author here and on [PACS](pacs-paper.md); no page.
- **Ralf Römer** — first author of both FIPER and PACS: the same person built the intervention and the predictor.
- [Diffusion Policy](../entities/diffusion-policy.md) and [ACT](../entities/act.md) — the two policy backbones (diffusion U-Net; flow matching with an ACT transformer).
- [PushT](../entities/pusht.md) · [Franka Panda](../entities/franka-panda.md) — benchmark and hardware.
- [Sentinel](sentinel-paper.md) / [FAIL-Detect](fail-detect-paper.md) — reimplemented as baselines (STAC, `logpZO`), which makes this the first head-to-head in the wiki's runtime cluster.

## Concepts touched

- [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md) — the prediction row of that page's taxonomy.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — **TWA** and the ID/OOD × success/failure protocol.
- [Safety filters for learned policies](../concepts/robotics/safety-filters.md) — the *"timely intervention or safe fallbacks"* that prediction is supposed to enable.
- [Imitation learning](../concepts/learning/imitation-learning.md) — discrete action multimodality is the premise of ACE.

## Open questions

- **Prediction without a receiver is still an alarm.** FIPER predicts to enable *"timely intervention, safe fallbacks, or asking a human to demonstrate."* None of the three is implemented here, and [FOREWARN](forewarn-paper.md) — which *is* an intervention — assumes it is never called. The composition remains unbuilt across four papers that each name it.
- **The same lab wrote the predictor and the intervention** (Römer on FIPER and PACS). PACS brakes path-consistently when *safety* is threatened; FIPER predicts *task* failure. Wiring the second into the first is the obvious in-house experiment.
- **Does ACE survive a VLA?** It needs `B` sampled action chunks per timestep. Cheap for a diffusion policy, expensive for a large autoregressive model — the recurring wall for every sampling-based score in this cluster.
- **0.78 accuracy is not deployable on its own.** What the number needs to be, and what a false alarm costs against a missed failure, is unaddressed by every paper here — and it is a system-design question, not a detector question.
