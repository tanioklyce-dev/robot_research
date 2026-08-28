---
title: HWM (Hierarchical World Models)
type: entity
subtype: method
created: 2026-05-31
updated: 2026-07-26
sources: 5
tags: [hwm, hierarchical-jepa, h-jepa, world-model, latent-planning, cem, mpc, lecun, dino-wm, pldm, v-jepa-2, worlddp]
---

**HWM (Hierarchical World Models / "Hierarchical Planning with Latent World Models")** — a **model-agnostic hierarchical MPC framework** that plans with latent world models at **two temporal scales** ([Zhang et al., arXiv 2604.03208, April 2026](../sources/hwm-paper.md); senior authors [Yann LeCun](yann-lecun.md) + Nicolas Ballas). The wiki's **first concrete realization of LeCun's long-promised Hierarchical JEPA (H-JEPA)** — it answers the open question that the [JEPA concept](../concepts/world-models/jepa.md) and [LeCun page](yann-lecun.md) had carried since the 2022 position paper.

## What it is (and isn't)
- **Not a new world model** — a **planning wrapper** that sits on top of an existing latent world model. Demonstrated on three: [DINO-WM](dino-wm.md) (Push-T), [PLDM](pldm.md) (Diverse Maze), [V-JEPA 2](v-jepa-2.md)-AC (real Franka).
- **Two-level latent MPC:** a high-level world model predicts long-horizon transitions on **latent macro-actions**; a low-level model predicts short-horizon transitions on **primitive actions**. The high-level plan's **first predicted latent state = a subgoal** the low-level planner steers toward. [CEM](../concepts/world-models/jepa.md) at both scales.
- No hierarchical policies, skill learning, or task-specific rewards; zero-shot at deploy.

## Headline results ([paper](../sources/hwm-paper.md))
- **Real Franka pick-&-place: 0% → 70%** from a single goal image (flat planner: 0%); drawer 30% → 70%.
- **Push-T (DINO-WM) at the hardest horizon (d=75): 17% → 61%** (+44); also 84→89 at d=25, 55→78 at d=50.
- **Diverse Maze (PLDM), unseen layouts: +39%** (D∈[13,16] 44% → 83%).
- **Up to 3–4× less test-time planning compute** than flat planners.
- **Empirical justification (Fig. 6):** low-level model wins at short horizons (≤1 s), high-level model wins at long horizons (≥1.5 s).

> [!note] The video's "5 → 15 steps" is a simplification
> The [Welch Labs Part 2 explainer](../sources/welchlabs-lecun-1b-bet-against-llms-part2.md) described this as extending Push-T planning "from 5 to 15 steps." The paper frames it as **task horizons d=25 → d=75** with success **17% → 61%** — use the paper's numbers.

## Why it matters
- **Composes with, doesn't compete with, the JEPA zoo.** Because HWM is model-agnostic, it strengthens [DINO-WM](dino-wm.md), [PLDM](pldm.md), and [V-JEPA 2](v-jepa-2.md) rather than replacing them — a different axis (planning structure) than the usual JEPA-vs-JEPA architecture comparisons.
- **Directly targets LeCun's anti-VLA argument** (explicit planning, predict-the-consequences) — the 0%→70% single-goal-image Franka result is the cleanest evidence that latent hierarchical planning enables long-horizon, non-greedy control where flat MPC fails.

## Related
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — H-JEPA section; HWM is the realized instance.
- [WorldDP](worlddp.md) — the other LeCun-coauthored hierarchical latent planner; the architectural contrast is the low level — **HWM optimizes physical actions with a second world model; WorldDP tracks subgoals with a diffusion policy** (faster, more robust to imperfect subgoals, longer multi-stage sequences).
- [DINO-WM](dino-wm.md) / [PLDM](pldm.md) / [V-JEPA 2](v-jepa-2.md) — the base world models HWM wraps.
- [LeWorldModel](leworldmodel.md) — sibling JEPA; the single-level push-t model the Welch Labs video demoed (HWM's push-t base is DINO-WM, not LeWM).
- [Yann LeCun](yann-lecun.md) — senior author; H-JEPA is his 2022-position-paper substrate.

## Mentioned in
- [Hierarchical Planning with Latent World Models (paper)](../sources/hwm-paper.md)
- [Welch Labs — Yann LeCun's $1B Bet Against LLMs Part 2 (video)](../sources/welchlabs-lecun-1b-bet-against-llms-part2.md)
- [WorldDP paper (Goswami et al., 2026)](../sources/worlddp-paper.md) — contrasts its diffusion-policy low level against HWM's second-world-model low level.
