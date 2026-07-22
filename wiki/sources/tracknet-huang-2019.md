---
title: "TrackNet: A Deep Learning Network for Tracking High-speed and Tiny Objects in Sports Applications"
type: source
url: https://arxiv.org/abs/1907.03698
author: Yu-Chuan Huang, I-No Liao, Ching-Hsuan Chen, Tsì-Uí İk, Wen-Chih Peng (National Chiao Tung University)
published: 2019-07-08
ingested: 2026-07-21
local_path: raw/1907.03698v1.pdf
venue: arXiv preprint (cs.CV), 1907.03698v1 — presented at IEEE AVSS 2019
license: null
format: PDF (12 pages)
tags: [object-detection, object-tracking, heatmap, small-object-detection, computer-vision, sports-analytics, tennis, badminton, vgg, deconvnet]
---

# TrackNet: A Deep Learning Network for Tracking High-speed and Tiny Objects in Sports Applications

## Summary

The founding paper of the **[TrackNet](../entities/tracknet.md)** family. A team at **National Chiao Tung University (Taiwan)** attacks a perception problem that standard object detectors handle badly: locating a **tiny, fast, motion-blurred, frequently occluded** ball in ordinary broadcast video. Their answer abandons bounding boxes entirely in favour of **[heatmap-based localization](../concepts/robotics/heatmap-object-localization.md)** — a VGG-16 encoder plus a DeconvNet-style upsampling decoder emits a full-resolution heatmap whose Gaussian peak *is* the ball position. The second key idea is **temporal stacking**: feeding **three consecutive frames** instead of one lets the network learn flight patterns, so it can position a ball that is invisible in the current frame. On the 2017 Summer Universiade men's tennis final, the three-frame model reaches **99.7% precision / 97.3% recall / 98.5% F1**, crushing a conventional image-processing baseline. The paper is the origin of a design pattern — heatmap output + multi-frame input — that every subsequent version and most sports-tracking repos still use.

## Key claims

- **Why detectors fail here (§I–II).** In broadcast video the ball is a handful of pixels, smeared into an afterimage by a 30 fps shutter, and routinely occluded by players or blended into the court. Two-stage R-CNN-family detectors are too slow for real time; one-stage YOLO is fast but still block-based and struggles at this object scale. Fully-convolutional, pixel-wise prediction is the better fit.
- **Architecture (§IV).** 18 conv layers, all `3×3`, all ReLU + BatchNorm. Conv1–13 replicate **VGG-16** as the encoder (64→128→256→512 channels with max-pooling); Conv14–18 form the **DeconvNet** decoder, using upsampling layers symmetric to the encoder's max-pools to recover the resolution lost in pooling. Input is `640×360` (downsized from `1280×720` for speed).
- **Heatmap output, not coordinates (§IV).** The final layer is a **softmax over 256 grayscale values per pixel**, producing a continuous-valued heatmap. Ground truth is a **2-D Gaussian** centred on the labelled ball, with the diameter of the distribution matched to the ball's apparent size — so the network is trained to paint a blob, not regress an `(x, y)`.
- **Heatmap → coordinate (§IV).** Post-processing thresholds the heatmap at **t = 128** into a binary mask, then takes the contour/centroid of the resulting blob as the ball position.
- **Multi-frame input is the single biggest win (§V).** Two variants: **Model I** (one input frame) vs **Model II** (three consecutive frames).

  | Model | Precision | Recall | F1 |
  |---|---|---|---|
  | Archana's conventional algorithm | 92.5% | 74.5% | 82.5% |
  | TrackNet **Model I** (1 frame) | 95.7% | 89.6% | 92.5% |
  | TrackNet **Model II** (3 frames) | 99.8% | 96.6% | 98.2% |
  | TrackNet **Model II'** (3 frames, enriched training set) | 99.7% | 97.3% | 98.5% |

  Recall is where the temporal context pays: +7 points from Model I to Model II. The authors show Model II **correctly positions occluded balls** by interpolating from the neighbouring frames — e.g. a ball hidden behind a player in `0139.jpg` is located using `0138.jpg` and `0140.jpg`.
- **Datasets (§III).** Primary set: **20,844 labelled frames** from the broadcast of the **2017 Summer Universiade** men's singles tennis final (`1280×720`, 30 fps), split 70/30 train/test. To fight overfitting, **16,118 further frames** from **9 additional videos** across **grass, red clay, and hard courts** were added, producing Model II'. A separate **badminton** dataset of **18,242 frames** is also used. Labels are per-frame CSV rows of `filename, visibility, x, y, status`.
- **Honest generalization result (§V).** Under **10-fold cross-validation**, Model II' drops to **95.3% / 75.7% / 84.3%** — precision holds but **recall collapses by over 20 points**. The 98.5% headline is a same-distribution number; cross-video generalization is substantially weaker.
- **Transfer learning across sports fails (§V).** Applying the tennis-trained model zero-shot to badminton ("TrackNet-Tennis") yields **75.8% precision / 22.9% recall / 35.2% F1** — effectively unusable. The authors attribute this to camera framing (badminton broadcasts use a shorter focal length, so ball and players are larger). **Each sport needs its own training data**, not a fine-tune.
- **Training setup (Table III).** Adadelta optimizer, learning rate **1.0**, batch size **2**, 200 steps/epoch, **500 epochs**, weights initialized random-uniform in `[−0.05, 0.05]`. Epoch count was tuned from the loss curve to sit between underfitting and overfitting.

- **The 5-pixel tolerance is derived, not arbitrary (§V).** The authors measure the ball's apparent diameter in the video — **2 to 12 pixels, mean ≈ 5** — and argue that an error within one ball-width cannot mislead trajectory identification. So **positioning error (PE) > 5 pixels counts as a false prediction**. ~99.9% of Model I and Model II detections fall inside it.

> [!note] Comparing across versions
> Later members of the family standardized on a **4-pixel** tolerance ([TrackNetV4](tracknetv4-motion-attention-2024.md), following V2/V3), so V1's headline numbers are not perfectly comparable to V2/V3/V4 tables without care.

## Entities mentioned

- [TrackNet](../entities/tracknet.md) — the model family this paper originates.
- [Ultralytics YOLO](../entities/ultralytics-yolo.md) — cited as the fast one-stage alternative that TrackNet deliberately does *not* use (block-based detection is the wrong tool at this object scale).

## Concepts touched

- [Heatmap-based object localization](../concepts/robotics/heatmap-object-localization.md) — this paper is the canonical sports-tracking instance.
- [SAHI (Slicing Aided Hyper Inference)](../concepts/robotics/sahi-slicing-inference.md) — the *other* mainstream answer to small-object detection; TrackNet solves it by changing the output representation, SAHI by changing the inference procedure.

## Open questions

- The 10-fold-CV recall drop (97.3% → 75.7%) is the real generalization signal and gets one sentence in the paper. How much of the gap is court/lighting diversity vs. label noise in the partially-labelled extra videos?
- The 256-way softmax per pixel is an unusual choice — why classify grayscale levels rather than regress a scalar heatmap, as later heatmap methods (pose estimation, CenterNet) do? The paper doesn't ablate it.
- Transfer from tennis to badminton fails badly. Is that really focal length, or is it the shuttlecock's very different appearance and deceleration profile? No experiment separates the two.
