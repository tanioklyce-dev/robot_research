---
title: Helix — Vision-Language-Action Model for Humanoid Control (Figure AI blog, Feb 2025)
type: source
url: https://www.figure.ai/news/helix
author: Figure AI
affiliation: Figure AI
published: 2025-02-20
ingested: 2026-05-10
created: 2026-05-10
updated: 2026-05-10
tags: [helix, figure, vla, humanoid, system-1-system-2, hierarchical-policy, onboard-inference]
---

> [!note] Ingest depth
> This source page is **based on the Figure AI blog post**, not a peer-reviewed paper. Architectural and training-data claims come from Figure's marketing copy and have **not been independently verified**. Filed as part of the curriculum-driven backfill for [Module 9 (VLA models)](../syntheses/curriculum/robot-learning-curriculum.md).

## Summary

**Helix** — [Figure AI](../entities/figure.md) (announced 2025-02-20). A **two-tier vision-language-action model** for the [Figure 02](../entities/figure.md) humanoid using a **System 1 / System 2 architecture**: a 7B-parameter internet-pretrained VLM ("S2") runs at 7–9 Hz for slow scene understanding and language reasoning; an 80M-parameter transformer-based visuomotor policy ("S1") runs at 200 Hz for high-rate continuous control. End-to-end gradient flows between the two. Demonstrates several Figure-claimed firsts including full humanoid upper-body continuous control (wrists, torso, head, individual fingers), multi-robot collaboration on shared long-horizon tasks, generalization to "thousands" of unseen household objects via natural-language prompts, and onboard inference on embedded low-power GPUs. Trained on **~500 hours of teleoperated demonstrations** ("<5%" the size of typical VLA datasets according to Figure).

## Verbatim claims (from blog)

> "Helix is the first VLA to output high-rate continuous control of the entire humanoid upper body, including wrists, torso, head, and individual fingers."

> "First VLA to operate simultaneously on two robots, enabling them to solve a shared, long-horizon manipulation task with items they have never seen before."

> "Pick up virtually any small household object, including thousands of items they have never encountered before, simply by following natural language prompts."

> "Runs entirely onboard embedded low-power-consumption GPUs."

## Key claims

- **System 1 / System 2 split.**
  - **S2:** 7B-parameter internet-pretrained VLM @ 7–9 Hz. "Thinks slow." Scene understanding, language comprehension, high-level intent.
  - **S1:** 80M-parameter transformer visuomotor policy @ 200 Hz. "Thinks fast." Precise continuous robot actions.
  - Decoupled rates allow each component to specialize.
  - End-to-end gradient propagation between S1 and S2.
- **Full humanoid upper-body continuous control** — claimed as first-of-kind in VLAs. Wrists, torso, head, individual fingers.
- **Multi-robot collaboration** — two Figure 02 humanoids cooperating on a shared long-horizon manipulation task with novel objects.
- **Object generalization** — "thousands" of unseen household objects via language prompts.
- **Single weight set** — one model across diverse tasks, no task-specific fine-tuning.
- **Onboard inference** — runs on embedded low-power GPUs (commercial-readiness pitch).
- **Training scale** — ~500 hours teleoperated demos. Auto-labeling pipeline uses VLM to generate hindsight instructions from video clips.

## Why it matters in this wiki

- **Architecturally the most novel of the four backfill ingests.** The S1/S2 hierarchical split — slow-VLM-as-planner + fast-policy-as-controller, with end-to-end gradients — is a structural pattern that's becoming load-bearing across VLAs (similar splits appear in NVIDIA GR00T N1 and elsewhere). Worth tracking in [VLA models concept](../concepts/learning/vla-models.md).
- **Closes a long-standing open question on the [Figure entity](../entities/figure.md).** Helix had been referenced via the entity page only; the primary source is now filed.
- **Data-efficiency claim.** "<5%" of a typical VLA dataset is striking enough to warrant cross-checking against [GR00T](../entities/nvidia-groot.md)'s 20,854 hours of egocentric video pretraining — different training-data flavors but worth comparing in any VLA-data-economics synthesis.

## Confidence flags

> [!warning] Vendor blog, not peer-reviewed
> All architectural and training-data details come from a single Figure AI blog post. Numbers (parameter counts, frequencies, hours of data) are Figure's claims, not independently verified. Treat as marketing-grade until replicated in a paper or third-party evaluation.

## Entities mentioned

- [Figure](../entities/figure.md) — the humanoid platform; Helix is its VLA.
- [NVIDIA GR00T](../entities/nvidia-groot.md) — sibling/competing humanoid VLA.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — Helix is an instance with an unusual hierarchical structure.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — orthogonal pattern (LLM-emits-tool-calls); contrast.

## Open questions / TBD

- **No paper.** Figure has not (as of ingest date) released a Helix paper. Architectural details may be incomplete.
- **System-1-System-2 as a concept page.** If the pattern shows up in 2+ more wiki sources (it likely will), promote `concepts/system-1-system-2-policy.md` from a vla-models.md subsection to its own page.
- **Specs for Figure 03** — referenced as the next-gen platform; not detailed in the Helix blog.
- **How does Helix relate to Figure's earlier OpenAI-partnership work?** The OpenAI partnership dissolved in 2024; Helix is Figure's first VLA developed in-house.
