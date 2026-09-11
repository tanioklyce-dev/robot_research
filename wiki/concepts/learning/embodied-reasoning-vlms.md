---
title: Embodied-reasoning VLMs (ER backbones)
type: concept
created: 2026-09-11
updated: 2026-09-11
sources: 4
tags: [embodied-reasoning, vlm-backbone, spatial-reasoning, pointing, benchmarks, vla, molmo2-er, gemini-robotics-er, cosmos-reason, unifolm]
---

# Embodied-reasoning VLMs (ER backbones)

An **embodied-reasoning VLM** is a vision-language model post-trained on spatial, metric and interaction-grounded tasks — pointing, referring expressions, relative depth, free-space and affordance questions, trajectory prediction, multi-view correspondence — so that it can serve either as the **backbone of a [VLA](vla-models.md)** or as a **planner that emits tool calls** over a lower-level policy. The suffix "-ER" has become the convention: Gemini Robotics-ER, Molmo2-ER, UnifoLM-ER, Cosmos-Reason, RoboBrain, Embodied-R1.

The class exists because of one observation, made independently by every group in it: general VLMs are trained on semantic image understanding and are poor at the *metric* and *temporal* skills a robot needs. [Molmo2-ER](../../entities/molmo2-er.md)'s ablation is the cleanest evidence that fixing this transfers into control — swapping Molmo2 for Molmo2-ER with no other change lifts LIBERO-Long discrete-action accuracy **+6.0 points** ([MolmoAct2 paper](../../sources/molmoact2-paper.md)).

## Two roles, one model class

| Role | Example | The ER model's output |
|---|---|---|
| **Backbone** for a VLA | [Molmo2-ER](../../entities/molmo2-er.md) → [MolmoAct2](../../entities/molmoact2.md); Cosmos-Reason2 → [GR00T N1.7](../../entities/nvidia-groot.md); UnifoLM-ER-Flow → [UnifoLM-WLA-1.0](../../entities/unifolm.md) | hidden states consumed by an action expert |
| **Orchestrator** over a policy | [Gemini Robotics-ER](../../entities/gemini-robotics.md) 1.5 / 2 | tool calls, subgoals, points, plans — an [LLM-agent architecture](../agents/llm-agent-architecture.md) |

The same model can do both; the distinction is where the action comes from.

## The benchmark suite

The field has converged on a shared basket, and [UnifoLM](../../sources/unifolm-wla-1-project-page.md)'s launch table — 23 models × 16 benchmarks — is the widest single view of it in this wiki:

- **Pointing / referring:** RefSpatial-Bench, Where2Place, Pixmo-Point, RoboSpatial.
- **Spatial relations and depth:** BLINK (depth + spatial subtasks), CV-Bench, EmbSpatial, VSR, SAT.
- **Video / temporal spatial:** VSI-Bench.
- **Planning / robot QA:** RoboVQA, Ego-Plan2, ERQA.
- **General VLM (regression check):** RealWorldQA, MME, MMMU.

## Current state (2026-09)

- **The 4B class is where the open action is.** Molmo2-ER-4B (Ai2), UnifoLM-ER-1-4B (Unitree), Thinker-4B and Qwen3-VL-4B itself all sit in the same weight class, and the table shows them trading columns: UnifoLM leads on pointing and static spatial relations (Where2Place 82.0, EmbSpatial 88.9, Pixmo-Point 73.8), Molmo2-ER on video spatial reasoning (VSI-Bench 74.5 vs 54.2), Thinker on planning (Ego-Plan2 63.7).
- **Proprietary frontier models still own the hard reasoning columns.** In Unitree's own API tests, the models it lists as GPT-6-Astra and Gemini 3.1 Pro lead ERQA by 15–27 points and RefSpatial by 8–18 over the best open 4B model — while losing on pointing benchmarks to the specialized open models.
- **Two recipes for the same regression problem.** Specializing a VLM on embodied data costs general capability. Ai2's answer is *specialize-then-rehearse* (a second stage interleaving the original multimodal mix, p=0.5). Unitree's is single-stage *co-training* with general image–text data — and its own table shows the base Qwen3-VL-4B still ahead on MME (−102), MMMU (−3.1), RealWorldQA (−1.2) and VSI-Bench (−5.1). The rehearse stage appears to be worth its cost; nobody has run the two recipes on one base to check.
- **Video is the under-served axis.** VSI-Bench is the column where image-only training mixes (UnifoLM) fall furthest, and it is the one closest to what manipulation-over-time needs. The [spatial intelligence](../world-models/spatial-intelligence.md) page's "leave and return" probe is a temporal one.

> [!warning] Cross-paper tables are not experiments
> Most rows in every ER comparison are copied from other papers' reports; harnesses, prompts and benchmark versions differ, and no one reports intervals. The [success-rate audit](../../syntheses/platforms/vla-success-rate-audit.md) discipline applies: gaps under ~3 points are ties.

## Key references

- [MolmoAct2 paper](../../sources/molmoact2-paper.md) — the backbone-swap ablation; the Molmo2-ER corpus and recipe.
- [UnifoLM-WLA-1.0 project page](../../sources/unifolm-wla-1-project-page.md) — the 23×16 table; single-stage co-training and its regression.
- [Gemini Robotics 1.5 report](../../sources/gemini-robotics-1-5-report.md) — ER as orchestrator; ERQA.
- [Isaac-GR00T GitHub](../../sources/isaac-gr00t-github.md) — Cosmos-Reason2-2B as the N1.7 backbone.

## Related concepts

- [VLA models](vla-models.md) — the VLM-backbone taxonomy this page specializes.
- [Knowledge Insulation](knowledge-insulation.md) — how the backbone is protected once an action expert is attached.
- [Spatial intelligence](../world-models/spatial-intelligence.md) — the capability the benchmarks approximate.
- [Chain-of-thought](chain-of-thought.md) — pointing / spatial CoT as the bridge from language to action.
- [Physical reasoning benchmarks](../world-models/physical-reasoning-benchmarks.md) — the adjacent, physics-focused basket.

## Mentioned in

- [UnifoLM-WLA-1.0 project page](../../sources/unifolm-wla-1-project-page.md)
- [MolmoAct2 paper](../../sources/molmoact2-paper.md)
- [Gemini Robotics 1.5 report](../../sources/gemini-robotics-1-5-report.md)
- [Isaac-GR00T GitHub](../../sources/isaac-gr00t-github.md)
