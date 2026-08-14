---
title: LingBot-Map — Geometric Context Transformer for Streaming 3D Reconstruction (Robbyant, 2026)
type: source
url: https://github.com/Robbyant/lingbot-map
author: Robbyant Team (Ant Group robotics)
published: 2026-04-15 (repo created; arXiv 2604.14141; last push 2026-08-12)
ingested: 2026-08-13
license: Apache-2.0
tags: [lingbot-map, robbyant, ant-group, 3d-reconstruction, slam, feed-forward, streaming, transformer, kv-cache, foundation-model, kitti, oxford-spires, primary-source]
---

## Summary

**LingBot-Map** — *"a feed-forward 3D foundation model for reconstructing scenes from streaming data"* from **Robbyant**, Ant Group's robotics arm. **16,471★ / 1,837 forks** four months after creation, **Apache-2.0**, weights on both Hugging Face and ModelScope. arXiv **2604.14141**.

It is the learned, amortized answer to the problem [RTAB-Map](../entities/rtab-map.md) and classical SLAM solve by optimization — and the star count makes it, by that measure, one of the most-adopted single artifacts in this wiki.

## Key claims

Three, as the README states them:

- **Geometric Context Transformer** — *"architecturally unifies coordinate grounding, dense geometric cues, and long-range drift correction within a single streaming framework through **anchor context**, **pose-reference window**, and **trajectory memory**."*
- **High-efficiency streaming inference** — *"a feed-forward architecture with **paged KV cache attention**, enabling stable inference at **~20 FPS on 518×378** resolution over long sequences **exceeding 10,000 frames**."*
- **State-of-the-art reconstruction** — *"compared to both existing streaming and iterative optimization-based approaches."*

Evaluation is on **KITTI** and **Oxford Spires**, with the benchmark scripts released (2026-05-25). A published worked example runs a **~25,000-frame, 13-minute indoor walkthrough**.

Engineering detail from the changelog, which is unusually candid about its own bugs:
- **2026-04-24** — a FlashInfer KV-cache bug silently cached non-keyframes when `--keyframe_interval > 1`. *"You should now see better pose and reconstruction quality when running with more than 320 frames."*
- **2026-06-28** — an SDPA KV-cache fix; FlashInfer still recommended for best performance.
- `--compile` support, `bf16`, windowed inference for sequences >3,000 frames, sky masking.

## Analysis

> [!note] Drift correction is the hard part, and it is architectural here
> Classical SLAM handles long-horizon drift with **loop closure plus back-end optimization over a factor graph** ([GTSAM](../entities/gtsam.md)-class). LingBot-Map instead folds *"long-range drift correction"* into the transformer via **trajectory memory** and a **pose-reference window** — no explicit optimizer, no loop-closure detector, no map to re-solve. That the demo is a **25,000-frame walkthrough** is the claim being made: drift is handled implicitly and holds over thirteen minutes.
>
> If that survives independent evaluation it is a genuine architectural shift, and the honest caveat is that **this wiki has read the README, not the paper or a third-party benchmark.**

> [!note] Paged KV cache — an LLM-serving technique carried into geometry
> **Paged attention** comes from LLM inference (vLLM's contribution to memory-efficient long-context serving). Applying it to a streaming reconstruction model treats **frames like tokens and the map like a KV cache** — which is what makes 10,000+ frame sequences tractable at all. Worth noting as an instance of a pattern: **serving infrastructure built for language models is migrating into perception**, the same way [DimOS](../entities/dimos.md) inherited [LangGraph](../entities/langgraph.md) for robot agents.

> [!warning] ~20 FPS on unstated hardware
> The headline rate carries **no device**. `bf16`, `--compile`, and FlashInfer all imply a datacentre or workstation NVIDIA GPU, not a robot. For this wiki's purposes — [XLeRobot](../entities/xlerobot.md)'s Orin NX, the [Jetson ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md) — **the number that matters is edge latency, and it is not published.** Same gap the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) keeps finding: an impressive rate quoted without the compute class it required.

> [!note] Ant Group now has a full-stack physical-AI program, and this wiki has been meeting it in pieces
> Four separate entries, never connected until now:
> - **LingBot-VLA** — Ant Group's manipulation foundation model ([top-10 physical AI models](top-10-physical-ai-models-2026.md))
> - **LingBot-World** — a world model, **5th of 10** on [WorldRoamBench](worldroambench-paper.md) (64.25 overall; physics 47.32)
> - **LingBot-Map** — this, the geometric-reconstruction layer
> - **[UME](../entities/ume.md)** — the torque-feedback teleoperation exoskeleton and data-collection rig, also Ant Group (with Stanford)
>
> That is **policy + world model + map + data collection**, published openly, from one company. The wiki has been filing them as unrelated one-offs. Recorded on [Robbyant](../entities/robbyant.md).

> [!warning] 16.5k stars is not evidence of quality
> It is evidence of *attention*. The repo is four months old, the README publishes no accuracy table (the numbers are in the paper and the released benchmark scripts), and two KV-cache correctness bugs shipped and were fixed inside three months — both of which materially affected output quality at longer sequences. Read the star count as reach, and hold the SOTA claim until the paper or an independent benchmark is read.

## Entities mentioned

- [LingBot-Map](../entities/lingbot-map.md) — the subject · [Robbyant](../entities/robbyant.md) — the lab
- [RTAB-Map](../entities/rtab-map.md), [GTSAM](../entities/gtsam.md) — the classical stack it competes with
- [Niantic Spatial](../entities/niantic-spatial.md) — the independent feed-forward reconstruction play
- [UME](../entities/ume.md) — the other Ant Group robotics artifact here

## Concepts touched

- [Visual relocalization and mapping](../concepts/robotics/visual-relocalization-and-mapping.md)
- [World models](../concepts/world-models/world-model.md) — the adjacent tradition

## Open questions

- **Paper un-ingested** (arXiv 2604.14141) — all quantitative claims live there. KITTI and Oxford Spires numbers, and the comparison set, are unread.
- **What hardware gives ~20 FPS?** Unstated, and it decides whether this is deployable on a robot or only in a datacentre.
- **Is it usable as a SLAM replacement, or only a reconstructor?** Pose output is implied by *"better pose and reconstruction quality"*, but relocalization against a prior map — the thing [RTAB-Map](../entities/rtab-map.md)'s localization-only mode gives the [XLeRobot plan](../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md) — is not described.
- **What is "Robbyant"** and how does it relate to Ant Group formally? The name appears on the repo and at `technology.robbyant.com` with no corporate description read here.
