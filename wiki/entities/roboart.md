---
title: RoboART
type: entity
subtype: system
created: 2026-08-03
updated: 2026-08-03
sources: 2
tags: [roboart, red-teaming, anomaly-detection, conformal-prediction, policy-evaluation, google-deepmind, safety]
---

**RoboART** (automated **R**ed **T**eaming) — the pipeline behind **[predictive red teaming](../sources/predictive-red-teaming-paper.md)**: discovering a policy's environmental vulnerabilities and **predicting the performance drop without running the hardware experiment**.

## How it works
1. **Generative image editing** (Imagen 3) varies environmental factors in nominal observations from language instructions — *"add a person close to the table"*, background, lighting, table height.
2. **Anomaly detection** predicts degradation from distances **in the policy's own embedding space** between edited and nominal observations, thresholded by **conformal prediction**.

No new model is trained: the policy's own representation is asked whether the edited scene looks unfamiliar.

## Results (500+ hardware trials, 12 factors, 2 diffusion policies)
| | π_hyb | π_dfn |
|---|---:|---:|
| Spearman ρ (factor ranking) | **0.8** | **0.7** |
| Avg. prediction error | **0.10** | **0.19** |

Correctly predicts that changing table height hurts far more than a human distractor. **Targeted data collection** on the three predicted-worst conditions gave **2–7×** gains there and **2–5×** in conditions never collected for.

> [!note] Accurate to the resolution of its own ground truth
> The authors note 0.19 "is roughly in the range of noise when estimating success rates from ~20 trials" — so RoboART is validated at about the precision of the measurement it predicts, not finer.

## Limitations
**Edit-to-real gap** (lighting edits don't move shadows) and, more seriously, **multi-view inconsistency** — edited overhead and wrist views don't share a geometry. That limitation directly motivates the multi-view-consistent [Veo simulator](veo.md) line ten months later.

## Related
- [Veo](veo.md) — the successor that makes multi-view consistency a design goal.
- [ASIMOV Benchmark](asimov-benchmark.md) — the semantic-safety sibling.
- [Diffusion policy](diffusion-policy.md) — the policy class tested.
- [AI red teaming](../concepts/safety/ai-red-teaming.md) · [Semantic safety](../concepts/safety/semantic-safety.md).

## Mentioned in
- [Predictive Red Teaming paper](../sources/predictive-red-teaming-paper.md) — primary source.
- [Responsibly advancing AI and robotics](../sources/deepmind-gemini-robotics-safety-page.md) — named as a safety pillar.
