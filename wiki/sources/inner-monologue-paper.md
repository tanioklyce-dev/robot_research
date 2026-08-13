---
title: "Inner Monologue: Embodied Reasoning through Planning with Language Models"
type: source
url: https://arxiv.org/abs/2207.05608
author: "Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky Liang, Pete Florence, Andy Zeng, Jonathan Tompson, Igor Mordatch, Yevgen Chebotar, Pierre Sermanet, Noah Brown, Tomas Jackson, Linda Luu, Sergey Levine, Karol Hausman, Brian Ichter"
affiliation: Robotics at Google
published: 2022-07-12
ingested: 2026-08-03
venue: CoRL 2022
format: conference paper (25 pp with appendices)
local_path: raw/2207.05608.pdf
tags: [inner-monologue, llm-agent, closed-loop, feedback, replanning, success-detection, saycan, primary-source]
---

## Summary

**Inner Monologue** closes the loop on [SayCan](saycan-paper.md). SayCan plans once against affordances and never learns what actually happened; Inner Monologue continually injects **textual environment feedback** — success detection, scene description, object recognition, and human answers — back into the LLM prompt, forming a running monologue the planner reasons over. No training; few-shot prompting only.

Its importance to this wiki is that it is the **2022 origin of the finding both 2026 papers rediscover**: what matters is not the model but the *feedback channel*. And it establishes the specific result that closed-loop feedback is worth little in nominal conditions and worth everything under disturbance.

## Key claims

### Taxonomy of feedback
- **Task-specific:** *Success* — did the last action work?
- **Passive scene:** *Object* (recognizers) and *Scene* (task-progress description), injected automatically.
- **Active scene:** *Human* — provided in response to the planner's own questions.

### Results

**Simulated tabletop** (Ravens-based, **50 episodes/task**, with injected test-time noise). The critical block is the unseen tasks:

| Task | CLIPort | CLIPort +oracle | IM (Object) | IM (Obj+Success) | IM (Obj+Scene) |
|---|---:|---:|---:|---:|---:|
| Put blocks in matching bowls | 0.0% | 0.0% | 56.0% | 70.0% | **82.0%** |
| Put blocks on mismatched bowls | 0.0% | 0.0% | 62.0% | 76.0% | **86.0%** |
| Stack all blocks on [x] corner | 0.0% | 0.0% | 0.0% | 4.0% | 6.0% |

**CLIPort scores 0.0% on every unseen task, even with a termination oracle** — the same imitation-collapse shape as [Code as Policies](code-as-policies-paper.md)' Table III and [LIBERO-PRO](libero-pro-paper.md) four years later.

**Real tabletop** (UR5e + MDETR, **10 runs/task**, with injected σ=4mm action noise):

| Task | LLM (Object only) | IM Object | IM Success | **IM Object+Success** |
|---|---:|---:|---:|---:|
| Finish 3-block stacking | 20% | 40% | 40% | **100%** |
| Sort fruits from bottles | 20% | 50% | 40% | **80%** |
| **Total** | 20% | 45% | 40% | **90%** |

The two feedback types are **complementary, not redundant**: each alone gets ~40–45%; together, 90%.

**Real kitchen mobile manipulation** (SayCan's environment, **120 evaluations**):

| Task family | SayCan | +IM Success | +IM Object+Success |
|---|---:|---:|---:|
| Manipulation (no disturbance) | 50.0% | 62.5% | **75.0%** |
| Mobile manipulation (no dist.) | 50.0% | 50.0% | **75.0%** |
| Drawers (no disturbance) | 83.3% | 83.3% | **100.0%** |
| Manipulation (**with** disturbance) | 12.5% | 25.0% | **33.3%** |
| Mobile manipulation (**with** dist.) | **0.0%** | 25.0% | **75.0%** |
| Drawers (**with** disturbance) | **0.0%** | 44.4% | **44.4%** |
| **Total** | **30.8%** | 48.7% | **60.4%** |

> [!note] The result worth carrying forward
> **Under adversarial disturbance, SayCan drops to 0% on two of three families** — "since it does not have explicitly high-level retry behavior." Closed-loop feedback is not a marginal improvement to open-loop planning; it is the difference between working and not working the moment anything goes wrong.
>
> This is the same lesson [ASPIRE](aspire-paper.md) re-derives in 2026 at finer granularity — its per-primitive traces move macro-average success 14% → 62%. Inner Monologue proved *that* feedback matters; ASPIRE proved *resolution* of feedback matters.

### Emergent behaviors
The paper reports capabilities it did not train for: continued adaptation to new instructions mid-task (a human changes their mind twice and the robot re-plans and resumes), multilingual instruction, and proposing new goals after human interaction.

## Entities mentioned
- **[Inner Monologue](../entities/inner-monologue.md)** — the subject of this source.
- [Google DeepMind](../entities/google-deepmind.md) (Robotics at Google) · [Everyday Robots](../entities/everyday-robots.md) · [CLIPort](../entities/cliport.md)
- [Wenlong Huang](../entities/wenlong-huang.md) · [Fei Xia](../entities/fei-xia.md) · [Andy Zeng](../entities/andy-zeng.md) · [Karol Hausman](../entities/karol-hausman.md) · [Brian Ichter](../entities/brian-ichter.md) · [Sergey Levine](../entities/sergey-levine.md)

## Concepts touched
- [Code as policy](../concepts/agents/code-as-policy.md) — the closed-loop branch of the lineage.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) · [Chain-of-thought](../concepts/learning/chain-of-thought.md) (used to improve goal/achievement consistency)
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) · [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md)

## Open questions
> [!warning] Oracle feedback in two of three domains
> The paper's own Limitations: "In Sec 4.1 and Sec 4.3, we assume access to **oracle scene descriptors** in the form of human observers or scripted systems." So the simulated tabletop and the real kitchen results both depend on feedback quality a deployed system would have to produce itself. Only the real tabletop experiment (§4.2) uses learned perception (MDETR) end-to-end.

- **Small n.** 10 runs per real tabletop task; 120 evaluations spread across 6 family×condition cells (≈20 each). The 45%-vs-40% Object-vs-Success comparison is not separable at n=20; the 20% → 90% headline is.
- The LLM sometimes **ignores the feedback** and proposes skills involving absent objects — an early sighting of the deference-calibration problem [Anthropic measures in 2026](anthropic-how-claude-performs-on-robotics-tasks.md).
- "No matter how much the LLM reasoning improves, it can still be bottlenecked by what low-level control policies are able to achieve" — the ceiling that motivates the whole code-writing branch.

## Related sources
- [SayCan](saycan-paper.md) — the baseline and the environment.
- [Code as Policies](code-as-policies-paper.md) — sibling paper, overlapping authors; the code branch rather than the feedback branch.
- [ASPIRE](aspire-paper.md) — the 2026 descendant that makes feedback *per-primitive* and measures the gain.
