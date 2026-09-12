---
title: "RoboTTT: Context Scaling for Robot Policies"
type: source
url: https://arxiv.org/abs/2607.15275
local_path: raw/2607.15275.pdf
sha256: 6e3cbcbc0ab4db0c20e693c905c9ff4e7f7afe726b15f8fb6dc3a6d7415e4ca0
author: "Yunfan Jiang, Yevgen Chebotar, Ruijie Zheng, Fengyuan Hu, Yunhao Ge, Jimmy Wu, Tianyuan Dai, Scott Reed, Li Fei-Fei, Yuke Zhu, Linxi 'Jim' Fan"
affiliations: "NVIDIA (GEAR), Stanford University, UT Austin"
published: 2026-07-16
venue: "arXiv preprint (v1); no peer-reviewed venue as of ingest"
format: paper (22 pp; 12 pp body + references + appendix)
arxiv: 2607.15275
project_page: https://research.nvidia.com/labs/gear/robottt
tags: [robottt, test-time-training, fast-weights, long-context-policy, in-context-learning, one-shot-imitation, human-video, dagger, algorithm-distillation, groot-n1-7, yam, bimanual, assembly, long-horizon, scaling-laws, nvidia-gear]
ingested: 2026-09-12
---

# RoboTTT: Context Scaling for Robot Policies

## Summary

**A robot policy whose memory is a small neural network trained by gradient descent while the robot runs.** RoboTTT ([NVIDIA GEAR](../entities/nvidia-gear.md) + Stanford, July 2026) inserts Test-Time Training (TTT) layers into the action head of [GR00T N1.7](../entities/nvidia-groot.md): the recurrent state is a set of *fast weights* — a two-layer MLP per layer — updated by gradient descent on every observation during both training and inference, while the model's ordinary *slow* weights stay frozen at deployment. That makes inference cost constant in history length, and lets the visuomotor context scale to **8K timesteps (about 4.5 minutes at 30 Hz)**, which the authors put at three orders of magnitude beyond current VLAs.

The paper's actual headline is a **new scaling axis**: closed-loop task completion rises steadily with *pretraining context length* from 128 to 8K timesteps (**43.9% at 1K → 71.5% at 8K**), and a matched recurrent baseline without test-time gradient descent (Gated DeltaNet) shows **no trend at all**. The long context is then used two ways — **across episodes**, conditioning on one human video to imitate an unseen assembly configuration (6/10 vs 0/10 for the baseline), and **within an episode**, conditioning on the robot's own rollout to track progress, recover from perturbations, and, via a procedure they call *DAgger Distillation*, correct its own mistakes on the fly.

Everything is measured on three real bimanual assembly tasks with rubric scores, full-success counts, matched-compute baselines, and ablations. Trial counts are small (10–20), the one-shot result is on the shortest task with the task itself seen in training, and every model is post-trained per task. It is nonetheless the first source in this wiki's in-context cluster with **any** controlled ablation of the mechanism.

> [!note] What "test-time training" means here — and why it is not what the wiki's concept pages call it
> The wiki separates **in-context learning** (no weight update) from **[test-time adaptation](../concepts/learning/test-time-adaptation.md)** (gradient steps on the model). RoboTTT is neither, cleanly. Gradient descent *does* run at inference — but only on the fast weights, which are the sequence model's recurrent state, initialized from a meta-learned $W_0$ and discarded at the end of the rollout. The model parameters never change. The authors say it themselves: RoboTTT *"can also be viewed as an RNN policy whose recurrent states are fast weights."* So from the outside it is in-context learning (one forward pass over a context, no persistent update); from the inside the context is compressed by literal gradient descent. This is the most *explicitly designed* inner loop in the wiki, and the paper cites MAML for the gradients-of-gradients meta-learning of $W_0$. See [Relationship to S1 and GEN-1.5](#relationship-to-the-s1-vs-gen-15-dispute).

## Key claims

### Headline numbers (Sec. 4)

| Result | RoboTTT | Best baseline | Single-step GR00T N1.7 |
|---|---|---|---|
| Average task completion, 3 tasks | **79%** | 56% (GDN) | 42% |
| Full successes — Pup Go Car / Circuit / Gear Bot | **9/20 · 13/20 · 2/10** | 3/20 · 8/20 · 0/10 (GDN) | 3/20 · 3/20 · 0/10 |
| Pretraining context scaling (avg. score) | **71.5% at 8K** vs 43.9% at 1K | 45.6% (GR00T N1.7 Hist.) | — |
| One-shot imitation from human video (Circuit, unseen config) | **65% · 6/10** | 33% · **0/10** (GDN) | cannot condition |
| Perturbation recovery — roof / tire (of 20) | **15 · 18** | 13 · 18 (GDN) | 10 · 11 |
| DAgger Distillation gain over pre-DAgger | **+36%** | +29% (GDN) | n/a (+9% avg. for standard DAgger) |

- *"RoboTTT improves overall performance by 87% over the single-step context baseline and fully completes a five-minute, ten-stage assembly task, which no baseline ever does"* (Abstract). The 2/10 on Gear Bot is the "fully completes."
- *"RoboTTT trained with 8K-timestep context outperforms the same model pretrained with 1K timesteps by 62%"* (Abstract; the body says 63%), *"suggesting context length as a new scaling axis for robot foundation models."* The scaling curve (Fig. 8) *"surpass[es] the best short-context baseline from 1K onward with no sign of saturation; GDN does not benefit from longer context."* Note the caveat in the figure caption: *"All evaluations in this figure predate the DAgger training used for Pup Go Car in the main results."*
- **Naive history hurts.** GR00T N1.7 with one history frame scores **39.5% vs 57%** for the no-history model on Pup Go Car — *"appended histories can introduce spurious correlations and leave the robot temporally out of distribution."* This is the causal-confusion problem (de Haan et al. 2019, cited), and it is why "just add frames" is not the answer.
- **Below 1K context the model underperforms its own longer variants**, attributed to *"the rollout horizon exceeding the training context: 1K timesteps is about half a minute, shorter than our shortest task episode."*

### Method (Sec. 3)

- **Architecture.** GR00T N1.7 = Eagle VLM backbone + 16-layer DiT flow-matching action head (538M). A TTT layer is added after the attention layers in each DiT layer (~10M each → **690M** action head). Attention runs *within* a timestep; TTT runs *across* timesteps. Each timestep contributes 16 learned **register tokens**, proprioception, and noised action tokens to the TTT stream — the vision-language tokens themselves are not passed through TTT, for cost; the registers carry them. A **tanh gate** initialized near zero (α = 0.001) keeps the TTT contribution negligible at the start so the pretrained VLA is not disrupted.
- **Fast weights.** Per layer, a two-layer GeLU MLP; update rule is standard gradient descent on a key→value MSE with a learned inner learning rate (base 0.1). The projections and $W_0$ are learned through the outer flow-matching loss — $W_0$ *"is meta-learned through gradients of gradients."*
- **Training recipe** — the two things that made long sequences trainable: (1) **sequence action forcing** — the flow-matching noise level is sampled *independently per action chunk* in the sequence, after Diffusion Forcing; sharing one noise level makes whole sequences uniformly easy or hard and training is unstable without it (the ablation shows collapse); (2) **truncated BPTT** — gradients stop at segment boundaries but the fast weights *carry across* them, so context can grow at fixed GPU memory.
- **Learning from heterogeneous context by loss masking (Sec. 3.3).** Masking the flow-matching loss on chosen timesteps makes them *pure context*: they update the fast weights but supply no imitation target. Two uses:
  - **One-shot imitation from human video.** Pairs of (human demonstration video, robot trajectory) of the same configuration are concatenated into one sequence; loss is masked on the video. The prompt is held constant (*"assemble circuit"*) across all 80 configurations, *"so the target configuration is identifiable only from the in-context video."*
  - **DAgger Distillation.** In a DAgger rollout the executed action is either the robot's own (suboptimal) action or a human correction. Standard DAgger fine-tunes on the corrections and throws away the robot's mistakes. RoboTTT keeps both in *asymmetric roles*: **failures as context, corrections as targets** — the fast weights update on the full interleaved history, the loss is computed only on the corrections. *"We view it as an instantiation of Algorithm Distillation (Laskin et al. 2023) in robotics."* At test time the policy's own corrections enter its context the way the human's did in training.
- **Pretraining data.** *"A mixture of tabletop bimanual robot data and egocentric human video data"* (EgoScale, uningested), curated for long trajectories; 41.4% of trajectories are over 4K timesteps. **Only the new TTT (or GDN) layers are trained during pretraining; GR00T N1.7 is frozen.** 30K steps on 16 GB200 GPUs, context grown gradually to the target. Post-training then tunes **all parameters** on each task, at 1K context, 20K steps.

### Evaluation (Sec. 4, App. B)

- **Platform.** [YAM](../entities/yam.md) bimanual tabletop setup, four RealSense D405 cameras (top, bottom, two wrist) at 480p, **30 Hz control**, inference on one RTX 5090.
- **Tasks and data** — all real, all multi-stage assembly with drills, screws, flips and bimanual handoffs:

| Task | Real data | Avg. episode | Notes |
|---|---|---|---|
| Pup Go Car | 8 h | 2 min | toy car roof + wheel; drilling; 14-step rubric |
| Circuit | 6 h | 1 min | ~80 configurations (components, order, count); **train 20, test 60**; no credit for wrong order |
| Gear Bot | 5 h | **5 min** | ten stages incl. two chassis flips and driving the result by remote |

- **Baselines**, all post-trained on the same task data: GR00T N1.7 single-step; GR00T N1.7 Hist. (one history frame); **GDN** — RoboTTT with every TTT layer swapped for a Gated DeltaNet layer at matched placement, gating and parameter count — *"a linear-complexity recurrent memory that updates its state without test-time gradient descent."* GDN is the controlled comparison: same fixed-size state, different update rule.
- **Trials.** 20 per policy per task; **10** for Gear Bot and for the one-shot human-video setting. Initial object placements are recorded and reproduced across methods. Scores are task-specific rubrics on [0, 1]; "full success" is a separate count.
- **Perturbations.** A human removes the roof or a tire after installation; 30 minutes of perturbation data are co-trained for *all* methods, which the authors note is probably why every method shows some recovery.
- **DAgger study.** 50 DAgger trajectories collected under RoboTTT and 50 under GR00T N1.7, pooled; all methods fine-tuned on the same 100. Standard DAgger: +9% average across four methods, +13% on the two sequence models. DAgger Distillation: **+33% average, +36% RoboTTT, +29% GDN**. The control that matters: fine-tuning GR00T N1.7 on the *full* trajectories including robot actions scores exactly what corrections-only scores (57% both) — *"the suboptimal robot actions carry no value as imitation targets. Their value is as context."*
- **Ablations (Pup Go Car, Fig. 12).** No sequence action forcing → the policy cannot make meaningful progress. Linear fast model → 27% worse than the MLP. Adding action tokens to the TTT stream → +23% relative; adding register tokens → a further +18%; register tokens added to plain GR00T N1.7 do **not** help, so the gain is from TTT using them, not the extra capacity.

### Limitations stated by the authors (Sec. 6)

Training cost grows with context length; the TTT inner objective is generic (key→value MSE), not robotics-specific; and *"it does not handle every failure mode encountered in deployment; combining it with reinforcement learning to optimize task success directly is a natural next step."*

## Relationship to the S1-vs-GEN-1.5 dispute

The [in-context page](../concepts/learning/in-context-robot-learning.md) records two vendors reporting the same capability from opposite premises: [S1](skild-s1-blog.md) says the inner loop must be *designed* into episodic pretraining; [GEN-1.5](generalist-gen-1-5-blog.md) says it *emerged* with no meta-learning and no packing. RoboTTT sits at the far "designed" end and, unlike either, publishes a controlled ablation:

| | S1 | GEN-1.5 | **RoboTTT** |
|---|---|---|---|
| Inner loop | designed (episodic data) | emergent | **designed and literal** — gradient descent on fast weights, $W_0$ meta-learned |
| Context structure in training | task identifiable only from demo | random contiguous spans | **paired (video, trajectory) sequences with loss masking**; DAgger histories with corrections-only loss |
| Ablation of the mechanism | none | none | **GDN**: same fixed-size state, no test-time gradient descent → 0/10 one-shot, no scaling trend |
| Scaling axis reported | pretraining hours (1k → 100k) | wall-clock months of pretraining | **pretraining context length (128 → 8K)** |
| Post-training on the test task | none | none (or 10 steps) | **yes — 20K steps, all parameters, per task** |
| Evidence | vendor blog | vendor blog | arXiv preprint, rubric + counts + baselines + ablations |

Two things follow. First, RoboTTT does **not** settle the designed-vs-emergent question, because it never tests a model *without* its structure on the same axis — the GDN ablation varies the update rule, not the episodic packing. What it does show is that **the update rule is load-bearing**: a recurrent memory that *encodes* the human video (GDN scores 33% on the rubric, so it is not blind to it) still cannot *use* it (0/10 full successes), while the gradient-descent memory can. *"Although recurrent-memory policies can encode contextual information, they struggle to use it."* That is the first controlled evidence in this wiki that *how* the context is compressed matters, not merely that it is present.

Second, it adds an emergence claim on a *different axis*: *"capabilities such as long-context conditioning emerge only once context length is sufficiently scaled"* — context length, not data hours. Whether S1's crossover in hours and RoboTTT's ramp in context length are the same phenomenon seen from two sides, or unrelated, no source yet says.

RoboTTT is also the first instance in the wiki that does **both** of the concept page's "two modes" in one model: demonstration-conditioned (the human video across episodes) *and* experience-conditioned (its own rollout and corrections within the episode, explicitly framed as Algorithm Distillation — the in-context-RL lineage [LocoFormer](locoformer-paper.md) belongs to).

> [!note] Is Skild's characterisation fair?
> The S1 post calls RoboTTT (and GEN-1.5) work that *"largely cover[s] tasks which are short-horizon or already present in the pre-training distribution."* On the paper's own evidence, **for the in-context-imitation result, yes**: the one-shot test is on Circuit, the *shortest* task (1-minute episodes), the task itself is post-trained on, and what is unseen is the *configuration* (60 held out of 80) — a within-task generalization, not a new skill. RoboTTT's long-horizon results (the 5-minute, ten-stage Gear Bot) are a different capability, long-context conditioning on the robot's own rollout, not learning a task from a demonstration. So Skild's sentence is accurate about the ICL claim and silent about the paper's actual headline, which is not an ICL claim at all. The asymmetry cuts the other way too: RoboTTT publishes trial counts, baselines, a rubric and an ablation, none of which S1 does — and one of S1's two supporting quotations for its own framing is from [Jim Fan](../entities/jim-fan.md), RoboTTT's last author.

## Entities mentioned

- [NVIDIA GEAR](../entities/nvidia-gear.md) — the lab; [Jim Fan](../entities/jim-fan.md), [Yuke Zhu](../entities/yuke-zhu.md) and [Fei-Fei Li](../entities/fei-fei-li.md) share equal advising credit.
- [GR00T N1.7](../entities/nvidia-groot.md) — the backbone; frozen during RoboTTT pretraining, fully tuned in post-training.
- [YAM](../entities/yam.md) — the bimanual platform for every experiment.
- [NVIDIA](../entities/nvidia.md) — GB200 training, RTX 5090 inference.
- [Skild AI](../entities/skild-ai.md) and [Generalist AI](../entities/generalist-ai.md) — not cited by RoboTTT (it predates both posts); named here because [S1](skild-s1-blog.md) cites RoboTTT as concurrent work.

## Concepts touched

- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — a third demonstration-conditioned instance, and the first with an ablation; also the first doing both modes at once.
- [Test-time adaptation](../concepts/learning/test-time-adaptation.md) — the term "test-time training" here means fast-weight recurrence, not fine-tuning; the page's boundary needs this case.
- [VLA models](../concepts/learning/vla-models.md) — a plug-in sequence-modeling layer for flow-matching VLAs; instantiated on GR00T N1.7.
- [Scaling laws for VLAs](../concepts/learning/scaling-laws-vla.md) — context length as a scaling axis, with a matched baseline that does not scale.
- [Imitation learning](../concepts/learning/imitation-learning.md) — DAgger Distillation: failures as context, corrections as targets.
- [Continual learning](../concepts/learning/continual-learning.md) — within-episode improvement without weight change; the RL follow-up the authors name is where persistent improvement would enter.

## Open questions

- **Does the context-length scaling hold without per-task post-training?** Every number is after 20K post-training steps on the task. The pretraining-only model is never evaluated.
- **Is 8K the ceiling or the budget?** *"No sign of saturation"* at 8K; training cost is the stated limit.
- **One-shot across tasks, not configurations.** The human-video result selects among assembly configurations of a post-trained task. Nothing here says whether a video of a *new* task would work — which is exactly S1's claim.
- **Small trials, no intervals.** 10–20 rollouts per cell; 6/10 vs 0/10 is convincing, 15/20 vs 13/20 is not.
- **[EgoScale](egoscale-paper.md)** — the egocentric human dataset behind both GR00T N1.7 and RoboTTT's pretraining mix. Ingested; what fraction of RoboTTT's long-trajectory pretraining mix is human video vs robot data is not stated.
- **The fast-weight objective is generic.** A robotics-specific inner loss is named as future work; what it should predict is open.
