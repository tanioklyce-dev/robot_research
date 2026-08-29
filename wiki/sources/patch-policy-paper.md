---
title: "Patch Policy: Efficient Embodied Control via Dense Visual Representations"
type: source
url: https://arxiv.org/abs/2607.18236
local_path: raw/patch-policy_2607.18236.pdf
sha256: 9c4c9a5416831e337a9b76ac5edd6f0c2cc8746ec7b76f582565b53b2d37b919
author: Gaoyue Zhou, Zichen Jeff Cui, Ada Langford, Bowen Tan, Yann LeCun, Lerrel Pinto
published: 2026-07-20
ingested: 2026-08-26
venue: arXiv (cs.RO, cs.LG)
format: paper (27 pp)
tags: [robot-learning, visuomotor-policy, dense-features, dinov2, webssl, vq-bet, diffusion-policy, openvla, latency, vla, lecun, lerrel-pinto]
---

# Patch Policy: Efficient Embodied Control via Dense Visual Representations

## Summary

The most directly useful of the LeCun August-2026 batch for this wiki. Argues that robot policies face a false choice: compress each observation to a **single global token** (CLS or average-pool) and lose spatial detail, or consume **dense patch tokens** and pay for a billion-parameter VLM backbone. **Patch Policy** is a minimal architectural fix — a **block-causal attention mask** that lets a standard transformer policy attend over many patch tokens per observation while preserving the temporal causality of a normal policy — applied on top of a **frozen** pretrained ViT. The result beats a fine-tuned [OpenVLA-OFT](../entities/openvla.md) on all four simulated suites and all three real-robot tasks, at **~0.7% of its total parameters** and **10.99 ms** inference latency.

## Key claims

### The headline comparison

| | Total params | Trainable params | Inference latency |
|---|---:|---:|---:|
| **Patch Policy — VQ-BeT (DINOv2)** | **51.55M** | 29.49M | **10.99 ms** |
| Patch Policy — Diffusion Policy (DINOv2) | 40.43M | 9.19M | **445.85 ms** |
| ACT (ResNet-18) | — | — | 8.63 ms |
| **OpenVLA-OFT** | **7.61B** | 177.90M | **61.71 ms** |

Training cost: **6.5 GPU-hours** (1×L40S) vs OpenVLA-OFT's 16 GPU-hours (4×L40S) and ACT's 24 GPU-hours (2×L40S).

> [!warning] The speed claim and the accuracy claim belong to different heads
> The 10.99 ms figure is the **VQ-BeT** head. The **Diffusion Policy** head — which posts the better simulated numbers on Push-T (0.80 vs 0.68) and LIBERO Goal (0.98 vs 0.94) — runs at **445.85 ms**, roughly **40× slower** and far outside any reactive control loop. The paper's framing ("high-frequency, reactive control") holds only for the VQ-BeT variant. Anyone reading this as "dense patch features are now free" should check which row they mean. See [control-rate ladder](../syntheses/platforms/control-rate-ladder.md).

### Simulated results (100 trajectories per seed, 3 seeds)

Push-T (target coverage), LIBERO Goal (success rate), BlockPush / Cube (avg objects placed):

| Visual representation | Policy | Push-T | LIBERO Goal | BlockPush | Cube |
|---|---|---|---|---|---|
| WebSSL Avg Pool | VQ-BeT | 0.54 | 0.97 | 0.84 | 0.25 |
| WebSSL CLS | VQ-BeT | 0.59 | 0.95 | 0.77 | 0.23 |
| WebSSL Avg Pool | Diffusion Policy | 0.79 | 0.98 | 1.34 | 0.21 |
| **WebSSL Patch (ours)** | **VQ-BeT** | 0.68 | 0.94 | **1.68** | **1.68** |
| **WebSSL Patch (ours)** | **Diffusion Policy** | **0.80** | **0.98** | 1.65 | **1.73** |
| ResNet-18 Patch | ACT | 0.64 | 0.93 | 0.15 | 0.69 |
| DINOv2+SigLIP Patch | OpenVLA-OFT | 0.59 | 0.95 | 1.43 | 1.50 |

**Where the gain actually is:** BlockPush and Cube — the **multi-object / spatial** tasks — where patch features take VQ-BeT from 0.23–0.25 to **1.68**. On LIBERO Goal every method sits at 0.93–0.98; the benchmark discriminates nothing here, exactly as [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) predicts of a saturated suite.

> [!note] Two comparability caveats the paper flags itself
> The OpenVLA-OFT **LIBERO Goal** number is *"reported directly as provided in the original manuscript,"* not re-run in this harness. And the claim that Patch Policy "outperforms fine-tuned OpenVLA-OFT on all four environments" holds for the Diffusion Policy head; the VQ-BeT head is **0.94 vs 0.95** on LIBERO Goal — a tie at best.

### Real-robot results (7-DoF Franka, 20 trials, cumulative success through stages)

| Task | Method | Stage 1 | Stage 2 | Stage 3 |
|---|---|---|---|---|
| Cable Insertion | **DINOv2 Patch VQ-BeT (ours)** | 1.00 | **0.85** | **0.70** |
| | DINOv2 CLS VQ-BeT | 1.00 | 0.70 | 0.60 |
| | DINOv2+SigLIP Patch OpenVLA-OFT | 1.00 | 0.55 | 0.30 |
| Task 2 | **ours** | 1.00 | **1.00** | **0.85** |
| | DINOv2 CLS VQ-BeT | 1.00 | 0.95 | 0.65 |
| | OpenVLA-OFT | 1.00 | 0.85 | 0.60 |
| Task 3 | **ours** | 1.00 | **0.90** | **0.90** |
| | DINOv2 CLS VQ-BeT | 1.00 | 0.75 | 0.70 |
| | OpenVLA-OFT | 0.95 | 0.90 | 0.65 |

> [!warning] n = 20 per cell
> At 20 trials the 95% Clopper-Pearson band is roughly **±20 percentage points**. The **0.70 vs 0.30** Cable Insertion gap survives that comfortably; **0.90 vs 0.70** and **0.85 vs 0.65** do not. Read the direction, not the ordering of close pairs — the wiki's standing rule from the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md). The paper does not report confidence intervals.

### The backbone comparison — the most reusable result here

Five frozen pretrained encoders swept across all tasks, three seeds, encoder frozen so this isolates out-of-the-box representation quality: **[DINOv2](../entities/dinov2.md), [DINOv3](../entities/dinov3.md), WebSSL, [V-JEPA 2](../entities/v-jepa-2.md), SigLIP 2.**

- **WebSSL and DINOv2 are the best** across the majority of tasks; the paper's explicit recommendation is *"use WebSSL or DINOv2 as the vision backbones for robot learning tasks."*
- **SigLIP 2 falls short across the environments.** The offered explanation: its "emphasis on semantic language–image alignment sacrifices the dense geometric features necessary for manipulation." For tasks prioritizing spatial reasoning over linguistic understanding, vision-language grounding is *"a less effective signal for policy learning."*
- **The ranking of representations is stable across policy architectures** for a given task, and the average ranking is stable across the whole suite. The paper's inference: **"the quality of the visual representation is still a primary bottleneck for policy learning, independent of the downstream action head."**

> [!note] V-JEPA 2 is evaluated as a policy backbone and does not win
> The wiki holds [V-JEPA 2](../entities/v-jepa-2.md) as the flagship large-scale JEPA encoder (1B params, 1M+ hours of video, zero-shot Franka manipulation). Here, frozen and used as a patch-feature source for behavior-cloning policies, it is beaten by DINOv2 and WebSSL. That is a narrow test — one usage mode, no action-conditioned predictor, frozen — and it does not touch V-JEPA 2's own zero-shot planning claims. But it is a datapoint the wiki did not have: **as a frozen dense-feature extractor for imitation-learned control, video-pretrained JEPA features are not the best available.**

### Method

- Patch tokens from a **frozen** ViT are flattened into the sequence alongside other state information; a **block-causal attention mask** gives patches full bidirectional attention *within* an observation while preserving causality *across* time. At inference, patch features from the current observation are appended to a rolling buffer.
- Freezing the encoder lets visual embeddings be **precomputed**, which is where much of the training-speed advantage comes from.
- Heads tested: **VQ-BeT** and **Diffusion Policy**. Baselines: DynaMo (global features), ACT, OpenVLA-OFT.

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md), [Lerrel Pinto](../entities/lerrel-pinto.md) — NYU.
- [OpenVLA](../entities/openvla.md) / OpenVLA-OFT — the baseline beaten.
- [V-JEPA 2](../entities/v-jepa-2.md), [DINOv2](../entities/dinov2.md) — backbones compared.
- [Diffusion Policy](../entities/diffusion-policy.md), [ACT](../entities/act.md), [LIBERO](../entities/libero.md).
- [DINOv3](../entities/dinov3.md), [VQ-BeT](../entities/vq-bet.md) — existing pages.
- [WebSSL](../entities/webssl.md), [SigLIP 2](../entities/siglip-2.md), [DynaMo](../entities/dynamo.md) — **all filed 2026-08-26**, WebSSL and DynaMo with their primaries.
- **Patch Policy** — [entity page](../entities/patch-policy.md).
- [SigLIP / SigLIP 2](../entities/siglip.md) — falls short as a frozen policy backbone — semantic alignment over dense geometry.
- [WebSSL](../entities/webssl.md) — the best-performing frozen backbone in the sweep, and the paper’s recommendation.
- [DynaMo](../entities/dynamo.md) — the in-domain-pretraining baseline it beats on spatial tasks.
- [SigLIP 2](../entities/siglip-2.md) — weakest of the five frozen backbones.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — the direct challenge: a 51M-parameter policy beating a 7.6B VLA in-domain.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — n = 20 real trials; LIBERO Goal saturation.
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) / [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) — the 10.99 ms vs 445.85 ms split.

## Open questions

- **In-domain only.** The paper's own framing of the OpenVLA-OFT result is *"for **in-domain** tasks with sufficient demonstrations, a lightweight policy on strong features can match or exceed a heavy pretrained VLA fine-tuned on the same data."* Nothing here tests language generalization, novel objects, or instruction following — the things a 7.6B VLA is *for*. A 51M model beating a 7.6B model on the 7.6B model's fine-tuning distribution is a real result about parameter efficiency, not evidence that VLA pretraining is unnecessary.
- **No language axis at all** — "all policies receive only visual inputs," and proprioception was removed from ACT's encoder for consistency. LIBERO Goal is the only multi-task suite.
- **No confidence intervals anywhere**, and n = 20 on the real robot.
- ~~WebSSL / SigLIP 2 / DynaMo unfiled~~ — **all filed 2026-08-26**. The [WebSSL primary](webssl-paper.md) also resolved an identity the wiki had missed: **WebSSL's DINO member is Web-DINO**, which [action-relevant latents](action-relevant-latents-paper.md) measures at 0.16 action R² with negative rotation. **The encoder this paper recommends for policies is one of the worst measured choices for a latent world model.**
