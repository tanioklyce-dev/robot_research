---
title: "RoboDojo — RoboDojo-IsaacLabArena branch (GitHub READMEs)"
type: source
url: https://github.com/RoboDojo-Benchmark/RoboDojo/tree/RoboDojo-IsaacLabArena
fetch_url: https://raw.githubusercontent.com/RoboDojo-Benchmark/RoboDojo/RoboDojo-IsaacLabArena/README.md
local_path: raw/2026-11-07-robodojo-isaaclabarena-readme.md
sha256: 5eb38a143b5f991ebae43a037e04349bf1ee43114a9d5572c061bf0392f786c8
author: "RoboDojo team (Tianxing Chen et al.); branch PR by TonyTang-123"
published: 2026-10-30
venue: "GitHub repository branch (RoboDojo-Benchmark/RoboDojo); main project page robodojo-benchmark.com"
format: "branch README plus arena_migrate/, policy_eval/, agent_system/, multi_env/, Assets/ and policy/pi05/ READMEs, plus the main-branch README for context; GitHub API metadata"
license: MIT
related_raw: "raw/2026-11-07-robodojo-isaaclabarena-branch-readmes.md (branch sub-READMEs + main-branch README bundle)"
github_stats: "832 stars; repo created 2026-07-07; branch head 7689a6d (2026-10-30, merge of PR #79 'add IsaacLab Arena evaluation support'); 3 commits on the branch beyond main"
tags: [robodojo, isaac-lab-arena, isaac-sim, isaac-lab, benchmark, evaluation, pi0.5, openpi, arx-x5, bimanual, xpolicylab, robotwin, multi-env, deformable, github, mit]
ingested: 2026-11-07
---

# RoboDojo — RoboDojo-IsaacLabArena branch

## Summary

[RoboDojo](../entities/robodojo.md) is a sim-and-real manipulation benchmark from the team behind [RoboTwin](../entities/robotwin.md), released 2026-07-06 (arXiv 2607.04434). This branch ports its **42 simulation tasks, plus 12 `_random` variants**, onto **[Isaac Lab-Arena](../entities/isaac-lab-arena.md)**. The port uses the official layouts, object models and annotations unchanged, on the **ARX X5 dual-arm robot** (`dual_x5`), with a **π0.5** adapter as the one shipped policy. The full suite is **54 tasks and 2,100 episodes**. This is the "RoboDojo suite" that Arena's README listed as *coming soon* when the wiki captured it on 2026-09-14. It now exists, as a branch of RoboDojo's repo rather than in Arena's tree.

Most of the documentation is about making the evaluation **auditable**. The port pins dependencies and a 38.4 GiB asset snapshot by hash, ships CPU-only contract tests that parse the production code's AST, and refuses to mark a task done unless the per-episode details reconcile with the aggregates. Several environments run in one simulation, with heterogeneous layouts and per-slot termination. The branch does **not** publish success rates. It ships a tool for comparing against native-RoboDojo baselines but no comparison results, and its one real-model validation was a 7-task integration check, which the README says is *"not the full 54-task success-rate benchmark."*

## Key claims

### Scope
- **54 tasks** = 42 base + 12 `_random` variants. The 12 base/variant pairs get **25 episodes** each, and the other 30 base tasks get **50**, for **2,100 episodes** in total. `tasks.json` is the sole manifest.
- **Robot.** ARX X5 dual-arm. Arm joint stiffness/damping is **4000/40** and the gripper's is **2300/100**, written into an "evaluation control contract". A separate **support Franka** appears in some tasks, driven from recorded trajectories (`Traj/RoboDojo/`).
- **Task kinds.** Rigid, articulated, conveyor, support-arm, **fluid and cloth** tasks all use one entry point.
- **Policy.** A [π0.5](../entities/pi-zero-5.md) adapter (OpenPI) that takes head and wrist RGB plus a **14-D joint state**. The checkpoint is `RoboDojo-sim-arx_x5-joint-0` (step 59999), with `arx_x5_sim` norm stats. Also shipped: `debug_policy` and a `hold_policy`, the latter used for reset checks.
- **Outputs.** `_result.json` holds the episode count, success rate, a **process score on a 0–100 scale**, and per-layout details. Video is on by default, and HDF5 observation/action export is optional.

### Stack and pins
- **Platform.** Ubuntu 22.04/24.04, Python 3.11, **Isaac Sim 5.1.0**, Torch 2.7.0 / CUDA 12.8.
- **Pinned sources.** IsaacLab-Arena at commit `e25ccf5` and IsaacLab at `6acdd82`. A patch, `arena-offline-assets.patch`, lets Arena load assets offline.
- **Version mismatch.** Arena main is on Isaac Lab 3.0 / Isaac Sim 6.0 per the [Arena capture](isaaclab-arena-github.md). The port runs on Isaac Sim 5.1, so it pins an older Arena commit.
- **Assets.** These come from the Hugging Face dataset `RoboDojo-Benchmark/RoboDojo` at **pinned revision `269457a3`**: **9,977 files, 41,186,520,379 bytes (~38.4 GiB)**, verified by size and by LFS SHA-256 or git-blob SHA-1.
- **No substitution.** Objects are selected by exact official type, category and five-digit ID. *"IDs are not remapped and object types are not substituted."* Conflicting local files are reported, never overwritten.
- **Layouts.** All 54 tasks share the default **seed-0** layouts in `Eval_Layout/RoboDojo/arx_x5/0/`, with exact `<task>_<index>.json` matching.

### Multi-environment evaluation
- `NUM_ENVS` runs several **different real layouts** in one simulation, and **layouts are never duplicated to fill a batch**.
- Scenes whose global DomeLight settings differ must go in separate batches.
- Each slot latches success, failure or timeout independently. A finished slot holds its last targets and stops scoring and recording.
- `parallel_manifest.json` records batches, layout paths with **SHA-256**, slots and per-environment results.
- **Inference is per environment.** π0.5 runs its single-observation inference once per active environment. There is *no* model-level batch inference.
- **No split across GPUs.** Each GPU in `GPUS=0,1` runs its own simulation and model process. The split-GPU client/server setup used for validation is **not merged**.
- **Validation ("D-Robotics6").**
  - Scope: 7 representative tasks, 19 multi-environment episodes plus 1 single-environment episode, covering rigid, 4-environment heterogeneous pickup, articulated, conveyor, support-arm, cloth and fluid tasks.
  - Partial reset restored the selected environment with zero error and left sibling environments unchanged.
  - Stated scope: *"representative integration validation rather than the full 54-task success-rate benchmark."* The evidence artifacts are machine-local and **not in git**.

### Validation discipline
- **CPU-only checks.** `check_eval.py` and `agent_system/tests` need only the Python standard library and Bash. `control_contract.py` **inspects the production code's AST** to confirm the shared X5 gains and the task integration.
- **Completion rules.** A task is marked `done` only if the process returns 0, the result is complete, the episode counts match, and the aggregates agree with the per-episode details. *"A zero task success rate can still be a complete, valid evaluation result."*
- **Invalid layouts.** For support-arm tasks they are excluded from success-rate accounting and replaced with later layouts. A task fails if it cannot reach its quota of valid episodes.
- **Baseline comparison.** `compare_baseline.py` and `gap_investigate.py` compare a run against native-RoboDojo `_result.json` baselines and require *"matching checkpoints, seeds, and layout identities."* **No baseline results are included.**
- The README is careful about the limits of its own checks: *"CPU checks validate code and configuration; simulator behavior and policy success require actual GPU runs."*

### Native RoboDojo context (main-branch README)
- **Scope.** 42 sim tasks and 18 real-world tasks across 3 embodiments: Piper X, [Piper](../entities/agilex-piper.md) and ARX X5.
- **Capability axes.** Five of them: **Generalization, Memory, Precision, Long-Horizon, Open**. They are designed to probe *"different skills rather than simple object or layout reskins."*
- **Runtime.** Native RoboDojo runs on Isaac Sim, with heterogeneous parallel simulation, a RoboDojo-RealEval protocol and a live leaderboard.
- **Eval only.** Policies live in **XPolicyLab** (arXiv 2608.09892), which *"unifies 40+ policies behind one interface."*
- **Sept 16–17 fixes.** A single-frame `get_obs` discrepancy was fixed, and an RGB channel-ordering fix was made *"together with RoboTwin"*. Reruns were *"essentially unchanged."*

## Entities mentioned
- [RoboDojo](../entities/robodojo.md) · [Isaac Lab-Arena](../entities/isaac-lab-arena.md) · [Isaac Lab](../entities/nvidia-isaac-lab.md) · [Isaac Sim](../entities/nvidia-isaac-sim.md)
- [π0.5](../entities/pi-zero-5.md) · [Physical Intelligence](../entities/physical-intelligence.md) (OpenPI)
- [RoboTwin](../entities/robotwin.md) · [AgileX Piper](../entities/agilex-piper.md) · [Franka](../entities/franka-panda.md)
- ARX X5, XPolicyLab, D-Robotics (no pages)

## Concepts touched
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md): reproducibility as pinned hashes and reconciled aggregates. Also the question whether a benchmark ported between simulators still measures the same thing.

## Open questions
- **Parity.** Do π0.5 success rates on the Arena port match native RoboDojo, which also runs on Isaac Sim? The comparison tooling exists and the result does not. Until it is published, Arena-port numbers and native leaderboard numbers should not be mixed.
- **Upstreaming.** Will this merge into Arena's own catalog, as RoboTwin 2.0's branch is listed? Arena's README still read "coming soon" when the wiki last captured it (2026-09-14).
- **Version drift.** Arena main has moved to Isaac Sim 6.0 / Isaac Lab 3.0, and this branch pins 5.1. Expect re-pinning churn.
- **Throughput.** Inference is per environment rather than batched, so the multi-env speedup is capped by π0.5 latency × NUM_ENVS. No throughput figure is given.
- **Source depth.** The RoboDojo paper (2607.04434) and XPolicyLab (2608.09892) are not ingested. The [RoboDojo entity](../entities/robodojo.md) rests on the main README only.
