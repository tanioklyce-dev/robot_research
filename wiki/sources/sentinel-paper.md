---
title: "Sentinel — Unpacking Failure Modes of Generative Policies: Runtime Monitoring of Consistency and Progress"
type: source
url: https://arxiv.org/abs/2410.04640
local_path: raw/Sentinel_UnpackingFailureModes_2410.04640.pdf
project_page: https://sites.google.com/stanford.edu/sentinel
author: "Christopher Agia, Rohan Sinha, Jingyun Yang, Zi-ang Cao, Rika Antonova, Marco Pavone, Jeannette Bohg (Stanford; Pavone also NVIDIA Research)"
published: 2024-10-06
ingested: 2026-08-16
venue: arXiv 2410.04640 (v2, 2024-10-10); CoRL 2024 (PMLR v270)
format: pdf
tags: [runtime-monitoring, failure-detection, generative-policies, diffusion-policy, stac, temporal-consistency, vlm, video-qa, conformal-prediction, out-of-distribution, mobile-manipulation, stanford]
---

# Sentinel — Runtime Monitoring of Consistency and Progress

## Summary

The counterpart to everything ingested this afternoon: those were mechanisms that **prevent** physical harm, and this one **detects** that the policy is failing at its task. Its organizing move is a **divide-and-conquer failure taxonomy** — split generative-policy failures into two complementary categories and give each a specialized detector, because the requirements are opposite:

- **Erratic failures** — the policy's action distributions jitter between conflicting modes; the robot collides, thrashes, ends up somewhere expensive to reset from. **Must be caught fast.** Detected by **STAC** (Statistical measures of Temporal Action Consistency), which costs nearly nothing.
- **Task-progression failures** — the policy is perfectly consistent and confidently doing the wrong thing: stalling, drifting, placing the object in the wrong spot. **Cannot be caught fast** — you have to watch for a while. Detected by a **VLM doing chain-of-thought video QA**, at ~14 s latency, which is acceptable precisely because these failures are not time-critical.

Defining one category as the complement of the other is what makes the combination trivial (a logical OR) and what makes it work: **Sentinel detects 18% more failures than either detector alone**, >97% of unknown failures across simulated and real mobile-manipulation domains, and needs only **successful rollouts plus a task description** to calibrate.

> [!note] STAC's mechanism is the part worth stealing, and it falls out of action chunking
> A chunked policy sampled at time `t` predicts actions for `t…t+h−1`; sampled again at `t+k`, it predicts `t+k…t+h−1+k`. **The two chunks overlap**, so you have *two distributions over the same future timesteps*, generated from different observations. Their statistical distance (MMD, forward/reverse KL) is a direct measure of how much the policy just changed its mind.
>
> Cumulated over the rollout and thresholded, that is the whole detector. It requires no extra model, no failure data, and no assumption about *what* the failure looks like — and it is well-posed for multimodal policies, where comparing two *sampled* action sequences would be meaningless.

## Key claims

- **Calibration is conformal, and the false-positive rate is bounded.** The threshold `γ` is the `1−δ` quantile of cumulative consistency scores over `M` successful validation rollouts (M = 50 sim, **M = 10 real**). Proposition 1: the probability of raising any false alarm on an i.i.d. success trajectory is **at most δ**. A guarantee on *false alarms*, not on detection — the paper is explicit about which direction it can prove.
- **Embedding-based OOD detectors conflate "unfamiliar" with "failing," and the numbers are brutal.** On out-of-distribution Close Box, CLIP/ResNet/policy-encoder embedding similarity all score **TNR = 0.00** — they flag *every* OOD rollout, including the ones where the policy generalizes and succeeds. STAC keeps **TNR 0.85–0.97** there. **State atypicality is not policy failure**, and this is the cleanest demonstration of it in the wiki.
- **Output variance does not work on multimodal policies.** Diffusion output variance scores 0.26–0.33 TPR: in a genuinely multimodal domain (PushT) *both* successes and failures have high-variance outputs. On PushT, STAC is the **only** method above 90% balanced accuracy.
- **It is the statistical distance that matters, not the temporality.** Ablation: bolting temporal consistency onto the baselines helps "at most marginally," and using a **non-statistical** distance (min over samples) is worse than the baselines because it throws away multimodality. The combination is what works.
- **VLMs must reason over video, not images.** GPT-4o single-image QA: **TNR = 0.00** — useless. The same model over the rollout video: **TNR 0.91**. Giving it elapsed time `t` and the horizon `H` lets it judge whether the current *rate* will finish in time.
- **And the two detectors' weaknesses are exactly complementary.** On task-progression shifts, STAC gets **44% TPR** (as designed — the policy is consistent, just wrong); the VLM catches those, and the union reaches **93% TPR for +7% FPR** and **+48% TPR** over STAC alone. On erratic failures the VLM only manages 77% TPR because they are *"visually more subtle"*, while STAC gets ~99%.
- **Real hardware, small n, strong result.** Push Chair (nonprehensile mobile manipulation), 10 successes / 10 failures, calibrated on 10 rollouts: STAC 0.80 TPR / 0.90 TNR; GPT-4o video QA 0.90 / 1.00; **Sentinel 1.00 / 0.90, 95% accuracy, 9.6 s detection**. The VLM does *better* in the real world than in sim — plausibly because rendered images are a larger domain gap for a VLM than real ones.

## Limitations, as stated

- **The two categories may not be exhaustive.** Offered as a hypothesis, not a proof of coverage.
- **No formal guarantee on detection** — only on the false-alarm rate. A detection guarantee *"would require data of both successful and unsuccessful policy rollouts to calibrate,"* which is the assumption the whole method exists to avoid.
- **The union of detectors can raise false alarms** in the worst case.
- **It detects failures as they occur, not before.** Not a predictor.

## Entities mentioned

- [Marco Pavone](../entities/marco-pavone.md) — co-author (Stanford + NVIDIA Research); his fifth ingested source, and the third distinct approach to the same deployment problem.
- **Jeannette Bohg** — senior author, Stanford; no page yet despite being a major manipulation-research figure.
- [Diffusion Policy](../entities/diffusion-policy.md) — the policy class monitored throughout.
- [PushT](../entities/pusht.md) — the multimodality stress case.
- Funding: **[TRI](../entities/tri.md)**, Toshiba, Stanford HAI, Blue Origin, NASA ULI — worth noting given that [FAIL-Detect](fail-detect-paper.md), its main rival, is TRI's own.
- Without pages: Christopher Agia, Rohan Sinha, Rika Antonova; GPT-4o and Claude as the VLM monitors.

## Concepts touched

- [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md) — **new concept page from this ingest.**
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — detection *during* a rollout, where that page measures success *after*.
- [Safety filters for learned policies](../concepts/robotics/safety-filters.md) — the prevention half; Sentinel is the detection half.
- [Imitation learning](../concepts/learning/imitation-learning.md) — OOD behavior of behavior-cloned policies is the whole subject.
- [VLA models](../concepts/learning/vla-models.md) — the method needs only action chunks, so it applies to VLAs as written.

## Open questions

- **Detect ≠ recover.** Sentinel raises a flag and stops execution. What the robot should *do* next — human handoff, retry, replan — is out of scope here and is the [empty execution rail](../syntheses/agents/guardrails-for-robot-agents.md) this wiki keeps finding.
- **A 14-second VLM in the loop is a cost nobody has priced.** The paper argues progression failures tolerate it. On a robot doing a 25-second task, a monitor that answers after 14 s is a meaningful fraction of the episode.
- **Would STAC survive on a VLA?** It needs a *distribution* over overlapping action chunks, so it needs a policy you can sample in batch. Cheap for a diffusion policy on a GPU; unclear for a large autoregressive VLA — and [FAIL-Detect](fail-detect-paper.md) argues the sampling cost is already prohibitive.
