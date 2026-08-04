---
title: Language to Rewards
type: entity
subtype: system
created: 2026-08-03
updated: 2026-08-03
sources: 2
tags: [language-to-rewards, code-as-policy, reward-design, mujoco-mpc, google-deepmind, quadruped]
---

**Language to Rewards** — Google DeepMind, CoRL 2023. Has an LLM write **reward-function parameters** rather than action code, optimized in real time by **MuJoCo MPC**, enabling a conversational behavior-authoring loop where the user describes a motion, watches it immediately, and corrects in language ([paper](../sources/language-to-rewards-paper.md)).

## The move it makes
Reward is the interface. The stated reasoning: "low-level robot actions are hardware-dependent and underrepresented in LLM training corpora," but reward functions are semantically rich and hardware-agnostic — exactly what an LLM can specify well.

Two LLM stages, not one: a **Motion Descriptor** expands the instruction into a structured motion description (via a per-morphology template), then a **Reward Coder** turns that into reward parameters. Skipping the intermediate description performs substantially worse.

## Headline numbers
17 tasks across a simulated quadruped and dexterous manipulator; 10 generated responses per task, each run 50x in MJPC:
- **90% of tasks solved vs 50% for a [Code as Policies](../sources/code-as-policies-paper.md) baseline** using primitive skills as the interface.
- Significantly better on **11 of 17** categories.
- Non-prehensile pushing **emerges** on a real arm without being a primitive.

The stated reason CaP loses is the recurring one: CaP does well on tasks expressible by the given primitives but "fails to generalize to novel low-level skills."

## Related
- [VoxPoser](voxposer.md) — the sibling "write the objective" paper, same conference; value maps rather than rewards.
- [Code as Policies](../sources/code-as-policies-paper.md) — the baseline.
- [MuJoCo](mujoco.md) — MJPC is the real-time optimizer.
- [NVIDIA GEAR](nvidia-gear.md) — the Eureka / DrEureka LLM-as-reward-designer line is the closest descendant.
- [Optimal control](../concepts/robotics/optimal-control.md) / [Code as policy](../concepts/agents/code-as-policy.md) — the concepts.

## Mentioned in
- [Language to Rewards paper](../sources/language-to-rewards-paper.md) — primary source.
- [Introducing Waddle](../sources/waddle-labs-introducing-waddle.md) — cited in Waddle's lineage survey.
