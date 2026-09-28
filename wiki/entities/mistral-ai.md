---
title: Mistral AI
type: entity
subtype: company
created: 2026-09-28
updated: 2026-09-28
sources: 1
tags: [mistral, company, france, llm, vlm, robotics, navigation, robostral]
---

# Mistral AI

**Mistral AI** is a Paris-based frontier-model lab known for its LLMs (Mistral 7B, Mixtral, and the Pixtral / Ministral vision-language line). In July 2026 it made its first move into robotics with **Robostral Navigate**, an 8B instruction-following navigation model ([paper](../sources/robostral-navigate-paper.md)).

## Robotics: Robostral Navigate (2026-07)

- **What it is.** An in-house 8B VLM, specialized for pointing, counting and localization, fine-tuned to navigate from a **single RGB camera** by **pointing at the next waypoint** in the image, with a metric-displacement fallback. A 121M diffusion transformer and a per-robot tracker turn waypoints into motion ([paper](../sources/robostral-navigate-paper.md)).
- **How it was trained.** Sim-only (2.4M trajectories, 350k scenes), with prefix-tree episode packing (22× fewer tokens) and online RL via CISPO. It is explicitly a transfer of LLM post-training infrastructure (vLLM rollouts, group-relative RL) into embodied control. The blog puts it as "we leverage our knowledge of post-training LLMs at scale."
- **Claims.** R2R-CE val-unseen **77.4%** SR (paper; the launch blog said 76.6%) and RxR-CE **75.1%**. It is shown on a [Galaxea R1](galaxea-r1.md) and a [Hiwonder](hiwonder.md) JetAuto with shared weights. The benchmark numbers use Habitat's pathfinder between predicted waypoints; see the caveat on the [source page](../sources/robostral-navigate-paper.md).
- **Availability.** **Closed.** No weights, code or data; commercial access via the sales team. It is pitched at "manufacturing, delivery, logistics, and hospitality." The blog calls it "only the first step toward a unified embodied agent" and is recruiting.

## Why it matters in this wiki

- **Another frontier LLM lab enters robotics**, alongside [Google DeepMind](google-deepmind.md) (Gemini Robotics) and the Qwen team (Qwen-VLA / Qwen-RobotNav). Mistral starts with **navigation**, the domain the [visual navigation policies](../concepts/robotics/visual-navigation-policies.md) page calls the solved cross-embodiment scope, rather than manipulation.
- **The recipe is LLM-lab-shaped.** Its contributions are training-efficiency (sequence packing, attention masks) and RL post-training. These are Mistral's home skills, and they generalize beyond navigation.
- **Of the European labs, it is closed.** Unlike Mistral's open-weight LLM heritage, this model is not open, so it cannot be reproduced or deployed by anyone evaluating it outside Mistral.

## Related

- [Visual navigation policies](../concepts/robotics/visual-navigation-policies.md) — the MLLM-VLN lineage it tops.
- [Molmo](molmo.md) — the other pointing-first VLM program; Robostral's masking recipe credits Molmo2.
- [Qwen](qwen.md) — Qwen-RobotNav is the strongest baseline in its table.

## Mentioned in

- [Robostral Navigate paper](../sources/robostral-navigate-paper.md) — primary.
