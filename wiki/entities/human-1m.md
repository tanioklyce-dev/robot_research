---
title: Human-1M
type: entity
subtype: dataset
created: 2026-11-09
updated: 2026-11-09
sources: 2
tags: [dataset, human-video, egocentric, nvidia, gr00t-2, open-data]
---

**Human-1M** — NVIDIA's dataset of about 1 million hours of egocentric video of people working, with dense language annotations, SLAM and 3D hand keypoints ([GR00T 2 whitepaper](../sources/gr00t-2-whitepaper.md)). It is the largest component of [GR00T 2](nvidia-groot.md)'s pretraining.

## Scale and availability

- GR00T 2 uses a filtered **402,730 hours**, about 13.75 million episodes from over 51,500 collectors and 123,000 scenes.
- **100,000 hours are open** as [Human-1M-100K on Hugging Face](https://huggingface.co/datasets/nvidia/PhysicalAI-Human-1M-100K), with a [browser-based explorer](https://huggingface.co/spaces/nvidia/PhysicalAI-Human-1M-Explorer). The dataset's licence wasn't checked at ingest.

## Why it matters in this wiki

It scales up the [EgoScale](../sources/egoscale-paper.md) approach about 20-fold, from 20,854 hours. With robot data held fixed, real-robot success on 72 tasks rises from 18% with none of it to 41% with all of it, without levelling off ([whitepaper](../sources/gr00t-2-whitepaper.md), Fig. 10). See [scaling laws for VLAs](../concepts/learning/scaling-laws-vla.md).

## Related

- [NVIDIA GR00T](nvidia-groot.md) · [NVIDIA GEAR](nvidia-gear.md) · [UMI](umi.md)

## Mentioned in

- [GR00T 2 whitepaper](../sources/gr00t-2-whitepaper.md)
