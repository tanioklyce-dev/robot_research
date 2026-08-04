---
title: ASPIRE
type: entity
subtype: system
created: 2026-08-03
updated: 2026-08-03
sources: 1
tags: [aspire, code-as-policy, skill-library, continual-learning, nvidia-gear, voyager, evolutionary-search, cross-embodiment, claude-opus]
---

**ASPIRE** (*Agentic Skill Programming through Iterative Robot Exploration*) — a continual-learning robotics system from [NVIDIA GEAR](nvidia-gear.md) + UMich + UIUC + UC Berkeley + CMU that **autonomously writes and repairs robot control programs** while compounding validated repairs into a **reusable skill library** ([paper](../sources/aspire-paper.md), Jun 2026). Built on [CaP-X](cap-x.md).

Project page: `https://research.nvidia.com/labs/gear/aspire/`

## The three components

1. **Closed-loop robot execution engine** — per-primitive multimodal traces (inputs, outputs, return codes, RGB keyframes before/after each call, perception overlays, grasp candidates, motion-planning results) so the agent can *localize which subsystem failed* rather than only learning that the task failed.
2. **Continually expanding skill library** — stores **heterogeneous repair knowledge**, not whole task programs: localization heuristics, perception prompts, grasping constraints, navigation recovery, motion primitives, debugging workflows. The taxonomy is **not prescribed in advance**; each skill is a failure signature + when-to-apply condition + repair strategy + optional code sketch.
3. **Evolutionary search** — a population of candidate programs conditioned on top performers and residual failure traces, to escape local repair loops.

**Coordinator–actor architecture:** a coordinator spawns one actor coding agent per task. Actors never share chat histories or raw rollouts — only distilled skills move through the library. The coordinator audits findings and admits only validated, reusable repairs.

**Model stack:** [Claude Code](anthropic.md) with **Claude Opus 4.6 (1M context)** for all simulation work; **OpenAI Codex GPT-5.5 (reasoning-xhigh)** for the real-robot study on a bimanual [YAM](yam.md) station.

## Headline results

- **LIBERO-Pro** — gains over the strongest baseline of **+77 / +41.5 / +42.5 points** on Object / Goal / Spatial (averaging position and instruction perturbation axes), against [OpenVLA](openvla.md) and [π0](pi-zero.md) at **0**.
- **[Robosuite](robosuite.md) bimanual handover — 20% → 92%.**
- **BEHAVIOR-1K** `navigate-and-pick-up-radio` task success **56% → 88%**; beats human experts on both BEHAVIOR tasks.
- **Zero-shot transfer** — a library accumulated on LIBERO-90 lifts held-out LIBERO-Pro Long from **4% → ~31%**, and success **rises with library size** (N = 0 → 25 → 50 → 90).
- **Real-robot cross-embodiment** — sim-discovered skills as in-context guidance take drawer opening from **0/20 to 11/20** while cutting tokens from 334.9M to 81.67M.
- **Ablation** — the execution engine alone drives **14% → 62%**; evolutionary search adds the last 10 points to **72%**.

## Why it matters in this wiki

- **It closes the Voyager loop on real robotics.** [Voyager](nvidia-gear.md) (TMLR 2024) is itself a GEAR paper; ASPIRE is the same lab porting its own open-ended skill-library pattern from Minecraft to manipulation — where trials are expensive and failures are physical. Shared authors include [Jim Fan](jim-fan.md) and Guanzhi Wang.
- **It is the wiki's first measured evidence that a skill library compounds.** The N∈{0,25,50,90} scaling curve is the specific claim [Waddle](waddle-labs.md) asserted and never quantified.
- **Its limitations section is the wiki's most useful reality-check on the paradigm** — see the [source page](../sources/aspire-paper.md); notably that the predefined API still bounds expressible behavior, which contradicts the strong reading of vendor "works with any embodiment" claims.

## Related
- [CaP-X](cap-x.md) — the framework it runs on and the baseline it beats.
- [NVIDIA GEAR](nvidia-gear.md) — home lab; also home of Voyager.
- [Code as policy](../concepts/agents/code-as-policy.md) · [Agent skills](../concepts/agents/agent-skills.md) — the concepts.
- [Waddle Labs](waddle-labs.md) — the commercial system making similar architectural claims without numbers.
- [Anthropic](anthropic.md) — Claude Opus 4.6 is the coding agent behind every simulation result.

## Mentioned in
- [ASPIRE paper](../sources/aspire-paper.md) — primary source.
