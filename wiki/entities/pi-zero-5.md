---
title: π0.5
type: entity
subtype: model
created: 2026-08-03
updated: 2026-11-14
sources: 28
tags: [pi-zero-5, physical-intelligence, vla, co-training, open-world, mobile-manipulation, hierarchical-inference, baseline]
---

**π0.5** ("pi oh five") — [Physical Intelligence](physical-intelligence.md)'s open-world-generalization VLA (Apr 2025), built on [π0](pi-zero.md) via **co-training on heterogeneous data** ([paper](../sources/pi-zero-5-paper.md), now ingested — previously the wiki's most-cited secondhand model). The first end-to-end learned system demonstrated **cleaning kitchens and bedrooms in entirely unseen homes**, on 10–15-minute tasks from high-level prompts.

## What it is

- **Recipe, not architecture:** ~400 hr mobile-manipulation data across ~100 homes is only **2.4%** of first-phase training; the rest is other robots (ME/CE), high-level subtask prediction (HL), web data (WD), and verbal instructions (VI). Removing any cross-embodiment source significantly degrades performance; web data is what buys **out-of-distribution object vocabulary**.
- **Hierarchical inference in one model:** predict the semantic subtask ("pick up the cutting board"), then the action chunk conditioned on it.
- **Hybrid training** — discrete [FAST](fast-action-tokenization.md) tokens in pre-training, a 300M flow-matching expert attached in post-training. This recipe became the template for [π0.5-KI](../concepts/learning/knowledge-insulation.md) and [MolmoAct2](molmoact2.md).
- **Scaling result:** at **104 training locations**, matches a control model trained directly on the test homes — the environment-generalization gap closed.

## Role in the wiki: the standing 2026 baseline

π0.5 is the model the 2026 record is measured against, and the record is two-sided:

| Where | What π0.5 shows |
|---|---|
| [π0.5 paper](../sources/pi-zero-5-paper.md) (2025) | Real scene-level generalization: cleans unseen homes; beats π0 and π0-FAST+Flow |
| [LIBERO-PRO](../sources/libero-pro-paper.md) (2026) | Most robust of the three VLAs tested under **position** perturbation (0.17–0.38) — and **~0.00 under instruction paraphrase** |
| [CaP-X](../sources/cap-x-paper.md) (2026) | Beats training-free CaP-Agent0 on position perturbation in 2 of 3 suites; loses decisively on paraphrase |
| [ASPIRE](../sources/aspire-paper.md) (2026) | "Largely collapses under task paraphrases" vs the coding agent |
| [MolmoAct2](../sources/molmoact2-paper.md) (2026) | Runner-up on RoboEval (44.3 vs 40.5); in-house π0-SO100/101 beaten by 11.4 on SO-100 |
| [Knowledge Insulation](../sources/knowledge-insulation-paper.md) | The π0.5-KI variant; LIBERO-90 + Spatial SOTA claims |

> [!note] The two records are about different axes — keep them apart
> π0.5's demonstrated generalization is **environment- and object-level**; the 2026 collapses are **instruction-level** (paraphrase), on benchmark-finetuned variants. Both are real. The honest one-line summary: **the co-training recipe bought scene generalization but not instruction generalization** — which the paper's own "relatively simple prompts" limitation anticipated.

## Related
- [Physical Intelligence](physical-intelligence.md) — lab · [π0](pi-zero.md) — base · [π0.6 stub](pi-zero-6.md) / [π0.7](pi07.md) / [π*0.6](pistar06.md) — successors
- [MolmoAct2](molmoact2.md) — adopts the hybrid recipe; the open-everything counterpart
- [VLA models](../concepts/learning/vla-models.md) · [Knowledge insulation](../concepts/learning/knowledge-insulation.md)

## Mentioned in
- [π0.5 paper](../sources/pi-zero-5-paper.md) — primary source.
- [Knowledge Insulation paper](../sources/knowledge-insulation-paper.md) — π0.5-KI.
- [LIBERO-PRO paper](../sources/libero-pro-paper.md) · [CaP-X paper](../sources/cap-x-paper.md) · [ASPIRE paper](../sources/aspire-paper.md) · [MolmoAct2 paper](../sources/molmoact2-paper.md) — the 2026 comparisons.
- [π0.7 paper](../sources/pi07-paper.md) · [π*0.6 paper](../sources/pistar06-paper.md) — successor lineage references.
- [RoboJEPA paper](../sources/robojepa-scaling-robotic-latent-world-models-paper.md) — π0.5 (DROID-finetuned, text goal) as a reference on a Franka: **Pick and Place 53%** beats every RoboJEPA size (best 31%), but **Object Lift 0%** and Grasp 5% (n=50). Not like-for-like (text vs goal image).

## As the reference policy in world-model benchmarking

[WorldArena](worldarena.md) uses π0.5 as the yardstick every embodied world model is measured against, and the comparison is not close. Trained on real RoboTwin 2.0 data it reaches **77% / 66%** on two bimanual tasks; the best world model **as an action planner** manages 20% / 21%, and the best **as a data engine** (WoW) reaches 45% / 71% — beating real data on only the easier task ([WorldArena paper](../sources/worldarena-paper.md)).

The one role where world models earn their place is as **RL environments**: a π0.5 policy optimized inside one reaches 75.0 / 70.7 against 87.3 / 78.9 for simulator-based RL and 43.8 / 55.1 for SFT ([WorldArena 2.0](../sources/worldarena-2-paper.md)). See [what world models are measurably good for](../syntheses/world-models/what-world-models-are-measurably-good-for.md).

## As the shipped adapter in RoboDojo's Arena port (2026-10-30)

[RoboDojo](robodojo.md)'s Isaac Lab-Arena branch ships π0.5 (via OpenPI) as its only real policy adapter. The adapter takes head and wrist RGB and a 14-D joint state from the dual ARX X5. The checkpoint is a RoboDojo sim fine-tune (`RoboDojo-sim-arx_x5-joint-0`), and inference is unbatched, one call per environment ([branch READMEs](../sources/robodojo-isaaclabarena-branch.md)). In Ai2's [ToyBlocks](toyblocks.md), π0.5 is one of three VLAs reported to *"generalize poorly"* to held-out workspace regions and stack heights ([Ai2 blog](../sources/ai2-toyblocks-blog.md)).

## As the target of a weight edit (2026-11)

Claude Opus 5.5 edited a π0.5 **Training-Time RTC** checkpoint with no gradients, changing 1.16% of its parameters ([SII, SJTU and HKU](../sources/robotics-weight-editing-pi05.md)).
- **Speedup.** A RoPE action-spacing intervention (P + i → P + 1.25i), fitted into the Q/K weights of layers 1–17, made the policy advance about 20% further along its own path per step offline. On a bimanual YAM, bottle placement got 4.3%, 7.4% and 12.0% faster at 30, 35 and 40 Hz, with 3 trials per condition. Block stacking did not change.
- **A porting hazard in TT-RTC.** The sampler returns the conditioned prefix after one more, untrained velocity update. Any deployment whose prefix is longer than its actual latency therefore executes drifted actions, which show up as about 26 mm chunk jumps. A one-line restore fixes it, and Opus's rank-one weight edit does roughly the same job. It was confirmed in PI's reference code, where the official eval never executes those positions.

## Mentioned in (additional)

- [Editing π0.5's weights (SII, SJTU and HKU)](../sources/robotics-weight-editing-pi05.md) — a gradient-free Opus 5.5 edit (RoPE tempo plus RTC prefix repair) on a YAM. 4–12% faster at matched rates, 3 trials each.

- [WorldArena paper](../sources/worldarena-paper.md) · [WorldArena 2.0 paper](../sources/worldarena-2-paper.md)
- [RoboDojo — IsaacLabArena branch](../sources/robodojo-isaaclabarena-branch.md) · [ToyBlocks (Ai2 blog)](../sources/ai2-toyblocks-blog.md)
- [RoboDojo paper](../sources/robodojo-paper.md) — the strongest *real-world* policy (22.9 / **12.8%** over 180 trials, 3 embodiments), third in sim (6.91%), and the only policy above 1.5% on Open tasks (1.67%). Spatial Forcing, a π0.5 fine-tune with 3D spatial alignment, beats it in sim and holds up better under randomization (−67% vs −72%).
- [Runway GWM-Robotics policy evaluation](../sources/runway-gwm-robotics-policy-evaluation.md) — pi05_droid ranked best of eight RoboArena policies both in the world model and in the real world.
