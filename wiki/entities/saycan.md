---
title: SayCan
type: entity
subtype: system
created: 2026-08-03
updated: 2026-08-03
sources: 2
tags: [saycan, llm-agent, affordances, value-functions, skill-selection, google, palm]
---

**SayCan** ("Do As I Can, Not As I Say") — Robotics at Google / [Everyday Robots](everyday-robots.md), CoRL 2022. The canonical **LLM-proposes, affordance-disposes** system: an LLM scores how *relevant* each available skill is to the instruction, a learned value function scores how *feasible* it is from the current state, and the product selects the next action ([paper](../sources/saycan-paper.md)).

## Why it matters in this wiki
- **It is the branch [code-as-policy](../concepts/agents/code-as-policy.md) defines itself against.** Skill selection can only reach behaviors that already exist as named skills; [Code as Policies](../sources/code-as-policies-paper.md) uses "move the coke can a bit to the right" as the example SayCan structurally cannot express.
- **It is the origin of the "robot capability rides LLM progress" argument** — "a robot's performance can be improved simply by enhancing the underlying language model" — the same bet [Waddle](waddle-labs.md) makes fourteen years of model generations later.
- It is **level 3 (policy control)** in the [control abstraction taxonomy](../concepts/robotics/control-abstraction-levels.md), which [Anthropic's 2026 evaluation](../sources/anthropic-how-claude-performs-on-robotics-tasks.md) finds is where LLMs actually perform well.

## Headline numbers
101 instructions, 7 families, PaLM 540B, human-rated:
- **Mock kitchen 84% plan / 74% execute; real kitchen 81% / 60%** — the 14-point execution drop with only a 3-point plan drop locates the fragility in the *skills*, not the planner.
- Removing affordance grounding: 84% → 67% plan. Removing language grounding: **0%**.
- **~0% under adversarial disturbance** ([Inner Monologue](inner-monologue.md)'s measurement) — SayCan has no retry behavior.

## Related
- [Inner Monologue](inner-monologue.md) — the direct successor that closes the loop; uses SayCan's environment and takes it as baseline.
- [Code as Policies](../sources/code-as-policies-paper.md) — the rival branch.
- [Everyday Robots](everyday-robots.md) — the platform.
- [Chelsea Finn](chelsea-finn.md), [Sergey Levine](sergey-levine.md), [Brian Ichter](brian-ichter.md), [Karol Hausman](karol-hausman.md), [Fei Xia](fei-xia.md), [Andy Zeng](andy-zeng.md) — among the 40 authors.

## Mentioned in
- [SayCan paper](../sources/saycan-paper.md) — primary source.
- [Inner Monologue paper](../sources/inner-monologue-paper.md) — baseline and environment.
- [Code as Policies paper](../sources/code-as-policies-paper.md) — the contrast case.
- [Introducing Waddle](../sources/waddle-labs-introducing-waddle.md) — cited in Waddle's lineage survey.
