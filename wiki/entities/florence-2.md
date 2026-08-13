---
title: Florence-2
type: entity
subtype: model
created: 2026-08-13
updated: 2026-08-13
sources: 2
tags: [florence-2, vlm, vision-language-model, microsoft, backbone, xvla]
---

**Florence-2** — Microsoft's unified vision-language model (Xiao et al., 2024), trained on the FLD-5B corpus with a single prompt-conditioned sequence-to-sequence interface spanning captioning, grounding, detection, and segmentation. Small by VLM standards (Base ≈ 0.23 B, Large ≈ 0.77 B).

## Why it appears in this wiki

Florence-2-Large is the **vision-language encoder inside [X-VLA](x-vla.md)** ([paper](../sources/xvla-paper.md), App. C), and Florence-2-Base is the encoder used throughout its preliminary heterogeneity study. X-VLA's design uses it asymmetrically: the **main fixed-camera view plus the language instruction** go through Florence-2, while **auxiliary wrist views bypass it** and go to a shared ViT, "as current VLMs have limited multi-view perception."

This is a notably smaller and older backbone than the VLA field's defaults — PaliGemma in [π0](pi-zero.md), Gemma3 in [π0.7](pi07.md), Eagle-2 then Cosmos in [GR00T](nvidia-groot.md), SmolVLM-2 in [SmolVLA](smolvla.md) — and X-VLA's results are the wiki's strongest evidence that **backbone choice is not where cross-embodiment VLA performance comes from**. A 0.9 B model on a 2024 Florence-2 encoder beats 7–9 B models on five of six benchmarks; the difference is [soft-prompt conditioning](../concepts/learning/soft-prompt-cross-embodiment.md) and the data recipe, not the VLM.

A vendored `modeling_florence2.py` ships inside [LeRobot](lerobot.md)'s `xvla` policy directory.

## Second appearance: as a robot-stack VLM

[DimOS](dimos.md) ships Florence-2 as one of four interchangeable VLM backends in `dimos/models/vl/` alongside Moondream (local and hosted), Qwen, and OpenAI ([repo](../sources/dimos-github.md)) — loaded through `transformers` with `trust_remote_code`. Worth noting because the two uses are unrelated in kind: [X-VLA](x-vla.md) uses Florence-2 as a **frozen-ish encoder inside a policy**, DimOS uses it as a **queryable perception service** an LLM agent calls. The same 2024 model serves both the highest-performing cross-embodiment VLA in the wiki and a production robot stack's scene-understanding tier, which says something about how much headroom small VLMs still have in robotics.

## Related

- [X-VLA](x-vla.md) — the VLA built on it
- [VLA models](../concepts/learning/vla-models.md) — backbone comparison across the family
- [DimOS](dimos.md) — uses it as an agent-callable perception service

## Mentioned in

- [X-VLA paper](../sources/xvla-paper.md)
- [DimOS GitHub repository](../sources/dimos-github.md)
