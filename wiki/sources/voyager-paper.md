---
title: "Voyager: An Open-Ended Embodied Agent with Large Language Models"
type: source
url: https://arxiv.org/abs/2305.16291
author: "Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi \"Jim\" Fan, Anima Anandkumar"
affiliation: NVIDIA, Caltech, UT Austin, Stanford, UW Madison
published: 2023-05-25
ingested: 2026-08-03
venue: TMLR 2024
format: research paper (42 pp with appendices)
local_path: raw/2305.16291.pdf
license: arXiv preprint (v2, 2023-10-19)
tags: [voyager, skill-library, lifelong-learning, open-ended, minecraft, gpt-4, self-verification, curriculum, nvidia-gear, primary-source]
---

## Summary

**Voyager** is the skill-library ancestor of [ASPIRE](aspire-paper.md) — and, as this wiki now records, *literally the same lab and several of the same authors*. It is the first LLM-powered lifelong learning agent in Minecraft: it continuously explores, acquires skills, and makes discoveries with **no human intervention and no gradient updates**, interacting with GPT-4 through blackbox queries only.

Three components, which map almost one-to-one onto ASPIRE's three components three years later:

| Voyager (2023, Minecraft) | [ASPIRE](aspire-paper.md) (2026, robots) |
|---|---|
| Automatic curriculum maximizing exploration | Evolutionary search over task sequences |
| Ever-growing skill library of **executable code** | Skill library of validated **repair knowledge** |
| Iterative prompting: env feedback + execution errors + **self-verification** | Robot execution engine: per-primitive multimodal traces |

Skills are stored as code and prompted to be "generic and reusable," so they compound compositionally and — the paper stresses — **alleviate catastrophic forgetting**, the failure mode that motivates lifelong-learning benchmarks like [LIBERO](../entities/libero.md).

## Key claims

### Exploration and tech-tree mastery

Baselines are ReAct, Reflexion, and AutoGPT, re-implemented for MineDojo. **All results are over 3 trials.**

- **63 unique items** discovered in 160 prompting iterations — **3.3×** the next best.
- **2.3× longer** map traversal.
- Tech tree (fewer iterations is better; fractions are successful runs of 3):

| Method | Wooden | Stone | Iron | Diamond |
|---|---|---|---|---|
| ReAct | 0/3 | 0/3 | 0/3 | 0/3 |
| Reflexion | 0/3 | 0/3 | 0/3 | 0/3 |
| AutoGPT | 92±72 (3/3) | 94±72 (3/3) | 135±103 (3/3) | 0/3 |
| Voyager w/o skill library | 7±2 (3/3) | 9±4 (3/3) | 29±11 (3/3) | 0/3 |
| **Voyager** | **6±2** (3/3) | **11±2** (3/3) | **21±7** (3/3) | **102 (1/3)** |

**15.3× faster** to wooden, 8.5× to stone, 6.4× to iron, and the only method to reach diamond — once, in one of three runs.

### Zero-shot generalization — and the cross-agent skill transfer result

Inventory cleared, new world, unseen tasks (max 50 iterations, 3 attempts):

| Method | Diamond Pickaxe | Golden Sword | Lava Bucket | Compass |
|---|---|---|---|---|
| ReAct / Reflexion / AutoGPT | 0/3 | 0/3 | 0/3 | 0/3 |
| **AutoGPT + Voyager's skill library** | 39 (1/3) | 30 (1/3) | 0/3 | 30 (2/3) |
| Voyager w/o skill library | 36 (2/3) | 30±9 (3/3) | 27±9 (3/3) | 26±3 (3/3) |
| **Voyager** | **19±3 (3/3)** | **18±7 (3/3)** | **21±5 (3/3)** | **18±2 (3/3)** |

> [!note] The skill library transfers to a *different agent architecture*
> Handing Voyager's library to **AutoGPT** lifts it from 0/3 on every task to solving three of four at least once. This is the 2023 precursor of the cross-agent and cross-embodiment transfer claims made by [ASPIRE](aspire-paper.md) (sim→real, Claude-authored→GPT-consumed) and asserted without evidence by [Waddle](waddle-labs-introducing-waddle.md). A skill library is portable capability, not just cached work for its author.

## Entities mentioned
- **[Voyager](../entities/voyager.md)** — the subject of this source.
- [NVIDIA GEAR](../entities/nvidia-gear.md) — Voyager is a GEAR paper, listed under its open-ended-agents pillar
- [Guanzhi Wang](../entities/guanzhi-wang.md) (first author; also on [CaP-X](cap-x-paper.md) **and** [ASPIRE](aspire-paper.md)) · [Jim Fan](../entities/jim-fan.md) · [Yuke Zhu](../entities/yuke-zhu.md) · Ajay Mandlekar (also on ASPIRE)
- [MineDojo](../entities/minedojo.md) — the environment substrate

## Concepts touched
- [Code as policy](../concepts/agents/code-as-policy.md) — Voyager's action space is literally code; it is the "cheap-trial domain" precedent for autonomous revision.
- [Agent skills](../concepts/agents/agent-skills.md) — the agent-authored library.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) · [Chain-of-thought](../concepts/learning/chain-of-thought.md)

## Open questions

Stated limitations — the first is the one the wiki has been chasing:

> [!warning] Cost was flagged as limitation #1, in 2023
> "The GPT-4 API incurs significant costs. It is **15× more expensive than GPT-3.5**. Nevertheless, Voyager requires the quantum leap in code generation quality from GPT-4, which GPT-3.5 and open-source LLMs cannot provide."
>
> Both halves recur verbatim in 2026: [ASPIRE](aspire-paper.md) reports 334.9M tokens for one real-robot task and states it "has not verified that smaller or weaker LLMs can sustain the same debugging loop." **Three years, same two constraints.** The wiki's [audit directive to record compute at ingest](../syntheses/platforms/vla-success-rate-audit.md) has a 2023 precedent nobody acted on either.

- **Hallucinations** — the curriculum proposes items that don't exist ("copper sword"); GPT-4 calls absent APIs and treats cobblestone as fuel.
- **Self-verification fails sometimes** — e.g. not recognizing spider string as evidence a spider was beaten.
- **n=3 for every headline number.** The 3.3×/2.3×/15.3× multipliers and every tech-tree cell rest on three runs. Diamond at "1/3" is a single success. These are demonstrations of a capability gap, not estimates of a rate — and the gaps against 0/3 baselines are the only ones that would survive any statistical bar.
- **Minecraft is a cheap-trial domain.** The paper's whole loop depends on failures being free and resets being instant — exactly the property [ASPIRE](aspire-paper.md) says real robots lack ("real-world deployment still requires robust success detection, safe reset, safety monitoring, and calibration maintenance").

## Related sources
- [ASPIRE](aspire-paper.md) — the robotics port, same lab, overlapping authors.
- [CaP-X](cap-x-paper.md) — cites Voyager as the motivation for its auto-synthesized skill library.
- [CodeAct](codeact-paper.md) — the sibling "code as action space" argument, made for general agents rather than embodied ones.
- [Introducing Waddle](waddle-labs-introducing-waddle.md) — the commercial claim whose skill-library architecture is Voyager's.
