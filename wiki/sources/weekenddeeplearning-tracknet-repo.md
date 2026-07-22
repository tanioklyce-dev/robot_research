---
title: "TrackNet (weekenddeeplearning/TrackNet) — Keras reimplementation with labeling tool"
type: source
url: https://github.com/weekenddeeplearning/TrackNet
author: weekenddeeplearning (GitHub)
published: null
ingested: 2026-07-21
local_path: null
venue: GitHub repository (community reimplementation)
license: GPL-3.0
format: GitHub repo — Python, Keras/TensorFlow
tags: [object-tracking, heatmap, badminton, tennis, open-source, keras, tensorflow, annotation-tooling, sports-analytics]
---

# TrackNet (weekenddeeplearning/TrackNet) — Keras reimplementation with labeling tool

## Summary

A community **Keras/TensorFlow reimplementation of TrackNetV2** ("TrackNet II", the three-frame-input model), packaged for practical reuse rather than research novelty. It reproduces no new results and claims none — its value is **operational**: pre-trained `.h5` weights for **both badminton and tennis**, separate `Code_Baddy` / `Code_Tennis` trees, and, most usefully, a **bundled labeling tool** for building your own dataset. Since [TrackNetV1 showed that cross-sport transfer fails badly](tracknet-huang-2019.md) (35.2 F1 tennis→badminton), the ability to label a new sport cheaply is the binding constraint on applying TrackNet anywhere new — and that is exactly what this repo supplies. The catch is **GPL-3.0**, a materially different licensing posture from the MIT-licensed [TrackNetV3 repo](tracknetv3-repo.md).

## Key claims

- **What it is.** "Heatmap based high speed tiny sport objects tracking" — a **TrackNet II / V2** architecture (three-frame temporal input, heatmap regression, no bounding boxes) in **Keras/TensorFlow**, evidenced by `.h5` weight files.
- **Two sports, pre-trained.** Separate code and weights for **badminton** (`Code_Baddy`) and **tennis** (`Code_Tennis`) — a direct concession to V1's finding that a tennis-trained model does not transfer to badminton.
- **Training configuration** mirrors the original recipe closely: input `360×640`, **batch size 2**, **500 epochs**, and **256 classes** representing pixel intensity 0–255 — i.e. it retains [V1's unusual per-pixel 256-way softmax](tracknet-huang-2019.md) over grayscale levels rather than regressing a scalar heatmap.
- **Labeling tool included.** A custom annotation utility for producing the `Frame, Visibility, X, Y` CSV format the TrackNet family expects, plus heatmap ground-truth generation from those labels. This is the repo's most differentiated asset.
- **Inference** runs on video files and writes out a tracked/annotated output video.
- **License: GPL-3.0** — copyleft. Any derived work distributed downstream must also be GPL. For a hobby or research project this is a non-issue; for anything shipped, [the MIT-licensed V3 repo](tracknetv3-repo.md) is the safer base.

> [!warning] Framework generation gap
> This is **Keras/TensorFlow**, while the modern reference implementation ([TrackNetV3](tracknetv3-repo.md)) and [TrackNetV4](tracknetv4-motion-attention-2024.md) are **PyTorch**. Weights, augmentation code, and the V4 motion-attention module are **not portable** between them. Choosing this repo means forgoing the V3 rectification module and the V4 motion-attention plug-in unless you reimplement them.

## Entities mentioned

- [TrackNet](../entities/tracknet.md) — this reimplements the V2 generation of the family.

## Concepts touched

- [Heatmap-based object localization](../concepts/robotics/heatmap-object-localization.md) — the approach reimplemented here.

## Open questions

- No published metrics of its own — it is unverified whether these weights reproduce the original TrackNetV2 numbers. Anyone relying on them should re-evaluate on a held-out set first.
- Repository activity, maintenance status, and TF/Keras version pins were not established at ingest; Keras 2 → 3 is a breaking change and this code's era is unclear.
- Provenance of the pre-trained weights (which datasets, whose labels) is not documented — relevant both to expected accuracy and to whether the weights are redistributable.
