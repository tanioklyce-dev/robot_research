---
title: Runway
type: entity
subtype: company
created: 2026-11-12
updated: 2026-11-12
sources: 4
tags: [runway, video-generation, world-model, world-action-model, gen-4-5, praxis-1, open-weights, cosmos-coalition, physical-ai]
---

# Runway

**A generative-video company that moved into robotics, starting from video generation rather than robot data.** Its video models include the Gen line (e.g. Gen-4.5), the interactive world models Solaris and GWM Worlds 2, and **[Praxis-1](praxis-1.md)**, an open-weight world-action model released in November 2026 ([launch](../sources/runway-praxis-1-launch.md)).

## Robotics thesis

- **Video, not teleoperation, is the scalable data source.** *"Real-world data is scarce… Video, however, is effectively limitless."* Runway reports that policy quality improves as third-person video scales, and that web video ties teleoperated robot video as pretraining. That tie is shown on a single placement-error proxy (16.1 vs 16.0 cm) ([September post, in launch source](../sources/runway-praxis-1-launch.md)).
- **World models as evaluators.** Runway claims policy rollouts simulated inside its world model predict real-world results with **0.95 correlation**. This is not yet backed by an ingested primary.
- **Policies and LLM agents are complementary.** An agent plans a task and a fast policy carries out each step. Runway's own comparison has [GPT-6 Astra](gpt-6-astra.md) 15.6× slower and 51× more expensive per task than Praxis-1 ([report §7.3](../sources/runway-praxis-1-technical-report.md)).

## Positioning

- **The same path as [Black Forest Labs](black-forest-labs.md).** Both are generative-video labs that turned their video model into an action model, FLUX 3 Action for BFL and Praxis-1 for Runway. BFL decodes actions from a frozen backbone, while Runway fine-tunes the whole model with the video loss kept on. Runway's report benchmarks directly against FLUX 3 Action on BFL's own published tasks.
- **Open weights as a political argument.** The launch frames Apache-2.0 release as part of *"U.S. leadership in physical AI"*. Runway calls itself a **founding member of the Cosmos Coalition** with [NVIDIA](nvidia.md) ([launch](../sources/runway-praxis-1-launch.md)).
- **Launch partners:** Noble Machines (legged humanoid / bimanual), [Standard Bots](standard-bots.md) (RO1 six-axis arm) and Ultra (dual-arm warehouse robot / mobile base). Positronic operated the Franka FR3 used for the real-robot evaluations.

## Related

- [Praxis-1](praxis-1.md) · [FLUX 3](flux-3.md) · [Black Forest Labs](black-forest-labs.md) · [NVIDIA Cosmos](nvidia-cosmos.md)
- [World-action model](../concepts/world-models/world-action-model.md)

## Mentioned in

- [Praxis-1 Is Now Available (launch)](../sources/runway-praxis-1-launch.md)
- [Praxis-1 technical report](../sources/runway-praxis-1-technical-report.md)
- [praxis-1-oss GitHub README](../sources/praxis-1-oss-github.md)
- [FLUX 3 launch](../sources/flux-3-launch.md) — Runway Gen-4.5 as a video-preference baseline (BFL claims a 77% preference win).
