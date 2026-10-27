---
title: "World Action Models are Zero-shot Policies (DreamZero) (Ye, Ge, Zheng, Gao, Yu, …, Zhu, Fan, Jang, 2026)"
type: source
url: https://arxiv.org/abs/2602.15922
fetch_url: https://arxiv.org/pdf/2602.15922v1
local_path: raw/2602.15922v1.pdf
sha256: cb91d24a04717a6c77fd39594af7f3f85a05317b7078b0d9c8d8b4ddd932f483
author: Seonghyeon Ye, Yunhao Ge, Kaiyuan Zheng, Shenyuan Gao, Sihyun Yu, George Kurian, Suneel Indupuru, You Liang Tan, …, Guanzhi Wang, Dantong Niu, Ruijie Zheng, Danfei Xu, Yilun Du, Yevgen Chebotar, Scott Reed, Jan Kautz, Yuke Zhu, Linxi "Jim" Fan, Joel Jang
published: 2026-02-17
ingested: 2026-10-27
venue: arXiv (cs.RO), v1
format: "paper, 36 pp (19 main + appendices A–H). NVIDIA. Project leads: Seonghyeon Ye, Yuke Zhu, Jim Fan, Joel Jang. Project: dreamzero0.github.io (not inspected). Code: github.com/dreamzero0/dreamzero (weights, inference code, RoboArena / PolaRiS / Genie Sim 3.0 eval code)."
tags: [dreamzero, world-action-model, wam, nvidia-gear, wan2-1, video-diffusion, autoregressive, flow-matching, inverse-dynamics, agibot-g1, droid, franka, yam, cross-embodiment, egocentric-human-data, data-diversity, real-time-inference, gb200, nvfp4, open-weights]
---

# World Action Models are Zero-shot Policies (DreamZero) (2026-02-17)

## Summary

[DreamZero](../entities/dreamzero.md) is [NVIDIA GEAR](../entities/nvidia-gear.md)'s **14B [world-action model](../concepts/world-models/world-action-model.md)**. It is built by fine-tuning the **Wan2.1-I2V-14B** image-to-video diffusion model to predict **future video and actions jointly**, adding only state/action encoders and an action decoder. The model is **autoregressive over 1.6 s chunks**, is trained with teacher forcing, and shares one flow-matching timestep between video and action. In closed loop, **real observations replace the predicted frames in the KV cache** after each chunk, which stops errors from compounding. The paper's thesis is that a WAM turns action learning into **inverse dynamics on imagined video**. That lets it learn from **diverse, non-repetitive data**: ~500 h of AgiBot G1 teleop across 22 real environments, with a deprecate-each-task-after-50-episodes collection rule. Evaluated in unseen environments with unseen objects, it reaches **62.2% task progress on seen tasks** against 27.4% for the best *pretrained* VLA, and **39.5% on 10 unseen tasks** against 16.3%. VLAs trained from scratch on the same data stay near 0. A stack of system, kernel and model optimisations, including **DreamZero-Flash** (decoupled noise schedules), gives a **38× speedup**, from 5.7 s to 150 ms per chunk, so the model runs at **~7 Hz on 2 GB200s**. Cross-embodiment results: 10–20 minutes of **video-only** YAM or human demos lift unseen-task progress from 38.3% to 55.4% / 54.3%, and **30 minutes of YAM play data** adapts the AgiBot-pretrained model to a new robot.

## Key claims

**Formulation and architecture (§3.1, App. C)**
- Joint prediction factors as autoregressive video prediction × an **inverse-dynamics model** on the predicted frames (Eq. 1). DreamZero learns both in one network rather than two, which it argues gives tighter video–action alignment.
- Backbone: Wan2.1-I2V-14B-480P. Trainable parts are all DiT blocks plus the state encoder, action encoder and action decoder. **Text encoder, image encoder and VAE are frozen.** LoRA "led to suboptimal results". Multi-view input is concatenated into one frame, with no architectural change (§3.1, §4.1).
- **Shared denoising timestep for video and action**, chosen for faster early convergence. The paper says this is unlike other recent WAMs (§3.1).
- Chunk = K = 2 latent frames. Video runs at 5 FPS; actions at 30 Hz (AgiBot, H = 48) or 15 Hz (DROID, H = 24), so each chunk spans 1.6 s. Maximum context is 4 chunks = **6.6 s** of video (App. C). The paper calls the visual memory "short-horizon".
- **Autoregressive vs bidirectional** (App. B, Table 4): equal task progress (50% vs 50%). AR gives smoother motion, **3–4× faster** inference via the KV cache, and native frame rate. Bidirectional models must subsample video to match a language caption, which distorts FPS.

**Data (§4.1, App. E)**
- ~500 h of AgiBot G1 teleop: 7,193 episodes, averaging 4.4 min and **42 subtasks per episode**, collected in 22 environments (homes, restaurants, supermarkets, offices, warehouses, hotels).
- Each episode chains three coarse tasks from a printed sheet. A task is **retired after 50 episodes**, and operators must propose new ones, so the task distribution keeps growing a long tail (App. E).
- Franka results come from [DROID](../entities/droid.md) alone. The AgiBot dataset is "planned" for release.

**Baselines and protocol (§4)**
- [GR00T N1.6](../entities/nvidia-groot.md) and π0.5, each in two versions. *From scratch*: VLM weights, no robot pretraining. *From pretrained*: official checkpoints, continued on the same data. Batch size and gradient steps are matched.
- AgiBot: 10 seen and 10 unseen tasks × 8 rollouts across 4 robots = 80 rollouts per checkpoint. **Every evaluation site is in a different geographic location from the training data.** DROID: 20 seen + 20 unseen tasks (unseen = verbs absent from DROID) × 2 rollouts = 80, scored 0–1 for partial progress.

**Results (§5.1)**

| Setting | Best VLA (pretrained) | DreamZero |
|---|---|---|
| AgiBot seen tasks, avg task progress (Fig. 8) | 27.4% | **62.2%** |
| AgiBot unseen tasks, avg task progress (Fig. 9) | 16.3% | **39.5%** |
| DROID unseen, task progress / success (Fig. 9) | 33% / 7.5% (π0.5); 31% / 12.5% (GR00T N1.6) | **49% / 22.5%** |
| Post-training (shirt / fruit / bussing) avg (Fig. 10) | matched or exceeded | ≥ VLAs; large gain on fruit packing |

- From-scratch VLAs score **near zero** on the AgiBot seen tasks and **< 1%** on the unseen ones. They "reach toward the correct object but fail to interact".
- Best unseen tasks: Remove Hat from Mannequin 85.7%, Shake Hands 59.2%.
- **Failures are video failures.** "The policy faithfully executes whatever trajectory the video predicts." In the marker task the model imagines a handover instead of drawing, and the robot does the handover. In the croissant task it imagines picking up the bread before opening the oven (App. H).

**Cross-embodiment (§5.1 Q4–Q5)**
- **Video-only** transfer. 72 trajectories of 9 unseen tasks (20 min of YAM or 12 min of human video), co-trained 1:1 with pretraining data for 10K steps, **with no action labels**. Results: 38.3 ± 7.6% → **55.4 ± 9.5%** (YAM) and **54.3 ± 10.4%** (human) (Table 2).
- **Few-shot embodiment adaptation**: 55 trajectories, 11 tasks, ~30 min of [YAM](../entities/yam.md) play data. The adapted model keeps language following for unseen objects. The evidence is qualitative only (Fig. 12).

**Ablations (§5.2, Table 4)** — 50K steps, batch size 32, PnP-Easy only

| Ablation | Result |
|---|---|
| Diverse vs repetitive data (same 500 h; repetitive = 70 tasks) | **50% vs 33%** |
| 14B vs 5B backbone | **50% vs 21%**; the 5B model hallucinates in its video |
| Size-matched VLAs (Qwen3 8B/32B truncated + DiT action head) | **0%** at both sizes |
| AR vs bidirectional | 50% vs 50% (BD has ±14.4 SE) |

**Real-time execution (§3.2, Table 1)**
- The naive 14B model takes **5.7 s per chunk** on one GPU. Asynchronous execution sets the target at ~200 ms within each 1.6 s chunk.
- Cumulative speedups:
  - CFG split across 2 GPUs (1.9×)
  - DiT caching, which reuses velocities when cosine similarity is high (16 → 4 effective steps; 5.5×)
  - torch.compile + CUDA graphs (8.9× / 10.9×)
  - kernel and scheduler optimisations (9.6× H100 / 14.8× GB200)
  - NVFP4 quantisation on Blackwell (16.6×)
  - DreamZero-Flash (**38× on GB200**)
- **DreamZero-Flash**: video timesteps are biased toward high noise (Beta(7,1), E[t_video] = 0.125) while action timesteps stay uniform. The model learns to emit clean actions from a still-noisy video. With 1 denoising step it reaches **74%** table bussing, against 52% for plain 1-step DreamZero and 83% at 4 steps (350 ms → 150 ms) (Table 3).
- The paper's own caveat: "compared to current VLAs which runs up to over 20Hz on consumer GPUs, DreamZero is still computationally expensive" (§6).
- Footnote 3: generating actions only, without video, barely speeds things up at 14B. Latency is set by step count × DiT depth.

**Limitations stated (§6)**: no scaling-law study; human-video transfer tested only on 12 minutes of lab video; System-1 only, with 6 s of memory; behaviour-cloning precision limits (key insertion, fine assembly); higher-DoF bodies will need more play data for the implicit IDM.

**Comparison with latent world models (App. A)**: JEPA / Dreamer / PointWorld model p(s′|s,a) and "require goal-conditioned planning or search at test time". A WAM models p(o, a | history, c) directly and needs no test-time optimisation.

## Reading notes (wiki inference)

- **The headline comparison mixes architecture with initialisation.** DreamZero starts from a 14B *video* model trained on web video. The "from-scratch" VLAs start from a VLM. The size-matched VLA ablation (0% at 8B/32B) is the paper's answer, and it is strong. It is also run on one task category, at batch size 32, with no seeds.
- **"Failures are video failures" cuts both ways.** It supports the thesis that better video means better policy. It also means the policy has **no independent check on its own plan**: it executes whatever it imagines, wrong order included. That is the gap [AW-0](agentic-world-action-models-aw0-paper.md) later fills from the same group, by putting a code plan *upstream* of the video (C→V→A).
- **The data-collection rule is the most transferable idea here.** Retiring a task after 50 episodes forces breadth. Its 50% vs 33% ablation is one of the few same-hours diversity-vs-repetition comparisons in the wiki. It is measured only on PnP-Easy, though.
- **Inference cost puts it in the cloud.** 7 Hz needs 2 × GB200 with NVFP4. Next to [mimic-video](mimic-video-paper.md)'s finding that a VAM's best policy runs at pure video noise, DreamZero-Flash is the same discovery reached from the other side: actions can be decoded from a mostly noisy video.
- **Later independent numbers are mixed.** On [Cosmos 3](cosmos-3-technical-report.md)'s RoboLab-120 sim benchmark, DreamZero scores 25.2% against π0.5 at 28.1%. In [AW-0](agentic-world-action-models-aw0-paper.md)'s real-world tests, it beats π0.5 on average (46.0 vs 43.6 rubric) and wins clearly on contact-rich tasks (Replace Lightbulb, Deal Poker), but loses on semantic ones. Neither replicates the paper's 2× margin. Both use benchmark-standard data, not DreamZero's diverse-data regime.
- **Chronology.** DreamZero (2026-02-17) postdates [DreamDojo](dreamdojo-paper.md) (2026-02-06). The wiki's "DreamGen → DreamZero → DreamDojo" ordering was a framing, not a sequence. DreamDojo is the action-*conditioned* simulator, and DreamZero is the action-*generating* policy. They are parallel branches.

## Entities mentioned
- [DreamZero](../entities/dreamzero.md) (new)
- [NVIDIA GEAR Lab](../entities/nvidia-gear.md), [NVIDIA](../entities/nvidia.md)
- [Joel Jang](../entities/joel-jang.md), [Jim Fan](../entities/jim-fan.md), [Yuke Zhu](../entities/yuke-zhu.md) (project leads); [Guanzhi Wang](../entities/guanzhi-wang.md)
- [AGIBOT](../entities/agibot.md) (G1 robot), [AGIBOT Genie Sim 3.0](../entities/agibot-genie-sim.md), [Franka Panda](../entities/franka-panda.md), [DROID](../entities/droid.md), [YAM](../entities/yam.md), [RoboArena](../entities/roboarena.md)
- [NVIDIA GR00T](../entities/nvidia-groot.md) (N1.6 baseline), [Physical Intelligence](../entities/physical-intelligence.md) (π0.5 baseline)
- Without wiki pages: Wan2.1 (Alibaba), PolaRiS (DROID sim eval).

## Concepts touched
- [World-action model](../concepts/world-models/world-action-model.md)
- [VLA models](../concepts/learning/vla-models.md)
- [Cross-embodiment](../concepts/learning/cross-embodiment.md)
- [JEPA](../concepts/world-models/jepa.md) (App. A contrast)

## Related sources
- [DreamDojo paper](dreamdojo-paper.md), [DreamGen paper](dreamgen-paper.md): the other Dream* papers.
- [AW-0 paper](agentic-world-action-models-aw0-paper.md): DreamZero as the pure-WAM baseline, beaten by adding a code stream.
- [Cosmos 3 technical report](cosmos-3-technical-report.md): DreamZero as a RoboLab baseline.
- [mimic-video paper](mimic-video-paper.md): the VAM alternative (frozen backbone + IDM decoder).
- [EgoScale paper](egoscale-paper.md): GEAR's parallel *VLA* bet on human video.

## Open questions
- Does the diverse-data advantage hold on harder task categories, and with seeds? The ablation is PnP-Easy only.
- How much of the margin over VLAs comes from the 14B web-video initialisation itself? A VLA built from a 14B video model's *encoder* would isolate it.
- The few-shot YAM adaptation is shown only qualitatively. What are the numbers?
- Whether a distilled or smaller backbone keeps the generalisation: the paper's own route to on-robot deployment.
- AgiBot dataset release status.
