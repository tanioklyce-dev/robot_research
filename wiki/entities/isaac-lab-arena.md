---
title: Isaac Lab-Arena
type: entity
subtype: product
created: 2026-09-14
updated: 2026-09-14
sources: 6
tags: [isaac-lab-arena, nvidia, isaac-lab, evaluation, benchmark, simulation, lightwheel, robolab, lerobot, envhub, osmo, sensitivity-analysis]
---

# Isaac Lab-Arena

**Isaac Lab-Arena** — NVIDIA's open-source (Apache-2.0) *benchmark-authoring and policy-evaluation* framework on top of [Isaac Lab](nvidia-isaac-lab.md): environments composed from independent **scene / embodiment / task** primitives, evaluated GPU-parallel across thousands of environments and multi-node through OSMO, with per-episode variation recording and a posterior-based sensitivity analysis to say *which* environment factor broke a policy. Co-developed with [Lightwheel](lightwheel.md); the productization path for [RoboLab](nvidia-robolab.md). **Alpha (v0.3.0)**, Isaac Lab 3.0 / Isaac Sim 6.0, Linux x86_64 only ([GitHub](../sources/isaaclab-arena-github.md)).

## What it does

| Workflow | What Arena provides ([README](../sources/isaaclab-arena-github.md)) |
|---|---|
| **Author** | `ArenaEnvBuilder` compiles scene + embodiment + task into a standard Isaac Lab `ManagerBasedRLEnvCfg`; relational placement (`On`, `NextTo`, `FaceTo`…) via a differentiable solver and a cuRobo reachability gate; sequential task chaining; **agentic generation** from a natural-language prompt (experimental); controlled *variations* over lighting, camera, background, mass. |
| **Execute** | One policy across thousands of parallel environments per run; experiments of many runs dispatched locally or through OSMO; GR00T, π0/π0.5 (OpenPI), Cosmos, DreamZero and custom policies behind one `get_action(env, obs)` contract, served over websockets. |
| **Analyze** | Predicate-based subtask progress; per-episode `episode_results.jsonl` with the sampled variations; `sbi` NPE/MNPE joint posterior conditioned on success. |

## Timeline

- **2025-08-15** repo created; **2025-11-25** `release/0.1.0` (composable task API, GR00T N1.5 static- and loco-manipulation workflows).
- **2026-01-05** announced as *pre-alpha* at CES ([NVIDIA blog](../sources/isaaclab-arena-github.md)) with LeRobot EnvHub integration ([HF blog](../sources/nvidia-hf-lerobot-open-robotics-blog.md) came in July; the January HF post is summarized on the source page).
- **v0.2.0** (≈ March 2026): Isaac Lab 3.0 / [Newton](newton-physics-engine.md), sequential tasks, relation solver, GR00T N1.6 + [DROID](droid.md), Galbot / AgiBot A2D embodiments, G1 WBC-AGILE velocity policy, RSL-RL evaluation.
- **v0.3.0** (September 2026): agentic environment generation, typed YAML experiments and multi-node OSMO dispatch, variations + sensitivity analysis, OpenPI / Cosmos / DreamZero policies, the **RoboLab catalog** (38 task specs against the 120 RoboLab tasks) and a **31-task DROID Kitchen Benchmark** on Lightwheel and Replicator kitchens, native `uv` install.

## Numbers held here

- Single RTX 5880 Ada, camera-free, zero-action: **5.4 → 2,390 env-steps/s** from 1 to 1,024 parallel environments; OSMO **7.95× at 8 GPUs** ([docs](../sources/isaaclab-arena-github.md)).
- Lightwheel's headline: 10 RoboCasa tasks × 4,096 variations, GR00T N1.5, 8 GPUs — **0.76 h parallel vs 34.9 h sequential (40×)**.
- Agentic generation: p50 **5–18 s** to first spec; kitchen layout resolution at 1,280 layouts **up to 649 s**.
- **No policy success rates are published in the repo or docs** — the catalogs show executions, not scores.

## Embodiments registered

Franka (IK / joint), [DROID](droid.md), GR1T2 ([Fourier GR-1](fourier-gr-1.md)), [Unitree G1](unitree-g1.md) (WBC + navigation), Galbot, [AgiBot](agibot.md) A2D, Kuka + Allegro. Nothing in the hobby tier.

## Ecosystem (README "Published Benchmarks")

[Lightwheel](lightwheel.md) RoboFinals, RoboCasa Tasks (138+), LIBERO Tasks; [RoboTwin 2.0](robotwin.md) on an `IsaacLab-Arena` branch; [LeRobot](lerobot.md) Environment Hub; Isaac for Healthcare RHEO. Announced: RoboDojo, RLWRLD DexBench, UC Berkeley, X Square, Sharpa, [GEAR](nvidia-gear.md) *G1 Factory*.

## Why it matters for this wiki

It is the **infrastructure pole** of [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md): RoboLab argued a ±2 pp band needs ≈1,030 rollouts; Arena is the machine that makes 1,030 rollouts per condition a few minutes on one GPU, and the variation-plus-posterior loop is the diagnostic that turns a frozen leaderboard score into *"which factor."* It is also where NVIDIA's own policies are scored: the [Cosmos 3](nvidia-cosmos.md) RoboLab-120 numbers and the [GR00T e2e workflow](../sources/nvidia-gr00t-e2e-workflow-docs.md) sim path both run through it. The gaps are the usual ones — sim-only, no published sim-to-real correlation for its own scores, and a hardware floor (RTX workstation, x86_64) that excludes [DGX Spark](dgx-spark.md) natively and Jetson entirely.

## Related
- [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — the substrate it extends.
- [RoboLab](nvidia-robolab.md) — methodology and task catalog folded in.
- [RoboArena](roboarena.md) — the real-world, pairwise-preference counterpart.
- [Lightwheel](lightwheel.md) — co-developer.
- [LeRobot](lerobot.md) — EnvHub distribution.
- [The NVIDIA robot-AI stack](../syntheses/platforms/nvidia-robot-ai-stack.md) — where this sits among the layers.

## Mentioned in
- [Isaac Lab-Arena GitHub](../sources/isaaclab-arena-github.md) — primary: README, v0.3 docs, release notes, announcement blogs.
- [NVIDIA + HF LeRobot partnership blog](../sources/nvidia-hf-lerobot-open-robotics-blog.md) — EnvHub registration (July 2026).
- [GR00T end-to-end workflow docs](../sources/nvidia-gr00t-e2e-workflow-docs.md) — the sim path of the G1 pick-and-place workflow.
- [How to Evaluate General-Purpose Robot Policies](../sources/nvidia-robolab-evaluation-blog.md) — "productization stated for August 2026."
- [Post-train Cosmos 3 Edge](../sources/nvidia-cosmos3-edge-post-training-blog.md) — the RoboLab client for closed-loop Edge-policy evaluation.
- [RoboLab project page](../sources/nvidia-robolab-project.md) — the benchmark whose catalog Arena now carries.
