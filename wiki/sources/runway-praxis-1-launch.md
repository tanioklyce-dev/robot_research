---
title: "Praxis-1 Is Now Available — Runway (November 2026)"
type: source
url: https://runway.com/news/company-news/praxis-1-is-now-available
fetch_url: https://runway.com/news/company-news/praxis-1-is-now-available
local_path: raw/2026-11-11-runway-praxis-1-launch.md
sha256: 4cd60ba3b8678aaea60a391f7e76cc09a25f6d721bf1ac21d7b5976cf60895c9
author: Runway
published: 2026-11-11
venue: "Runway company news. The raw file also holds the September research post it follows, *Introducing Praxis-1* (runway.com/research/introducing-praxis-1)."
format: vendor announcement (~650 words), plus the ~1,100-word September pre-announcement
license: "Model, inference code and fine-tuning code: Apache-2.0"
tags: [praxis-1, runway, world-action-model, open-weights, apache-2, robolab, flux-3, cosmos, lerobot, jetson-thor, video-pretraining, cosmos-coalition, standard-bots]
ingested: 2026-11-12
---

## Summary

**A video-generation company has released an open-weight world-action model under Apache 2.0, and claims it is the best one on NVIDIA's RoboLab-120 benchmark.** Runway first announced [Praxis-1](../entities/praxis-1.md) in September 2026 as a partner-only preview. With this launch the weights, inference code and fine-tuning code (full and LoRA) are open for commercial use. They are on GitHub, on Hugging Face with LeRobot support, and in vLLM-Omni, and Runway also offers hosted inference. The model is a **27B mixture-of-experts diffusion transformer that predicts video and actions together**. It scores **46.2% on RoboLab-120** over 1,200 episodes, ahead of FLUX 3 Action (42.9%), Cosmos3 Nano (36.8%) and π0.5 (28.0%). The September post's argument is that general video is effectively unlimited while teleoperation is not, and that **policy quality grows with the amount of third-person video**. The detail behind these claims is in the [technical report](runway-praxis-1-technical-report.md), and the hardware facts are in the [GitHub README](praxis-1-oss-github.md). Both are more cautious than this post.

## Key claims

**Launch (2026-11-11)**
- **Model.** A 27B-parameter MoE diffusion transformer that predicts video and actions jointly. It is built on the same video pretraining as Runway's general world models.
- **Benchmark.** **#1 world-action model** on [RoboLab-120](../entities/nvidia-robolab.md) at 46.2% over 1,200 episodes, and better than every open-weight VLA. Other scores given: FLUX 3 Action 42.9%, Cosmos3 Nano 36.8%, π0.5 28.0%, all "as of November 2026".
- **Release.** Weights, inference code and fine-tuning code (full fine-tuning and LoRA) are released under **Apache 2.0**, including for commercial use. Distribution is through GitHub, Hugging Face with native [LeRobot](../entities/lerobot.md) support, vLLM-Omni, hosted inference on "Reactor", Runway Dev, and NeMo Automodel post-training tutorials.
- **Hardware.** The post says it *"runs out of the box"* on H100 and B200, on RTX 5090 and RTX PRO 6000, and on [Jetson Thor](../entities/jetson-thor.md). See the warning below.
- **New embodiment.** Fine-tuned on Google's [RT-1](../entities/rt-1.md) robot, which never appeared in its training data, it reaches **80.0% on [SimplerEnv](../entities/simplerenv.md)** against 52.4% for the original RT-1 policy.
- **Pretraining data.** *"Our research has shown that web video matches teleoperated robot video as pretraining data for policy performance."*
- **Partners.** Noble Machines (legged humanoid), [Standard Bots](../entities/standard-bots.md) (six-axis industrial arm) and Ultra (dual-arm warehouse robot) ran it on their own hardware.
- **Policy framing.** The case for open weights is put in terms of US leadership in physical AI. Runway calls itself a **founding member of the Cosmos Coalition** with [NVIDIA](../entities/nvidia.md) (see [NVIDIA Cosmos](../entities/nvidia-cosmos.md)).

**September pre-announcement (*Introducing Praxis-1*)**
- **Policy evaluation.** *"Simulating robot policies inside our world model predicts real-world results with **0.95 correlation**."* The details are in a separate Runway post, *Accelerating Robot Policy Evaluation with General World Models*, which is not ingested.
- **Scaling.** *"Policy performance improves as we scale third-person video."* Figure 2 shows final placement error after fine-tuning against hours of pretraining video. **Web video from scratch reaches 16.1 cm, teleoperated robot video 16.0 cm** (±1 SEM over 93 evaluation pairs, with the x-axis running 10¹–10³ hours).
- **Hard cases.** Four kinds of task that defeat demonstration-only policies are shown as targets: rigid repeated objects, clutter, transparent objects and deformable objects. These are shown as video only, with no numbers.

## Where the launch post goes past its own primary

> [!warning] Three claims that the technical report and README qualify
> - **"#1" covers part of the board, not all of it.** The report names four entries above Praxis-1 on RoboLab-120: AMP1 (86.0%, a zero-shot frontier-model agent), SenseNova-RoboRSI (57.1%), Lakeside (51.0%) and BiMind v0.5 (49.2%). The claim is #1 *among WAMs and among open-source robot foundation models*.
> - **"Web video matches teleop" rests on one proxy.** The evidence is a placement-error tie (16.1 vs 16.0 cm) on one evaluation of 93 pairs, from a September figure, not policy success rates. The launch post turns this into a claim about *"policy performance"*. This is the same scope loss described in the [JetPack 7.2 correction](../log.md).
> - **"Runs out of the box" on RTX 5090 and Jetson Thor.** The [README](praxis-1-oss-github.md) asks for **one GPU with at least 80 GB** for the quick start. RTX 5090 support depends on the opt-in NVFP4 checkpoints, where the README says a 32 GB card *"should fit (the peak is not measured yet)"*. Thor has its own NVFP4 code path, but the README excerpts read here give no Thor latency figure.

> [!note] The headline gap over FLUX 3 Action is not statistically separable
> 46.2% vs 42.9% at 1,200 episodes each is a 3.3-point difference. A two-proportion test gives z ≈ 1.6 and p ≈ 0.10. Praxis-1 clearly beats Cosmos3 Nano (+9.4 pp) and π0.5. Its lead over FLUX 3 Action is within noise.

## Entities mentioned

[Runway](../entities/runway.md) · [Praxis-1](../entities/praxis-1.md) · [FLUX 3](../entities/flux-3.md) · [NVIDIA Cosmos](../entities/nvidia-cosmos.md) · [NVIDIA RoboLab](../entities/nvidia-robolab.md) · [NVIDIA](../entities/nvidia.md) · [Physical Intelligence](../entities/physical-intelligence.md) (π0.5) · [RT-1](../entities/rt-1.md) · [SimplerEnv](../entities/simplerenv.md) · [LeRobot](../entities/lerobot.md) · [Jetson Thor](../entities/jetson-thor.md) · [Standard Bots](../entities/standard-bots.md)

## Concepts touched

[World-action model](../concepts/world-models/world-action-model.md) · [Mixture of experts](../concepts/learning/mixture-of-experts.md) · [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md)

## Open questions

- **The 0.95 sim-to-real correlation.** How many policies, which tasks, and is it rank or Pearson? Ingest *Accelerating Robot Policy Evaluation with General World Models* before quoting it.
- **The Cosmos Coalition.** What does founding membership involve, and does Praxis-1 use any Cosmos components? The technical report names Wan2.2's VAE and Qwen3.5 as its frozen encoders, not Cosmos.
- **Partner results.** Noble Machines, Standard Bots and Ultra appear only in video. No partner success rates are published.
