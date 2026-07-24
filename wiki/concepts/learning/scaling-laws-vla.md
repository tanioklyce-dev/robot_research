---
title: Scaling laws — VLAs and human data
type: concept
created: 2026-05-15
updated: 2026-07-04
sources: 10
tags: [scaling-laws, vla, human-data, egocentric, gr00t, egoscale, pretraining]
---

**Scaling laws for Vision–Language–Action (VLA) models** — the empirical relationship between **pretraining data scale** and **downstream real-robot performance**. The robotics analogue of Hoffmann et al.'s Chinchilla scaling laws for LLMs. As of 2026, the field has exactly one published clean scaling law: **EgoScale (NVIDIA GEAR, Feb 2026)** on human-video pretraining for dexterous manipulation.

## Definition

Two related quantities are typically measured:

1. **Validation loss vs. pretraining data scale** — an *offline* metric. EgoScale fits:
   ```
   L = 0.024 − 0.003 · ln(D)         R² = 0.9983
   ```
   where `D` is hours of human video (1k–20k hr range, [EgoScale](../../sources/egoscale-paper.md) Eq. 1).
2. **Real-robot task success vs. pretraining data scale** — the *online* metric that actually matters. EgoScale reports monotonically increasing task completion (0.30 → 0.71) across the same 1k → 20k hr range.

The critical empirical finding is that **(1) tracks (2)** — offline validation loss is a *predictive* indicator of online robot performance, so you can iterate on pretraining at offline speed. This is the same insight that made LLM scaling laws useful: you can sweep models on validation perplexity and trust that downstream metrics will follow.

## Why this is hard for robotics
- **No standard pretraining dataset.** Unlike LLMs (web-scale text) or vision (ImageNet → LAION), there is no agreed-on robotics pretraining corpus. EgoScale's 20,854 hr is the largest published.
- **Embodiment gap.** A human-video scaling law doesn't directly tell you what robot-teleop scaling looks like, or sim-rollout scaling, or how the three combine.
- **Quality-vs-quantity confound.** EgoScale's data is noisy (in-the-wild SLAM + hand-pose estimation) but works at scale; would clean, smaller datasets like [EgoDex](../../entities/egodex.md) (Apple Vision Pro) follow the same law?
- **Long evaluation cycle.** Each data point on the curve = a full pretrain run + real-robot eval. Sweeping data scale at all is expensive; EgoScale's 5 points (1k / 2k / 4k / 10k / 20k hr) is already a major investment.

## What EgoScale shows

| Aspect | EgoScale finding |
|---|---|
| **Functional form** | Log-linear in data: `L = a − b · ln(D)`. Not the power-law `L = a · D^(-α)` of LLM scaling. |
| **Range** | 1k–20k hours; no saturation in the explored regime. |
| **R²** | 0.9983 — essentially noiseless. |
| **Online correlation** | Validation loss tracks real-robot task success monotonically. |
| **Saturation** | None observed at 20k hr. The authors decline to extrapolate but note "substantial headroom." |
| **Action representation matters** | Joint-space hand actions beat fingertip-SE(3) and wrist-only ablations. Scaling law applies to the **joint-space** representation. |
| **Cross-embodiment** | Pretraining transfers to a tri-finger hand on the Unitree G1 (+30% absolute) — the learned motor prior is not specific to the 22-DoF training target. |

## What's still unknown
- **Does the law continue beyond 20k hr?** Logarithmic-in-data implies diminishing returns; eventually you'd need a 10× data jump per fixed loss decrement. Whether real-robot performance keeps tracking is empirical.
- **What's the *compute*-optimal trade-off?** LLM scaling-law work (Chinchilla) is about jointly choosing data scale and model size. EgoScale fixed its model size and only varied data; there's no published VLA Chinchilla yet.
- **What's the cross-task transfer story?** EgoScale evaluates on dexterous tabletop tasks. Does the same scaling law apply to long-horizon locomotion, navigation, or whole-body humanoid control?
- **Does sim-data scaling follow the same law?** Cosmos / world-foundation-model lines are betting on synthetic data; if synthetic scales differently, the "where to invest next dollar" answer flips.

## Related concepts
- [VLA models](vla-models.md) — the model class the scaling law characterizes.
- [Imitation learning](imitation-learning.md) — pretraining objective is human-video imitation.
- [Sim-to-real transfer](sim-to-real-transfer.md) — the alternative-paradigm pretraining-data source (sim rollouts instead of human video).
- [World model](../world-models/world-model.md) — adjacent line; world-model pretraining has its own (unpublished) scaling story.

## Key references
- **[EgoScale Paper](../../sources/egoscale-paper.md)** (Zheng et al., NVIDIA GEAR, Feb 2026) — the first and currently only VLA pretraining scaling law in the literature. 20,854 hr human video, log-linear loss-vs-data law, robot-performance correlation.
- **Hoffmann et al. 2022** (Chinchilla) — not in `raw/`; the LLM-side reference scaling-law paper. Different functional form (power-law) and different problem (compute-optimal model-vs-data trade-off).
- **[Welch Labs Illustrated Guide to AI, Vol I, Ch 6](../../sources/welchlabs-illustrated-guide-to-ai.md)** (Welch, 2026) — pedagogy-grade companion. Walks through Kaplan et al. 2020 (the OpenAI scaling-law paper) with the fitted slopes (compute ≈ −0.050, params ≈ −0.076, dataset ≈ −0.09). The wiki's accessible-pedagogy entry point for the LLM-side scaling-law literature; useful complement when readers ask "is the EgoScale law really a robotics version of the LLM thing, or is it different?"

## Current state (2026-05)
- One published scaling-law paper (EgoScale). Everything else in the VLA literature ([GR00T](../../entities/nvidia-groot.md), [π0](../../entities/physical-intelligence.md), [Helix](../../entities/figure.md)) reports *single-point* training runs without a scaling sweep.
- GR00T N1.7 ships on the **same 20,854 hr corpus** EgoScale uses — so the largest VLA in production is built on the scaling-law-validated regime.
- The wiki's [LeWorldModel](../../entities/leworldmodel.md) JEPA line has *no* published scaling law of any kind; this is a major TBD.

## Mentioned in
- [EgoScale Paper](../../sources/egoscale-paper.md)
- [Welch Labs Illustrated Guide to AI, Vol I](../../sources/welchlabs-illustrated-guide-to-ai.md)

## Open follow-ups
- **Chinchilla-style compute-optimal sweep** — would require a model-size dimension on top of the data-size sweep. Reasonable next paper for the GEAR team.
- **Cross-task scaling** — does the law hold for humanoid whole-body control, or only dexterous tabletop? GEAR's SONIC / HOVER / ASAP lines are the natural test beds.
- **Real-vs-sim data scaling comparison** — Cosmos generates synthetic data; a controlled comparison of "1k hr sim" vs "1k hr real human video" at matched model size would be a foundational result.
- **A `concepts/scaling-laws-llm.md` partner page** if/when the wiki needs the LLM scaling-law literature in scope. Currently out of scope; the wiki is robotics-focused.
