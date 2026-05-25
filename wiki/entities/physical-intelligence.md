---
title: Physical Intelligence
type: entity
subtype: organization
created: 2026-05-09
updated: 2026-05-25
sources: 3
tags: [physical-intelligence, vla, pi0, pi-zero, generalist-policy, robotics, flow-matching]
---

**Physical Intelligence** (also written as π) — San Francisco AI robotics company; develops cross-platform generalist robot policies. Known for the **[π0](pi-zero.md)** (2024) and **π0.6** (2025) VLAs that demonstrate task generalization across different robot platforms without task-specific retraining.

## Key capabilities

- **[π0](pi-zero.md)** (Black, Brown, Driess, et al., October 2024 — [paper](../sources/pi-zero-paper.md), now full-HTML-ingested): 3.3 B-param vision-language-action **flow-matching** model = PaliGemma 3 B VLM + ~0.3 B flow-matching "action expert" with full bidirectional self-attention. Trained on **~10,000 hours of in-house dexterous teleop** across 7 robot configurations + 68 tasks + OXE + DROID + Bridge. Demonstrated on laundry folding, table bussing, microwave dish loading, egg-carton stacking, box assembly, grocery bagging. Beat OpenVLA and Octo as baselines. **See the [π0 entity](pi-zero.md) for the full architectural + comparison detail.**
- **π0.6** (2025): successor; broader task coverage. (Primary source not yet filed — referenced via the [Stanford HAI AI Index 2026](../sources/stanford-hai-ai-index-2026.md).)
- The action-head choice — **flow matching** — is now the canonical contrast point against [Diffusion Policy](diffusion-policy.md)'s DDPM and OpenVLA's autoregressive action tokens. Both [SmolVLA](smolvla.md) and [EgoScale](../sources/egoscale-paper.md) adopted flow matching as their action head after π0.

## Significance

Physical Intelligence and [NVIDIA GR00T](../entities/nvidia-groot.md) / Gemini Robotics represent the main non-academic demonstration that VLA-style generalist policies can work across real robot platforms. The [Stanford HAI AI Index 2026](../sources/stanford-hai-ai-index-2026.md) cites π0/π0.6 as the leading examples of Physical AI / foundation models for robotics.

## Related
- [π0](pi-zero.md) — model entity (split off 2026-05-25 with the full-HTML π0 ingest).
- [VLA models](../concepts/learning/vla-models.md) — π0/π0.6 are in this paradigm.
- [SmolVLA](smolvla.md) — Hugging Face's smaller open contemporary; uses π0 as baseline.
- [NVIDIA GR00T](../entities/nvidia-groot.md) — parallel generalist-policy effort.

## Mentioned in
- [π0 Paper](../sources/pi-zero-paper.md) — primary source.
- [SmolVLA Paper](../sources/smolvla-paper.md) — uses π0 as primary baseline.
- [Stanford HAI — AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md)
