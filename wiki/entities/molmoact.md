---
title: MolmoAct
type: entity
subtype: model
created: 2026-07-17
updated: 2026-08-03
sources: 8
tags: [molmoact, vla, vision-language-action, discrete-tokens, spatial-reasoning, depth-tokens, allen-institute, molmo, baseline]
---

# MolmoAct

**MolmoAct** (Lee et al., 2025 — *MolmoAct: Action Reasoning Models that can Reason in Space*, arXiv 2508.07917) is a **[VLA](../concepts/learning/vla-models.md)** built on the Allen Institute for AI's open **[Molmo](molmo.md)** vision-language model, positioned as an **"action reasoning model"** that reasons about **space** before acting. In the wiki's action-head taxonomy it is a **discrete-token** VLA (like [OpenVLA](openvla.md)).

## Why it matters in this wiki

MolmoAct is one of the **large-scale-action-pretrained** baselines in the wiki's most complete cross-method [LIBERO](libero.md) table — a fully-open (Allen Institute) VLA data point alongside the NVIDIA / Physical Intelligence / Hugging Face entries. It scores **86.8** avg on LIBERO ([VLA-0 paper](../sources/vla-0-paper.md), Table I), placing it **below** [VLA-0](vla-0.md) (94.7, no pretraining), [π0](pi-zero.md) (94.2), and [GR00T-N1](nvidia-groot.md) (93.9) but above plain [OpenVLA](openvla.md) (76.5) and [Octo](octo.md) (75.1) — i.e. a mid-pack discrete-token pretrained VLA. Its distinguishing pitch is **explicit spatial/action reasoning** (reasoning in space, not just emitting actions), which is why the [VLA-0](vla-0.md) authors group it with the discrete-token family while noting its reasoning framing.

> [!note] Superseded by MolmoAct2 (2026)
> **[MolmoAct2](molmoact2.md)** ([Fang, Duan et al. 2026](../sources/molmoact2-paper.md)) is the ingested successor and advances MolmoAct along five axes: a stronger [Molmo2-ER](molmo2-er.md) backbone, three new open datasets, an open-data [FAST](fast-action-tokenization.md) tokenizer, a hybrid **continuous** action head via [per-layer KV conditioning](../concepts/learning/per-layer-kv-conditioning.md), and **adaptive** depth reasoning. MolmoAct2 reports MolmoAct-7B-D at **86.6** on LIBERO (consistent with the 86.8 below) and beats it by **+10.6**. The successor paper is now the wiki's best window into MolmoAct's own design (below).

> [!note] MolmoAct primary (2508.07917) still not directly ingested
> **Primary ingested 2026-08-03** — [MolmoAct paper](../sources/molmoact-paper.md) (arXiv 2508.07917, Ai2 + UW). This page was previously grounded only in the [VLA-0 table](../sources/vla-0-paper.md) and [MolmoAct2](../sources/molmoact2-paper.md)'s description of its predecessor.

## Depth-token reasoning (the "reason in space" mechanism)

Per the [MolmoAct2 paper](../sources/molmoact2-paper.md) §5, MolmoAct's spatial-reasoning step is **depth-token prediction**: before acting, it predicts a compact discrete depth representation (a depth VQ-VAE producing a **10×10 grid** of codes, each one of 128 values) as an intermediate reasoning target that grounds the policy in 3D structure. This is a non-textual **[embodied chain-of-thought](../concepts/learning/chain-of-thought.md)**. Its limitation — re-predicting the **full** depth grid at every control step — is exactly what [MolmoAct2-Think](molmoact2.md)'s [adaptive depth reasoning](../concepts/learning/adaptive-depth-reasoning.md) fixes by only recomputing changed cells.

## Reported numbers (from ingested sources)

- **LIBERO** ([VLA-0 paper](../sources/vla-0-paper.md), Table I): **86.8** avg (Spatial 87.0 / Object 95.4 / Goal 87.6 / Long 77.2), with large-scale action pretraining; rank 6.5. (The [MolmoAct2 paper](../sources/molmoact2-paper.md) reports the same model, MolmoAct-7B-D, at **86.6** avg.)

## Related

- [MolmoAct2](molmoact2.md) — the ingested successor; hybrid continuous action head + adaptive depth reasoning.
- [Molmo](molmo.md) — the Allen Institute open VLM backbone MolmoAct is built on ([Molmo2-ER](molmo2-er.md) is MolmoAct2's).
- [VLA-0](vla-0.md) — the action-as-text VLA that surpasses MolmoAct on LIBERO without any action pretraining.
- [OpenVLA](openvla.md) — the other open-weights discrete-token VLA baseline.
- [Adaptive depth reasoning](../concepts/learning/adaptive-depth-reasoning.md) — the successor's fix for MolmoAct's full-grid depth step.
- [VLA models](../concepts/learning/vla-models.md) — action-head taxonomy (discrete-token family).

## Open questions

- **MolmoAct primary (arXiv 2508.07917) still not directly ingested** — the depth VQ-VAE tokenization and pretraining corpus are now described secondhand via [MolmoAct2](molmoact2.md); read the original for exact details if needed.
- MolmoAct's spatial-reasoning framing **is** confirmed as a non-textual [embodied chain-of-thought](../concepts/learning/chain-of-thought.md) (depth tokens) per the successor paper.

## First-hand from the primary (added 2026-08-03)

- **Action Reasoning Model (ARM) pipeline** — three independently-decodable autoregressive stages: **depth perception tokens** (2.5D scene) → **visual reasoning trace** (2D trajectory plan over the image) → **action tokens**. The distinctive capability is **steering by editing the trace**, which the paper finds more reliable than language corrections.
- **Robots: Franka only** — single-arm (incl. on a DROID-style mobile platform for home data) and a bimanual Franka rig; sim on [LIBERO](libero.md) and SimplerEnv. The YAM/SO-100 breadth arrived with [MolmoAct2](molmoact2.md).
- **Released the MolmoAct Dataset** — 10,689 Franka trajectories, 93 tasks, home + tabletop, five operators × two months; +5.5% average from mid-training on it.
- **Headline results:** SimplerEnv zero-shot **70.5%** (above π0 and GR00T N1.5); real-world **+10% single-arm / +22.7% bimanual** task progression over π0-FAST (25 trials/task); **+23.3%** OOD; top **Elo** in arena-style human preference — an early instance of preference-based policy evaluation predating [RoboArena](roboarena.md)'s formalization.
- **Stated limitation:** spatial reasoning depends on an unoccluded front camera view.

## As the supervised policy in Anthropic's robotics evaluation

MolmoAct is the pretrained manipulation policy that frontier LLMs were given to **supervise** (and override) on LIBERO-40 in [How Claude Performs on Robotics Tasks](../sources/anthropic-how-claude-performs-on-robotics-tasks.md). The result is a useful external datapoint on MolmoAct itself as much as on the supervisors: **every one of eleven tested models scored *worse* than MolmoAct running alone** on the tasks it already handles. On three novel LIBERO-like tasks MolmoAct **cannot** do alone, the better supervisors (Claude Opus 4.5/4.6, Gemini 3.1) produced net uplift.

The variable is deference calibration — how often the supervisor copies MolmoAct's exact 7-DoF action versus overriding it. See [control abstraction levels](../concepts/robotics/control-abstraction-levels.md).

## Mentioned in

- [How Claude Performs on Robotics Tasks](../sources/anthropic-how-claude-performs-on-robotics-tasks.md) — MolmoAct as the pretrained policy under LLM supervision; supervision *hurts* in-distribution, helps on novel tasks.
- [VLA-0 paper](../sources/vla-0-paper.md) — MolmoAct as a discrete-token, action-pretrained LIBERO baseline.
- [MolmoAct2 paper (Fang, Duan et al. 2026)](../sources/molmoact2-paper.md) — describes MolmoAct as its predecessor (depth-token reasoning, LIBERO number).
- [MolmoAct paper](../sources/molmoact-paper.md) — the primary source, ingested 2026-08-03.
