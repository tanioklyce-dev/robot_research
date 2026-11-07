---
title: "ToyBlocks: A controlled world for robot learning and evaluation (Ai2 blog)"
type: source
url: https://allenai.org/blog/toyblocks
local_path: raw/2026-11-06-ai2-toyblocks-blog.txt
sha256: c75f8d675bdd92ece435276e79c2a69207c7a9deca86fa96c1764ee16c8fc6cb
author: "Ai2 (no individual byline)"
published: 2026-11-06
venue: "Ai2 blog, with code (allenai.github.io/ToyBlocks), data and models on Hugging Face"
format: "blog post (HTML → text, nav and footer stripped); chart images were not captured as data"
license: "not stated in the post"
tags: [ai2, toyblocks, foundationworlds, simulation, isaac-lab, benchmark, evaluation, tamp, data-generation, vla, generalization, hierarchical-policy, molmo, maniflow, pi0.5, molmoact2, world-model-evaluation, lewm, wan, sim-to-real, franka, mcp, agents, claude, agent-skills]
ingested: 2026-11-07
---

# ToyBlocks: A controlled world for robot learning and evaluation (Ai2)

## Summary

[Ai2](../entities/ai2.md) introduces **FoundationWorlds**: a simulated world built to study one domain, packaged with automatic task and demonstration generators and with metrics. The first one is **[ToyBlocks](../entities/toyblocks.md)**, a single arm with lettered and pictured blocks on a tabletop. The pitch is the petri dish. A deliberately narrow domain is the only kind where you can have all four of realistic physics, generation at scale, tasks that need reasoning *and* dexterity, and coverage of the whole task space at once. Demonstrations come from RL-trained skills (flip, rotate, push) and motion-planned pick-and-place, sequenced by a [TAMP](../concepts/robotics/task-and-motion-planning.md) planner and run in parallel in [Isaac Lab](../entities/nvidia-isaac-lab.md) at up to 24× real time on one GPU. The post then uses that world for five studies:

- VLA spatial generalization.
- A hierarchical [Molmo 2](../entities/molmo.md) + ManiFlow system.
- Claude-driven agents acting through MCP.
- Action-conditioned world models scored against simulator ground truth: Wan 2.2, an agent-built simulator ("Astra") and [LeWM](../entities/leworldmodel.md).
- Zero-shot sim-to-real on a Franka FR3.

The release covers assets, generators, 85,336 long-horizon demonstrations (~1,600 h, 144 M frames), two trained models, training code, and evaluation code and validation sets.

## Key claims

### The framework
- A FoundationWorld must satisfy four requirements: *"(1) realistic physics and appearance, (2) automatic generation of tasks and demonstrations at scale, (3) challenges that combine reasoning with dexterity, and (4) broad coverage of the tasks possible within a domain."* Open-ended domains cannot meet all four. The narrow scope is the point.
- The block faces carry letters and pictures, so tasks include **search, sort and arrange**. A robot may have to turn a block over to see a hidden face. Domain randomization varies block size, table height and other physical properties.
- **Skill generation.** RL plus motion planning, trained in Isaac Lab. The RL skills are non-prehensile: pushing, and flipping a block onto another face without grasping it. Skill training may use **privileged state** (exact block pose), *"which would require teleoperation in the real world"* otherwise.

  > [!warning] Contradiction
  > The released code ([allenai/ToyBlocks](allenai-toyblocks-github.md)) has **scripted** flip and rotate skills (ported from a TAMP executor) and **no push skill**; push is excluded from generation by default. RL exists only as separate PPO scripts.

- **Demonstration generation.** A task-and-motion planner selects and sequences the skills and plans the motion between them. Each executed plan yields a labelled demonstration. Hundreds of plans run in parallel on one GPU, at up to **24× real time**.
- The trained models act from raw sensor observations, not privileged pose.
- **Evaluation metrics go beyond success.** They include execution speed, **forces exerted on objects**, and task progress, measured with the same specifications the planner uses.
- A web interface lets a frontier model such as Claude take natural-language instructions and drive the robot.
- Ai2 places ToyBlocks after [MolmoAct 2](../entities/molmoact2.md), MolmoBot and MolmoSpaces.

### Study 1: VLA spatial generalization
- The policies tested are **ManiFlow** (arXiv 2509.01819), **[π0.5](../entities/pi-zero-5.md)** and **[MolmoAct 2](../entities/molmoact2.md)**, on four tasks: Stack, Unstack, Flip, Rotate.
- Each task has an **interpolation** split (new configurations inside the training range) and an **extrapolation** split (outside it). Two examples:
  - Train on objects spawned in the left region, test on the right.
  - Train on stack heights 2 and 5, test on 3 and 4.
- Finding: *"Despite large-scale pretraining, these popular action models generalize poorly in the initial results."* Ai2 tries several techniques to improve this, LoRA among them, and attributes the gains. The per-technique numbers are in a chart this capture does not include.
- Ai2's position: *"action model generalization remains far from solved."*

### Study 2: Hierarchical VLM + low-level policy
- Molmo 2 is the planner. It picks a skill and **points** at the target block. ManiFlow executes, then pauses and queries Molmo 2 for the next step.
- **Oracles** exist at both levels, so a failure can be traced to the planner or to the executor.
- The tasks are three-letter spelling stacks, e.g. "Stack Ai2", at three difficulties:
  - Easy: letters upright and facing the camera.
  - Medium: letters not upright.
  - Hard: letters not visible at the start.

### Study 3: Frontier-model agents through MCP
- The ToyBlocks skills are exposed over **MCP**. The agent sees camera images, calls pick, flip or rotate **by pointing at a pixel**, and decides when to search, build, or declare a task complete or impossible. The same tools can run either the scripted skills or the learned ManiFlow skills.
- **Classical planning, with a system built on Claude Opus 5.5.** It solves **30/30** block-stacking tasks from text descriptions. The post says these tasks are similar to ones frontier models struggled with "a few years ago" and links to a NeurIPS 2023 Datasets & Benchmarks paper. It also solves **30/30** in closed loop from camera images.
- **Search-and-spell.** The agent builds a three-letter word from up to 8 blocks, and **50% of scenes are infeasible**, in which case it must say so.
  - It solved or correctly declared infeasible **63%** of tasks.
  - The main errors were look-alike letters (**13%**) and wrong letter orientation (**15%**).
  - When block faces follow a semantic pattern (an A-block carries apple, ant, A, a…), the agent declares infeasibility after seeing fewer faces. It infers what the hidden faces show instead of checking each one.
- **Self-written skill descriptions.** The agent experiments on its own skills, hypothesizing and testing, and rewrites their descriptions. Success rises from **24% with the default descriptions to 63%**, against **36% with descriptions written by a human expert**.
- A video shows **Claude Fable 5.1** running a controlled test of its own gripper's yaw convention, then building the "Ai2" tower with the 'A' sideways. The post says frontier models *"often make similar perceptual errors… despite their impressive planning, spatial reasoning, and search capabilities."*

### Study 4: Action-conditioned world models against ground truth
- **Setup.**
  - Four skills (pick-and-place, flip, rotate, mixed), **900 trajectories each**, half successful and half failed through small spatial changes, so always predicting success scores 50%.
  - Each model is fine-tuned, then **probed** for predicted block and gripper pose and for the final success outcome.
  - Two regimes: **full trajectory** (only the initial image is observed) and **interaction segment** (the model starts from the real frame just before a single pick, place, flip or rotate).
- **Models.**
  - **Wan 2.2**, a 5B video model (the post links the Wan report, arXiv 2503.20314).
  - **"Astra"**, *"an agentic model that created its own physics simulator tuned to match the demonstration data."* The link goes to an OpenAI "GPT-6 Astra" page.
  - **[LeWM](../entities/leworldmodel.md)**, a latent world model (arXiv 2603.19312).
- **Results.**
  - **Wan 2.2 predicts block motion and outcomes most accurately.**
  - **Astra** tracks the gripper well but *"struggles to simulate contact."*
  - **LeWM** is *"fast and more accurate over short interaction segments, though it drifts over full trajectories."*
- **World-model rollouts as training data.** Models that probe better also generate better data. Adding **100 rollouts from the best video model** raises a policy's success in an unseen region from **19% to 78%**.

### Study 5: Zero-shot sim-to-real
- **Hardware.** **Franka FR3** with a Robotiq gripper, a front ZED camera and a wrist ZED Mini. 30 scene configurations with 4–10 blocks seen in training. Any operator intervention counts as a failure.
- **Results.**
  - **ManiFlow atomic skills:** **80.0% sim vs 81.1% real.**
  - **Molmo 2 + ManiFlow spelling:** **55.5% (111/200) sim vs 50.0% (15/30) real**, on the easiest configuration only. The post itself says *"further trials are needed to establish statistical confidence."*
- **Transfer recipe, in three stages:**
  - **System identification** of joint friction and armature against real trajectories.
  - **Physical and visual domain randomization** (object size, friction, table height, lighting, backgrounds, materials, camera parameters).
  - **Stereo depth at inference time**, from **FastFoundationStereo** (arXiv 2512.11130) run on RGB pairs instead of the depth sensor.

### Release and roadmap
- **Released:**
  - Simulation assets.
  - Procedural task and demonstration generators.
  - **85,336 long-horizon demonstrations**, about 6–12 skills each: ~1,600 hours and 144 M frames.
  - Two trained models on Hugging Face, `allenai/Molmo2-4B-tb` and `allenai/maniflow-tb`.
  - Training code, plus evaluation code and validation sets.
- **Coming in "a few weeks":**
  - A larger dataset.
  - More skills.
  - More benchmarking.
  - Integrated RL training, which the current package does not contain.
- **Later directions:**
  - Bimanual manipulation.
  - Dexterous hands with force and touch sensing.
  - Play with unstructured block piles, to study emergent behaviour.

## Entities mentioned
- [ToyBlocks](../entities/toyblocks.md) · [Ai2](../entities/ai2.md)
- [Molmo](../entities/molmo.md) (Molmo 2) · [MolmoAct2](../entities/molmoact2.md) · [π0.5](../entities/pi-zero-5.md)
- [LeWorldModel](../entities/leworldmodel.md)
- [Isaac Lab](../entities/nvidia-isaac-lab.md) · [Franka](../entities/franka-panda.md) (FR3)
- [Anthropic](../entities/anthropic.md) (Claude Opus 5.5, Claude Fable 5.1) · [OpenAI](../entities/openai.md) (Astra, by link only)
- ManiFlow, Wan 2.2, FastFoundationStereo, MolmoBot and MolmoSpaces (no pages yet)

## Concepts touched
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md): a controlled world with metrics beyond success.
- [Task and motion planning](../concepts/robotics/task-and-motion-planning.md): TAMP used as a **demonstration generator**.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) and [world-model simulators](../concepts/world-models/world-model-simulators.md): ground-truth-state probing, with a JEPA model in the line-up.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md): sysID + DR + learned stereo depth.
- [VLA models](../concepts/learning/vla-models.md): the spatial-extrapolation failure.
- [Agent skills](../concepts/agents/agent-skills.md): self-written skill descriptions.
- [Synthetic data flywheel](../concepts/learning/synthetic-data-flywheel.md).

## Open questions
- **There is no paper.** The generalization chart, the spelling success rates by difficulty and the world-model probe scores are all images not captured here. Every quantitative claim above is the blog's own text. Ingest the technical report when one appears.
- **Seeds and intervals.** None are reported for the VLA or world-model studies. The sim-to-real hierarchical result is n = 30 real episodes, and the post flags this itself.
- **The data-engine result is under-specified.** "19% → 78% in an unseen region" with 100 rollouts. Which policy, which model, and how many real or sim demonstrations were in the baseline?
- **Is the LeWM drift a property of LeWM or of the protocol?** LeWM is trained to plan over short horizons, and the full-trajectory regime gives it one initial image only. Was LeWM's probe trained on its latents with the same budget as the pixel models' pose read-outs?
- **What exactly is "Astra"?** One sentence and an OpenAI link. Whether it is an Ai2 system using an OpenAI model or the OpenAI product is unclear.
- **Self-written skill descriptions (24 → 63%).** The post links an OpenReview paper for the method, not yet ingested. Does it transfer to other skill sets? *(Partly answered 2026-11-07: the method is **LEAP** in [allenai/agentic_robotics](allenai-agentic-robotics-github.md). The baselines are Control (declared docstrings), Naive, Harness and Oracle (expert), and the experimentation phase is capped by a dollar budget. Which condition and budget gave 63% is still not stated.)*
- **The agent studies use Anthropic models.** Claude Opus 5.5 and Claude Fable 5.1 are named. No other frontier model is reported, so whether the 63% is Claude-specific is unknown.
