---
title: LeRobot
type: entity
subtype: software-framework
created: 2026-05-10
updated: 2026-07-04
sources: 17
tags: [lerobot, imitation-learning, hugging-face, framework, open-source, act, mobile-manipulator, smolvla, pi0, tutorial, iclr-2026]
---

**LeRobot** — open-source **end-to-end robot learning library** maintained by [Hugging Face](hugging-face.md). Provides a vertically-integrated stack: unified Python middleware for low-level motor control, the `LeRobotDataset` format for multimodal high-frame-rate data, an optimized async inference stack (physical + logical decoupling), and reference PyTorch implementations of SOTA robot-learning algorithms across RL (HIL-SERL, TD-MPC), single-task BC (ACT, Diffusion Policy, VQ-BET), and multi-task VLAs (π0, SmolVLA). De-facto OSS stack for the affordable mobile-manipulator class (SO-ARM100/101, LeKiwi, XLeRobot, Koch v1.1) bringing "buy → assemble → teleop → train → deploy" within reach of sub-$1k hobbyist hardware.

Repository: [github.com/huggingface/lerobot](https://github.com/huggingface/lerobot). **Canonical academic reference:** [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) (Cadene, Aliberts, Capuano, …, Wolf — 17 HF authors).

## Why it matters in this wiki

LeRobot is the **dominant open-source IL framework for the affordable mobile-manipulator class** — directly relevant to the wiki's assistive-robotics, accessible-robotics, and household-manipulation themes. It complements the wiki's existing IL coverage:

- **[Diffusion Policy](diffusion-policy.md)** — research code, often run on Franka/UR5e platforms costing $20k+.
- **[Stretch AI](stretch-ai.md)** — Hello Robot's stack targeted at the $20k Stretch platform.
- **LeRobot** — broader and lower-cost; supports SO-ARM101, LeKiwi, and downstream compositions like XLeRobot at ~$600–$1,000.

LeRobot also distributes **two reference VLA checkpoints** directly:

- **[`lerobot/pi0_base`](pi-zero.md)** — Physical Intelligence's [π0](pi-zero.md) (3.3 B params; PaliGemma + flow-matching action expert).
- **[`lerobot/smolvla_base`](smolvla.md)** — Hugging Face LeRobot team's [SmolVLA](smolvla.md) (450 M params; SmolVLM-2 + flow-matching action expert with interleaved CA + causal SA + async-inference stack). **SmolVLA beats π0-3.5 B by +16.6 pts on real-world SO-100 multi-task** despite ~7× fewer params.

The canonical 7-step LeRobot workflow (install → motor config → calibration → teleop → data collection → train → evaluate) is repeated across nearly every LeRobot-compatible hardware tutorial. **ACT (Action Chunking with Transformers)** is the default reference policy class, though Diffusion Policy and others are supported.

## Composition stack examples in this wiki

| Platform | Base | Arm | Cost | Source |
|---|---|---|---|---|
| [LeKiwi](lekiwi.md) | LeKiwi 3-wheel Kiwi-drive | SO-ARM101 (optional) | sub-$1k | [LeKiwi GitHub](../sources/lekiwi-github.md), [Seeed tutorial](../sources/seeed-lekiwi-wiki.md) |
| [XLeRobot](xlerobot.md) | LeKiwi-class wheeled base | 2× SO-ARM101 | ~$660 | [XLeRobot docs](../sources/xlerobot-docs.md) |

## Key facts

- Maintained by [Hugging Face](hugging-face.md); robotics lead [Remi Cadene](remi-cadene.md).
- Apache 2.0.
- Active development; framework moves quickly enough that distributor tutorials (e.g., [Seeed Studio LeKiwi wiki](../sources/seeed-lekiwi-wiki.md)) carry "consult upstream for latest features" caveats.
- Compatible hardware ecosystem: SO-ARM100/101 (The Robot Studio, [FeeTech](feetech.md)), Koch v1.1 ([Dynamixel](dynamixel.md)), LeKiwi (SIGRobotics-UIUC), XLeRobot (Vector Wang), Bambot, others.
- Native motor SDK support: **[FeeTech](feetech.md) + [Dynamixel](dynamixel.md) only** ([ICLR 2026 paper §3.1](../sources/lerobot-iclr-2026-paper.md)). Other motor lineages (e.g. Hiwonder HX-12H on [ROSOrin Pro](rosorin-pro.md)) require a bridge layer like [Rosetta](rosetta.md).

### Officially-supported real-world platforms (ICLR 2026 paper, Table 1a)

| Robot | Type | Cost (single / bimanual) |
|---|---|---|
| [SO-100/101](so-arm101.md) | Manipulator | ~€225 / €550 |
| Koch-v1.1 | Manipulator | ~€670 / €1346 |
| [ALOHA-2](aloha.md) | Bimanual manipulator | ~€21k |
| [HopeJR-Arm](hope-jr-arm.md) | Humanoid arm + hand | ~€500 |
| [LeKiwi](lekiwi.md) | Mobile manipulator | ~€230 |
| [Stretch-3](stretch.md) | Mobile manipulator | (Hello Robot) |
| [Reachy-2](reachy.md) | Humanoid | (Pollen Robotics) |

Went from **3 manipulation setups (Koch-v1.1, SO-100, ALOHA) at start of 2025 → 8 platforms (regular, humanoid, mobile)** by paper submission (Feb 2026). Middleware integrates directly with FeeTech and Dynamixel low-level SDKs.

### Supported algorithms (ICLR 2026 paper, §3.3)

| Paradigm | Implementations |
|---|---|
| RL | [HIL-SERL](hcrlab.md), [TD-MPC](td-mpc.md) |
| Single-task BC | [ACT](act.md), [Diffusion Policy](diffusion-policy.md), [VQ-BET](vq-bet.md) |
| Multi-task VLA | [π0](pi-zero.md), [SmolVLA](smolvla.md) |

ACT dominates uploads + downloads — paper attributes this to small size + usability with as few as **50 real-world trajectories**.

### `LeRobotDataset` format

`.parquet` tabular records + `.mp4` compressed videos + lightweight metadata. **Streaming variant `StreamingLeRobotDataset`** uses `IterableDataset` + `torchcodec` for on-the-fly video decode — bounded memory regardless of dataset size, comparable timing to pre-loaded in the steady-state. **16K+ openly-shared datasets from 2.2K+ contributors as of Sep 2025** ([ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md)).

### Optimized inference stack

Decouples **action prediction** from **action execution** at two levels:

- **Physical decoupling** — inference on remote machine over network; control loop runs onboard.
- **Logical decoupling** — async producer-consumer; predict next action chunk while current chunk is executing. Overlapping chunks merged via user-defined aggregation `f`.

Benchmark on **SmolVLA + SO-100** across 3 real-world tasks (Table 5, 60s episodes): async preserves comparable success (78.3% → 73.3%, drop only on sorting) while **doubling throughput** in fixed time (1.8 → 3.8 cubes). See [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) Appendix E.

### Native simulation integration

- **[LIBERO](libero.md)** — 4 task suites (SPATIAL, OBJECT, GOAL, LONG/90); the de-facto VLA-eval bench.
- **[Metaworld](metaworld.md)** — 50 manipulation tasks; MT10/MT50 for multi-task, ML1/ML10/ML45 for meta-learning.

Simulation is used **for evaluation, not training** — the library philosophy is to train on real-world data ([ICLR 2026 paper, §4](../sources/lerobot-iclr-2026-paper.md)).

### Compute footprint (ICLR 2026 paper, Tables 2 + 3, fp32)

| Model | # Params | Peak mem (A100) | Avg latency RTX 4090 | A100 |
|---|---|---|---|---|
| ACT | 52 M | 211 MB | **5.0 ms** | 13.8 ms |
| Diffusion Policy | 263 M | 1.12 GB | 69.8 ms | 613.9 ms |
| π0 | 3.5 B | 13.32 GB | 209.4 ms | 569.0 ms |
| SmolVLA | 450 M | 1.75 GB | 99.2 ms | 278.8 ms |

ACT runs **~100–200 Hz** on high-end GPUs. **π0 fails to complete inference within 5 s on CPU and MPS** — confirms frontier VLAs need a GPU; SmolVLA runs even on CPU.

## Ecosystem scale (June 2025 snapshot)

The [LeRobot Worldwide Hackathon 2025](lerobot-worldwide-hackathon-2025.md) (June 14–15, 2025) is the clearest community-scale signal for the framework: **916 registered team members, ~400 submissions, 30 ranked winners, 189 hackathon datasets, 12 hackathon models** ([all-winners HF Space](../sources/lerobot-worldwide-hackathon-2025-winners.md)). The `submissions` dataset alone has 11.3k downloads.

## Official pedagogical reference

**["Robot Learning: A Tutorial"](../sources/lerobot-robot-learning-tutorial.md)** (Capuano, Pascal, Zouitine, Wolf, Aractingi — Oct 14, 2025; arXiv 2510.12403 + HF Space at https://huggingface.co/spaces/lerobot/robot-learning-tutorial) is the **team-authored canonical tutorial** for the framework — a chapter arc from Classical Robotics through RL and IL to Generalist (VLA) policies, with runnable `lerobot` code examples (ACT, Diffusion Policy, async inference, [π₀](physical-intelligence.md), SmolVLA). 410 likes on the Space at ingest time. This is the recommended single-source onboarding for the framework, complementary to the wiki's own [bottom-up curriculum](../syntheses/curriculum/robot-learning-curriculum.md).

## Downstream / hardware-ecosystem projects

- **[Grievous](grievous.md)** ([source](../sources/grievous-github.md)) — Alex Koven's in-progress "cheap, human-like, fully-autonomous testbed" registered as `lerobot.robots.grievous.grievous_host`. Design ancestors: [Mobile ALOHA](aloha.md) + [XLeRobot](xlerobot.md).

### Running LeRobot on Jetson (containerized)

NVIDIA's **[Jetson AI Lab LeRobot tutorial](../sources/nvidia-jetson-ai-lab-lerobot.md)** (now archived) packages LeRobot as the **`dustynv/lerobot`** Docker image, deployed via the **[jetson-containers](jetson-containers.md)** framework + `autotag`, to run the full teleop → record → train ([ACT](act.md)) → eval loop **onboard a Jetson** (AGX Orin / Orin NX 16 GB / [Orin Nano 8 GB](jetson-orin-nano.md)). Bundles JupyterLab + Rerun.io + PulseAudio-TTS; uses **Koch v1.1** as the reference robot. It is NVIDIA's containerized "get LeRobot running on edge silicon" recipe — distinct from the ROS 2 bridges below (which adapt LeRobot to ROS 2 robots) and from [Cutting the Cord](../sources/cutting-the-cord-untethered-xlerobot.md) (which measures policy latency on a self-built onboard stack). **Caveat:** the tutorial is deprecated and pins the pre-refactor LeRobot CLI (`control_robot.py` / Hydra `train.py`) + JetPack 6 GA/6.1, not the current `lerobot-record`/`lerobot-train` entry points.

### LeRobot ↔ [ROS 2](ros2.md) bridges (3 independent projects)

| Project | Approach | Hardware | ROS 2 distro | Stars (May 2026) | License |
|---|---|---|---|---|---|
| **[Rosetta](rosetta.md)** ([source](../sources/rosetta-github.md)) | YAML contract | any ROS 2 robot | distro-agnostic | 76 | Apache-2.0 |
| **[lerobot-ros](lerobot-ros.md)** ([source](../sources/lerobot-ros-github.md)) | Python sub-class | any ros2_control / MoveIt arm | **Jazzy only** | **194** | not specified |
| **[so101-ros2](so101-ros2.md)** ([source](../sources/so101-ros2-readthedocs.md)) | SO-101 workspace | **SO-101 only** | **Humble only** | 50 | MIT |

Choice depends on (1) robot type — mobile bases need Rosetta; (2) ROS 2 distribution — Humble vs Jazzy is operationally load-bearing. All three address LeRobot's [ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) Limitation #2 (algorithm coverage non-exhaustive) by adding integrations the upstream lacks.

## Related

- [Hugging Face](hugging-face.md) — maintainer
- [SO-ARM101](so-arm101.md) — arm platform
- [LeKiwi](lekiwi.md) — mobile base
- [XLeRobot](xlerobot.md) — dual-arm composition
- [Imitation learning](../concepts/learning/imitation-learning.md)
- [Diffusion Policy](diffusion-policy.md) — alternative IL approach
- [Stretch AI](stretch-ai.md) — counterpart IL/agent stack on Stretch

## Mentioned in

- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — **canonical academic reference**; Cadene, Aliberts, Capuano, …, Wolf; 17 HF authors.
- [GR00T N1 Paper](../sources/groot-n1-paper.md) — NVIDIA **extends the `LeRobotDataset` format** (`modality.json`, fine-grained state/action semantics, explicit rotation representations) for GR00T's cross-embodiment training corpus.
- [Isaac-GR00T GitHub](../sources/isaac-gr00t-github.md) — the GR00T codebase consumes "a flavor of the **LeRobot v2** dataset format" + `meta/modality.json`; the concrete fine-tuning data path for all GR00T versions.
- [NVIDIA Jetson AI Lab — HuggingFace LeRobot (archived)](../sources/nvidia-jetson-ai-lab-lerobot.md) — `dustynv/lerobot` containerized Jetson recipe (Koch v1.1 + ACT).
- [Rosetta GitHub](../sources/rosetta-github.md) — downstream ROS 2 bridge (YAML-contract).
- [lerobot-ros GitHub](../sources/lerobot-ros-github.md) — downstream ROS 2 bridge (Python sub-class, Jazzy).
- [so101_ros2 readthedocs](../sources/so101-ros2-readthedocs.md) — downstream ROS 2 bridge (SO-101-specific, Humble + Isaac Sim).
- [SmolVLA Paper](../sources/smolvla-paper.md) — team-authored VLA built on LeRobot framework.
- [π0 Paper](../sources/pi-zero-paper.md) — Physical Intelligence's VLA; distributed via LeRobot.
- [Robot Learning: A Tutorial (LeRobot)](../sources/lerobot-robot-learning-tutorial.md) — official team-authored tutorial.
- [Grievous GitHub](../sources/grievous-github.md) — downstream hardware project built on LeRobot.
- [XLeRobot Documentation](../sources/xlerobot-docs.md)
- [Seeed Studio LeRobot LeKiwi Wiki](../sources/seeed-lekiwi-wiki.md)
- [LeKiwi GitHub](../sources/lekiwi-github.md)
- [LeRobot Worldwide Hackathon 2025 — All Winners](../sources/lerobot-worldwide-hackathon-2025-winners.md)

## Open questions / TBD

- Stable release cadence — distributor tutorials note framework volatility, but the upstream release history is not yet ingested.
- Performance comparison: ACT (LeRobot default) vs. [Diffusion Policy](diffusion-policy.md) / [VQ-BeT](vq-bet.md) / [BET](bet.md) on the same low-cost hardware. No head-to-head numbers in ingested sources.
- Relationship to [Stretch AI](stretch-ai.md) — both are LLM/IL-adjacent open robot stacks. Any cross-pollination?
- **Quantization / graph compilation roadmap** — ICLR 2026 paper Limitation #3; current numbers leave headroom for π0 onboard deployment.
- **No world-model algorithms supported** ([Dreamer](dreamer.md), [V-JEPA-2](v-jepa-2.md)) — coverage roadmap question or deliberate scope decision?
