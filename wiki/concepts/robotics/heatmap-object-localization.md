---
title: Heatmap-based object localization
type: concept
created: 2026-07-21
updated: 2026-07-21
sources: 10
tags: [object-detection, object-tracking, small-object-detection, computer-vision, heatmap, perception]
---

# Heatmap-based object localization

**Heatmap-based localization** replaces the bounding-box output of a standard detector with a **dense, per-pixel confidence map** the same size as the input. The object's position is read off as the **peak** (or thresholded centroid) of a blob in that map, rather than regressed as box coordinates.

## Definition

Training targets are **2-D Gaussians** centred on each labelled object, with the Gaussian's spread matched to the object's apparent size. The network — typically an encoder-decoder (a downsampling CNN backbone plus an upsampling/deconvolution decoder, symmetric so that resolution lost to max-pooling is recovered) — is trained to reproduce that map. At inference, the heatmap is thresholded into a binary mask and the blob's contour or centroid gives the coordinate.

The representation's advantage appears exactly where box regression degrades: **very small objects**. A ball 2–12 pixels across offers almost no gradient signal for width/height regression and falls below the effective resolution of anchor-based detectors, but it is perfectly well-described by a small Gaussian in a dense map. The output is also naturally **multi-modal** — ambiguity shows up as two blobs rather than being collapsed into one averaged, wrong box — and it composes cleanly with **temporal stacking**, since consecutive frames can be concatenated on the channel axis with no change to the output head.

The cost is that heatmaps carry **no extent, class, or instance identity** by default. They answer "where," not "what" or "which one" — so they suit single-known-object-class tracking far better than general detection.

## Key references

- [TrackNet (Huang et al., 2019)](../../sources/tracknet-huang-2019.md) — the canonical sports-tracking instance: VGG-16 encoder + DeconvNet decoder at `640×360`, output a **256-way softmax per pixel** over grayscale levels, thresholded at 128. Three-frame input lifts F1 from 92.5 to 98.2, and lets the model **locate balls that are fully occluded** in the current frame by inference from neighbours.
- [TrackNetV3 implementation](../../sources/tracknetv3-repo.md) — adds a second stage that treats the *trajectory* as the object to repair (InpaintNet), pushing recall to 99.33%.
- [TrackNetV4 (Raj et al., 2024)](../../sources/tracknetv4-motion-attention-2024.md) — supplies the clearest head-to-head evidence for the representation: **YOLOv7 68.0 F1 vs TrackNetV3 97.5 F1** on the same shuttlecock task.

## Related concepts

- [SAHI (Slicing Aided Hyper Inference)](sahi-slicing-inference.md) — the **complementary** answer to the same small-object problem. SAHI keeps the box-regression detector and changes the *inference procedure* (slice the image so small objects are effectively larger); heatmap localization keeps the whole-frame pass and changes the *output representation*. Heatmaps win when the object class is known and singular; SAHI wins when you need general multi-class detection with extent.
- [Motion attention](motion-attention.md) — a module class that plugs directly into heatmap trackers, exploiting the fact that the output head is dense and spatially aligned with the features.
- [AprilTags](apriltags.md) — the engineering shortcut: instead of making perception robust to tiny, ambiguous targets, change the target into a fiducial designed for detection.

## Current state

Heatmap output is standard well beyond sports tracking — it is the dominant representation in **human pose estimation** (where each keypoint gets its own channel) and underpins anchor-free detectors like CenterNet. Within the [TrackNet](../../entities/tracknet.md) family it has been stable for six years and four versions; every improvement since 2019 (skip connections, background subtraction, trajectory inpainting, motion attention) has modified what feeds *into* the heatmap head or what post-processes its output, while the heatmap itself has gone unchallenged. That stability is a reasonable signal the representation is right for the problem.

Its main unaddressed weakness for **robotics** is that the whole family assumes a roughly **static camera**, which broadcast sports provides and a robot does not.

## Mentioned in

- [TrackNet: A Deep Learning Network for Tracking High-speed and Tiny Objects (2019)](../../sources/tracknet-huang-2019.md)
- [TrackNetV4: Enhancing Fast Sports Object Tracking with Motion Attention Maps (2024)](../../sources/tracknetv4-motion-attention-2024.md)
- [TrackNetV3 — reference implementation](../../sources/tracknetv3-repo.md)
- [TrackNet (weekenddeeplearning) — Keras reimplementation](../../sources/weekenddeeplearning-tracknet-repo.md)
