---
title: Code as policy
type: concept
created: 2026-08-03
updated: 2026-08-03
sources: 1
tags: [code-as-policy, llm-agent, agentic-robotics, program-synthesis, skill-library, voyager, saycan, tool-use, waddle]
---

# Code as policy

## Definition

**Code as policy** is the control pattern in which a language model, given a natural-language goal and a perception/actuation API, **writes an executable program** that runs on the robot — rather than emitting low-level actions directly (as a [VLA](../learning/vla-models.md) does) or selecting from a fixed menu of tool calls (the classic [LLM-agent](llm-agent-architecture.md) pattern). The program *is* the policy: it composes perception primitives, control primitives, and library skills into task-specific logic, with loops, conditionals, and verification.

It is best read as a **sub-pattern of [LLM-agent architecture](llm-agent-architecture.md)** where the action vocabulary is *arbitrary code* instead of a discrete tool schema. That distinction matters: a JSON-tool agent can only reach behaviors someone pre-named as tools; a code-writing agent can express new control flow — retries, servoing, parametrized sweeps — the tool designer never enumerated.

## The lineage (as surveyed by [Introducing Waddle](../../sources/waddle-labs-introducing-waddle.md))

The [Waddle](../../entities/waddle-labs.md) position piece frames its own approach as the deployed endpoint of a research line; the references below are its citations (none independently ingested yet — candidates for future ingests):

- **Code as Policies** (Liang et al., ICRA 2023, arXiv 2209.07753) — the seminal result that LLMs can write executable robot programs from language.
- **Model-writes-intermediate-structure variants** — instead of final motor code, the model writes an object for a downstream optimizer: **VoxPoser** (Huang et al., CoRL 2023) writes composable **3D value maps**; **Language to Rewards** (Yu et al., CoRL 2023) writes **reward functions** for skill synthesis.
- **Model-selects-skills variants** — the model chooses which pretrained skill runs next rather than writing code: **SayCan** ("Do As I Can, Not As I Say," Ahn et al., CoRL 2022) grounds language in **robotic affordances**; **Inner Monologue** (Huang et al., CoRL 2022) closes the loop with embodied feedback in-context.
- **The revision problem.** In the original code-writing line, the program was generated **once per instruction**; revision, where it existed, came from **human corrections** (Zha et al., 2023) or from **cheap-trial domains** — games (**Voyager**, Wang et al., 2023, in Minecraft) and software (**Executable Code Actions / CodeAct**, Wang et al., 2024).
- **Closing the loop autonomously (2026).** **CaP-X** (Fu et al., arXiv 2603.22435) benchmarks multi-turn coding agents that **revise against execution feedback on real embodiments**; **ASPIRE** (Lu et al., arXiv 2607.00272) pairs **failure diagnosis + repair** with a **growing skill library**, porting Voyager's Minecraft pattern to robotics.

Waddle reads this convergence — autonomous revise-against-execution + a persistent skill library — as evidence that code-as-policy "has become viable as a path towards robot intelligence," and claims to run it as a **deployed system** with a shared, cross-agent skill library and nothing retraining between tasks.

## The skills hierarchy

Code-as-policy systems tend to grow a **three-level abstraction stack** (explicit in Waddle's Fig. 2):

1. **Primitives** — a fixed vocabulary the platform provides (e.g. `bounding_box`, `detect_in_base`, `approach_until`, `reset_home`). Ported per robot; this is where embodiment-specificity actually lives.
2. **Skills** — parametrized, reusable routines the agent *authors* from primitives (e.g. `fold_grasp`, `servo_align`, `top_grasp`) and shares in a library. Skills transfer across tasks and across agents (Waddle: `fold_grasp` created while flipping a package, reused to fold a towel and a t-shirt).
3. **Programs** — per-task code the agent writes by composing skills.

This is the **motor-skill analogue** of [agent skills (portable SKILL.md)](agent-skills.md): both are shared, discoverable, reusable capability packages, but SKILL.md bundles are hand-authored runbooks + scripts, whereas a code-as-policy skill library is **agent-authored and grows from experience**.

## Related concepts
- [LLM-agent architecture](llm-agent-architecture.md) — the parent pattern; code-as-policy is the "action vocabulary = code" special case. That page's autoresearch example (edit/train/measure/commit) is the same loop with an ML-training target instead of a robot.
- [Agent skills (portable SKILL.md)](agent-skills.md) — the hand-authored-runbook cousin of the learned skill library.
- [VLA models](../learning/vla-models.md) — the end-to-end alternative; in the code-as-policy stack a VLA becomes a *callable tool*, not the whole policy.
- [World-action models](../world-models/world-action-model.md) — grouped with VLAs as "action models" a code-writing agent can call.
- [Guardrails for robot agents](../../syntheses/agents/guardrails-for-robot-agents.md) — an agent that writes *arbitrary code* widens the execution-rail problem beyond name-level tool allowlisting: `pick(knife)` was already hard to gate; freely-generated control code is harder.

## Current state

As of mid-2026 the pattern spans research demos (Code as Policies, VoxPoser), open-ended-agent skill libraries (Voyager → ASPIRE), autonomous revision benchmarks (CaP-X), and at least one deployed commercial API ([Waddle](../../entities/waddle-labs.md)). The wiki's evidence is **thin and vendor-sourced**: the one deployed system is documented only by a [position piece with no success rates](../../sources/waddle-labs-introducing-waddle.md), and the cited research papers are not yet ingested. The architectural argument (code > fixed-tool-menu for expressiveness; a shared skill library compounds across tasks) is coherent; the *measured* head-to-head against end-to-end VLAs does not yet exist here.

> [!note] Contrast with the wiki's other LLM-supervises-robot data point
> [Claude Plays Robotics](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md) measured a related-but-different setup — an LLM *in the loop* supervising a pretrained VLA — and found low-level control still broadly fails (LIBERO end-to-end ≤5.5%) and that supervision *hurts* in-distribution. Code-as-policy sidesteps the in-the-loop latency wall (the agent writes code *offline*; the emitted program runs the fast loop), but inherits the same open question: how good is the code the model writes, measured rather than demoed.

## Mentioned in
- [Introducing Waddle — Agents that Control Robots](../../sources/waddle-labs-introducing-waddle.md) — deployed code-as-policy system + the lineage survey this page is built from.
