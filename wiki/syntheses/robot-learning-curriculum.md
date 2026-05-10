---
title: Robot-learning curriculum — from neurons to LeWorldModel
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, course, learning-path, jepa, diffusion-policy, vla, world-model, lewm, home-robotics]
status: outline — module pages not yet written
---

A bottom-up curriculum for building the mental model needed to read the [LeWorldModel paper](../sources/leworldmodel-paper.md) and reason about home-robotics policy-learning techniques (BC, diffusion policy, JEPA, VLA, world models).

Audience assumption (set 2026-05-10): **strong programmer, some ML and robotics exposure**. Tier 1 is therefore brisk-but-rigorous (refresher pace), not ground-zero. The bulk of the depth lives in tiers 3–4.

Each module below is scoped to become its own synthesis page (`syntheses/curriculum-NN-<slug>.md`). This hub is the syllabus; module bodies are written on signal, in order, after this outline is approved.

## Goal

Be able to read [LeWorldModel](../sources/leworldmodel-paper.md) and answer:

1. Why is "predicting next-embedding MSE plus SIGReg" a viable training signal at all? What stops the encoder from collapsing?
2. How does LeWM differ from [DINO-WM](../entities/dino-wm.md), [V-JEPA 2](../entities/v-jepa-2.md), Dreamer, TD-MPC, and PLDM along the world-model design axes?
3. Why does latent-space MPC plan up to 48× faster than foundation-model-based world models, and what does "MPC against a world model" actually mean operationally?
4. What does any of this have to do with a robot doing the dishes in a home, and is LeWM-class technique a credible path there?

Question 4 is the domain anchor — every module ends with a "what this unlocks for home robotics" pointer.

## Pedagogical principle — PushT as the connecting thread

[PushT](../entities/pusht.md) (2D T-block pushing, introduced by [IBC](../entities/ibc.md), popularized by [Diffusion Policy](../entities/diffusion-policy.md), used as the default lightweight bench in [LeWM](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md), and [JEPA-WMs](../entities/jepa-wms.md)) appears in **every tier 2+ module**. The same task is solved with progressively more powerful machinery, so each module's contribution shows up as a delta on the same benchmark. Other recurring benches: PointMaze, Reacher, Franka kitchen-style tasks ([RoboCasa](../entities/robocasa.md)).

## Module list

> [!note] Reading order
> Modules are linear by default. Tier 1 modules can be skipped or skimmed if the prereq diagnostic at the top of each one is comfortable. Tier 5 modules require all prior tiers.

### Tier 1 — ML foundations (refresher pace)

#### Module 1 — Neural networks and training
- **Concept beats:** neuron, MLP, forward pass, MSE / cross-entropy loss, gradient descent, backprop, overfitting / regularization, normalization (batch / layer), residual connections, why depth helps, Adam.
- **Why for LeWM:** every other module assumes you can read `loss = ||predictor(z_t, a_t) − z_{t+1}||²` and know what happens during a backward pass. Layer norm + residuals are the inner-loop primitive of every encoder we'll meet.
- **Anchor exercise:** train an MLP digit classifier on a tiny dataset; reason about what "the embedding before the last layer" is.
- **Future home:** `syntheses/curriculum-01-neural-networks.md`

#### Module 2 — CNNs and visual representation learning
- **Concept beats:** convolution, pooling, receptive field, feature maps, ResNet skip connections, ImageNet pretraining, fine-tuning, the meaning of "visual encoder."
- **Why for LeWM:** the "encoder" half of every JEPA. [DINO-WM](../entities/dino-wm.md) uses a frozen ViT; [LeWM](../entities/leworldmodel.md) uses a small ViT trained end-to-end. ResNet is the BC-line baseline visual encoder (used in [Diffusion Policy](../entities/diffusion-policy.md)'s real-world Push-T setup).
- **Anchor exercise:** load a ResNet-18, extract features for a batch of PushT frames, visualize the feature similarity structure.
- **Future home:** `syntheses/curriculum-02-cnns.md`

#### Module 3 — Sequence models and attention
- **Concept beats:** RNN / LSTM (briefly — for context only), attention, self-attention, multi-head, transformer block, ViT, positional encoding, causal masking.
- **Why for LeWM:** LeWM's encoder is a ViT. Its predictor is a causal autoregressive transformer over `(z_t, a_t) → z_{t+1}`. [BeT](../entities/bet.md) is a transformer over actions. [VLA models](../concepts/vla-models.md) are transformers conditioning on language.
- **Anchor exercise:** patch a 64×64 PushT frame into 8×8 tokens, run them through a 2-layer transformer, inspect attention maps.
- **Future home:** `syntheses/curriculum-03-attention-and-transformers.md`

#### Module 4 — Self-supervised learning and embeddings
- **Concept beats:** representation learning, contrastive learning (SimCLR / MoCo) vs predictive (MAE / JEPA), the [latent space](../concepts/latent-space.md) as object, **representation collapse** as a failure mode, anti-collapse families: EMA target encoders + stop-gradient (BYOL / DINO), variance / covariance regularization (VICReg, BarlowTwins), normality-based (LeWM's SIGReg).
- **Why for LeWM:** this is the module that turns the LeWM abstract from word-soup into a sensible engineering claim. SIGReg is intelligible only against the backdrop of "every prior end-to-end JEPA needed 4–6 anti-collapse hyperparameters."
- **Anchor exercise:** reproduce VICReg on CIFAR with and without the regularizer; observe collapse to constant.
- **Future home:** `syntheses/curriculum-04-self-supervised-learning.md`

### Tier 2 — Generative models for control

#### Module 5 — Generative modeling fundamentals (with a DDPM destination)
- **Concept beats:** autoencoder, VAE, energy-based models (just enough for [IBC](../entities/ibc.md)), score matching intuition, **DDPM** forward + reverse process, classifier-free guidance, conditional diffusion. [DDPM paper](../sources/ddpm-paper.md) ingest is the anchor reading.
- **Why for LeWM:** prerequisite for [Diffusion Policy](../entities/diffusion-policy.md) (Module 7). Also sharpens the contrast in Module 10 between *generative-video world models* (which are giant conditional diffusion / flow models over pixels) and JEPA (which sidesteps generation entirely).
- **Anchor exercise:** train a tiny DDPM on MNIST; sample.
- **Future home:** `syntheses/curriculum-05-generative-models.md`

### Tier 3 — Robot learning

#### Module 6 — Imitation learning and behavior cloning
- **Concept beats:** [imitation learning](../concepts/imitation-learning.md), behavior cloning as supervised learning, demonstration data, observation–action pairs, **multi-modal action distributions** (the central failure mode of vanilla MSE-BC), distribution shift / DAgger, action chunking, the canonical [PushT](../entities/pusht.md) setup.
- **Why for LeWM:** behavior cloning is the policy-side counterpart to world models. Many world-model papers (LeWM, DINO-WM) compose `BC-policy + world-model-MPC` baselines. You can't read DP / IBC / BeT without owning multi-modal action distributions as a concept.
- **Anchor exercise:** train a vanilla MSE-MLP behavior-cloning policy on PushT demos; observe it fail by averaging modes.
- **Future home:** `syntheses/curriculum-06-imitation-learning.md`

#### Module 7 — BC evolution: IBC → BeT → Diffusion Policy (PushT case study)
- **Concept beats:** energy-based BC and InfoNCE training ([IBC](../entities/ibc.md)); k-means action discretization + transformer ([BeT](../entities/bet.md)); conditional DDPM over action chunks ([Diffusion Policy](../entities/diffusion-policy.md)); receding-horizon execution; visual encoders for policy (ResNet vs end-to-end); [UMI](../entities/umi.md) data collection (one paragraph — context for "where the demonstrations come from").
- **Why for LeWM:** this is the *policy-learning lineage* the wiki has filed end-to-end ([IBC paper](../sources/ibc-paper.md), [BeT paper](../sources/bet-paper.md), [Diffusion Policy paper](../sources/diffusion-policy-paper.md), [UMI](../sources/umi-paper.md), [DDPM paper](../sources/ddpm-paper.md)). LeWM's ablations against [DINO-WM](../entities/dino-wm.md) implicitly ride on this lineage. Diffusion Policy is also the *thing on the other side* of "JEPA world model + planner" — they're both ways to get from PushT pixels to actions.
- **Anchor exercise:** run pretrained Diffusion Policy on PushT; inspect a sampled action trajectory; quantify multi-modality.
- **Future home:** `syntheses/curriculum-07-bc-lineage-pusht.md`

#### Module 8 — Reinforcement learning, enough to read a paper
- **Concept beats:** MDP, return, value function, policy, on-policy vs off-policy, policy gradient (REINFORCE → PPO sketch), Q-learning sketch, **model-free vs model-based RL**, Dreamer-class latent imagination as a model-based-RL technique (so the LeWM Dreamer / TD-MPC baselines parse).
- **Why for LeWM:** LeWM compares against Dreamer (task-specific reward) and TD-MPC (state-based). Without knowing what reward, value, and policy gradient are, those baseline columns are illegible. RL is *not* the focus of this curriculum — read for vocabulary, not implementation.
- **Anchor exercise:** read a Dreamer-V3 figure caption out loud and have it make sense.
- **Future home:** `syntheses/curriculum-08-rl-vocabulary.md`

#### Module 9 — Vision-Language-Action models (VLA)
- **Concept beats:** [VLA](../concepts/vla-models.md) = vision encoder + language tokens + action head; instruction-conditioned policies; major instances ([NVIDIA GR00T](../entities/nvidia-groot.md), π0 / [Physical Intelligence](../entities/physical-intelligence.md), [Gemini Robotics](../entities/gemini-robotics.md), Helix); how VLAs differ from BC (instruction-following, multi-task generalization); why VLAs *aren't* world models (they emit actions, not next states).
- **Why for LeWM:** VLAs are the dominant paradigm for home-robotics generalists in 2025–2026. Knowing how they relate to (and don't replace) world models is essential for placing LeWM in the field. [VLA-JEPA](../entities/vla-jepa.md) is the explicit cross-over point — JEPA used as auxiliary loss inside a VLA.
- **Anchor exercise:** sketch the data flow for π0 vs Diffusion Policy vs LeWM-MPC on the same PushT episode.
- **Future home:** `syntheses/curriculum-09-vla.md`

### Tier 4 — World models

#### Module 10 — World models, broad
- **Concept beats:** [world model](../concepts/world-model.md) functional definition; the four families (generative-video, JEPA / latent-prediction, frozen-foundation-feature, Dreamer-style reward-conditioned); MPC vs CEM vs gradient-based planning; planning horizon and compounding error; the [generative-video vs JEPA](generative-video-vs-jepa-world-models.md) tradeoff.
- **Why for LeWM:** LeWM is "JEPA, end-to-end-trained, with MPC planner." Every word in that sentence comes from this module. Without a clean four-way taxonomy, the LeWM contribution looks like noise.
- **Anchor exercise:** write a 3-line MPC loop pseudocode that plans against a learned next-state predictor and a cost function.
- **Future home:** `syntheses/curriculum-10-world-models.md`

#### Module 11 — JEPA in depth
- **Concept beats:** what "joint embedding" means (per [JEPA concept page](../concepts/jepa.md)); V-JEPA 1 → [V-JEPA 2](../entities/v-jepa-2.md) → V-JEPA 2-AC → V-JEPA 2.1 progression; [DINO-WM](../entities/dino-wm.md) (frozen-encoder JEPA-adjacent) vs end-to-end JEPA (LeWM, PLDM); [JEPA-WMs](../entities/jepa-wms.md) on real Franka; action conditioning; the collapse problem revisited.
- **Why for LeWM:** LeWM is a single point in this design space. Need the surrounding axes to evaluate why "no EMA, no stop-grad, no frozen encoder" is a real claim and not a marketing line.
- **Anchor exercise:** annotate the LeWM architecture figure with which design choices match V-JEPA 2 and which differ.
- **Future home:** `syntheses/curriculum-11-jepa-deep.md`

#### Module 12 — LeWorldModel paper deep-dive
- **Concept beats:** the [LeWM paper](../sources/leworldmodel-paper.md) section by section; **SIGReg derivation** (random unit projection → empirical CDF → Anderson-Darling-style normality test → backprop through the test statistic); the two-loss claim (next-embedding MSE + SIGReg); 4-environment benchmark suite (PushT, PointMaze, Reacher, Cube); planning protocol; surprise evaluation; latent probing; comparison table against PLDM / DINO-WM / Dreamer / TD-MPC.
- **Why for LeWM:** this is the destination. By module 12, every term should already be familiar — the deep-dive consolidates rather than introduces.
- **Anchor exercise:** install [LeWM](../sources/lewm-github.md) per [the howto](leworldmodel-howto.md); reproduce a single PushT eval at a pretrained checkpoint.
- **Future home:** `syntheses/curriculum-12-lewm-deep-dive.md`

### Tier 5 — Home robotics integration

#### Module 13 — Home robotics — the deployment reality
- **Concept beats:** [Stretch](../entities/stretch.md) as the de-facto research platform ([why](stretch-as-assistive-platform.md)); [RUM](../entities/robot-utility-models.md) and [OK-Robot](../entities/ok-robot.md) as the "real-data" path; the AI Index 89.4% RLBench vs 12.4% [BEHAVIOR-1K](../sources/stanford-hai-ai-index-2026.md) gap; physically assistive robotics ([systematic review](../sources/nanavati2024-physically-assistive-robots-review.md)); [autonomy-preference finding](../syntheses/levels-of-autonomy-in-assistive-robotics.md); why JEPA could matter here ([assistive-robotics R&D landscape](assistive-robotics-research-landscape.md)).
- **Why for LeWM:** the user's actual goal. LeWM and friends are not deployed in homes today. This module places the technique inside the deployment reality and identifies which barriers it could plausibly move (data efficiency, planning speed) and which it won't (whole-body manipulation, dressing, bathing, real-world robustness).
- **Anchor exercise:** read [DINO-WM on Stretch experiment plan](dino-wm-on-stretch-experiment.md) and [LeWM on Stretch feasibility](lewm-on-stretch-feasibility.md); state the one experiment most worth running.
- **Future home:** `syntheses/curriculum-13-home-robotics-deployment.md`

#### Module 14 — Capstone: hands-on LeWM, then a real-platform experiment design
- **Concept beats:** end-to-end practical loop. Reproduce LeWM PushT from scratch ([detailed scope already filed](lewm-hello-world-project-scope.md)); install / train / eval per [the howto](leworldmodel-howto.md); design the smallest credible LeWM-on-Stretch or DINO-WM-on-Stretch experiment ([feasibility analysis](lewm-on-stretch-feasibility.md)).
- **Why for LeWM:** the only way to know if you understood it is to train it. The Stretch experiment design is the deliverable that demonstrates you can place LeWM in a home-robotics research context.
- **Anchor exercise:** the capstone *is* the exercise.
- **Future home:** `syntheses/curriculum-14-capstone.md`

## Module dependency graph

```
1 → 2 → 3 → 4 ─┐
              ├→ 5 ─┐
              │     ├→ 7 ─┐
              │     │     ├→ 9 ─┐
              │     6 ────┘     │
              │                 │
              └─────────────────┼→ 10 → 11 → 12 ─┐
                                │                ├→ 14
                            8 ──┘                │
                                                 │
                                            13 ──┘
```

- 1–4 are linear.
- 5 (generative) depends on 1–4 and unlocks 7.
- 6 (BC fundamentals) depends on 1–4 and unlocks 7.
- 7 (BC lineage) needs 5 and 6.
- 8 (RL vocab) only depends on 1; can be done any time before 10.
- 9 (VLA) depends on 7 (it's a generalization).
- 10 (world models broad) depends on 4, 5, 6, 8.
- 11 (JEPA depth) depends on 4, 10.
- 12 (LeWM deep-dive) depends on 11.
- 13 (home robotics) only depends on 6 and 9 — can run in parallel with 10–12.
- 14 (capstone) depends on 12 and 13.

## What's already in the wiki vs. what each module needs to add

| Module | Existing wiki coverage | Needs new |
|---|---|---|
| 1 NN basics | none | full module |
| 2 CNNs | none | full module |
| 3 Attention / transformers / ViT | none | full module |
| 4 SSL & embeddings | partial in [latent-space](../concepts/latent-space.md), [JEPA](../concepts/jepa.md) | broader SSL framing, collapse taxonomy |
| 5 Generative / DDPM | [DDPM paper](../sources/ddpm-paper.md) source ingest | derivation walkthrough + pedagogy |
| 6 Imitation learning | [concept](../concepts/imitation-learning.md), [PushT entity](../entities/pusht.md) | multi-modality emphasis + worked example |
| 7 BC lineage (IBC/BeT/DP) | [IBC](../sources/ibc-paper.md), [BeT](../sources/bet-paper.md), [Diffusion Policy](../sources/diffusion-policy-paper.md), [UMI](../sources/umi-paper.md) all ingested | linear narrative tying them on PushT |
| 8 RL vocab | none | full module |
| 9 VLA | [concept](../concepts/vla-models.md), [GR00T](../entities/nvidia-groot.md), [Gemini Robotics](../entities/gemini-robotics.md), [Physical Intelligence](../entities/physical-intelligence.md) | π0, Helix entity / source ingests; VLA-vs-WM contrast |
| 10 World models | [concept](../concepts/world-model.md), [WM simulators concept](../concepts/world-model-simulators.md), [generative-video vs JEPA synthesis](generative-video-vs-jepa-world-models.md) | MPC explainer; Dreamer / TD-MPC source ingests would help |
| 11 JEPA depth | [concept](../concepts/jepa.md), [V-JEPA 2 paper](../sources/v-jepa-2-paper.md), [V-JEPA 2.1](../sources/v-jepa-2-1-paper.md), [JEPA-WMs](../sources/jepa-wms-paper.md), [DINO-WM](../sources/dino-wm-paper.md), [VLA-JEPA](../sources/vla-jepa-paper.md) | linear narrative + collapse-fix taxonomy |
| 12 LeWM deep-dive | [paper ingest](../sources/leworldmodel-paper.md), [howto](leworldmodel-howto.md), [GitHub](../sources/lewm-github.md), [feasibility](lewm-on-rosorin-pro-feasibility.md), [Stretch feasibility](lewm-on-stretch-feasibility.md) | SIGReg math walkthrough |
| 13 Home robotics deployment | rich — see [assistive-robotics R&D landscape](assistive-robotics-research-landscape.md), [Stretch as platform](stretch-as-assistive-platform.md), [autonomy levels](levels-of-autonomy-in-assistive-robotics.md) | curriculum-shaped framing |
| 14 Capstone | [hello-world Project 1](lewm-hello-world-project-scope.md), [Stretch feasibility](lewm-on-stretch-feasibility.md), [DINO-WM on Stretch](dino-wm-on-stretch-experiment.md) | nothing new — points to the existing artifacts |

## Effort estimate (rough)

Self-paced with strong-coder-some-ML background, ~5–10 hr/module reading + 2–5 hr/exercise:

- Tier 1 (1–4): ~25–40 hr
- Tier 2 (5): ~10–15 hr
- Tier 3 (6–9): ~30–50 hr
- Tier 4 (10–12): ~25–40 hr
- Tier 5 (13–14): ~20–60 hr (capstone is the variable)

Total: ~110–205 hr depending on capstone depth. Realistic 3–6 month evening pace.

## Open scoping questions for the user

1. **Tier 1 brevity.** Is 4 modules across NN / CNN / attention / SSL the right granularity, or would you rather collapse 1–3 into a single "ML primer" module since you've seen this material before?
2. **Math depth.** How much of the SIGReg derivation in module 12 should be done by hand vs. understood at the level of "an Anderson-Darling-style test, differentiable through the projection"? The former adds significant effort.
3. **Diffusion math depth.** Same question for DDPM — full forward/reverse derivation with KL bounds, or "you can write the training loop and inference loop, you understand classifier-free guidance, that's enough"?
4. **Should module 14 actually run on hardware,** or stay paper-only? The wiki has [LeWM-on-Stretch feasibility](lewm-on-stretch-feasibility.md) but you don't yet own a Stretch — running the capstone on simulator-only PushT/PointMaze is the realistic version unless that changes.
5. **Skipped entirely:** classical robotics (kinematics, control, dynamics), ROS, perception pipelines (SLAM / segmentation), formal MDP / RL theory beyond paper-reading vocabulary. Confirm these are out of scope, or flag the ones you want added.

## Mentioned in
- [Index](../index.md) (curriculum entry)
- [Log](../log.md)
