---
title: "A Sim-to-Real VLA Pipeline with Seeed reBot Arm and NVIDIA Isaac (DLI course)"
type: source
url: https://www.seeedstudio.com/sim-to-real-with-seeed-rebot-and-nvidia-isaac
author: Seeed Studio with NVIDIA (course content by Youjiang Yu et al.)
published: 2026-08-19
ingested: 2026-08-27
venue: NVIDIA Deep Learning Institute series (hosted by Seeed Studio)
format: online course, 19 modules / 5 chapters
tags: [seeed-studio, rebot-arm, b601-rs, b601-dm, nvidia-dli, sim-to-real, lerobot, isaac-sim, cosmos, cosmos3-nano, groot, gr00t-1-7, tensorrt, jetson-thor, agx-orin, jetpack-7, vla, data-augmentation, teleoperation, course]
---

# A Sim-to-Real VLA Pipeline with Seeed reBot Arm and NVIDIA Isaac

> [!note] Provenance
> The Seeed URL is a Magento shell whose body is an **iframe** to `https://279070161-sketch.github.io/dli-course`, whose own body is rendered client-side from **`js/course-data.js`**. `WebFetch` on the Seeed URL returns nav chrome and nothing else. The 19 module bodies transcribed here were parsed out of that JS payload (`window.COURSE_DATA`), which is the course's primary text. Timestamps inside the logs run **2026-05-28 → 2026-08-19**; the latest is used as `published`.

## Summary

A free, hands-on **19-module / 5-chapter** curriculum, co-developed by [Seeed Studio](../entities/seeed-studio.md) and NVIDIA under the **Deep Learning Institute** banner, that walks a single manipulation task — *"organize stationery,"* a tabletop pick-and-place — end to end through the entire 2026 physical-AI stack: **teleoperated data collection in [LeRobot](../entities/lerobot.md) → optional parallel collection inside [Isaac Sim](../entities/nvidia-isaac-sim.md) → generative scene augmentation with [Cosmos3-Nano](../entities/nvidia-cosmos.md) Transfer → fine-tuning [GR00T 1.7](../entities/nvidia-groot.md) → seven-engine TensorRT export and on-robot inference on [Jetson AGX Thor / AGX Orin](../entities/jetson-thor.md)**. Self-described as ~20 learning hours, intermediate level. The hardware is the **[reBot Arm B601-RS](../entities/rebot-arm-b601.md)** follower plus a **[Star Arm 102](../entities/star-arm-102.md)** leader.

Its wiki value is not the pedagogy — it is that this is the **first fully specified, command-level, reproducible end-to-end Cosmos-augmented-GR00T-to-Jetson pipeline** the wiki has ingested. Every prior source covered one link of that chain. It is also unusually candid about where the pipeline is still bad.

## Chapter map

| Ch. | Modules | Content |
|---|---|---|
| 1. Overview | 1.1–1.5 | Course framing, LeRobot background, what sim-to-real is, reBot B601-RS spec sheet |
| 2. Build Your Robot Lab | 2.0–2.2 | Assembly, motor-ID reset, LeRobot calibration, teleop verification, the "Lightbox" workspace |
| 3. Get Your Own VLA Model | 3.1–3.5 | Real data collection, Isaac Sim data collection, **Cosmos3 Transfer augmentation**, GR00T 1.7 fine-tune, real-environment evaluation |
| 4. Deploy on Jetson | 4.1–4.5 | JetPack 7.2 flashing, robot wiring + USB-CAN, GR00T runtime, dataset/model asset prep, **seven-engine TensorRT inference** |
| 5. Reference | 5.1 | Links |

## Key claims and extracted specifics

### The hardware (§1.4, §2.1–2.2)

- **reBot Arm B601-RS spec table**: 6+1 DOF, **754 mm** max reach, **2.5 kg** payload (5 kg max), **6.5 kg** weight, **< 0.1 mm** repeatability, **ROBSTRIDE 06 ×3 + ROBSTRIDE 00 ×4**, −20–50 °C, **48 V 15 A**. Supported: ROS, MoveIt 1/2, LeRobot, Pinocchio, Isaac Sim. These differ substantially from the **B601-DM** numbers on the [product page](seeed-rebot-arm-b601-dm-thor-bundle.md) — see the contradiction callout below.
- **Leader arm** is the **Star Arm 102** ($200), 6+1 DOF, explicitly **"adhering to the Pieper criterion, so it supports analytical inverse kinematics with transparent algorithms."** That is a real engineering claim, not marketing: Pieper's criterion (three consecutive axes intersecting at a point) is what makes a closed-form IK solution exist at all.
- **The workspace is a controlled light box.** Chapter 2 requires building a *"standardized light-controlled workspace (the Lightbox) to match the visual assets in Isaac Lab"* — Lab Box + 2 adjustable light sources + 2 cameras + mounts, listed as a forthcoming Seeed product. The course is explicit that *"building an Embodied AI pipeline requires strict kinematic and visual consistency between the digital twin and the physical world."* **This is a sim-to-real gap being closed by constraining reality, not by improving the simulator** — worth naming, because it is the opposite of the [domain-randomization](../concepts/learning/sim-to-real-transfer.md) approach and it silently bounds how well the resulting policy will generalize outside the box.

### Data collection (§3.1–3.2)

- Software is three Seeed forks — `Seeed-Projects/lerobot`, `lerobot-teleoperator-rebot-arm-102`, `lerobot-robot-seeed-b601` — installed editable into a `uv` Python 3.12 venv, plus `motorbridge`. **The main-line LeRobot is not used directly.**
- Real collection: `lerobot-record` with two OpenCV cameras (`front` wrist-following + `side` fixed), **640×480 @ 30 fps**, **100 episodes**, 25 s episodes / 5 s reset, task string `"Organize stationery"`, output in **LeRobotDataset v3**.
- Sim collection (marked **optional**) uses a separate repo, `yuyoujiang/rebot-arm-dli-isaacsim`, on **Isaac Sim 4.5 / Ubuntu 22.04**. The architecture is worth noting: the leader arm drives the *simulated* B601 over **UDP `127.0.0.1:5005`** from a LeRobot Python bridge — i.e. the same physical teleop rig produces sim and real datasets in the same format. Domain randomization (objects, lighting, `front` camera) is applied per reset via `config/domain_randomization.json`, and task success is scripted (`config/grasp_config.json`).
- Operator-in-the-loop data hygiene is explicit: `C` discards an episode *"if an object falls, a grasp fails, the motion quality is poor, or the camera is occluded."* The dataset is curated as it is recorded.

### Cosmos3 Transfer augmentation (§3.3) — the most substantive module

- **Cosmos3 Transfer is used as a video-to-video model** (`"model_mode": "video2video"`) taking three inputs: source video, **control signals**, and a structured JSON text prompt. Available controls: **Edge** (Canny), **Segmentation** (requires SAM2), **Blur**, **Depth** (requires DepthAnything).
- **The load-bearing trick: action labels carry over unchanged.** Because Edge control is weighted dominant, the robot's geometry and trajectory are preserved while the background is replaced — so *"the original actions (joint angles, gripper state) work as-is for augmented videos."* One teleop episode becomes N training episodes across N scenes at zero extra robot time. **Recommended weights: `edge 0.9 / seg 0.1`**, `guidance 3.0`, `control_guidance 1.5`; the course notes only the *ratio* of control weights matters and they should sum to ~1.0.
- **Deployment footprint, stated:** **Cosmos3-Nano ~24 GB VRAM** (single RTX 4090 / A5000 / **Jetson AGX Thor**); **Cosmos3-Super ~80 GB × 4** (4× A100/H100). This is the wiki's first per-variant VRAM figure for Cosmos 3.
- **A concrete Jetson bug and its workaround.** On **L4T R39 + CUDA 13.2 + PyTorch 2.10**, `torch.addmm` (fused matmul+bias) raises `CUBLAS_STATUS_NOT_INITIALIZED` from `cublasLtMatmulAlgoGetHeuristic`. The course ships a `jetson_cublas_patch.py` that monkey-patches `F.linear`/`nn.Linear.forward` into separate `matmul + add`, imported before any other import, plus a `run_inference_jetson.py` wrapper. `--no-use-torch-compile` and `--no-use-cuda-graphs` are listed as **required** on Jetson, not optional.
- **The prompts are structured JSON**, not prose — `subjects[]` (description, appearance, action, pose, state_changes), `background_setting`, `lighting`, `aesthetics`, `cinematography`, `style_medium`, `context`, `actions[]` with timecodes, `temporal_caption`, `audio_description` — plus a shared `negative_prompt.json`. Three target scenes are shipped as examples: kitchen, lab, workshop.
- **Chunking:** the model's recommended frame range is **[24, 200]**; a 25-second 30 fps clip is 748 frames, so the framework falls back to **chunked autoregressive generation** (`num_video_frames_per_chunk` 57, 33 under memory pressure, 1 conditional overlap frame). The course warns quality degrades on long clips and that raising chunk size improves inter-chunk consistency at a memory cost.

> [!warning] The course reports its own augmentation result as *not good*
> Verbatim, on the output preview: *"We plan to transfer the data collection scenario to an industrial computer room. However, due to the resolution we have set being only 480p and possible issues with the prompt writing, the current outcome is not the best."* And its own suggested validation — FID/IS, a **policy transfer test** (train on augmented, measure real success rate), manual frame inspection — **is described but never run in the course**. So this module demonstrates the *mechanism* of generative augmentation without demonstrating that it *helps*. Treat the 0.9/0.1 weights as a working recipe, not as a validated one.

### GR00T 1.7 fine-tuning (§3.4)

- Base model is written **`nvidia/GR00T-1.7-3B`** (the wiki's [GR00T page](../entities/nvidia-groot.md) records the id as `nvidia/GR00T-N1.7-3B`; verify against the Hub before scripting it).
- **LeRobot v3 must be downgraded to v2** for GR00T: `scripts/lerobot_conversion/convert_v3_to_v2.py`. Worth flagging against the wiki's note that N1.7-in-LeRobot *requires* Dataset v3.0 — the **Isaac-GR00T repo path still consumes v2.1**, so the two N1.7 entry points disagree on dataset version and a conversion step sits between them.
- The **embodiment config** is the interesting part. Registered as `EmbodimentTag.NEW_EMBODIMENT` with: video keys `front` + `side` at `delta_indices=[0]`; state `single_arm` (6) + `gripper` (1); **action horizon 16** (`delta_indices=range(0,16)`); and per-modality action representations — **`single_arm` RELATIVE** (*"delta from current state (better generalization)"*) but **`gripper` ABSOLUTE** (*"binary open/close works better absolute"*), both `NON_EEF` joint-space. That relative-arm / absolute-gripper split matches the reference SO-101 recipe the wiki already records ("relative actions excluding gripper") — independent corroboration that this is the settled convention, not a one-off.
- Note the horizon: **16**, not the 40 the wiki records as N1.7's expanded action horizon. The course sets it explicitly in `ModalityConfig`, so 40 is evidently a ceiling, not a requirement.

### Evaluation (§3.5)

- Deployment is **decoupled server/client**: an inference server (`gr00t/eval/run_gr00t_server.py`) and a control client (`eval_rebot_arm_rs.py`) that owns the arm and cameras, talking over `127.0.0.1:5555`. Both can run on one box; the course requires **≥ 8 GB VRAM** for the PyTorch path.
- Result reported as narrative only: *"GR00T has successfully controlled the robotic arm to perform autonomous manipulation."* **No success rate, no trial count, no baseline.**
- Safety note carried as a CAUTION: on power or signal loss during teleop, stop the program and return the arm to zero **before** reconnecting, *"to prevent data disorder from causing robotic arm runaway."*

### Jetson deployment (§4.1–4.5) — the most operationally dense chapter

- **Validated targets: Jetson AGX Orin and Jetson AGX Thor, both on JetPack 7.2 / L4T R39.2.** Orin uses a `.venv-jp72` environment, Thor a `.venv`. Reserve **45–50 GB** for a full local TensorRT workflow.
- The deployment repo is a **third-party fork pinned to a commit** — `jjjadand/Isaac-GR00T-Orin-JP72` at `dcf5f6b759fd17cab3644a97fc4429bca7451e38` — not NVIDIA's own repo. That is a meaningful supply-chain detail for anyone reproducing this.
- **Backbone:** GR00T 1.7 defaults to **`nvidia/Cosmos-Reason2-2B`** (license acceptance required on the Hub); the pinned fork also validates **`Qwen/Qwen3-VL-2B-Instruct`** as a swap-in via `GR00T_BACKBONE_PATH`, explicitly *"a validated alternative for this checkpoint and repository revision, not the official GR00T 1.7 default."*
- **The TensorRT pipeline builds seven engines**: `vit`, `llm_bf16`, `vl_self_attention`, `state_encoder`, `action_encoder`, `dit_bf16`, `action_decoder` — built at **bf16, batch 1**, steps `export,build,verify,benchmark`. **This is a full-graph compile, not the official recipe's DiT-head-only compile** that the wiki's [GR00T-on-Jetson synthesis](../syntheses/platforms/gr00t-inference-on-jetson.md) analyzes. No latency numbers are printed in the course text (results appear only inside screenshots), so it does not settle whether the full-graph path beats 10.9 Hz — but it establishes that the path exists and is reproducible.
- **Engines are target-specific and must never be copied between Orin and Thor** — they bind GPU architecture, TensorRT version, checkpoint, graph shapes, precision, and builder config. Rebuild after changing any of checkpoint, backbone, TensorRT version, precision, batch size, action horizon, or shapes.
- **JetPack 7.2 ships without working USB-CAN kernel modules.** The course distributes prebuilt `gs_usb.ko` and `peak_usb.ko` **from a Seeed OneDrive share**, to be `modinfo`-checked against `uname -r` and installed into `/lib/modules/$(uname -r)/extra/`. CAN is then brought up at **1 Mbit/s** (`bitrate 1000000 restart-ms 100`). A robot arm that talks CAN does not work out of the box on JetPack 7.2.
- **Jetson AGX Thor has only two USB Type-A ports** — a powered USB 3.0 hub is required to run two cameras plus a USB-CAN adapter simultaneously. A small hardware fact with real consequences for a two-camera VLA rig.
- Repeated operational warning: `/dev/videoX` indices are **not stable** across reconnects or reboots; re-run `lerobot-find-cameras` / `v4l2-ctl --list-devices` before every session.

## Contradiction with the product page

> [!warning] Contradiction — the course teaches the B601-**RS** but the hardware list links the B601-**DM**
> §1.4 specs the **B601-RS** (Robstride motors, 2.5 kg, < 0.1 mm, 48 V) and every command in the course uses `--robot.type=seeed_b601_rs_follower` over SocketCAN `can0`. But §2.1's "Reset Motors ID" hardware list links **"reBot Arm B601 DM Robotic Arm × 1"**, a **DM CAN-USB Driver Board**, a **24 V 15 A** supply, and **`DM_Tools_v1.8.0.1.exe`** (Damiao's Windows motor tool) — and the same section carries an *alternative* calibration log for `--robot.type=seeed_b601_dm_follower --robot.can_adapter=damiao` on `/dev/ttyACM0`, dated **2026-05-28**, three months before the RS log dated **2026-07-28**.
>
> Read together, this looks like a course **originally authored against the DM arm and later re-shot on the RS**, with the motor-ID section left un-migrated. Practical consequence: **a DM owner following §2.1 verbatim will hit RS commands that do not match their arm.** The two variants differ in CAN adapter (`damiao` vs `socketcan`), device node (`/dev/ttyACM0` vs `can0`), motor CAN ID pairs, joint-limit signs (DM: `elbow_flex (-200, 1)`; RS: `elbow_flex (-0, 200)`), and control mode (`ensure mode 2` vs `ensure mode 1`). The DM path is documented but not carried through the rest of the course.

## Entities mentioned

- [Seeed Studio](../entities/seeed-studio.md)
- [reBot Arm B601](../entities/rebot-arm-b601.md), [Star Arm 102](../entities/star-arm-102.md), [Damiao](../entities/damiao.md), [Robstride](../entities/robstride.md)
- [LeRobot](../entities/lerobot.md), [Hugging Face](../entities/hugging-face.md)
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md), [NVIDIA Cosmos](../entities/nvidia-cosmos.md), [NVIDIA GR00T](../entities/nvidia-groot.md)
- [Jetson Thor](../entities/jetson-thor.md), [Jetson Linux](../entities/jetson-linux.md)
- [SO-ARM101](../entities/so-arm101.md) — the reference recipe this one parallels

## Concepts touched

- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md)
- [Generative data augmentation](../concepts/learning/generative-data-augmentation.md)
- [VLA models](../concepts/learning/vla-models.md)
- [Imitation learning](../concepts/learning/imitation-learning.md)

## Open questions

- **Does the Cosmos augmentation actually improve real-world success rate?** The course proposes the policy-transfer test and does not run it. This is the single most valuable unmeasured number in the source.
- **What throughput does the seven-engine full-graph TensorRT pipeline achieve on Thor?** The benchmark output exists only as a screenshot. If full-graph beats the official DiT-only 10.9 Hz, the wiki's [Jetson inference table](../syntheses/platforms/gr00t-inference-on-jetson.md) needs a new row.
- **Why does the sim-collection module say the simulation dataset is "optional"?** For a course titled *sim-to-real*, the sim half is marked skippable and never enters the training command, which trains on the real (and Cosmos-augmented) data only. The pipeline as taught is closer to **real → generative augmentation → real** than to sim-to-real.
- **Is `nvidia/GR00T-1.7-3B` or `nvidia/GR00T-N1.7-3B` the canonical Hub id?**
- **Does the Lightbox generalize?** Training inside a light-controlled box and augmenting backgrounds generatively are two answers to the same problem, and the course uses both without discussing whether the second undoes the constraint the first imposes.
