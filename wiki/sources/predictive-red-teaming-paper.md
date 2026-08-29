---
title: "Predictive Red Teaming: Breaking Policies Without Breaking Robots"
type: source
url: https://predictive-red-team.github.io/
author: "Anirudha Majumdar, Mohit Sharma, Dmitry Kalashnikov, Sumeet Singh, Pierre Sermanet, Vikas Sindhwani"
affiliation: Google DeepMind, Princeton University
published: 2025-02-10
ingested: 2026-08-03
venue: arXiv preprint (2502.06575)
format: research paper (26 pp) + project page
local_path: raw/2502.06575.pdf
sha256: 5540d859be4a7a575ee8935bc261dd9471c7805db29d08019a0eca478bac5291
tags: [predictive-red-teaming, roboart, red-teaming, robot-policy-evaluation, anomaly-detection, conformal-prediction, diffusion-policy, google-deepmind, safety, primary-source]
---

## Summary

Proposes **predictive red teaming**: discovering a policy's vulnerabilities to environmental factors and **predicting the resulting performance degradation without running hardware evaluations** in those off-nominal conditions. The motivating problem is one the wiki has documented repeatedly — visuomotor policies trained by imitation are "often extremely brittle to lighting, visual distractors, and object locations," and those vulnerabilities "depend unpredictably on the specifics of training."

The system is **RoboART**, a two-step pipeline:
1. **Generative image editing** (Imagen 3) modifies nominal RGB observations to vary environmental factors from language instructions — *"add a person close to the table"*, background swaps, lighting changes, table-height changes.
2. **Anomaly detection** predicts degradation by computing distances **in the policy's own embedding space** between edited and nominal observations, with the anomaly threshold calibrated by **conformal prediction**.

The elegance is that the predictor is *policy-specific and training-free*: no new model is fitted, the policy's own representation is asked whether an edited scene looks unfamiliar.

## Key claims

### Prediction accuracy — 500+ hardware trials, twelve factors, two policies

| Metric | π_hyb | π_dfn |
|---|---:|---:|
| **Spearman ρ** (predicted vs actual factor ranking) | **0.8** | **0.7** |
| **Average prediction error** (predicted vs real success rate) | **0.10** | **0.19** |

Two visuomotor **diffusion policies with significantly different architectures**. Twelve off-nominal conditions: background, lighting, distractors, injected humans, table height, and others.

> [!note] The authors' own calibration of that error
> The paper notes 0.19 "is roughly in the range of noise when estimating success rates from ~20 trials." That is a candid and important framing: **with ~20 trials per condition, the ground truth itself is noisy**, so the predictor is accurate to roughly the resolution of the measurement it is predicting. It does not establish accuracy finer than that — see the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), where n=20 puts the minimum detectable gap around 40 pp near 50%.

RoboART correctly predicts *relative* severity — e.g. that changing table height degrades performance substantially more than a human distractor — and identifies that π_dfn is more vulnerable than π_hyb to specific factors (blue lighting, table height).

### Targeted data collection — the payoff
Co-finetuning with demonstrations collected under **the three conditions predicted to be most adverse**:
- **2–7× performance boost** in those predicted-adverse conditions.
- **Cross-domain generalization: 2–5× improvement in conditions that were never collected for.**

This is the practical argument: red teaming is not only an audit, it is a **data-collection targeting policy**. Rather than collecting more data uniformly, collect where the policy's own embedding space says it is lost.

## Entities mentioned
- [Google DeepMind](../entities/google-deepmind.md) · Princeton University · [Anirudha Majumdar](../entities/anirudha-majumdar.md) (first author; "work done while on sabbatical at Google DeepMind") · [Pierre Sermanet](../entities/pierre-sermanet.md) · [Vikas Sindhwani](../entities/vikas-sindhwani.md)
- [RoboART](../entities/roboart.md) · [Diffusion policy](../entities/diffusion-policy.md) — the policy class evaluated

## Concepts touched
- [AI red teaming](../concepts/safety/ai-red-teaming.md) — extends the concept from language models to *visuomotor policies*.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — a fourth paradigm alongside real rollouts, pairwise preference, and world-model simulation.
- [Semantic safety](../concepts/safety/semantic-safety.md) — sibling paper's concern; this one is about *capability* brittleness rather than judgment.
- [Imitation learning](../concepts/learning/imitation-learning.md) — the brittleness this addresses.

## Open questions

Stated limitations:
- **Edit-to-real gap.** Image edits are imperfect — "edits that reflect lighting changes do not modify the shadows of objects as real lighting changes do." More seriously, **multi-view consistency fails**: edited overhead and wrist-camera observations "do not represent a consistent geometry for the new object." Gaussian-splatting-based 3D scene editing is proposed as the fix. *(Notably, the [Veo simulator paper](veo-robotics-policy-evaluation-paper.md) ten months later makes multi-view consistency a first-class design goal — this limitation is the direct motivation for that line.)*
- **Anomaly-to-failure gap.** Anomaly rate is a proxy for degradation and "predictions are not perfectly accurate." Suggested fix: edit observations from multiple timesteps per episode and compute sequential anomaly rates.

Wiki additions:
- **n≈20 per condition** means the individual factor-level success rates are not separable from each other; only the coarse ranking (Spearman ρ) and the large 2–7× fine-tuning gains are robust.
- **Only two policies, both diffusion policies.** Whether embedding-space anomaly detection predicts degradation for VLAs (which have very different representations) is untested — and VLAs are what the wiki mostly tracks.
- Edits are RGB-only; depth channels are not edited, which the authors flag.

## Related sources
- [ASIMOV Benchmark](asimov-benchmark-paper.md) — the semantic-safety sibling; overlapping authors.
- [Veo world simulator evaluation](veo-robotics-policy-evaluation-paper.md) — the successor line that fixes multi-view consistency.
- [DeepMind — Responsibly advancing AI and robotics](deepmind-gemini-robotics-safety-page.md) — names this work as one of three safety pillars.
- [Success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) — the standard this paper's n≈20 is read against.
