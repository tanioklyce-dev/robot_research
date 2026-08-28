---
title: Pollen Robotics
type: entity
subtype: company
created: 2026-05-09
updated: 2026-08-27
sources: 5
tags: [pollen-robotics, france, bordeaux, hugging-face, open-source, humanoid, reachy, microduck, embodied-ai]
---

**Pollen Robotics** — open-source robotics company in **Bordeaux, France**, **founded in 2016 by former Inria researchers**. **Joined [Hugging Face](hugging-face.md) in April 2025 and is now its robotics team** ([Microduck press kit](../sources/pollen-robotics-microduck.md)). Self-description: *"Expressive, open-source robots for AI builders and makers."*

> [!note] The acquisition changes how to read this company
> Pollen is not an independent French startup that Hugging Face invests in — it *is* Hugging Face's robotics hardware arm. That makes Hugging Face a **robot manufacturer**, not only a framework maintainer, and it is why Pollen's products are documented on the HF Hub (`huggingface.co/docs/reachy_mini`) and train on **Hugging Face Jobs**. See the correction on the [Hugging Face](hugging-face.md) page.

## Products

| | Class | Status |
|---|---|---|
| [Reachy 2](reachy.md) | research bimanual mobile manipulator; 7 DOF/arm; ROS 2 Humble; VR teleop | shipping; price on request |
| [Reachy Mini](reachy-mini.md) | desktop HRI robot — *"AI that interacts"* | **10,000+ shipped** as of Aug 2026 |
| [Microduck](microduck.md) | 25 cm RL biped — *"AI that acts"* | pre-orders 2026-08-27, **$399**, ships before Christmas 2026 |

Reachy Mini and Microduck are described by Pollen as their **first and second consumer robots** — Reachy 2 sits in a different (research-platform) tier.

## Philosophy

Fully open-source **software** across the line (Apache-2.0). The hardware story is less uniform than the marketing implies:

> [!warning] "Open source" means the software, and the company says so
> The [Microduck press kit](../sources/pollen-robotics-microduck.md) instructs press explicitly: *"The open-source statement covers the software stack. The mechanical and electronic design files are not, so please do not describe the robot as open-source hardware."* Meanwhile Reachy 2 is described on its own [product page](../sources/pollen-robotics-reachy.md) as "fully open-source hardware and software," and `microduck_rl` states hardware files are **CC BY-SA-NC**. The line's openness is therefore **per-product and per-layer**, not a blanket property. Check before quoting.

Design philosophy stated at the Microduck launch, applying to both consumer robots: *"both should be fun when you first turn them on, approachable when you start coding, and powerful enough to become serious development platforms as your projects grow."*

## Two software stacks, one parent

Notably, Pollen's robots do **not** all run [LeRobot](lerobot.md), despite sharing a parent with it:

- **Reachy 2** is one of LeRobot's 8 natively-supported platforms ([ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md)).
- **Microduck** ships its own Rust runtime plus an [mjlab](mjlab.md)/PPO training stack with no LeRobot dependency. Its RL repo predates the product repo by eight months.

The apparent split is **imitation-learning manipulation (LeRobot)** vs **RL locomotion (mjlab)** — two different problem classes with two different tool lineages, kept separate rather than forced together. Flagged as an open question on the [Microduck source page](../sources/pollen-robotics-microduck.md).

## People

Microduck core team, per the launch post: **Matthieu Lapeyre**, **Antoine Pirrone**, **Augustin Crampette**, **Coralie Deplane**, **Anne Charlotte Passanisi** — with **Thomas Wolf** (HF co-founder / CSO) as a co-author, another marker of how integrated the two organisations are. Pirrone is also the author of the community **Open Duck Mini** project from which Microduck descends.

## Related

- [Hugging Face](hugging-face.md) — parent since April 2025
- [Reachy 2](reachy.md) · [Reachy Mini](reachy-mini.md) · [Microduck](microduck.md) — the product line
- [LeRobot](lerobot.md) — sibling stack under the same parent
- [mjlab](mjlab.md) — the training framework behind Microduck

## Mentioned in

- [Reachy 2 product page](../sources/pollen-robotics-reachy.md)
- [Microduck — Pollen Robotics launch](../sources/pollen-robotics-microduck.md) — the HF acquisition, Bordeaux/Inria origins, the consumer-robot line, the openness caveat.
