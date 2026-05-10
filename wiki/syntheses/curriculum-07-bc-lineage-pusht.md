---
title: Curriculum Module 7 — BC lineage on PushT (IBC → BeT → DP)
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-7, behavior-cloning, ibc, bet, diffusion-policy, pusht, multi-modal-actions, action-chunking, ddpm]
prereqs: [curriculum-05, curriculum-06]
status: draft
---

> [!note] Curriculum context
> This is **Module 7** of the [Robot-learning curriculum](robot-learning-curriculum.md). It assumes you've done **Module 5** (generative models / DDPM) and **Module 6** (imitation learning + behavior cloning + the multi-modal-action failure mode). It feeds **Module 9** (VLAs) and is a sibling of **Module 10** (world models) — the two modules cover the two ways to get from PushT pixels to robot actions.
>
> Acronyms used here are also in the [Glossary](../glossary.md). First-mention links go there.

## What this module is

A close reading of three behavior-cloning papers — [Implicit BC](../sources/ibc-paper.md), [Behavior Transformer](../sources/bet-paper.md), and [Diffusion Policy](../sources/diffusion-policy-paper.md) — through one lens: **the multi-modal action distribution problem**, and what successive papers do to solve it. We pin the story to the [PushT](../entities/pusht.md) benchmark, which IBC introduced and the field has been re-running ever since.

By the end of the module you should be able to:

1. Explain in one paragraph why a vanilla [MSE](../glossary.md#mse)-regression BC policy fails on PushT.
2. Write the loss function and training procedure for each of IBC, BeT, and Diffusion Policy from memory.
3. Explain action chunking and receding-horizon execution, and why they help.
4. Place each of the three on the same axis as the [world-model](../concepts/world-model.md) approach: both are ways to map PushT pixels to actions; only one tries to model environment dynamics.

## Pedagogical principle — one task, three models

PushT is a 2D pushing task: a circular pusher must shove a T-shaped block to a target pose using only top-down image input. Why this task? Two reasons.

**Multi-modality is unavoidable.** A human teleoperator demonstrating "push the T into the target" can choose to approach from the left or from the right. Both work; they're symmetric. A BC dataset will contain both. A regression policy that averages "go left" and "go right" predicts "stand still" — and fails. PushT was *engineered* so MSE-BC fails by design.

**It's tiny.** Single 2D plane, no contact dynamics beyond rigid pushing, ~96×96 pixel observations, two-DOF action. You can train a respectable policy on a single GPU in an hour. That makes it the rare benchmark used identically in BC-line and world-model-line work — see [LeWM](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md), and [JEPA-WMs](../entities/jepa-wms.md), all of which evaluate on PushT alongside richer benches.

The PushT data: ~200 expert demos collected by humans, each ~25–50 timesteps. Observation = top-down RGB image (or low-dimensional state in some variants). Action = 2D end-effector setpoint.

## The failure mode: multi-modal action distributions

Plain BC fits a deterministic regressor `π_θ(s) = a` against `(s, a)` pairs from demos using MSE loss. This is fine when, given a state, there's one action the expert always took. It is silently broken when the expert takes any of several different actions in similar states.

Concretely: for state `s` (T-block in some position), demos contain action `a_left` ~50% of the time and `a_right` ~50% of the time. The MSE-optimal predictor outputs `(a_left + a_right) / 2`, which is neither pushing-from-left nor pushing-from-right — and that point may be inside the block, off the table, or otherwise nonsensical.

Three escape routes:

1. **Make the policy implicit and energy-based** — IBC.
2. **Discretize the action space and predict a category, then refine** — BeT.
3. **Model the action distribution explicitly with a generative model over actions** — Diffusion Policy.

The lineage runs IBC (2021) → BeT (2022) → Diffusion Policy (2023). Each paper benchmarks on PushT and ablates against the previous. The same lead-author cluster (Cheng Chi, Shuran Song, Russ Tedrake, with crossovers to NYU's Lerrel Pinto via [BeT](../entities/bet.md)) carries the line forward and into [UMI](../entities/umi.md) for data collection.

## IBC — Implicit Behavior Cloning (Florence et al., CoRL 2021)

[Source page](../sources/ibc-paper.md). [Entity](../entities/ibc.md).

**Idea.** Replace the explicit regressor `π_θ(s) = a` with an [energy-based model](../glossary.md#ebm) `E_θ(s, a)` and define the policy as `π(s) = argmin_a E_θ(s, a)`. The energy function can have multiple low-energy regions for the same `s` — that's how the model represents "either left or right is fine." Inference samples or optimizes over actions to find a low-energy one.

**Training.** [InfoNCE](../glossary.md#infonce) (a [contrastive](../glossary.md#contrastive-learning) loss family). For each demo `(s, a_pos)`, sample `K` negative actions `a_neg` (uniform random, MCMC, or otherwise), and train so the positive scores higher than the negatives:

```
L_IBC(s, a_pos, {a_neg}) = -log [ exp(-E_θ(s, a_pos)) / (exp(-E_θ(s, a_pos)) + Σ_k exp(-E_θ(s, a_neg^k))) ]
```

**Inference.** Optimize over actions: gradient descent in action space (DFO-MCMC variants in the paper) or sample-and-rank.

**What works.** IBC handles multi-modal action distributions cleanly on PushT — it's the paper that *defines* the PushT benchmark — and substantially outperforms MSE-BC and stochastic-MLP-BC across simulation and a real UR5e. On 1D demonstrations it matches the discontinuous structure of expert behavior that MLPs blur away.

**What doesn't.** Two persistent issues:
- **InfoNCE is unstable and slow.** Negative sampling is sensitive; training takes longer than supervised regression.
- **Inference is iterative.** Each control-loop tick runs an action-space optimization, not a feedforward pass. Latency is real.
- **Limited capacity for very complex distributions.** The Diffusion Policy paper later shows IBC underperforms on hard RoboMimic tasks; the EBM is hard to train to capture sharp multi-modal structure with many modes.

**Why it matters.** IBC is the *first* paper to take multi-modal action distributions in BC seriously and the proximate ancestor of Diffusion Policy. PushT comes from this paper. Read it for: the multi-modality problem statement, the EBM-as-policy framing, and InfoNCE in action space.

## BeT — Behavior Transformer (Shafiullah et al., NeurIPS 2022)

[Source page](../sources/bet-paper.md). [Entity](../entities/bet.md).

**Idea.** Avoid generative modeling of continuous actions by **discretizing**. Cluster the demonstration actions into `K` categories with k-means; predict the cluster ID with a [transformer](../glossary.md#transformer); then predict a small continuous offset *within* the cluster.

**Architecture.**
1. **k-means on actions.** Run k-means (`K=64` or so) on `{a_t}` from all demos. Each demo action is now `(cluster_id, offset_within_cluster)`.
2. **Transformer over (state, history).** Input the recent observation history; output two heads:
   - Categorical head over `K` cluster IDs (cross-entropy loss).
   - Regression head predicting the continuous offset.
3. **Inference.** Sample a cluster ID from the categorical, add the predicted offset.

**Why this handles multi-modality.** The categorical head can put mass on multiple clusters (left-push and right-push live in different clusters). Sampling picks one. The offset is then a regression *within* a cluster — small enough that within-cluster averaging doesn't blur modes.

**Why a transformer.** The paper's larger frame is *sequence-to-sequence* BC: sometimes the right action depends on history, not just the current frame. A transformer over recent frames lets the policy condition on temporal context. In practice the receptive field is small (a few frames), but the architecture choice matters for harder benchmarks.

**What works.** Strong on benchmarks that are sequence-modeling-flavored — BeT outperforms MSE-BC and IBC on BlockPush (multi-block manipulation with order ambiguity) where action distributions are very obviously multi-modal in time and space.

**What doesn't.** k-means clustering is a fixed pre-processing step; the cluster boundaries may not match the actual mode structure of the data. On hard, long-horizon tasks (Franka Kitchen multi-stage), BeT shows weakness — the discrete head loses information.

**Successor: VQ-BeT.** [VQ-BeT](../entities/vq-bet.md) (Lee et al. 2024) replaces k-means with a *learned* vector-quantized codebook trained jointly with the transformer. Same conceptual structure, better empirical results — top performer in the [Robot Utility Models](../entities/robot-utility-models.md) ablation.

**Why it matters.** BeT is the bridge between IBC (continuous-action EBM) and Diffusion Policy (continuous-action generative model): "what if we just discretize?" is a natural intermediate, and the answer turns out to be "you get something simple that works on some tasks and fails on others." That motivates the move to a more expressive continuous-action generative model — i.e., DDPM.

## Diffusion Policy (Chi et al., RSS 2023)

[Source page](../sources/diffusion-policy-paper.md). [Entity](../entities/diffusion-policy.md).

**Idea.** Use a conditional [DDPM](../sources/ddpm-paper.md) (or [DDIM](../glossary.md#ddim) for inference) to model the action distribution `p(A_t | O_t)` directly. Action = noise-prediction network output, sampled by iterative denoising. No discretization, no implicit-energy hack.

This is the cleanest answer to "how do you represent an arbitrarily complex multi-modal action distribution conditioned on observations?" — model it as a conditional generative process and sample from it.

**Architecture.**
- **Action chunk.** Predict a sequence of `T_a` future actions at once (typical: `T_a = 8` or `16`), not just the next one.
- **Observation conditioning.** A short observation history `O_t` (typical: 2 frames) is encoded once and used to condition the denoising network at every diffusion step.
- **Visual encoder.** ResNet-18 (modified) per frame in the original paper; can also be end-to-end trained or pretrained ([R3M](../glossary.md#r3m) appears as an ablation).
- **Denoising network.** Either a CNN-based U-Net over the action chunk (for low-dim actions) or a transformer (for higher-dim or long-chunk variants).
- **Noise schedule.** Square-cosine schedule from [iDDPM](../glossary.md#iddpm) (Nichol & Dhariwal 2021); 100 training steps, 10 inference steps via DDIM.

**Training loss.** Standard DDPM: predict the noise `ε` added to the ground-truth action chunk at a random diffusion step `k`, conditioned on observations:

```
L = MSE( ε_k , ε_θ(A_t + ε_k, k, O_t) )
```

This is exactly the [DDPM](../sources/ddpm-paper.md) training objective with `x = action chunk` and conditioning `O_t`.

**Inference: receding horizon.**
1. Encode current observation history `O_t`.
2. Denoise from random noise to a full action chunk `A_t = (a_t, a_{t+1}, ..., a_{t+T_a−1})`. (10 DDIM steps, ~10 ms on a small model.)
3. Execute the **first few** actions (`T_e ≪ T_a`) on the robot.
4. Re-observe and repeat.

**Why action chunking helps.** Predicting a chunk regularizes the policy: it has to commit to a coherent short trajectory rather than oscillate between modes per timestep. This dramatically reduces the "mode flickering" that plagues per-timestep multi-modal policies.

**Why receding horizon.** Even with chunking, the world drifts from what the model expected by step 5 or 6 of an 8-step chunk. Re-planning every few steps closes the loop.

**What works.** A lot.
- **+46.9% average improvement across 12 benchmark tasks** vs the previous-best BC baseline ([Diffusion Policy paper](../sources/diffusion-policy-paper.md) headline).
- Real-world: 95% on Push-T (UR5e), 90% on mug flip, 79% on sauce pouring, 100% on sauce spreading.
- Beats IBC and BeT on RoboMimic-Hard tasks where their respective failure modes (training instability for IBC; rigid clustering for BeT) bite.
- **Setting:** the Diffusion Policy paper became the BC reference architecture for ~2 years and is the implicit baseline that any new BC method now has to beat.

**What's still hard.**
- Inference latency. 10 DDIM steps × per-step cost = real time on CPU; fine on GPU. Embedded deployment is non-trivial.
- Compute cost vs simple regression. ~10× the FLOPs per action.
- *Goal* conditioning (vs just observation conditioning) is its own line of work — Diffusion Policy is unconditioned on language; that's [VLA](../concepts/vla-models.md) territory ([Module 9](robot-learning-curriculum.md)).

**Why it matters.** Diffusion Policy is the proximate ancestor of every modern BC-style policy in the wiki, and [π0](../sources/pi-zero-paper.md) extends the same idea (conditional generative-model action head) by swapping DDPM for **flow matching** and adding a VLM backbone. The architectural recipe — `(observation encoder) + (conditional generative action head) + (action chunking) + (receding horizon)` — is the contemporary default.

## Visual encoders for policies — a side note

All three papers depend on a frozen-or-trained visual encoder mapping pixels to a feature vector. Practical choices in this lineage:

- **End-to-end ResNet-18** (Diffusion Policy default). Trained jointly with the action head. Cheap and effective when you have enough demos.
- **Pretrained R3M** (Nair et al. 2022). A manipulation-pretrained encoder; appears as a Diffusion Policy ablation. Sometimes wins on small datasets, sometimes loses to end-to-end ResNet-18.
- **Frozen DINOv2** ([DINOv2](../entities/dinov2.md)). The dominant choice in the *world-model* lineage ([DINO-WM](../entities/dino-wm.md)). Less common as a BC visual encoder but cited as a strong default.

The encoder choice is mostly orthogonal to the action-head choice. You can pair any of these encoders with IBC, BeT, or Diffusion Policy. The Diffusion Policy paper's ablations are a good reference point for what changes which numbers.

> [!note] Curriculum cross-link
> Visual encoders are covered in [Module 2](robot-learning-curriculum.md) (CNNs / ResNet) and [Module 3](robot-learning-curriculum.md) (ViTs); the *self-supervised* pretraining of encoders like DINOv2 is in [Module 4](robot-learning-curriculum.md).

## Where the demonstrations come from — UMI in one paragraph

[UMI](../sources/umi-paper.md) (Universal Manipulation Interface, Chi et al., RSS 2024) is the data-collection-side companion to Diffusion Policy from the same lead author. Hand-held gripper with a wrist-mounted GoPro; collected demos transfer zero-shot to UR5e and Franka by mounting the same gripper at a known offset. ~111 demos/hour throughput on novel tasks. Why mention it here: BC-class methods are dataset-limited, and UMI is what made it cheap enough to collect the kind of diverse data the next generation of policies (including [π0](../sources/pi-zero-paper.md) and [Robot Utility Models](../entities/robot-utility-models.md), via Stick-v2 inspired by UMI) actually train on. Module 13 (home robotics) revisits the data-collection question; for now, the takeaway is that "demos" is not free — and the reason these BC papers all benchmark on PushT is partly that PushT is the rare task where collecting good demos is cheap.

## The bridge to Module 10 — BC lineage vs world models

This is the most important framing in the curriculum, and it's the reason this module exists in the order it does.

There are **two** ways to get from PushT pixels to robot actions:

1. **BC lineage (this module).** Train a function `π_θ: O_t → A_t` from `(observation, action)` demonstration pairs. The policy is the model.
2. **World-model lineage ([Module 10](robot-learning-curriculum.md)).** Train a function `f_θ: (z_t, a_t) → z_{t+1}` from observation sequences (action-conditioning where available). At deployment, use [MPC](../glossary.md#mpc) to plan actions against `f_θ` and a goal cost. The dynamics model is the model; planning produces actions.

Both produce an action at every control tick. The differences:

| Axis | BC (Module 7) | World-model + MPC (Module 10) |
| --- | --- | --- |
| **What's learned** | direct policy `O → A` | dynamics `(z, a) → z'` |
| **Training data** | `(observation, action)` pairs | observation sequences (sometimes action-conditioned) |
| **Action selection** | sample from the policy | optimize the cost-of-rollout over candidate `a` sequences |
| **Multi-modality** | handled by the policy class (EBM / discrete / DDPM / flow) | handled by the planner (sample multiple plans, pick best) |
| **Goal specification** | implicit in the data | explicit cost function |
| **Generalization to new goals** | requires re-training or instruction-conditioning | re-plan with a new cost; same model |

[LeWM](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md), and [V-JEPA 2-AC](../entities/v-jepa-2.md) are the world-model-line answers to PushT. Their ablations against [Diffusion Policy](../entities/diffusion-policy.md)-style BC baselines are the reason this module had to exist before [Module 11](robot-learning-curriculum.md) (JEPA depth) and [Module 12](robot-learning-curriculum.md) (LeWM deep-dive). When you read the LeWM paper's results table and see "BC" or "DP" in a column header, this module is what that column represents.

## Anchor exercise

The curriculum's anchor exercise for this module is:

> **Run pretrained Diffusion Policy on PushT; inspect a sampled action trajectory; quantify multi-modality.**

Concrete suggestion:

1. Clone [diffusion_policy](https://github.com/columbia-ai-robotics/diffusion_policy) and follow the README to download a pretrained PushT checkpoint and run a single rollout.
2. Modify the inference loop to **sample 10 action chunks** at a fixed start state (don't re-observe between samples). Plot all 10 in 2D.
3. You should see the policy choosing different push-direction modes across samples — this is the multi-modal action distribution made visible.
4. Repeat with an MSE-BC baseline (the paper's `LSTM-GMM` or `MLP` ablation, or roll your own MSE-MLP). The samples will collapse to a narrow region, often inside the block.
5. Time the inference. With 10 DDIM steps on a small CNN U-Net, expect single-digit milliseconds per chunk on a consumer GPU. This is the latency budget Module 12's MPC-against-LeWM has to compete with.

If you're short on time, the [LeWM howto](leworldmodel-howto.md) covers the LeWM side and notes how to install the same `stable-worldmodel` env zoo PushT environment used by both lines of work.

## Recommended reading

In order:

1. **[Diffusion Policy paper](../sources/diffusion-policy-paper.md)** — the centerpiece. §I motivation, §II DDPM tutorial, §III the policy formulation, §V experiments. Skip the appendix on first pass.
2. **[DDPM paper](../sources/ddpm-paper.md)** — Module 5 prerequisite; re-read the simplified loss derivation if it's hazy.
3. **[IBC paper](../sources/ibc-paper.md)** — read for the multi-modality problem statement and the InfoNCE-in-action-space training procedure. The DFO-MCMC inference variants are skippable on first pass.
4. **[BeT paper](../sources/bet-paper.md)** — the shortest of the three. Read for the discretization-as-policy-architecture argument and the cross-entropy + offset two-head structure. Note the BlockPush numbers as the "BeT wins" benchmark.
5. **[UMI paper](../sources/umi-paper.md)** — one section ("data collection") for context.

If you have an extra hour, the [VQ-BeT](../entities/vq-bet.md) paper closes the BeT line and is referenced by [Robot Utility Models](../entities/robot-utility-models.md). And [π0](../sources/pi-zero-paper.md) is the obvious next step — same architectural recipe, flow-matching head, VLM backbone.

## What you should now be able to do

- Read the LeWM, DINO-WM, V-JEPA 2-AC, and JEPA-WMs papers' BC-baseline columns and know which paper each baseline name refers to.
- Read a new BC paper and immediately classify its action head (regression / energy-based / discrete / DDPM / flow / autoregressive) and observation conditioning (frame stack / sequence model / VLM).
- Explain to yourself why the world-model lineage is *not* a strictly better answer: BC is simpler, has fewer moving parts, and benefits directly from more demonstrations; the world-model lineage's bet is that data is better spent on dynamics than on (observation, action) pairs. Module 10 picks up that thread.

## Related curriculum modules

- **[Module 5 — Generative models / DDPM](robot-learning-curriculum.md)** — prerequisite for the Diffusion Policy section.
- **[Module 6 — Imitation learning + BC fundamentals](robot-learning-curriculum.md)** — prerequisite for the multi-modality problem statement.
- **[Module 9 — VLAs](robot-learning-curriculum.md)** — the next step after Diffusion Policy: same recipe + VLM backbone + language conditioning.
- **[Module 10 — World models, broad](robot-learning-curriculum.md)** — the alternative answer to the same PushT problem.
- **[Module 12 — LeWM deep-dive](robot-learning-curriculum.md)** — where the BC lineage shows up as baseline columns in the LeWM results tables.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../index.md)

## Open questions / TBD

- **VQ-BeT primary source.** Currently filed only as an [entity](../entities/vq-bet.md); a source-page ingest of Lee et al. 2024 would close the BeT lineage end to end.
- **DDIM and iDDPM source pages.** Both are referenced by Diffusion Policy and used at inference and in the noise schedule respectively; neither has a source page yet.
- **Cheng Chi / Shuran Song / Russ Tedrake** author entity pages — would anchor the Diffusion Policy / UMI / Push-T-line research thread.
- **Multi-modality quantification.** The anchor exercise as written is qualitative ("you should see different modes"). A quantitative version (mode count via clustering, KL between sampled action distributions) would be a richer artifact.
