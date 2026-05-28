---
title: "LeRobot: An Open-Source Library for End-to-End Robot Learning (Cadene et al., ICLR 2026)"
type: source
url: https://arxiv.org/abs/2602.22818
arxiv: https://arxiv.org/abs/2602.22818
local_path: raw/2602.22818v1.pdf
venue: ICLR 2026 (conference paper)
author: Remi Cadene, Simon Aliberts, Francesco Capuano, Michel Aractingi, Adil Zouitine, Pepijn Kooijmans, Jade Choghari, Martino Russi, Caroline Pascal, Steven Palma, Mustafa Shukor, Jess Moss, Alexander Soare, Dana Aubakirova, Quentin Lhoest, Quentin Gallouédec, Thomas Wolf
affiliations: Hugging Face (17 authors; Capuano now at University of Oxford, work done while at HF)
published: 2026-02-26 (arxiv v1)
ingested: 2026-05-28
tags: [lerobot, hugging-face, iclr-2026, framework, dataset-format, async-inference, so-100, so-101, aloha, koch, lekiwi, hope-jr-arm, stretch-3, reachy-2, act, diffusion-policy, vq-bet, td-mpc, hil-serl, pi0, smolvla, libero, metaworld]
---

## Summary

The **canonical ICLR 2026 paper** for [LeRobot](../entities/lerobot.md) — an open-source library by [Hugging Face](../entities/hugging-face.md) that vertically integrates the **entire robot learning stack**: low-level motor middleware, large-scale data collection / storage / streaming, optimized inference, and PyTorch implementations of SOTA robot learning algorithms. The paper formalizes what was previously known only through the repo, the [team-authored tutorial](lerobot-robot-learning-tutorial.md), and downstream sources ([SmolVLA paper](smolvla-paper.md), [π0 paper](pi-zero-paper.md), [LeKiwi GitHub](lekiwi-github.md), etc.). 17-author Hugging Face core team; lead author **[Remi Cadene](../entities/remi-cadene.md)**.

The thesis: robot learning is bottlenecked by **fragmentation** (per-platform middleware, incompatible dataset formats, irreproducible algorithm implementations), not by ML capability. LeRobot's contribution is a single vertically-integrated stack that lowers the barrier to entry for accessible, real-world, learning-based robotics.

## Key claims

### Four pillars (§3)

1. **Unified robot integration** — Python-based middleware API for real-world motor control across diverse platforms; bridges ML frameworks (PyTorch) and real-world robotics; supports low-end manipulators through humanoid arms.
2. **Standardized datasets** (`LeRobotDataset`) — efficient multimodal format for high-frame-rate sensorimotor + image data; self-contained schema (text descriptions for language conditioning, robot embodiment, FPS, sensor types); native streaming via `StreamingLeRobotDataset`.
3. **Optimized inference** — decouples action prediction from action execution **both physically** (inference on remote machine connected over network) **and logically** (asynchronous producer-consumer; predict next action chunk while current one is executing).
4. **Efficient, reusable algorithms** — pure-PyTorch reference implementations; train from scratch in **<100 LoC**; serve in **<40 LoC**.

### Supported real-world robot platforms (Table 1a, §3.1)

| Robot | Type | Cost (single / bimanual €) |
|---|---|---|
| [SO-100 / SO-101](../entities/so-arm101.md) | Manipulator | ~225 (550) |
| Koch-v1.1 | Manipulator | ~670 (1346) |
| [ALOHA-2](../entities/aloha.md) | Bimanual manipulator | ~21k |
| HopeJR-Arm | Humanoid arm + hand | ~500 |
| [LeKiwi](../entities/lekiwi.md) | Mobile manipulator | ~230 |
| [Stretch-3](../entities/stretch.md) | Mobile manipulator | (Hello Robot; not in cost table) |
| [Reachy-2](../entities/reachy.md) | Humanoid | (Pollen Robotics; not in cost table) |

> The paper notes LeRobot **went from 3 manipulation setups (Koch-v1.1, SO-100, ALOHA) at the start of 2025 to 8 platforms (regular, humanoid, and mobile) by paper submission** — and flags maintaining that rate as paramount.

BOM links for each platform are in Appendix A. Middleware is built on the low-level SDKs of major low-cost actuator producers (**FeeTech, Dynamixel**) and is designed to be "easily extensible and highly composable."

### Dataset ecosystem (Table 1b + Figure 5, §3.2)

As of **September 2025**:

- **16K+ openly-shared datasets** from **2.2K+ individual contributors** using the `LeRobotDataset` format.
- Top robots by HF Hub downloads: **Franka Panda (1.88 M), xArm (1.11 M), WidowX (832K), KUKA (663K), SO-101 (320K), SO-100 (279K), Koch-v1.1 (44K)**.
- **SO-10X dominates community-contributed datasets** — 50%+ of contributed datasets are on SO-100/101, despite Panda dominating downloads (Panda is the platform of large centralized academic releases like [Open X-Embodiment](../entities/open-x-embodiment.md) and [DROID](../entities/droid.md)).
- Largest centralized download targets are the academic benchmark releases ([Collaboration et al., 2025 = OXE](../entities/open-x-embodiment.md); [Khazatsky et al., 2025 = DROID](../entities/droid.md)).

> [!note] Interpretation
> The paper frames this split as **centralized vs decentralized data collection**: Panda/xArm/WidowX/KUKA are the centralized academic-rig story; SO-10X is the decentralized community story powered by hardware accessibility and `LeRobotDataset` format. The argument is that the *coexistence* validates the format's flexibility.

### `LeRobotDataset` format (§3.2 + Appendix C)

- Tabular records (`.parquet`) + compressed videos (`.mp4`) + lightweight metadata.
- Streaming variant `StreamingLeRobotDataset` uses an `IterableDataset` interface and `torchcodec` for on-the-fly video decoding — bounded memory regardless of dataset size.
- Figure 10 shows streaming timing comparable to pre-loaded in the steady-state regime (after init).
- API supports `delta_timestamps={"observation.images.wrist_camera": [-0.2, -0.1, 0.0]}` for retrieving multi-step history per frame.

### Supported algorithms (§3.3, Figure 6)

| Paradigm | Models |
|---|---|
| **RL** | [HIL-SERL](../entities/hcrlab.md) (Luo et al. 2024), [TD-MPC](../entities/td-mpc.md) (Hansen et al. 2022) |
| **Single-task BC** | [ACT](../entities/act.md) (Zhao et al. 2023), [Diffusion Policy](../entities/diffusion-policy.md) (Chi et al. 2024), [VQ-BET](../entities/vq-bet.md) (Lee et al. 2024) |
| **Multi-task VLA** | [π0](../entities/pi-zero.md) (Black et al. 2024), [SmolVLA](../entities/smolvla.md) (Shukor et al. 2025) |

> ACT is the most popular: dominates uploads (Figure 7a) and consistently top in downloads (Figure 7d). The paper attributes this to (1) small size + fast inference and (2) usability with as few as **50 real-world trajectories**.

### Compute footprint benchmarks (Tables 2 + 3, §3.3)

Run in full **fp32**; diffusion / flow models use 10 denoising steps; 5s hard timeout.

**Peak memory (Table 2):**

| Model | # Params | CPU | MPS | RTX 4090 | A100 |
|---|---|---|---|---|---|
| ACT | 52 M | 817 MB | 462 MB | 211 MB | 211 MB |
| Diffusion Policy | 263 M | 1.22 GB | 224 MB | 1.12 GB | 1.12 GB |
| π0 | 3.5 B | 4.13 GB | 97 MB | 13.32 GB | 13.32 GB |
| SmolVLA | 450 M | 1.69 GB | 555 MB | 1.75 GB | 1.75 GB |

**Avg inference latency over 100 forward passes (Table 3):**

| Model | CPU (ms) | MPS (ms) | RTX 4090 (ms) | A100 (ms) |
|---|---|---|---|---|
| ACT | 182.3 ± 40.8 | 42.7 ± 10.1 | 5.0 ± 0.06 | 13.8 ± 0.45 |
| Diffusion Policy | 3453.8 ± 39.3 (100% timeout) | 1369.8 ± 0.19 | 69.8 ± 0.19 | 613.9 ± 10.2 |
| π0 | (100% timeout) | (100% timeout) | 209.4 ± 2.8 | 569.0 ± 2.9 |
| SmolVLA | 2028.5 ± 302.6 (2% timeout) | 721.8 ± 57.7 | 99.2 ± 1.2 | 278.8 ± 1.9 |

> [!note] Operational implications
> - **π0 fails to complete inference within 5 s on CPU and MPS** — confirms the "frontier VLA needs a GPU" reality. SmolVLA runs even on CPU.
> - ACT achieves **~100–200 Hz** on RTX 4090 / A100 — fits comfortably above the typical 30 Hz control rate.
> - Diffusion Policy CPU latency is the worst on the chart (3.4s), all timing out — incompatible with onboard deployment without GPU.

### Async inference results (Table 5, Appendix E)

Tested on **SmolVLA + SO-100 arm** on three real-world tasks: pick-place, stacking, sorting (10 episodes × 60s each).

| | Success rate avg | Total time (s) | Avg time (s) | # Cubes (60s) |
|---|---|---|---|---|
| **Sync** | 78.3% | 137.5 | 13.75 ± 2.42 | 1.8 ± 0.45 |
| **Async** | 73.3% | 97.0 | 9.70 ± 2.95 | **3.8 ± 1.3** |

> Async preserves comparable success (drops only on the hardest task, sorting) while **doubling effective throughput** in fixed-time evaluation (1.8 → 3.8 cubes). The speedup comes from **logical decoupling alone** — both server and client run on the same machine in this benchmark.

### Inference stack architecture (§3.4 + Figure 8)

- **Action chunks** `a_{t:t+H-1}` are the primitive (per [ACT](../entities/act.md), Zhao et al. 2023).
- **Physical decoupling** — inference on remote machine, control loop on robot. Network in between.
- **Logical decoupling** — async producer-consumer; predict next chunk *while* current one is executing.
- Overlapping chunks merged via a **user-defined aggregation function f** — flexible per-use-case (e.g., temporal ensembling, latest-wins, weighted average).
- Goal: **non-empty action queue at all times** to prevent robot idleness.

### Simulation (§4)

> "The core focus of `lerobot` is to lower the barrier to entry to enable real-world robotics applications" — simulation is **for evaluation, not training**.

Native integration with two benchmarks:

- **[LIBERO](../entities/libero.md)** — Liu et al. 2023. Four fixed task suites (SPATIAL, OBJECT, GOAL, plus continuing-task LIBERO-90 and long-horizon LIBERO-LONG). Used as the de-facto VLA-eval bench by π0, SmolVLA.
- **[Meta-World](../entities/metaworld.md)** — Yu et al. 2020. 50 manipulation tasks; MT10/MT50 for multi-task, ML1/ML10/ML45 for meta-learning. Shared robot setup across all tasks → common interface for skill transfer.

### Limitations (§5)

The paper is explicit:

1. **Robot coverage is non-exhaustive** — 8 platforms is "practical but incomplete." Need to keep adding embodiments at a similar rate to 2025's 3→8 expansion.
2. **Algorithm coverage is non-exhaustive** — strong reproducible implementations across paradigms, but adding more is future work.
3. **Inference performance lacks low-level optimization** — no quantization, no graph compilation. The current numbers leave headroom.

## Code examples (from appendices, ≤40 LoC each)

- **Teleop** (Appendix B): `SO100Leader()` + `SO100Follower()` + `teleop.get_action()` → `robot.send_action(action)`.
- **Load streaming dataset** (Appendix C.3): `StreamingLeRobotDataset("lerobot/svla_so101_pickplace", delta_timestamps=...)`.
- **Train Diffusion Policy on PushT** (Appendix D.1): ~80 LoC including DataLoader and checkpoint save.
- **Use pretrained SmolVLA** (Appendix D.2): `SmolVLAConfig() → SmolVLAPolicy(cfg) → policy.select_action(...)` then `robot.send_action(...)`.
- **Remote policy server + robot client** (Appendix E.1, E.2): `PolicyServerConfig(host, port) → serve(config)` + client uses `RobotClientConfig(server_address, policy_type="pi0", pretrained_name_or_path="lerobot/pi0")`.

## Entities mentioned

- [LeRobot](../entities/lerobot.md) — the framework itself.
- [Hugging Face](../entities/hugging-face.md) — maintainer; 17 authors core team.
- [Remi Cadene](../entities/remi-cadene.md) — lead author + LeRobot tech lead.
- Hardware: [SO-ARM101](../entities/so-arm101.md), [ALOHA / ALOHA-2](../entities/aloha.md), [LeKiwi](../entities/lekiwi.md), [Stretch](../entities/stretch.md), [Reachy](../entities/reachy.md), [HopeJR Arm](../entities/hope-jr-arm.md), [The Robot Studio](../entities/the-robot-studio.md), [SIGRobotics UIUC](../entities/sigrobotics-uiuc.md), [Hello Robot](../entities/hello-robot.md), [Pollen Robotics](../entities/pollen-robotics.md).
- Algorithms: [ACT](../entities/act.md), [Diffusion Policy](../entities/diffusion-policy.md), [VQ-BET](../entities/vq-bet.md), [TD-MPC](../entities/td-mpc.md), [π0](../entities/pi-zero.md), [SmolVLA](../entities/smolvla.md), [BET](../entities/bet.md).
- Datasets: [DROID](../entities/droid.md), [Open X-Embodiment](../entities/open-x-embodiment.md), [Franka Panda](../entities/franka-panda.md), [xArm-7](../entities/xarm-7.md).
- Sims: [LIBERO](../entities/libero.md), [Metaworld](../entities/metaworld.md), [MuJoCo](../entities/mujoco.md), [PushT](../entities/pusht.md).
- Other VLAs cited but not LeRobot-integrated: [GR00T N1](../entities/nvidia-groot.md) (Bjorck et al. 2025), Gello teleop (Wu et al. 2024).

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md)
- [VLA models](../concepts/learning/vla-models.md)
- [Flow matching](../concepts/learning/flow-matching.md) (cited as π0 / SmolVLA action expert)
- Action chunking + async inference (currently no dedicated concept page; see this source and [SmolVLA paper](smolvla-paper.md))

## Cross-source relationships

- **Supersedes** [LeRobot robot-learning tutorial](lerobot-robot-learning-tutorial.md) as the **canonical academic reference** for the library — the tutorial remains the recommended onboarding read, but the ICLR paper is now what should be cited.
- **Confirms** the SO-10X dominance pattern visible in the [LeRobot Worldwide Hackathon 2025 winners](lerobot-worldwide-hackathon-2025-winners.md): community contribution flows to the cheapest hardware.
- **Validates** the [SmolVLA paper](smolvla-paper.md)'s async-inference contribution by reproducing the speedup numbers in a controlled setting (Table 5).

## Open questions

- **Quantization / graph compilation roadmap.** Limitation #3 explicitly flags this as future work — when does π0 become deployable on consumer hardware?
- **Per-platform support depth.** The 8 platforms are listed equally, but some (SO-100, ALOHA) are mature; others (Reachy-2, Stretch-3) are newer integrations. What is full vs partial support?
- **Tabletop bimanual cost gap.** ALOHA-2 (€21k) is **~40×** the cost of SO-100 bimanual (€550). Is there a planned middle-tier platform, or does HopeJR-Arm fill that gap?
- **Algorithm gap: no world-model methods.** TD-MPC is the only model-based / world-model entry; no [DreamerV3](../entities/dreamer.md), no [V-JEPA-2](../entities/v-jepa-2.md). Is this a coverage roadmap question or a deliberate scope decision?

## Cited references appearing in the paper

Key references for cross-linking: Aldaco et al. 2024 (ALOHA-2), Ball et al. 2023 (RLPD), Bekris et al. 2024 (explicit vs implicit models), Bjorck et al. 2025 ([GR00T N1](../entities/nvidia-groot.md)), Black et al. 2024 ([π0](../entities/pi-zero.md)), Brohan et al. 2023 (RT-2), Chi et al. 2024 ([Diffusion Policy](../entities/diffusion-policy.md)), Collaboration et al. 2025 ([Open X-Embodiment](../entities/open-x-embodiment.md)), Florence et al. 2022 (IBC), Haarnoja et al. 2018 (SAC), Hansen et al. 2022 ([TD-MPC](../entities/td-mpc.md)), Henderson et al. 2018 (RL reproducibility), Ho et al. 2020 (DDPM), Jang et al. 2022 (BC-Z), Khazatsky et al. 2025 ([DROID](../entities/droid.md)), Kingma & Welling 2022 (VAE), Knight et al. 2024 (SO-10X), Kober et al. 2013 (RL in robotics survey), Lee et al. 2024 ([VQ-BET](../entities/vq-bet.md)), Lipman et al. 2023 ([Flow Matching](../concepts/learning/flow-matching.md)), Liu et al. 2023 ([LIBERO](../entities/libero.md)), Luo et al. 2024 (HIL-SERL), Luo et al. 2025 (SERL), Mick et al. 2019 ([Reachy](../entities/reachy.md)), Mnih et al. 2013 (DQN), Pomerleau 1988 (ALVINN), Shukor et al. 2025 ([SmolVLA](smolvla-paper.md)), Siciliano & Khatib 2016 (Springer Handbook of Robotics), Sutton & Barto 2018 (RL textbook), Yu et al. 2020 ([Metaworld](../entities/metaworld.md)), Zhao et al. 2023 ([ACT / ALOHA](../entities/act.md)).
