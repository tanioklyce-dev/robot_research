---
title: "Develop Physical AI with NVIDIA Cosmos 3 (Hugging Face blog)"
type: source
url: https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai
author: NVIDIA
published: 2026-06-01
ingested: 2026-06-02
venue: Hugging Face Blog
tags: [cosmos, omnimodal, world-model, physical-ai, nvidia, diffusers, synthetic-data]
---

# Develop Physical AI with NVIDIA Cosmos 3 (Hugging Face blog)

## Summary

NVIDIA's launch blog announcing **Cosmos 3** on Hugging Face — the secondary/announcement companion to the [Cosmos 3 technical report](cosmos-3-technical-report.md). It frames Cosmos 3 as NVIDIA's first open **omni-model for physical AI reasoning and action**, consolidating what previously required separate Cosmos Predict / Transfer / Reason / Policy models into one **Mixture-of-Transformers** model with an autoregressive (reasoning) subsequence and a diffusion (generation) subsequence sharing joint attention. Heavier on usage/onboarding than the report; lighter on numbers.

## Key claims

- Two released sizes: **Cosmos3-Nano (16B = 8B reasoner + 8B generator)** for workstation-grade compute (RTX PRO 6000), and **Cosmos3-Super (64B = 32B + 32B)** for large-scale synthetic data generation and research (Hopper / Blackwell). *(Matches the report's Nano/Super; the report adds an unreleased 4B Edge.)*
- Operational modes table: Text/Image/Video→Video (video model), Text/Video→Text (VLM), Action/Image/Text→Video (forward dynamics), Text/Video→Action (inverse dynamics), Image/Text→Video&Action (policy).
- **Diffusers integration** shipping (`Cosmos3OmniPipeline`); post-training scripts on GitHub via the **Cosmos-Framework** repo.
- Released **synthetic data generation (SDG) datasets** for robotics, physics (Isaac Sim), spatial reasoning, digital humans, autonomous driving, and warehouse operations on Hugging Face.
- Applications: robotics manipulation (pick-and-place, laundry folding), autonomous driving long-tail scenarios, smart-spaces/warehouse safety.
- Resources: [github.com/nvidia/Cosmos](https://github.com/nvidia/Cosmos), Cosmos-Framework, Cosmos Cookbook, NIM microservices on build.nvidia.com, and the [technical report](https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf).

> [!note] Blog omits audio; report includes it
> The blog's modality framing centers language/image/video/action and does not foreground **audio**, which the technical report lists as a core fifth modality (frozen 48 kHz audio VAE, synchronous audio-video generation, audio benchmark scores). Treat the report as authoritative on modality coverage.

## Entities mentioned
- [NVIDIA](../entities/nvidia.md), [NVIDIA Cosmos](../entities/nvidia-cosmos.md), [Hugging Face](../entities/hugging-face.md).

## Concepts touched
- [World model](../concepts/world-models/world-model.md), [World-action model](../concepts/world-models/world-action-model.md), [VLA models](../concepts/learning/vla-models.md).

## Open questions
- Blog states per-model "model cards and licensing"; the report specifies a single **OpenMDW-1.1** umbrella license — the report is authoritative.
