---
title: TrackNet (model family)
type: entity
created: 2026-07-21
updated: 2026-07-22
sources: 5
tags: [object-tracking, heatmap, small-object-detection, computer-vision, sports-analytics, tennis, badminton, pinball, open-source]
---

# TrackNet (model family)

**TrackNet** is a family of deep networks for tracking **small, fast, frequently-occluded objects** — principally tennis balls and badminton shuttlecocks — in ordinary video, using **[heatmap output](../concepts/robotics/heatmap-object-localization.md)** rather than bounding boxes and **stacked consecutive frames** rather than single images.

## Lineage

Version numbers are **community-assigned across four different groups**, not one lab's roadmap — a fact worth knowing before reading "V4 > V3" as a straightforward succession.

| Version | Year | Group | Core contribution |
|---|---|---|---|
| **[V1](../sources/tracknet-huang-2019.md)** | 2019 | NCTU, Taiwan (Huang, Liao, Chen, İk, Peng) | VGG-16 encoder + DeconvNet decoder → Gaussian heatmap; 3-frame input; tennis + badminton datasets |
| **V2** | 2020 | NCTU, Taiwan | Multi-input/multi-output, skip connections, weighted BCE loss; faster and more GPU-efficient |
| **[V3](../sources/tracknetv3-repo.md)** | 2023 | ACM MM Asia 2023 | Background-estimation input + mixup; **InpaintNet** trajectory-rectification module |
| **[V4](../sources/tracknetv4-motion-attention-2024.md)** | 2024 | ANU / Curtin (Raj, Wang, Gedeon) | **[Motion attention maps](../concepts/robotics/motion-attention.md)** from absolute frame differencing, fused into any heatmap tracker |

V4 is a **plug-in module**, not a replacement architecture — it is demonstrated *on top of* both V2 and V3 and improves each.

## Why heatmaps instead of bounding boxes

A tennis ball in broadcast video is **2–12 pixels across (mean ≈ 5)** and smeared by motion blur ([V1 §V](../sources/tracknet-huang-2019.md)). Box-regression detectors have too little signal at that scale: a **YOLOv7** baseline scores **68.0 F1** on shuttlecock tracking where TrackNetV3 scores **97.5** ([V4, Table I](../sources/tracknetv4-motion-attention-2024.md)) — a ~30-point gap that is the family's central empirical justification. Pixel-wise heatmap prediction sidesteps anchor/box machinery entirely; the peak of the predicted blob *is* the answer. See [Ultralytics YOLO](ultralytics-yolo.md) for the detector family being outperformed here.

## Performance trajectory

| Model | Task | Precision | Recall | F1 |
|---|---|---|---|---|
| Archana's classical CV baseline | Tennis | 92.5% | 74.5% | 82.5% |
| V1 Model I (1 frame) | Tennis | 95.7% | 89.6% | 92.5% |
| V1 Model II' (3 frames) | Tennis | 99.7% | 97.3% | 98.5% |
| V2 | Shuttlecock | 99.64% | 94.56% | 97.03% |
| V3 | Shuttlecock | 97.79% | 99.33% | 98.56% |
| V3 + V4 motion attention | Shuttlecock | 99.5% | 96.3% | 97.9% |

> [!warning] These numbers are not directly comparable
> Different rows come from different papers, datasets, splits, and tolerances (V1 uses a **5-pixel** positioning-error spec; V2–V4 use **4 pixels**). The V3 row is from [its own repo's README](../sources/tracknetv3-repo.md); the V4 row is from [V4's Table I](../sources/tracknetv4-motion-attention-2024.md) on a different shuttlecock evaluation subset. Read each as within-paper evidence, not a leaderboard.

## Known limitations

- **Cross-sport transfer fails.** Tennis-trained V1 applied zero-shot to badminton: **35.2 F1** (recall 22.9%) ([V1 §V](../sources/tracknet-huang-2019.md)). Every new sport needs its own labelled data — which is why the [labeling tool in the Keras repo](../sources/weekenddeeplearning-tracknet-repo.md) matters.
- **Cross-video generalization is much weaker than headline numbers.** V1's 10-fold cross-validation drops recall from 97.3% to **75.7%**.
- **Independently reproduced outside sports (2026-07-22).** A first-party pinball tracker ([pinball_tracker](../sources/pinball-tracker-repo.md)) trained on one machine scores **0.914 F1** on a second machine and **0.232 F1 (recall 25.6%)** on a third — nearly the same figure and the same recall-dominated shape as V1's tennis→badminton **35.2 F1 / 22.9% recall**. Notably the two held-out venues differ by a factor of ~4 in F1 with no reliable way to predict which kind a new venue will be. This is the family's most consistently reproduced weakness, and it generalizes past "sport" to **any change of venue with bespoke visual content**. See [fast-ball-tracking §9](../syntheses/projects/fast-ball-tracking-for-robots.md).
- **Static-camera assumption.** V3's background estimation and V4's frame differencing both assume a roughly fixed camera. Neither paper tests a panning or robot-mounted camera — the key open question for robotics reuse.

## Implementations

- **[qaz812345/TrackNetV3](../sources/tracknetv3-repo.md)** — PyTorch, **MIT**, ~276 ★. Reference V3 implementation; the practical modern starting point.
- **[weekenddeeplearning/TrackNet](../sources/weekenddeeplearning-tracknet-repo.md)** — Keras/TF, **GPL-3.0**. V2-generation, pre-trained tennis + badminton weights, includes a **labeling tool**.

> [!warning] License split
> The two main community implementations sit on **opposite sides of the copyleft line** (MIT vs GPL-3.0), and they are on **different frameworks** (PyTorch vs Keras) so weights and modules don't port. Pick deliberately.

## Mentioned in

- [TrackNet: A Deep Learning Network for Tracking High-speed and Tiny Objects in Sports Applications (2019)](../sources/tracknet-huang-2019.md)
- [TrackNetV4: Enhancing Fast Sports Object Tracking with Motion Attention Maps (2024)](../sources/tracknetv4-motion-attention-2024.md)
- [TrackNetV3 — reference implementation](../sources/tracknetv3-repo.md)
- [TrackNet (weekenddeeplearning) — Keras reimplementation](../sources/weekenddeeplearning-tracknet-repo.md)
- [pinball_tracker (tanioklyce-dev)](../sources/pinball-tracker-repo.md) — first-party implementation of a TrackNet-class tracker outside sports; the wiki's only measured field evidence for this family.
