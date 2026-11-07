---
title: "allenai/ToyBlocks — repository and user-guide docs (GitHub)"
type: source
url: https://github.com/allenai/ToyBlocks
fetch_url: https://raw.githubusercontent.com/allenai/ToyBlocks/main/README.md
local_path: raw/2026-11-07-allenai-toyblocks-readme.md
sha256: fee95c1b36ac18d813a19c29311708a91d56f9da60e88f8fff645b50dee2085f
author: "Ai2 (no individual authors named in the README)"
published: 2026-11-04
venue: "GitHub repository; docs at allenai.github.io/ToyBlocks/docs; tech report 'coming soon'"
format: "README, CLAUDE.md, the full Sphinx user guide (install, datagen stages, rendering, training, evaluation, metrics, agentic robotics), TAMPER and HVLA task-suite design docs, the domain-randomization YAML reference, and the vecgen flip/rotate skill docstrings; GitHub API metadata"
license: Apache-2.0
related_raw: "raw/2026-11-07-allenai-toyblocks-docs-bundle.md (all docs markdown + skill docstrings)"
github_stats: "36 stars, 2 forks; created 2026-11-04; 70 commits; head 931fd7a (2026-11-07); 764 tree entries"
tags: [toyblocks, ai2, isaac-lab, isaac-sim, curobo, pddl, ff-planner, tamp, data-generation, lerobot, domain-randomization, rendering, maniflow, molmo, hierarchical-policy, evaluation, partial-progress, dagger, tamper, ppo, determinism, apache-2]
ingested: 2026-11-07
---

# allenai/ToyBlocks

## Summary

This is the framework behind the [ToyBlocks launch post](ai2-toyblocks-blog.md). The repository shows that ToyBlocks is mainly a **declarative data-generation and evaluation pipeline**. A task is a PDDL goal, and everything downstream is generated from it: the Isaac Lab environment, the reset states, the plans, the demonstrations, the success check and the partial-progress metric. Execution and visuals are deliberately separated. The **vecgen** engine runs an FF symbolic plan per environment, executes batched skills on a pool of [cuRobo](../entities/curobo.md) v2 solvers (~256 environments per GPU), verifies every skill's effect against the live simulator (snapshot-retry, then re-plan), and records trajectories with **no camera images**. A separate render stage replays the states kinematically under domain randomization, as many times as wanted. The output is [LeRobot](../entities/lerobot.md) v3, with the symbolic state, high- and low-level action labels and the goal on every frame.

Around that core sit:
- ManiFlow training (`maniflow-tb` submodule) and Molmo 2 high-level serving.
- GPU-parallel closed-loop evaluation with oracle substitution at either level.
- **TAMPER**, a DAgger-style loop that plans expert demonstrations *from the states where a policy failed*.
- Play data, PPO scripts, and the [agentic_robotics](allenai-agentic-robotics-github.md) submodule.

The repo also corrects part of the launch post. The released vecgen **flip and rotate skills are scripted** trajectories ported from a TAMP executor, not RL policies, and the **push actions have no skill** and are excluded from generation by default.

## Key claims

### Stack
- **Simulator.** Isaac Sim 5.1 through `isaaclab[isaacsim,all]==2.3.2.post1`, Python 3.11, torch ≥ 2.7 on CUDA 12.8 (driver ≥ 570).
- **Datasets.** `lerobot==0.4.3`.
- **Motion planning.** cuRobo v2 compiles its kernels at runtime with NVRTC, so no CUDA toolkit is needed.
- **Submodules:** `curobo` (NVlabs), `maniflow-tb` (Python package `hvla`, pinned to `c04eab7`), `molmo2` and `agentic_robotics`.
- **Assets.** About 280 MB, from a public R2 bucket, cached in `~/.toyblocks`. Datasets are listed on a GCS bucket (`toyblocks-data`) as well as Hugging Face.
- **Robot.** The default robot baked into generated tasks is `fr3_robotiq_gripper_sysid`. Configs include FR3 soft/softer, a DROID Franka, and `fr3_sysid_isaac_rcs`.

### Data generation ("vecgen")
- **Declarative and "correct by construction."**
  - Tasks are PDDL problems over `on`, `on_table`, `clear`, `ori_of` and similar predicates, from generators in `scripts/task_gen/` (stack_three, flip, rotate, pnp, and so on).
  - The FF planner is **vendored**. A CLAUDE.md rule says *"No TAMP. The TAMP submodule (`tmp3`) is gone,"* and a test enforces it.
  - After each skill the effect is checked in simulation. On failure the environment restores a pre-skill snapshot and retries, then re-plans. **An episode counts as successful only if the PDDL goal holds**, and failures go to a separate split.
- **Scale.**
  - One Isaac process per GPU, with hundreds of environments (*"256 per GPU in measured runs"*).
  - Batched skills on a cuRobo IK and trajectory-optimization solver pool, with a collision world per environment. FF plans take milliseconds on the CPU.
  - 8 problems share one process to amortize Isaac start-up.
- **Skills.** Each PDDL action maps to a vecgen skill class with `verify()`. An action with no skill fails as `"no program"`.
  - **`push_to_right` and `push_next_to` exist in the domain but have no skill** and are excluded by default.
  - **`flip`:** *"Reorient (scripted flip) skill, reusing the TAMP executor's flip geometry"*, a press-and-pull.
  - **`rotate`:** *"scripted grasp-and-twist."*
  - `pick` is ~90 lines.
- **Scene randomization (physics).**
  - **Defaults:** block size 0.03–0.05 m, table height ±0.05 m, **friction 0.5–0.5** (fixed by default), optional distractors, block x/y windows, optional collision-free random robot start pose, gripper closed with p = 0.5.
  - **Baked-in profiles:** each environment package bakes in 8 scene profiles drawn from these ranges, rather than sampling per episode.
- **Rendering (visuals).** Recorded states are replayed with no physics, under randomized lighting and sky images, table materials, camera pose and FOV, and block letters and colours. Glyph **train/val splits** are supported. One physics run can be rendered N times. The render seeds are recorded so evaluation can reproduce an episode's look, though *"rendered pixels match the original rendering closely but not exactly."*
- **Provenance.** Each run pins the git commit and saves its config, and the dataset carries source checksums and copies of the PDDL files. Interrupted runs resume.
- **Annotation.** This adds `goal.action` (e.g. `pick`, `push left`) and `goal.position`, the target's pixel in the front camera. That pixel is the **target heatmap** ManiFlow is conditioned on.
- **Play data.** Each scene plays a chain of goals with no reset in between, with DFA goal policies and skill balancing.

### Training
- ManiFlow (*"conditioned on language and on a target heatmap"*) is trained through `maniflow-tb` with `accelerate` and DeepSpeed ZeRO-2, multi-node via `torchrun`, on the merged LeRobot data.
- It uses a timm RGB backbone and `t5-small`. Datasets can be co-trained with sampling ratios, and the default validation hold-out is 5%.
- **RL.** `scripts/ppo_fast.py` and `run_ppo_train.sh` exist, for the `isolate` task with 8,192 environments and the sysID'd FR3. The launch post says *"fully integrated RL training capability… is not contained in the current package."*

### Evaluation
- **Parallelism.** Up to 50 environments per GPU in one Isaac scene, served by one **GPU-batched** policy call, with several GPU workers pulling from one episode queue. *"The Molmo2 + ManiFlow server accepts a single eval worker."*
- **Starting states.** An episode starts from a fresh unseen scene or from the **exact initial state of a recorded dataset episode**. **Scene verification** compares the eval scene with the recording before any numbers are reported.
- **Oracles** can replace the high-level or the low-level policy. Open-loop **replay** of the expert actions checks the setup.
- **Partial progress for free.** Goals are PDDL conjunctions, so the fraction of goal predicates satisfied is a progress metric for every task with no task-specific code. Per-conjunct first-true steps and change-point traces are recorded.
- **Other metrics:** joint, end-effector, collision, and task-specific (each one a tensor per environment, added in `evaluate()`).
- **Not bit-reproducible, by design.** All parallel environments share one PhysX scene (one environment's outcome can depend on its batch-mates), the GPU solver is nondeterministic, there is no per-environment physics step, and contact history survives teleport resets. The docs' advice: *"compare runs by aggregate metrics over many episodes."* `--deterministic-cuda` narrows the gap on one machine only.

### TAMPER (TAMP Expert Relabeling)
- *"A DAgger-style loop with a TAMP expert."* The states where a policy failed are captured at the moment before auto-reset. The vecgen expert replans from the scene read off each captured state toward the recorded goal, and the resulting demonstrations go back into training, *"so the next round of training data covers the distribution the policy visits."*

### HVLA task-suite design (internal proposal doc)
- The question: *"can a hierarchical VLA solve problems that classically require a TAMP planner?"* Every task family is evaluated in **clean / few distractors (1–3) / many distractors (6–12+)** scenes, including distractors that physically obstruct the goal.
- Each task is marked by datagen coverage, from 🟢 generable today down to ⛔ not specifiable. The blockers are named:
  - **G1: no region or absolute-pose predicate.** Eight tasks are blocked by it, six of them *only* on phrases like "the center".
  - **G3: no disjunction.** *"`exists` is rejected and `or` is silently flattened, which is the more dangerous failure."*
  - **Multi-block support.** `on` is single-support, so pyramids cannot be expressed.
- Held-out-word splits test high-level compositional generalization with the low-level skill set fixed.

## Entities mentioned
- [ToyBlocks](../entities/toyblocks.md) · [Ai2](../entities/ai2.md)
- [cuRobo](../entities/curobo.md) · [Isaac Lab](../entities/nvidia-isaac-lab.md) · [Isaac Sim](../entities/nvidia-isaac-sim.md) · [LeRobot](../entities/lerobot.md)
- [Molmo](../entities/molmo.md) (Molmo 2 high-level policy) · [Franka](../entities/franka-panda.md) (FR3, DROID Franka configs) · [DROID](../entities/droid.md) (scene and robot config)
- ManiFlow / maniflow-tb, FF planner (no pages)

## Concepts touched
- [Task and motion planning](../concepts/robotics/task-and-motion-planning.md): FF + cuRobo with verify-retry-replan as a data engine, and TAMPER.
- [Symbolic task planning](../concepts/agents/symbolic-task-planning.md): PDDL as the task language, and where its expressiveness runs out (G1/G3).
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md): automatic partial progress, oracle substitution, and shared-scene nondeterminism.
- [Synthetic data flywheel](../concepts/learning/synthetic-data-flywheel.md): render-many-times, and failure-state relabeling.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md): the sysID'd FR3 config and visual-only domain randomization at render time.

## Open questions
- **Which skills made the released dataset?** The launch post says RL-trained flip, rotate and push. The released vecgen code has scripted flip and rotate and no push. Either the 85,336-demonstration release used an earlier RL-skill pipeline, or "RL" refers to the start-pose generator (`PreRLPoseGenerator`) and the separate PPO scripts. The tech report should settle it.
- **Is friction actually randomized?** The default range is 0.5–0.5, and the post lists friction under domain randomization. It depends on whether the released datasets passed a wider range.
- **The batching trade-off.** Shared-scene nondeterminism means per-episode outcomes depend on batch composition. How large is the run-to-run spread in success rate? None is reported, and it bounds how small a difference the blog's comparisons can resolve.
- **Does TAMPER work?** No result for it is published yet.
