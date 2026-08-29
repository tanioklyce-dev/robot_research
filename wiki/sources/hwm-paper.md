---
title: "Hierarchical Planning with Latent World Models (HWM)"
type: source
url: https://arxiv.org/abs/2604.03208
local_path: raw/2026-04-hierarchical-planning-latent-world-models-2604.03208.pdf
sha256: 0f60bed10fff3d873f246b0655f4f4b176d3f59063e5c643e148453cc79b7f40
project_page: https://kevinghst.github.io/HWM/
author: Wancong Zhang, Basile Terver, Artem Zholus, Soham Chitnis, Harsh Sutaria, Mido Assran, Amir Bar, Randall Balestriero, Adrien Bardes, Yann LeCun, Nicolas Ballas
affiliations: NYU, Meta (FAIR), Mila, Brown University
published: 2026-04-03
ingested: 2026-05-31
tags: [hierarchical-jepa, h-jepa, world-model, jepa, latent-planning, cem, mpc, dino-wm, pldm, v-jepa-2, push-t, lecun]
---

## Summary

**[HWM (Hierarchical World Models)](../entities/hwm.md)** is the primary paper behind the "hierarchical JEPA extends the planning horizon" claim in the [Welch Labs Part 2 explainer](welchlabs-lecun-1b-bet-against-llms-part2.md). It is a **modular, model-agnostic hierarchical MPC framework**: train latent world models at **two temporal scales** in a shared latent space, then plan top-down — a high-level planner optimizes **latent macro-actions** to reach the goal, its **first predicted latent state becomes a subgoal**, and a low-level planner optimizes **primitive actions** to reach that subgoal. No hierarchical policies, skill learning, or task-specific rewards. Senior authors **[Yann LeCun](../entities/yann-lecun.md) and Nicolas Ballas (joint advising)**; lead Wancong Zhang (NYU); co-authors include **Basile Terver** (JEPA-WMs lead) and **Randall Balestriero** (the JEPA collaborator credited in the Welch Labs video).

> [!note] Resolves a wiki open question
> The [Yann LeCun page](../entities/yann-lecun.md) and [JEPA concept](../concepts/world-models/jepa.md) flagged "has anyone built a working Hierarchical JEPA?" as open, and the [Part 2 video ingest](welchlabs-lecun-1b-bet-against-llms-part2.md) couldn't name the paper. **This is it.**

## Key claims

- **Model-agnostic abstraction.** The same hierarchical-planning wrapper is demonstrated on **three different base world models**: **[V-JEPA 2](../entities/v-jepa-2.md)-AC** (real Franka), **[DINO-WM](../entities/dino-wm.md)** (Push-T), **[PLDM](../entities/pldm.md)** (Diverse Maze).
- **Real-robot pick-&-place (V-JEPA2-AC, Franka):** **0% → 70%** with *no oracle subgoals*, from a single final-goal image (flat world-model planner fails entirely). Drawer open/close **30% → 70%**. With oracle subgoals both are 80% (hierarchy adds nothing when subgoals are given — the gain is in *generating* good subgoals).
- **Push-T (DINO-WM), success across extended task horizons** (Table 2; `d` = start–goal separation in timesteps, vs the d=25 used in the original DINO-WM eval):

  | d | DINO-WM (flat) | DINO-WM + hierarchy |
  |---|---|---|
  | 25 | 84% | 89% |
  | 50 | 55% | 78% |
  | 75 | **17%** | **61%** (+44) |

- **Diverse Maze (PLDM), zero-shot on unseen layouts** (Table 3): D∈[9,12] **63% → 95%**; D∈[13,16] **44% → 83%** (+39); D∈[5,8] 100% → 100%.
- **Compute:** hierarchy reaches higher success with **up to 3–4× less test-time planning compute** than flat planners.
- **Why hierarchy works (Fig. 6):** prediction-error crossover — the **low-level** model is more accurate for short horizons (≤1 s); the **high-level** model has lower error for long horizons (≥1.5 s). Short-term precision + long-term guidance, each from the model that's actually good at it.
- **Subgoal quality (Fig. 7):** a **latent macro-action dimension of 4** is the sweet spot — expressive enough to encode useful trajectories, not so expressive it proposes unreachable/over-complex subgoals.
- **Planner:** **CEM** at both temporal scales (MPPI for maze); receding-horizon MPC, replanning each step.

> [!warning] Correction to the video's "5 → 15 steps"
> The [Welch Labs Part 2 video](welchlabs-lecun-1b-bet-against-llms-part2.md) framed the result as "extending the Push-T planning horizon from 5 to 15 steps." The paper does **not** report it that way — its Push-T story is **task horizons extended from d=25 to d=75 timesteps**, with success at the hardest setting rising **17% → 61%**. (The flat-planner CEM *prediction horizon* does scale 5→10→15 across d=25/50/75 in Table 9, which is the likely source of the video's shorthand.) Cite the paper's framing, not the video's.

## Method detail

- **Low-level WM** `P(1)(z_{t+1} | z_t, a_t)` — short-horizon transitions on primitive actions; trained with a multi-step **rollout loss** (L1 in latent space).
- **High-level WM** `P(2)(z_{t+h} | z_t, l_t)` — long-horizon transitions on **latent macro-actions** `l_t`, produced by a transformer-based **action encoder** that compresses chunks of low-level actions (CLS token). Causal, latent-space trained.
- **Planning:** high-level CEM unrolls macro-actions to the goal → intermediate latent **subgoals** `z̃_i = P(2)(l*_{1:i}; z_1)`; low-level CEM minimizes `‖z̃_1 − P(1)(â_{1:h}; z_1)‖` to reach the first subgoal.

## Entities mentioned
- [Yann LeCun](../entities/yann-lecun.md) — senior author (joint advising)
- [DINO-WM](../entities/dino-wm.md) — Push-T base model
- [V-JEPA 2](../entities/v-jepa-2.md) (V-JEPA2-AC) — Franka base model
- [PLDM](../entities/pldm.md) — Diverse Maze base model
- [Basile Terver](../entities/basile-terver.md), [Adrien Bardes](../entities/adrien-bardes.md) — co-authors (FAIR JEPA line)
- [Octo](../entities/octo.md) — generalist-policy comparison point.

## Concepts touched
- [Hierarchical JEPA / H-JEPA](../concepts/world-models/jepa.md) — the realized instance
- [World model](../concepts/world-models/world-model.md) / [latent space](../concepts/world-models/latent-space.md)
- [VLA models](../concepts/learning/vla-models.md) — π0/π0.5/Octo are baselines on Franka

## Why this matters for the wiki
- **Closes the H-JEPA loop.** Converts the wiki's longest-standing JEPA open question (a *working* hierarchical world model, per LeCun's 2022 vision) from "open / unnamed" to a concrete, reproducible, model-agnostic result.
- **Reframes the contribution: it's not a new world model, it's a planning wrapper.** HWM sits *on top of* DINO-WM / PLDM / V-JEPA2-AC — so it composes with, rather than competes with, the existing JEPA entities in the wiki.
- **The real-robot 0%→70% from a single goal image** is the strongest evidence to date that latent-space hierarchical planning addresses LeCun's "VLAs can't plan" critique — though it's still goal-image-conditioned, not language-conditioned like a VLA.

## Open questions
- HWM uses **two** levels. LeCun's vision is N-level emergent hierarchy — does it stack beyond two, and does the hierarchy become emergent rather than hand-designed (waypoint indices are currently chosen)?
- All evals are **goal-image-conditioned**. Bridging to language-conditioned tasks (the VLA setting) is unaddressed.
- Subgoal generation needs the latent action dim tuned (≈4); how sensitive is this across domains beyond the three shown?
