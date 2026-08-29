---
title: "FAIL-Detect — Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies"
type: source
url: https://arxiv.org/abs/2503.08558
local_path: raw/FAILDetect_UncertaintyAwareRuntimeFailureDetection_2503.08558.pdf
sha256: d8dfcca672a8d343fc52fbaa6b29d0f5b102697081b3640643b9e61a7b80d332
project_page: https://cxu-tri.github.io/FAIL-Detect-Website/
author: "Chen Xu, Tony Khuong Nguyen, Emma Dixon, Christopher Rodriguez, Patrick Miller, Robert Lee, Paarth Shah, Rares Ambrus, Haruki Nishimura, Masha Itkina (Toyota Research Institute; Robert Lee at Woven by Toyota)"
published: 2025-03-11
ingested: 2026-08-16
venue: arXiv 2503.08558 (v3, 2025-06-20); RSS 2025
format: pdf
tags: [runtime-monitoring, failure-detection, imitation-learning, diffusion-policy, flow-matching, conformal-prediction, out-of-distribution, normalizing-flows, epistemic-uncertainty, tri, franka, bimanual]
---

# FAIL-Detect — Failure detection without failure data

## Summary

**[TRI](../entities/tri.md)'s answer to the same problem [Sentinel](sentinel-paper.md) attacks, and a direct rebuttal of it on the axes that matter for deployment: accuracy, and speed.**

The framing is a deliberate constraint. Most failure detectors are binary classifiers, and binary classifiers need failure examples — which are *"time-consuming, expensive, and even infeasible"* to enumerate, and which generalize badly to unseen failure modes. FAIL-Detect trains on **successful data only** by reframing detection as **sequential OOD detection**, in two decoupled stages:

1. **Distill policy inputs and outputs into a scalar score** that correlates with failure and captures epistemic uncertainty. Nine candidates are compared, spanning learned density estimation, second-order (evidential) methods, one-class discriminators, and post-hoc metrics.
2. **Threshold it with conformal prediction** — specifically a **time-varying CP band** `[·, μ_t + h_t]` calibrated on successful rollouts, which controls the false-positive rate at level `α` while adapting to the changing dynamics of the task.

The headline empirical finding is that **learned scores beat post-hoc scores**, and the best of them is the paper's own: **`logpZO`**, a normalizing-flow density estimate evaluated **in the latent noise space** rather than observation space.

## The mechanism worth understanding: `logpZO`

Fit a continuous normalizing flow `f_θ` to observations from successful rollouts. The obvious use is to score a new observation's likelihood directly (`logpO`) — but that requires integrating the **divergence** of `f_θ` along the ODE, which is hard to estimate in high dimensions.

`logpZO` avoids it. Run the **forward** ODE from the observation to obtain its noise encoding `Z_{O_t}`. If the observation is in-distribution, `Z_{O_t}` should be approximately standard Gaussian, so `p(Z) ∝ exp(−½‖Z‖²)` and **`‖Z_{O_t}‖²` is the score**. No divergence, no density in observation space — a norm in latent space.

That is a clean trick with reach beyond robotics: **push the sample through the flow and check whether it lands where noise should be.**

## Key claims

- **Failure detection without failure data works, and the numbers are honest about being modest.** Average best balanced accuracy **~78% in simulation** and **~72% on hardware**. Detection is faster than average successful-trajectory completion. This is not a solved problem; it is a demonstration that the failure-free formulation is viable.
- **Learned > post-hoc, consistently.** In simulation (Robomimic Square / Transport / Can / Toolhang, ID and OOD, 2000 rollouts): `logpZO` takes **top-1 in 10/16** cases and **top-3 in 14/16**; RND 5/16 and 9/16. The post-hoc baselines: **STAC top-1 in 3/16**, PCA-kmeans **0/16**. On hardware (2 bimanual Franka tasks, 50 rollouts): `logpZO` top-1 in **8/12**, top-3 in **11/12**.
- **A time-varying CP band beats a constant threshold.** STAC uses a single scalar threshold on cumulative divergence; FAIL-Detect's band tracks `μ_t + h_t` over the rollout, which matters because manipulation tasks have phases with genuinely different score statistics.
- **The score candidates are a useful map of the OOD-detection literature applied to policies**: density (`logpO`, `logpZO`), second-order/evidential (NatPN, DER), one-class discriminators (RND, consistency flow matching), post-hoc (SPARC smoothness, STAC, PCA-kmeans). Most were adapted from other fields; the comparison under one calibration protocol is a contribution in itself.
- **Failure diversity is the argument for the whole design.** Figure 2 shows six qualitatively different failures from *one* trained policy on *one* pick-and-place task — slipped early, slipped late, tilted up, tilted down, tilted slightly, never picked up. No classifier trained on an enumerated failure set covers that.
- **Hardware is genuinely hard**: bimanual Franka **FoldRedTowel** (with a human pulling the towel mid-rollout — a disturbance that sometimes appears in training data, so recovery is legitimate) and **CleanUpSpill** with an unseen green towel. These are distribution shifts a policy can sometimes survive, which is precisely the case that breaks naive OOD detectors.

> [!warning] Contradiction: this paper and Sentinel disagree about whether STAC is fast enough to deploy
> [Sentinel](sentinel-paper.md) describes STAC as detecting erratic behavior *"at negligible computational cost."*
>
> FAIL-Detect measures it: STAC needs a **batch of 256 action predictions per timestep**, costing **1.45 s per step** on an A6000 against **0.033–0.04 s** for `logpZO` — a **36–44× slowdown**. They report STAC's detection time *"consistently exceeds practical limits, surpassing the average success trajectory time, rendering the detection not practical"*, and they **omit STAC from the hardware comparison entirely** because it was too slow to run in real time. They also drop Sentinel's VLM component *"to remain as real-time feasible as possible."*
>
> Both can be true as stated: "negligible" is relative to a diffusion policy's own denoising cost when batching is parallelized on a GPU, and Sentinel's own reported detection times (5–14 s) are within its episode lengths. But the operational verdict differs sharply, and it is TRI — a group that actually deploys these policies — saying the sampling-based score does not fit. Note also that FAIL-Detect reproduces STAC with **PushT hyperparameters** on different tasks, which is a reproduction caveat worth naming.

## Limitations, as stated

- **The learned scores lean on robot state over vision.** *"At times, the learned scores focus on simpler robot state information (e.g., gripper closed or open) over the higher-dimensional visual features"* — an admission that the detector may be reading proprioception rather than understanding the scene.
- **False positives in OOD settings** where trajectories degrade; the setting-dependent CP band is a partial answer, adaptive significance levels are future work.
- **The scores are not temporal.** Only the CP band is time-aware; each score sees the last `T_O = 2` observations. Distilling temporal patterns into the score is left open — which is exactly what STAC does, so the two approaches are less opposed than the benchmark suggests.
- **No sound or tactile.** Multimodal sensing is named as a route to faster detection.

## Entities mentioned

- [TRI](../entities/tri.md) — the affiliation, and the reason this matters: the same lab that builds [LBMs](../concepts/learning/large-behavior-models.md) and [Diffusion Policy](../entities/diffusion-policy.md) is building the monitor for them. Thanks to **Ben Burchfiel** and Vitor Guizilini in the acknowledgements, and to TRI's **robot teacher team** for data collection.
- **Masha Itkina, Haruki Nishimura, Rares Ambrus** — TRI authors; also the group behind other TRI runtime-monitoring work. No pages.
- [Diffusion Policy](../entities/diffusion-policy.md) and **flow matching** — both policy classes are tested; the method is architecture-agnostic by construction.
- [Franka Panda](../entities/franka-panda.md) — bimanual station for the hardware tasks.
- **Robomimic** — the simulation benchmark (Square, Transport, Can, Toolhang).
- Woven by Toyota — second affiliation (Robert Lee).

## Concepts touched

- [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md) — **the concept page this and [Sentinel](sentinel-paper.md) jointly anchor.**
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — the offline counterpart.
- [Safety filters for learned policies](../concepts/robotics/safety-filters.md) — prevention vs detection.
- [Imitation learning](../concepts/learning/imitation-learning.md) · [Large behavior models](../concepts/learning/large-behavior-models.md) — the policies being monitored, and TRI's own program.

## Open questions

- **What happens when the detector fires?** Same gap as Sentinel: detection is not recovery, and neither paper closes the loop.
- **`logpZO` reads robot state more than pixels** — by the authors' own admission. A detector that mostly watches the gripper is a weaker claim than "we detect OOD conditions," and testing that directly (ablate the visual features) would settle it.
- **Nobody has combined the two lines.** FAIL-Detect's time-varying CP band is orthogonal to Sentinel's failure taxonomy; STAC as a *score* inside FAIL-Detect's stage-2 band is an experiment the paper half-runs (it keeps STAC's own constant threshold as the baseline) and nobody has run the full cross.
- **Does it survive on an LBM?** Both papers monitor single-task policies. TRI's own generalist program is the obvious next target, and the acknowledgements suggest the people to do it are in the building.
