---
title: World-model simulators
type: concept
created: 2026-05-06
updated: 2026-11-13
sources: 51
tags: [world-model, generative-simulation, video-generation, jepa, latent-prediction, paradigm-shift]
---

**World-model simulators** use learned models — not authored physics engines — as the environment for training, evaluating, or planning robot policies. Two paradigms have emerged.

## Paradigm A: Generative-video world models
Generate the next frame's *pixels*. Train and plan inside a learned video generator.

| | Physics simulator | Generative-video world model |
|---|---|---|
| Environment | Hand-authored geometry, equations of motion | Learned from video |
| Output | Next state via simulation | Next frame via generation |
| Compute bound | Physics solver | Video model inference |

Notable systems:
- **[NVIDIA Cosmos](../../entities/nvidia-cosmos.md)** — world foundation model (Cosmos-Predict2-2B-Video2World powers downstream simulators). **[Cosmos 3](../../sources/cosmos-3-technical-report.md)** (June 2026) goes further: one omnimodal Mixture-of-Transformers model is *itself* a forward-dynamics simulator, an inverse-dynamics model, **and** a policy — a [world-action model](world-action-model.md) rather than a simulator you train a separate policy inside.
- **[DreamDojo](../../entities/dreamdojo.md)** ([NVIDIA GEAR](../../entities/nvidia-gear.md), Feb 2026). A Cosmos-Predict2.5 model, 2B and 14B, pretrained on 44,711 h of egocentric human video, with latent actions standing in for missing action labels. It is distilled to 10.81 FPS for live teleoperation and planning ([DreamDojo paper](../../sources/dreamdojo-paper.md)). It is the clearest case of training a policy *inside* this kind of simulator: [GR00T 2](../../sources/gr00t-2-whitepaper.md) runs GRPO in an adapted DreamDojo, and four real tasks improve from 42.5% to 71.7%. That fine-tunes an existing policy and needs about 300 physical rollouts per task to adapt the model. Code is Apache-2.0, and the weights use the NVIDIA Open Model License.
- **[Genie Envisioner](../../entities/genie-envisioner.md)** / GE-Sim2 — built on Cosmos-Predict2; introduces the World Action Model framework where action is a first-class variable; minute-scale stable rollouts ([AGIBOT Genie Envisioner 2.0 Announcement](../../sources/agibot-genie-envisioner-2-announcement.md)).
- **[UnifoLM-WMA-0](../../sources/unifolm-wma-0-project-page.md)** ([Unitree](../../entities/unitree.md), Sep 2025) — a **DynamiCrafter** (2023) fine-tune on Open-X and five Unitree sets with a diffusion action head; its *simulation mode* is pitched as an interactive data engine ("generate synthetic data for robot learning") but no trained-on-synthetic result was ever shown, and the successor [WLA-1.0](../../sources/unifolm-wla-1-project-page.md) dropped pixel generation. The compact, vendor-built end of this paradigm.
- **[Genesis](../../entities/genesis.md)** — adjacent: physics-based but uses a [VLM](../learning/vla-models.md) agent to *generate* the simulation content from text.

> [!note] New in late 2026, not yet measured here
> From a [news roundup](../../sources/ai-search-news-2026-11-01.md) checked against project pages only; none of these have full paper ingests.
> - **[Genie 4](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)** (DeepMind): adds native audio to the interactive line after [Genie 3](../../entities/genie-3.md). Trusted-tester preview; DeepMind concedes drift in object permanence over longer runs.
> - **[MUNDO](https://mundo-world-model.github.io/)** (NTU MMLab + ACE Robotics): dynamics from MuJoCo over an inferred scene program, with a video model only for rendering, so it does not fit cleanly in Paradigm A. Unitree G1 demos with no reported numbers; weights promised for end of November.
> - **[UniAction](https://uniaction.github.io/)** (Stanford): one Wan 2.2-based model conditioned on force, camera, hand pose or robot pose.
> - **[OverSeer](https://runjiali-rl.github.io/OverSeer/)** (Oxford + Meta): multi-agent shared worlds anchored by fixed auxiliary cameras; game and studio domains, no robotics claim.

## Paradigm B: JEPA / latent-prediction world models
Predict the next-state *representation* in a learned latent space — no pixels generated. See [Joint-Embedding Predictive Architecture](jepa.md) for the architectural definition. Pioneered in Yann LeCun's group at FAIR / NYU / Mila.

| | Generative-video | JEPA / latent-prediction |
|---|---|---|
| What's predicted | Next-frame pixels | Next-state embedding |
| Training cost | Massive (per-frame generation) | Lower (no decoder) |
| Planning cost | High (video rollout) | Far lower; LeWM reports 48× faster planning |
| Pretraining at scale | Possible but costly | Web-video-scale pretraining is tractable |

Notable systems:
- **[V-JEPA 2 / V-JEPA 2-AC](../../entities/v-jepa-2.md)** ([Meta FAIR](../../entities/meta-fair.md) + [Mila](../../entities/mila.md)) — 1B-param ViT-g pretrained on 1M+ hours of internet video; 300M-param action-conditioned predictor post-trained on 62 hr of Droid robot data; **zero-shot Franka manipulation in new labs** ([V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md)).
- **[LeWorldModel](../../entities/leworldmodel.md)** ([Mila](../../entities/mila.md) + NYU + Samsung SAIL + Brown) — first stable end-to-end JEPA from raw pixels with just two loss terms; 15M params; single-GPU training; 48× faster planning ([LeWorldModel Paper](../../sources/leworldmodel-paper.md)).

## Paradigm C: task-reconstructed generative simulators

A third shape, distinct from both above: instead of a *general* learned environment, reconstruct **one specific real task** into an interactive world that carries appearance, geometry **and** physics, then reuse that world across policies and embodiments. This is [real-to-sim-to-real](../robotics/real-to-sim-to-real.md), shipped by [World Labs / SceniX](../../sources/world-labs-r2s2r.md).

What separates it from Paradigm A is the **output type**, which is exactly the [renderer/simulator line](world-model-functional-taxonomy.md): a generative-video model emits pixels; [Marble](../../entities/marble.md)-class systems emit Gaussian splats **and collision meshes a physics engine can operate on**. A policy trained in the first is learning from a video; in the second it is acting on geometry.

That distinction is doing real work in this wiki, because it is the only available reconciliation of a contradiction:

> [!warning] Marginal data engine vs. sole source of training experience
> [WorldArena](../../sources/worldarena-paper.md) measured generative-video world models as **data engines** and found them marginal — only 2 of 6 beat real data, on the easier task only. R2S2R claims policies trained on **zero real data** transferring directly across ALOHA, YAM, RB-Y1, Flexiv and xArm on contact-rich deformable tasks. If the geometry-vs-pixels distinction is what separates these outcomes, it is direct evidence for the taxonomy's simulator-is-the-linchpin claim. If it is not, one of the two results is overstated — and R2S2R is the one with no numbers, no paper, and a commercial interest.

## What they are measurably good for (2026)

The thesis on this page — use a learned model as the environment — now has independent measurement, and it survives **narrowed to one role**:

| Role | Verdict | Evidence |
|---|---|---|
| **RL environment** (train a policy inside it) | **Works** — ~⅔ of the gap to simulator-based RL closed; every model beats SFT | [WorldArena 2.0](../../sources/worldarena-2-paper.md) |
| **Policy evaluator** | Ranking yes (r = 0.986 for [Ctrl-World](../../entities/ctrl-world.md); r = 0.95 over 8 real RoboArena policies for Runway's GWM-Robotics), absolute rates no | [WorldArena](../../sources/worldarena-paper.md), [GWM-Robotics](../../sources/runway-gwm-robotics-policy-evaluation.md) |
| **Data engine** (generate training data) | Marginal — only 2 of 6 models beat real data, on the easier task only | [WorldArena](../../sources/worldarena-paper.md) |
| **Action planner** (be the policy) | **No** — loses 3–4× to [π0.5](../../entities/pi-zero-5.md) | [WorldArena](../../sources/worldarena-paper.md) |

**Learned dynamics are good enough to shape a policy, not to be one.** Full argument and caveats in [what world models are measurably good for](../../syntheses/world-models/what-world-models-are-measurably-good-for.md).

Two things this qualifies on the page below: the [Genie Envisioner](../../entities/genie-envisioner.md) minute-scale-rollout claim is a vendor announcement that independent benchmarking places **last of 14**, and none of these benchmarks evaluates a **Paradigm B / JEPA** model at all — 16 of WorldArena's metrics score *video*, which a latent predictor doesn't produce.

**Update 2026-11-07.** One benchmark now scores a Paradigm B model next to video models. [ToyBlocks](../../entities/toyblocks.md) compares [LeWM](../../entities/leworldmodel.md) with Wan 2.2 by probing predicted state rather than scoring video. The JEPA model is good on single interactions and drifts over full trajectories, while Wan 2.2 is the most accurate ([ToyBlocks (Ai2 blog)](../../sources/ai2-toyblocks-blog.md)).

> [!warning] Contradiction (soft): data-engine role
> WorldArena rates world models as data engines **"marginal"** (2 of 6 beat real data). ToyBlocks reports that 100 rollouts from its best video model raised a policy's success in an **unseen workspace region from 19% to 78%** ([ToyBlocks (Ai2 blog)](../../sources/ai2-toyblocks-blog.md)). The settings differ: rigid blocks in a narrow domain versus RoboTwin tasks, and spatial gap-filling versus replacing real data. The ToyBlocks figure comes with no baseline details. Read it as "world-model data can fill a spatial hole in a narrow domain," not as a reversal.

## Where world-model simulators are most useful (2026)
- **Pretraining policies on observed-data distributions** before any physics-based fine-tuning.
- **Generating long-horizon scenarios** for evaluation that would be expensive to author.
- **Domains where the visual or representational distribution matters more than precise physics** (high-level reasoning, manipulation strategy).

## Limits
- Not yet a substitute for physics engines on contact-rich, dynamics-critical tasks (true for both paradigms).
- Real-world adoption signals are early.
- Failure modes:
  - **Generative video** — hallucination, drift over long rollouts.
  - **JEPA** — latent collapse during training, predictor overfitting on small interaction sets.

## Related
- [VLA models](../learning/vla-models.md) — the policies that train inside or alongside world-model environments.
- [Sim-to-real transfer](../learning/sim-to-real-transfer.md) — relevance shifts: latent-prediction reduces the visual-axis gap but introduces a "model fidelity gap" instead.
- [Joint-Embedding Predictive Architecture](jepa.md) — paradigm B's underlying architecture family.
- [World-model evaluation](world-model-evaluation.md) — how you establish a learned simulator is valid for what you're using it for, and the **train-and-judge-in-the-same-model** trap that [Veo](../../entities/veo.md)-style evaluation harnesses sit closest to.
- [World-model governance](../safety/world-model-governance.md) — the procurement and certification consequences of a simulator you cannot inspect.

## Mentioned in

> [!note] Curated list — **50** source pages link here; the ones below are those that shaped this page.

- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../../sources/hai-world-model-spatial-intelligence-brief.md) — the "simulator" row of the [functional taxonomy](world-model-functional-taxonomy.md); learned simulation as the cheaper-to-update alternative to hand-built Omniverse-class environments, "still early, limited by scarce physical data."
- [DreamGen Paper](../../sources/dreamgen-paper.md) — video WM used as a **synthetic data generator** ("neural trajectories") rather than a real-time planner; the data-generation face of this concept.
- [History-Guided Video Diffusion (DFoT)](../../sources/history-guided-video-diffusion-paper.md) — the rollout-stability datapoint: history-guided sampling stabilizes autoregressive extension to **862 frames from one image** (~54× training clip length), and existing VDMs can be fine-tuned into it at ~12.5% cost — long-horizon stability being the gating requirement for video-as-simulator.
- [DIAMOND paper](../../sources/diamond-paper.md) — early playable instance: a diffusion WM trained on 87 h of CS:GO becomes an **interactive neural game engine** (Dust II), the research-scale ancestor of the Genie/Cosmos playable-world wave.
- [AGIBOT Genie Envisioner 2.0 Announcement](../../sources/agibot-genie-envisioner-2-announcement.md)
- [Genie Envisioner Paper](../../sources/genie-envisioner-paper.md)
- [V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md)
- [LeWorldModel Paper](../../sources/leworldmodel-paper.md)
- [Cosmos 3 Technical Report](../../sources/cosmos-3-technical-report.md)
- [Evaluating Gemini Robotics Policies in a Veo World Simulator](../../sources/veo-robotics-policy-evaluation-paper.md) — [Veo](../../entities/veo.md) used as an **evaluation harness** rather than a policy or data generator; action-conditioned, multi-view-consistent, with generative image editing for scene variation.
- [WorldArena paper](../../sources/worldarena-paper.md) · [WorldArena 2.0 paper](../../sources/worldarena-2-paper.md) — the four functional roles, measured.
- [WorldRoamBench paper](../../sources/worldroambench-paper.md) — long-horizon stability of interactive world models.
- [AI Search news roundup (2026-11-01)](../../sources/ai-search-news-2026-11-01.md) — pointer to Genie 4, MUNDO, UniAction and OverSeer.
- [UnifoLM-WMA-0 project page](../../sources/unifolm-wma-0-project-page.md) — Unitree's DynamiCrafter-based generative world model with a simulation mode.
- [Gemini 4 Argon for Robotics](../../sources/gemini-4-argon-robotics-blog.md) — an LLM **steering** a video world model (Gemini Omni) in closed loop: timestamped action prompts, keyframe inspection, refinement (33 steps). The world model is driven by a planner's prompts, not by a policy's actions.
- [ToyBlocks (Ai2 blog)](../../sources/ai2-toyblocks-blog.md) — LeWM vs Wan 2.2 on a ground-truth-state probe; video-model rollouts fill an unseen workspace region (19% → 78%).
- [Runway GWM-Robotics policy evaluation](../../sources/runway-gwm-robotics-policy-evaluation.md) — a commercial video world model as policy evaluator: 30 s real-time rollouts from start images, r = 0.95 against real RoboArena progress over 8 policies.
