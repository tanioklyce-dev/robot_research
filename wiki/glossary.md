# Abbreviations & Glossary

A flat index of acronyms used across this wiki, with one-line definitions and a pointer to the curriculum module where each is introduced. Designed to be linked into from any wiki page on first mention of an acronym.

> Cross-referenced from [Robot-learning curriculum](syntheses/robot-learning-curriculum.md). When a curriculum module is written, the relevant glossary entries pick up a link to that module page.

## How to use
- Search this page (`Ctrl-F`) for any acronym you encounter elsewhere in the wiki.
- Each entry: **ACRONYM** — Full Expansion. One-line description. *(Module N — where it lands in the curriculum.)*
- Confidence flags: `(?)` = exact expansion uncertain, see linked source.
- Entries are sorted alphabetically (case-insensitive, ignoring hyphens), regardless of curriculum module.

---

### Adam
**Adaptive Moment Estimation** — the de-facto SGD variant in 2026; uses running averages of gradients and squared gradients. *(Module 1.)*

### AE
**Autoencoder** — encoder-decoder pair trained to reconstruct its input. *(Module 5.)*

### AR
**Autoregressive** — predict token *t+1* conditioned on tokens *1..t*. LeWM's predictor is an AR transformer over `(z_t, a_t) → z_{t+1}`. *(Module 3.)*

### Barlow Twins
SSL whose loss makes the cross-correlation of two augmented-view embeddings the identity (no collapse, no redundancy). *(Module 4.)*

### BC
**Behavior Cloning** — the simplest IL: supervised regression / classification from observation to action. *(Module 6.)*

### BEHAVIOR-1K
Stanford household-task benchmark; 12.4% best result (per [AI Index 2026](sources/stanford-hai-ai-index-2026.md)) — the gap that motivates module 13. *(Module 13.)*

### BeT
**Behavior Transformer** — Shafiullah et al., NeurIPS 2022 ([source page](sources/bet-paper.md)); transformer policy that emits actions via k-means discretization + offset regression. *(Module 7.)*

### BN
**Batch Normalization** — normalize activations across the batch to stabilize training. *(Module 1.)*

### BYOL
**Bootstrap Your Own Latent** — Grill et al. 2020; SSL using a target network updated by EMA; predict target features without negatives. Direct ancestor of JEPA. *(Module 4.)*

### CE
**Cross-Entropy** — the standard classification loss; for predicted distribution `p̂` and target `p`, `−Σ p log p̂`. *(Module 1.)*

### CEM
**Cross-Entropy Method** — derivative-free sampling-based optimizer; used inside MPC against learned world models. *(Module 10.)*

### CFG
**Classifier-Free Guidance** — Ho & Salimans 2022; train one conditional + one unconditional model, sample by extrapolating between them; the standard conditioning method for diffusion. *(Module 5.)*

### CNN
**Convolutional Neural Network** — NN whose layers slide a small filter across the input (image), exploiting local spatial structure. *(Module 2.)*

### COCO / ImageNet
Vision benchmark datasets used for pretraining / evaluating CNNs and ViTs. *(Module 2.)*

### DAgger
**Dataset Aggregation** — Ross et al. 2011; iteratively roll out a learned policy, query expert for corrections, retrain — fixes BC's distribution-shift problem. *(Module 6.)*

### DDIM
**Denoising Diffusion Implicit Models** — Song, Meng, Ermon 2020; deterministic non-Markovian sampler that produces samples in far fewer steps. *(Module 5.)*

### DDPM
**Denoising Diffusion Probabilistic Models** — Ho, Jain, Abbeel 2020 ([source page](sources/ddpm-paper.md)); foundational diffusion-model class. Forward process adds Gaussian noise; reverse process learns to denoise. The action-distribution model used by [Diffusion Policy](entities/diffusion-policy.md). *(Module 5.)*

### DINO
**self-DIstillation with NO labels** — Caron et al. 2021; SSL with EMA teacher + cross-entropy on student predictions; produces strong semantic features. *(Module 2 / 4.)*

### DINOv2
The 2023 successor; the encoder used by [DINO-WM](entities/dino-wm.md), [DINO-world](entities/dino-world.md), and [JEPA-WMs](entities/jepa-wms.md). *(Module 4.)*

### DINO-WM
**DINO World Model** — Zhou et al., NYU + FAIR ([source page](sources/dino-wm-paper.md)); JEPA-adjacent (frozen DINOv2 encoder + learned predictor). *(Module 11.)*

### DNN
**Deep Neural Network** — an NN with many layers (2010s convention: anything more than ~3 hidden layers). *(Module 1.)*

### DOF
**Degrees of Freedom** — independent joint axes a robot can move. Stretch has 3 + arm DOF; Franka has 7. *(Throughout.)*

### DP
**Diffusion Policy** — Chi et al., RSS 2023 ([source page](sources/diffusion-policy-paper.md)); BC where the action distribution is modeled by a conditional DDPM. *(Module 7.)*

### DQN
**Deep Q-Network** — Mnih et al. 2015; Q-learning with a CNN value network; the original Atari result. *(Module 8.)*

### Dreamer / DreamerV3
Hafner et al. ([source page](sources/dreamer-v3-paper.md), [entity](entities/dreamer.md)); MBRL family that learns a recurrent latent dynamics model and trains an actor-critic in imagination. Baseline in LeWM. *(Module 10.)*

### DROID
**Distributed Robot Interaction Dataset** — Khazatsky et al. 2024 ([entity](entities/droid.md)); 350 hr / 76k trajectories on Franka; the dominant real-robot dataset in JEPA-for-robotics work. *(Modules 11–13.)*

### EBM
**Energy-Based Model** — model that assigns a scalar "energy" to each input and learns to lower energy on data, raise it elsewhere; the substrate of [IBC](entities/ibc.md). *(Module 5 / 7.)*

### EE
**End-Effector** — gripper / hand at the tip of a robot arm. *(Throughout.)*

### ELBO
**Evidence Lower Bound** — variational lower bound on log-likelihood; the underlying objective for VAEs and the diffusion training loss. *(Module 5.)*

### EMA
**Exponential Moving Average** — running weighted average of past values; used in [V-JEPA](entities/v-jepa-2.md) / BYOL-line as a "target encoder" — a slowly-updating teacher whose outputs serve as prediction targets, preventing collapse. [LeWM](entities/leworldmodel.md)'s contribution is doing without EMA. *(Module 4.)*

### Embedding / Latent
A vector representation of an input; the output of an encoder. The substrate JEPA models predict in. See [latent space](concepts/latent-space.md) concept page. *(Modules 2–4.)*

### EUP
**End-User Programming** — letting non-experts customize robot behavior. See [concept page](concepts/end-user-robot-programming.md). *(Module 13.)*

### FCN
**Fully Convolutional Network** — CNN with no fully-connected head, used for dense prediction. *(Module 2.)*

### GAN
**Generative Adversarial Network** — generator + discriminator trained adversarially. Largely superseded by diffusion in 2022+. *(Module 5.)*

### GPU
**Graphics Processing Unit** — parallel compute substrate for NN training. *(Throughout.)*

### GR00T
**Generalist Robot 00 Technology** *(NVIDIA's expansion)* — NVIDIA's open VLA bundled with Isaac Lab. See [entity page](entities/nvidia-groot.md). *(Module 9.)*

### GRU
**Gated Recurrent Unit** — simpler LSTM variant; same role. *(Module 3.)*

### HAB
**Home Assistant Benchmark** — long-horizon household manipulation tasks (referenced by [ManiSkill-HAB](sources/maniskill-hab-paper.md)). *(Module 13.)*

### Helix
[Figure](entities/figure.md) AI's VLA ([source page](sources/helix-blog.md)), deployed on Figure 02/03 humanoids. Hierarchical System 1 / System 2 design: 7B VLM @ 7–9 Hz + 80M transformer @ 200 Hz, end-to-end trained. *(Module 9.)*

### IBC
**Implicit Behavior Cloning** — Florence et al., CoRL 2021 ([source page](sources/ibc-paper.md)); BC where the policy is an EBM over actions trained with InfoNCE. Introduced [PushT](entities/pusht.md). *(Module 7.)*

### iDDPM
**improved DDPM** — Nichol & Dhariwal 2021; learned variance + cosine noise schedule. *(Module 5.)*

### IL
**Imitation Learning** — learn a policy from demonstrations. See [imitation learning concept](concepts/imitation-learning.md). *(Module 6.)*

### InfoNCE
**Information Noise-Contrastive Estimation** — the contrastive loss family used by SimCLR, MoCo, and (in policy form) [IBC](entities/ibc.md). *(Module 4 / 7.)*

### IoU
**Intersection over Union** — overlap metric for bounding boxes / masks. *(Module 2.)*

### JEPA
**Joint-Embedding Predictive Architecture** — predict the *embedding* of the next state, not pixels. Yann LeCun's program. See [concept page](concepts/jepa.md). *(Module 11.)*

### JEPA-WMs
Terver et al., FAIR, Dec 2025 ([source page](sources/jepa-wms-paper.md)); first JEPA-for-robotics paper using [RoboCasa](entities/robocasa.md). *(Module 11.)*

### KL
**Kullback–Leibler divergence** — asymmetric distance between two probability distributions; building block for VAE / diffusion losses. *(Module 5.)*

### LBM
**Large Behavior Model** — TRI's name for its generalist policy effort; analogous to "LLM but for actions." *(Module 7 / 9.)*

### LeWM
**LeWorldModel** — Maes et al., 2026 ([source page](sources/leworldmodel-paper.md)); first stable end-to-end JEPA from raw pixels with two loss terms. The destination of this curriculum. *(Module 12.)*

### LIBERO
**LIfelong learning BEnchmark for RObotic manipulation** — de-facto VLA-eval benchmark. *(Module 9.)*

### LLM
**Large Language Model** — transformer trained on text at scale (GPT, Claude, Llama, Qwen). *(Module 9.)*

### LN
**Layer Normalization** — normalize activations across features per sample; the transformer-default normalizer. *(Module 1.)*

### LSTM
**Long Short-Term Memory** — RNN variant with gating mechanisms that let it learn long-range dependencies; standard pre-2018 sequence model. *(Module 3.)*

### MAE
**Masked Autoencoder** — He et al. 2021; reconstruct image patches with most of the image masked. Predictive (not contrastive) SSL. *(Module 4.)*

### MBRL
**Model-Based Reinforcement Learning** — RL with an explicit learned dynamics model (a world model). Dreamer is the canonical MBRL family. *(Modules 8 / 10.)*

### MCP
**Model Context Protocol** — Anthropic-led protocol for connecting LLMs to tools. *(Module 9.)*

### MDP
**Markov Decision Process** — `(S, A, P, R, γ)`: states, actions, transition probabilities, reward function, discount factor. The formalism behind RL. *(Module 8.)*

### MFRL
**Model-Free Reinforcement Learning** — RL without an explicit dynamics model; learn value or policy directly. *(Module 8.)*

### MHA
**Multi-Head Attention** — running self-attention with several independent attention heads in parallel. *(Module 3.)*

### MJX
**MuJoCo XLA** — JAX-accelerated MuJoCo; the substrate for [MuJoCo Playground](entities/mujoco-playground.md). *(Module 13.)*

### MLP
**Multi-Layer Perceptron** — the simplest deep NN: stacked fully-connected (`linear`) layers separated by nonlinearities. *(Module 1.)*

### MoCo
**Momentum Contrast** — He et al. 2020; contrastive SSL with a queue of negatives and momentum encoder. *(Module 4.)*

### MPC
**Model Predictive Control** — at each step, plan a short-horizon action sequence using a model, execute the first action, replan. The control method paired with world models in [LeWM](entities/leworldmodel.md), [DINO-WM](entities/dino-wm.md), [V-JEPA 2-AC](entities/v-jepa-2.md). *(Module 10.)*

### MSE
**Mean Squared Error** — `mean((y - ŷ)²)`; the standard regression loss; the loss term in JEPA next-embedding prediction. *(Module 1.)*

### NCE
**Noise-Contrastive Estimation** — Gutmann & Hyvärinen 2010; train by classifying real vs noise. Generalizes to InfoNCE in SSL. *(Modules 4 / 5.)*

### NN
**Neural Network** — a function built by stacking layers of weighted sums and nonlinearities; trained by gradient descent on a loss. Umbrella term. *(Module 1.)*

### OK-Robot
NYU 2024 ([entity](entities/ok-robot.md)); zero-shot pick-and-drop in 10 NYC homes; 58.5% success. *(Module 13.)*

### OpenVLA
Open-weights VLA used as a baseline in many 2024–2026 papers. *(Module 9.)*

### OVMM
**Open Vocabulary Mobile Manipulation** — HomeRobot benchmark for Stretch. *(Module 13.)*

### PAR
**Physically Assistive Robotics** — robots that physically assist disabled users (feeding, dressing, transfer). See [Nanavati 2024 systematic review](sources/nanavati2024-physically-assistive-robots-review.md). *(Module 13.)*

### π0 / π0.6 (pi-zero)
[Physical Intelligence](entities/physical-intelligence.md)'s flagship cross-platform VLA. π0 ([source page](sources/pi-zero-paper.md)) uses a flow-matching action head on a pre-trained VLM backbone. *(Module 9.)*

### PLDM
**Planning with Latent-space Dynamics Models** — comparison baseline in [LeWM](sources/leworldmodel-paper.md); end-to-end JEPA-style WM with 6 anti-collapse hyperparameters. *(Module 11.)*

### PPO
**Proximal Policy Optimization** — Schulman et al. 2017; the dominant on-policy actor-critic algorithm. *(Module 8.)*

### R3M
A pretrained visual encoder for manipulation (Nair et al. 2022); appears as a Diffusion Policy ablation. *(Module 7.)*

### ReLU
**Rectified Linear Unit** — the activation function `max(0, x)`; default nonlinearity in deep networks since ~2012. *(Module 1.)*

### ResNet
**Residual Network** — He et al. 2015; CNN with skip connections (`x + F(x)`); enabled training of very deep networks; the BC-line baseline visual encoder. *(Module 2.)*

### RL
**Reinforcement Learning** — learn a policy that maximizes expected reward through environment interaction. *(Module 8.)*

### RNN
**Recurrent Neural Network** — sequence model that maintains a hidden state across timesteps; superseded by transformers for most tasks. *(Module 3.)*

### ROS / ROS 2
**Robot Operating System** — middleware for robotics software (publish-subscribe + services). *(Module 13.)*

### RUM
**Robot Utility Models** — Etukuru et al., NYU/Meta 2024 ([entity](entities/robot-utility-models.md)); zero-shot mobile-manipulation BC on [Stretch](entities/stretch.md). *(Module 13.)*

### SAC
**Soft Actor-Critic** — Haarnoja et al. 2018; max-entropy off-policy actor-critic for continuous control. *(Module 8.)*

### SGD
**Stochastic Gradient Descent** — gradient descent on minibatches; the canonical NN optimizer. *(Module 1.)*

### SIGReg
**Sketched Isotropic Gaussian Regularizer** (Balestriero 2025; the foundational reference cited from [LeWM](entities/leworldmodel.md) as [25]). The single anti-collapse regularizer in LeWM: project latent embeddings onto `M` random unit-norm directions; run the **Epps–Pulley** univariate normality test on each 1-D projection; average the test statistics; backprop the result as a loss term. Justified by the **Cramér–Wold theorem** — matching all 1-D marginals of a `d`-D distribution is equivalent to matching the full joint distribution. Encourages an isotropic Gaussian latent and gives a provable anti-collapse guarantee with a single hyperparameter (`λ`, the SIGReg loss weight; default 0.1) vs. 4–6 for prior end-to-end JEPAs ([PLDM](#pldm)). *(Module 4 introduction; [Module 12 derivation](syntheses/curriculum-12-lewm-deep-dive.md).)*

### SimCLR
**Simple framework for Contrastive Learning of Representations** — Chen et al. 2020; contrastive SSL with augmentation and a projection head. *(Module 4.)*

### SLAM
**Simultaneous Localization And Mapping** — classical robotics technique; out-of-scope for this curriculum but you'll see it. *(Out of scope.)*

### SSL
**Self-Supervised Learning** — train on unlabeled data by inventing a pretext task whose labels can be derived from the input itself. The umbrella for everything in self-supervised pretraining. *(Module 4.)*

### TD
**Temporal Difference** — bootstrap-style update using `r + γ V(s') − V(s)`; backbone of value-based RL. *(Module 8.)*

### TD-MPC
**Temporal Difference Model Predictive Control** — Hansen et al. 2022 / 2024 ([TD-MPC2 source page](sources/td-mpc2-paper.md), [entity](entities/td-mpc.md)); model-based control combining a learned latent dynamics model with MPC and TD-bootstrapping. Decoder-free (no pixel reconstruction). Baseline in [LeWM](sources/leworldmodel-paper.md). *(Module 10.)*

### TPU
**Tensor Processing Unit** — Google's NN-specialized accelerator. *(Throughout.)*

### Transformer
NN architecture (Vaswani et al. 2017) built around self-attention; replaced RNNs as the dominant sequence model. *(Module 3.)*

### TRPO
**Trust Region Policy Optimization** — Schulman et al. 2015; PPO's predecessor with a hard trust-region constraint. *(Module 8.)*

### UMI
**Universal Manipulation Interface** — Chi et al., RSS 2024 ([source page](sources/umi-paper.md)); hand-held gripper for collecting in-the-wild demonstrations at high throughput (111 demos/hr). *(Module 7.)*

### URDF / MJCF / USD
Robot description formats — XML-based ([URDF](concepts/world-model-simulators.md) for ROS, MJCF for [MuJoCo](entities/mujoco.md)) and scene-description ([USD / OpenUSD](entities/openusd.md) for NVIDIA Omniverse). *(Module 13.)*

### VAE
**Variational Autoencoder** — Kingma & Welling 2013; AE with a probabilistic latent space and KL regularization. *(Module 5.)*

### VICReg
**Variance-Invariance-Covariance Regularization** — Bardes, Ponce, LeCun 2022; non-contrastive SSL that prevents collapse via variance and covariance penalties. Same author family as JEPA / SIGReg. *(Module 4.)*

### ViT
**Vision Transformer** — Dosovitskiy et al. 2020; transformer applied to image patches as tokens; the default visual encoder in JEPA-line models including [LeWM](entities/leworldmodel.md) and [V-JEPA 2](entities/v-jepa-2.md). *(Module 3.)*

### V-JEPA / V-JEPA 2 / V-JEPA 2-AC / V-JEPA 2.1
**Video JEPA** family from Meta FAIR; "AC" = Action-Conditioned. See [V-JEPA 2 entity](entities/v-jepa-2.md). *(Module 11.)*

### VLA
**Vision-Language-Action** — VLM adapted to emit *actions* rather than text; the dominant 2024–2026 generalist-policy paradigm. See [VLA concept](concepts/vla-models.md). *(Module 9.)*

### VLM
**Vision-Language Model** — multimodal model accepting image + text, emitting text (e.g. GPT-4V, Gemini, Claude with vision). *(Module 9.)*

### VQ-BeT
**Vector-Quantized Behavior Transformer** — Lee et al. 2024; replaces BeT's k-means with a learned VQ codebook; top performer in [RUM](entities/robot-utility-models.md) ablations. *(Module 7.)*

### WFM
**World Foundation Model** — NVIDIA marketing term for very-large generative-video world models like [Cosmos](entities/nvidia-cosmos.md). A *type* of WM, not a synonym. *(Module 10.)*

### WM
**World Model** — learned predictive model of environment dynamics: `s_{t+1} = f(s_t, a_t)`. See [concept page](concepts/world-model.md). *(Module 10.)*

---

## Mentioned in
- [Robot-learning curriculum](syntheses/robot-learning-curriculum.md) — primary consumer.
- [Index](index.md).
- Linked from individual module synthesis pages as they're written.
