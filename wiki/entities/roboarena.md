---
title: RoboArena
type: entity
subtype: benchmark
created: 2026-07-27
updated: 2026-08-03
sources: 3
tags: [roboarena, benchmark, evaluation, real-world, droid, bradley-terry, pairwise-preference, distributed, leaderboard]
---

**RoboArena** — a **distributed, real-world, pairwise-preference leaderboard** for generalist robot policies. Evaluators across a network of institutions choose their own tasks and environments but run **double-blind A/B comparisons** between policy pairs on a shared [DROID](droid.md) platform; preferences are aggregated into a global ranking by an extended **Bradley-Terry** model. Introduced at CoRL 2025 ([paper](../sources/roboarena-paper.md), arXiv 2506.18123, 32 authors led by Pranav Atreya and [Karl Pertsch](karl-pertsch.md)); now a live leaderboard.

## The design in one line

**Diversity from decentralization, comparability from pairing.** Standardized benchmarks buy comparability by fixing tasks, which caps diversity; RoboArena frees the tasks and recovers comparability from the paired A/B structure plus a task-difficulty term in the model.

- **Rubric per episode**: continuous progress score [0–100], binary preference, free-form explanation.
- **Aggregation**: Bradley-Terry extended with per-policy ability **θ**, per-task-bucket difficulty **τ**, and policy×task offsets **ψ**, fit by EM. Beats plain Elo and vanilla BT — modeling task difficulty is what makes free task choice viable.
- **Scale at publication**: 7 institutions, **4,284 episodes / 612 pairwise comparisons**, 7 policies.

## Why it matters to this wiki

It is the **empirical case against the wiki's own tables**. RoboArena reaches **Pearson r ≈ 0.95** with oracle rankings where conventional centralized success-rate evaluation reaches **r ≈ 0.60**, and it converges in about **100 pairwise comparisons**. That is a measurement showing the standard protocol ranks policies badly — complementing the [~1,030-rollout requirement](../concepts/robotics/robot-policy-evaluation.md) from [RoboLab](nvidia-robolab.md) and the wiki's own [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md).

The two approaches diverge in prescription:

| | [RoboLab](nvidia-robolab.md) (NVIDIA SRL) | **RoboArena** |
|---|---|---|
| Domain | Simulation | **Real world** |
| Fix | Collect **far more rollouts** (≈1,030 for ±2 pp) | **Stop measuring absolute rates**; measure preferences |
| Output | Absolute success rates + diagnostics | **Ordering only** — no magnitude |
| Task set | Curated, competency-tagged, agent-authored | **Evaluator's free choice** |
| Scale lever | Cheap simulation | Distributed human evaluators |

They share people — **Xuning Yang** authors both the RoboLab methodology blog and RoboArena.

## As a leaderboard

The wiki cites **Cosmos3-Nano-Policy-DROID as "#1 policy model on RoboArena" (2026-05-30)** ([Cosmos 3 technical report](../sources/cosmos-3-technical-report.md)) — a claim that predates this entity page by two months. **Whether the live leaderboard still runs the paper's exact BT variant, and how many comparisons back that #1, is unknown** — see the [source page](../sources/roboarena-paper.md)'s open questions.

## Results at publication

Seven policies, all DROID-finetuned: **π₀-flow**, **π₀-FAST**, and five PaliGemma-backbone action-representation variants (PG-flow, PG-FAST, PG-FAST+, PG-FSQ, PG-Bin). Findings: expressive action representations beat simple binning; **discrete tokenization outperformed diffusion** in this sweep; **π₀-FAST-DROID strongest overall**. Because the backbone is held fixed across five of the seven, this is one of the cleaner action-representation comparisons in the wiki — see [FAST](fast-action-tokenization.md) and the [VLA action-head taxonomy](../concepts/learning/vla-models.md).

## Limitations (from the paper)

DROID-only (no cross-embodiment); decentralization makes controlled ablation hard; **no hardening against adversarial raters**; and **Goodhart's law is named explicitly** — as the ranking becomes a target its validity may erode.

## Related
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — the concept; RoboArena is its real-world pole.
- [RoboLab](nvidia-robolab.md) — the simulation pole.
- [DROID](droid.md) — the shared platform that makes distribution possible.
- [Success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) — the wiki-internal version of the same concern.
- [LIBERO](libero.md) / [LIBERO-PRO](../sources/libero-pro-paper.md) — the simulation benchmark whose weaknesses RoboArena's real-world pairing routes around.

## Mentioned in
- [RoboArena paper (CoRL 2025)](../sources/roboarena-paper.md)
- [Cosmos 3 technical report](../sources/cosmos-3-technical-report.md) — Cosmos3-Nano-Policy-DROID reported #1 (2026-05-30)
- [Veo world simulator evaluation](../sources/veo-robotics-policy-evaluation-paper.md) — the third evaluation paradigm, and one that makes the **same trade as RoboArena**: reliable ranking, unreliable absolute magnitude.
