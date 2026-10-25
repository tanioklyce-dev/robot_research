---
title: RPG (Reconstruct, Practice, Go Real)
type: entity
subtype: system
created: 2026-10-24
updated: 2026-10-24
sources: 1
tags: [rpg, code-as-policy, agent-as-policy, self-improvement, skill-library, regression-gate, privileged-information, uc-berkeley, amazon-far, yam]
---

# RPG (Reconstruct, Practice, Go Real)

**RPG** is a framework from UC Berkeley and Amazon FAR (Wang, Jiang, Deng, …, Sastry, Abbeel, Qi; arXiv 2610.02204, 2026-10-01). It improves an **agent-as-policy** robot system by **rewriting its shared skill library and system prompt through practice in simulation**. Model weights are never updated ([paper](../sources/rpg-guided-self-improvement-paper.md)).

## How it works
- **Reconstruct:** practice tasks in MuJoCo, derived from an offline dataset (ABC), each with a human-checked success evaluator.
- **Practice:** a **Runtime Agent** and a **Privileged Agent** (adds simulator state) run each task. A **Video Analyzer** diagnoses the first failure. An **Implementor** proposes skill and prompt edits. A **Merger** keeps those that pass a cross-task gate: *mean up, no task down more than 20 pp*.
- **Go Real:** the system is calibrated and frozen for the physical [YAM](yam.md).

## Results ([paper](../sources/rpg-guided-self-improvement-paper.md))
- **Simulation:** 28.6% → **95.0%** over 15 rounds on 22 tasks × 10 held-out seeds, against [ASPIRE](aspire.md) 75.5% and [CaP-Agent0](cap-x.md) at best 60.0% (GPT-6 Astra Pro). The runtime is Gemini 3.8 Flash; offline revision uses Fable 5.1.
- **The largest single jump (+30.5 pp) was a prompt-only change** to how the agent spends its observation budget.
- The ablation needs **both** the Video Analyzer and the Privileged Agent. Either alone adds roughly nothing.
- **Physical:** 30/30 on three tasks. The physical towel criterion is easier than the simulation one.
- **Limits:** deformable folding plateaus in sim (a 1 cm-tolerance variant stays at 0/10); rate limits bind.

## Why it matters here
RPG is the most complete published **self-improvement loop with a regression gate** in the wiki: fixed evaluators, gated merges, held-out seeds excluded from selection. It extends the [Voyager](voyager.md) → [ASPIRE](aspire.md) line from skill accumulation to **library repair**. Many of its gains are bugs fixed in shared skills, such as a lift that reported its commanded height instead of its achieved height.

## Related
- [ASPIRE](aspire.md) · [CaP-X](cap-x.md) · [Voyager](voyager.md) — the lineage and baselines
- [Code as policy](../concepts/agents/code-as-policy.md) · [Agent skills](../concepts/agents/agent-skills.md)
- [YAM](yam.md) — the robot

## Mentioned in
- [RPG paper](../sources/rpg-guided-self-improvement-paper.md)
