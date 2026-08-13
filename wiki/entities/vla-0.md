---
title: VLA-0
type: entity
subtype: vla-model
created: 2026-07-17
updated: 2026-07-17
sources: 2
tags: [vla, vision-language-action, action-as-text, nvidia, qwen, libero, so-100]
---

# VLA-0

**VLA-0** — an NVIDIA [vision-language-action model](../concepts/learning/vla-models.md) (Goyal, Hadfield, Yang, Blukis, Ramos; [paper](../sources/vla-0-paper.md), arXiv 2510.13054, Oct 2025) built on the premise of **zero modification to the base VLM**: actions are emitted as **plain text** — space-separated integers — using the VLM's native autoregressive text generation, with no action tokens, no vocabulary change, and no added action head. It defines a **fourth** VLA family ("action-as-text" / "Simple") alongside discrete-token, generative-action-head, and custom-architecture designs.

## Why it matters in this wiki

VLA-0 is the wiki's clearest "**the simplest thing works best, with the right recipe**" data point on the [VLA action-head design](../concepts/learning/vla-models.md#action-head-design-across-vlas) question. Every other VLA in the wiki's table adds machinery — flow-matching heads (π0, SmolVLA), diffusion, discrete action vocabularies (OpenVLA), custom tokenizers (π0-FAST) — and VLA-0 **beats all of them on [LIBERO](libero.md) when trained on the same data**, and beats several *large-scale-pretrained* models (π0, [GR00T-N1](nvidia-groot.md), Octo, MolmoAct) despite having **no action pretraining at all**. It rhymes with the wiki's recurring "engineering-recipe-beats-scale" findings ([SmolVLA](smolvla.md) > π0 on real SO-100; [RUM](robot-utility-models.md) data-diversity; Mobile ALOHA co-training) — here the recipe is action-text ensembling + masking, not a bigger model.

## Key facts

- **Backbone:** unmodified **[Qwen2.5-VL-3B](qwen.md)**; method claimed VLM-agnostic (only one backbone reported).
- **Action representation:** continuous actions normalized to an integer range (resolution **1000** optimal) and generated as space-separated text; `H × D` integers per prediction. Arbitrary resolution without vocabulary changes.
- **Critical recipe (all three needed):** (1) **prediction ensembling** ([ACT](act.md)-style action-chunk averaging, **+2.0 pts** — the biggest lever); (2) **masked action augmentation** (mask target-string characters in training, **+1.2 pts**); (3) integer action decoding.
- **Training:** full fine-tune, cross-entropy over the vocabulary, 64 epochs, batch 192, LR 5e-6, ~32 h on 8× A100.
- **LIBERO:** avg **94.7** (Spatial 97.0 / Object 97.8 / Goal 96.2 / Long 87.6) — **rank 1.0** among no-pretraining models; rank 2.8 vs. all models, 2nd only to OpenVLA-OFT.
- **Real:** SO-100 + [LeRobot](lerobot.md); **+12.5 pts over [SmolVLA](smolvla.md)** across 4 tasks; ~**4 Hz** inference on a single RTX 5090 (unquantized PyTorch).
- **Open/reproducible:** code + models at vla0.github.io.

## Limitations

- **Inference speed** — action-as-text pays a token-generation cost; 4 Hz is slow for reactive control (distillation/quantization left as future work), where fixed-size flow-matching heads are cheaper.
- **No large-scale pretraining tested** — its headline comparison is un-pretrained; whether the design scales with action pretraining (to challenge OpenVLA-OFT) is open.

## Related

- [VLA models](../concepts/learning/vla-models.md) — the concept; VLA-0 is the "action-as-text" entry.
- [OpenVLA](openvla.md) / [OpenVLA-OFT](openvla-oft.md) — discrete-token family; OFT (custom architecture) is the only pretrained model above VLA-0 on LIBERO.
- [SmolVLA](smolvla.md) / [π0](pi-zero.md) — generative-action-head family VLA-0 outperforms.
- [ACT](act.md) — source of the ensembling trick.
- [Qwen](qwen.md) — the backbone VLM.

## Mentioned in

- [VLA-0 paper](../sources/vla-0-paper.md) — the introducing source (NVIDIA, arXiv 2510.13054).
