---
title: Enhancing YOLOv11n for Reliable Child Detection in Noisy Surveillance Footage
type: source
url: https://arxiv.org/abs/2602.10592
author: Khanh Linh Tran, Minh Nguyen Dang, Thien Nguyen Trong, Hung Nguyen Quoc, Linh Nguyen Kieu (PTIT, Hanoi)
published: 2026-02-11
ingested: 2026-07-17
local_path: raw/2602.10592v1.pdf
venue: arXiv preprint (cs.CV), 2602.10592v1
license: null
format: PDF (11 pages)
tags: [object-detection, yolo, sahi, small-object-detection, data-augmentation, edge-ai, surveillance, computer-vision]
---

# Enhancing YOLOv11n for Reliable Child Detection in Noisy Surveillance Footage

## Summary

A short applied-CV paper from **Posts and Telecommunications Institute of Technology (PTIT), Hanoi** that improves **child detection** on low-quality CCTV footage **without touching the model architecture** — the gains come entirely from (1) a **domain-specific data-augmentation pipeline** that composites segmented child cutouts into real daycare scenes and layers on CCTV-style degradations, and (2) **[SAHI](../concepts/robotics/sahi-slicing-inference.md)** (Slicing Aided Hyper Inference) at inference time to recover small/truncated instances. The base detector is **YOLOv11n**, the smallest [Ultralytics YOLO](../entities/ultralytics-yolo.md) variant, chosen for edge deployment. On a child-only subset of the Roboflow Daycare dataset the full pipeline lifts **mAP@0.5 0.963 → 0.967** and **mAP@0.5:0.95 0.760 → 0.783** (+0.7 / +2.3 absolute) over the baseline — modest gains the authors themselves attribute to the dataset's single-camera limitation. The wiki value is the concrete **edge-perception recipe** (YOLOv11n + scene-aware augmentation + SAHI), not the headline numbers.

## Key claims

- **Architecture-free approach.** All improvement comes from data augmentation + inference-time slicing; YOLOv11n is fine-tuned from COCO-pretrained Ultralytics weights, unchanged. (Abstract, §3.4)
- **Two-part augmentation (§3.3).**
  - **Synthetic child compositing** — segment child cutouts from labeled frames, scale each to the local bounding-box-area distribution, rotate slightly, and paste under one of three placement strategies: **occlusion** (overlap an existing box without sharing its center), **edge truncation** (≥50% of the box kept in-frame), or **neutral/center** placement. Alpha-blend using local brightness + **Laplacian-variance** noise estimates for photometric consistency.
  - **Image-level degradation** — additive stripe noise (analog/compression artifacts), spatial filtering (motion blur), and lighting shifts (histogram equalization, contrast stretching, color grading).
- **SAHI at inference (§3.5).** Slice the image into overlapping `S×S` patches (`S = min(H,W)·r`, overlap ratio γ∈[0,0.5]), run YOLOv11n per patch, map boxes back to full-image coordinates, and merge with IoU-threshold NMS. Trades extra compute for higher small-object recall — justified as acceptable in a safety-critical child-monitoring setting.
- **Dataset (§3.2, §4).** Roboflow Universe **Daycare** dataset, filtered to a **single `child` class** (adults discarded): 3,300 images / 22,340 child instances, split 69/14/17 train/val/test. Fixed 564-image / 3,755-instance test set across all runs.
- **Ablation (Table 4).** Trained 100 epochs, batch 16.

  | Config | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
  |---|---|---|---|---|
  | YOLOv11n baseline | 0.947 | 0.925 | 0.963 | 0.760 |
  | + Dataset A (synthetic children) | 0.942 | 0.937 | 0.964 | 0.764 |
  | + Dataset B (noise/light effects) | 0.939 | 0.935 | 0.961 | 0.773 |
  | + Dataset C (both) | 0.943 | 0.934 | 0.964 | 0.779 |
  | + Dataset C + **SAHI** | 0.946 | 0.933 | **0.967** | **0.783** |

  Augmentations help most at the stricter mAP@0.5:0.95 (localization) end; SAHI adds the final small-object bump.
- **Honest limitation (§5).** Gains are "consistent yet modest," bounded by the **single-camera** Roboflow Daycare dataset (limited background/cross-view diversity). Future work: multi-camera collection, larger datasets, domain-adaptive / self-supervised pretraining.
- **Edge framing.** The whole point is a **deployment-ready, low-power** pipeline — YOLOv11n keeps real-time inference on resource-constrained CCTV/edge hardware while augmentation + SAHI recover the accuracy that small/occluded children otherwise cost.

## Entities mentioned

- [Ultralytics YOLO](../entities/ultralytics-yolo.md) — YOLOv11n is the base detector, fine-tuned from Ultralytics COCO weights.

## Concepts touched

- [SAHI (Slicing Aided Hyper Inference)](../concepts/robotics/sahi-slicing-inference.md) — the inference-time small-object technique this paper applies.

## Open questions

- Does the scene-aware compositing generalize beyond one daycare camera? The authors explicitly flag single-camera bias as the ceiling on their gains.
- What is the actual SAHI latency cost on an edge device (e.g. a Jetson) — the paper claims real-time compatibility but reports no on-device FPS with slicing enabled.
