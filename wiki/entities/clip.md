---
title: CLIP
type: entity
subtype: model
created: 2026-08-30
updated: 2026-09-01
sources: 1
tags: [clip, openai, vision-language, contrastive, zero-shot, backbone, robustness]
---

**CLIP (Contrastive Language–Image Pre-training)** — OpenAI, ICML 2021 ([paper](../sources/clip-paper.md)). An image encoder and a text encoder trained jointly on **400M internet (image, text) pairs** so that matching pairs land near each other in a shared embedding space. At inference the **text encoder synthesizes a classifier** from class names, giving zero-shot transfer with no labelled examples and no output head.

**The mechanism by which language got attached to vision** — and therefore the ancestor of the "vision-language" half of every [VLA](../concepts/learning/vla-models.md).

## Why it is load-bearing here

- **Zero-shot ImageNet 76.2%**, matching the original ResNet-50 without using any of its 1.28M training examples. Prior work in this line reached 11.5%.
- **~12× training efficiency from choosing a weaker objective** — predicting the caption is 3× slower than a bag-of-words baseline; going contrastive buys a further 4×. Same lesson as [JEPA](../concepts/world-models/jepa.md) and [NPLM](../sources/bengio2003-neural-probabilistic-language-model.md): *pick the weakest objective that still forces the representation you want.*
- **Closes the robustness gap on 7 natural distribution shifts by up to 75%** — and reports that the benefit is "almost entirely gone" after full supervised fine-tuning, which is what every robot policy does to its backbone.
- **Prompt engineering is worth ~5 points**, comparable to 4× compute. The text side is a programmable interface, and its phrasing is an unswept hyperparameter in language-conditioned policies.

Downstream in this wiki: [CLIPort](cliport.md), the VLM backbones inside VLAs, EchoCLIP in the [echocardiography](../sources/echojepa-paper.md) line.

## Where it fails

Near-random on **counting**, satellite imagery (EuroSAT, RESISC45), tumour detection (PatchCamelyon), and synthetic benchmarks (CLEVR, MNIST, GTSRB). Zero-shot CLIP ≈ a 16-shot linear classifier on BiT-M features. The counting and spatial-relation failure is the one that matters for manipulation — CLIP's embedding is a bag of concepts, not a scene description with cardinality.

## Mentioned in

- [CLIP paper](../sources/clip-paper.md)
- [Gato paper](../sources/gato-paper.md) — the multimodal-tokenization contemporary.
- [DiT World-Action Model for AV Scene Prediction](../sources/dit-world-action-model-av-paper.md) — fourth of six on a nuScenes ego-action probe (steer RMSE 0.117), **behind DINOv2 and both V-JEPA2 variants**. Consistent with the wiki's running pattern: language alignment does not buy geometric or dynamical structure.

## Open questions / TBD

- **What robot fine-tuning costs in effective robustness** — CLIP says the gain largely vanishes under supervision, and nobody has measured it for policies.
- **OpenCLIP / LAION** — the open reproduction and datasets most robot policies actually use — are un-ingested.
