---
title: Introducing Waddle — Agents that Control Robots
type: source
url: https://waddlelabs.ai/research/introducing-waddle
author: Waddle Team
affiliation: Waddle Labs
published: 2026-07
ingested: 2026-08-03
venue: Waddle Labs Blog
format: company blog post / position piece (product announcement)
local_path: raw/2026-07-waddle-labs-introducing-waddle.md
tags: [waddle, waddle-labs, code-as-policy, llm-agent, agentic-robotics, skill-library, vla, world-action-model, multi-agent, act, foundation-models, position-piece, primary-source]
---

## Summary

Company announcement from **[Waddle Labs](../entities/waddle-labs.md)** arguing that the dominant robot-learning recipe — collect large datasets and train an end-to-end [VLA](../concepts/learning/vla-models.md) or [world-action model](../concepts/world-models/world-action-model.md) that maps pixels+instruction directly to motor commands — has three deployment-blocking problems (data hunger, poor steerability, weak cross-embodiment generalization), and that none of these is intrinsic to large models: **LLMs** already train at internet scale, are steered by conversation, and transfer without finetuning. Waddle's bet is to transfer those properties into robotics by putting an **[LLM agent](../concepts/agents/llm-agent-architecture.md) on top** that decomposes goals, writes control code ([code as policy](../concepts/agents/code-as-policy.md)), and *calls* action models like VLAs as tools — rather than training a monolithic policy. The agent emits a runnable program you iterate on by talking to it.

This is a **position piece and product announcement, not a benchmarked paper**: it reports an architecture, three capability demos on real hardware, three use cases, and a scaling trend across three LLMs — but **no success rates, sample sizes, or confidence intervals** (see Open questions). Its most concrete external number is borrowed from Anthropic. Treat the capability claims as vendor claims pending independent evaluation.

## Key claims

### The core architecture — agent on top, action models as tools
- **Fig. 1 contrast.** Current pipeline: `Instructions → Action model (VLA/WAM) → actions → Robot`. Waddle's stack: `Instructions → Agent (code as actions) → subtask → Action model → actions → Robot`. The agent retains the ability to call action models as tools rather than replacing them.
- The agent "decomposes goals into subtasks, and complete[s] each one by viewing camera feeds, writing control code, and calling models like VLAs." Output is a program the user can run and iterate on conversationally.
- **Hypothesis, stated plainly:** LLMs are "uniquely capable of tool use, reasoning, and writing programs," and these capabilities can be transferred into robotics by using LLM agents to control robots. Explicitly framed as inheriting the code-as-policy line ([Code as Policies](../concepts/agents/code-as-policy.md), refs [6][7]).

### Three claimed capabilities (each "demonstrated on real hardware")
- **Generalist** — "Our agents work with any arms, grippers, and camera setups without new data collection." (The claimed antidote to VLA cross-embodiment finetuning.)
- **Long-horizon planning** — "Planning is done by the reasoning model, not the policy." The agent decomposes long tasks into stages, verifies intermediate outcomes, and re-plans on failure.
- **Multi-agent coordination** — scaling to more robots "does not require changes to the system": a master agent spawns subagents and coordinates multiple robots concurrently; "the same structure carries from a pair of arms to a fleet."

### The skills hierarchy — primitives → skills → programs (Fig. 2)
- Three levels: **PRIMITIVES** (fixed platform vocabulary, e.g. `bounding_box`, `detect_in_base`, `approach_until`, `reset_home`) → **SKILLS** (agent-created, parametrized, shared in a library, e.g. `fold_grasp`, `servo_align`, `orbit_view`, `top_grasp`) → **PROGRAM** (agent-written, per-task, composed of skills).
- **Skills transfer across tasks and agents.** The `fold_grasp` skill was first created by one agent flipping a package, then adapted by another agent to fold a t-shirt and a towel (Fig. 3 — one parametrized skill reused across three tasks). "This skill library allows agents to learn from experience and learn from each other."
- Contrasted with prior code-writing work where "the program was generated once per instruction" and revision came from human corrections or cheap-trial domains (games, software). Waddle claims to run the revise-against-execution loop continuously as a deployed system: robots connect via API, agents run against them continuously, and "every solved task adds skills to a library shared by all agents … nothing retrains between tasks."

### Three use cases (agent API)
- **"Create a working policy in 20 minutes"** — *"Write a program to place one microswitch inside each slot."*
- **"Generate data for model training"** — *"Pick and place lego bricks at random positions 1000 times."* The agent ran ~1,000 pick-and-place repetitions overnight and **autonomously trained an [ACT](../entities/act.md) policy from scratch** that could pick up LEGOs. (Agent-as-data-collector-and-trainer.)
- **"Facilitate robotics auto-research"** — *"I am tuning a policy overnight. Reset the scene after each trial."*

### Scaling with foundation models (Fig. 4)
- Evaluated **three LLMs — Opus 4.8, Fable 5, and GPT 5.6 Sol** — across a manipulation task suite. Reported trend: "larger models, given larger budgets, produce better policies." All models solved easy tasks ("pick up the lego"); **only Fable 5 and GPT 5.6 with `xhigh` thinking** solved harder tasks like "fold the t-shirt."
- Fig. 4 plots average success rate vs. cost per task (bold = `xhigh` thinking, light = `high` thinking); success rises with budget and larger models reach higher plateaus. **No axis values, success rates, task counts, or trial counts are given.**

### Next steps and the "billion robots" thesis
- **Tools that agents prefer** — cites **VIA** (visual interface agent, ref [15]) and **[Claude Plays Robotics](anthropic-how-claude-performs-on-robotics-tasks.md)** (Anthropic, ref [16]): "adding a movable cursor the model could query for position and depth raised success on a manipulation suite from **6% to 32%**." (See contradiction flag below.)
- **Benchmarks and standardized evaluation** — Waddle itself calls for a shared benchmark for agent-controlled robots, noting results across labs are hard to compare.
- **Training more capable agents** — "six months" of using agents to control robots has generated data and intervention traces they plan to use to train physical-task LLMs.
- **Mission:** "every robot will be directed by its own agent … There will be a billion robots. Our mission is to enable everyone to take part in building that future."

## Contradictions & flags

> [!warning] Waddle's characterization of the Anthropic result vs. the wiki's ingest of the same source
> Waddle cites [Claude Plays Robotics](anthropic-how-claude-performs-on-robotics-tasks.md) for a "movable cursor … position and depth" raising a manipulation suite **6% → 32%**. The wiki's existing ingest of that same Anthropic source (same URL, `anthropic.com/research/claude-plays-robotics`) recorded **end-to-end LIBERO manipulation topping out at ~5.5%**, and found passive **depth heatmaps / crosshair overlays "roughly neutral"** — with a real-world model that **"disregarded the depth information entirely."** These may be reconcilable (Waddle describes an *interactive, queryable* cursor tool, which is not the same as a passive depth overlay, and the "manipulation suite" may not be LIBERO-40), or Waddle may be quoting a result the wiki's ingest did not capture. **Unverified from here** — flagged for a re-read of the primary source. Recorded, not resolved.

> [!note] Evaluation rigor
> This source reports **no success rates, N, or confidence intervals** for any Waddle result — Fig. 4 is an unlabeled trend curve. Against this wiki's [VLA success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) standard (where even large published tables collapse into statistical ties at typical N≈50), every Waddle capability claim here is **anecdote-grade**: real-hardware demos, not measured success rates. The one quantified figure in the piece (6%→32%) is borrowed from Anthropic and is itself flagged above.

## Entities mentioned
- [Waddle Labs](../entities/waddle-labs.md) — the company; the Waddle agent / agent API is its product.
- [ACT (Action Chunking Transformer)](../entities/act.md) — the policy the agent autonomously trained from LEGO pick-and-place data.
- [Anthropic](../entities/anthropic.md) — via the [Claude Plays Robotics](anthropic-how-claude-performs-on-robotics-tasks.md) citation.
- Models named in Fig. 4 — **Opus 4.8, Fable 5, GPT 5.6 Sol** — no dedicated wiki pages (consistent with how the Anthropic robotics source's model list was handled).

## Concepts touched
- [Code as policy](../concepts/agents/code-as-policy.md) — the lineage Waddle explicitly builds on (this ingest creates that page).
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — Waddle is a code-as-actions instance of the planner-emits-actions-against-a-skill-library pattern.
- [VLA models](../concepts/learning/vla-models.md) — the paradigm Waddle positions against, but *calls as a tool* rather than replacing.
- [World-action models](../concepts/world-models/world-action-model.md) — grouped with VLAs as "action models" in Fig. 1.
- [Agent skills (portable SKILL.md)](../concepts/agents/agent-skills.md) — adjacent notion of shared, discoverable capability packages (Waddle's skill library is the *learned-motor-skill* analogue).
- [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md) — Waddle's "bigger model + bigger budget → better policy" is a foundation-model-scaling claim, here without numbers.

## Open questions
- **What are the actual success rates?** No numbers anywhere. A shared benchmark (which Waddle itself calls for) or an independent eval would move every claim here from anecdote to measurement.
- **Does "generalist across any arms/grippers/cameras without new data" hold under a real embodiment shift**, or only within the platform's fixed primitive set (`bounding_box`, `detect_in_base`, …), which itself has to be ported per robot?
- **The 6%→32% cursor result** — reconcile against the wiki's [Anthropic ingest](anthropic-how-claude-performs-on-robotics-tasks.md); is it a passive-overlay vs. queryable-tool distinction, a different task suite, or an uncaptured result? Needs the primary source.
- **How much does the agent actually call VLAs vs. write pure code?** Fig. 1 shows VLAs as callable tools, but the demos (microswitch insertion, LEGO pick-place, scene reset) read as classical perception+control code. The claimed VLA-as-tool integration is asserted, not demonstrated.
- ~~**CaP-X and ASPIRE** (refs [13][14], both arXiv 2026) are cited as the closest prior work. Neither is ingested~~ — **both ingested 2026-08-03**: [CaP-X](cap-x-paper.md), [ASPIRE](aspire-paper.md). They confirm the architectural bet and quantify the skill-library compounding claim, but contradict the strong reading of "works with any arms, grippers, and camera setups" — ASPIRE states the predefined API bounds expressible behavior and must be human-extended. See the [claim-by-claim comparison](../entities/waddle-labs.md) on the entity page.
- **Latency.** The [Anthropic robotics ingest](anthropic-how-claude-performs-on-robotics-tasks.md) puts an LLM-in-the-loop at 0.2–0.4 Hz against an ~83 Hz real-time requirement. Waddle's "agent writes a program you then run" sidesteps this (the agent is offline; the emitted code runs in the loop) — but the piece never states control rates. Worth confirming the agent is not in the fast loop.
