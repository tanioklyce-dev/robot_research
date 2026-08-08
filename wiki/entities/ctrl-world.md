---
title: Ctrl-World
type: entity
subtype: model
created: 2026-08-08
updated: 2026-08-08
sources: 2
tags: [world-model, action-conditioned, generative-video, manipulation, policy-evaluation, stanford]
---

**Ctrl-World** — a **controllable generative world model for robot manipulation** (Guo, Shi, Chen & [Finn](chelsea-finn.md), arXiv 2510.10125, Oct 2025). Action-conditioned rather than text-conditioned, and the best-performing world model across the [WorldArena](worldarena.md) cluster on the dimensions that matter functionally.

> [!note] Thin entry — no primary source ingested
> Everything here is secondhand from [WorldArena](../sources/worldarena-paper.md) and [WorldArena 2.0](../sources/worldarena-2-paper.md). Architecture, parameter count, training data, and the paper's own claims are not in the wiki. Given how well it scores, ingesting arXiv 2510.10125 is the obvious next step.

## Measured results

| Role | Result | Source |
|---|---|---|
| **Policy evaluator** | **Pearson r = 0.986** against the RoboTwin simulator's own policy ranking — near-perfect | [WorldArena](../sources/worldarena-paper.md) |
| Perceptual (EWMScore) | **59.70**, 2nd of 14, behind only Wan 2.6 | [WorldArena](../sources/worldarena-paper.md) |
| Physics adherence | Best interaction quality (0.6212) and **best trajectory accuracy (0.4766)** among embodied models | [WorldArena](../sources/worldarena-paper.md) |
| **RL environment** | **Best on the long-horizon task** (adjust bottle, 70.70) — vs simulator-RL 78.90, SFT 55.08 | [WorldArena 2.0](../sources/worldarena-2-paper.md) |
| Human evaluation | Notably better physical adherence and win rate than text-conditioned models | [WorldArena](../sources/worldarena-paper.md) |

## Why it matters here

Ctrl-World is the wiki's strongest evidence that **action conditioning is load-bearing**, not a design detail. WorldArena's summary: action-conditioned approaches "demonstrate notably better physical adherence and higher win rates than text-only counterparts, suggesting that explicit action modeling plays a critical role in producing physically plausible interactions."

That claim now has a clean natural experiment inside a single model family — [Cosmos](nvidia-cosmos.md)-Predict 2.5 was evaluated in **both** a text-conditioned and an action-conditioned variant, and the action variant scores higher on EWMScore (55.90 vs 50.81), trajectory accuracy (0.2945 vs 0.0816), and instruction following (0.5840 vs 0.2664).

> [!warning] It still inflates the scores it reports
> Ctrl-World's r = 0.986 correlation is with the simulator's *ranking*. Its absolute success rates run consistently **higher** than the simulator's — "partial overfitting to successful trajectories." Excellent as a comparator, unsafe as a measurement.

## Related

- [Chelsea Finn](chelsea-finn.md) — senior author.
- [WorldArena](worldarena.md) — where these numbers come from.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) · [world-model evaluation](../concepts/world-models/world-model-evaluation.md)
- [Veo](veo.md) — the other learned policy-evaluation harness in the wiki; opposite inflation sign.

## Mentioned in

- [WorldArena paper](../sources/worldarena-paper.md)
- [WorldArena 2.0 paper](../sources/worldarena-2-paper.md)
