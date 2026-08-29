---
title: "MolmoAct: Action Reasoning Models that can Reason in Space"
type: source
url: https://arxiv.org/abs/2508.07917
author: "Jason Lee, Jiafei Duan, Haoquan Fang (equal contribution), Yuquan Deng, Shuo Liu, et al.; Ali Farhadi, Dieter Fox, Ranjay Krishna (senior)"
affiliation: Allen Institute for AI, University of Washington
published: 2025-08-11
ingested: 2026-08-03
venue: arXiv preprint (2508.07917, v4 2025-09-18)
format: research paper (61 pp)
local_path: raw/2508.07917.pdf
sha256: 5cbeae70c9ee4efcd34897fa2e8d516641583c5f3e749217dba3310a9a66e23e
tags: [molmoact, action-reasoning-model, vla, depth-tokens, visual-trace, steerability, franka, libero, simplerenv, ai2, open-source, open-data, primary-source]
---

## Summary

**The MolmoAct v1 primary — closing the wiki's last secondhand gap in the Ai2 robotics line.** Previously known only through [VLA-0's table](vla-0-paper.md), [MolmoAct2's](molmoact2-paper.md) description of its predecessor, and its role as the supervised policy in [Anthropic's evaluation](anthropic-how-claude-performs-on-robotics-tasks.md).

Introduces **Action Reasoning Models (ARMs)**: instead of mapping perception + instruction directly to control, the model reasons through a **structured three-stage autoregressive pipeline**, each stage independently decodable:

1. **Depth Perception Tokens** — a 2.5D reconstruction of the scene (decodable to a depth map);
2. **Visual Reasoning Trace Tokens** — a mid-level spatial plan as a 2D trajectory over the image (decodable to a trace overlay);
3. **Action Tokens** — the low-level control commands.

The pitch is **explainability and steerability**: you can *see* the plan before it executes, and you can *edit the trace* to redirect the robot — which the paper finds "more reliable than language commands, which can suffer from ambiguity." Fully open: weights, training code, and all datasets.

## The robots (answering the wiki's standing question first-hand)

- **Real hardware: Franka, in two configurations** — a **single-arm Franka** and a **bimanual Franka** setup. For home-environment data collection the single arm was mounted on **"a lightweight, mobile platform similar to [DROID](../entities/droid.md)"**, carried across living rooms, kitchens, bathrooms, and bedrooms.
- **Simulation:** [LIBERO](../entities/libero.md) (Franka Emika Panda, front + wrist 256×256 views, delta-EE actions) and **SimplerEnv (Google Robot)**.
- So the v1 platform story is **Franka-only in the real world** — the YAM / SO-100 / DROID-fleet breadth arrived with [MolmoAct2](molmoact2-paper.md).

## Key claims

### Data
- **Pre-training:** ~**190K robot episodes** from a filtered [Open X-Embodiment](../entities/open-x-embodiment.md) set, plus multimodal web data (captioning, 2D pointing — the [Molmo](../entities/molmo.md) recipe).
- **Mid-training: the MolmoAct Dataset** — **10,689 high-quality trajectories** of the single-arm Franka across **93 tasks** in home + tabletop settings; ~112 timesteps/trajectory; collected over **two months by five full-time operators**. Released openly; training on it adds **+5.5%** average over the base model. *(This is the direct ancestor of MolmoAct2's much larger released-dataset program.)*
- Trace annotations come from **VLM-based pointing** (Molmo, RoboPoint) rather than bounding-box detectors — box-based points "collapse toward box centers" and transfer poorly across embodiments.

### Results
- **SimplerEnv (Google Robot) zero-shot: 70.5%** visual-matching accuracy — surpassing π0 and GR00T N1.5; fine-tuned 71.6/72.1 across splits.
- **[LIBERO](../entities/libero.md): 86.6%** average — consistent with the 86.8 in [VLA-0's table](vla-0-paper.md); +6.3% over ThinkAct on long-horizon.
- **Real-world fine-tuning** (6 tasks, 50 teleop demos each, **25 trials/task**, task-progression metric): **+10% (single-arm)** and **+22.7% (bimanual)** over π0-FAST. Tasks: put_bowl_in_sink, wipe_table, table_bussing; set_table, lift_tray, fold_towel.
- **Out-of-distribution: +23.3%** over baselines.
- **Human preference:** top Elo in arena-style evaluations for open-ended instruction following and trajectory steering.

### Stated limitations
- **Front-camera dependence:** spatial reasoning leans on the front view; end-effector occlusion degrades trace prediction. Proposed fix: wide-FoV camera + SLAM-generated traces ("temporal rather than purely spatial reasoning").
- **Steerability requires trace quality/diversity** and broad action-composition coverage in post-training data.

## Entities mentioned
- [Ai2](../entities/ai2.md) · University of Washington · [MolmoAct](../entities/molmoact.md) · [Molmo](../entities/molmo.md) · [Franka Panda](../entities/franka-panda.md) · [DROID](../entities/droid.md) (mobility-platform design) · [Open X-Embodiment](../entities/open-x-embodiment.md) · [LIBERO](../entities/libero.md)
- Baselines: [π0](../entities/pi-zero.md) / π0-FAST, [GR00T N1.5](../entities/nvidia-groot.md), [OpenVLA](../entities/openvla.md), [Octo](../entities/octo.md), RT-1/RT-2-X, SpatialVLA, TraceVLA, ThinkAct

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) — the ARM framing is a structured-reasoning variant of the paradigm.
- [Chain-of-thought](../concepts/learning/chain-of-thought.md) — depth→trace→action is embodied CoT with *decodable* intermediate steps.
- [Adaptive-depth reasoning](../concepts/learning/adaptive-depth-reasoning.md) — MolmoAct2 makes stage 1 adaptive; here it runs every step (the latency cost MolmoAct2 fixes).
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — arena-style Elo for policies predates [RoboArena](roboarena-paper.md)'s formalization of pairwise preference.

## Open questions
- **Trace-editing steerability is the paper's most distinctive contribution** and did not carry visibly into the wiki's MolmoAct2 record — whether MolmoAct2 retains editable traces is not recorded. Worth checking on next contact with that line.
- **n=25/task real-world, task-progression metric** — per the [audit](../syntheses/platforms/vla-success-rate-audit.md), fine-grained orderings don't separate; the +22.7 bimanual gap is the robust one.
- The paper's Elo arena evaluation is an early instance of preference-based policy evaluation — its protocol (raters, comparisons count) wasn't captured at this depth.

## Related sources
- [MolmoAct2 paper](molmoact2-paper.md) — the successor; +10.6 LIBERO, hybrid continuous head, YAM/SO-100/DROID breadth.
- [VLA-0 paper](vla-0-paper.md) — the cross-method table that was this page's prior grounding.
- [How Claude Performs on Robotics Tasks](anthropic-how-claude-performs-on-robotics-tasks.md) — MolmoAct as the supervised policy.
- [Molmo and PixMo](molmo-pixmo-paper.md) — the VLM lineage underneath.
