---
title: FLUX 3
type: entity
subtype: model
created: 2026-09-07
updated: 2026-09-07
sources: 2
tags: [flux-3, black-forest-labs, multimodal, flow-matching, self-flow, video-generation, audio, action-prediction, world-model, video-action-model, open-weights]
---

# FLUX 3

[Black Forest Labs](black-forest-labs.md)' **multimodal flow-matching foundation model** — one architecture jointly trained on **image, video and audio from the beginning**, and the backbone from which robot **actions** are decoded ([launch, 2026-07-23](../sources/flux-3-launch.md)).

The framing is that the modalities are not separate capabilities but different views of one thing:

> Each is a projection of the same underlying reality, captured by different sensors… the sound has to match the impact, the motion has to obey the mass, the future has to follow from the past. **The modalities stop being separate and start being evidence about one underlying reality.**

## Capabilities

**Video** — up to **20 seconds with native audio in a single generation**: text-to-video, image-to-video (animation or visual reference), video-to-video from a reference clip, keyframe-to-video, generative video-audio continuation, multilingual dialogue, and **agentic chaining** of clips into multi-shot sequences several minutes long with character consistency. **Image** — synthesis and editing across styles, aspect ratios and resolutions, with improved complex-prompt handling and multilingual text rendering. **Action** — two routes: native action prediction integrated into FLUX 3 directly ("FLUX 3 Action"), and the **[mimic robotics](mimic-robotics.md)** partnership route, **FLUX-mimic**.

## Where the compute goes

| Modality | Share |
|---|---|
| **Video prediction** | **>95% of total training compute** |
| Audio | **<0.5%** of tokens in a 720p video with audio |
| Actions | *"a low dimensional representation of a robot's state"* |

The argument for that allocation: *"to generate realistic videos, a model has no choice but to learn contact, motion, weight, cause and effect; get any of them wrong and it looks wrong."*

**Training data**: *"tens of millions of hours of general video content"* plus *"hundreds of thousands of hours of video content focused on human and robot manipulation tasks."*

## Self-Flow — the mechanism

Built on **Self-Flow** ([arXiv 2603.06507](https://arxiv.org/abs/2603.06507), ICML 2026), whose stated key idea is **Dual-Timestep Scheduling**: *"applies heterogeneous noise levels across tokens, creating an information asymmetry that forces the model to infer missing information from corrupted inputs."*

That is **masked modeling with a continuous knob**, inside flow matching. Its purpose is to fix the objection that generative models learn *"less disentangled representations, which puts a ceiling on their usefulness"* — without bolting on an external representation model, which the paper argues *"require separate training, operate on misaligned objectives, and exhibit unexpected scaling behavior."* BFL reports **reciprocal improvement**: better generation (Fréchet distance) *and* better representations (robot manipulation success). **Not ingested; abstract only.**

## Measured claims worth carrying

- **Adding actions costs the video model nothing permanent**: human ratings on text-to-video and image-to-video fell **up to 10%** when action prediction entered the curriculum, and recovered fully after **3,500 steps**.
- **The action decoder beats VLAs from a completely frozen backbone** — *"a setting where previous VLAs fail to succeed."* Fine-tuning both reaches state-of-the-art. Chart median is over **20 autonomous trials**, so treat as qualitative.
- **Sample efficiency**: Self-Flow halves the steps to a given success rate versus a non-Self-Flow video model; mimic-video reports up to **10×** over VLAs; FLUX-mimic *"combines both effects."*
- **Latency**: backbone input → world representation in **<80 ms on one RTX 5090**; full system reaction time **101 ms**. Better representations → capability per parameter → a shallower backbone, and *"backbone depth is the dominant driver of deployment latency."*
- Self-reported preliminary video preference wins over Grok Imagine Video (69%), Runway Gen-4.5 (77%), Luma Ray 3.2 (93%), Kling v3 Pro (60%), Seedance 2.0 and Gemini Omni Flash (52%) — **no n, no CIs, no protocol**.

## Availability

Early access at launch, then staged: **FLUX 3 Video** (API + private weights) → **action prediction via selected partners, beginning with mimic** → **FLUX 3 Image** → **"FLUX 3 Dev": open-weight access to a multimodal backbone, for content creation *and action prediction***.

> [!note] The open-weight tier is announced, not shipped
> If FLUX 3 Dev arrives as described it is an **open-weight video-action backbone** — materially different from the open [VLAs](../concepts/learning/vla-models.md) this wiki tracks. It is also listed one line after action prediction is described as partner-gated. Watch, don't assume.

Stated next goal: *"unify perceptual, action and language prediction in the same unified model"* — **language is the missing modality**, which inverts the VLA line where language came first and physics is the gap.

## Related

- [Black Forest Labs](black-forest-labs.md) · [mimic robotics](mimic-robotics.md)
- [World-action model](../concepts/world-models/world-action-model.md) — the class FLUX-mimic joins, with a twist: a *frozen general-purpose* backbone.
- [Generative-video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md) · [JEPA](../concepts/world-models/jepa.md) — the dispute it takes a third position in.
- [Representation evaluation](../concepts/learning/representation-evaluation.md) — the frozen-backbone result is a probe result.
- [Flow matching](../concepts/learning/flow-matching.md) — the generative framework.

## Mentioned in

- [FLUX 3 and FLUX-mimic launch](../sources/flux-3-launch.md)
