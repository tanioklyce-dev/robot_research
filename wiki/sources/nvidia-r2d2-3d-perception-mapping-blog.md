---
title: "R²D²: Building AI-based 3D Robot Perception and Mapping with NVIDIA Research"
type: source
url: https://developer.nvidia.com/blog/r2d2-building-ai-based-3d-robot-perception-and-mapping-with-nvidia-research/
author: "Raffaello Bonghi (NVIDIA)"
published: 2025-06-17
format: vendor technical blog post (R²D² series)
tags: [nvidia, nvidia-research, r2d2, foundationstereo, foundationpose, bundlesdf, cuvslam, pycuvslam, nvblox, perception, slam, pose-estimation, depth]
ingested: 2026-11-10
---

# R²D²: Building AI-based 3D Robot Perception and Mapping with NVIDIA Research

## Summary

Five perception components presented as one 3D stack: FoundationStereo for depth, cuVSLAM for camera pose, [nvblox](../entities/nvblox.md) for mapping, and FoundationPose and BundleSDF for object pose and shape.

> [!note] Secondary for the research it covers
> This post summarises NVIDIA papers. Its figures weren't checked against those papers at ingest. The arXiv IDs listed are the primaries to ingest before any number here feeds a decision.

## Key claims

- **FoundationStereo.** A stereo-depth model trained on over 1 million synthetic stereo pairs, using a frozen DepthAnythingV2 prior through a side-tuning adapter. It claims leading zero-shot results on Middlebury, KITTI and ETH3D, and a CVPR 2025 best-paper nomination. A commercial version is listed as coming soon. arXiv 2501.09898.
- **PyCuVSLAM.** A Python API for cuVSLAM, the CUDA stereo visual-inertial SLAM previously available through [Isaac ROS](../entities/isaac-ros.md). Suggested uses include estimating camera trajectories from first-person videos to build training data. arXiv 2506.04359.
- **nvblox_torch.** A PyTorch interface to [nvblox](../entities/nvblox.md) with zero-copy tensors. It adds **deep feature fusion**, lifting features from vision foundation models into the 3D map so it holds semantics as well as geometry.
- **FoundationPose.** 6D pose estimation and tracking for new objects from a CAD model or a few reference images, without retraining. It is reported to beat CosyPose and StablePose on YCB-Video, T-LESS and LM-OCC. arXiv 2312.08344.
- **BundleSDF.** Online pose tracking and neural reconstruction from RGB-D video at about 10 Hz, needing only a first-frame segmentation. arXiv 2303.14158.

The [GB300 case study](nvidia-r2d2-gb300-tester-tray-assembly-blog.md) later found FoundationPose unreliable on small, textureless connectors, and replaced it with a per-part model.

## Entities mentioned

- [nvblox](../entities/nvblox.md), [Isaac ROS](../entities/isaac-ros.md)

## Concepts touched

- [Visual relocalisation and mapping](../concepts/robotics/visual-relocalization-and-mapping.md) — cuVSLAM and nvblox.

## Open questions

- **Licence of the "commercial version" of FoundationStereo.** The post implies the research release isn't licensed for commercial use, without saying so.
