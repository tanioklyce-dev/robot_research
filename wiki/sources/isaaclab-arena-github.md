---
title: "Isaac Lab-Arena GitHub (isaac-sim/IsaacLab-Arena) — README, v0.3.0 docs and release notes"
type: source
url: https://github.com/isaac-sim/IsaacLab-Arena
fetch_url: https://raw.githubusercontent.com/isaac-sim/IsaacLab-Arena/main/README.md
local_path: raw/2026-09-14-isaaclab-arena-github-readme.md
sha256: 0a9f93a4eb627cabb5589a8bca970e15693894c9bf34c7f0a399cd4c04ef0f52
author: "NVIDIA Robotics (Isaac Lab-Arena core team), with Lightwheel and NVIDIA SRL RoboLab contributors"
published: 2025-11-25
venue: "GitHub repository + Sphinx docs (isaac-sim.github.io/IsaacLab-Arena, release/0.3.0)"
format: "repository README, docs pages (release notes, motivation, performance, policy, sensitivity analysis, model selection, catalogs), pyproject, CONTRIBUTORS.md, GitHub API metadata; plus the 2026-01-05 NVIDIA announcement blog and the same-day HF blog"
github_stats: "564 stars, 104 forks, 137 open issues, 901 merged PRs, 23 GitHub contributors; created 2025-08-15, pushed 2026-09-15 (captured 2026-09-14)"
latest_release: "v0.3.0 (release/0.3.0 branch, alpha; last cherry-pick 2026-09-14); main tracks v0.3.0 + Isaac Lab 3.0"
related_raw: "raw/2026-09-14-isaaclab-arena-docs-v0.3-bundle.md (docs pages), raw/2026-01-05-nvidia-blog-isaac-lab-arena.txt (announcement blog)"
tags: [isaac-lab-arena, isaac-lab, isaac-sim, nvidia, lightwheel, robolab, evaluation, benchmark, simulation, github, droid, gr00t, openpi, pi0, cosmos, dreamzero, lerobot, envhub, newton, osmo, sensitivity-analysis, npe, agentic-environment-generation, apache-2]
ingested: 2026-09-14
---

# Isaac Lab-Arena GitHub (isaac-sim/IsaacLab-Arena)

## Summary

The repository for **[Isaac Lab-Arena](../entities/isaac-lab-arena.md)**, NVIDIA's open-source *"composable environment creation and policy evaluation"* layer on top of [Isaac Lab](../entities/nvidia-isaac-lab.md). Its thesis, stated in the docs' motivation page, is that **the evaluation space scales combinatorially and the evaluation stack does not**: every new object or robot becomes another hand-copied Isaac Lab config, every benchmark rebuilds the same policy adapters and result collectors, frozen leaderboards *"show what failed, but not where or which environment factor exposed the weakness,"* and sequential rollouts force teams to cut seeds and variations to meet a deadline. Arena's answer has three parts. **Author**: environments are composed from three independent primitives — a *scene*, an *embodiment* and a *task* — which `ArenaEnvBuilder` compiles into a standard Isaac Lab `ManagerBasedRLEnvCfg`; objects are placed by *relations* (`On`, `NextTo`, `FaceTo`…) solved differentiably rather than by coordinates, and since v0.3 an LLM agent can produce the whole environment spec from a natural-language prompt. **Execute**: one policy across thousands of GPU-parallel environments per run, and many runs across GPUs through NVIDIA's OSMO orchestrator, with GR00T, π0/π0.5 (OpenPI), Cosmos and DreamZero policies served behind one observation-and-action contract. **Analyze**: predicate-based subtask progress, per-episode recording of every sampled *variation* (lighting, camera intrinsics, HDR background, object mass), and a **sensitivity analysis** that fits a joint posterior over those factors conditioned on success using the `sbi` library's neural posterior estimators.

The repo was created 2025-08-15, first tagged as a release branch 2025-11-25, announced as a *"pre-alpha"* at CES on 2026-01-05 with a co-published Hugging Face blog on LeRobot EnvHub integration, and is at **v0.3.0 alpha** on Isaac Lab 3.0 / Isaac Sim 6.0 as of this capture. The README's own warning is unambiguous: *"APIs are unstable and will change. Features are incomplete… Do not use this in production."* Co-developed with **[Lightwheel](../entities/lightwheel.md)**, which the README credits for *"the evaluation and task layers,"* and *"built in collaboration with the authors of [RoboLab](../entities/nvidia-robolab.md)"* — whose productization into Arena, which the wiki had on record as "stated for August 2026," is what v0.3 delivers.

## Key claims

### What it is, and what it is not
- Positioning (README): *"an open-source framework for scalable benchmark authoring and robot policy evaluation in simulation. It extends NVIDIA Isaac Lab with reusable APIs to author benchmarks, execute evaluations at scale, and analyze results for actionable feedback."* The docs' Solution section draws the boundary: *"Your benchmark defines the tasks and metrics. Isaac Lab-Arena provides the shared system."*
- Status ladder: the January blog called it *"pre-alpha… intentionally an early framework skeleton"*; the v0.3 README calls it **alpha**, *"Not an Early Access or General Availability release."* `AGENTS.md` in the same tree still says *"alpha (v0.2.x)"* — a small internal inconsistency worth knowing when an agent reads the repo.
- Licensing: README and `pyproject.toml` say **Apache-2.0**; the GitHub API reports the license as `NOASSERTION`, presumably because `LICENSE.md` carries the Isaac Sim proprietary-component notice alongside. Isaac Sim itself remains under the Omniverse licence.
- **Not pip-installable** (v0.3 Limitations): *"Installation from a published Python package is not yet supported; use the native `uv` source workflow or Docker."* The `uv` lock is for **Linux x86_64 only** (`environments = ["sys_platform == 'linux' and platform_machine == 'x86_64'"]`), Python **≥3.12, <3.13**, torch 2.11.0 on the cu128 index.

### The composition model
- Three primitives (README): *"a **scene**, which defines the physical layout and its objects, furniture, and fixtures; an **embodiment**, which defines the robot, observations, actions, sensors, and controllers; and a **task**, which defines what the robot must accomplish."* The January blog's earlier four-block phrasing (Object, Scene, Embodiment, Task) with an **Affordance** system (*Openable*, *Pressable*) is the same idea; affordances let one task scale across objects.
- **Relational placement** (v0.2 → v0.3): a *"differentiable relation-based object placement solver"* with `On`, `NextTo`, `AtPosition`, `PositionLimits`, and in v0.3 `NotNextTo`, `FaceTo`; mesh-based non-collision via Warp SDF kernels; homogeneous vs heterogeneous placement (a different object per parallel environment); pooled layouts; build-time physics settling; and a **simulation-free cuRobo IK reachability gate** that rejects layouts the robot cannot reach before any rollout runs (v0.3, for DROID and Franka).
- **Sequential task chaining** (`SequentialTaskBase`, v0.2): atomic skills — pick, walk, place, open, close, press, rotate — chained into long-horizon composites, with order-independent composite tasks and normalized progress scoring in v0.3.
- Task library on `main`: pick-and-place, open/close door, press button, rotate revolute joint (knob), lift, goal pose, place upright, sorting, assembly (peg insert, gear mesh), plus predicates for articulations, spatial relations and object settling.
- Embodiments on `main`: **Franka** (`franka_ik`, `franka_joint_pos`), **[DROID](../entities/droid.md)** (`droid_abs_joint_pos`), **GR1T2** (`gr1_pink`, `gr1_joint`) — the [Fourier GR-1](../entities/fourier-gr-1.md), **[Unitree G1](../entities/unitree-g1.md)** (`g1_wbc_pink`, whole-body controller with a navigation P-controller in Mimic; the G1 **WBC-AGILE end-to-end velocity policy** arrived in v0.2), **Galbot**, **AgiBot A2D**, **Kuka + Allegro** hand, and a `no_embodiment` sandbox. No low-cost arm (no SO-101, no LeKiwi) is registered.
- **Agentic environment generation** (v0.3, *experimental*): `EnvironmentGenerationAgent` builds a prompt from the asset catalogs (~15,000 characters), asks an OpenAI-compatible model for a JSON `ArenaEnvGraphSpec`, validates only admissibility (registered asset names, known relation kinds, prim paths present in the background's tree — 886 prims / ~30,000 characters for the Lightwheel RoboCasa kitchen) and hands the result to a review GUI. The docs are candid that *"Arena does not reason about the scene… A bad answer is rejected… but Arena cannot fix it."* SimReady asset search (`simready-search`) finds USD assets.

### Policy contract and integrations
- One method: `get_action(env, obs)` on `PolicyBase`, with a typed `PolicyCfg`; the runner generates CLI flags from the config. Built-ins: `zero_action`, `replay` (HDF5), `rsl_rl` (checkpoint + `params/agent.yaml`).
- First-party integration packages: `isaaclab_arena_gr00t` (**[GR00T](../entities/nvidia-groot.md)** remote closed-loop with pluggable *action schedulers* — chunked, synced-batch), `isaaclab_arena_openpi` (**π0 / π0.5** via `openpi-client`, DROID support), `isaaclab_arena_dreamzero` (NVIDIA GEAR's DreamZero world-model policy, remote), and **[Cosmos](../entities/nvidia-cosmos.md)** policies (v0.3 release notes; experiment configs `robolab_20_tasks_pi0_and_cosmos.yaml`, `kitchen_bench_17_tasks_pi0_and_cosmos.yaml`). Policies run as **servers** behind a websocket client (`remote_policy_base.py`, `websocket_client.py`); GR00T's Docker flavour is `./docker/run_docker.sh -g`.
- Version lineage of the GR00T integration: N1.5 (v0.1.0, *"GN1.5"*) → N1.6 (v0.2.0) → the `gr00t==0.1.0` client on `main`.
- Teleop and data generation are delegated to Isaac Lab's own scripts through an *"external environment registration callback"* (v0.3); `isaacteleop[retargeters,ui,cloudxr]==1.4.126rc1` is pinned — so **[Isaac Teleop](../entities/nvidia-isaac-teleop.md)** is a hard dependency, at a release candidate.

### Catalogs shipped in v0.3
- **17 Python-registered environments**: `kitchen_pick_and_place`, `pick_and_place_maple_table`, `galileo_pick_and_place`, `galileo_g1_locomanip_pick_and_place`, `gr1_open_microwave`, `gr1_turn_stand_mixer_knob`, `press_button`, `tabletop_sort_cubes`, `peg_insert`, `gear_mesh`, `tabletop_place_upright`, `cube_goal_pose`, `lift_object`, `dexsuite_lift`, `gr1_table_multi_object_no_collision`, `put_item_in_fridge_and_close_door`, `franka_put_and_close_door`.
- **Kitchen Benchmark: 31 DROID task specs** as environment-graph YAML across Lightwheel RoboCasa kitchens (U-shaped farmhouse, G-shaped Scandinavian, L-shaped…) and NVIDIA Replicator kitchens — open cabinet/fridge/freezer/microwave/oven, pick-and-place, press toaster button, turn oven knob. Each row shows a **π policy execution GIF**, not a success rate.
- **RoboLab catalog: 38 task YAMLs over 17 scene YAMLs**, mapped against the **120 RoboLab tasks** (whose subtask counts run 1 to 11; 53 single-subtask, 41 two-subtask, 17 three-subtask). Each Arena spec records the generating prompt, e.g. *"droid Pick up the banana and place it in the bowl. Using maple table background."* Experiment configs exist for 2, 18 and 20 RoboLab tasks with π0 and Cosmos. RoboLab's Fabio Ramos and Xuning Yang are listed contributors.
- Ecosystem benchmarks named in the README: **Lightwheel RoboFinals** (industrial), **Lightwheel RoboCasa Tasks** (*"138+ open-source tasks, 50 datasets per task, 7+ robots"*, in `LW-BenchHub`), **Lightwheel LIBERO Tasks**, **[RoboTwin 2.0](../entities/robotwin.md)** on an `IsaacLab-Arena` branch (arXiv 2603.01229), **[LeRobot](../entities/lerobot.md) Environment Hub**, and **Isaac for Healthcare RHEO** workflows. *Coming soon*: full RoboTwin and RoboDojo suites, RLWRLD DexBench, UC Berkeley, X Square, Sharpa, and NVIDIA GEAR's *G1 Factory*.

### Performance (docs `performance.rst`, *"preliminary reference measurements"*)
- Single GPU, RTX 5880 Ada (49 GB), i9-10920X, camera-free DROID cube-into-bowl with the zero-action policy, 300 vectorized steps:

| Parallel envs | Mean vectorized step | Throughput (env-steps/s) |
|---|---|---|
| 1 | 185.0 ms | 5.41 |
| 64 | 200.0 ms | 319.93 |
| 256 | 234.4 ms | 1,092.18 |
| 512 | 280.6 ms | 1,824.90 |
| 1,024 | 428.4 ms | 2,390.22 |

  The step time barely moves from 1 to 64 environments — the fixed per-step cost dominates — and throughput is still sub-linear but climbing at 1,024. The docs' own caveats: no cameras, no policy inference, an engineering workstation not a lab system, CPU wall-clock timers without CUDA sync.
- OSMO, 8 identical runs × 256 envs on NVIDIA L40s: **7.95× at 8 concurrent GPUs** (1,255 s → 158 s), mean run duration within 2 % across configurations.
- The January blog (updated 2026-02-03 with Lightwheel's numbers): **10 RoboCasa tasks × 4,096 homogeneous variations per task, GR00T N1.5, 8× RTX 6000D — parallel 0.76 h vs sequential 34.9 h, 40×** — against sequential Arena, not against the MuJoCo RoboCasa original, whose figure is not given.
- Agentic generation, model `gpt-5.6-terra` on an internal endpoint, 100 trials per environment, 100 % parseable first specs: **p50 4.9 s** (tabletop, 2 objects) to **18.1 s** (kitchen, 16 objects), with p99 tails of 25–75 s. Layout resolution on an RTX 6000 Ada grows from **2.4 s** (tabletop, 2 objects, 5 layouts) to **649 s** (kitchen, 16 objects, 1,280 layouts) — the kitchen background's collision mesh, not the LLM, is the slow part at scale.
- Model selection (5 prompts × 3 runs each): the public NVIDIA NIM default `deepseek-v4-pro-0813` passes 15/15 at **150.66 s** mean; `gpt-5.6-terra` 15/15 at 10.15 s; `claude-opus-5` 15/15 at 11.71 s with **0 validation retries**; `glm-5.2` 15/15 with 5 retries; `nemotron-3-ultra` **9/15** with 9 retries. Context length is named as *"usually the limiting factor."*

### Sensitivity analysis (docs `concept_sensitivity_analysis.rst`)
- Input is one `episode_results.jsonl` with each episode's sampled `variations` and outcome; the schema is discovered from the data. `SensitivityAnalyzer` fits **NPE** (all-continuous) or **MNPE** (mixed categorical + continuous) from `sbi` and samples the **joint posterior conditioned on success** — *"given success, which factor values were in play?"* The argument for the joint over per-factor rates: interactions (*"a matte object may succeed at low light while a shiny one needs far more"*) and confounds. This is the NPE machinery the [RoboLab methodology blog](nvidia-robolab-evaluation-blog.md) described, now productized.

### LeRobot EnvHub (HF blog, 2026-01-05, Bonghi, ben horin, S., Vadrevu, with Palma and Choghari of HF)
- `lerobot-eval --env.type=isaaclab_arena --env.hub_path=nvidia/isaaclab-arena-envs --env.environment=gr1_microwave --env.embodiment=gr1_pink --policy.path=nvidia/smolvla-arena-gr1-microwave`. The documented stack at the time was **release/0.1.1 on Isaac Sim 5.1 / Isaac Lab 2.3**, with `numpy==1.26.0` pinned by hand; a February comment on the post reports a `packaging` conflict between lerobot 0.4.4 and isaacsim-core 5.1 and *"cannot find isaaclab."* Whether EnvHub tracks v0.3 is not stated anywhere read here.

### Repo hygiene worth noting
- Ships **`AGENTS.md`, `CLAUDE.md`** and an **agent skill library** (`skills/user`: `setup-arena`, `run-experiment`, `serve-gr00t-policy`, `serve-openpi-policy`; `skills/developer`: `dev-container`, `run-tests`, `commit-and-pr`, `download-osmo-evaluation-output`) exposed to Codex and Claude Code through symlinks — the second NVIDIA repo in this wiki to do so after [Halos](halos-outside-in-safety-github.md).
- DCO sign-off required; per-clone Docker containers; CI runs all-environment smoke tests and a GR00T closed-loop end-to-end job.
- Newton: `main` is Isaac Lab 3.0 (Newton) since v0.2; September commits add *"Enable Newton support for DROID control,"* a cable asset class and a temporary gear-insertion environment; *What's Next* names *"contact-rich insertion, cables, and deformables."* A 2026-09-10 commit *"Upgrade Isaac Sim dependencies to 6.1"* means `main` is already past the README's 6.0.0 badge.

## Entities mentioned
- [Isaac Lab-Arena](../entities/isaac-lab-arena.md) — the subject.
- [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) · [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) · [Newton](../entities/newton-physics-engine.md) · [NVIDIA](../entities/nvidia.md)
- [Lightwheel](../entities/lightwheel.md) — co-developer; RoboCasa / LIBERO task suites; RoboFinals.
- [RoboLab](../entities/nvidia-robolab.md) — task catalog and methodology folded in.
- [NVIDIA GR00T](../entities/nvidia-groot.md) · [Physical Intelligence](../entities/physical-intelligence.md) (π0 / π0.5 via OpenPI) · [NVIDIA Cosmos](../entities/nvidia-cosmos.md) · [NVIDIA GEAR](../entities/nvidia-gear.md) (DreamZero, G1 Factory)
- [DROID](../entities/droid.md) · [Franka Panda](../entities/franka-panda.md) · [Fourier GR-1](../entities/fourier-gr-1.md) · [Unitree G1](../entities/unitree-g1.md) · [AgiBot](../entities/agibot.md)
- [RoboCasa](../entities/robocasa.md) · [LIBERO](../entities/libero.md) · [RoboTwin 2.0](../entities/robotwin.md)
- [LeRobot](../entities/lerobot.md) · [Hugging Face](../entities/hugging-face.md) · [NVIDIA Isaac Teleop](../entities/nvidia-isaac-teleop.md) · [CuRobo](../entities/curobo.md)

## Concepts touched
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — Arena is the infrastructure pole of that page: rollouts at scale, variations, and the NPE sensitivity analysis.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — the framework evaluates in sim only; *"sim-to-real validated evaluation methods"* is listed as a contribution area, i.e. not yet supplied.
- [VLA models](../concepts/learning/vla-models.md) — the policies under test.
- Domain randomization (see [sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md)) — "variations" are controlled, recorded randomization used for diagnosis rather than training.

## Open questions
- **No success rates anywhere in the docs.** The kitchen and RoboLab catalogs show GIFs of π executions; the performance page benchmarks a zero-action policy. What GR00T N1.6/N1.7, π0.5 and Cosmos actually score on Arena's 31 kitchen tasks is presumably in the ecosystem partners' hands.
- **Sim-to-real correlation of Arena scores is unmeasured** (or unpublished). The RoboLab paper is the nearest evidence, and it is a different task set.
- **Platform reach**: Linux x86_64 only in the `uv` lock; [DGX Spark](../entities/dgx-spark.md) is aarch64, so native install is out and Docker is untested here; Jetson is out by the RT-core rule. Arena is a workstation/data-centre tool.
- **Does EnvHub track v0.3?** The only documented EnvHub recipe pins release/0.1.1.
- **Low-cost embodiments**: nothing below a Franka is registered. Adding an [SO-101](../entities/so-arm101.md) embodiment through the *Arena in Your Repository* path is the obvious experiment for the wiki's own hardware.
- **Lightwheel's role and business model** — a first entity page now exists, but from Arena's side only.
