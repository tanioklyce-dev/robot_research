---
title: GEAR-SONIC
type: entity
subtype: method
created: 2026-07-04
updated: 2026-07-04
sources: 2
tags: [gear-sonic, sonic, whole-body-control, humanoid, loco-manipulation, motion-tracking, unitree-g1, nvidia, gear, groot]
---

**GEAR-SONIC** ("Supersizing mOtion tracking for Natural humanoId Control") — NVIDIA GEAR's generalist **humanoid whole-body controller**, and the concrete controller behind the **`UNITREE_G1_SONIC`** embodiment tag in [Isaac-GR00T](../sources/isaac-gr00t-github.md). Primary source: [SONIC paper](../sources/sonic-paper.md) (arXiv 2511.07820); code `NVlabs/GR00T-WholeBodyControl`; checkpoints `nvidia/GEAR-SONIC`. Resolves the "GEAR-SONIC controller" gap flagged during the GR00T whole-body-control ingest.

## Core idea
**Motion tracking is the scalable foundational task** for humanoid control (dense per-frame mocap supervision that survives dataset scaling, unlike adversarial imitation). A single PPO motion-tracking policy scaled across model / data / compute (1.2M→42M params; ~700 h mocap → 611 h / 100M+ frames; ~2K→21K GPU-hrs) yields a robust, natural, zero-shot-generalizing [Unitree G1](unitree-g1.md) controller with direct sim-to-real.

## The VLA interface (why GR00T needs it)
SONIC exposes a **universal token action space** (FSQ-quantized) that decouples the low-level controller from the high-level policy. A [GR00T N1.5](../sources/groot-n1_5.md) VLA predicts a **78-dim action = 64-dim universal motion token + 14 hand joints**, which SONIC decodes into whole-body motor commands — enabling **autonomous whole-body loco-manipulation** (5-task avg 75%). Predicting tokens beats predicting SMPL poses by +42 points. This is the mechanism behind GR00T N1.7's `UNITREE_G1_SONIC` whole-body support.

## Headline numbers
- 42M model: 99.6% success / 23.8 mm MPJPE (OOD); 41% MPJPE reduction vs BeyondMimic; 98.5% survival vs OpenHomie's 43% at high speed; sim-to-real 99.2%.
- Runs onboard [Jetson Orin](jetson-orin-nano.md) at 1–2 ms/forward (TensorRT + CUDA Graph), policy 50 Hz.
- Public **BONES-SEED** motion dataset (142,220 sequences / 288 h / 522 actors) on HF.

## Related
- [NVIDIA GR00T](nvidia-groot.md) — SONIC is the whole-body controller under GR00T N1.5/N1.6/N1.7 (`UNITREE_G1_SONIC`).
- [Unitree G1](unitree-g1.md) — the target robot; SONIC is why G1 is GR00T's whole-body embodiment.
- [NVIDIA GEAR](nvidia-gear.md) — originating lab.
- [VQ-BeT](vq-bet.md) — a cousin in the "discrete latent action space" idea (FSQ vs VQ codebook), here for whole-body control rather than manipulation BC.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md), [VLA models](../concepts/learning/vla-models.md).

## Mentioned in
- [SONIC Paper](../sources/sonic-paper.md) — primary source.
- [Isaac-GR00T GitHub](../sources/isaac-gr00t-github.md) — `UNITREE_G1_SONIC` tag + GEAR-SONIC controller.

## Open questions
- Extension to other humanoids beyond [Unitree G1](unitree-g1.md) (paper is G1-only; no Fourier GR-1).
- Safety/energy for extended deployment; foot-placement sim-to-real gap.
