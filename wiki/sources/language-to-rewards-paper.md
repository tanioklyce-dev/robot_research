---
title: "Language to Rewards for Robotic Skill Synthesis"
type: source
url: https://arxiv.org/abs/2306.08647
author: "Wenhao Yu, Nimrod Gileadi, Chuyuan Fu, Sean Kirmani, Kuang-Huei Lee, Montse Gonzalez Arenas, Hao-Tien Lewis Chiang, Tom Erez, Leonard Hasenclever, Jan Humplik, Brian Ichter, Ted Xiao, Peng Xu, Andy Zeng, Tingnan Zhang, Nicolas Heess, Dorsa Sadigh, Jie Tan, Yuval Tassa, Fei Xia"
affiliation: Google DeepMind
published: 2023-06-14
ingested: 2026-08-03
venue: CoRL 2023
format: conference paper (31 pp with appendices)
local_path: raw/2306.08647.pdf
sha256: 30584e7dfc10e654719cccb942686ef54654977e96c30d868ca0518f7f110b39
tags: [language-to-rewards, code-as-policy, reward-design, mujoco-mpc, quadruped, dexterous-manipulation, mpc, primary-source]
---

## Summary

**Language to Rewards** makes the same move as [VoxPoser](voxposer-paper.md) — have the LLM write an *objective* rather than a *call sequence* — but the objective is a **reward function**, optimized in real time by **MuJoCo MPC (MJPC)**. The motivating observation is sharp: "low-level robot actions are hardware-dependent and underrepresented in LLM training corpora," so LLMs should not emit actions; but reward functions are semantically rich, hardware-agnostic, and exactly the kind of thing an LLM can specify.

Because MJPC optimizes at interactive rates, the system supports a **conversational behavior-authoring loop** — the user describes a motion, watches it immediately, and corrects in language.

## Key claims

### Architecture — two LLM stages, not one
1. **Motion Descriptor** — expands the user instruction into a structured natural-language *motion description*, using a hand-designed template per robot morphology.
2. **Reward Coder** — translates that description into reward-function parameters.
3. **MuJoCo MPC** — optimizes the reward into control in real time.

The intermediate motion description is the paper's key ablation: going straight from instruction to reward code ("Reward Coder only") performs substantially worse.

### Results — 17 tasks, two morphologies

Simulated quadruped and dexterous manipulator. Protocol: **10 responses generated per task, each evaluated in MJPC 50 times** — so the metric captures end-to-end pipeline stability, not just best-of-N.

- **Headline: 90% of the 17 designed tasks solved, vs. 50% for a [Code as Policies](code-as-policies-paper.md) baseline using primitive skills as the interface.**
- Significantly higher success on **11 of 17** task categories; comparable on the rest.
- The stated reason CaP loses is the now-familiar one: CaP "can perform well on tasks that can be expressed by the given primitives (e.g. *Touch object*) or very close to the given examples in prompt (e.g. *Sit down*), but **fails to generalize to novel low-level skills**."
- Validated on a **real robot arm**, where non-prehensile pushing "emerges through our interactive system" without being a primitive.

> [!note] Three independent papers, one finding
> [VoxPoser](voxposer-paper.md) (CoRL 2023), Language to Rewards (CoRL 2023), and [CaP-X](cap-x-paper.md) (ICML 2026) all conclude that Code as Policies is **bounded by its primitive set**. The first two routed *around* the ceiling by changing the output representation; CaP-X was the first to *measure* it as a controlled variable. The 2026 "discovery" was established by CaP's immediate successors in 2023 — see [code as policy](../concepts/agents/code-as-policy.md).

## Entities mentioned
- **[Language to Rewards](../entities/language-to-rewards.md)** — the subject of this source.
- [Google DeepMind](../entities/google-deepmind.md) · [MuJoCo](../entities/mujoco.md) (MJPC as the real-time optimizer)
- [Brian Ichter](../entities/brian-ichter.md) · [Andy Zeng](../entities/andy-zeng.md) · [Fei Xia](../entities/fei-xia.md)

## Concepts touched
- [Code as policy](../concepts/agents/code-as-policy.md) — the "model writes a reward" branch.
- [Optimal control](../concepts/robotics/optimal-control.md) — MPC as the thing the LLM steers.
- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md) — LLM-as-reward-designer; the direct ancestor of Eureka/DrEureka in the [GEAR](../entities/nvidia-gear.md) line.
- [Whole-body control](../concepts/robotics/whole-body-control.md) — the quadruped half.

## Open questions
Stated limitations:
- **Motion-description templates are hand-designed per robot morphology** — manual work that must be redone for each new embodiment. *This is the same "the API/scaffold has to be ported per robot" cost that recurs through [ASPIRE](aspire-paper.md) and [Waddle](waddle-labs-introducing-waddle.md) in 2026; it never goes away, it only moves.*
- **Language-only interface** struggles with tasks not easily described in words ("walk gracefully"); multi-modal input proposed as a fix.

Wiki additions:
- **All quantitative results are in simulation.** The real-robot arm is a qualitative demonstration.
- "90% vs 50% of tasks" is a **task-level** metric over 17 tasks — i.e. roughly 15 vs 8.5 tasks. At n=17 this is a 6–7 task difference; directionally strong but not a precise effect size, and not the same unit as a per-trial success rate.

## Related sources
- [VoxPoser](voxposer-paper.md) — the sibling "write the objective" paper; value maps instead of rewards.
- [Code as Policies](code-as-policies-paper.md) — the baseline.
- [CaP-X](cap-x-paper.md) — the 2026 paper that measures the primitive-abstraction axis directly.
