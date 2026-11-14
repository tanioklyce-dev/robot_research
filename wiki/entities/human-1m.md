---
title: Human-1M
type: entity
subtype: dataset
created: 2026-11-09
updated: 2026-11-13
sources: 2
tags: [dataset, human-video, egocentric, nvidia, gr00t-2, open-data]
---

**Human-1M** — NVIDIA's dataset of about 1 million hours of egocentric video of people working, with dense language annotations, SLAM and 3D hand keypoints ([GR00T 2 whitepaper](../sources/gr00t-2-whitepaper.md)). It is the largest component of [GR00T 2](nvidia-groot.md)'s pretraining.

## Scale and availability

- GR00T 2 uses a filtered **402,730 hours**, about 13.75 million episodes from over 51,500 collectors and 123,000 scenes.
- **Three tiers of collection** (whitepaper App. C.1). Most of it is in the wild: households, workplaces, farms, kitchens, retail and logistics. About 80,000 h is studio tabletop work. About 3,000 h (700k episodes) is "in-lab" data, recorded with wrist cameras placed to reproduce a target robot's view and at speeds the robot can match. About 90,000 h includes wrist cameras.
- **Annotations**: 21 3D keypoints per hand, head pose from SLAM, and two tiers of language: an episode summary and timestamped 1–10 s action segments. NVIDIA's Flora models label actions, and relabeling all 400k hours takes about two days.
- **Training timesteps are filtered automatically** on head speed, both hands in view, consistent finger-bone lengths and wrist speed ≤ 1 m/s.
- **100,000 hours are open** as [Human-1M-100K on Hugging Face](https://huggingface.co/datasets/nvidia/PhysicalAI-Human-1M-100K), with a [browser-based explorer](https://huggingface.co/spaces/nvidia/PhysicalAI-Human-1M-Explorer). The dataset's licence wasn't checked at ingest.

## Why it matters in this wiki

It scales up the [EgoScale](../sources/egoscale-paper.md) approach about 20-fold, from 20,854 hours. With robot data held fixed, real-robot success on 72 tasks rises from 18% with none of it to 41% with all of it, without levelling off ([whitepaper](../sources/gr00t-2-whitepaper.md), Fig. 10). That is +23.1 points (95% CI 13.4–33.3). The 1%→10% step is within noise on the robot, and each share is one training run. See [scaling laws for VLAs](../concepts/learning/scaling-laws-vla.md).

## Related

- [NVIDIA GR00T](nvidia-groot.md) · [NVIDIA GEAR](nvidia-gear.md) · [UMI](umi.md)

## Mentioned in

- [GR00T 2 whitepaper](../sources/gr00t-2-whitepaper.md)
