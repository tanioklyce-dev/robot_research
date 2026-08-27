---
title: Patch Policy
type: entity
subtype: model
created: 2026-08-26
updated: 2026-08-26
sources: 1
tags: [visuomotor-policy, dense-features, patch-tokens, dinov2, webssl, vq-bet, openvla, latency, robot-learning, lecun, lerrel-pinto]
---

**Patch Policy** — a minimal architectural extension letting a transformer-based robot policy consume **dense pretrained ViT patch tokens** directly, without a VLM backbone. Core mechanism: a **block-causal attention mask** giving patches full bidirectional attention *within* an observation while preserving causality *across* time. The vision encoder is **frozen**, so embeddings can be precomputed. Zhou, Cui, Langford, Tan, [LeCun](yann-lecun.md), [Pinto](lerrel-pinto.md) (NYU), July 2026 ([paper](../sources/patch-policy-paper.md)).

## The efficiency result

| | Total params | Trainable | Latency |
|---|---:|---:|---:|
| **Patch Policy — VQ-BeT (DINOv2)** | **51.55M** | 29.49M | **10.99 ms** |
| Patch Policy — Diffusion Policy (DINOv2) | 40.43M | 9.19M | 445.85 ms |
| ACT (ResNet-18) | — | — | 8.63 ms |
| [OpenVLA-OFT](openvla.md) | 7.61B | 177.90M | 61.71 ms |

Training: **6.5 GPU-hours** vs OpenVLA-OFT's 16 and ACT's 24.

> [!warning] The fast head and the accurate head are different rows
> 10.99 ms is **VQ-BeT**. The **Diffusion Policy** head posts the better simulated Push-T (0.80 vs 0.68) and LIBERO Goal (0.98 vs 0.94) numbers at **445.85 ms** — ~40× slower, outside any reactive loop. The "high-frequency, reactive control" framing applies to the VQ-BeT variant only. See [control-rate ladder](../syntheses/platforms/control-rate-ladder.md).

## Where the gain actually lives

Patch features help most on **multi-object / spatial** tasks: VQ-BeT goes from 0.23–0.25 (CLS or avg-pool) to **1.68** on BlockPush and Cube. On LIBERO Goal everything sits at 0.93–0.98 — a saturated suite that discriminates nothing, exactly as [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) predicts.

Real robot (7-DoF Franka, **20 trials**, cumulative through stages): beats fine-tuned OpenVLA-OFT on all three tasks, most clearly on **Cable Insertion, 0.70 vs 0.30**. At n=20 the 95% band is ~±20 pp, so that gap survives and the closer ones (0.90 vs 0.70) do not.

## The backbone finding, which is the reusable part

Five frozen encoders swept across all tasks, 3 seeds: **DINOv2, DINOv3, WebSSL, [V-JEPA 2](v-jepa-2.md), SigLIP 2.**

- **WebSSL and DINOv2 win**; the paper recommends them for robot learning.
- **SigLIP 2 falls short** — "emphasis on semantic language-image alignment sacrifices the dense geometric features necessary for manipulation."
- **Representation ranking is stable across policy architectures**, from which: *"the quality of the visual representation is still a primary bottleneck for policy learning, independent of the downstream action head."*

> [!note] V-JEPA 2 loses as a frozen policy backbone
> Narrow test — frozen, no action-conditioned predictor, imitation learning only — and it does not touch [V-JEPA 2](v-jepa-2.md)'s own zero-shot planning claims. But as a dense-feature source for behavior cloning, video-pretrained JEPA features lose to DINOv2 and WebSSL.

## The claim it does and does not support

> [!warning] In-domain only
> The paper's own wording: *"for **in-domain** tasks with sufficient demonstrations, a lightweight policy on strong features can match or exceed a heavy pretrained VLA fine-tuned on the same data."* All policies here receive **visual input only** — no language axis at all. A 51M model beating a 7.6B model on that model's own fine-tuning distribution is a result about **parameter efficiency**, not evidence that [VLA](../concepts/learning/vla-models.md) pretraining is unnecessary. What a big VLA is *for* — language generalization, novel objects, instruction following — is untested here.

## Related

- [OpenVLA](openvla.md) — the baseline beaten in-domain.
- [V-JEPA 2](v-jepa-2.md) / [DINOv2](dinov2.md) — backbones compared.
- [Diffusion Policy](diffusion-policy.md) / [ACT](act.md) / [LIBERO](libero.md).
- [VLA models](../concepts/learning/vla-models.md) — the class it undercuts on cost.
- [Lerrel Pinto](lerrel-pinto.md) / [Yann LeCun](yann-lecun.md).

## Mentioned in

- [Patch Policy paper](../sources/patch-policy-paper.md)
