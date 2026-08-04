---
title: Waddle Labs
type: entity
subtype: company
created: 2026-08-03
updated: 2026-08-03
sources: 3
tags: [company, waddle, code-as-policy, llm-agent, agentic-robotics, skill-library, robot-api, startup]
---

**Waddle Labs** — a robotics-AI company building **Waddle**, an agent system (and agent API) that controls robots by putting an [LLM agent](../concepts/agents/llm-agent-architecture.md) on top of the stack: the agent decomposes a goal into subtasks, writes control code ([code as policy](../concepts/agents/code-as-policy.md)), and calls action models like [VLAs](../concepts/learning/vla-models.md) as tools, emitting a runnable program the user iterates on conversationally. Positioned explicitly *against* the end-to-end "train a monolithic policy" recipe ([Introducing Waddle](../sources/waddle-labs-introducing-waddle.md)).

> [!note] Coverage is one company blog post
> Everything below comes from a single **position-piece / product announcement** with no reported success rates, sample sizes, or CIs. Company facts (founding date, funding, team, location, hardware partners) are **not stated** in the source and are unknown to the wiki. Capability claims are vendor claims pending independent evaluation.

## The Waddle agent (product)

- **What it is** — an agent that controls robots via an **API**: "robots connect through our API, agents run against them continuously." Output is a program you run and refine by talking to the agent.
- **Architecture** — the agent sits *above* action models rather than replacing them (Fig. 1): `Instructions → Agent (code as actions) → subtask → Action model → actions → Robot`. See [code as policy](../concepts/agents/code-as-policy.md) for the lineage and [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) for the general pattern.
- **Skills library** — a three-level hierarchy: platform **primitives** → agent-authored, parametrized **skills** (shared across all agents) → per-task **programs**. Skills (e.g. `fold_grasp`) transfer across tasks and agents; "every solved task adds skills to a library shared by all agents" and "nothing retrains between tasks."

## Claimed capabilities

Because the controller is an LLM agent, Waddle claims it inherits the underlying model's properties (each "demonstrated on real hardware," none quantified):

- **Generalist** — works with "any arms, grippers, and camera setups without new data collection."
- **Long-horizon planning** — planning done by the reasoning model, not the policy; decompose → verify intermediate outcomes → re-plan on failure.
- **Multi-agent coordination** — a master agent spawns subagents to coordinate multiple robots concurrently; "the same structure carries from a pair of arms to a fleet."

## Demonstrated use cases

- **Fast policy authoring** — "create a working policy in 20 minutes" (e.g. place a microswitch in each slot).
- **Autonomous data generation + training** — asked to pick-and-place LEGO bricks ~1,000× overnight, the agent then **autonomously trained an [ACT](act.md) policy from scratch** that could pick up LEGOs. This is the wiki's first instance of an LLM agent used as an end-to-end data-collector *and* policy-trainer.
- **Robotics auto-research** — e.g. reset the scene after each overnight trial (the agent as lab assistant). Compare [Karpathy's autoresearch](../sources/karpathy-autoresearch.md) (same loop, ML-training target) documented under [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md).

## Stated direction

- **Tool design for agents** — cites [Claude Plays Robotics](../sources/anthropic-how-claude-performs-on-robotics-tasks.md) (queryable position/depth cursor, claimed 6%→32%) and VIA (visual interface agent) as evidence that interfaces dominate agent performance. (The 6%→32% figure is [flagged against the wiki's ingest of that source](../sources/waddle-labs-introducing-waddle.md).)
- **A shared benchmark** for agent-controlled robots — Waddle itself notes cross-lab results are not comparable.
- **Training physical-task LLMs** — "six months" of agent-controlled-robot deployment has produced data and intervention traces they plan to train on.
- **Thesis** — "every robot will be directed by its own agent … There will be a billion robots."

## Relation to prior work / the wiki's landscape

- **Same architectural family** as the [LLM-agent robot stacks](../concepts/agents/llm-agent-architecture.md) already documented ([stretch_ai](stretch-ai.md), [ROSOrin](rosorin.md)/[OpenClaw](openclaw.md), [Spot + Gemini Robotics-ER](../sources/bostondynamics-spot-gemini-robotics.md)) — but with two distinctive moves: **(1) code as actions** (the agent writes executable programs) rather than selecting from a fixed JSON tool menu, and **(2) a self-growing shared skill library** with cross-agent transfer.
- **Positioned against** the end-to-end VLA/WAM camp ([π0](pi-zero.md), [GR00T](nvidia-groot.md), [MolmoAct2](molmoact2.md), [Cosmos 3](nvidia-cosmos.md)) — yet *calls VLAs as tools*, so it is complementary rather than strictly rival.

## How the claims look now that the research is ingested

Waddle cited [CaP-X](cap-x.md) and [ASPIRE](aspire.md) as its closest prior work (refs [13][14]); **both are now ingested** ([CaP-X](../sources/cap-x-paper.md), [ASPIRE](../sources/aspire-paper.md)), which lets several vendor claims be checked against a research group with nothing to sell.

| Waddle claim | What the research shows |
|---|---|
| Code-as-policy "has become viable as a path towards robot intelligence" | **Supported.** ASPIRE beats post-trained VLAs by 41–77 points under perturbation and human experts on two long-horizon tasks. |
| A shared skill library lets agents "learn from experience and learn from each other" | **Supported and quantified.** ASPIRE's zero-shot transfer rises with library size (N = 0 → 90); Waddle never quantified this. |
| "Works with any arms, grippers, and camera setups without new data collection" | **Overstated.** ASPIRE states the predefined API "bounds the behaviors the agent can express" and must be human-extended; CaP-X needed per-embodiment primitive changes for bimanual hardware. Generality is real *within* the primitive set — which is exactly the wiki's standing suspicion, now confirmed. |
| A deployed always-on revise-against-execution loop | **Not yet demonstrated in research.** ASPIRE's own limitation: real deployment "still requires robust success detection, safe reset, safety monitoring, and calibration maintenance" — it is not yet a real-world lifelong learner. Waddle claims to run this; nobody has verified it. |

The research also surfaces the question Waddle's framing omits entirely: **cost**. ASPIRE reports 81.67M–334.9M tokens for a single real-robot task. "Nothing retrains between tasks" is true and does not mean cheap.

## Open questions

- Company basics — founding, funding, team, location, hardware partners — **all unstated**.
- No reported success rates or trial counts anywhere (see [source flags](../sources/waddle-labs-introducing-waddle.md)). The bar has risen: two 2026 papers in the same paradigm publish full protocols, so the absence is now conspicuous rather than merely typical.
- ~~Whether "generalist without new data" survives a genuine embodiment shift~~ — **largely answered**: bounded by the primitive set, per ASPIRE and CaP-X. What remains is how *much* porting Waddle's platform actually requires.
- How often the agent truly calls VLAs vs. writes classical perception+control code (the demos read as the latter). Note neither research system calls a VLA at all — both write classical perception+control code, which makes Waddle's "calls VLAs as tools" the *unvalidated* part of its architecture diagram.

## Mentioned in
- [Introducing Waddle — Agents that Control Robots](../sources/waddle-labs-introducing-waddle.md) — the founding source (company blog, Jul 2026).
- [CaP-X paper](../sources/cap-x-paper.md) — cited by Waddle as prior work; supplies the benchmark numbers Waddle omits.
- [ASPIRE paper](../sources/aspire-paper.md) — cited by Waddle as prior work; the research analogue of Waddle's skill-library claim.
