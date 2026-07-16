---
title: BeingBeyond
type: entity
subtype: company
created: 2026-07-15
updated: 2026-07-15
sources: 1
tags: [beingbeyond, humanoid, whole-body-control, peking-university, zongqing-lu, china, robot-learning]
---

# BeingBeyond

**BeingBeyond** (智在无界) — a robot-learning group/company working on **humanoid [whole-body control](../concepts/robotics/whole-body-control.md)**, closely tied to **Peking University** and led by **[Zongqing Lu](zongqing-lu.md)** (corresponding author, lu@beingbeyond.com). Source of **[BumbleBee](../sources/bumblebee-experts-to-generalist-wbc.md)**, the expert→generalist WBC framework that reaches SOTA general whole-body control on a real [Unitree G1](unitree-g1.md).

## What it works on

- **Agile humanoid whole-body control** — the [BumbleBee](../sources/bumblebee-experts-to-generalist-wbc.md) line: cluster human-motion data, train per-cluster RL experts with iterative delta-action sim-to-real, distill into one Transformer generalist. Project hub: [beingbeyond.github.io/BumbleBee](https://beingbeyond.github.io/BumbleBee/).
- Positions against the NVIDIA-GEAR WBC line ([SONIC](../sources/sonic-paper.md), [HOVER](../sources/nvidia-gear-publications.md)) and academic baselines (OmniH2O, Exbody2, HumanPlus) — a **data-level "decompose the complexity"** approach vs. GEAR's **model-level "scale one policy"** approach.

## Why it matters in this wiki

- A **China-based humanoid-WBC group** entering the wiki's mostly-US humanoid coverage; the counterweight-by-method to NVIDIA GEAR on the same [Unitree G1](unitree-g1.md) platform.
- Demonstrates SOTA WBC on **modest compute** (2× RTX 4090 desktops) — a data-curation-over-scale story.

## Related

- [Zongqing Lu](zongqing-lu.md) — lead / corresponding author.
- [Whole-body control](../concepts/robotics/whole-body-control.md) — its research area.
- [Unitree G1](unitree-g1.md) — its target robot.
- [NVIDIA GEAR](nvidia-gear.md) — the parallel (model-scaling) WBC program.

## Mentioned in

- [BumbleBee — From Experts to a Generalist](../sources/bumblebee-experts-to-generalist-wbc.md) — the company's primary source.

## Open questions

- Company vs. academic-lab status, funding, headcount, and other products beyond BumbleBee — not surfaced by the single ingested source.
