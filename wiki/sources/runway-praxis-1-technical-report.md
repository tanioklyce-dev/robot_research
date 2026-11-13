---
title: "Praxis-1: From Video Pretraining to Robot Control — Runway technical report (November 2026)"
type: source
url: https://runway.com/research/praxis-1-video-pretraining-to-robot-control
fetch_url: https://runway.com/research/praxis-1-video-pretraining-to-robot-control
local_path: raw/2026-11-11-runway-praxis-1-technical-report.md
sha256: 511157a8ac083ded404996dc7ce0dec05ee5840dc766c6a03a556a304b6d2de9
author: Runway
published: 2026-11-11
venue: "Runway Research, an interactive web technical report with no arXiv version. It cites DeepSeek-V3, DDT, DeVA, mimic-video and arXiv 2610.22471 (SenseNova-RoboRSI)."
format: "web technical report, about 7,000 words of extracted text with 17 figures and tables"
license: "Released checkpoints and code: Apache-2.0"
tags: [praxis-1, runway, world-action-model, mixture-of-experts, diffusion-transformer, rectified-flow, action-expert, chunk-causal-attention, teacher-forcing, video-pretraining, egocentric-video, robolab, droid, yam, rt-1, simplerenv, so-101, lerobot, nvfp4, quantization, real-time-chunking, classifier-free-guidance, gpt-6-astra, flux-3, success-prediction]
ingested: 2026-11-12
---

## Summary

**The primary source for [Praxis-1](../entities/praxis-1.md).** Runway takes its 27B-parameter video generation model (a mixture-of-experts diffusion transformer, 2.8B parameters active per token) and turns it into a [world-action model](../concepts/world-models/world-action-model.md). It makes the attention **chunk-causal**, mid-trains on embodied video that is mostly egocentric human footage, then adds a **separate 314M action expert**. This expert cross-attends into eight backbone layers *while the backbone imagines the next 1.6 seconds*. On each call the model returns predicted video plus **24 action rows at 15 Hz** after two joint Euler steps, which takes about 0.55 s on one H100. The DROID fine-tune scores **46.2% on RoboLab-120** (555/1,200). That is the best WAM and best open model on the board, but **fourth-to-fifth overall**. It also gets **88/100 vs 80/100** against FLUX 3 Action on a real Franka, and **80.0% on RT-1 SimplerEnv**, an embodiment it had never seen. The report is unusually candid about its limits. It says when differences are not significant, reports a compute-scaling curve that **plateaus** at its last point, and finds that **most action error comes from imagining the wrong future, not from reading motion off the right one**. Oracle error is 1.14 cm against 5.71 cm when the model imagines its own future.

## Key claims

### Architecture (§2)
- **Backbone.** Runway's video foundation model, a DDT-style split into a condition encoder (14 blocks) and a velocity decoder (6 blocks). It runs in the **frozen Wan2.2 VAE** latent space and reads text through a **frozen Qwen3.5-2B** encoder. 17 of 20 FFN layers are MoE, each with **1 shared + 128 routed experts, top-8**, balanced as in DeepSeek-V3. That gives **26.9B total and about 2.8B active** parameters.
- **Chunk-causal attention.** The pretrained model attended over whole clips. Mid-training switches it to **1.6 s chunks of six latent frames**, each of which sees only earlier chunks. Training uses teacher forcing with clean real-video context, which lets it train four chunks in one pass. Inference reads **one clean context chunk** of real camera frames.
- **Action expert.** A dense 16-layer, width-1024, **314M** transformer that alternates cross-attention and self-attention. Its **8 cross-attention layers each read one backbone encoder block**, from early to late. It reads the backbone's *noised current chunk*, so it acts on the future as the backbone imagines it. **Nothing flows back into the backbone in the forward pass**, but the action loss still trains the backbone through those reads. The report says the design is closest to DeVA.
- **Rejected alternative.** Putting action tokens inside the backbone (mixture-of-transformers) made **no clear difference (+0.01 cm action error) and cost more**. Cosmos 3 uses this kind of MoT layout ([Cosmos 3 report](cosmos-3-technical-report.md)).
- **Interface.** Exterior and wrist cameras are each tiled at 224×416, side by side on a 224×832 canvas at 15 fps. Action rows are per-embodiment: DROID Franka uses 10-D (xyz, 6-D rotation, gripper), bimanual YAM 20-D, and human hands 21 joints in 3-D. Actions are relative to the pose at the start of the chunk. Robot state is dropped for 10% of samples. **Each robot has its own thin input and output projections**, while the backbone and expert are shared.
- **Objective and size.** Rectified flow on both streams, with video and action noise levels drawn independently. **27.2B parameters, 54.4 GB in bf16, fits on one 80 GB GPU.**

### Training (§3)
1. **Video pretraining** on twelve generation tasks (text/image/reference → image/video/audio), using clips of up to 20 s with full attention.
2. **Embodied-video mid-training**, now chunk-causal. The mix is **58% egocentric human video, 20% general video, 18% real-robot video, under 1% gameplay**.
3. **Joint video and action mid-training.** The expert is added with fresh weights, and its learning rate and the action gradient into the backbone ramp up from zero over 1,500 updates *"to protect the video model"*. About **30% of tasks stay video-only**. Embodiments: DROID, YAM, low-cost bimanual arms, UMI and human hands. Optimizers are Muon plus AdamW.
4. **Embodiment fine-tuning** of everything except the frozen encoders, with the video loss kept on. The DROID run uses **about 277 hours of successful episodes only, 128 H100s, 50k steps at LR 5×10⁻⁵**.

### Compute scaling (§4)
- **DROID (a seen embodiment).** Five mid-training checkpoints, each fine-tuned identically, score **25.5 → 35.2 → 39.2 → 41.2 → 41.2%** on RoboLab-120. **The last point levels off.** Total compute is roughly 6–9 × 10²³ FLOPs.
- **RT-1 (an unseen embodiment).** SimplerEnv rises from **56.3% to 80.0%**, but not at every step: 65.6, 66.9, then 64.1 before 80.0. Each point is 864 episodes with 95% intervals.
- The report says this *"measures more training compute rather than more data"*, because later checkpoints revisit the same data, and that *"the exact relationship needs further study"*.

### Inference (§5)
- **Default chunked mode.** About **0.55–0.6 s round trip per 1.6 s chunk** on one H100. Server p50 is 545 ms for YAM and 522 ms for DROID with video CFG 4.
- **Real-time chunking (RTC), opt-in.** Blending the old and new plans made the arm oscillate. Continuing from where the arm will actually be fixed this. Idle time drops **from 32% to 5%**, and the server p50 is about 125 ms with streaming optimization. On a five-object bag task RTC succeeded **24/30 vs 28/30** for chunked mode, with median time to success **9.1 vs 15.2 s**.

### Results (§6)
- **RoboLab-120 under the official protocol of 10 trials per task: 555/1,200 = 46.2%.**

| Model | RoboLab-120 | Class (per report) |
|---|---|---|
| AMP1 | 86.0% | zero-shot frontier-model agent |
| SenseNova-RoboRSI | 57.1% | frontier VLM as policy |
| Lakeside | 51.0% | closed, partly sim-trained |
| BiMind v0.5 | 49.2% | closed, **fine-tuned on RoboLab data** |
| **Praxis-1 (DROID FT)** | **46.2%** | WAM, open |
| FLUX 3 Action | 42.9% | WAM |
| Atomic-WAM | 39.6% | WAM |
| OASIS WAM | 39.0% | WAM |
| Cosmos 3 Nano | 36.8% | WAM |
| π0.5 | 28.0% | open VLA |
| DreamZero | 25.7% | WAM |
| GR00T N1.6 | 7.3% | open VLA |

- **SenseNova-RoboRSI's cost.** Its own authors report about **55 minutes of compute per episode** on RoboDojo and call it impractical for deployment (arXiv 2610.22471).
- **Real Franka FR3**, operated by Positronic on FLUX 3 Action's own ten published tasks with 10 episodes each, run on 2026-11-02: **Praxis-1 88/100, FLUX 3 Action 80/100**. Per task, Praxis-1 is ahead on five tasks and tied on five.

### Against a frontier LLM agent (§7.3)
- On the same YAM station and three tasks, [GPT-6 Astra](../entities/gpt-6-astra.md) took **15.6× longer** (4:13 vs 0:16 average) and cost **51× more per completed task** ($1.87 vs $0.04). Praxis-1 is costed at one H100 at $3.95/hour. The data was collected 2026-11-09.
- The two are framed as complementary: *"an agent can plan a new task, and a fast policy like Praxis-1 can carry out each step."*

### New embodiments (§8)
- **RT-1.** RT-1 data appears in **no** pretraining or mid-training stage. Fine-tuning ran 30k steps (about 28 hours on 32 H100s) on 78k episodes and 95 hours, with the head camera only. On SimplerEnv visual matching (864 episodes, 4 tasks): **Praxis-1 80.0%, RT-1 52.4%, FLUX 3 Action 39.7%**. Per task, Praxis-1 scored pick coke can 98.3, move near 81.7, drawer 56.5, apple into drawer 83.3. Runway fine-tuned the FLUX 3 Action baseline itself, using BFL's published *DROID* recipe.
- **SO-100/SO-101.** Runway gathered **3,956 public LeRobot datasets from 1,783 contributors, about 1,260 hours**. Camera names were unreliable (*"a camera called 'phone' or 'top' is often mounted on the wrist"*), so each camera was labelled as wrist or scene from its video. Both a motion check and a CLIP check had to agree. Fine-tuning used about 1,070 hours from 3,814 datasets, with 102 held out. The model predicts **5 joints plus gripper as offsets at 15 Hz** and works with or without a wrist camera. Results are shown as video only, with no success rates.

### Guidance (§9)
- Two Euler steps, with CFG on the instruction only. The step-wise search ended **4.0 pp above the start**, and the shipped settings are **video CFG 4, shift 12.5**. These settings are **embodiment-specific**: *"other robots need their own."* One tested setting cost −14.0 pp.

### Offline evaluation (§10)
- **Where the error comes from.** End-effector error on 32 held-out DROID windows is **1.14 cm with the true future video (oracle) against 5.71 cm when the model imagines its own**. *"Most of the remaining error comes from which future the video model imagines, not from the action expert."* The method follows the mimic-video oracle test.
- **Imagined rollouts.** 12.6 s open-loop self-rollouts from a single synthetic first frame are scored by a VLM judge. The report calls this *"a proxy… how it relates to real-world success still needs further study"*.
- **Predicting success.** A small head on the frozen model's predicted next chunk, trained only on whole-episode outcomes, reaches **AUROC 0.77 (0.70–0.83)** after about 6 s on 272 held-out real Franka episodes. Elapsed time alone gives 0.64. It ranks nine policies with **Spearman 0.79 (CI 0.19–1.00)**. This used an **earlier, unreleased** model, and the head does not read the instruction.

### Quantization (§11)
- NVFP4 is applied to the routed experts only, with a 5k-step quantization-aware fine-tune. RoboLab-120 drops from **47.8% to 46.5%** (600 episodes), and the real YAM bag task from **28/30 to 26/30**. Neither difference is significant. **Weights shrink from 54.4 GB to 17.5 GB.**

### Limitations (§12)
- **Look-alike objects** cause the most common failure, and *the wrong choice is usually already visible in the imagined video*.
- **Vague instructions** do worse than ones that name an attribute.
- **Long tasks** work only when each step gets its own instruction. Pairing with an LLM or VLM planner is listed as future work.

## Entities mentioned

[Runway](../entities/runway.md) · [Praxis-1](../entities/praxis-1.md) · [FLUX 3](../entities/flux-3.md) · [NVIDIA Cosmos](../entities/nvidia-cosmos.md) · [NVIDIA RoboLab](../entities/nvidia-robolab.md) · [DreamZero](../entities/dreamzero.md) · [GPT-6 Astra](../entities/gpt-6-astra.md) · [RoboDojo](../entities/robodojo.md) · [DROID](../entities/droid.md) · [YAM](../entities/yam.md) · [RT-1](../entities/rt-1.md) · [SimplerEnv](../entities/simplerenv.md) · [LeRobot](../entities/lerobot.md) · [Qwen](../entities/qwen.md) · [Physical Intelligence](../entities/physical-intelligence.md) (π0.5)

## Concepts touched

[World-action model](../concepts/world-models/world-action-model.md) · [Mixture of experts](../concepts/learning/mixture-of-experts.md) · [Flow matching](../concepts/learning/flow-matching.md) · [Cross-embodiment](../concepts/learning/cross-embodiment.md) · [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) · [Scaling laws for VLAs](../concepts/learning/scaling-laws-vla.md)

## Open questions

- **Is the RoboLab lead over FLUX 3 Action real?** 46.2 vs 42.9 at n = 1,200 each gives p ≈ 0.10. The real-robot 88 vs 80 at n = 100 each gives p ≈ 0.12. Both point the same way, but neither is decisive alone, and **Runway ran both arms of the real-robot comparison**.
- **Is the RT-1 baseline fair?** FLUX 3 Action was fine-tuned with a recipe written for a different robot. The RT-1 comparison shows Praxis-1 adapts well. It does not show that FLUX 3 Action adapts badly.
- **Does compute scaling continue?** The DROID curve is flat at its last point, and the RT-1 curve is not monotonic. Five points cannot tell a slowdown from noise.
- **The oracle gap puts the bottleneck in video prediction.** Error falls fivefold when the model is given the true future. If that holds, better video models should give better policies directly. The test is whether deployment error moves toward the oracle figure as the backbone improves. Watch the next release.
- **SO-101.** A public checkpoint trained on about 1,070 hours of community SO-101 data is a large, cheap-hardware data point, but **no success rate is published**.
