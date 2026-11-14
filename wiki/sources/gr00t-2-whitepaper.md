---
title: "GR00T 2: Scaling Robot Foundation Models for Generalization, Dexterity, and Adaptation"
type: source
url: https://research.nvidia.com/labs/gear/gr00t-2/
local_path: raw/gr00t2_whitepaper.pdf
sha256: a7316845d53aa61db023de15ca4f4fad422ed071f256d9fa7e8801aa7376dd50
fetch_url: https://research.nvidia.com/labs/gear/gr00t-2/assets/gr00t2_whitepaper.pdf
author: "NVIDIA et al."
published: 2026-11-09
venue: "NVIDIA whitepaper; not peer reviewed"
format: whitepaper (135 pp; 26 pp body + appendices) plus project page
tags: [gr00t-2, world-action-model, wam, nvidia-gear, human-video, cross-embodiment, x-adapt, umi, dexumi, real-world-rl, grpo, autorl, agentic-robotics, code-as-policy, gr00t-2-turbo, sonic, jetson-thor, elo, gear-arena]
ingested: 2026-11-09
---

# GR00T 2: Scaling Robot Foundation Models for Generalization, Dexterity, and Adaptation

## Summary

**NVIDIA's GR00T line changes architecture.** GR00T 1.x was a VLM plus a flow-matching action head. [GR00T 2](../entities/nvidia-groot.md) is a [world-action model](../concepts/world-models/world-action-model.md): one 2B-parameter transformer, started from Cosmos-Predict2.5-2B, that jointly denoises future video and robot actions. It pretrains on 402,730 hours of egocentric human video, 10,184 hours of handheld UMI demonstrations and 23,500 hours of teleoperation.

The report makes four claims: strong zero-shot behaviour with fast few-shot adaptation, transfer of skills from people or handheld devices to robots that never practised them, reliability gains from real-world RL, and control by a frontier agent. A smaller variant, GR00T 2 Turbo, runs on the Jetson Thor inside a [Unitree G1](../entities/unitree-g1.md).

The evidence is unusually broad for a vendor report: real robots, named baselines, some blinded evaluation, and an explicit statement of what its sample sizes can't resolve. Several headline numbers also carry conditions that appear in the report and not in the [launch blog](nvidia-corl-2026-robotics-simulation-blog.md). They are listed below.

> [!warning] Read these conditions before quoting the headlines
> - **95% with five demonstrations is partly selected.** *"The 50 tasks were chosen among those the model learns with five episodes (at least 80% success), so the five-episode rate is high partly by construction"* (Sec. 3.1). The blog gives 71% and 95% without this.
> - **"40 of 50 tasks" is the generous form of the zero-shot result.** Trial-level success is **40%**. Forty tasks succeeded at least once, and four succeeded in every trial. The tasks are new to the target robot but appear in YAM data, human video or both.
> - **"Without robot demonstrations" still needs robot data.** Human and UMI transfer uses task-agnostic play data from the target robot to specify the body.
> - **97 or more of 100 assemblies needs three layers.** Supervised fine-tuning scores 23–69, adding DAgger scores 71–84, and adding the agent reaches 97–98. The agent uses per-task recovery skills such as `flip_tractor`.
> - **Truck assembly's 65% used easier scenes.** GR00T 2 and Turbo ran on a revised, easier set of start scenes. On the original scenes GR00T 2 succeeds in 7 of 20, which is 35% (Table 1 caption).

## Key claims

### Model (Sec. 2, 4.1)

- **Inputs and outputs.** 0.8 s of history from up to four cameras at 224×320 and 5 fps, robot state and an instruction go in. An action chunk and predicted future frames for every camera come out.
- **Backbone.** Cosmos-Predict2.5-2B, a frozen Wan 2.1 VAE and a frozen Cosmos-Reason1 text encoder. Small per-embodiment MLPs handle state and action. Action tokens attend to all video tokens, including the future frames being generated.
- **Three-stage pretraining.** Single-view video, then multi-view joint video-action, then a robot-upweighted stage. It used 1,024 GB300 GPUs (Sec. 4.7).
- **Turbo.** The same 2B transformer with a higher-compression Wan 2.2 VAE and a 4× smaller spatial latent grid. It loses 6.7 points on YAM after post-training and half its success on dexterous hands, 68.6% to 34.3%.

### Data (Sec. 4.2)

| Source | Scale | Role |
|---|---|---|
| [Human-1M](../entities/human-1m.md), filtered | 402,730 h, about 13.75M episodes, 51,500+ collectors | Coverage of objects, scenes and interactions |
| Robot-aligned studio human data | 3,000 h | Matches robot viewpoints and speed |
| UMI-10K | 10,184 h, 942k episodes, 2,897 tasks | Task-focused, robot-compatible actions |
| Teleoperation | 23.5k h, 1.16M episodes | YAM 18.7k h, Sharpa 2.9k h, Wuji 1.3k h, G1 275 h, DROID Franka |

**Human-video scaling (Fig. 10).** With the same post-training robot data, real-robot success on 72 Dexter tasks rises from 18% with no human video to 41% with all of it, and task progress rises from 50% to 70%. Nothing levels off at 100%. This is 3 rollouts per task, a vision-language model scores progress, and the 0%→1% step also includes a shared pretraining stage.

### Capabilities (Sec. 3)

| Claim | Result | Conditions |
|---|---|---|
| Zero-shot, Dexter-50 | 40% of trials | Selected tasks; see warning |
| Few-shot, Dexter-50 | 71% with 1 demo, 95% with 5 | About 30 min LoRA on one RTX 5090; selected tasks |
| Zero-shot, all 71 Dexter tasks | 49.8% vs π0.5 26.3%, GR00T 1.7 18.3% | 3 trials per task; blinded operator |
| YAM long-horizon, 6 tasks | 71.7% vs at most 12.5% for baselines | Up to 20 trials per task |
| Dexterous long-horizon, 7 tasks | 68.6% vs at most 0.7% | Truck scenes differ, see warning |
| Human demos to Sharpa hands, no teleop | 65%, 30%, 10%, 50% on four tasks | 20 trials per task; needs play data |
| UMI to YAM, no teleop | Truck 60%, NIST board 50%, conveyor 86% of items | 41–75 demos per task |
| Real-world RL, four contact-rich tasks | 88–98% vs 40–76% after fine-tuning | The 88–98% is self-imitation on GRPO's successes. GRPO alone gives 72–94%, and only 2 of its 4 gains are significant (F.4) |
| Visual steering, YAM | 92% vs 40% on what-and-where instructions | Marks don't convey pouring, wiping or final orientation |
| Turbo on G1, four tasks | 80.8% average vs GR00T 1.7 at 62.5% | Popcorn 48/48; spill clean-up only 46.7% |
| Adding simulated data, G1 | 6.7% to 63.3%; GR00T 1.7 reaches 40% | 30 trials each |

**Latency (Sec. 2, 3.5, 4.6).** GR00T 2 takes a median 153 ms per Dexter action chunk on an RTX 5090. Turbo takes 38 ms on a 5090 and **124 ms on the G1's Jetson Thor**, planning 1.6 s chunks about once a second. SONIC runs at 50 Hz on a Jetson Orin NX.

> [!warning] These latencies measure different things (Sec. I.1, Tab. 27, D.6)
> - **153 ms excludes image encoding.** On Dexter and YAM, the optimized timings leave out VAE encoding done before the request ("prefetch"). The G1 timings include it.
> - **The 38 ms and 124 ms are the G1 checkpoint with fewer denoising steps** (1 video + 2 action steps, down from 2 + 4) and FP8. The unoptimized Thor baseline is 720 ms, and the Thor runs in its 120 W mode.
> - **In real A/B serving logs, the Turbo reference took 187 ms** of server compute per call (Fig. 38). Fig. 23 gives 52 ms against 171 ms for GR00T 2 on YAM. The report says these figures aren't comparable with each other.

### Agentic control (Sec. 3.4, G)

The agent is a separate "System 2" reached through MCP tools such as `wam_act` and `stop_wam`. It does four jobs: run programs that call GR00T 2, repair the scene when GR00T 2 stalls, steer it with image-space marks, and improve it. The improvement case is **AutoRL, a research agent that iterated for about 35 days and found the basis of the RL recipe** (Sec. 4.1, F.2).

Recovery skills come from [ASPIRE](../entities/aspire.md). The steering experiments use GPT-6 Astra as the agent (Sec. G.2).

### Benchmarks (Sec. 4.5.4, J.3)

| Benchmark | GR00T 2, no agent | Standing | With RL and agent |
|---|---|---|---|
| RoboCasa365 | 67.2% | First among VLA and WAM, 2.8 points ahead | 88.0%, first overall |
| [RoboDojo](../entities/robodojo.md) | 35.5% | First, but 0.5 points ahead of WALL-OSS at 34.97% | 75.8%, first overall on one of three layout banks |
| RoboLab | 47.4% | Third | Not reported |
| MolmoSpaces | 45.1% | Second | Not reported |
| G1 Factory | 84.7% | GR00T 1.7 scores 69.4% | Not reported |

Baselines are taken from public leaderboards as of 2026-11-06, except GR00T 1.7, which NVIDIA retrained itself. In the agentic rows, each task's default executor is chosen on development seeds disjoint from test seeds.

### Evaluation method (Sec. 4.3, 5, D)

**GearArena** rates checkpoints with blinded A/B matches on real robots: 195 campaigns, 16,044 graded episodes, 11,767 pairwise comparisons, 71 checkpoints, 10 YAM stations. GR00T 2 leads π0.5 by 236 Elo (95% CI 171–325) and GR00T 1.7 by 95 Elo (50–148).

The authors limit their own evidence. Twenty trials per task can't resolve deployment-relevant gaps: separating 95% from 99% takes about 285 trials per policy. Independent units are tasks, not trials, and 30–35% of comparisons are ties. Elo is relative to one suite, and the arena is NVIDIA's own, on the robot with the most training data.

Simulated evaluation tracks real results on 25 YAM tasks and 14 checkpoints (Pearson 0.92 on success, 0.93 on Elo). The authors say it remains to be shown for contact-rich assembly.

### Stated open problems (Sec. 5)

- What to predict, at what resolution and horizon. Whether prediction helps mainly as a training signal or also at inference is unknown.
- Memory. GR00T 2 sees 0.8 s of history and delegates memory to the agent.
- Force and touch as inputs. Force is only an output today.
- No exchange rate between human video, UMI, teleoperation and simulation data.

## Appendix detail (A–K, read in full 2026-11-13)

The appendices run from page 38 to 135. The items below add to or qualify the body claims above. Tables 2 and 3 were checked against the rendered pages, because text extraction reorders their columns.

### Zero-shot and few-shot (A)

- **The zero-shot lead is in harder motions, not language.** On YAM V2 (Tab. 2), GR00T 1.7 matches GR00T 2 on language following (progress 47.7 vs 45.2; success 30.4 vs 31.4). The gap is on medium and hard motion primitives, with 29.9% success against 5.4%. GearArena's matched rubric scores show the same split (Tab. 14).
- **Turbo trails on Dexter zero-shot**, 36.6% against GR00T 2's 49.8% (Tab. 3). Operators were blind to the model.
- **The few-shot recipe** is rank-32 LoRA on every transformer linear layer. Training windows are sampled in proportion to the frozen model's loss, so updates concentrate on hard phases such as grasping. It uses one set of hyperparameters and is merged back into the weights after training.

### Learning from people and handheld devices (B, E)

| Setting | Result | Baselines | What it needs |
|---|---|---|---|
| Human gloves to Tianji + Sharpa hands, 4 tasks | 65, 30, 10, 50% (20 trials) | GR00T 1.7 and target-only pretraining fail every lab task | 100 human demos per task, plus robot play data mixed 1:1 |
| Same, plus 10 teleop demos | 95, 70, 50% on the lab tasks | 45, 40, 30% without cross-embodiment pretraining | — |
| DexUMI exoskeleton to XHAND, 3 tasks | 60, 80, 75% | π0.5 and GR00T 1.7 complete no trials | Exoskeleton demos only |
| DexUMI to a Sharpa hand it doesn't replicate | 60, 65% | 0% | Fingertip retargeting, wrist-view reprojection, play data |
| One human video to sim to real (V2D + CHORD) | Hammer nail 9/10, sweep 8/10, flask handover 2/10 | 0/10 for both | 1.5k sim episodes per task from an RL expert |
| UMI to the matching robot gripper, 4 assemblies | 35% average (progress 79–94) | 2.5% without UMI in pretraining | 3–5 h of UMI per task |

- **A same-data VLA comparison exists for these tasks.** B.1.5 describes GR00T 1.7 as "a VLA pretrained on the same data and post-trained with the same recipe." The backbone and initialization differ, so it tests the WAM design as a whole, on four tasks.
- **The model predicts the robot's hands for tasks only people showed it** (Fig. 28). This is evidence that video prediction separates what should happen from which body does it.
- **Human demos remove teleop's speed ceiling.** The conveyor toss is a timed throw that can't be teleoperated, and it reaches 50% from human data alone.
- **For UMI to YAM, wrist-camera geometry is the deciding factor** (Tab. 17). Without re-rendering UMI's fisheye as YAM's pinhole view, long-horizon success drops to 0%, though task progress stays at 76–79. Rough agreement in field of view and viewing direction is enough. Appearance (human arms, a blue handheld gripper) transfers without editing.
- **A task's hardest subskill sets how much data it needs.** Halving the NIST board demos takes it from 50% to 0%, because one nut-removal step disappears. The conveyor task keeps 70% of items sorted with a quarter of the data.
- **The "without UMI pretraining" baseline is confounded.** It comes from an earlier run with fewer samples, a different robot mixture and small model differences (E.2).
- **Force for dexterous hands** uses Adaptive Compliance Policy in joint space. Fingertip forces are projected to joint torques, and stiffness drops to 0.3× as torque rises from 0.1 to 0.4 N·m.
- **Hardware.** The Gripper UMI uses a 3D-printed TPU flexure linkage instead of pins and springs, with an encoder for width. GEAR DexUMI has 16 DoF, matches the XHAND's tactile format with 30 channels per hand, and is anodized green so it can be masked during training.

### Data (C)

- **Human-1M** has about 1M hours, of which 402,730 are used. About 80,000 h is studio data, about 90,000 h includes wrist cameras, and about 3,000 h is "in-lab" data recorded to match the robot's viewpoint and speed.
- **Timesteps are filtered automatically** on head speed, hand visibility, bone-length consistency and wrist speed (Tab. 8).
- **Human-video scaling with intervals (C.1.5).** All versus none adds 23.1 points of robot success (95% CI 13.4–33.3, paired over tasks). The 1%→10% step is within noise on the robot. Each data share is one training run.
- **UMI-10K** has no task above 1.2% of hours. 88% of episodes go beyond pick-and-place, and quality control removes about a quarter of recorded episodes.
- **Mixture weights favour dexterous data.** Sharpa and Wuji hold 18% of robot hours but get 35% of samples. YAM holds 64% of hours and gets 51%.
- **Flora**, NVIDIA's annotation model set, relabels the 400k human hours in about two days.

### GearArena (D)

- **Bradley–Terry ratings with per-pair task normalization** and a bootstrap that resamples tasks rather than trials. Re-deriving weights inside each resample avoided intervals about 30% too narrow.
- **GR00T 2 Turbo leads the YAM V2 board.** It is statistically indistinguishable from GR00T 2: −14 Elo [−58, +28], P(GR00T 2 better) = 0.28. Turbo trails on dexterous post-training (above), so its standing depends on the evaluation.
- **Serving settings can reorder the board.** On the dexterous suite, a new inference regime moved the previous leader from first of 13 to fifth of 9. Inference settings are therefore part of each entry's identity.
- **One campaign is withheld** because its operator could see the checkpoint labels. The GR00T 1.7 and π0.5 comparisons rest on campaigns from the last week before the snapshot.
- **176 of 253 checkpoint pairs** are resolved at 95%. The median interval is 93 Elo wide.

### RL post-training (F)

- **Real robot, 50 trials per task.** GRPO raises success from 66, 58, 76 and 40% to 86, 72, 92 and 94%. One round of self-imitation on GRPO's successes gives 88, 98, 94 and 96%. Residual RL, which leaves GR00T 2 frozen, gives 76, 84, 82 and 70%.
- **The GRPO baseline remembers each context.** A per-context running average enters the leave-one-out baseline, so groups that all succeed or all fail still produce a learning signal.
- **AutoRL ran on simulated RoboCasa365 with an early checkpoint** and gained 10 points. Its stage-progress rewards are simulation-only. Real robots use binary success.
- **Neural-simulation RL in DreamDojo** needs about 300 physical rollouts per task to adapt the world model, and a learned success detector provides the reward. RoboLab success rises from 51.3% to 70.9% over 5,000 episodes, and four real tasks rise from 42.5% to 71.7% (60 trials each). Each configuration is one run, and the hardware-sorting SFT and RL trials were collected in separate batches.
- **Infrastructure halves real-robot iteration time**, from 140–160 min to 62–72 min, mostly by removing upload and download.

### Agents (G)

- **Who runs the simulated benchmarks.** Agent-selected programs, not GR00T 2, are the default executor on 27 of 50 RoboCasa365 tasks and 42 of 54 RoboDojo configurations. The agent intervenes in 37% of RoboDojo episodes and 40% of RoboCasa365 episodes. Those interventions succeed 24% and 56% of the time (Tab. 20).
- **Memory comes from the agent.** RoboDojo Memory success rises from 36.0% to 93.7% with it.
- **Real assembly failures with the agent were 8 of 300.** They were incomplete fastening, interventions too late to reverse, and a dropped or jammed screw.
- **Steering cost on trash sorting:** a median of 9 agent turns per episode costing $0.26 on YAM, with the robot idle for 38% of the episode. Steering moves one arm per step, so it can't coordinate two-arm motion. The Dexter steering numbers use "an earlier implementation of the model" (Tab. 22).

### Humanoid (H)

- **Turbo outputs SONIC tokens at 1 Hz, as 1.6 s chunks** that SONIC samples at 50 Hz. Teleoperation records directly in this token space.
- **Synthetic data came from fitting scenes to recorded motion.** CMA-ES fits table and object poses to recorded G1 motions, keeping a fit only if the object survives a pull equal to its weight. The result is 250,000 episodes, about 1,000 h.
- **The sim-data advantage over the VLA is suggestive.** Out of distribution, 19 vs 12 of 30 trials, Fisher p ≈ 0.12. π0.5 *gets worse* in distribution with sim data, falling from 40% to 16.7%.

### Speed and smoothness (I)

- **Noisy-prefix real-time chunking** adds noise to the prefix of committed actions during fine-tuning. At 320 ms of delay, success rises from 15.0% to 21.4% and 95th-percentile jerk falls by 87%.
- **Phase-dependent speed-up** cuts completion time on three Dexter tasks by 15–26%. Success is within ±5 points.

### Simulation (J)

- **The sim–real correlation is reported against a noise ceiling**: the best correlation a perfect simulator could reach with the same trial counts. YAM's r = 0.92–0.93 is 95–99% of that ceiling. On DROID, r = 0.95–0.98 over only five checkpoints.
- **Simulation chose the final checkpoint.** It narrowed the candidates to three, then real robots decided.
- **The assembly scenes run in Isaac Lab Arena** on [Newton](../entities/newton-physics-engine.md) with the MuJoCo Warp solver. Coarse colliders handle grasping and SDF colliders handle threading. An extension joins parts once they are seated.
- **RoboLab and MolmoSpaces are zero-shot real-to-sim.** The checkpoint is post-trained on real DROID data only. Its weakest MolmoSpaces suite uses randomized cameras, at 20.3%.

### Infrastructure (K)

- **The cluster has 2,016 GB300 GPUs in 28 NVL72 racks**, and the main run used 1,024. The model fits without pipeline parallelism, so training is data-parallel with DeepSpeed ZeRO-2.
- **The training mixture** is 25 versioned datasets in Lance (LanceDS), with 15.6M episodes and 46.2B timesteps. The data loader waits 0.049% of step time.
- **Orchestration** uses Kubernetes, SkyPilot and Ray. Evaluation runs on L40/L40S GPUs and data processing on RTX PRO 6000s. Ingestion handles 722–780 demonstration-hours per hour on 100 CPU nodes.

## Project page

The [project page](https://research.nvidia.com/labs/gear/gr00t-2/) says **"Code Available in December."** It links the open [Human-1M-100K](https://huggingface.co/datasets/nvidia/PhysicalAI-Human-1M-100K) dataset. No weights link or licence was found on 2026-11-09, so "open" in the blog is a statement of intent for the model.

It is a summary of this report and matches it where checked. It omits the selection note, the truck-scene note and the trial limits.

## Entities mentioned

- [NVIDIA GR00T](../entities/nvidia-groot.md), [NVIDIA GEAR](../entities/nvidia-gear.md), [NVIDIA Cosmos](../entities/nvidia-cosmos.md)
- [Human-1M](../entities/human-1m.md), [UMI](../entities/umi.md), [ASPIRE](../entities/aspire.md), [GEAR-SONIC](../entities/gear-sonic.md)
- [YAM](../entities/yam.md), [Unitree G1](../entities/unitree-g1.md), [Jetson Thor](../entities/jetson-thor.md)
- [RoboDojo](../entities/robodojo.md), [π0.5](../entities/pi-zero-5.md), [MolmoAct2](../entities/molmoact2.md), [FLUX 3](../entities/flux-3.md), [DreamDojo](dreamdojo-paper.md)

## Concepts touched

- [World-action model](../concepts/world-models/world-action-model.md) — a flagship foundation model moves to this architecture.
- [Scaling laws for VLAs](../concepts/learning/scaling-laws-vla.md) — a controlled human-video scaling ablation.
- [Code as policy](../concepts/agents/code-as-policy.md) — agent as supervisor of a learned skill model.
- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md) — GRPO-induced self-imitation on a world-action model.

## Open questions

- **Will weights ship under the same licence as GR00T 1.7?** Code is promised for December.
- **How much does the WAM architecture itself contribute?** The report changes the architecture, the data and the recipe together. A same-data GR00T 1.7 appears only for the four human-to-robot tasks (B.1.5), and there it also differs in backbone and initialization. No clean single-variable test exists.
- **Is Turbo better or worse than GR00T 2?** It leads the zero-shot A/B board but loses up to half its success on dexterous post-training. Which one to deploy depends on the task, and no single figure answers it.
- **Are the 50-task results reproducible on unselected tasks?** The zero-shot suite of 71 is the less selected number, and it reports no few-shot rate.
- **Independent replication.** Every real-robot result is NVIDIA's own.
