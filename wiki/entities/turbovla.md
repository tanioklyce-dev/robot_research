---
title: TurboVLA
type: entity
subtype: model
created: 2026-08-04
updated: 2026-08-04
sources: 1
tags: [vla, turbovla, efficient-inference, llm-free-vla, dinov3, bert, cross-attention, act, libero, robotwin, hust, huawei]
---

**TurboVLA** — a 0.2 B-parameter [VLA](../concepts/learning/vla-models.md) from [HUST](hust.md) + [Huawei](huawei.md) that **removes the language model from the control loop entirely**, reaching **97.7% average [LIBERO](libero.md) at 31.2 ms / 0.9 GB VRAM on a consumer RTX 4090** ([paper](../sources/turbovla-paper.md), 2026-07-29). The reference implementation of the [LLM-free V+L→A paradigm](../concepts/learning/llm-free-vla.md).

## Architecture

| Component | Choice |
|---|---|
| Vision encoder | [DINOv3](dinov3.md) ViT-B (LIBERO) / ViT-L (RoboTwin), + per-view positional & camera embeddings |
| Text encoder | **BERT** (216 M) — full token sequence retained, not pooled |
| Fusion | **6 layers of bidirectional cross-attention**, init from [Grounding DINO](grounding-dino.md) feature-enhancement weights |
| Robot state | separate lightweight projection, injected **only at the decoder** |
| Action head | [ACT](act.md)-style transformer, `H` learnable queries decoded in parallel, ℓ1 behavior cloning |
| Chunk size | `H = 12` (LIBERO, 7-DoF) / 50 (RoboTwin, 14-dim absolute joint) |
| Shared dim | `d = 256` |

No autoregressive decoding, no flow matching, no diffusion, no action tokenizer, and **no auxiliary language-modeling objective**.

## Measured numbers

| Benchmark | N | Result | Against |
|---|---:|---|---|
| [LIBERO](libero.md) 4-suite avg | 2,000 | **97.7%** | [π0.5](pi-zero-5.md) 96.9, [OpenVLA-OFT](openvla-oft.md) 97.1 — **all ties** |
| [RoboTwin 2.0](robotwin.md), 50 bimanual tasks | 5,000 | **60.2%** | π0.5 57.0 — **survives**, p = 0.0012 |
| Real [AgileX Piper](agilex-piper.md), 4 tasks | 40/task | 92.5 / 80 / 90 / 87.5% | π0.5 — gaps below the n=40 detection floor |

**Efficiency: 0.2 B params, 0.9 GB inference VRAM, 31.2 ms (32 Hz), RTX 4090 batch 1.** Competitor efficiency figures in the paper were re-measured by the authors on the same GPU rather than quoted. **Training used four RTX 4090s** (80 k steps on LIBERO) — the smallest disclosed training footprint of any top-tier LIBERO result in this wiki, and one obtained with **no embodied pretraining**.

## Why it matters

- **It is the wiki's first serious evidence that the `L` stage is optional at execution level.** Every other VLA here — [π-series](physical-intelligence.md), [GR00T](nvidia-groot.md), [OpenVLA](openvla.md), [SmolVLA](smolvla.md), [MolmoAct2](molmoact2.md), [VLA-0](vla-0.md) — routes actions out of a language-model representation. TurboVLA does not, and lands in the same LIBERO tier. See [LLM-free VLA](../concepts/learning/llm-free-vla.md).
- **It changes the shape of the efficiency frontier.** Prior efficiency work shrank, pruned, quantized, cached, or distilled the backbone. TurboVLA deletes it. The paper's line: *"neither accelerating action generation nor reducing model scale alone is sufficient."*
- **0.9 GB is the first VLA inference footprint in this wiki that comfortably fits an [Orin Nano](jetson-orin-nano.md) 8 GB** — the board that GR00T's 16 GB floor rules out. No edge measurement exists yet; see [control-rate ladder](../syntheses/platforms/control-rate-ladder.md).
- **Its ablation is the wiki's cleanest measurement of what instruction conditioning buys.** No language → 70.8% with LIBERO-Goal collapsing 97.4 → 11.6; a closed-set task ID recovers to 95.4 but stays a statistically real 2.3 pp short of semantic text. So language matters *and* a BERT-sized encoder is enough.

## Limitations

- **Execution-level only.** The authors state it "may not provide the complex semantic understanding and reasoning required for high-level task planning," and propose an LLM planner above a TurboVLA executor — the [System 1 / System 2](../concepts/learning/vla-models.md) split, with a much cheaper System 1.
- **Untested against [LIBERO-PRO](../sources/libero-pro-paper.md)**, and arguably the model most exposed to it: no embodied pretraining, no web-scale language priors, trained on LIBERO alone.
- **No cross-embodiment or open-world evaluation.** All real-world results are in-distribution after fine-tuning on 65 demos/task.
- **Effective command rate may be below 32 Hz** — a 12-step chunk at 32 Hz implies heavy overlap, and the chunk-execution/replanning policy is unspecified.

## Related
- [LLM-free VLA (V+L→A)](../concepts/learning/llm-free-vla.md) — the paradigm
- [VLA deployability landscape](../syntheses/platforms/vla-deployability-landscape.md) — where it sits on the four axes
- [Success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) — which of its claims survive
- [Evo-1](evo-1.md), [SmolVLA](smolvla.md) — the lightweight-VLA cohort it beats *separably*
- [Grounding DINO](grounding-dino.md) — architectural ancestor of the fusion module

## Mentioned in
- [TurboVLA paper](../sources/turbovla-paper.md)
