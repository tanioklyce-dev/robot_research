---
title: Robot-learning curriculum — from neurons to LeWorldModel
type: synthesis
created: 2026-05-10
updated: 2026-05-11
tags: [curriculum, course, learning-path, jepa, diffusion-policy, vla, world-model, lewm, home-robotics]
status: "complete — all 14 modules drafted 2026-05-10. Reader-traversable bottom-up. Module bodies may be deepened or revised on signal."
---

A bottom-up curriculum for building the mental model needed to read the [LeWorldModel paper](../sources/leworldmodel-paper.md) and reason about home-robotics policy-learning techniques (behavior cloning, diffusion policy, JEPA, VLA, world models).

Audience assumption (set 2026-05-10): **strong programmer, some ML and robotics exposure**. Tier 1 is therefore brisk-but-rigorous (refresher pace), not ground-zero. The bulk of the depth lives in tiers 3–4.

Each module below is scoped to become its own synthesis page (`syntheses/curriculum-NN-<slug>.md`). This hub is the syllabus; module bodies are written on signal, in order, after this outline is approved.

> [!note] Acronyms — see the [Glossary](../glossary.md)
> Every acronym used below is also defined in the wiki's [Glossary](../glossary.md). Each module spells out acronyms on first mention with a link to the glossary entry. Reach for the glossary the first time any term is unclear.

> [!note] Video overview — recommended before starting
> [Welch Labs — "Yann LeCun's $1B Bet Against LLMs" (2026-05-01, ~37 min)](../sources/welchlabs-lecun-1b-bet-against-llms.md) is a popular-explainer that walks the same arc this curriculum ends on: blurry generative-video → Siamese networks → representation collapse → Barlow Twins → DINO → JEPA / world models, with on-camera LeCun framing. **Watch it before Module 1** as a non-technical orientation to *why* the curriculum points at JEPA / [LeWM](../entities/leworldmodel.md) at all. Tier 1 is the same story rebuilt rigorously from first principles.

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

#### [Module 1](curriculum-01-neural-networks.md) — Neural networks and training
- **Concept beats:** neuron, [MLP (multi-layer perceptron)](../glossary.md#mlp), forward pass, [MSE (mean squared error)](../glossary.md#mse) / [CE (cross-entropy)](../glossary.md#ce) loss, [SGD (stochastic gradient descent)](../glossary.md#sgd), backprop, overfitting / regularization, normalization ([BN — batch](../glossary.md#bn) / [LN — layer](../glossary.md#ln)), residual connections, why depth helps, [Adam](../glossary.md#adam).
- **Why for LeWM:** every other module assumes you can read `loss = ||predictor(z_t, a_t) − z_{t+1}||²` and know what happens during a backward pass. Layer norm + residuals are the inner-loop primitive of every encoder we'll meet.
- **Anchor exercise:** train an MLP digit classifier on a tiny dataset; reason about what "the embedding before the last layer" is.
- **Module page:** [Curriculum Module 1 — Neural networks and training](curriculum-01-neural-networks.md) **(drafted 2026-05-10)**.

#### [Module 2](curriculum-02-cnns.md) — [CNNs (convolutional neural networks)](../glossary.md#cnn) and visual representation learning
- **Concept beats:** convolution, pooling, receptive field, feature maps, [ResNet (residual network)](../glossary.md#resnet) skip connections, ImageNet pretraining, fine-tuning, the meaning of "visual encoder."
- **Why for LeWM:** the "encoder" half of every [JEPA](../glossary.md#jepa). [DINO-WM](../entities/dino-wm.md) uses a frozen [ViT (vision transformer)](../glossary.md#vit); [LeWM (LeWorldModel)](../glossary.md#lewm) uses a small ViT trained end-to-end. ResNet is the [BC (behavior cloning)](../glossary.md#bc)-line baseline visual encoder (used in [Diffusion Policy](../entities/diffusion-policy.md)'s real-world Push-T setup).
- **Anchor exercise:** load a ResNet-18, extract features for a batch of PushT frames, visualize the feature similarity structure.
- **Module page:** [Curriculum Module 2 — CNNs and visual representation learning](curriculum-02-cnns.md) **(drafted 2026-05-10)**.

#### [Module 3](curriculum-03-attention-and-transformers.md) — Sequence models and attention
- **Concept beats:** [RNN (recurrent neural network)](../glossary.md#rnn) / [LSTM (long short-term memory)](../glossary.md#lstm) (briefly — for context only), attention, self-attention, [MHA (multi-head attention)](../glossary.md#mha), [transformer](../glossary.md#transformer) block, [ViT (vision transformer)](../glossary.md#vit), positional encoding, causal masking.
- **Why for LeWM:** LeWM's encoder is a ViT. Its predictor is a causal [AR (autoregressive)](../glossary.md#ar) transformer over `(z_t, a_t) → z_{t+1}`. [BeT (behavior transformer)](../glossary.md#bet) is a transformer over actions. [VLA (vision-language-action)](../glossary.md#vla) [models](../concepts/vla-models.md) are transformers conditioning on language.
- **Anchor exercise:** patch a 64×64 PushT frame into 8×8 tokens, run them through a 2-layer transformer, inspect attention maps.
- **Module page:** [Curriculum Module 3 — Sequence models, attention, and transformers](curriculum-03-attention-and-transformers.md) **(drafted 2026-05-10)**.

#### [Module 4](curriculum-04-self-supervised-learning.md) — [SSL (self-supervised learning)](../glossary.md#ssl) and embeddings
- **Concept beats:** representation learning, contrastive learning ([SimCLR](../glossary.md#simclr) / [MoCo (momentum contrast)](../glossary.md#moco)) vs predictive ([MAE (masked autoencoder)](../glossary.md#mae) / [JEPA](../glossary.md#jepa)), the [latent space](../concepts/latent-space.md) as object, **representation collapse** as a failure mode, anti-collapse families: [EMA (exponential moving average)](../glossary.md#ema) target encoders + stop-gradient ([BYOL — bootstrap your own latent](../glossary.md#byol) / [DINO](../glossary.md#dino)), variance / covariance regularization ([VICReg](../glossary.md#vicreg), [Barlow Twins](../glossary.md#barlow-twins)), normality-based (LeWM's [SIGReg](../glossary.md#sigreg)).
- **Why for LeWM:** this is the module that turns the LeWM abstract from word-soup into a sensible engineering claim. SIGReg is intelligible only against the backdrop of "every prior end-to-end JEPA needed 4–6 anti-collapse hyperparameters."
- **Anchor exercise:** reproduce VICReg on CIFAR with and without the regularizer; observe collapse to constant.
- **Module page:** [Curriculum Module 4 — Self-supervised learning and embeddings](curriculum-04-self-supervised-learning.md) **(drafted 2026-05-10)**.

### Tier 2 — Generative models for control

#### [Module 5](curriculum-05-generative-models.md) — Generative modeling fundamentals (with a DDPM destination, full math)
- **Concept beats:** [AE (autoencoder)](../glossary.md#ae), [VAE (variational autoencoder)](../glossary.md#vae), [EBM (energy-based model)](../glossary.md#ebm) (just enough for [IBC (implicit behavior cloning)](../glossary.md#ibc)), score matching intuition, **[DDPM (denoising diffusion probabilistic models)](../glossary.md#ddpm)** forward + reverse process — *full math walkthrough*: [ELBO (evidence lower bound)](../glossary.md#elbo) derivation, [KL (Kullback–Leibler) divergence](../glossary.md#kl) bounds, noise schedule, the simplified ε-prediction loss; [CFG (classifier-free guidance)](../glossary.md#cfg) derivation, conditional diffusion. [DDPM paper](../sources/ddpm-paper.md) ingest is the anchor reading.
- **Why for LeWM:** prerequisite for [Diffusion Policy](../entities/diffusion-policy.md) (Module 7). Also sharpens the contrast in Module 10 between *generative-video world models* (which are giant conditional diffusion / flow models over pixels) and JEPA (which sidesteps generation entirely).
- **Anchor exercise:** train a tiny DDPM on MNIST; sample. Then derive the simplified loss `L_simple = E[||ε − ε_θ(x_t, t)||²]` from the ELBO on paper.
- **Module page:** [Curriculum Module 5 — Generative modeling fundamentals (DDPM, full math)](curriculum-05-generative-models.md) **(drafted 2026-05-10)**.

### Tier 3 — Robot learning

#### [Module 6](curriculum-06-imitation-learning.md) — [IL (imitation learning)](../glossary.md#il) and [BC (behavior cloning)](../glossary.md#bc)
- **Concept beats:** [imitation learning](../concepts/imitation-learning.md), BC as supervised learning, demonstration data, observation–action pairs, **multi-modal action distributions** (the central failure mode of vanilla [MSE](../glossary.md#mse)-BC), distribution shift / [DAgger (dataset aggregation)](../glossary.md#dagger), action chunking, the canonical [PushT](../entities/pusht.md) setup.
- **Why for LeWM:** BC is the policy-side counterpart to world models. Many world-model papers (LeWM, [DINO-WM (DINO world model)](../glossary.md#dino-wm)) compose `BC-policy + world-model-`[`MPC (model predictive control)`](../glossary.md#mpc) baselines. You can't read [DP (diffusion policy)](../glossary.md#dp) / [IBC](../glossary.md#ibc) / [BeT (behavior transformer)](../glossary.md#bet) without owning multi-modal action distributions as a concept.
- **Anchor exercise:** train a vanilla MSE-MLP BC policy on PushT demos; observe it fail by averaging modes.
- **Module page:** [Curriculum Module 6 — Imitation learning and behavior cloning](curriculum-06-imitation-learning.md) **(drafted 2026-05-10)**.

#### [Module 7](curriculum-07-bc-lineage-pusht.md) — BC evolution: [IBC](../glossary.md#ibc) → [BeT](../glossary.md#bet) → [DP (diffusion policy)](../glossary.md#dp) (PushT case study)
- **Concept beats:** [EBM (energy-based model)](../glossary.md#ebm) BC and [InfoNCE](../glossary.md#infonce) training ([IBC](../entities/ibc.md)); k-means action discretization + transformer ([BeT](../entities/bet.md)); conditional [DDPM](../glossary.md#ddpm) over action chunks ([Diffusion Policy](../entities/diffusion-policy.md)); receding-horizon execution; visual encoders for policy ([ResNet](../glossary.md#resnet) vs end-to-end); [UMI (universal manipulation interface)](../glossary.md#umi) data collection (one paragraph — context for "where the demonstrations come from").
- **Why for LeWM:** this is the *policy-learning lineage* the wiki has filed end-to-end ([IBC paper](../sources/ibc-paper.md), [BeT paper](../sources/bet-paper.md), [Diffusion Policy paper](../sources/diffusion-policy-paper.md), [UMI](../sources/umi-paper.md), [DDPM paper](../sources/ddpm-paper.md)). LeWM's ablations against [DINO-WM](../entities/dino-wm.md) implicitly ride on this lineage. Diffusion Policy is also the *thing on the other side* of "JEPA world model + planner" — they're both ways to get from PushT pixels to actions.
- **Anchor exercise:** run pretrained Diffusion Policy on PushT; inspect a sampled action trajectory; quantify multi-modality.
- **Module page:** [Curriculum Module 7 — BC lineage on PushT](curriculum-07-bc-lineage-pusht.md) **(drafted 2026-05-10)**.

#### [Module 8](curriculum-08-rl-vocabulary.md) — [RL (reinforcement learning)](../glossary.md#rl), enough to read a paper
- **Concept beats:** [MDP (Markov decision process)](../glossary.md#mdp), return, value function, policy, on-policy vs off-policy, policy gradient (REINFORCE → [PPO (proximal policy optimization)](../glossary.md#ppo) sketch), Q-learning sketch ([DQN — deep Q-network](../glossary.md#dqn)), **[MFRL (model-free)](../glossary.md#mfrl) vs [MBRL (model-based)](../glossary.md#mbrl) RL**, [Dreamer](../glossary.md#dreamer--dreamerv3)-class latent imagination as an MBRL technique (so the LeWM Dreamer / [TD-MPC (temporal-difference MPC)](../glossary.md#td-mpc) baselines parse).
- **Why for LeWM:** LeWM compares against Dreamer (task-specific reward) and TD-MPC (state-based). Without knowing what reward, value, and policy gradient are, those baseline columns are illegible. RL is *not* the focus of this curriculum — read for vocabulary, not implementation.
- **Anchor exercise:** read a Dreamer-V3 figure caption out loud and have it make sense.
- **Module page:** [Curriculum Module 8 — Reinforcement learning vocabulary](curriculum-08-rl-vocabulary.md) **(drafted 2026-05-10)**.

#### [Module 9](curriculum-09-vla.md) — [VLA (vision-language-action) models](../glossary.md#vla)
- **Concept beats:** [VLA](../concepts/vla-models.md) = vision encoder + language tokens + action head, descended from [LLM (large language model)](../glossary.md#llm) and [VLM (vision-language model)](../glossary.md#vlm); instruction-conditioned policies; major instances ([NVIDIA GR00T](../glossary.md#gr00t), [π0](../glossary.md#π0--π06-pi-zero) / [Physical Intelligence](../entities/physical-intelligence.md), [Gemini Robotics](../entities/gemini-robotics.md), [Helix](../glossary.md#helix), [OpenVLA](../glossary.md#openvla)); how VLAs differ from BC (instruction-following, multi-task generalization); why VLAs *aren't* world models (they emit actions, not next states).
- **Why for LeWM:** VLAs are the dominant paradigm for home-robotics generalists in 2025–2026. Knowing how they relate to (and don't replace) world models is essential for placing LeWM in the field. [VLA-JEPA](../entities/vla-jepa.md) is the explicit cross-over point — JEPA used as auxiliary loss inside a VLA.
- **Anchor exercise:** sketch the data flow for π0 vs Diffusion Policy vs LeWM-MPC on the same PushT episode.
- **Module page:** [Curriculum Module 9 — Vision-Language-Action models](curriculum-09-vla.md) **(drafted 2026-05-10)**.

### Tier 4 — World models

#### [Module 10](curriculum-10-world-models.md) — [WMs (world models)](../glossary.md#wm), broad
- **Concept beats:** [world model](../concepts/world-model.md) functional definition; the four families (generative-video / [WFM (world foundation model)](../glossary.md#wfm), [JEPA](../glossary.md#jepa) / latent-prediction, frozen-foundation-feature, [Dreamer](../glossary.md#dreamer--dreamerv3)-style reward-conditioned); [MPC](../glossary.md#mpc) vs [CEM (cross-entropy method)](../glossary.md#cem) vs gradient-based planning; planning horizon and compounding error; the [generative-video vs JEPA](generative-video-vs-jepa-world-models.md) tradeoff.
- **Why for LeWM:** LeWM is "JEPA, end-to-end-trained, with MPC planner." Every word in that sentence comes from this module. Without a clean four-way taxonomy, the LeWM contribution looks like noise.
- **Anchor exercise:** write a 3-line MPC loop pseudocode that plans against a learned next-state predictor and a cost function.
- **Module page:** [Curriculum Module 10 — World models, broad](curriculum-10-world-models.md) **(drafted 2026-05-10)**.

#### [Module 11](curriculum-11-jepa-deep.md) — [JEPA (joint-embedding predictive architecture)](../glossary.md#jepa) in depth
- **Concept beats:** what "joint embedding" means (per [JEPA concept page](../concepts/jepa.md)); V-JEPA 1 → [V-JEPA 2](../entities/v-jepa-2.md) → V-JEPA 2-[AC (action-conditioned)](../glossary.md#ar) → V-JEPA 2.1 progression; [DINO-WM](../entities/dino-wm.md) (frozen-encoder JEPA-adjacent) vs end-to-end JEPA ([LeWM](../glossary.md#lewm), [PLDM](../glossary.md#pldm)); [JEPA-WMs](../glossary.md#jepa-wms) on real Franka; action conditioning; the collapse problem revisited.
- **Why for LeWM:** LeWM is a single point in this design space. Need the surrounding axes to evaluate why "no [EMA](../glossary.md#ema), no stop-grad, no frozen encoder" is a real claim and not a marketing line.
- **Anchor exercise:** annotate the LeWM architecture figure with which design choices match V-JEPA 2 and which differ.
- **Module page:** [Curriculum Module 11 — JEPA in depth](curriculum-11-jepa-deep.md) **(drafted 2026-05-10)**.

#### [Module 12](curriculum-12-lewm-deep-dive.md) — LeWorldModel paper deep-dive (full math)
- **Concept beats:** the [LeWM paper](../sources/leworldmodel-paper.md) section by section; **[SIGReg](../glossary.md#sigreg) full derivation** — random unit-vector projection (sketched approach) → empirical characteristic function → **Epps–Pulley** univariate normality test → Cramér–Wold theorem (legitimacy argument) → backprop through the test statistic, with all intermediate steps; the two-loss claim (next-embedding [MSE](../glossary.md#mse) + SIGReg); 4-environment benchmark suite ([PushT](../entities/pusht.md), Reacher, OGBench-Cube, Two-Room); the BN-after-CLS engineering trick; planning protocol ([CEM](../glossary.md#cem)-[MPC](../glossary.md#mpc) details, horizon, action sampling); surprise / violation-of-expectation evaluation; latent probing; comparison table against [PLDM](../glossary.md#pldm) / [DINO-WM](../glossary.md#dino-wm) / [Dreamer](../glossary.md#dreamer--dreamerv3) / [TD-MPC](../glossary.md#td-mpc).
- **Why for LeWM:** this is the destination. By module 12, every term should already be familiar — the deep-dive consolidates rather than introduces.
- **Anchor exercise:** install [LeWM](../sources/lewm-github.md) per [the howto](leworldmodel-howto.md); reproduce a single PushT eval at a pretrained checkpoint. Then derive SIGReg's gradient-through-projection on paper.
- **Module page:** [Curriculum Module 12 — LeWorldModel deep-dive (with full SIGReg math)](curriculum-12-lewm-deep-dive.md) **(drafted 2026-05-10)**. *Note: corrects the curriculum-outline reference to "Anderson-Darling-style" — the paper actually uses **Epps–Pulley**.*

### Tier 5 — Home robotics integration

#### [Module 13](curriculum-13-home-robotics-deployment.md) — Home robotics — the deployment reality
- **Concept beats:** [Stretch](../entities/stretch.md) as the de-facto research platform ([why](stretch-as-assistive-platform.md)); [RUM (robot utility models)](../glossary.md#rum) and [OK-Robot](../glossary.md#ok-robot) as the "real-data" path; the AI Index 89.4% [RLBench](https://github.com/stepjam/RLBench) vs 12.4% [BEHAVIOR-1K](../glossary.md#behavior-1k) gap; [PAR (physically assistive robotics)](../glossary.md#par) ([systematic review](../sources/nanavati2024-physically-assistive-robots-review.md)); [autonomy-preference finding](../syntheses/levels-of-autonomy-in-assistive-robotics.md); [EUP (end-user programming)](../glossary.md#eup); why [JEPA](../glossary.md#jepa) could matter here ([assistive-robotics R&D landscape](assistive-robotics-research-landscape.md)).
- **Why for LeWM:** the user's actual goal. LeWM and friends are not deployed in homes today. This module places the technique inside the deployment reality and identifies which barriers it could plausibly move (data efficiency, planning speed) and which it won't (whole-body manipulation, dressing, bathing, real-world robustness).
- **Anchor exercise:** read [DINO-WM on Stretch experiment plan](dino-wm-on-stretch-experiment.md) and [LeWM on Stretch feasibility](lewm-on-stretch-feasibility.md); state the one experiment most worth running.
- **Module page:** [Curriculum Module 13 — Home robotics deployment reality](curriculum-13-home-robotics-deployment.md) **(drafted 2026-05-10)**.

#### [Module 14](curriculum-14-capstone.md) — Capstone: paper-first, hardware-second
- **Phase A (paper / sim — required):** reproduce LeWM PushT from scratch ([detailed scope already filed](lewm-hello-world-project-scope.md)); install / train / eval per [the howto](leworldmodel-howto.md); produce a written experiment-design memo for the smallest credible LeWM-on-Stretch or DINO-WM-on-Stretch experiment ([feasibility analysis](lewm-on-stretch-feasibility.md), [DINO-WM-on-Stretch plan](dino-wm-on-stretch-experiment.md)).
- **Phase B (hardware — when Stretch is available):** execute the phase-A memo on a real [Stretch](../entities/stretch.md). Use the [RUM](../glossary.md#rum) open dataset to bootstrap the action-conditioning data. Compare against a Diffusion Policy baseline.
- **Why for LeWM:** the only way to know if you understood it is to train it. Phase B is gated on hardware acquisition; the curriculum is fully completable on phase A alone.
- **Anchor exercise:** the capstone *is* the exercise. Phase-A deliverable: a 5–10 page memo + a working PushT-LeWM training run.
- **Module page:** [Curriculum Module 14 — Capstone (paper-first, hardware-second)](curriculum-14-capstone.md) **(drafted 2026-05-10)**.

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

| Module                           | Existing wiki coverage                                                                                                                                                                                                                                   | Needs new                                                 |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 1 NN basics                      | none                                                                                                                                                                                                                                                     | **drafted** — [Curriculum Module 1 — Neural networks and training](curriculum-01-neural-networks.md)         |
| 2 CNNs                           | none                                                                                                                                                                                                                                                     | **drafted** — [Curriculum Module 2 — CNNs and visual representation learning](curriculum-02-cnns.md)         |
| 3 Attention / transformers / ViT | none                                                                                                                                                                                                                                                     | **drafted** — [Curriculum Module 3 — Sequence models, attention, and transformers](curriculum-03-attention-and-transformers.md) |
| 4 SSL & embeddings               | partial in [latent-space](../concepts/latent-space.md), [JEPA](../concepts/jepa.md)                                                                                                                                                                      | **drafted** — [Curriculum Module 4 — Self-supervised learning and embeddings](curriculum-04-self-supervised-learning.md) |
| 5 Generative / DDPM              | [DDPM paper](../sources/ddpm-paper.md) source ingest                                                                                                                                                                                                     | **drafted** — [Curriculum Module 5 — Generative modeling fundamentals (DDPM, full math)](curriculum-05-generative-models.md) |
| 6 Imitation learning             | [concept](../concepts/imitation-learning.md), [PushT entity](../entities/pusht.md)                                                                                                                                                                       | **drafted** — [Curriculum Module 6 — Imitation learning and behavior cloning](curriculum-06-imitation-learning.md) |
| 7 BC lineage (IBC/BeT/DP)        | [IBC](../sources/ibc-paper.md), [BeT](../sources/bet-paper.md), [Diffusion Policy](../sources/diffusion-policy-paper.md), [UMI](../sources/umi-paper.md) all ingested                                                                                    | **drafted** — [Curriculum Module 7 — BC lineage on PushT](curriculum-07-bc-lineage-pusht.md) |
| 8 RL vocab                       | none                                                                                                                                                                                                                                                     | **drafted** — [Curriculum Module 8 — Reinforcement learning vocabulary](curriculum-08-rl-vocabulary.md) |
| 9 VLA                            | [concept](../concepts/vla-models.md), [GR00T](../entities/nvidia-groot.md), [Gemini Robotics](../entities/gemini-robotics.md), [Physical Intelligence](../entities/physical-intelligence.md), [π0 source](../sources/pi-zero-paper.md), [Helix source](../sources/helix-blog.md), [VLA-JEPA source](../sources/vla-jepa-paper.md)         | **drafted** — [Curriculum Module 9 — Vision-Language-Action models](curriculum-09-vla.md) |
| 10 World models                  | [concept](../concepts/world-model.md), [WM simulators concept](../concepts/world-model-simulators.md), [generative-video vs JEPA synthesis](generative-video-vs-jepa-world-models.md), [Dreamer entity](../entities/dreamer.md), [TD-MPC entity](../entities/td-mpc.md), [DreamerV3 source](../sources/dreamer-v3-paper.md), [TD-MPC2 source](../sources/td-mpc2-paper.md) | **drafted** — [Curriculum Module 10 — World models, broad](curriculum-10-world-models.md) |
| 11 JEPA depth                    | [concept](../concepts/jepa.md), [V-JEPA 2 paper](../sources/v-jepa-2-paper.md), [V-JEPA 2.1](../sources/v-jepa-2-1-paper.md), [JEPA-WMs](../sources/jepa-wms-paper.md), [DINO-WM](../sources/dino-wm-paper.md), [VLA-JEPA](../sources/vla-jepa-paper.md) | **drafted** — [Curriculum Module 11 — JEPA in depth](curriculum-11-jepa-deep.md) |
| 12 LeWM deep-dive                | [paper ingest](../sources/leworldmodel-paper.md), [howto](leworldmodel-howto.md), [GitHub](../sources/lewm-github.md), [feasibility](lewm-on-rosorin-pro-feasibility.md), [Stretch feasibility](lewm-on-stretch-feasibility.md)                          | **drafted** — [Curriculum Module 12 — LeWM deep-dive (with full SIGReg math)](curriculum-12-lewm-deep-dive.md) |
| 13 Home robotics deployment      | rich — see [assistive-robotics R&D landscape](assistive-robotics-research-landscape.md), [Stretch as platform](stretch-as-assistive-platform.md), [autonomy levels](levels-of-autonomy-in-assistive-robotics.md)                                         | **drafted** — [Curriculum Module 13 — Home robotics deployment reality](curriculum-13-home-robotics-deployment.md) |
| 14 Capstone                      | [hello-world Project 1](lewm-hello-world-project-scope.md), [Stretch feasibility](lewm-on-stretch-feasibility.md), [DINO-WM on Stretch](dino-wm-on-stretch-experiment.md)                                                                                | **drafted** — [Curriculum Module 14 — Capstone (paper-first, hardware-second)](curriculum-14-capstone.md) |
|                                  |                                                                                                                                                                                                                                                          |                                                           |

## Effort estimate (rough, post-decisions)

Self-paced with strong-coder-some-ML background, ~5–10 hr/module reading + 2–5 hr/exercise. Updated with the "go deep" decisions on modules 5 (DDPM math) and 12 (SIGReg math).

- Tier 1 (1–4): ~25–40 hr
- Tier 2 (5, full DDPM math): ~15–25 hr (was 10–15)
- Tier 3 (6–9): ~30–50 hr
- Tier 4 (10–12, full SIGReg math): ~30–50 hr (was 25–40)
- Tier 5 (13–14, phase A only): ~25–40 hr; phase B adds 40–80+ hr if hardware is available

Total without hardware phase: ~125–205 hr. Realistic 4–7 month evening pace at 8–10 hr/week.

## Mentioned in
- [Index](../index.md) (curriculum entry)
- [Glossary](../glossary.md) (companion reference)
- [Log](../log.md)
