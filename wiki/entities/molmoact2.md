---
title: MolmoAct2
type: entity
subtype: model
created: 2026-07-25
updated: 2026-08-03
sources: 6
tags: [molmoact2, molmoact, vla, vision-language-action, flow-matching, per-layer-kv-conditioning, adaptive-depth, fast-tokenizer, hybrid-action-head, allen-institute, molmo, real-world-deployment, open-source, open-data]
---

# MolmoAct2

**MolmoAct2** ([Fang, Duan et al. 2026](../sources/molmoact2-paper.md) — *MolmoAct2: Action Reasoning Models for Real-World Deployment*, arXiv 2605.02881) is [Ai2](ai2.md)'s **fully open** action-reasoning [VLA](../concepts/learning/vla-models.md) and the successor to [MolmoAct](molmoact.md). Where MolmoAct was a **discrete-token** policy, MolmoAct2 is a **hybrid**: a discrete-token VLM backbone ([Molmo2-ER](molmo2-er.md)) grafted onto a **continuous [flow-matching](../concepts/learning/flow-matching.md) action expert** via **[per-layer KV conditioning](../concepts/learning/per-layer-kv-conditioning.md)**. Its explicit design target is not benchmark leadership but **real-world deployability** — open weights *and* data, out-of-the-box on cheap-to-mid-cost robots, performant after light fine-tuning, and fast enough for closed-loop control.

## Why it matters in this wiki

MolmoAct2 is the wiki's **most complete "open-everything" deployable VLA** — the point where Ai2's radical-openness thread ([OLMo](olmo.md) → [Molmo](molmo.md) → [MolmoAct](molmoact.md)) reaches a policy you can actually run on a **<$6,000 off-the-shelf setup**. It is the first ingested VLA to combine, in one system:

- a **hybrid discrete+continuous action head** (discrete FAST tokens as a training/representation signal, continuous flow-matching expert for deployment) — the [knowledge-insulation](../concepts/learning/knowledge-insulation.md) idea taken to a full architecture;
- **[per-layer KV conditioning](../concepts/learning/per-layer-kv-conditioning.md)**, a novel VLM→expert interface that beats the standard final-hidden-state conditioning of [π0](pi-zero.md)/[GR00T](nvidia-groot.md); and
- **adaptive-depth reasoning** ([MolmoAct2-Think](#molmoact2-think)) that makes "embodied chain-of-thought" cheap enough to keep in the control loop.

On the wiki's cross-method [LIBERO](libero.md) table it **displaces π0.5 and GR00T N1.7 at the top** (97.2 / 98.1), and it is the first entry with a large, released **real-world** deployment suite behind the number.

## Architecture

- **Backbone:** [Molmo2-ER](molmo2-er.md) — a 4B embodied-reasoning VLM (SigLIP2 ViT → Molmo2 connector → LLM), **36 layers**.
- **Action expert:** DiT-style flow-matching transformer, **also 36 layers**, matching backbone depth. Trained with a flow-matching velocity objective (`x_t = (1−t)ε + t·a`, predict `a − ε`).
- **Interface — [per-layer KV conditioning](../concepts/learning/per-layer-kv-conditioning.md):** each expert block cross-attends to the **keys and values of the corresponding VLM layer** (via learned adapter projections P_K, P_V), giving the controller the same hierarchical attention state the VLM uses — not a single compressed residual-stream vector.
- **Action tokenizer — MolmoAct2-FAST:** open-weight/open-data [FAST](fast-action-tokenization.md); 2048-token vocab, 1-second chunks, 32-D padded action space, trained on 1M sequences across 5 embodiments. State discretized into 256 tokens.

## Three-stage training

1. **Pre-training** — Molmo2-ER → discrete autoregressive robot policy predicting FAST action tokens; 200K steps, 64 H100s, 90% robot / 10% multimodal.
2. **Post-training** — attach the flow-matching expert; co-train discrete + continuous losses (`L_LM + L_flow`); **[knowledge insulation](../concepts/learning/knowledge-insulation.md)** detaches the KV conditioning path so the flow loss doesn't corrupt the VLM; K=4 flow samples.
3. **Deployment fine-tuning** — embodiment-specific, robot-only, K=8 flow samples, knowledge insulation **dropped** (gradients allowed through the VLM).

## MolmoAct2-Think

The **adaptive-depth reasoning** variant. Before acting, it predicts a compact discrete depth map (Depth Anything V2 → depth VQ-VAE → **10×10 grid, 128 codes**) that conditions the action expert. Its innovation over [MolmoAct](molmoact.md)'s fixed depth-token step is that depth prediction is **adaptive across time**: cached codes are reused for static regions and re-predicted **only for cells whose RGB patch changes** (cosine sim < 0.996). Geometric-reasoning cost scales with scene change, not the full grid — keeping interpretable depth reasoning in the loop without paying full latency every step. See [adaptive depth reasoning](../concepts/learning/adaptive-depth-reasoning.md).

## Reported numbers (from ingested sources)

- **[LIBERO](libero.md)** ([MolmoAct2 paper](../sources/molmoact2-paper.md), Table 8): MolmoAct2 **97.2** avg (Spatial 97.8 / Object 100.0 / Goal 97.8 / Long 93.2); **MolmoAct2-Think 98.1** — top of the table, above π0.5 (96.9), GR00T N1.7 (97.0), and +10.6 over MolmoAct-7B-D (86.6).
- **Real-world DROID** (zero-shot, random cameras, novel objects): **87.1%**, +38.7 over runner-up MolmoBot.
- **Real-world SO-100** (zero-shot): **56.7%**, +11.4 over in-house π0-SO100/101.
- **RoboEval** (fine-tuned): **44.3%**, +3.8 over π0.5; also shorter/smoother trajectories.
- **Real-world YAM, 8 in-the-wild tasks** (50 trials each): **50.1%** avg [45.0–55.0], +15 over OpenVLA-OFT. **The +15 pp survives** aggregated over 400 rollouts (p=0.00002); the companion **"wins 7 of 8 tasks" does not** (sign test p=0.070), nor would +15 pp within any *single* 50-trial task (p=0.13). See the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md).
- **OOD robustness** (spatial/lighting/language/distractor): **50.69%**, +10.8 over OpenVLA-OFT.
- **Inference:** **55.79 Hz** (continuous path, CUDA Graphs, 2.42× over baseline); MolmoAct2-Think 12.71 Hz. Continuous flow path is 3.94× faster than the discrete autoregressive action path — hence continuous is the deployment default.

## Released checkpoints and deployment envelope (added 2026-08-03)

From the [GitHub repo](../sources/molmoact2-github-repo.md) and the [SO-100/101 model card](../sources/molmoact2-so100-101-model-card.md):

| Kind | Checkpoints |
|---|---|
| **Base** | MolmoAct2, MolmoAct2-Think, MolmoAct2-Pretrain, [Molmo2-ER](molmo2-er.md) |
| **Fine-tuned** | MolmoAct2-DROID ([Franka](franka-panda.md)), MolmoAct2-BimanualYAM ([YAM](yam.md)), **MolmoAct2-SO100_101** ([SO-ARM101](so-arm101.md)), MolmoAct2-LIBERO, MolmoAct2-Think-LIBERO |

**Memory footprint** — note the spread; "MolmoAct2 needs X GB" is not one number:

| Deployment | float32 | bfloat16 |
|---|---|---|
| SO-100/101 (**5B params**) | ~24–26 GB | **~16 GB** |
| YAM (bimanual) | ~26 GB | under 16 GB |
| DROID (Franka) | **~88 GB** | ~16 GB |

- **Ships as a [LeRobot](lerobot.md) application** — datasets in LeRobot v3.0 format, LeRobot vendored as a git submodule, training through LeRobot workflows. Not a parallel stack to the one this wiki's projects use; the same one.
- **Deployment is client/server** — two FastAPI inference servers (DROID :8000, YAM :8202), i.e. the model is expected to run off-robot.
- Sim eval runs on **[ManiSkill](maniskill.md)** at the repo level, though the paper's headline sim benchmark is [LIBERO](libero.md).
- Tested on **RTX A6000**; Intel XPU supported. **No Jetson build, benchmark, or mention anywhere.**
- The SO-100/101 checkpoint uses **absolute joint-pose control** with annotated language instructions — joint-space and absolute, so calibration agreement matters more than it would for relative end-effector actions.
- Ai2's stated porting guidance: start from the **nearest embodiment's fine-tuned checkpoint** (YAM / DROID Franka / SO-100/101), not the generalist base.

> [!warning] ~16 GB bf16 is not an Orin NX 16 GB fit
> Jetson uses unified memory shared with the CPU, so a 16 GB Orin NX has well under 16 GB free after OS, cameras, and ROS. A 5B checkpoint whose weights alone want ~16 GB in bf16 is **not a realistic Orin NX target** — AGX Orin 64 GB or [Thor](jetson-thor.md) are the plausible edge tiers. Inference from the stated footprint, **not a measurement**; nobody has published MolmoAct2 on Jetson. See the [XLeRobot compute page](../syntheses/platforms/jetson-onboard-compute-xlerobot.md).

## Datasets released

- **MolmoAct2-BimanualYAM Dataset** — 720 hrs, 34.5k demos, 28+ tasks on bimanual [YAM](yam.md); largest open bimanual dataset to date.
- **MolmoAct2-DROID Dataset** — 74,604 quality-filtered Franka episodes from [DROID](droid.md).
- **MolmoAct2-SO100/101 Dataset** — 38,059 filtered episodes from 1,222 community LeRobot datasets.

## Related

- [MolmoAct](molmoact.md) — the discrete-token predecessor; MolmoAct2 keeps the "reason in space" framing but adds a continuous expert and adaptive depth.
- [Molmo2-ER](molmo2-er.md) — the embodied-reasoning VLM backbone.
- [π0.5 / π0.6](pi-zero-6.md), [π0](pi-zero.md) — the main [Physical Intelligence](physical-intelligence.md) baselines it targets and beats.
- [Knowledge insulation](../concepts/learning/knowledge-insulation.md) / [FAST](fast-action-tokenization.md) — the PI training-recipe ingredients MolmoAct2 adopts and open-sources.
- [Per-layer KV conditioning](../concepts/learning/per-layer-kv-conditioning.md) / [adaptive depth reasoning](../concepts/learning/adaptive-depth-reasoning.md) — its two architectural contributions.
- [VLA deployability landscape](../syntheses/platforms/vla-deployability-landscape.md) — the four-axis cross-player comparison this model anchors.
- [VLA models](../concepts/learning/vla-models.md) — hybrid action-head family.

## Open questions

- **Molmo2 / Molmo2-ER primary (Clark et al. 2026) not ingested** — base VLM scale/data only summarized via this paper.
- ~~Is MolmoAct2-Think's ~4× latency penalty (12.7 vs 55.8 Hz) worth its +0.9 LIBERO gain in deployment?~~ — **sharpened 2026-07-27 by the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md)**: the **+0.9 is not statistically established** (p=0.35 at 500 trials/suite; p=0.06 even at 2,000). So the trade is a *measured* 4× latency cost against an *unmeasured* gain. The question is no longer "is it worth it" but **"is there a gain at all"** — which needs either more rollouts or a task suite where Think's advantage is larger than LIBERO's headroom allows. (Think's +2.2 on the hardest suite, Long, is the most likely place a real effect survives.)
- How does adaptive-depth's latency advantage hold up on **egocentric / mobile** views where the whole scene moves and few cells stay static?

## Mentioned in

- [MolmoAct2 paper (Fang, Duan et al. 2026)](../sources/molmoact2-paper.md) — the primary source.
- [MolmoAct2-SO100_101 model card](../sources/molmoact2-so100-101-model-card.md) — the SO-100/101 checkpoint; 5B params, ~16 GB bf16, absolute joint-pose control.
- [MolmoAct2 GitHub repo](../sources/molmoact2-github-repo.md) — full checkpoint family, LeRobot-native training, FastAPI deployment servers, ManiSkill sim eval.
