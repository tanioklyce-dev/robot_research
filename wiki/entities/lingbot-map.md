---
title: LingBot-Map
type: entity
subtype: model
created: 2026-08-13
updated: 2026-08-13
sources: 4
tags: [lingbot-map, robbyant, ant-group, 3d-reconstruction, slam, feed-forward, streaming, transformer, paged-kv-cache, apache-2-0]
---

**LingBot-Map** — *"a feed-forward 3D foundation model for reconstructing scenes from streaming data"*, from **[Robbyant](robbyant.md)** (Ant Group robotics). **16,471★ / 1,837 forks** four months after release, **Apache-2.0**, weights on Hugging Face **and** ModelScope. arXiv 2604.14141. Primary source: [repo](../sources/lingbot-map-github.md).

The learned, amortized answer to what [RTAB-Map](rtab-map.md) and classical SLAM solve by optimization.

## Claims

- **Geometric Context Transformer** — unifies *"coordinate grounding, dense geometric cues, and long-range drift correction"* in one streaming framework via **anchor context**, **pose-reference window**, and **trajectory memory**.
- **~20 FPS at 518×378** over sequences **>10,000 frames**, using **paged KV cache attention**.
- SOTA *"compared to both existing streaming and iterative optimization-based approaches."* Benchmarks: **KITTI**, **Oxford Spires** (scripts released). Worked example: a **~25,000-frame, 13-minute** indoor walkthrough.

> [!note] Drift correction moved from the optimizer into the architecture
> Classical SLAM handles long-horizon drift with **loop closure + back-end factor-graph optimization** ([GTSAM](gtsam.md)-class). LingBot-Map folds it into the transformer — no explicit optimizer, no loop-closure detector, no map to re-solve. The 25,000-frame demo *is* the claim. If it survives independent evaluation it is a real architectural shift.

> [!note] Paged KV cache — LLM serving infrastructure migrating into perception
> Paged attention comes from LLM inference (vLLM). Using it here treats **frames like tokens and the map like a KV cache**, which is what makes 10,000+ frame sequences tractable. Same pattern as [DimOS](dimos.md) inheriting [LangGraph](langgraph.md) for robot agents: **serving infrastructure built for language models is moving into robotics.**

> [!warning] ~20 FPS on unstated hardware — and 16.5k stars is reach, not quality
> The headline rate names **no device**; `bf16`, `--compile`, and FlashInfer all imply a workstation or datacentre GPU. For [XLeRobot](xlerobot.md)'s Orin NX the relevant number is edge latency, **and it is not published** — the same omission the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) keeps finding.
>
> And the repo is four months old with **no accuracy table in the README**, having shipped and fixed **two KV-cache correctness bugs** in three months, both of which degraded pose and reconstruction quality at longer sequences. Hold the SOTA claim until the paper or an independent benchmark is read.

## Related

- [Robbyant](robbyant.md) — the lab, and Ant Group's wider physical-AI program
- [RTAB-Map](rtab-map.md), [GTSAM](gtsam.md) — the classical alternative
- [Niantic Spatial](niantic-spatial.md) — the independent feed-forward play, from AR rather than robotics
- [Visual relocalization and mapping](../concepts/robotics/visual-relocalization-and-mapping.md)

## Open questions

- **Paper un-ingested** (arXiv 2604.14141) — every quantitative claim lives there.
- **What hardware gives ~20 FPS?** Decides deployability.
- **SLAM replacement or reconstructor only?** Relocalization against a prior map — what [RTAB-Map](rtab-map.md)'s localization-only mode gives the [XLeRobot plan](../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md) — is not described.

## Mentioned in

- [LingBot-Map GitHub repository](../sources/lingbot-map-github.md)
