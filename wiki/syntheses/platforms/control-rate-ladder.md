---
title: The control-rate ladder — LLMs, VLAs, and servo loops on one axis
type: synthesis
created: 2026-07-27
updated: 2026-08-04
tags: [latency, inference, control-frequency, vla, llm-agent, edge-ai, jetson, action-chunking, control-abstraction-levels, platforms, turbovla, llm-free-vla]
---

# The control-rate ladder — LLMs, VLAs, and servo loops on one axis

The wiki carries frequency numbers in three places that never touch: **what robots require** (a Franka servos at 1 kHz), **what learned policies achieve** (SmolVLA runs at 1.4 Hz on an Orin Nano), and **what a language model in the loop achieves** ([0.2–0.4 Hz](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md)). Anthropic's robotics evaluation states its gap as **83 Hz needed vs 0.2–0.4 Hz achieved — ~100×**, and that figure has been sitting next to the wiki's on-Jetson VLA numbers without anyone lining them up.

This page lines them up. The short version: **the full span is about five orders of magnitude, no single system closes it, and none is expected to** — the gap is bridged architecturally, by hierarchy and by action chunking, not by making inference faster.

> [!warning] This is a ladder of magnitudes, not a benchmark
> These numbers come from wildly different conditions: an H100, an RTX 4090, a 25 W Orin Nano, a **paused simulator**, and vendor self-reports. Rows are not comparable to each other as measurements. What survives the incomparability is the **band structure** — the separations here are 10× to 1000×, far larger than the measurement noise.

## The one axis

**REQ** = a rate something demands. **MEAS** = a rate something achieved. **CAP** = a teleop/dataset *capture* rate (neither a requirement nor an inference speed — included because these set the action-chunk cadence policies are trained to reproduce). Descending.

† MotionBricks' 15,000 FPS is batched throughput, not a single-stream control rate; its 2 ms latency figure (~500 Hz) is the comparable one. Listed at the top because that is how the source headlines it.

| Hz | Kind | What | Where |
|---:|:---:|---|---|
| **15,000** † | MEAS | MotionBricks latent motion model — **15,000 FPS throughput**, separately **2 ms latency** (≈500 Hz single-stream) | [MotionBricks](../../sources/motionbricks-paper.md) |
| **1,000** | REQ | [Franka Panda](../../entities/franka-panda.md) joint servo loop | robot firmware |
| **9,550** | MEAS | [OSCBF](../../sources/oscbf-paper.md) safety filter, **1 CBF** (singularity avoidance), velocity control — JAX/XLA QP | Franka Panda, i7 NUC |
| **2,940** | MEAS | [OSCBF](../../sources/oscbf-paper.md) **168 concurrent CBF constraints**, torque control, full second-order dynamics | Franka Panda, i7 NUC |
| **5,000** | MEAS | [PACS](../../sources/pacs-paper.md) reachability safety step, **0.20 ms** (CBF baseline 0.64 ms ≈ 1.6 kHz); deployed at 1 kHz | Franka FR3 |
| **~1,000** | MEAS | [OSCBF](../../sources/oscbf-paper.md) with **>400 CBF constraints** (cluttered scene, whole-body collision avoidance) | Franka Panda, i7 NUC |
| **~1,000** | MEAS | **[Diffusion Policy](../../sources/diffusion-policy-paper.md)'s mid-level controller** — constrained diff-IK QP, *"runs around 1kHz"*, interpolating the 10 Hz policy's commands | Franka station (TRI/MIT) |
| **500** | REQ | Upper bound of [whole-body control](../../concepts/robotics/whole-body-control.md) torque loops | humanoid WBC |
| **~200** | MEAS | [ACT](../../entities/act.md), 5.0 ms | RTX 4090 |
| **200** | REQ | Helix **System 1** fast controller (80 M params) | [Figure](../../entities/figure.md) 02, onboard |
| **200** | MEAS | [Operational-space-control](../../concepts/robotics/operational-space-control.md) torque QP (position/velocity/torque limits as constraints) — haptic teleop mode | Franka station (TRI/MIT) |
| **120** | REQ | [GR00T](../../entities/nvidia-groot.md) N1 **System 1** flow-matching DiT | design target |
| **100** | REQ | [Stretch](../../entities/stretch.md) Body loop, watchdog, self-collision avoidance | robot firmware |
| **~83** | **REQ** | **Real-time legged control** — the Anthropic figure | [robotics eval](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md) |
| **55–333** | MEAS | [VQ-BeT](../../entities/vq-bet.md), 3–18 ms/step — *closed-loop on a Stretch **CPU*** | Stretch |
| **55.8** | MEAS | [MolmoAct2](../../entities/molmoact2.md) continuous path (Think: 12.7) | **H100** |
| **50** | REQ | [GEAR-SONIC](../../entities/gear-sonic.md) WBC policy (1–2 ms/forward on Orin) | Unitree G1 |
| **50** | CAP | [ALOHA](../../entities/aloha.md) camera rate; shirt-folding teleop capture | real rigs |
| **32.1** | MEAS | [TurboVLA](../../entities/turbovla.md) — **0.2 B, 31.2 ms, 0.9 GB VRAM**, no LLM in the loop | RTX 4090 |
| **32.1** | MEAS | GR00T N1.6-3B TensorRT | RTX 5090 |
| **30** | REQ | [YAM](../../entities/yam.md) bimanual control, absolute joint (MolmoAct2's real rig) | real rig |
| **27.8** | MEAS | **[ACT](../../entities/act.md) on-edge, 36 ms** — the only edge policy fast enough for reactive control | [Orin Nano](../../entities/jetson-orin-nano.md) |
| **25** | MEAS | [OpenVLA-OFT+](../../entities/openvla-oft.md) bimanual, real | ALOHA |
| **22–24** | MEAS | GR00T N1.6, community CUDA kernels | [Jetson Thor](../../entities/jetson-thor.md) |
| **20** | CAP | [Fourier GR-1](../../entities/fourier-gr-1.md) teleop capture (VIVE + Metagloves); table-bussing capture | real rigs |
| **15** | CAP | [DROID](../../entities/droid.md) capture rate | dataset |
| **15** | MEAS | **[Cosmos 3 Edge](../../sources/nvidia-cosmos3-edge-hf-blog.md) (4B world model)**, 32 actions/inference @ 640×360 — vendor-reported | [Jetson Thor](../../entities/jetson-thor.md) |
| **10.9** | MEAS | GR00T N1.6, official TensorRT | Jetson Thor |
| **10.7** | MEAS | [π0.5](../../entities/pi-zero-5.md), 93.6 ms — *re-measured by the TurboVLA authors on the same 4090* | RTX 4090 |
| **~10** | REQ | Helix **System 2** / GR00T **System 2** VLM planner tier | design target |
| **8–11** | MEAS | GR00T-3B *estimated* (bandwidth-derived, unmeasured) | [DGX Spark](../../entities/dgx-spark.md) |
| **8.9** | MEAS | [OpenVLA-OFT](../../entities/openvla-oft.md), 112.2 ms — same re-measurement | RTX 4090 |
| **7.3** | MEAS | [Evo-1](../../entities/evo-1.md) 0.8 B, 137.2 ms — small but **not** fast | RTX 4090 |
| **5.8** | MEAS | GR00T N1.6, TensorRT | AGX Orin 64 GB |
| **5** | MEAS | [RT-2](../../entities/rt-2.md) 5B variant | TPU cloud |
| **5** | CAP | BridgeV2 capture rate | dataset |
| **4.9** | MEAS | [SmolVLA](../../entities/smolvla.md), 203.1 ms — same re-measurement | RTX 4090 |
| **4** | MEAS | [VLA-0](../../entities/vla-0.md) — action-as-text is slow | GPU |
| **3** | MEAS | **[RT-1](../../entities/rt-1.md)** — 35M, FiLM-EfficientNet + TokenLearner; the rate was a *design constraint* | onboard |
| **1–3** | MEAS | **[RT-2](../../entities/rt-2.md)-PaLI-X 55B** — *"infeasible on standard desktop machines"*; **served from a multi-TPU cloud over the network** | TPU cloud |
| **1.8** | MEAS | [Diffusion Policy](../../entities/diffusion-policy.md), 540 ms | Orin Nano |
| **1.4** | MEAS | [SmolVLA](../../entities/smolvla.md)-450M, 714 ms | Orin Nano |
| **1.3** | MEAS | [FAST](../../entities/fast-action-tokenization.md) autoregressive decode, ~750 ms/1 s chunk | RTX 4090 |
| **1** | REQ | **[Nav2](../../entities/nav2.md) global replanning** — `RateController hz="1.0"` in the shipped default [behavior tree](../../concepts/robotics/behavior-trees.md) | ROS 2, production |
| **~1** | MEAS | Agent heartbeats — [AgenticROS](../../entities/agenticros.md), [ros2-mcp-server](../../entities/ros2-mcp-server.md) capability beacons | Orin NX |
| **0.5** | MEAS | SmolVLA on **CPU**, 2,028 ms | CPU |
| **0.2–0.4** | **MEAS** | **Frontier LLM, non-reasoning** (2–8 s text; 5–15 s with images; **15–180 s with reasoning**) | [robotics eval](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md) |

## Four bands, and the gaps between them

**Band A — servo/torque, 100–1,000 Hz (requirement only).** Where physics is. Nothing learned and general runs here; it is occupied by firmware, PD loops, and small purpose-trained controllers (SONIC at 50 Hz on 1–2 ms forwards, Helix S1 at 200 Hz on 80 M params). Anthropic's **83 Hz** sits at the bottom edge of this band.

> [!note] The one controlled slice of this ladder (added 2026-08-04)
> Every row here comes from a different rig, which is why the page warns it is a ladder of magnitudes rather than a benchmark. The **[TurboVLA](../../entities/turbovla.md)** ingest supplies the exception: seven of the rows above — TurboVLA 32.1, π0.5 10.7, OpenVLA-OFT 8.9, Evo-1 7.3, SmolVLA 4.9, plus DDVLA and OpenVLA — were **measured by one group, on one RTX 4090, at batch size 1, from official checkpoints**, all input→action-chunk. Within that slice the comparisons are real.
>
> Two things it shows. **(1) Parameter count is a poor latency predictor**: [Evo-1](../../entities/evo-1.md) at 0.8 B (137.2 ms) is *4.4× slower* than TurboVLA at 0.2 B (31.2 ms), and slower than π0.5 at 3.4 B — because it keeps a pretrained multimodal backbone in the loop. What costs time is **what is in the pathway**, not how many weights are in the file. **(2) The 4090 numbers land a full band below where desktop-GPU intuition puts them** — π0.5 on a 4090 runs at 10.7 Hz, essentially the same as GR00T on a Jetson Thor. The "just use a big GPU" escape from Band C is smaller than it looks; changing the architecture moved a policy three times further than changing the silicon.

**Band B — reactive policy, ~10–60 Hz (achievable, barely, at the edge).** [ACT](../../entities/act.md) at 27.8 Hz on an Orin Nano is the wiki's only edge policy comfortably here. Thor gets GR00T to 22–24 Hz with hand-written kernels, and **[Cosmos 3 Edge](../../sources/nvidia-cosmos3-edge-hf-blog.md) reports 15 Hz on Thor for a 4B *world* model** (2026-07-20) — the first 2026-class edge number in this band, and notably above official-TensorRT GR00T on the same board. MolmoAct2's 55.8 Hz belongs to this band only on an **H100** — a caveat the [deployability landscape](vla-deployability-landscape.md) already flags.

**TurboVLA at 32.1 Hz is the first entry in Band B that is a *general language-conditioned VLA on a single consumer GPU*** — ACT gets there by having no language conditioning, MolmoAct2 by using an H100, GR00T by hand-written Thor kernels. Its 0.9 GB inference footprint also makes it the only VLA in this table that would *fit* an [Orin Nano](../../entities/jetson-orin-nano.md) 8 GB without contortion. **No edge measurement exists**, and a 4090 is not an Orin — the Cutting-the-Cord numbers show edge boards costing roughly an order of magnitude against desktop parts — so the honest expectation is Band C, not Band B, on a Nano. That measurement is the most valuable single experiment this page could acquire. See [LLM-free VLA](../../concepts/learning/llm-free-vla.md).

**Band C — deliberative policy, ~1–10 Hz.** Where most VLAs actually live on real edge hardware: SmolVLA 1.4, Diffusion Policy 1.8, GR00T 5.8–10.9. Also where the S1/S2 designs *place* their planner tier by intent (Helix S2 at 7–9 Hz, GR00T System 2 at 10 Hz).

**Band D — language model, 0.2–0.4 Hz, and far below with reasoning.** Three to four orders of magnitude beneath Band A.

The two big separations: **~100× from Band D to Band B**, and **~10–100× from Band B to Band A**. Anthropic's stated 100× gap is the *first* of those. The second one is older, is not about LLMs at all, and nobody has closed it either — which is exactly why the field's architectures look the way they do.

## What actually bridges the gap

Neither separation is closed by faster inference. Three mechanisms do the work, and all three are already documented in the wiki:

> [!note] Band A is not only about tracking — in a manipulation stack it is where **safety** is enforced
> The 1 kHz entry above is not a servo loop the vendor supplied; it is a **constrained QP the lab wrote**, and its constraints are arm–arm collision, the table, an end-effector keep-out region, and joint limits. The learned policy at 10 Hz emits *requests*; this layer decides what actually reaches the joints, ~100 times per request. Its authors call it *"particularly valuable for safeguarding the learned policy during hardware deployment"* ([Diffusion Policy](../../sources/diffusion-policy-paper.md) App. D.1; the same architecture reappears in the [TRI LBM](../../sources/tri-lbm-paper.md) stack).
>
> **And the safety layer has far more headroom than the policy does.** [OSCBF](../../sources/oscbf-paper.md) holds ~3 kHz with **168 simultaneous constraints** and ~1 kHz with **over 400** — on a **laptop-class CPU**, in **Python** (JAX/XLA). The constraint layer is not what limits this stack; a policy three orders of magnitude slower is.
>
> This reframes the ladder's central gap. The 10 Hz-policy-over-1 kHz-controller ratio is usually read as *the policy is too slow*. Read the other way, **the ratio is what makes a slow stochastic policy deployable at all**: something fast, model-based, and unable to be talked out of its constraints sits between it and the hardware. See [operational space control](../../concepts/robotics/operational-space-control.md).

**1. Hierarchy (the S1/S2 split).** [Helix](../../sources/helix-blog.md) pairs a 7 B VLM at 7–9 Hz with an 80 M transformer at 200 Hz; [GR00T N1](../../entities/nvidia-groot.md) pairs an Eagle-2 VLM at 10 Hz with a flow-matching DiT at 120 Hz; [SONIC](../../entities/gear-sonic.md) puts a 50 Hz WBC policy under a GR00T VLA. The pattern is the same every time: **let the slow tier be slow, and put something fast underneath it.** This is Band C driving Band A across a ~20× ratio, and it is the field's answer to the question Anthropic's 83 Hz figure poses.

**2. Action chunking.** A policy that infers at 1.8 Hz but emits a 16-step chunk is not controlling the robot at 1.8 Hz. GR00T N1 produces a 16-action chunk in 63.9 ms; [OpenVLA-OFT](../../entities/openvla-oft.md) gets **26×** throughput from 8-step chunks and **43×** from 25-step. **Inference Hz and control Hz are different quantities**, and most of the alarming numbers on this page are inference Hz. (Note the dissent: [VQ-BeT](../../entities/vq-bet.md) argues chunking *hurt* where tried, because at 3–18 ms/step it is fast enough to close the loop honestly — on a **CPU**.)

**3. Async inference.** [SmolVLA](../../entities/smolvla.md)'s RobotClient/PolicyServer pattern overlaps computing the next chunk with executing the current one: 1.8 → 3.8 cubes/60 s on SO-100, same policy.

> [!note] The reframe
> Anthropic's 83 Hz figure describes **level-1 direct control** in the [control-abstraction taxonomy](../../concepts/robotics/control-abstraction-levels.md) — a level at which *nothing in this wiki deploys, LLM or otherwise*. The honest comparison is not "LLM vs the servo loop." It is **LLM at 0.2–0.4 Hz vs the VLA planner tier at 1.4–27.8 Hz** — the tier an LLM would actually have to occupy. That gap is ~10–100×, not ~100–400×, and it is the one worth tracking.

## Two findings that only appear side-by-side

**The bottlenecks are different, so the fixes are different.** [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) found that on an Orin Nano, SmolVLA-450M (714 ms) adds only *minor* overhead over Diffusion Policy (540 ms) — the wall is the **iterative denoising/flow steps (T=10)**, not the semantic head. So Band C's problem is **sampling steps**, and the fix is distillation or fewer steps. Band D's problem is **autoregressive token generation over a long context with images**, and the fix is something else entirely. Two numbers one order of magnitude apart, commonly discussed as one "latency problem," with no shared cause. Compare [FAST](../../entities/fast-action-tokenization.md)'s 1.3 Hz autoregressive decode on a **4090** — that is the Band-D failure mode appearing inside a VLA, and it is precisely what OpenVLA-OFT's parallel decoding was built to kill.

**Reasoning tokens are a rate decision.** Anthropic measured 2–8 s without reasoning and **15–180 s with** — up to a 20× penalty, on the same model. [MolmoAct2](../../entities/molmoact2.md) shows the same trade inside a VLA: 55.8 Hz continuous vs **12.7 Hz** for MolmoAct2-Think, ~4×, for +0.9 LIBERO points. And Anthropic found that reasoning budget produced **no general robotics gain and sometimes hurt**. Across both, the pattern holds: **on embodied tasks, reasoning tokens cost an order of magnitude of control rate and have not yet bought a commensurate capability gain.** The one exception in either source is Claude Mythos Preview (40.2 → 54.1 across reasoning configs), which is unexplained.

## What this page cannot tell you

- **No row is a controlled comparison.** Hardware, precision, batch size, chunk length, and image count all vary. Treat bands as real and individual gaps as approximate.
- **The Anthropic 0.2–0.4 Hz figure is API-served frontier-model latency**, not an optimized on-robot deployment. Nobody has measured a small local LLM in a robot control loop in any ingested source — the nearest things are 1 Hz agent *heartbeats* ([AgenticROS](../../entities/agenticros.md), [ros2-mcp-server](../../entities/ros2-mcp-server.md)), which are status beacons, not control.
- **Almost no 2026-class VLA has an on-Jetson number.** [Cosmos 3 Edge](../../sources/nvidia-cosmos3-edge-hf-blog.md)'s 15 Hz on Thor is the first, and it is a vendor self-report at 640×360 whose end-to-end scope is unclear. MolmoAct2's 55.8 Hz is H100-only; the [deployability landscape](vla-deployability-landscape.md) flags this and the [Jetson ladder](jetson-module-ladder-power-performance.md) holds the sparse edge numbers. The single most valuable missing measurement in this whole area is **MolmoAct2 (or any 2026-class VLA) on Thor**.

  > [!note] Update 2026-08-03 — the *memory* half of this gap is now answerable, the *rate* half is not
  > Ingesting the [MolmoAct2 repo](../../sources/molmoact2-github-repo.md) and [SO-100/101 card](../../sources/molmoact2-so100-101-model-card.md) supplies footprints but no throughput: the SO-100/101 checkpoint is **5B params, ~24–26 GB float32, ~16 GB bf16**; YAM under 16 GB bf16; DROID ~88 GB float32. Tested hardware is **RTX A6000 and Intel XPU — no Jetson build, benchmark, or mention anywhere in the repo.**
  >
  > So the model is now *sizeable* against the [Jetson ladder](jetson-module-ladder-power-performance.md) (16 GB bf16 rules out Orin NX 16 GB once unified memory and OS overhead are counted; AGX Orin 64 GB and Thor remain plausible) but still not *rateable*. **The missing measurement is unchanged** — and MolmoAct2 ships nothing that would make producing it easy, since its CUDA-12.1-pinned `uv` toolchain is a known friction point against JetPack's own CUDA.
- **Chunk-adjusted effective control rates are not published** for most policies, so the inference-Hz vs control-Hz distinction stays qualitative here.
- **Power is a hidden third axis.** 27.8 Hz on a 25 W Orin Nano and 55.8 Hz on a 700 W H100 are not the same achievement; see the [Jetson module ladder](jetson-module-ladder-power-performance.md).

## Related
- [Control abstraction levels](../../concepts/robotics/control-abstraction-levels.md) — *where* in the stack a controller acts; this page is the frequency each level demands.
- [VLA deployability landscape](vla-deployability-landscape.md) — the latency axis scored per-model, with the H100-vs-edge caveat.
- [GR00T inference on Jetson](gr00t-inference-on-jetson.md) — the deepest single-model version of this question.
- [Jetson module ladder](jetson-module-ladder-power-performance.md) — the hardware underneath the MEAS rows.
- [Onboard compute for XLeRobot](jetson-onboard-compute-xlerobot.md) — where the 27.8 / 1.8 / 1.4 Hz numbers come from.
- [Whole-body control](../../concepts/robotics/whole-body-control.md) — Band A's actual occupant.
- [VLA models](../../concepts/learning/vla-models.md) — the S1/S2 structural pattern.

## Sources
- [How Claude Performs on Robotics Tasks](../../sources/anthropic-how-claude-performs-on-robotics-tasks.md) — 83 Hz requirement; 0.2–0.4 Hz inference; reasoning-latency range.
- [Cutting the Cord (Shaw et al., 2026)](../../sources/cutting-the-cord-untethered-xlerobot.md) — the on-edge ACT / Diffusion Policy / SmolVLA measurements.
- [Isaac GR00T TensorRT deployment docs](../../sources/isaac-gr00t-tensorrt-deployment-docs.md) + [NVIDIA forum report](../../sources/nvidia-forum-thor-realtime-vla-inference.md) — Thor / AGX Orin / RTX 5090 GR00T numbers.
- [MolmoAct2 paper](../../sources/molmoact2-paper.md), [OpenVLA-OFT paper](../../sources/openvla-oft-paper.md), [FAST paper](../../sources/fast-paper.md), [Knowledge Insulation paper](../../sources/knowledge-insulation-paper.md), [SmolVLA paper](../../sources/smolvla-paper.md), [LeRobot ICLR 2026 paper](../../sources/lerobot-iclr-2026-paper.md), [GR00T N1 paper](../../sources/groot-n1-paper.md), [Helix blog](../../sources/helix-blog.md), [SONIC paper](../../sources/sonic-paper.md), [MotionBricks paper](../../sources/motionbricks-paper.md).
