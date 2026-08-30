---
title: EchoWorld
type: entity
subtype: model
created: 2026-08-30
updated: 2026-08-30
sources: 2
tags: [jepa, action-conditioned, world-model, probe-guidance, medical-robotics, imitation-learning, 6-dof, tsinghua, cvpr-2025, open-source]
---

**EchoWorld** — an **action-conditioned [JEPA](../concepts/world-models/jepa.md)** for **robotic ultrasound probe guidance**, from Tsinghua's LeapLab (Gao Huang) with PLA General Hospital. CVPR 2025; [paper](../sources/echoworld-paper.md); code at [github.com/LeapLabTHU/EchoWorld](https://github.com/LeapLabTHU/EchoWorld).

**A robot-learning system in medical clothing.** Demonstrations are collected by sonographers manoeuvring a probe **mounted on a robotic arm**, with images and **6-DOF pose** recorded synchronously; the policy is behaviour cloning that predicts the relative rigid-body movement to reach one of ten standard cardiac imaging planes.

## Why it is in this wiki

- **Its motion world-modeling objective makes the action the JEPA latent.** Given two frames and the 6-DOF probe movement between them, predict the target's features. That is the [V-JEPA 2-AC](v-jepa-2.md) idea, contemporaneous, independent, in a real robotic domain, with released code.
- **It argues against interleaved image-action token sequences.** Rather than `{I₁, a₁, I₂, a₂, …}` through a causal transformer — the [Decision Transformer](../concepts/learning/vla-models.md) convention most [VLAs](../concepts/learning/vla-models.md) inherit — it injects **pairwise relative pose into the attention keys and values**. Beats Decision Transformer 7.44 → **7.05** with the same backbone.
- **Its ablation says proprioception beats pretraining.** Access to motion history is worth ~1.0; swapping in the world-model backbone is worth ~0.5. The headline contribution is the smaller effect, and the paper reports it.

## Numbers

| Protocol | Result (mean absolute error, mm + degrees, lower better) |
|---|---|
| Single-frame (representation quality) | **8.15**, vs EchoCLIP 8.37, USFM 8.42, DINOv2 8.52, scratch 9.07 |
| Sequential (guidance architecture, shared backbone) | **7.05**, vs Sequence-aware 7.42, Decision Transformer 7.44, US-GuideNet 7.72 |

Data: **356 clinical scans, ~1M frames**, 284/72 train/test split with no patient overlap, ViT-Small, 300 epochs on 4× A100.

> [!warning] Entirely open-loop
> Both protocols score prediction error against a recorded expert's movement on recorded scans. **No closed-loop control, no phantom, no patient.** 7.05 does not mean the probe reaches the plane. See the [source page](../sources/echoworld-paper.md).

## Mentioned in

- [EchoWorld paper](../sources/echoworld-paper.md)
- [EchoJEPA paper](../sources/echojepa-paper.md) — cites it in related work as the probe-guidance counterpart to its own diagnostic model.

## Open questions / TBD

- **Does motion-aware attention beat token interleaving on a standard robot benchmark?** The code is released; LIBERO or DROID would settle it.
- **Closed-loop performance** is the number that matters and does not exist.
- **No cross-comparison with [EchoJEPA](echojepa.md)** — two echocardiography JEPAs, different groups, different tasks, no shared benchmark.
