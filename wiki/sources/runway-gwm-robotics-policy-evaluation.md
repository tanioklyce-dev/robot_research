---
title: "Accelerating Robot Policy Evaluation with General World Models — Runway (February 2026)"
type: source
url: https://runway.com/research/accelerating-robot-policy-evaluation
fetch_url: https://runway.com/research/accelerating-robot-policy-evaluation
local_path: raw/2026-02-27-runway-accelerating-robot-policy-evaluation.md
sha256: 5c68834942e0d273e4cd9ef70d21a674c81252c4209fbe698f67b58ff43a404f
author: "Runway Robotics (Andy Chen, Lucas Eager Leavitt, Rik Heijdens, Robin Kahlow)"
published: 2026-02-27
venue: "Runway Research blog. Compares against PolaRiS (arXiv 2512.16881)."
format: "research blog post, about 1,000 words, with one correlation chart (per-policy values not in the text)"
tags: [runway, gwm-robotics, world-model, policy-evaluation, roboarena, polaris, veo, sim-to-real-correlation, mmrv, human-grading, gen-4-5, franka, droid, pi-zero-5, paligemma]
ingested: 2026-11-12
---

## Summary

**The source of the "0.95 correlation" claim in the [Praxis-1](runway-praxis-1-launch.md) announcement, and it is narrower than that line makes it sound.** Runway ran **eight DROID-trained VLA policies** from the [RoboArena](../entities/roboarena.md) dataset inside **GWM-Robotics**, a variant of its Gen-4.5 video model. Each policy acted on the world model's generated frames, starting from the initial conditions of real RoboArena episodes. **Human graders** then scored task progress on **1,450 simulated rollouts**, with about 10 graders per rollout and over 16,000 ratings in total. Per-policy simulated progress correlates with real-world progress at **Pearson 0.95** and **MMRV 0.033**. The best policy (pi05_droid) and the worst (paligemma_binning_droid) were identified correctly. The post states its own scope clearly: it **validates ranking, not absolute success rates**, on **one arm (Franka Panda), tabletop tasks only**. It is one more instance of the pattern on the [policy-evaluation page](../concepts/robotics/robot-policy-evaluation.md#the-sixth-paradigm-a-task-reconstructed-simulator-as-the-screening-layer): **ranking transfers, magnitude does not**.

## Key claims

- **Setup.** Eight VLA policies, all on a Franka Panda, run on RoboArena tasks. GWM-Robotics simulates each policy *"from the same initial conditions, with each policy generating its own actions in response to observations produced by the world model"*. GWM-Robotics was announced in December 2025. It needs **only starting images** as input and generates **rollouts of up to 30 s in real time**.
- **Scoring.** Human graders rated progress on 1,450 simulated rollouts (more than 16,000 ratings, about 10 per rollout). These were compared with the real-world progress scores in RoboArena.
- **Result.** **Pearson 0.95 and MMRV 0.033** across eight policies. pi05_droid ranked best and paligemma_binning_droid worst, matching the real ranking. The middle six showed *"only minor rank inversions between similarly performing models"*.
- **Against PolaRiS.** PolaRiS is a real-to-sim framework that rebuilds each scene with 3D Gaussian splatting, which requires scanning, reconstruction and manual object setup. On the subset of policy architectures PolaRiS also evaluated, GWM-Robotics scores **Pearson 0.986 and MMRV 0**, against **0.98 with perfect ordering** for PolaRiS.
- **Against Veo Robotics.** The post says Veo's simulator is limited to **8-second rollouts**, against 30 s for GWM-Robotics. This is Runway's description of a competitor.
- **Limitations stated by Runway.** The results show ranking only, *"rather than absolute success-rate prediction"*. Evaluation covered one embodiment, although the model was trained on several.
- **Training data and partners.** GWM-Robotics is *"trained on real-world video, including physical AI datasets from NVIDIA"* and fine-tuned on robot proprioceptive state. Partners named are **NVIDIA and Berkshire Grey**. Access is by request.

## Reading the numbers

> [!note] How much eight points can show
> A Pearson r of 0.95 over **n = 8** has a 95% confidence interval of about **0.74–0.99** (Fisher z). The PolaRiS comparison, 0.986 vs 0.98, is on an unstated smaller subset and is **within noise**. "Surpassing PolaRiS" should be read as "matching PolaRiS without per-scene reconstruction". That is the real advantage, and it is about cost, not accuracy.

- **People still do the scoring.** The world model replaces the robot and the lab, but not the evaluator: every simulated rollout was scored by about ten humans. Graded video is still cheaper than running hardware, but this is not yet the automatic screening loop that the [R2S2R](../concepts/robotics/real-to-sim-to-real.md) framing describes. Praxis-1's later success-prediction head (AUROC 0.77, [report §10.3](runway-praxis-1-technical-report.md)) is a step toward taking humans out of the scoring.
- **The ground truth is also human-graded.** RoboArena's real-world progress scores come from human evaluators, and RoboArena itself reports about **r ≈ 0.95** against oracle rankings ([RoboArena](../entities/roboarena.md)). A simulated evaluator that matches the real one at 0.95 may be close to the precision of the real protocol itself.
- **Possible overlap with training data, not addressed.** The initial frames come from RoboArena episodes on DROID-style setups. The post does not say whether DROID or RoboArena video was in GWM-Robotics' training mix. If it was, the model may be recalling scenes rather than generalizing to them.
- **Naming.** The chart caption says "GWM-1" while the text says GWM-Robotics. They appear to be the same model.

## Entities mentioned

[Runway](../entities/runway.md) · [RoboArena](../entities/roboarena.md) · [π0.5](../entities/pi-zero-5.md) · [PaliGemma](../entities/paligemma.md) · [Veo](../entities/veo.md) · [DROID](../entities/droid.md) · [NVIDIA](../entities/nvidia.md)

## Concepts touched

[Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) · [World-model simulators](../concepts/world-models/world-model-simulators.md) · [Real-to-sim-to-real](../concepts/robotics/real-to-sim-to-real.md)

## Open questions

- **Per-policy values.** These are in the chart image only, not in the text. Which of the eight policies are in the PolaRiS subset?
- **Training overlap** of GWM-Robotics with DROID or RoboArena (see above).
- **Can a VLM grader replace the human graders** without losing the correlation? That decides whether this is an automated evaluator or a cheaper form of crowdsourcing.
- **Absolute calibration.** Runway calls this "an active area of work". No follow-up has been ingested.
