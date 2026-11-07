---
title: ToyBlocks
type: entity
subtype: benchmark
created: 2026-11-07
updated: 2026-11-07
sources: 3
tags: [toyblocks, foundationworlds, ai2, simulation, isaac-lab, benchmark, evaluation, tamp, data-generation, generalization, world-model-evaluation, sim-to-real, mcp, agents]
---

# ToyBlocks

**ToyBlocks** is [Ai2](ai2.md)'s open simulation framework of one arm and lettered, pictured blocks on a tabletop, released 2026-11-06. It is the first **FoundationWorld**, Ai2's term for a deliberately narrow simulated domain that ships with automatic task and demonstration generators and with metrics. The stated purpose is controlled experiments on robot learning, like a petri dish ([Ai2 blog](../sources/ai2-toyblocks-blog.md)).

## What it is
- **Domain.** Pushing, flipping, rotating, picking and stacking blocks whose faces carry letters and images. That allows search, sort and spell tasks with hidden information.
- **Data engine.** Per the post, RL- and motion-planning-generated skills (the RL ones non-prehensile, trained on privileged state in [Isaac Lab](nvidia-isaac-lab.md)), sequenced by a [TAMP](../concepts/robotics/task-and-motion-planning.md) planner. *The released code differs; see the repository section below.* It runs at up to **24× real time** on one GPU, with hundreds of plans in parallel. Users control the training mixture: more flips, fewer picks, or a held-out region of the workspace.
- **Metrics.** Success, but also execution speed, **forces exerted on objects**, and task progress scored against the planner's own specifications.
- **Release.** 85,336 long-horizon demonstrations (~1,600 h, 144 M frames); `Molmo2-4B-tb` and `maniflow-tb` checkpoints; generators, training code and evaluation code. Integrated RL training and a larger dataset are promised in "a few weeks."

## What it has been used to show (all from the launch post; no paper yet)
- **VLAs extrapolate poorly.** ManiFlow, [π0.5](pi-zero-5.md) and [MolmoAct 2](molmoact2.md) were tested on held-out workspace regions and stack heights. Ai2: *"generalize poorly in the initial results."*
- **Hierarchy with oracles.** [Molmo 2](molmo.md) points at a block and picks the skill, and ManiFlow executes it. Oracles at each level separate planning failures from execution failures.
- **Frontier agents through MCP.** Built on Claude Opus 5.5:
  - 30/30 on classical block-stacking.
  - **63%** on search-and-spell, half of which is infeasible. Look-alike letters (13%) and orientation (15%) dominate the errors.
  - Self-written skill descriptions raise success from **24% to 63%**, against 36% for an expert's descriptions.
- **World models against ground-truth state.** 900 trajectories per skill, half of them failures.
  - **Wan 2.2** is the most accurate.
  - **"Astra"** is weak on contact.
  - **[LeWM](leworldmodel.md)** is fast and good on short interaction segments but drifts over full trajectories.
  - 100 rollouts from the best video model took a policy's unseen-region success from **19% to 78%**.
- **Zero-shot sim-to-real on a [Franka](franka-panda.md) FR3.**
  - ManiFlow skills: 80.0% sim vs 81.1% real.
  - Molmo 2 + ManiFlow spelling: 55.5% sim vs 50.0% real (15/30).
  - Recipe: sysID + DR + FastFoundationStereo depth.

## The repository: a PDDL-to-dataset compiler (2026-11-04)

[allenai/ToyBlocks](../sources/allenai-toyblocks-github.md) (Apache-2.0; Isaac Sim 5.1 / Isaac Lab 2.3.2; LeRobot 0.4.3; cuRobo v2) shows what the post compresses.

- **One PDDL goal drives everything.** From it the pipeline generates the environment, the reset states, an FF plan per environment, batched cuRobo-planned skills with a **verify → snapshot-retry → re-plan** loop (~256 environments per GPU), the success check and a **partial-progress metric** (the fraction of goal predicates satisfied).
- **Physics and pixels are separate.** Execution records no images. A kinematic render pass re-skins each episode N times under visual domain randomization, with glyph train/val splits.
- **Evaluation** starts from fresh scenes or the exact initial state of any dataset episode. It verifies the scene, can swap either level of the hierarchy for an oracle, and is GPU-batched.
- **TAMPER** is DAgger with a TAMP expert: it replans demonstrations from the states where the policy failed.
- **Determinism is deliberately given up.** All parallel environments share one PhysX scene, so per-episode outcomes depend on batch-mates. Runs should be compared only in aggregate.

> [!warning] Contradiction: how the skills are made
> The launch post says the non-prehensile skills (push, flip) are **learned by RL** ([Ai2 blog](../sources/ai2-toyblocks-blog.md)). In the released vecgen engine, **flip and rotate are scripted** trajectories ported from a TAMP executor, and **the push actions have no skill and are excluded by default** ([allenai/ToyBlocks](../sources/allenai-toyblocks-github.md)). PPO scripts exist (`isolate` task, 8,192 environments), and the post says integrated RL training is *not* in the current package. Which pipeline produced the 85,336 released demonstrations is unresolved.


The frontier-agent studies run on [allenai/agentic_robotics](../sources/allenai-agentic-robotics-github.md), an Apache-2.0 submodule of ToyBlocks. It is a robot-agnostic MCP host (`core/`) with ToyBlocks as its one domain server, and only JSON crosses the boundary between them. It has two model hosts: its own loop over OpenRouter, or Claude Code via the Agent SDK. The default model is Claude Opus 5.5. It releases the Search & Spell builder and scorer (an exact three-block tower, read from the front camera, 45° yaw tolerance; on infeasible tasks the agent's *declared* outcome is what is scored), the Blocksworld and PlanBench-format suites, and **LEAP**, the experimentation phase behind the 24% → 63% skill-description result. LEAP has four description sets: Control (declared), Naive (agent with subagents), Harness (a forced hypothesis → criteria → trials structure) and Oracle (expert-written). Suites ran on one A100 80 GB per job, ~7.6 GB per Isaac process. No result records are committed.

## Why it matters for this wiki
- **It is the first benchmark in the wiki to score a JEPA world model and video models on the same probe of state.** [World-model evaluation](../concepts/world-models/world-model-evaluation.md) had argued that the pixel and latent literatures cannot score each other, because video metrics need video. ToyBlocks sidesteps the problem by reading pose and outcome out of every model and comparing them with simulator truth. The LeWM verdict, good locally and drifting globally, matches the drift and collapse thread in the [LeWM](leworldmodel.md) page.
- **It is a test of the "controlled environment" argument in [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md),** made in software rather than hardware. The OpenArm cell fixes the visual conditions. ToyBlocks fixes the whole task distribution, and makes it editable.
- **The cost is narrowness.** Blocks are rigid and similar to one another, and the gripper is parallel-jaw. Whether findings here say anything about laundry is exactly what a FoundationWorld cannot answer about itself.

> [!note] Thin evidence base
> As of 2026-11-07 every *result* above comes from one blog post, with charts that were not captured. There are no seeds or intervals, and the real-robot hierarchical figure is n = 30.

## Related
- [Ai2](ai2.md) · [Molmo](molmo.md) · [MolmoAct2](molmoact2.md)
- [RoboDojo](robodojo.md) and [Isaac Lab-Arena](isaac-lab-arena.md) take a different route to evaluation: a broad benchmark in shared infrastructure, where ToyBlocks is a narrow world with editable data.
- [Task and motion planning](../concepts/robotics/task-and-motion-planning.md) · [Synthetic data flywheel](../concepts/learning/synthetic-data-flywheel.md)

## Mentioned in
- [ToyBlocks: A controlled world for robot learning and evaluation (Ai2 blog)](../sources/ai2-toyblocks-blog.md)
- [allenai/agentic_robotics](../sources/allenai-agentic-robotics-github.md) — the MCP agent harness, LEAP and the Search & Spell scorer.
- [allenai/ToyBlocks](../sources/allenai-toyblocks-github.md) — the framework: PDDL-driven vecgen datagen, render-many, evaluation with oracles and partial progress, TAMPER; scripted (not RL) flip/rotate in the released code.
