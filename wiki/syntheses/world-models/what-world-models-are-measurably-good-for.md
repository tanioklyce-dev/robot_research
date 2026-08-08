---
title: What world models are measurably good for
type: synthesis
created: 2026-08-08
updated: 2026-08-08
tags: [world-model, evaluation, synthesis, model-based-rl, data-generation, policy-evaluation, planning]
---

The wiki has tracked world models as an architecture question for months — pixels vs latents, action-conditioned or not, unified or staged. As of the [WorldArena](../../entities/worldarena.md) cluster it can be asked as an **empirical** question instead: given a learned world model, what job can you actually give it?

The answer has more structure than "not much yet." Four roles, four different verdicts, and the ordering is not the one the field's enthusiasm implies.

## The four roles, scored

| Role | Best measured result | Reference point | Verdict |
|---|---|---|---|
| **RL environment** — train a policy *inside* it | WoVR **75.0**, Ctrl-World **70.7** | simulator-RL 87.3 / 78.9; SFT 43.8 / 55.1 | **Works.** ~⅔ of the gap to a real simulator closed; every model beats SFT |
| **Policy evaluator** — rank policies without hardware | Ctrl-World **r = 0.986** vs simulator ranking | — | **Works for ranking, not for levels.** Scores are inflated |
| **Data engine** — generate training data | WoW 45% / 71% | real data 77% / 66% | **Marginal.** Only 2 of 6 models beat real data, only on the easier task |
| **Action planner** — drive the robot directly | WoW 20% / 21% | [π0.5](../../entities/pi-zero-5.md) 77% / 66% | **Doesn't work.** Loses 3–4× to a dedicated VLA |

(All from [WorldArena](../../sources/worldarena-paper.md) and [WorldArena 2.0](../../sources/worldarena-2-paper.md) on [RoboTwin 2.0](../../entities/robotwin.md); the two tasks are *adjust bottle* and *click bell*.)

## The one-line reading

**Learned dynamics are good enough to *shape* a policy. They are not good enough to *be* one.**

Neither paper states it this way, and it's the most decision-relevant thing in the cluster. It also explains what would otherwise look like a contradiction: the same world models that get a policy to within two-thirds of simulator-trained performance as an RL environment lose to that same policy class by 3–4× when asked to plan actions directly.

The reason is plausibly error accumulation with a corrective loop versus without one. As an RL environment the model's errors are *averaged over* by the optimizer, which is extracting a gradient signal across many imagined rollouts; individual bad rollouts are noise. As a planner the model's errors are *executed* — a single hallucinated transition becomes a real arm movement. Same fidelity, opposite tolerance for it.

If that reading is right, it predicts something testable: world-model quality should matter much more for the planner role than for the RL-environment role. WorldArena 2.0's RL table is weakly consistent with that (OpenSora, IRASim, iVideoGPT are "limited by their video generation quality" and show only marginal gains) but nobody has run the ablation.

## What this does to the wiki's existing world-model claims

### The generative-video-as-simulator thesis survives, narrowed

[World-model simulators](../../concepts/world-models/world-model-simulators.md) has been the wiki's home for the "train inside a learned model" story — [Cosmos](../../entities/nvidia-cosmos.md), [Genie Envisioner](../../entities/genie-envisioner.md), DreamGen, [Veo](../../entities/veo.md). The measured version says: **as an RL environment, yes; as a data engine, not yet; as the policy itself, no.** That's a real narrowing, and it lands hardest on the data-engine story, which is the one most of the wiki's generative-video sources are actually selling.

### Vendor claims and independent numbers diverge sharply

[Genie Envisioner](../../entities/genie-envisioner.md) entered this wiki through an AGIBOT announcement claiming minute-scale stable rollouts. Independently benchmarked it comes **last of 14** on EWMScore (43.65, seven points below 13th), lowest instruction-following (0.2028), and **0%/0%** on both WorldArena 2.0 visuotactile tasks. It also scores 10%/20% as a planner — mid-pack among a bad field.

The general lesson is one the wiki keeps relearning: [robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md) said it about VLAs, [LIBERO-PRO](../../sources/libero-pro-paper.md) said it about LIBERO, and it is true here. **Vendor-reported world-model capability has not once survived independent measurement in this wiki.**

### Action conditioning is load-bearing

The cleanest natural experiment available: **Cosmos-Predict 2.5 was evaluated in both a text-conditioned and an action-conditioned variant.** Same family, same training substrate.

| | Text-conditioned | Action-conditioned |
|---|---:|---:|
| EWMScore | 50.81 | **55.90** |
| Trajectory accuracy | 0.0816 | **0.2945** |
| Instruction following | 0.2664 | **0.5840** |

Plus [Ctrl-World](../../entities/ctrl-world.md), action-conditioned, taking the best policy-evaluator correlation and the best long-horizon RL result. This is direct support for the [world-action model](../../concepts/world-models/world-action-model.md) thesis — action as a first-class variable rather than a caption — from an evaluation rather than from a system paper.

### General video models are not embodied world models

Veo 3.1 and Wan 2.6 top visual and aesthetic scores and "show limited improvements in embodied-specific metrics"; visually strong models "suffer from semantic drift." Wan 2.6 nonetheless takes the top EWMScore — which is an indictment of EWMScore, not a claim about Wan 2.6, given that EWMScore correlates at 0.360 with planning performance.

One genuine counter-example: in WorldArena 2.0's **visuotactile** extension, the general-purpose Wan 2.2 beats every embodied specialist at tactile prediction, because "general-purpose world models retain richer cross-modal knowledge priors." Scale does buy something transferable; it just isn't dynamics.

## Where the measurements stop

- **Two tasks, 100 trials.** The entire functional record rests on *adjust bottle* and *click bell*. By the wiki's own [rollout standard](../../concepts/robotics/robot-policy-evaluation.md) that's ±10 pp — fine for 3–4× gaps, useless for ranking adjacent models. Treat the *ordering* within each column as unestablished.
- **25 synthetic trajectories** in the data-engine test — two orders of magnitude below the regime where synthetic data would be used in earnest.
- **Real-robot results are almost all zero**, with a few 10–50% outliers on two ALOHA tasks and no confidence intervals.
- **No cost accounting anywhere.** RL inside a video world model should be expensive; nobody says how expensive. The wiki's [code-as-policy](../../concepts/agents/code-as-policy.md) page notes the same silence across a ten-paper lineage. The one hard comparative number in the wiki still runs the other way: [LeWorldModel](../../entities/leworldmodel.md) reports up to **48× faster planning** in latent space than foundation-model world models.
- **Nothing bridges roaming and manipulation.** [WorldRoamBench](../../entities/worldroambench.md) and WorldArena share an author and zero models. "Good world to walk through" and "good world to train a robot in" remain unrelated measurements.
- **The JEPA family is absent from *these* benchmarks** — every model in WorldArena and WorldRoamBench is a pixel predictor, and WorldArena's 16 video metrics could not score a latent predictor without modification.

> [!warning] Correction (2026-08-08): "absent from these benchmarks" ≠ "unmeasured"
> An earlier version of this page called the JEPA family "entirely unmeasured," which was wrong. It is measured — by **different instruments**, which is the actual problem:
>
> | Instrument | What it scores | Family it can run on |
> |---|---|---|
> | [WorldArena](../../entities/worldarena.md) / [WorldRoamBench](../../entities/worldroambench.md) | Video quality + functional utility + long-horizon stability | Pixel predictors only |
> | [stable-worldmodel](../../sources/stable-worldmodel-paper.md) | Planning success under controllable factors of variation | Latent predictors (LeWM, DINO-WM, PLDM, TD-MPC2) |
> | [JEPA-WMs](../../sources/jepa-wms-paper.md) | Planning success, ablated by design choice | Latent predictors |
> | [Action-relevant latents](../../sources/action-relevant-latents-paper.md) | Inverse-dynamics probe R² | **Both** |
> | [Latent video prediction](../../sources/latent-video-prediction-better-world-models-paper.md) | Five robustness axes on frozen features | **Both** (as encoders) |
>
> The real condition is **incommensurability**: for most of 2026 the two literatures used instruments that could not be run on each other's models, so neither could rank the other. The bottom two rows are the first shared instruments, and they arrive at the probe/representation level rather than the system level.

**What the shared instruments say.** Both favour latent prediction, and both qualify it:

- **Pixel fidelity and action recoverability are orthogonal.** At ~20 dB PSNR, frozen action R² spans −0.01 to +0.46; the highest-PSNR backbones (SDXL VAE, the Cosmos-1 tokenizer) post the *lowest* action R², at or below zero ([action-relevant latents](../../sources/action-relevant-latents-paper.md)). This is WorldArena's r = 0.360 restated at the representation level — and it now covers both families.
- **The credit is mostly temporal video pretraining, not JEPA as such.** V-JEPA 2 +ID reaches 0.85 action R² against VideoMAE +ID at 0.75 — so the feature-level predictive objective is worth about **+0.10**, with most of the gap over image-only SSL coming from natural-video temporal context. A real but smaller win than the JEPA literature's framing implies.
- **But V-JEPA is not "semantic SSL."** Web-DINO and SigLIP 2 sit at 0.16–0.17 after the same tuning, clustered with reconstruction encoders — a caution that lands on [DINO-WM](../../entities/dino-wm.md), which builds on a frozen image-SSL encoder.
- **Stable ≠ usable.** VideoPrism holds representational similarity above 0.98 under severe patch dropout while collapsing to 2.7% top-1; V-JEPA 2.1 retains 46.1% ([latent video prediction](../../sources/latent-video-prediction-better-world-models-paper.md)). The same category error as judging a world model by how its rollouts look.

**Partly closed (2026-08-08).** [Reconstruction or Semantics?](../../sources/latent-space-robotic-world-models-paper.md) runs V-JEPA 2.1 latents through the **policy-evaluator** role — OpenVLA-7B rolled out inside each world model — and semantic latents roughly **double** VLA-in-the-loop success against VAE latents (0.362 vs 0.169), with the OOD gap wider still (0.575 vs 0.287 under distractors). The probe results' prediction held where it has been tested.

Two scoping notes: these are **diffusion world models whose latent space comes from V-JEPA**, not JEPA world models, so the encoder is isolated rather than the architecture; and success is VLM-adjudicated over 160 trials per encoder, which is thin by the wiki's [rollout standard](../../concepts/robotics/robot-policy-evaluation.md). Still untested: JEPA representations as **data engine**, **RL environment**, or **action planner**.

One finding from that paper worth carrying on its own: at larger DiT scale, VAE and Cosmos latents close much of the *policy-success* gap — better rendering helps a pixel-consuming VLA — but still lag on **CEM action recovery, IDM r, and classifier accuracy**. **Scale buys the parts of the problem that go through pixels and not the parts that go through dynamics.**

**And the dissociation is three years older than any of this.** [VP²](../../sources/vp2-paper.md) (Tian, Finn & Wu, ICLR 2023) showed perceptual metrics mis-rank video predictors for control — with the sign of the correlation *task-dependent*, so no constant correction recovers it. The best FVD in their study (4.9) scored 10% control success; the worst (51.7) scored 80%. Everything in this cluster is a rediscovery at scale.

## Sources

- [WorldArena paper](../../sources/worldarena-paper.md) · [WorldArena 2.0 paper](../../sources/worldarena-2-paper.md) · [WorldRoamBench paper](../../sources/worldroambench-paper.md)
- [World-model evaluation](../../concepts/world-models/world-model-evaluation.md) · [world-model simulators](../../concepts/world-models/world-model-simulators.md) · [world-action model](../../concepts/world-models/world-action-model.md)
- [HAI Issue Brief](../../sources/hai-world-model-spatial-intelligence-brief.md) — the policy framing that made this the wiki's next question.
