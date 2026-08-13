---
title: "TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM"
type: source
url: https://arxiv.org/abs/2607.27205
local_path: raw/2607.27205.pdf
author: Hengyi Xie, Chenfei Yao, Xianjin Wu, Xuanyang Xi, Yiping Tang, Di Xu, Yingying Zhu, Dingkang Liang, Xiang Bai, Han Ding
venue: arXiv preprint (cs.CV, cs.RO), 16 pp.
published: 2026-07-29
ingested: 2026-08-04
format: pdf
tags: [vla, efficient-inference, inference-latency, libero, robotwin, dinov3, bert, cross-attention, action-chunking, act, grounding-dino, edge-ai, huazhong, huawei, agilex-piper, bimanual]
---

# TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM

**Xie, Yao, Wu, Xi, Tang, Xu, Zhu, [Liang](../entities/dingkang-liang.md), [Bai](../entities/xiang-bai.md), Ding** — [Huazhong University of Science and Technology](../entities/hust.md) + [Huawei](../entities/huawei.md). Code: [H-EmbodVis/TurboVLA](https://github.com/H-EmbodVis/TurboVLA); project page [H-EmbodVis.github.io/TurboVLA](https://H-EmbodVis.github.io/TurboVLA).

## Summary

Every VLA in this wiki routes perception through a language model before emitting actions — what the paper names the **V→L→A pathway**. TurboVLA asks whether the `L` stage is load-bearing at *execution* level, and answers no. It encodes images with [DINOv3](../entities/dinov3.md) and the instruction with **BERT**, exchanges information between the two streams through six layers of **bidirectional cross-attention** borrowed from [Grounding DINO](../entities/grounding-dino.md), and decodes a continuous action chunk with an [ACT](../entities/act.md)-style transformer — **no LLM anywhere in the control loop**. The result is 0.2 B parameters, **0.9 GB inference VRAM**, and **31.2 ms latency (32 Hz) on a consumer RTX 4090**, at **97.7% average [LIBERO](../entities/libero.md)** — inside the top statistical tier while using ~6% of [π0.5](../entities/pi-zero-5.md)'s parameters and a third of its latency. The paper's own framing is a challenge to the field: *"execution-level control does not necessarily require a general-purpose LLM as the central interface between perception and action."*

> [!note] What is and isn't new here
> Small VLAs are not new ([SmolVLA](../entities/smolvla.md) 450 M, [Evo-1](../entities/evo-1.md) 0.8 B, VLA-Adapter 1.5 B), and neither is fast action decoding ([OpenVLA-OFT](../entities/openvla-oft.md)'s parallel decoding). What is new is **deleting the generative language backbone entirely** rather than shrinking, pruning, quantizing, or distilling it. The paper explicitly separates these: "neither accelerating action generation nor reducing model scale alone is sufficient."

## Key claims

### Architecture (§4)

- **V+L→A, not V→L→A.** Vision and language are encoded *independently* and fused directly; there is no shared language-model latent space acting as the bridge. Formally, LLM-centric VLAs compute `H_n^L = F_L[P_v(E_v(O_n)); Tok(x)]` and decode actions from `H_n^L`; TurboVLA never forms `H_n^L`.
- **Encoders (§4.1)** — [DINOv3](../entities/dinov3.md) ViT-B (LIBERO) / ViT-L (RoboTwin) for vision; **BERT** for text. Both project to a shared `d = 256`. The **full instruction token sequence is retained rather than pooled**, so objects, attributes, and spatial relations stay available for fine-grained visual conditioning. Multi-camera streams get per-view positional + camera-view embeddings and are concatenated.
- **Robot state is routed around the fusion module.** `Z^s_n` is encoded separately and injected only at the action decoder — deliberately keeping cross-modal interaction focused on task-conditioned *scene* understanding rather than embodiment configuration.
- **Vision-language interaction (§4.2)** — `N = 6` layers of LayerNorm → bidirectional cross-attention → per-modality FFN with residuals. Visual-to-instruction attention injects scene context into the text stream; instruction-to-visual attention conditions vision on task semantics. Initialized from **grounding-pretrained feature-enhancement weights** ([Grounding DINO](../entities/grounding-dino.md)) — the one place the model inherits large-scale pretraining, and it is *grounding* pretraining, not language-generation pretraining.
- **Action decoder (§4.3)** — [ACT](../entities/act.md)-style transformer over `H` learnable action queries, all decoded in parallel in one forward pass. Trained by plain behavior cloning with an **ℓ1 loss and no auxiliary language-modeling objective**. `H = 12` on LIBERO, 50 on RoboTwin.

### Results

**LIBERO (§5.3, Table 1)** — 50 rollouts/task × 10 tasks × 4 suites = **n = 2,000**, VLA-Adapter rollout protocol, one jointly-trained mixed-suite model, OpenVLA `no_noops` RLDS data.

| | Params (B) | VRAM (GB) | Latency (ms) | Spa. | Obj. | Goal | Long | **Avg** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **TurboVLA** | **0.2** | **0.9** | **31.2** | 99.2 | 99.8 | 97.4 | 94.2 | **97.7** |
| CogVLA | 8.3 | 16.1 | 115.5 | 98.6 | 98.8 | 96.6 | 95.4 | 97.4 |
| VLA-Adapter | 1.5 | 4.3 | 87.3 | 97.8 | 99.2 | 97.2 | 95.0 | 97.3 |
| [VLA-JEPA](../entities/vla-jepa.md) | 2.8 | 5.3 | 108.7 | 96.2 | 99.6 | 97.2 | 95.8 | 97.2 |
| [OpenVLA-OFT](../entities/openvla-oft.md) | 7.7 | 15.7 | 112.2 | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 |
| [π0.5](../entities/pi-zero-5.md) | 3.4 | 12.8 | 93.6 | 98.8 | 98.2 | 98.0 | 92.4 | 96.9 |
| DDVLA | 7.5 | 14.5 | 60.8 | 97.2 | 99.4 | 96.8 | 92.2 | 96.4 |
| [Evo-1](../entities/evo-1.md) | 0.8 | 1.7 | 137.2 | 92.7 | 97.7 | 96.3 | 92.3 | 94.8 |
| [π0](../entities/pi-zero.md) | 3.2 | 12.3 | 84.2 | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 |
| [SmolVLA](../entities/smolvla.md) | 2.3 | 7.1 | 203.1 | 93.0 | 94.0 | 91.0 | 77.0 | 88.8 |
| [OpenVLA](../entities/openvla.md) | 7.5 | 14.9 | 202.9 | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 |
| [Diffusion Policy](../entities/diffusion-policy.md) | 0.3 | 1.1 | 924.8 | 78.3 | 92.5 | 68.3 | 50.5 | 72.4 |

Efficiency figures for all competitors were **re-measured by the authors** on one RTX 4090 at batch size 1 from official checkpoints — not copied from the original papers. Latency is defined input→action-chunk (or an equivalent number of autoregressive tokens).

> [!warning] The headline LIBERO comparison is a statistical tie; the efficiency comparison is not
> Per this wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), at n = 2,000 near 97% the minimum separating gap is ~1.0 pp. **TurboVLA 97.7 vs π0.5 96.9 → p = 0.12; vs OpenVLA-OFT 97.1 → p = 0.23; vs VLA-Adapter 97.3 → p = 0.42. All ties.** The paper's word "matching" is correct and its word "outperforming" is not supported at the top of the table.
>
> What *does* survive is the separation from the lightweight cohort — **vs Evo-1 94.8 (p < 0.001) and vs SmolVLA 88.8 (p < 0.0001)** — and, more importantly, the efficiency axis, where the gaps are 3–40× and are engineering measurements rather than sampled proportions. **The result is "top-tier success at 6% of the parameters," and the second clause is the one doing the work.**

**RoboTwin 2.0 bimanual (§5.3, Table 2)** — 50 language-conditioned dual-arm tasks, 100 clean-setting rollouts each (**n = 5,000**), single multi-task model, DINOv3 ViT-L, 14-dim absolute joint positions.

| | Params (B) | Latency (ms) | Avg success |
|---|---:|---:|---:|
| **TurboVLA** (multi-task) | **0.4** | **43.4** | **60.2%** |
| π0.5 (multi-task) | 3.4 | 95.6 | 57.0% |
| UP-VLA (multi-task) | 1.6 | 74.3 | 52.9% |
| StarVLA-α (multi-task) | 3.8 | 74.9 | 50.3% |
| DP3 (per-task) | 0.3 | 78.4 | 55.2% |
| π0 (per-task) | 3.2 | 87.6 | 46.4% |
| ACT (per-task) | 0.1 | 20.4 | 29.7% |

> [!note] This — not LIBERO — is the paper's statistically strongest success claim
> **60.2 vs π0.5's 57.0 at n = 5,000 gives p = 0.0012 — it survives.** The 3.2 pp gap is smaller than anything at the top of the LIBERO table, but the sample is 2.5× larger and the base rate is near 60% where variance is highest, so it separates where the LIBERO numbers don't. It is also the harder setting (50 bimanual tasks, one joint policy) and TurboVLA has **no embodied pretraining** while π0.5 does. The paper headlines the LIBERO tie and buries the RoboTwin win.

**Real-world (§5.2, Fig. 4)** — [AgileX Piper](../entities/agilex-piper.md) 6-DoF arm, wrist + third-person RealSense D435. Four tasks (grab roller / move playing card / press stapler / stack three bowls), fine-tuned from the LIBERO checkpoint on **4 × 65 teleop demos** for 12.5 k steps, **40 trials/task**. TurboVLA: **92.5% / 80% / 90% / 87.5%**, reported as beating π0.5 on all four under identical data and protocol.

> [!warning] n = 40 cannot support the real-world comparison
> Per the [audit](../syntheses/platforms/vla-success-rate-audit.md)'s power table, at 40 trials/arm near 85–90% success **nothing under roughly 17 pp is detectable**. π0.5's exact per-task values are only given as a bar chart, but the visible gaps are well inside that floor. "Consistently outperforming π0.5" is a directional observation across four tasks, not a measured win — and a 4-of-4 sign test is p = 0.125 even if every gap were real. The useful content here is that a 0.2 B LLM-free policy **works at all** on a real arm from 65 demos/task, not that it beats π0.5.

### Ablations (§5.4) — the most interesting part of the paper

These run at n = 2,000 on LIBERO and are, unusually, well-powered.

| Ablation | Result | Verdict at n=2,000 |
|---|---|---|
| **No language at all** | 97.7 → **70.8**; LIBERO-Goal collapses **97.4 → 11.6** | survives, overwhelmingly |
| **Learned task-ID embedding** instead of text | 95.4 (−2.3) | **survives** (p = 0.0001) |
| Text encoder: BERT 97.7 / T5-small 97.1 / SigLIP 95.5 | BERT vs T5 **tie** (p = 0.23); vs SigLIP survives | mixed — supports the "not tied to one encoder" claim |
| Interaction: none 95.2 → one-way 96.1 / 96.5 → **bidirectional 97.7** | +1.2 over best one-way | survives, marginally (p = 0.024) |
| Interaction depth `N`: 2 → 93.5, 4 → 95.7, **6 → 97.7**, 8 → 96.6 | +4.2 from N=2 to N=6 | N=2→6 survives; **N=6 vs N=8 is marginal (p = 0.037)** |
| Action horizon `H`: 8 → 96.4, 10 → 96.9, **12 → 97.7**, 15 → 95.6 | inverted-U | H=12 vs H=15 survives (p = 0.0002) |

Three things follow:

1. **Language is doing real work, and it is semantic.** Removing it costs 27 pp; replacing it with a closed-set task ID recovers most but leaves a *statistically real* 2.3 pp deficit. So natural language carries more than task identity even at execution level — which is the strongest counter to reading this paper as "language models don't matter for robots."
2. **The LIBERO-Goal collapse (97.4 → 11.6) is the cleanest demonstration in the wiki of what instruction conditioning buys.** Goal is the suite where the same scene supports multiple valid behaviors; without language, the policy has nothing to disambiguate with. The other three suites barely move (Object stays at 99.4), which is itself a comment on how much of LIBERO is solvable from visual priors alone.
3. **A BERT-sized encoder suffices.** BERT (216 M) and T5-small (142 M) are indistinguishable. The capability that matters is grounding instruction tokens to visual regions, not generation or reasoning.

### Compute footprint (recorded per the audit's standing request)

- **Training: four RTX 4090s.** LIBERO 80 k steps (10 k warmup, effective batch 256); RoboTwin 55 k steps (1 k warmup, batch 192); real-world fine-tune 12.5 k steps. LR 5×10⁻⁵ throughout.
- **Inference: 0.9 GB VRAM, 31.2 ms, batch size 1, single consumer GPU.**

This is the smallest training-compute disclosure of any top-tier LIBERO result in the wiki, and one of very few that a small lab could reproduce. It also means the LIBERO number was obtained **without embodied pretraining** ("Emb. PT. ✗" in Table 1) — trained on LIBERO demonstrations alone.

## Limitations the paper states

The conclusion is unusually candid: TurboVLA "is designed primarily for concrete execution-level instructions and may not provide the complex semantic understanding and reasoning required for high-level task planning." The proposed future direction is explicitly hierarchical — **LLM planner on top, TurboVLA-style executor underneath** — which is the same [System 1 / System 2](../concepts/learning/vla-models.md) split as [Helix](../sources/helix-blog.md) and [GR00T](../entities/nvidia-groot.md), with the novelty being how little the System-1 tier needs.

## Open questions

- **Does it survive [LIBERO-PRO](../sources/libero-pro-paper.md)?** This is the decisive test and it was not run. TurboVLA is arguably the model in the wiki **most exposed** to the memorization critique: 0.2 B parameters, no embodied pretraining, no web-scale language pretraining, trained on LIBERO demonstrations only. The web-scale semantic priors that LIBERO-PRO found insufficient in π0.5 are largely *absent* here by construction. The counter-hypothesis is that Grounding-DINO-pretrained cross-attention gives open-vocabulary object grounding that transfers under object swaps better than a language-model latent does. Both are plausible; the [VLA evaluation harness](vla-evaluation-harness-github.md) now makes the test cheap. **Until it is run, 97.7% means what every other number in that table means, which may be very little.**
- **Edge latency is unmeasured.** 31.2 ms is on a ~450 W desktop RTX 4090, not a Jetson. But **0.9 GB is the first VLA inference footprint in this wiki that fits an [Orin Nano](../entities/jetson-orin-nano.md) 8 GB with room to spare** — where GR00T-3B's 16 GB floor rules the board out entirely. See the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md); a measured Orin number would be the single most valuable follow-up for this wiki's [XLeRobot](../entities/xlerobot.md)/[SO-101](../entities/so-arm101.md) threads.
- **No cross-embodiment or open-world claim.** π0.5's headline is unseen homes; TurboVLA's evaluations are all in-distribution after fine-tuning. Removing the LLM plausibly removes exactly the semantic transfer that co-training was meant to buy — the paper does not test this, and the task-ID ablation hints the model does use semantics, but 4 tasks on one arm cannot settle it.
- **No released checkpoints yet confirmed.** The GitHub repo is announced in the paper; contents were not verified during this ingest.
- **Is `H = 12` at 32 Hz self-consistent?** A 12-step chunk re-predicted at 32 Hz means chunks overlap heavily; the paper does not describe an execution/replanning policy (open-loop chunk execution vs temporal ensembling vs [real-time chunking](../entities/fast-action-tokenization.md)). ACT normally executes the chunk before re-predicting, which would make the *effective* command rate lower than 32 Hz.

## Entities mentioned

- [RDT](../entities/rdt.md)
- [TurboVLA](../entities/turbovla.md) · [HUST](../entities/hust.md) · [Huawei](../entities/huawei.md) · [Xiang Bai](../entities/xiang-bai.md) · [Dingkang Liang](../entities/dingkang-liang.md)
- [DINOv3](../entities/dinov3.md) · [Grounding DINO](../entities/grounding-dino.md) · [ACT](../entities/act.md)
- [LIBERO](../entities/libero.md) · [RoboTwin 2.0](../entities/robotwin.md) · [AgileX Piper](../entities/agilex-piper.md)
- Compared against: [π0](../entities/pi-zero.md) · [π0.5](../entities/pi-zero-5.md) · [OpenVLA](../entities/openvla.md) · [OpenVLA-OFT](../entities/openvla-oft.md) · [SmolVLA](../entities/smolvla.md) · [VLA-JEPA](../entities/vla-jepa.md) · [Evo-1](../entities/evo-1.md) · [Diffusion Policy](../entities/diffusion-policy.md) · [UniVLA](../entities/univla.md)

## Concepts touched

- [LLM-free VLA (V+L→A)](../concepts/learning/llm-free-vla.md) — the paradigm this paper names and this wiki now tracks
- [VLA models](../concepts/learning/vla-models.md) — the taxonomy this adds a branch to
- [Imitation learning](../concepts/learning/imitation-learning.md) — plain behavior cloning, ℓ1, no auxiliary objectives
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — the paper's core argument is that *execution level* has different requirements than the planning level
