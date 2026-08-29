---
title: "WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models"
type: source
url: https://arxiv.org/abs/2602.08971
local_path: raw/2602.08971.pdf
sha256: e41ab0f9ce75adad027e4e77402e1bbd77a50ab12340a6517a300d2edc94a6e6
author: Yu Shang, Zhuohang Li, Yiding Ma, Weikang Su, Xin Jin, Ziyou Wang, Lei Jin, Xin Zhang, Yinzhou Tang, Haisheng Su, Chen Gao, Wei Wu, Xihui Liu, Dhruv Shah, Zhaoxiang Zhang, Zhibo Chen, Jun Zhu, Yonghong Tian, Tat-Seng Chua, Wenwu Zhu, Yong Li
venue: Preprint (arXiv 2602.08971v2)
published: 2026-02-11
ingested: 2026-08-08
license: CC BY 4.0
tags: [benchmark, world-model, evaluation, embodied-ai, robotwin, ewmscore, perception-functionality-gap]
---

## Summary

**The benchmark the [HAI policy brief](hai-world-model-spatial-intelligence-brief.md) was asking for, and the numbers are worse than the brief guessed.** WorldArena scores 14 embodied world models on both *perceptual* quality (16 metrics across 6 sub-dimensions, aggregated into a single **EWMScore**) and *functional* utility in the three roles a world model actually gets used for — **data engine**, **policy evaluator**, **action planner**. Its headline result is the **perception–functionality gap**: EWMScore correlates with human judgment at **r = 0.825**, with data-synthesis utility at **r = 0.600**, and with action-planning performance at only **r = 0.360**. Visual realism buys human approval and almost nothing else.

Project lead Yu Shang; corresponding author Yong Li (Tsinghua). Eight institutions — Tsinghua, SJTU, HKU, Princeton (Dhruv Shah), CAS, USTC, PKU, NUS.

This is the first source in the wiki that measures a world model **by what it is for** rather than by what it looks like, which makes it the natural companion to [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) on the policy side.

## Key claims

### Setup

- **Substrate**: [RoboTwin 2.0](../entities/robotwin.md) — 50 bimanual manipulation scenarios, 2,500 videos (2,000 to post-train each world model, 500 held out for video-quality scoring). All models with public training code are post-trained on this data "following their official implementations," so this is a like-for-like comparison, not a zero-shot one.
- **14 models across three families** — general video models (CogVideoX, Wan 2.2, Wan 2.6, **Veo 3.1**); text-conditioned embodied models ([Genie Envisioner](../entities/genie-envisioner.md), GigaWorld-0, TesserAct, **[Cosmos](../entities/nvidia-cosmos.md)-Predict 2.5 (text)**, WoW, RoboMaster, Vidar); action-conditioned embodied models (IRASim, Cosmos-Predict 2.5 (action), **Ctrl-World**).
- **Human evaluation**: 70 annotators, 3,500 videos, scoring overall quality / instruction following / physical adherence plus head-to-head win rate.
- **EWMScore** is the arithmetic mean of the 16 normalized video metrics, scaled to 0–100. It is *purely perceptual* — the functional results are reported separately, which is what makes the correlation analysis possible.

### EWMScore leaderboard (perception only)

| Rank | Model | EWMScore |
|---:|---|---:|
| 1 | Wan 2.6 | 61.86 |
| 2 | Ctrl-World | 59.70 |
| 3 | Veo 3.1 | 58.87 |
| 4 | IRASim | 58.11 |
| 5 | CogVideoX | 57.88 |
| 6 | Cosmos-Predict 2.5 (action) | 55.90 |
| 7 | WoW | 54.88 |
| 8 | Wan 2.2 | 54.54 |
| 9 | GigaWorld-0 | 53.39 |
| 10 | TesserAct | 53.23 |
| 11 | RoboMaster | 51.84 |
| 12 | Vidar | 51.60 |
| 13 | Cosmos-Predict 2.5 (text) | 50.81 |
| 14 | **Genie Envisioner** | **43.65** |

> [!warning] Genie Envisioner ranks last of 14
> And not narrowly — 7 points below the next model, with the lowest instruction-following (0.2028 vs Veo 3.1's 0.9328) and near-lowest trajectory accuracy (0.0679). The paper attributes this to "persistent gaps in long-horizon coherence and instruction compliance" in earlier text-conditioned embodied models. This sits directly against the [Genie Envisioner](../entities/genie-envisioner.md) page's minute-scale-stable-rollout framing, which came from a vendor announcement.

### Role 1 — data engine (train a policy on synthetic data)

25 synthetic trajectories per world model, used to train a **[π0.5](../entities/pi-zero-5.md)** policy; two RoboTwin tasks (*adjust bottle*, *click bell*), 100 executions each.

| Data source | Adjust bottle | Click bell |
|---|---:|---:|
| π0.5 zero-shot | 2% | 5% |
| **π0.5 on real data** | **77%** | **66%** |
| WoW | 45% | 71% |
| RoboMaster | 7% | 68% |
| Vidar | 13% | 53% |
| Wan 2.2 | 15% | 41% |
| TesserAct | 1% | 35% |
| Genie Envisioner | 7% | 21% |

Only **RoboMaster and WoW beat real data, and only on the easier task**. Verdict: "current embodied world models are not yet reliable data sources for downstream learning."

### Role 2 — policy evaluator (world model as the eval harness)

Five π0.5 policies of varying quality, each evaluated by rolling out inside an action-controllable world model, success judged by a VLM, compared against the RoboTwin simulator's own verdict.

- **Ctrl-World: Pearson r = 0.986** against the simulator — it ranks policies almost perfectly.
- **Cosmos-Predict 2.5: r = 0.483** — it does not.

> [!warning] The measured version of "teaching to a flawed test"
> **"Both models have consistently higher success rates than those measured in the simulator, suggesting partial overfitting to successful trajectories."** This is the score-inflation the [HAI brief](hai-world-model-spatial-intelligence-brief.md) predicted and that the wiki recorded as unmeasured. It is now measured, and it is **directional, not random**: a learned evaluator flatters the policies it evaluates. Ranking survives (for Ctrl-World); absolute rates do not.
>
> Same shape as [Veo](../entities/veo.md)'s finding — Pearson 0.88 against 1,600+ real evaluations but absolute predicted rates run low. Note the *sign differs*, so this is not yet one settled effect.

### Role 3 — action planner (world model drives the robot)

World model + inverse dynamics model, predicted action sequences executed in the RoboTwin simulator.

| Planner | Adjust bottle | Click bell |
|---|---:|---:|
| **π0.5 policy** | **77%** | **66%** |
| WoW | 20% | 21% |
| Wan 2.2 | 12% | 20% |
| Genie Envisioner | 10% | 20% |
| RoboMaster | 8% | 20% |
| Vidar | 2% | 19% |
| TesserAct | 1% | 35% |

A dedicated VLA policy beats every world model as a planner by **3–4×**. The paper: world models "still struggle to reliably support closed-loop task execution, particularly over long horizons."

### The gap, stated

- EWMScore ↔ **human judgment**: r = 0.825
- EWMScore ↔ **data-engine** performance: r = 0.600
- EWMScore ↔ **action-planner** performance: r = 0.360

"Perceptual realism is a necessary condition for favorable human evaluation, [but] it does not directly translate into proportional gains in downstream embodied tasks."

Secondary finding with the same shape: commercial general-video models (Veo 3.1, Wan 2.6) take the top visual and aesthetic scores but "show limited improvements in embodied-specific metrics," and "visually strong models tend to suffer from semantic drift, while embodied world models produce more coherent and goal-consistent action sequences." **Action-conditioned** models (Ctrl-World) beat text-conditioned ones on physical adherence — explicit action modeling is doing real work.

## Entities mentioned

- [RoboTwin 2.0](../entities/robotwin.md) · [π0.5](../entities/pi-zero-5.md) · [Genie Envisioner](../entities/genie-envisioner.md) · [NVIDIA Cosmos](../entities/nvidia-cosmos.md) · [Veo](../entities/veo.md) · [Ctrl-World](../entities/ctrl-world.md) · [WorldArena](../entities/worldarena.md)

## Concepts touched

- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — this is now its primary source.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) · [world model](../concepts/world-models/world-model.md)
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) · [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md)

## Open questions

- **Two tasks carry the entire functional evaluation.** Video quality uses all 50 RoboTwin scenarios, but the data-engine and action-planner results rest on *adjust bottle* and *click bell* at 100 trials each. By the wiki's own [rollout-count standard](../concepts/robotics/robot-policy-evaluation.md), 100 trials gives roughly ±10 pp — fine for a 77%-vs-20% gap, not fine for ranking WoW against Wan 2.2.
- **The inflation direction contradicts Veo's.** WorldArena finds learned evaluators score *higher* than the simulator; the [Veo policy-evaluation paper](veo-robotics-policy-evaluation-paper.md) finds its predicted rates run *low*. Both preserve ranking better than level. Nobody has reconciled these.
- **Only 25 synthetic trajectories per model** in the data-engine test. Whether the ranking holds at 250 or 2,500 — the regime where synthetic data would actually be used — is untested.
- **EWMScore is an unweighted mean of 16 metrics.** Given that it correlates at 0.360 with the thing you care about, the obvious follow-up is a *functionally weighted* aggregate. The paper doesn't attempt one.
