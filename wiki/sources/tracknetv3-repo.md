---
title: "TrackNetV3 — reference implementation (qaz812345/TrackNetV3)"
type: source
url: https://github.com/qaz812345/TrackNetV3
author: qaz812345 (GitHub) — implementation of Chen & Wang et al., ACM MM Asia 2023
published: 2023-12
ingested: 2026-07-21
local_path: null
venue: GitHub repository (companion code to ACM MM Asia 2023, doi 10.1145/3595916.3626370)
license: MIT
format: GitHub repo — Python 100%, PyTorch
tags: [object-tracking, heatmap, trajectory-rectification, inpainting, badminton, shuttlecock, open-source, pytorch, sports-analytics, data-augmentation]
---

# TrackNetV3 — reference implementation (qaz812345/TrackNetV3)

## Summary

The canonical open-source implementation of **TrackNetV3**, the third and currently strongest published member of the [TrackNet](../entities/tracknet.md) family, accompanying *"TrackNetV3: Enhancing ShuttleCock Tracking with Augmentations and Trajectory Rectification"* (ACM MM Asia 2023). Its architectural contribution is the split into **two trained modules**: a tracking module that predicts per-frame heatmaps, and a separate **trajectory rectification module (InpaintNet)** that treats a broken trajectory as an *inpainting* problem — detect the holes, then fill them. This is a meaningfully different stance from V1/V2, which accept whatever the per-frame detector produces. Combined with **background estimation** as an auxiliary input and **mixup** augmentation, it reports **97.51% accuracy / 98.56% F1** on the shuttlecock test set. **MIT-licensed**, ~276 stars / 63 forks, PyTorch — the practical starting point for anyone building on TrackNet today.

## Key claims

- **Two-module architecture.**
  - **Trajectory prediction (TrackNet)** — heatmap prediction over a frame sequence, using an **estimated background image** as auxiliary input so the network can subtract out static court clutter, plus **mixup** augmentation for robustness.
  - **Trajectory rectification (InpaintNet)** — consumes the predicted trajectory, generates a **repair mask** identifying frames likely to be wrong or missing, and **inpaints** the corrected path. Trained separately and with a much longer schedule (300 epochs, `seq_len 16`) than the tracker (30 epochs, `seq_len 8`).
- **Reported performance vs. V2.**

  | Model | Accuracy | Precision | Recall | F1 | FPS |
  |---|---|---|---|---|---|
  | TrackNetV2 | 94.98% | **99.64%** | 94.56% | 97.03% | 27.70 |
  | **TrackNetV3** | **97.51%** | 97.79% | **99.33%** | **98.56%** | 25.11 |

  The gain is almost entirely **recall** (94.56 → 99.33), bought with ~1.9 points of precision — exactly what a trajectory-repair stage should do: fill gaps, occasionally hallucinating one. Costs ~9% throughput.
- **Dataset.** The **Shuttlecock Trajectory Dataset** — professional and amateur badminton matches, frame sequences with CSV annotations (`Frame, Visibility, X, Y`). Preprocessing generates **median background images** at match or rally level, plus validation splits.
- **Usage.**
  ```bash
  # tracking module
  python train.py --model_name TrackNet  --seq_len 8  --epochs 30  --batch_size 10
  # rectification module
  python train.py --model_name InpaintNet --seq_len 16 --epoch 300 --batch_size 32
  # inference on a video
  python predict.py --video_file test.mp4 \
      --tracknet_file ckpts/TrackNet_best.pt --inpaintnet_file ckpts/InpaintNet_best.pt
  ```
- **Environment.** Python 3.8.7, PyTorch 1.10.0, developed on Ubuntu 16.04.7 LTS. Note both are **old pins** (PyTorch 1.10 dates to late 2021) — expect friction on modern CUDA stacks.
- **Tooling beyond the model.** Ships a **Dash-based error-analysis web app** for inspecting failure cases frame by frame, an `IterableDataset` mode for videos too large to fit in memory, and trajectory-visualization output.
- **License: MIT** — permissive, commercially usable. This matters: the other widely-forked TrackNet implementation is [GPL-3.0](weekenddeeplearning-tracknet-repo.md).

> [!note] Repo authorship vs. paper authorship
> The GitHub account (`qaz812345`) does not map cleanly to the paper's author list in the repo's own README. The DOI (10.1145/3595916.3626370) is the reliable citation anchor; treat the repo as the authors' reference implementation, which is how the community and [TrackNetV4](tracknetv4-motion-attention-2024.md) treat it.

## Entities mentioned

- [TrackNet](../entities/tracknet.md) — V3 is the strongest published member and the usual modern baseline.

## Concepts touched

- [Heatmap-based object localization](../concepts/robotics/heatmap-object-localization.md) — the tracking module's output representation, inherited from V1/V2.
- [Motion attention](../concepts/robotics/motion-attention.md) — what V3 notably *lacks*; [TrackNetV4](tracknetv4-motion-attention-2024.md) bolts it on and lifts V3's shuttlecock F1 from 97.5 to 97.9.

## Open questions

- The reported FPS (25.1) is an order of magnitude below the ~160 fps that [TrackNetV4](tracknetv4-motion-attention-2024.md) measures for TrackNetV2 — but V4's footnote says its V3 figure covers the *entire script* including data loading and file writing. The true model-only inference cost of V3 is not cleanly published anywhere.
- InpaintNet is trained on ground-truth trajectories with synthetic holes; how well does the repair generalize to the *actual* failure distribution of the tracker (which is correlated with occlusion, not random)?
- Does the background-estimation input break on camera cuts or moving cameras? Broadcast badminton is a mostly-fixed camera; the repo doesn't say what happens otherwise.
