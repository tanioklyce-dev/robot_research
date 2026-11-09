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
| Real-world RL, four contact-rich tasks | 88–98% vs 40–76% after fine-tuning | 50 trials per bar, Wilson intervals |
| Visual steering, YAM | 92% vs 40% on what-and-where instructions | Marks don't convey pouring, wiping or final orientation |
| Turbo on G1, four tasks | 80.8% average vs GR00T 1.7 at 62.5% | Popcorn 48/48; spill clean-up only 46.7% |
| Adding simulated data, G1 | 6.7% to 63.3%; GR00T 1.7 reaches 40% | 30 trials each |

**Latency (Sec. 2, 3.5, 4.6).** GR00T 2 takes a median 153 ms per Dexter action chunk on an RTX 5090. Turbo takes 38 ms on a 5090 and **124 ms on the G1's Jetson Thor**, planning 1.6 s chunks about once a second. SONIC runs at 50 Hz on a Jetson Orin NX.

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
- **How much does the WAM architecture itself contribute?** The report changes the architecture, the data and the recipe together. GR00T 1.7 trained on the same mixture isn't reported.
- **Are the 50-task results reproducible on unselected tasks?** The zero-shot suite of 71 is the less selected number, and it reports no few-shot rate.
- **Independent replication.** Every real-robot result is NVIDIA's own.
