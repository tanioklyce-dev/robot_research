---
title: Diffusion Policy Paper (Chi et al., RSS 2023)
type: source
url: https://arxiv.org/abs/2303.04137
project_page: https://diffusion-policy.cs.columbia.edu
author: Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, Shuran Song
published: 2023-03 (arxiv); RSS 2023
ingested: 2026-05-09
created: 2026-05-09
updated: 2026-05-09
tags: [diffusion-policy, behavior-cloning, ddpm, action-diffusion, push-t, robomimic, franka, ur5, columbia, tri, mit]
---

## Summary

Introduces **Diffusion Policy** — a behavior-cloning method that represents a robot's visuomotor policy as a **conditional denoising diffusion process over the action space**. Instead of regressing observations to a single action, the policy iteratively denoises Gaussian-noise samples into action sequences conditioned on observation history. The paper benchmarks across **12 tasks from 4 manipulation benchmarks** (RoboMimic, Push-T, BlockPush, Franka Kitchen) and reports an average **46.9% improvement over prior state-of-the-art BC methods** ([LSTM-GMM](../entities/diffusion-policy.md), [IBC](../entities/pusht.md), [BET](../entities/vq-bet.md)). Real-world evaluation on UR5 and [Franka Panda](../entities/franka-panda.md) covers Push-T, 6-DoF mug flipping, sauce pouring, and periodic sauce spreading. Authors are at Columbia University, Toyota Research Institute, and MIT (Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, Shuran Song).

## Key claims

### Core formulation (§II–III)
- Visuomotor policies are formulated as **Denoising Diffusion Probabilistic Models (DDPMs)** over actions, conditioned on observations: `p(A_t | O_t)`.
- The policy infers the **action-score gradient** rather than the action directly; samples by `K` iterations of stochastic Langevin dynamics from Gaussian noise.
- Three technical contributions distinguish it from naive DDPM application:
  1. **Closed-loop action sequences via receding-horizon control.** The model predicts `T_p` future actions; only `T_a < T_p` are executed before re-planning. Balances long-horizon planning and reactivity.
  2. **Visual conditioning** (rather than joint distribution). Visual features are extracted *once per re-plan*, not per denoising iteration — drastically reducing inference cost and enabling real-time control.
  3. **Time-series Diffusion Transformer.** Transformer-based denoising backbone (alongside the CNN+FiLM variant) for tasks with high-rate action changes; reduces over-smoothing of the CNN backbone.

### Architecture details
- **CNN backbone (default recommendation)**: 1D conv U-Net with FiLM conditioning per layer; channel-wise modulation by the observation embedding (§III-A).
- **Transformer backbone**: action-token cross-attention to observation embeddings; sinusoidal step-`k` token prepended; causal mask within action tokens. More sensitive to hyperparameters but stronger for high-rate state-based control (§III-A).
- **Visual encoder**: ResNet-18 from scratch, two modifications — spatial softmax pooling (preserves spatial info), GroupNorm replacing BatchNorm (stable with EMA) (§III-B).
- **Noise schedule**: Square Cosine (iDDPM) empirically best for control (§III-C).
- **Inference acceleration**: DDIM with **100 training iterations and 10 inference iterations** → **0.1 s inference latency on Nvidia 3080** (§III-D).

### Simulation results (§V)
- 12 tasks across 4 benchmarks; success rates reported as `(max performance) / (average of last 10 checkpoints)`, averaged over 3 seeds × 50 environments = 150 evals per cell.
- **RoboMimic** (Lift, Can, Square, Transport, ToolHang) at proficient-human (`ph`) and multi-human (`mh`) data:
  - Diffusion Policy variants near-saturate Lift / Can (1.00 / 1.00) where baselines also do well, but pull substantially ahead on **Square mh (0.97 / 0.82 vs LSTM-GMM 0.86 / 0.59), Transport mh (0.68 / 0.46 vs 0.62 / 0.20), ToolHang ph (0.50 / 0.30 vs 0.67 / 0.31 → DiffusionPolicy-T 1.00 / 0.87)**.
- **Push-T** (state): DiffusionPolicy-C 0.95 / 0.91 vs LSTM-GMM 0.67 / 0.61 vs IBC 0.90 / 0.84 vs BET 0.79 / 0.70.
- **BlockPush** (multi-modal pushing): DiffusionPolicy-T `p1=0.99 / p2=0.94` vs BET 0.96 / 0.71 vs LSTM-GMM 0.03 / 0.01.
- **Franka Kitchen** (multi-stage, 4 sequential subtasks): DiffusionPolicy-C `p4=0.99` vs BET 0.44 vs LSTM-GMM 0.34 — the gap *widens* with more sequential subtasks completed.
- Headline: **average 46.9% improvement across all benchmark tasks**.

### Real-world results (§VI)
- **Push-T (UR5)**: 95% success, 0.80 IoU vs human 1.00 / 0.84. Best baselines: LSTM-GMM 20%, IBC 0%. End-to-end-trained CNN-Diffusion-Policy outperforms R3M-frozen-encoder + ImageNet variants.
- **6-DoF mug flipping (Franka Panda)**: 90% over 20 trials. LSTM-GMM 0%. Notably, the policy *sequences* multiple pushes for handle alignment and *re-grasps* dropped mugs even though those behaviors were never demonstrated.
- **Sauce pouring (Franka Panda, 6-DoF, fluid)**: 79% success / 0.74 IoU vs human 1.00 / 0.79. LSTM-GMM 0% (failed to lift the ladle in 15/20 trials; never self-terminated).
- **Sauce spreading (Franka Panda, periodic motion)**: 100% success / 0.77 coverage vs human 1.00 / 0.79. LSTM-GMM 0% (always lifted the spoon at start).
- **Robustness** (qualitative): graceful response to camera occlusion (waving hand for 3 s), block perturbation during pushing, and perturbation during the *finishing* stage — the policy aborts the end-zone retreat and returns the block to the goal *despite that behavior never being demonstrated*. Section IV-A frames this as multi-modal action distributions arising naturally from DDPM sampling.

### Training stability
- Diffusion Policy hyperparameters are largely consistent across tasks; in contrast, **IBC is prone to training instability** because of the negative-sample requirement of Info-NCE loss. This is one of the paper's quietly important practical contributions: BC methods that don't need per-task tuning are a usability step-change for real-robot work.

### Position vs. velocity control (§V-C)
- Switching from velocity control to position control **hurts BC-RNN and BET** but **helps Diffusion Policy** — the action-sequence + denoising structure means accumulated position-control errors are corrected during denoising rather than compounding.
- Diffusion Policy is also **more robust to control latency** than velocity-control baselines; maintains peak performance with up to ~4 steps simulated latency.

### Limitations (§VIII)
- Inherits behavior-cloning limitations (sub-optimal demos → sub-optimal policy; no negative-data leverage). RL extensions referenced (Hansen-Estruch IDQL, Wang DiffPo).
- Higher computation / inference latency than simpler methods (LSTM-GMM). Mitigated by action-sequence prediction and DDIM but not eliminated; high-rate control still constrains use.
- Future-work hooks: better noise schedules, faster solvers (DPM-Solver), consistency models for one-step distillation.

## Entities mentioned

- [Cheng Chi](../entities/diffusion-policy.md) (Columbia → ?), [Shuran Song](../entities/diffusion-policy.md) (Columbia, senior author) — entity pages not yet filed; first/last authorship of the paper.
- [Yilun Du](../entities/diffusion-policy.md) (MIT) — co-author; also referenced in JEPA-line work via Janner et al. trajectory-diffusion (cited).
- [Toyota Research Institute](../entities/tri.md) — TRI affiliation (Feng, Cousineau, Burchfiel).
- [Columbia University](../entities/diffusion-policy.md) and MIT — academic affiliations; not entity-tracked.
- [Franka Panda](../entities/franka-panda.md) — real-world platform for mug flipping + sauce manipulation tasks.
- UR5 — second real-world platform (Push-T); not yet an entity.
- [PushT](../entities/pusht.md) — primary 2D benchmark; this paper popularized it after IBC introduced it.
- [Diffusion Policy](../entities/diffusion-policy.md) — the method itself; this is its primary source.

### Baselines referenced
- **[IBC](../entities/ibc.md)** (Florence et al., CoRL 2021) — implicit BC via energy-based models; the work this paper most directly improves on. Originator of [PushT](../entities/pusht.md). See [IBC Paper](ibc-paper.md).
- **LSTM-GMM / BC-RNN** (RoboMimic, Mandlekar et al. 2021) — recurrent BC with Gaussian mixture output. Strong baseline; reproduced and tuned in this paper.
- **[BET](../entities/bet.md)** (Behavior Transformer; Shafiullah et al., NeurIPS 2022) — transformer + k-means action discretization. Co-authored by [Mahi Shafiullah](../entities/mahi-shafiullah.md) and [Lerrel Pinto](../entities/lerrel-pinto.md) (NYU); direct ancestor of [VQ-BeT](../entities/vq-bet.md). See [BET Paper](bet-paper.md).

## Concepts touched

- [Imitation learning](../concepts/imitation-learning.md) — the paper's training paradigm; key example of "diffusion policies" as a BC variant.
- Multi-modal action distributions — the paper's core thesis: diffusion captures multimodality without per-mode hyperparameters (k-means count, GMM components).
- Receding-horizon / model-predictive control — borrowed from classical control, fused with action-sequence prediction.
- Action sequence prediction (a.k.a. **action chunking**) — the paper popularized predicting `T_p` actions and executing `T_a` before re-planning; this convention persists across [VLA models](../concepts/vla-models.md) and downstream BC work (RUM, ACT, Pi VLAs).

## Why it matters in this wiki

- **Primary source for [Diffusion Policy](../entities/diffusion-policy.md) entity** — fills in mechanics that prior pages only cited indirectly (DDPM formulation, CNN+FiLM and Transformer backbones, DDIM acceleration, position-control finding, action-sequence prediction).
- **Primary source for [PushT](../entities/pusht.md) propagation** — IBC introduced PushT, but Diffusion Policy is what made it canonical. The paper documents the variant that the world-model literature ([LeWM](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md), [JEPA-WMs](../entities/jepa-wms.md)) inherits.
- **Origin of action-chunking + receding horizon as a robotics design pattern** — when a 2024–2026 BC paper says "we predict 16 actions and execute 8", the convention traces here.
- **Demonstrates the full empirical case for diffusion-as-policy** — 12-task simulation sweep + 4 hardware tasks across 2 platforms is the strongest single ablation backing the now-default treatment of Diffusion Policy as a baseline across the wiki's BC literature ([RUM](../entities/robot-utility-models.md) ablation §3.2 cites Diffusion Policy as runner-up; [VQ-BeT](../entities/vq-bet.md) is benchmarked against it).

## Open questions / TBD

- **DDIM paper** (Song, Meng, Ermon, ICLR 2021, arxiv 2010.02502) and **iDDPM paper** (Nichol & Dhariwal, ICML 2021) — Diffusion Policy uses DDIM at inference (10 steps) and iDDPM's square-cosine schedule, but neither has a source page yet. ([DDPM](../entities/ddpm.md) primary now filed.)
- **Cheng Chi / Shuran Song / Yilun Du** — author entity pages not yet filed; would clarify the Columbia → Stanford trajectory of the diffusion-for-robotics line.
- **R3M visual encoder** — appears in real-world Push-T ablation (R3M variant underperforms end-to-end). Not yet an entity; could become one if cited again.
- **TRI LBM (Large Behavior Model)** — primary TRI generalist policy, referenced as a baseline in [RoboCasa365 Paper](robocasa365-paper.md) but not yet a primary source. ([TRI](../entities/tri.md) parent entity now filed.)
- ~~IBC paper (Florence et al., CoRL 2021)~~ now filed as [IBC Paper](ibc-paper.md).
- ~~BET paper (Shafiullah et al., NeurIPS 2022)~~ now filed as [BET Paper](bet-paper.md).
- ~~DDPM primary~~ now filed as [DDPM Paper](ddpm-paper.md).
- ~~UMI / Universal Manipulation Interface~~ now filed as [UMI Project Page](umi-paper.md).
- ~~TRI as an organization~~ now filed as [TRI Website](tri-website.md).
