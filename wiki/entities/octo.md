---
title: Octo
type: entity
subtype: model
created: 2026-05-25
updated: 2026-08-26
sources: 8
tags: [octo, vla, generalist-policy, transformer, open-weights, baseline]
status: stub
---

> [!note] Stub entity
> Filed 2026-05-25 during lint (17 mentions across 10 wiki files). Primary source — Octo Model Team et al. 2024 — **not yet ingested**; deepen when filed.

**Octo** — open-source transformer-based generalist robot policy (Octo Model Team et al., 2024; arXiv 2405.12213). Trained from scratch on the **Open X-Embodiment** dataset across many robot configurations. Two main variants: **Octo-Small (~27M params)** and **Octo-Base (~93M params)**. The reference "transformer-from-scratch" VLA baseline — used as a comparison point in nearly every 2024–2025 VLA paper.

## What we know via the wiki's existing references

- **Architecture**: transformer encoder-decoder trained from scratch on demonstration data (no VLM backbone), unlike [π0](pi-zero.md)'s PaliGemma-based or [OpenVLA](openvla.md)'s Llama-based approaches.
- **Training data**: **800K trajectories** from the [Open X-Embodiment](open-x-embodiment.md) dataset.
- **Open weights** — the small + base variants are public.
- **Baseline performance**:
  - [π0 paper](../sources/pi-zero-paper.md) trained Octo for 320K steps on its own data mixture as a baseline and beat it on bussing tasks.
  - [SmolVLA paper](../sources/smolvla-paper.md) Table 2: Octo (0.09B) gets **75.1 LIBERO avg** — beaten by both OpenVLA (76.5) and SmolVLA (87.3) and π0 (86.0 with robotics pretraining).
- **Cited consistently as a pre-flow-matching baseline** — 2024 transformer-from-scratch generalist policy approach that the subsequent VLM-backbone + flow-matching wave (π0, SmolVLA) decisively beat.

## Why it matters in this wiki

- **The "transformer-from-scratch" reference point.** Filing closes 17 mentions across 10 files; converts text references into entity links.
- **Lineage anchor**: Octo predates VLM-backbone VLAs and is the comparison that demonstrates the value of pretrained VLM grounding for robotics.

## Related

- [VLA models](../concepts/learning/vla-models.md) — broader concept; Octo is one of the "transformer-from-scratch" entries.
- [Open X-Embodiment (OXE)](open-x-embodiment.md) — primary training corpus.
- [OpenVLA](openvla.md), [π0](pi-zero.md), [SmolVLA](smolvla.md) — successor / contemporary VLAs that beat Octo on benchmarks.
- [Chelsea Finn](chelsea-finn.md) — affiliated (Octo Model Team includes Finn's collaborators).
- [Sergey Levine](sergey-levine.md), [Karl Pertsch](karl-pertsch.md) — also affiliated.

## Code & weights

- Project page: https://octo-models.github.io
- Repo: https://github.com/octo-models/octo
- Weights on HF: `rail-berkeley/octo-small-1.5`, `rail-berkeley/octo-base-1.5`

## Open questions

- **Primary source not yet ingested.** When it lands, deepen with exact training-data mixture, architecture details, and per-embodiment evaluation numbers.
- **Octo v1.5 / v2** — successor versions referenced in 2025 papers; not ingested.

## Mentioned in

- [awesome-physical-ai (GitHub curated list)](../sources/awesome-physical-ai-github.md)
- [GR00T N1 — An Open Foundation Model for Generalist Humanoid Robots (paper)](../sources/groot-n1-paper.md)
- [Hierarchical Planning with Latent World Models (HWM)](../sources/hwm-paper.md)
- [MolmoAct: Action Reasoning Models that can Reason in Space](../sources/molmoact-paper.md)
- [RoboCasa365 Paper](../sources/robocasa365-paper.md)
- [SmolVLA: A vision-language-action model for affordable and efficient robotics (Shukor et al., June 2025)](../sources/smolvla-paper.md)
- [VLA-0 — Building State-of-the-Art VLAs with Zero Modification](../sources/vla-0-paper.md)
- [π0 Paper — A Vision-Language-Action Flow Model for General Robot Control (Black et al., Physical Intelligence, 2024)](../sources/pi-zero-paper.md)
