---
title: "AI finally sleeps, Gemini 4 Carbon, ETH cracked, energy-based models, Anthropic IPO: AI NEWS (AI Search, YouTube)"
type: source
url: https://www.youtube.com/watch?v=IGICYFyP_EI
author: AI Search (YouTube channel @theAIsearch)
published: 2026-11-01
ingested: 2026-11-02
format: "video, 53:54; about 30 items. Read through YouTube auto-captions. Sponsored segment (Luma) at 18:10."
tags: [video, news-roundup, secondary-source, energy-based-model, tem, world-model, genie-4, mundo, overseer, uniaction, physag3d, simready, motionbricks]
---

> [!note] Ingest depth and provenance
> This is a **secondary source**: a weekly news roundup that spends about a minute on each item. It is on file as a discovery index, and it should not be cited for technical claims when a primary is linked below. The ingest request linked to 40:00, immediately before the energy-based model segment at 40:47.
>
> Only the robotics, world-model and EBM segments were read closely and checked against primaries. The LLM, speech, OCR, video and IPO items are listed in the chapter index only, and **nothing in this wiki should cite this page for them**.

## Summary

A general AI news roundup whose useful content for this wiki is a cluster of physical-AI items: one new EBM paper, four world models and action-conditioned video models, a physically interactive asset generator, and NVIDIA's open sim-asset library. The segment that prompted the ingest presents energy-based models as a new kind of image generator. The description gives no link for it, but video frames at about 40:50–42:00 show the paper as [TEM](tem-scaling-transformer-ebm-paper.md). The video's main value is the pointers: its summaries were accurate on most checkable numbers, but it mischaracterized the EBM item's significance.

## Key claims, checked against primaries

| Time | Item | The video says | Primary says |
|---|---|---|---|
| 40:47 | [TEM](tem-scaling-transformer-ebm-paper.md) | "Completely new type" of image model; "proof of concept"; quality "a lot worse than the frontier"; code and training script out; 2.44 GB | **Not new:** [EBMs](../concepts/learning/energy-based-models.md) go back to 1982 in this wiki. FID 3.82 unguided beats unguided DiT and SiT, while guided diffusion stays ahead. Code, training script and the 2.44 GB checkpoint are confirmed. |
| 26:26 | [MUNDO](https://mundo-world-model.github.io/) | Builds an explorable world from images, with objects and physics; for training humanoids; code and weights end of November | Confirmed: 3D proxy → scene program (mass, friction) → **MuJoCo** → video diffusion render. NTU MMLab + ACE Robotics. Unitree G1 demos, **no reported numbers**. No paper ID. Repo TODO: "Code and weights (end of November)". |
| 41:53 | [OverSeer](https://runjiali-rl.github.io/OverSeer/) | "By Meta"; multi-agent world model anchored by fixed cameras; dataset out, no model | **Oxford and Meta** (arXiv 2610.28554). Confirmed otherwise. An auxiliary camera costs 108 tokens per latent frame instead of 864. Minecraft, Doom and a real studio capture. No quantitative metrics on the page and no robotics claim. |
| 06:57 | [UniAction](https://uniaction.github.io/) | One video model for force, camera, hand-pose and robot-pose control; based on Wan 2.2 | Confirmed (Stanford, [Jiajun Wu](../entities/jiajun-wu.md); arXiv 2610.32977). [Repo](https://github.com/KBRASK/UniAction) uses Wan2.2-I2V-A14B. Code is Apache-2.0. Project page has no robot-pose-specific numbers. |
| 33:24 | [Genie 4](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) | Interactive worlds with native audio; checkers demo with Gemini 4 Argon; trusted testers only | Confirmed, and the demo shows an [Apollo](../entities/apptronik-apollo.md) humanoid. DeepMind names "training environments for robots and agents" as a use, and concedes that visual details and object permanence can drift in longer runs. No resolution, fps or session length given. |
| 35:14 | [PhysAg3D](https://supra-3d.github.io/PhysAg3D/) | Single image → interactive 3D asset with moving parts; code and model released; MIT | Partly: source is MIT, but the [repo](https://github.com/Supra-3D/PhysAg3D) **does not bundle model weights** (TRELLIS.2 and others keep their own licenses). arXiv 2610.39924. Delivers a MuJoCo scene. Reports 91.3% action completion over 50 objects and 110 actions. |
| 11:42 | [SimReady assets](https://huggingface.co/datasets/nvidia/simready-assets) | 2,600+ assets, about 490 GB, CC-BY, with mass, friction, collision and articulation data | **2,677 assets, 490 GB, CC-BY-4.0.** The dataset card as fetched does not itself list the physics properties, so that part is unverified here. |
| 01:10 | [MotionBricks](motionbricks-paper.md) | "Drops" a new tool; 15,000 FPS, 2 ms, 350k+ clips; human and G1 models of about 800 MB each | The numbers match the paper, which dates from **April 2026** and is already in the wiki. The wiki records about 2.2 GB of checkpoints for an earlier preview release; the 800 MB figure was not checked against the current release. |

## Why the physical-AI cluster matters

This section is the wiki's reading, not the video's.

- **MUNDO is close to a hybrid of two approaches this wiki tracks separately.** It uses an authored physics engine for dynamics and a video model only for rendering. That makes it a counterexample to treating [world-model simulators](../concepts/world-models/world-model-simulators.md) as learned-dynamics systems, and its "scene program" resembles a [code world model](../concepts/world-models/code-world-model.md). The physics is inspectable; the rendered pixels are not guaranteed to be consistent with it.
- **Genie 4 and MUNDO make opposite bets on where physics lives:** implicit in a learned model and explicit in a simulator. DeepMind's listed research gaps (complex physical interactions, spatial accuracy, long-term consistency) are what MUNDO's design gets by construction, at the cost of an imperfect proxy of the real scene.
- **PhysAg3D and SimReady attack the same bottleneck from opposite ends:** generating assets on demand versus curating a large library.

## Entities mentioned

- [Genie 3](../entities/genie-3.md), [Google DeepMind](../entities/google-deepmind.md), [Gemini 4 Argon](../entities/gemini-4-argon.md), [Apptronik Apollo](../entities/apptronik-apollo.md)
- [NVIDIA](../entities/nvidia.md), [Unitree G1](../entities/unitree-g1.md), [MuJoCo](../entities/mujoco.md), [Jiajun Wu](../entities/jiajun-wu.md)

## Concepts touched

- [Energy-based models](../concepts/learning/energy-based-models.md)
- [World-model simulators](../concepts/world-models/world-model-simulators.md)

## Chapter index (from the video description)

00:00 intro · 01:10 MotionBricks · 03:11 Idol · 04:27 SceneBloom · 05:48 Unlimited OCR 2 · 06:57 UniAction · 08:00 AutoSwarm · 08:48 Paradee 1.2 · 10:02 Hy-SimulMT · 11:42 NVIDIA SimReady Assets · 12:55 OpenAI scientific discoveries · 18:10 Luma (sponsor) · 19:22 Anthropic IPO · 22:48 MatAnyone-E · 24:02 Open-H3-Regenerate-2K · 25:19 StreamVibe · 26:26 MUNDO · 27:40 GPT-6.1 Terra · 29:35 Gemini 4 Carbon · 32:04 NVIDIA Nemotron 3.5 Transcribe · 33:24 Genie 4 · 35:14 PhysAg3D · 36:24 SLEEP · 38:29 Audio8 TTS · 39:53 SenseNova Code2Video · 40:47 Energy-based model · 41:53 OverSeer · 43:03 Nanbeige4.3-33B · 44:17 LFM3 · 46:12 Apex 35B · 47:33 Groot · 49:23 Clover 35B · 50:44 Spark-X2.6-1.7B · 51:58 SenseNova-Loop 9B

> [!note] "Groot" at 47:33 is not checked
> The description links it to `huggingface.co/GrootTeam/models`. That is not obviously NVIDIA's [GR00T](../entities/nvidia-groot.md), and it sits in the video's open LLM run, so do not assume they are related.

## Open questions

- Full paper ingests for MUNDO, OverSeer, UniAction and PhysAg3D are not done; this page relies on project pages and READMEs. See the [backlog](../backlog.md).
- MUNDO's method has no quantitative robot result yet. Its release at the end of November is the first chance to test the sim-to-real claim implied by its Real-to-Sim framing.
