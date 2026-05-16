---
title: Physical Intelligence
type: entity
subtype: organization
created: 2026-05-09
updated: 2026-05-10
sources: 2
tags: [physical-intelligence, vla, pi0, generalist-policy, robotics]
---

**Physical Intelligence** (also written as π) — San Francisco AI robotics company; develops cross-platform generalist robot policies. Known for the **π0** (2024) and **π0.6** (2025) VLAs that demonstrate task generalization across different robot platforms without task-specific retraining.

## Key capabilities

- **π0** (Black, Brown, Driess, et al., October 2024 — [paper](../sources/pi-zero-paper.md)): vision-language-action **flow-matching** model built on a pre-trained VLM backbone. Trained across single-arm, dual-arm, and mobile-manipulator embodiments. Demonstrated on laundry folding, table cleaning, and box assembly. One of the first credible cross-platform generalist robot policies.
- **π0.6** (2025): successor; broader task coverage. (Primary source not yet filed — referenced via the [Stanford HAI AI Index 2026](../sources/stanford-hai-ai-index-2026.md).)
- Both models demonstrate the VLA approach of replacing the traditional modular perception-planning-action pipeline with a single end-to-end network. The action-head choice — flow matching — is a notable contrast with [Diffusion Policy](diffusion-policy.md)'s DDPM and OpenVLA's autoregressive action tokens.

## Significance

Physical Intelligence and [NVIDIA GR00T](../entities/nvidia-groot.md) / Gemini Robotics represent the main non-academic demonstration that VLA-style generalist policies can work across real robot platforms. The [Stanford HAI AI Index 2026](../sources/stanford-hai-ai-index-2026.md) cites π0/π0.6 as the leading examples of Physical AI / foundation models for robotics.

## Related
- [VLA models](../concepts/learning/vla-models.md) — π0/π0.6 are in this paradigm.
- [NVIDIA GR00T](../entities/nvidia-groot.md) — parallel generalist-policy effort.

## Mentioned in
- [Stanford HAI — AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md)
- [π0 Paper](../sources/pi-zero-paper.md)
