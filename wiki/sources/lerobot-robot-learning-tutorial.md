---
title: "Robot Learning: A Tutorial (LeRobot — HF Space + arXiv 2510.12403)"
type: source
url: https://huggingface.co/spaces/lerobot/robot-learning-tutorial
live_url: https://lerobot-robot-learning-tutorial.hf.space
arxiv: https://arxiv.org/abs/2510.12403
author: Francesco Capuano, Caroline Pascal, Adil Zouitine, Thomas Wolf, Michel Aractingi
affiliations: Hugging Face (LeRobot team)
published: 2025-10-14
ingested: 2026-05-25
tags: [lerobot, tutorial, pedagogy, imitation-learning, vla, smolvla, pi0, act, diffusion-policy, hugging-face, hf-space, primary-source]
---

## Summary

**"Robot Learning: A Tutorial"** — the **official LeRobot pedagogical reference** by the Hugging Face LeRobot team (Capuano, Pascal, Zouitine, Wolf, Aractingi). Published as **arXiv 2510.12403 (Oct 14, 2025)** and as an **interactive Hugging Face Space** that renders the same content with embedded code examples. 410 likes on the Space at ingest time. Covers the modern robot-learning landscape end-to-end: Classical Robotics → Reinforcement Learning → Imitation Learning → Generalist Policies (VLAs), with **ready-to-use `lerobot` code examples** at every step.

This is the **closest published equivalent to the wiki's own [Robot-learning curriculum](../syntheses/curriculum/robot-learning-curriculum.md)** — both are pedagogical paths into robot-learning, both target practitioners + researchers, both anchor on `lerobot`. The two are complementary: the LeRobot tutorial is denser and code-anchored from the start; the wiki's curriculum builds bottom-up from neurons through LeWorldModel with PushT as the connecting thread.

## Chapter structure (from the rendered HF Space)

1. **Foreword**
2. **Introduction**
3. **Classical Robotics**
   - Explicit and Implicit Models
   - Different Types of Motion
   - Example: Planar Manipulation
   - Limitations of Dynamics-based Robotics
4. **Robot (Reinforcement) Learning**
   - A (Concise) Introduction to RL
   - Adding Feedback Loops
   - Real-world RL for Robotics
   - Code Example: Real-world RL
   - Limitations of RL in Real-World Robotics: Simulators and Reward Design
5. **Robot (Imitation) Learning**
   - A (Concise) Introduction to Generative Models (VAEs, Diffusion Models, Flow Matching)
   - **[Action Chunking with Transformers (ACT)](../entities/act.md)** — Code Example: Training and Using ACT in Practice
   - **[Diffusion Policy](../entities/diffusion-policy.md)** — Code Example: Training and Using Diffusion Policies in Practice
   - Optimized Inference — Code Example: Using Async Inference
6. **Generalist Robot Policies**
   - Preliminaries: Models and Data — The dataset class design / LeRobotDataset / Code Example: Batching a (Streaming) Dataset / Code Example: Collecting Data
   - VLMs for VLAs
   - **VLAs** — π₀ (Code Example: Using π₀) and **SmolVLA** (Code Example: Using SmolVLA)
7. **Conclusions**

## Key claims

- **Single canonical pedagogical artifact** from the LeRobot team that ties together the wiki's IL + RL + VLA coverage into one narrative arc.
- **Code-first**: every major concept has a runnable `lerobot` example. Models referenced in the Space metadata:
  - `fracapuano/robot_learning_tutorial_act_example_model` (+ pipeline)
  - `fracapuano/robot_learning_tutorial_diffusion_example_model`
  - `fracapuano/smolvla_async`
  - `lerobot/pi0_base`
  - `lerobot/smolvla_base`
  - `microsoft/resnet-18`
- **Datasets** used in examples: `lerobot/example_hil_serl_dataset`, `lerobot/svla_so101_pickplace` — the latter is on the [SO-ARM101](../entities/so-arm101.md) platform, anchoring the IL examples to the wiki's affordable-robot tier.
- **Generative-model coverage** is unusually broad for a robot-learning tutorial — VAEs + Diffusion + [Flow Matching](../concepts/learning/flow-matching.md) all introduced in one chapter, then specialized into Diffusion Policy + π₀'s flow matching downstream.
- **Async inference** has its own subsection — practical concern for high-rate-control deployment that most academic papers skip.
- **VLAs front and center**: π₀ and SmolVLA are the named exemplars. SmolVLA is Hugging Face's own VLA; π₀ is Physical Intelligence's flow-matching VLA.

## Abstract (from arXiv)

> "Robot learning is at an inflection point, driven by rapid advancements in machine learning and the growing availability of large-scale robotics data. This shift from classical, model-based methods to data-driven, learning-based paradigms is unlocking unprecedented capabilities in autonomous systems. This tutorial navigates the landscape of modern robot learning, charting a course from the foundational principles of Reinforcement Learning and Behavioral Cloning to generalist, language-conditioned models capable of operating across diverse tasks and even robot embodiments. This work is intended as a guide for researchers and practitioners, and our goal is to equip the reader with the conceptual understanding and practical tools necessary to contribute to developments in robot learning, with ready-to-use examples implemented in `lerobot`."

## Entities mentioned

- [LeRobot](../entities/lerobot.md) — the framework the tutorial uses throughout.
- [Hugging Face](../entities/hugging-face.md) — publisher; LeRobot maintainer.
- [SO-ARM101](../entities/so-arm101.md) — the hardware substrate for the IL code examples (via `svla_so101_pickplace` dataset).
- [ACT](../entities/act.md) — covered in the IL chapter as the canonical action-chunking method.
- [Diffusion Policy](../entities/diffusion-policy.md) — covered alongside ACT.
- [DDPM](../entities/ddpm.md) — substrate for the diffusion-policy material.
- [π0](../entities/pi-zero.md) — featured VLA exemplar; full entity filed 2026-05-25 alongside the π0 paper deepening.
- [SmolVLA](../entities/smolvla.md) — Hugging Face's affordable-VLA; full entity filed 2026-05-25 alongside the SmolVLA paper ingest. **Several of the tutorial's authors (Capuano, Pascal, Zouitine, Aractingi, Wolf, Cadene) are also SmolVLA co-authors.**
- [Physical Intelligence](../entities/physical-intelligence.md) — π0's lab.

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md) — entire chapter; this tutorial is now the wiki's canonical pedagogical reference for IL.
- [VLA models](../concepts/learning/vla-models.md) — entire chapter; π0 + SmolVLA + VLM-for-VLA framing.
- Generative models — VAE / Diffusion / Flow Matching introduced as preliminaries to IL.
- Async inference — practical deployment topic; now also documented operationally in the [SmolVLA paper §3.3](smolvla-paper.md).

## Open questions

- ~~**π0 entity**~~ — **filed 2026-05-25** as [pi-zero.md](../entities/pi-zero.md) via the [π0 paper full-HTML deepening ingest](pi-zero-paper.md).
- ~~**SmolVLA entity**~~ — **filed 2026-05-25** as [smolvla.md](../entities/smolvla.md) via the [SmolVLA paper ingest](smolvla-paper.md).
- **Francesco Capuano + co-authors** — LeRobot/HF team; no individual entity pages yet, though [Remi Cadene](../entities/remi-cadene.md) is filed.
- **Reproducibility of the code examples** — the examples target Capuano-hosted HF models (`fracapuano/...`); whether they remain stable as `lerobot` evolves is an open question.
- **Relationship to wiki's own curriculum** — the [Robot-learning curriculum](../syntheses/curriculum/robot-learning-curriculum.md) is bottom-up from neurons; the LeRobot tutorial is mid-stack-first (jumps into RL/IL/VLA with ML prerequisites assumed). Likely complementary entries on the same map; worth a synthesis comparing the two pedagogical paths once readers have used both.

## Why this matters

- **First HuggingFace Space ingest** in this wiki. The Space form factor matters here — the interactive code examples are first-class, not appendix material. This is "documentation as living artifact."
- **The official LeRobot pedagogy**. The wiki's existing curriculum syntheses are user-authored; this is the team-authored canonical. Both can coexist as different paths into the same material.
- **Single coherent source for π₀ + SmolVLA + ACT + Diffusion Policy** in one narrative — the wiki has each of these as scattered references, this tutorial ties them together.
- **The "robot learning at an inflection point" framing** is becoming a standard 2025–2026 narrative across [the Stanford AI Index 2026](stanford-hai-ai-index-2026.md), [the EgoScale scaling-law paper](egoscale-paper.md), and now this tutorial. The published consensus is that the IL/VLA stack has consolidated enough to be teachable as a standard curriculum.
