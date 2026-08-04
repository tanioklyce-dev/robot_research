---
title: Voyager
type: entity
subtype: system
created: 2026-08-03
updated: 2026-08-03
sources: 3
tags: [voyager, skill-library, lifelong-learning, minecraft, gpt-4, nvidia-gear, open-ended]
---

**Voyager** — [NVIDIA GEAR](nvidia-gear.md) + Caltech/UT Austin/Stanford/UW Madison, TMLR 2024. The first LLM-powered **lifelong learning agent** in Minecraft: continuously explores, acquires skills, and makes discoveries with no human intervention and **no gradient updates** ([paper](../sources/voyager-paper.md)).

## Three components — and their 2026 descendants
| Voyager (Minecraft) | [ASPIRE](aspire.md) (robots) |
|---|---|
| Automatic curriculum maximizing exploration | Evolutionary search over task sequences |
| Ever-growing skill library of executable code | Skill library of validated repair knowledge |
| Iterative prompting + self-verification | Robot execution engine with per-primitive traces |

**ASPIRE is the same lab porting this architecture to real manipulation**, with overlapping authorship ([Guanzhi Wang](guanzhi-wang.md), [Jim Fan](jim-fan.md), Ajay Mandlekar). This is why the wiki treats Voyager → ASPIRE as one line rather than two similar ideas.

## Headline numbers (all n=3 trials)
- **63 unique items** in 160 iterations — 3.3x the next best; 2.3x map traversal.
- Tech tree **15.3x faster** to wooden, 8.5x stone, 6.4x iron; **only method to reach diamond** (1 of 3 runs).
- **Zero-shot in a fresh world:** 3/3 on all four unseen tasks; every baseline 0/3.
- **Handing Voyager's skill library to AutoGPT** lifts it from 0/3 on everything to solving three of four tasks at least once — a library is portable capability, not cached work for its author.

## Why it matters in this wiki
It is the **cheap-trial-domain precedent** for autonomous revision: the whole loop assumes failures are free and resets instant, exactly the property [ASPIRE](aspire.md) notes real robots lack. And its limitations section flagged **cost** and **frontier-model dependence** in 2023 — the two constraints still unresolved in 2026.

## Related
- [ASPIRE](aspire.md) — the robotics port.
- [NVIDIA GEAR](nvidia-gear.md) — home lab; Voyager sits under the open-ended-agents pillar.
- [MineDojo](minedojo.md) — the environment.
- [CodeAct](codeact.md) — the sibling code-as-action-space argument for general agents.
- [Agent skills](../concepts/agents/agent-skills.md) / [Code as policy](../concepts/agents/code-as-policy.md) — the concepts.

## Mentioned in
- [Voyager paper](../sources/voyager-paper.md) — primary source.
- [ASPIRE paper](../sources/aspire-paper.md) — the architecture it ports.
- [CaP-X paper](../sources/cap-x-paper.md) — cited as motivation for CaP-Agent0's auto-synthesized skill library.
- [Introducing Waddle](../sources/waddle-labs-introducing-waddle.md) — cited in Waddle's lineage survey.
