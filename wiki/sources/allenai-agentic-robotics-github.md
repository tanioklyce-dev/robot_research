---
title: "allenai/agentic_robotics — MCP agentic loop over ToyBlocks skills (GitHub)"
type: source
url: https://github.com/allenai/agentic_robotics
fetch_url: https://raw.githubusercontent.com/allenai/agentic_robotics/main/README.md
local_path: raw/2026-11-07-allenai-agentic-robotics-readme.md
sha256: ee2a375a8f3772f8c2704a033c258427250f3f4450e1b301f50c8de2486d28eb
author: "Ai2 (no individual authors named in the repo)"
published: 2026-11-05
venue: "GitHub repository; a submodule of ToyBlocks (installed via ToyBlocks's `agentic` extra)"
format: "README, CLAUDE.md, the LEAP prompts, the default experiment file, the oracle docstrings, and module docstrings for LEAP, the evaluation, the subagents, the harness and the Search & Spell scorer; GitHub API metadata"
license: Apache-2.0
related_raw: "raw/2026-11-07-allenai-agentic-robotics-bundle.md (CLAUDE.md, prompts, oracle docstrings, module docstrings)"
github_stats: "0 stars, 1 fork; created 2026-11-05; 19 commits, head 340731d (2026-11-06); 540 tree entries"
tags: [ai2, toyblocks, agents, mcp, agentic-loop, agent-skills, leap, tool-descriptions, claude, claude-agent-sdk, openrouter, search-and-spell, planbench, blocksworld, pddl, curobo, maniflow, isaac-sim, apache-2]
ingested: 2026-11-07
---

# allenai/agentic_robotics

## Summary

This is the code behind the frontier-agent studies in [Ai2's ToyBlocks post](ai2-toyblocks-blog.md). A vision-language model gets robot skills as **MCP tools** and runs a task by choosing tool calls, with **"no verifier and no success signal: the agent sees the post-state image and decides for itself what happened."** The repo's own statement of purpose is unusual: *"The output worth having is an account of **how the loop fails**, not a success rate."*

The architecture is a hard seam. `core/` is a robot-agnostic MCP host and model client (OpenAI Responses API, OpenRouter by default; any compatible endpoint, including local Ollama). Each robot domain is an MCP server behind an install extra, and only JSON crosses the boundary. The two run in separate Python interpreters, so `core` *cannot* import torch, Isaac Lab or ToyBlocks. There is one domain so far, [ToyBlocks](../entities/toyblocks.md) on Isaac Sim 5.1. Two skill backends sit behind it: scripted "oracle" skills (ToyBlocks's vecgen pick/place/flip/rotate, planned with [cuRobo](../entities/curobo.md) v2) and a served ManiFlow policy.

The repo releases three experiment families:
- **Search & Spell.**
- **Blocksworld** goals on color cubes, closed-loop and open-loop, plus a PlanBench-format language-only planner.
- **LEAP**, an *experimentation phase* in which an agent probes its own skills and rewrites their docstrings before a separate agent is evaluated with them.

LEAP is the source of the post's **24% → 63% (vs 36% expert)** result. The default model is **Claude Opus 5.5**.

## Key claims

### Architecture
- **The loop.** `AgenticLoop` runs model↔tool turns up to a `max_tool_calls` budget, re-injecting the remaining count each turn. It stops when the model calls no tool, then takes one final-answer turn.
- **A second host.** `claude_code_loop.py` runs the *same* loop inside **Claude Code via the Claude Agent SDK** (`--model-host claude-code`, pinned `claude-agent-sdk==0.2.174`). The SDK's hooks supply the per-call snapshots and the cutoff, and its dollar figure is recorded as `cost_source: "sdk_estimate"`.
- **Models.** The configured keys are `haiku-4.5`, `sonnet-5.5`, `opus-5.5`, `fable-5.1` and `gpt-6.1-sol-pro`. `default.toml` sets **`opus-5.5`**. The README's suite example uses `haiku-4.5`.
- **Pointing is in normalized coordinates.** The model points in a `[0,1000)` image space. Because the round trip through the pixel grid is lossy, the code never echoes a converted point back, since an agent told it asked for a different point *"will spend the episode hunting the difference instead of the block."*
- **Threading.** Isaac must be stepped from the thread that created it, so the simulator owns the main thread and the agent loop runs on a second one. Skill coroutines are dispatched back through a queue. Stepping PhysX from the wrong thread *crashes the process rather than raising*.
- **Preflight refuses bad scenes.** The block-asset check, scene preflight and reset-state check refuse to start a run on a scene the model cannot act in. One docstring records that a copied boot path without the block check *"let two pilots run on the wrong glyph library."*
- **The scripted skill surface** has nine tools: `get_zoomed_image`, `pick`, `stack`, `place_on_table`, `rotate`, `flip`, `return_home`, `open_gripper` and `close_gripper`. Each targets a block by pixel. The ManiFlow surface *"differ[s] on purpose."*

### "The model's interface is code"
- Tool names, schemas, docstrings and **the text of errors raised inside a skill** are *"behavior, not documentation… A skill's docstring is a prompt."* The repo's CLAUDE.md therefore reserves all agent-facing text, along with defaults and anything paper-visible, for the human developer: coding agents may propose wording but not write it.
- **Reproducibility.** A run's fully resolved config is written to `config.json`, *"so a result is reproducible from its artifacts alone."* No module holds mutable settings that another patches.

### LEAP: learning skill descriptions by experiment
- **Phase 1, experimentation.**
  - The agent gets the motor skills and perception tools, plus simulator get/set state, workspace files, `update_tool_docstring`, `clear_context`, and either `spawn_subagents` (**Naive**) or `plan_experiment`/`run_experiment` (**Harness**).
  - Harness's own motor skills *refuse every call*. It has to go through a hypothesis → success criteria → trials plan, which is validated and logged before anything runs, and each trial runs as a subagent on a pre-warmed pool simulator.
  - The phase ends when a **dollar budget** is spent. The prompt states token prices and warns that editing a docstring invalidates the prompt cache. The developer's stated plan is *"launch at $5, resume to $10, then to $50."*
- **Phase 2, evaluation.**
  - A fresh agent gets only the motor skills and the image perception tools, with one of four description sets:
    - **Control:** the declared docstrings.
    - **Naive / Harness:** the final snapshot of their experimentation phase.
    - **Oracle:** the developer's hand-written docstrings.
  - The tool set is checked against the declaration before the first call, and the run refuses to start on a mismatch.
- **Units.** A **task family** is one of 8 factor combinations: region {feasible, outside} × proximity {isolated, adjacent} × skill {flip, rotate}. Each family has 3 (feasible) or 9 (outside) PDDL **variants**, and 32 **instances** per variant are sampled. Evaluation uses instances 0 and 1 of every variant.
- **Budget.** The motor-call budget is **3× the optimal plan length**, which runs from 4 to 10 skills by family. The separate `ai2_stacked` task, with pre-stacked distractors, gets 60.
- **Recorded metrics:** success per conjunct, tool calls by category (motor/perception/other), model calls, dollars and wall-clock time. A module docstring calls LEAP a *"workshop paper."*
- **What the Oracle set contains.** The expert's docstrings state failure rates that the declared ones do not:
  - `stack` and `place_on_table` drop the block 6 cm above the target 10% of the time.
  - `rotate` turns the wrong way 25% of the time.
  - `flip` has no effect 10% of the time and goes the wrong direction 20% of the time.
  - `flip` displaces a block 1–3 cm, which can be used to separate it from a neighbour.
  - `pick` fails within ~3 cm of a stack.
  - There is a central "workable" table region.

  These are the kind of affordance facts LEAP is supposed to discover. The post reports that the agent-written descriptions beat these.

### Search & Spell (scorer is code-specified)
- A family fixes the target word, the block inventory (6–8 letter blocks plus color cubes), the initial stacks and each block's abstract orientation. **Every family hides the target letters at the start.**
- An infeasible family is its feasible twin with one letter's block(s) swapped for blocks carrying no letter of the word. Patterned and unpatterned collections share their layouts.
- **Success** requires a tower of *exactly three* blocks whose front faces spell the word, top to bottom, in either case, upright from the front camera, within a 45° yaw tolerance. The scorer also reports a `success_any_three` variant, *"should the developer read the rule that way instead."* On infeasible instances, success is always false, and the outcome that counts is the agent's **declared** claim, parsed from its final message.

### How the released suites were run
- One batch job per suite or LEAP phase on Ai2's Beaker cluster, on **one A100 80 GB**.
- Several Isaac processes in parallel, at **~7.6 GB each**.
- Model calls billed through OpenRouter.
- The cluster job specs are not released.

### CLAUDE.md as a research-code governance document
- The ~28 KB file is written for AI coding agents. Among its rules:
  - Ask before *any* choice that affects an experiment (step caps, scorer thresholds, prompts, defaults, the names of research units).
  - No speculative tests.
  - *"Surprising results get checked before they are explained."*
  - Never describe unrun code as working.
  - Runs that cost more than **$3** need the developer's explicit permission, and long runs go in detached tmux sessions with one watcher subagent.
  - Design history goes in commits, never in docstrings.
- It is a working example of a lab writing down how coding agents may touch experimental code. The reasoning is that agent-facing text and defaults *are* the experiment.

## Entities mentioned
- [ToyBlocks](../entities/toyblocks.md) · [Ai2](../entities/ai2.md)
- [Anthropic](../entities/anthropic.md) (Claude Opus 5.5 default; Haiku 4.5, Sonnet 5.5, Fable 5.1; the Claude Agent SDK and Claude Code) · [OpenAI](../entities/openai.md) (`gpt-6.1-sol-pro` configured)
- [cuRobo](../entities/curobo.md) · [Isaac Sim](../entities/nvidia-isaac-sim.md) · [Isaac Lab](../entities/nvidia-isaac-lab.md)
- ManiFlow, OpenRouter, PlanBench, Beaker (no pages)

## Concepts touched
- [Agent skills](../concepts/agents/agent-skills.md): skill docstrings as learned artifacts (LEAP).
- [LLM agent architecture](../concepts/agents/llm-agent-architecture.md): a robot-agnostic MCP host with domain servers, and two interchangeable hosts.
- [Agent hardware abstraction](../concepts/agents/agent-hardware-abstraction.md): the JSON-only seam between agent and robot.
- [Symbolic task planning](../concepts/agents/symbolic-task-planning.md): PDDL-generated tasks and PlanBench-format Blocksworld.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md): declared-outcome scoring for infeasible tasks.

## Open questions
- **No results in the repo.** The README says the experiments "behind the released results" are runnable, but neither the suite records nor the LEAP docstring snapshots are committed. The 24/36/63% figures exist only in the blog. Which condition produced 63%, Naive or Harness, and at what budget ($5, $10 or $50)?
- **The LEAP paper is not ingested.** The blog links OpenReview `gxEC7M0oZj`, and the code calls it a "workshop paper."
- **Single model family.** Every reported agent result uses Claude, though the client supports any OpenAI-compatible endpoint, including a configured `gpt-6.1-sol-pro`. Does LEAP's gain transfer to other models, or to a small local VLM through the Ollama path?
- **Where do the Oracle failure rates come from?** No noise injection was found in the scripted-skill server (searched for probability or noise parameters). They read as measured properties of the vecgen skills, but this is not confirmed.
- **Fragility of the scorer.** The tower must be exactly three blocks, and `success_any_three` is computed "should the developer read the rule that way." Which reading the published 63% Search & Spell figure used is not stated.
