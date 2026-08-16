---
title: Abbreviations & Glossary
type: reference
created: 2026-05-10
updated: 2026-08-16
tags: [glossary, reference, acronyms, curriculum]
---

# Abbreviations & Glossary

A flat index of acronyms used across this wiki, with one-line definitions and a pointer to the curriculum module where each is introduced. Designed to be linked into from any wiki page on first mention of an acronym.

> Cross-referenced from [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md). When a curriculum module is written, the relevant glossary entries pick up a link to that module page.

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

### CA
**Cellular Automaton** — a grid of discrete-state cells updated in parallel by a shared local rule; complex global behavior with no central controller. Canonical: [Conway's Game of Life](entities/game-of-life.md) (2D), Wolfram's elementary CAs / Rule 30 (1D). See [cellular automata](concepts/alife/cellular-automata.md). *(ALife branch.)*

### CFG
**Classifier-Free Guidance** — Ho & Salimans 2022; train one conditional + one unconditional model, sample by extrapolating between them; the standard conditioning method for diffusion. *(Module 5.)*

### Computational irreducibility
**Computational irreducibility** ([Wolfram](entities/stephen-wolfram.md)) — for many systems there is no shortcut to the outcome: the only way to know the state after *n* steps is to run the *n* steps. Underlies why simple [CAs](concepts/alife/cellular-automata.md) are inexhaustibly rich; rhymes with compounding rollout error in [world models](concepts/world-models/world-model.md). *(ALife branch.)*

### CNN
**Convolutional Neural Network** — NN whose layers slide a small filter across the input (image), exploiting local spatial structure. *(Module 2.)*

### CTDE
**Centralized Training, Decentralized Execution** — MARL paradigm: agents train with global/joint information (e.g. a centralized critic) but act on local observations only. [MADDPG](#maddpg) and Unity's [MA-POCA](#ma-poca) are instances. See [multi-agent RL](concepts/learning/multi-agent-rl.md). *(RL branch.)*

### COCO / ImageNet
Vision benchmark datasets used for pretraining / evaluating CNNs and ViTs. *(Module 2.)*

### DAgger
**Dataset Aggregation** — Ross et al. 2011; iteratively roll out a learned policy, query expert for corrections, retrain — fixes BC's distribution-shift problem. *(Module 6.)*

### DDIM
**Denoising Diffusion Implicit Models** — Song, Meng, Ermon 2020; deterministic non-Markovian sampler that produces samples in far fewer steps. *(Module 5.)*

### DDPM
**Denoising Diffusion Probabilistic Models** — Ho, Jain, Abbeel 2020 ([source page](sources/ddpm-paper.md)); foundational diffusion-model class. Forward process adds Gaussian noise; reverse process learns to denoise. The action-distribution model used by [Diffusion Policy](entities/diffusion-policy.md). *(Module 5.)*

### Differential IK
**Differential inverse kinematics** — solve for joint velocities `v` that realize a desired end-effector spatial velocity, `min ‖J(q)v − V_desired‖²`, instead of solving full IK for a pose. Posed as a **QP** it accepts joint-position, velocity, and acceleration limits and collision-avoidance constraints as linear inequalities — which is what turns it into a safety layer under a learned policy ([operational space control](concepts/robotics/operational-space-control.md)). Preferred over pseudo-inverse-then-clamp: solving inside the feasible set beats trimming an infeasible answer. `DifferentialInverseKinematicsIntegrator` ships in [Drake](entities/drake.md). *(Classical-robotics branch.)*

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

### Elo
**Elo rating** — relative-skill score (from chess; Arpad Elo) used as the fitness signal in self-play RL; rises as an agent beats stronger past versions of itself. The [USC table-tennis project](sources/usc-table-tennis-marl.md) tracks self-play by Elo (init 1200 → 2352 for its best SAC agent). *(RL branch.)*

### EMA
**Exponential Moving Average** — running weighted average of past values; used in [V-JEPA](entities/v-jepa-2.md) / BYOL-line as a "target encoder" — a slowly-updating teacher whose outputs serve as prediction targets, preventing collapse. [LeWM](entities/leworldmodel.md)'s contribution is doing without EMA. *(Module 4.)*

### Embedding / Latent
A vector representation of an input; the output of an encoder. The substrate JEPA models predict in. See [latent space](concepts/world-models/latent-space.md) concept page. *(Modules 2–4.)*

### Encoder
NN that maps a raw input (image, video clip, action sequence, etc.) into an embedding / latent vector. Concretely: a [CNN](#cnn) (ResNet for 2D images), a [ViT](#vit) (patches → tokens → transformer), or a 1D-CNN / transformer for sequences. In SSL the encoder is *what you train* — the downstream task uses its frozen output. In a [Joint-Embedding Predictive Architecture (JEPA)](concepts/world-models/jepa.md), one encoder embeds the context `x` and (often the same) encoder embeds the target `y`; the [predictor](#predictor) then operates between those embeddings. Distinguished from a *decoder* (which reverses the mapping to reconstruct pixels) — JEPA / [DINOv2](entities/dinov2.md)-line models deliberately have no decoder. *(Modules 2–4.)*

### EUP
**End-User Programming** — letting non-experts customize robot behavior. See [concept page](concepts/robotics/end-user-robot-programming.md). *(Module 13.)*

### FAST
**Frequency-space Action Sequence Tokenization** — Pertsch et al. 2025 ([entity](entities/fast-action-tokenization.md) / [paper](sources/fast-paper.md)); DCT + BPE compression of robot action chunks into discrete tokens, so autoregressive VLAs can learn high-frequency dexterous tasks that naïve per-timestep binning fails on. Powers π0-FAST; reused inside [Knowledge Insulation](concepts/learning/knowledge-insulation.md). *(Module 9.)*

### FCN
**Fully Convolutional Network** — CNN with no fully-connected head, used for dense prediction. *(Module 2.)*

### FD / ID
**Forward Dynamics / Inverse Dynamics** — in world/action modeling: FD predicts future observations given actions (= an action-conditioned [world model](concepts/world-models/world-model.md)); ID infers the actions that explain an observed transition. Two of the three modes of a [world-action model](concepts/world-models/world-action-model.md) (the third is *policy*). Central to [Cosmos 3](sources/cosmos-3-technical-report.md). *(Module 10.)*

### GAN
**Generative Adversarial Network** — generator + discriminator trained adversarially. Largely superseded by diffusion in 2022+. *(Module 5.)*

### GCS
**Graphs of Convex Sets** — an optimization framework where each graph vertex carries a convex set and each edge a convex length function; the shortest-path problem over it jointly selects a discrete path *and* continuous values along it. Its MICP formulation relaxes so tightly that one LP/[SOCP](#socp) plus randomized rounding usually recovers the global optimum — with a free per-query optimality certificate. Also the name of the collision-free motion planner built on it ([source page](sources/gcs-motion-planning-paper.md), [concept page](concepts/robotics/graphs-of-convex-sets.md)). *(Classical-robotics branch.)*

### Game of Life
Conway's 1970 2D [cellular automaton](concepts/alife/cellular-automata.md); one neighbor-count rule yields gliders, glider guns, and Turing-completeness. The archetypal Class-4 CA and the subject of [Wolfram's construction-vs-search innovation study](sources/wolfram-2025-game-of-life-engineering.md). See [Game of Life](entities/game-of-life.md). *(ALife branch.)*

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
**Imitation Learning** — learn a policy from demonstrations. See [imitation learning concept](concepts/learning/imitation-learning.md). *(Module 6.)*

### InfoNCE
**Information Noise-Contrastive Estimation** — the contrastive loss family used by SimCLR, MoCo, and (in policy form) [IBC](entities/ibc.md). *(Module 4 / 7.)*

### IoU
**Intersection over Union** — overlap metric for bounding boxes / masks. *(Module 2.)*

### IRIS
**Iterative Regional Inflation by Semidefinite programming** — algorithm that grows a large collision-free convex polytope around a seed configuration; supplies the safe regions that [GCS](#gcs) planning consumes. `IrisInConfigurationSpace` ships in [Drake](entities/drake.md). *(Classical-robotics branch.)*

### Jacobian
The `m×n` matrix of partial derivatives of a vector function `f: Rⁿ→Rᵐ`, `(∂f/∂x)ᵢⱼ = ∂fᵢ/∂xⱼ`. Vectorized backprop = multiplying Jacobians via the chain rule; SGD then uses the "gradient shape = parameter shape" convention. See [Clark's CS224n gradient notes](sources/clark-computing-nn-gradients.md). *(Module 1.)*

### JEPA
**Joint-Embedding Predictive Architecture** — predict the *embedding* of the next state, not pixels. Yann LeCun's program. See [concept page](concepts/world-models/jepa.md). *(Module 11.)*

### JEPA-WMs
Terver et al., FAIR, Dec 2025 ([source page](sources/jepa-wms-paper.md)); first JEPA-for-robotics paper using [RoboCasa](entities/robocasa.md). *(Module 11.)*

### KI
**Knowledge Insulation** — [Physical Intelligence](entities/physical-intelligence.md) VLA training recipe (Driess et al. 2505.23705): train the VLM backbone on discrete [FAST](entities/fast-action-tokenization.md) action tokens + co-train on VLM data, while a flow-matching action expert learns continuous actions with a **stop-gradient** to the backbone — so the action head can't corrupt pretrained knowledge. Behind [π0.7](entities/pi07.md) / [π*0.6](entities/pistar06.md). See [concept page](concepts/learning/knowledge-insulation.md). *(Module 9.)*

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

### McCormick envelope
The standard convex relaxation of a bilinear term `z = xy` over boxes: four linear inequalities from the products of the variable bounds. Cheap, general, and usually loose — on random [GCS](#gcs) instances the McCormick-based [MICP](#micp) has a **median relaxation gap of 29–34%** and solves 10–13× slower than the perspective formulation ([Marcucci et al. 2021](sources/shortest-paths-in-graphs-of-convex-sets-paper.md) §9). The GCS relaxation *collapses to* the McCormick envelope in the special case of real intervals. *(Classical-robotics branch.)*

### MICP
**Mixed-Integer Convex Program** — an optimization with both continuous and binary variables whose continuous relaxation is convex. Exact solution is branch-and-bound (worst case exponential in the binary count), which is why [GCS](#gcs)'s tight relaxation matters: it lets you skip branch-and-bound entirely. *(Classical-robotics branch.)*

### MADDPG
**Multi-Agent Deep Deterministic Policy Gradient** — Lowe et al. 2017; the canonical [CTDE](#ctde) actor-critic — each agent keeps a critic over the *joint* action to update a decentralized policy. See [multi-agent RL](concepts/learning/multi-agent-rl.md). *(RL branch.)*

### MAE
**Masked Autoencoder** — He et al. 2021; reconstruct image patches with most of the image masked. Predictive (not contrastive) SSL. *(Module 4.)*

### mAP
**mean Average Precision** — the standard object-detection accuracy metric (area under precision–recall, averaged over classes); reported at a single IoU (mAP@0.5) or averaged over IoU 0.5–0.95 (mAP@0.5:0.95). Used throughout [YOLOv11n child detection](sources/ptit-yolov11n-child-detection.md). *(Perception.)*

### MA-POCA
**MultiAgent POsthumous Credit Assignment** — Unity ML-Agents' [CTDE](#ctde) trainer with a shared "coach" critic that tolerates agents joining/leaving mid-episode; self-play-compatible. See [Unity ML-Agents](entities/unity-ml-agents.md) / [multi-agent RL](concepts/learning/multi-agent-rl.md). *(RL branch.)*

### MARL
**Multi-Agent Reinforcement Learning** — RL with several simultaneously-learning agents (cooperative / competitive / mixed), formalized as a [Markov Game](#mg); the central difficulty is non-stationarity. See [concept page](concepts/learning/multi-agent-rl.md). *(RL branch.)*

### MBRL
**Model-Based Reinforcement Learning** — RL with an explicit learned dynamics model (a world model). Dreamer is the canonical MBRL family. *(Modules 8 / 10.)*

### MCP
**Model Context Protocol** — Anthropic-led protocol for connecting LLMs to tools. *(Module 9.)*

### MDP
**Markov Decision Process** — `(S, A, P, R, γ)`: states, actions, transition probabilities, reward function, discount factor. The formalism behind RL. *(Module 8.)*

### MFRL
**Model-Free Reinforcement Learning** — RL without an explicit dynamics model; learn value or policy directly. *(Module 8.)*

### MG
**Markov Game** — a.k.a. stochastic game; the N-agent generalization of an [MDP](#mdp) where transition and reward depend on the *joint* action of all agents. The formalism behind [MARL](#marl). *(RL branch.)*

### MHA
**Multi-Head Attention** — running self-attention with several independent attention heads in parallel. *(Module 3.)*

### MJX
**MuJoCo XLA** — JAX-accelerated MuJoCo; the substrate for [MuJoCo Playground](entities/mujoco-playground.md). *(Module 13.)*

### MLP
**Multi-Layer Perceptron** — the simplest deep NN: stacked fully-connected (`linear`) layers separated by nonlinearities. *(Module 1.)*

### MoCo
**Momentum Contrast** — He et al. 2020; contrastive SSL with a queue of negatives and momentum encoder. *(Module 4.)*

### MoT
**Mixture-of-Transformers** — Liang et al. 2025; a transformer where each layer holds **separate parameter sets per modality/function** (e.g. one tower for autoregressive reasoning, one for diffusion generation) that interact only through shared attention. The backbone of [Cosmos 3](sources/cosmos-3-technical-report.md) (AR reasoner tower + DM generator tower). Distinct from Mixture-of-Experts (token-routed FFNs). *(Module 10.)*

### MPC
**Model Predictive Control** — at each step, plan a short-horizon action sequence using a model, execute the first action, replan. The control method paired with world models in [LeWM](entities/leworldmodel.md), [DINO-WM](entities/dino-wm.md), [V-JEPA 2-AC](entities/v-jepa-2.md). Receding-horizon approximation of the classical [optimal-control](concepts/robotics/optimal-control.md) problem (Bernoulli 1697 → Pontryagin 1956; see [Sussmann & Willems 1997](sources/sussmann-willems-1997-300-years-optimal-control.md) for the lineage). *(Module 10.)*

### MSE
**Mean Squared Error** — `mean((y - ŷ)²)`; the standard regression loss; the loss term in JEPA next-embedding prediction. *(Module 1.)*

### NCE
**Noise-Contrastive Estimation** — Gutmann & Hyvärinen 2010; train by classifying real vs noise. Generalizes to InfoNCE in SSL. *(Modules 4 / 5.)*

### NMS
**Non-Maximum Suppression** — post-processing that removes overlapping duplicate detections by keeping the highest-confidence box and dropping others above an [IoU](#iou) threshold; the merge step in [SAHI](concepts/robotics/sahi-slicing-inference.md). *(Perception.)*

### NN
**Neural Network** — a function built by stacking layers of weighted sums and nonlinearities; trained by gradient descent on a loss. Umbrella term. *(Module 1.)*

### OFT
**Optimized Fine-Tuning** — Kim/Finn/Liang 2025 VLA fine-tuning recipe: parallel decoding + action chunking + continuous L1-regression head (+FiLM). Instantiated as [OpenVLA-OFT](entities/openvla-oft.md); lifts OpenVLA's [LIBERO](entities/libero.md) 76.5→97.1 at 26× throughput. *(Module 9.)*

### OK-Robot
NYU 2024 ([entity](entities/ok-robot.md)); zero-shot pick-and-drop in 10 NYC homes; 58.5% success. *(Module 13.)*

### OpenVLA
Open-weights VLA used as a baseline in many 2024–2026 papers. *(Module 9.)*

### OSC
**Operational Space Control** — Khatib 1987; control the robot in task space (end-effector pose/force) rather than joint space, mapping the task objective through the Jacobian and inertia to joint torques, with a **null space** left over for secondary objectives on a redundant arm. Modern form: a **QP per control tick** with task objectives as costs and position/velocity/torque limits as hard constraints — 200 Hz in the [Diffusion Policy](sources/diffusion-policy-paper.md) haptic-teleop stack. See [concept page](concepts/robotics/operational-space-control.md). *(Classical-robotics branch.)*

### OVMM
**Open Vocabulary Mobile Manipulation** — HomeRobot benchmark for Stretch. *(Module 13.)*

### PAR
**Physically Assistive Robotics** — robots that physically assist disabled users (feeding, dressing, transfer). See [Nanavati 2024 systematic review](sources/nanavati2024-physically-assistive-robots-review.md). *(Module 13.)*

### Perspective function / perspective operator
For a closed convex function `f`, its perspective is `f̃(x, λ) := λ·f(x/λ)` for `λ > 0`, extended so that `f̃(0,0) = 0`; for a set, the perspective is the cone over it. Convexity is preserved and conic representations carry over, so a solver that handles `X` handles `X̃`. The workhorse of [GCS](#gcs): multiplying a cost or constraint by a `0/1` flow variable is ill-defined when the cost is `∞` and the flow is `0`, and the perspective **switches the edge cleanly off instead** ([Marcucci et al. 2021](sources/shortest-paths-in-graphs-of-convex-sets-paper.md)). *(Classical-robotics branch.)*

### π0 / π0.6 (pi-zero)
[Physical Intelligence](entities/physical-intelligence.md)'s flagship cross-platform VLA. π0 ([source page](sources/pi-zero-paper.md)) uses a flow-matching action head on a pre-trained VLM backbone. *(Module 9.)*

### PLDM
**Planning with Latent Dynamics Models** — Sobal et al. ([2025 source page](sources/pldm-paper.md), [entity](entities/pldm.md); 2022 precursor [arxiv 2211.10831](https://arxiv.org/abs/2211.10831) not yet a wiki source page). End-to-end JEPA-style WM trained with VICReg-inspired anti-collapse + inverse-dynamics + similarity loss; ~6 anti-collapse hyperparameters per [LeWM](sources/leworldmodel-paper.md)'s critique. The most-cited "end-to-end JEPA before LeWM" baseline. *(Module 11.)*

### Policy
**Policy** — a function `π(a | o)` (or `π(a | s)`) mapping observation/state to an action (or action distribution). The thing IL and RL train: IL fits π to demonstrations, RL fits π to maximize expected reward. Action heads can be deterministic, Gaussian, categorical, k-means-discretized ([BeT](#bet) / [VQ-BeT](#vq-bet)), or diffusion-based ([Diffusion Policy](sources/diffusion-policy-paper.md)). *(Modules 6 & 8.)*

### PRM
**Probabilistic RoadMap** — Kavraki et al. 1996; the canonical *multi-query* sampling-based planner: sample collision-free configurations offline, connect neighbors into a roadmap graph, then answer queries by graph search. Base version is provably suboptimal (PRM\* is asymptotically optimal); in practice plans are post-processed by short-cutting. The comparison baseline [GCS](#gcs) beats — and, per the GCS authors, generalizes. See [motion planning](concepts/robotics/motion-planning.md). *(Classical-robotics branch.)*

### Predictor
The module in [JEPA](concepts/world-models/jepa.md)-line world models that maps a context embedding `z_t` (often plus an action `a_t`) to a predicted future embedding `ẑ_{t+1}`. Loss is computed in latent space against `z_{t+1} = encoder(x_{t+1})` — *not* against pixels. Typically a small MLP ([DINO-WM](entities/dino-wm.md)) or an [AR](#ar) transformer ([V-JEPA 2-AC](entities/v-jepa-2.md), [LeWM](entities/leworldmodel.md)). The predictor's existence — and the fact that it operates between embeddings rather than over pixels — is what makes "JEPA" predictive (the J for Joint and the P for Predictive). Optionally takes a latent variable `z` to capture irreducible uncertainty about the future ([LeCun 2022, §4.4](sources/lecun2022-path-towards-ami.md)). *(Modules 10–12.)*

### PPO
**Proximal Policy Optimization** — Schulman et al. 2017; the dominant on-policy actor-critic algorithm. *(Module 8.)*

### PWA
**PieceWise-Affine** system — dynamics `s⁺ = A_ν s + B_ν a + c_ν` that switch between a finite set of affine modes according to which convex region `(s,a)` lies in. The standard model for hybrid dynamics: *"almost any dynamical system whose nonlinearity is exclusively due to discrete logics"* can be written this way. Optimal control of PWA systems is the target application of the [GCS](#gcs) framework paper — one graph vertex per (time step, mode), dynamics as edge constraints. *(Classical-robotics branch.)*

### QCQP
**Quadratically Constrained Quadratic Program** — a quadratic objective under quadratic constraints; nonconvex in general. The natural form of quasi-static contact dynamics, where SO(2) rotation constraints and **force × distance** terms are bilinear. Its standard **semidefinite relaxation** turns each contact mode's feasible set into a [spectrahedron](#spectrahedron), which is convex and can therefore be a [GCS](#gcs) vertex — the route by which GCS reaches planning through contact ([Tedrake 2024](sources/tedrake-gcs-foundation-models-talk.md)). *(Classical-robotics branch.)*

### R3M
A pretrained visual encoder for manipulation (Nair et al. 2022); appears as a Diffusion Policy ablation. *(Module 7.)*

### Rule 30
[Wolfram](entities/stephen-wolfram.md)'s 1D elementary [cellular automaton](concepts/alife/cellular-automata.md) that produces apparent randomness from a trivial rule; the canonical example of [computational irreducibility](concepts/alife/cellular-automata.md). *(ALife branch.)*

### ReLU
**Rectified Linear Unit** — the activation function `max(0, x)`; default nonlinearity in deep networks since ~2012. *(Module 1.)*

### ResNet
**Residual Network** — He et al. 2015; CNN with skip connections (`x + F(x)`); enabled training of very deep networks; the BC-line baseline visual encoder. *(Module 2.)*

### RL
**Reinforcement Learning** — learn a policy that maximizes expected reward through environment interaction. Canonical textbook: [Sutton & Barto](sources/sutton-barto-rl-textbook.md). *(Module 8.)*

### RLT
**Reformulation-Linearization Technique** — Sherali & Adams; generate valid inequalities for a nonconvex program by multiplying existing valid inequalities together and linearizing the products. The [GCS](#gcs) MICP is first-level RLT specialized to one bilinear structure, generalized from polytopes to arbitrary closed convex sets and made **set-based** (it needs only a separation oracle, not the defining inequalities). Related hierarchies: Lovász–Schrijver, Lasserre/[SOS](#sos). *(Classical-robotics branch.)*

### RNN
**Recurrent Neural Network** — sequence model that maintains a hidden state across timesteps; superseded by transformers for most tasks. *(Module 3.)*

### ROS / ROS 2
**Robot Operating System** — middleware for robotics software (publish-subscribe + services). *(Module 13.)*

### RUM
**Robot Utility Models** — Etukuru et al., NYU/Meta 2024 ([entity](entities/robot-utility-models.md)); zero-shot mobile-manipulation BC on [Stretch](entities/stretch.md). *(Module 13.)*

### SAC
**Soft Actor-Critic** — Haarnoja et al. 2018; max-entropy off-policy actor-critic for continuous control. See [SAC](entities/sac.md) / [original paper](sources/sac-paper.md) / [Algorithms and Applications](sources/sac-applications-paper.md) (practical SAC = automatic temperature α); the algorithmic root of the [real-world robotic RL](concepts/learning/real-world-robot-rl.md) lineage. *(Module 8.)*

### SAHI
**Slicing Aided Hyper Inference** — Akyon et al. 2022; inference-time small-object trick — slice the image into overlapping patches, detect per patch, merge via [NMS](#nms). See [concept page](concepts/robotics/sahi-slicing-inference.md). *(Perception.)*

### SGD
**Stochastic Gradient Descent** — gradient descent on minibatches; the canonical NN optimizer. *(Module 1.)*

### SOCP
**Second-Order Cone Program** — convex optimization over constraints of the form `‖Ax + b‖₂ ≤ cᵀx + d`. Sits between LP and SDP in expressiveness and cost; efficiently solved by MOSEK/Gurobi. The class [GCS](#gcs) motion planning reduces to — the entire point of choosing Bézier control points over [SOS](#sos) polynomials, which would have forced a mixed-integer *semidefinite* program instead. Exposed through [Drake](entities/drake.md)'s unified mathematical-program interface. *(Classical-robotics branch.)*

### Siamese network
NN architecture with two (or more) weight-tied sub-networks applied to two inputs, with a downstream head over the two embeddings. Introduced by [Bromley, Guyon, LeCun, Säckinger, Shah 1993](sources/bromley1993-siamese-signature-verification.md) for signature verification — two TDNNs + cosine + `±1` targets. Architectural ancestor of [Barlow Twins](sources/barlow-twins-paper.md), [VICReg](sources/vicreg-paper.md), [DINOv2](entities/dinov2.md)/[v3](entities/dinov3.md), and the J/A in [JEPA](concepts/world-models/jepa.md). See [concept page](concepts/world-models/siamese-network.md). *(Module 4.)*

### SIGReg
**Sketched Isotropic Gaussian Regularizer** — introduced by **[LeJEPA](sources/lejepa-paper.md)** (Balestriero & LeCun 2025; cited from [LeWM](entities/leworldmodel.md) as [25]). The single anti-collapse regularizer in LeWM: project latent embeddings onto `M` random unit-norm directions; run the **Epps–Pulley** univariate normality test on each 1-D projection; average the test statistics; backprop the result as a loss term. Justified by the **Cramér–Wold theorem** — matching all 1-D marginals of a `d`-D distribution is equivalent to matching the full joint distribution. Encourages an isotropic Gaussian latent and gives a provable anti-collapse guarantee with a single hyperparameter (`λ`, the SIGReg loss weight; default 0.1) vs. 4–6 for prior end-to-end JEPAs ([PLDM](#pldm)). *(Module 4 introduction; [Module 12 derivation](syntheses/curriculum/curriculum-12-lewm-deep-dive.md).)*

### SimCLR
**Simple framework for Contrastive Learning of Representations** — Chen et al. 2020; contrastive SSL with augmentation and a projection head. *(Module 4.)*

### SLAM
**Simultaneous Localization And Mapping** — classical robotics technique; out-of-scope for this curriculum but you'll see it. *(Out of scope.)*

### SOS
**Sums Of Squares** — a polynomial is SOS if it can be written as a sum of squared polynomials, which certifies nonnegativity and is checkable by semidefinite programming. The standard tool for verified region-of-attraction and containment proofs in model-based control (LQR-Trees; the SOS-based mixed-integer planners [GCS](#gcs) defines itself against). Exposed as its own solver class in [Drake](entities/drake.md). *(Classical-robotics branch.)*

### Spectrahedron
The feasible set of a **semidefinite program** — the intersection of the cone of positive-semidefinite matrices with an affine subspace. Convex by construction, which is the whole point: relax a nonconvex contact-dynamics [QCQP](#qcqp) into an SDP and its feasible set becomes a legal vertex set for a [graph of convex sets](concepts/robotics/graphs-of-convex-sets.md). One spectrahedron per contact mode ([Tedrake 2024](sources/tedrake-gcs-foundation-models-talk.md)). *(Classical-robotics branch.)*

### SSL
**Self-Supervised Learning** — train on unlabeled data by inventing a pretext task whose labels can be derived from the input itself. The umbrella for everything in self-supervised pretraining. *(Module 4.)*

### TD
**Temporal Difference** — bootstrap-style update using `r + γ V(s') − V(s)`; backbone of value-based RL. *(Module 8.)*

### TD-MPC
**Temporal Difference Model Predictive Control** — Hansen et al. 2022 / 2024 ([TD-MPC2 source page](sources/td-mpc2-paper.md), [entity](entities/td-mpc.md)); model-based control combining a learned latent dynamics model with MPC and TD-bootstrapping. Decoder-free (no pixel reconstruction). Baseline in [LeWM](sources/leworldmodel-paper.md). *(Module 10.)*

### TPU
**Tensor Processing Unit** — Google's NN-specialized accelerator. *(Throughout.)*

### Transformer
NN architecture ([Vaswani et al., *Attention Is All You Need*, NeurIPS 2017](sources/attention-is-all-you-need.md)) built around **self-attention** instead of recurrence. A stack of identical blocks; each block applies multi-head self-attention + an MLP + residual connections + [LN](#ln). Replaced [RNNs](#rnn) / [LSTMs](#lstm) as the dominant sequence model and now spans three major shapes: **encoder-only** (BERT, [DINOv2](entities/dinov2.md), [ViT](#vit) for representation learning), **decoder-only** (GPT-family, [LLMs](#llm), [AR](#ar) world-model [predictors](#predictor) as in [LeWM](entities/leworldmodel.md)), and **encoder-decoder** (the original — translation, [VLA](#vla) action heads). Positional information is injected externally — learned position embeddings, sinusoidal embeddings, or modern variants like axial RoPE (used in [DINOv3](entities/dinov3.md)). *(Module 3.)*

### TRPO
**Trust Region Policy Optimization** — Schulman et al. 2015; PPO's predecessor with a hard trust-region constraint. *(Module 8.)*

### UMI
**Universal Manipulation Interface** — Chi et al., RSS 2024 ([source page](sources/umi-paper.md)); hand-held gripper for collecting in-the-wild demonstrations at high throughput (111 demos/hr). *(Module 7.)*

### URDF / MJCF / USD
Robot description formats — XML-based ([URDF](concepts/world-models/world-model-simulators.md) for ROS, MJCF for [MuJoCo](entities/mujoco.md)) and scene-description ([USD / OpenUSD](entities/openusd.md) for NVIDIA Omniverse). *(Module 13.)*

### VAE
**Variational Autoencoder** — Kingma & Welling 2013 ([source page](sources/vae-paper.md), [concept page](concepts/learning/variational-autoencoder.md)); AE with a probabilistic latent space and KL regularization. *(Module 5.)*

### VICReg
**Variance-Invariance-Covariance Regularization** — Bardes, Ponce, LeCun 2022; non-contrastive SSL that prevents collapse via variance and covariance penalties. Same author family as JEPA / SIGReg. *(Module 4.)*

### Visibility graph
Graph over sampled configurations with an edge between any two connected by a straight collision-free line, **regardless of distance** (unlike a [PRM](#prm)'s k-nearest wiring). A **clique** in it — mutually visible samples — approximately corresponds to a convex region of the underlying space, so an approximate **minimum clique cover** of the visibility graph decides where to place [IRIS](#iris) regions. This is what replaced the hand-placed seeds in the original [GCS](#gcs) planner ([Tedrake 2024](sources/tedrake-gcs-foundation-models-talk.md)). *(Classical-robotics branch.)*

### ViT
**Vision Transformer** — [Dosovitskiy et al. 2020 (*An Image Is Worth 16x16 Words*)](sources/vit-paper.md). An image is split into a grid of non-overlapping patches (typically 14×14 or 16×16 pixels); each patch is flattened + linearly projected into a token; a learnable `[CLS]` token is prepended; positional embeddings are added; the resulting sequence is fed through a standard [transformer](#transformer) encoder. Output: a patch-token sequence plus the `[CLS]` token, which serves as the global image embedding. Sized by depth + width: ViT-S/14, ViT-B/14, ViT-L/14, ViT-g/14 (~1.1B params, [DINOv2](entities/dinov2.md)), ViT-7B/16 ([DINOv3](entities/dinov3.md)). The default visual [encoder](#encoder) in JEPA-line models including [LeWM](entities/leworldmodel.md), [V-JEPA 2](entities/v-jepa-2.md), and every DINO-line world model. *(Module 3.)*

### V-JEPA / V-JEPA 2 / V-JEPA 2-AC / V-JEPA 2.1
**Video JEPA** family from Meta FAIR; "AC" = Action-Conditioned. See [V-JEPA 2 entity](entities/v-jepa-2.md). *(Module 11.)*

### VLA
**Vision-Language-Action** — VLM adapted to emit *actions* rather than text; the dominant 2024–2026 generalist-policy paradigm. See [VLA concept](concepts/learning/vla-models.md). *(Module 9.)*

### VLM
**Vision-Language Model** — multimodal model accepting image + text, emitting text (e.g. GPT-4V, Gemini, Claude with vision). *(Module 9.)*

### VQ-BeT
**Vector-Quantized Behavior Transformer** — Lee et al. 2024; replaces BeT's k-means with a learned VQ codebook; top performer in [RUM](entities/robot-utility-models.md) ablations. *(Module 7.)*

### WAM
**World-Action Model** — a model that jointly couples a world model and an action model, so the same network can do forward dynamics, inverse dynamics, **and** act as a policy (predicting actions *and* their visual consequence). Instances: [Cosmos 3](sources/cosmos-3-technical-report.md), DreamZero, GE-Sim2. See [WAM concept](concepts/world-models/world-action-model.md). *(Module 10.)*

### WBC
**Whole-Body Control** — coordinating all of a high-DoF humanoid's joints into stable, dynamically-feasible motion (walk/jump/crouch/loco-manipulate); for learned humanoids, usually posed as RL **motion tracking** of retargeted human mocap. The low-level "System 1" beneath a [VLA](#vla). See [WBC concept](concepts/robotics/whole-body-control.md); instances [SONIC](sources/sonic-paper.md), [MotionBricks](sources/motionbricks-paper.md), [BumbleBee](sources/bumblebee-experts-to-generalist-wbc.md) — all on the [Unitree G1](entities/unitree-g1.md).

### WFM
**World Foundation Model** — NVIDIA marketing term for very-large generative-video world models like [Cosmos](entities/nvidia-cosmos.md). A *type* of WM, not a synonym. *(Module 10.)*

### WM
**World Model** — learned predictive model of environment dynamics: `s_{t+1} = f(s_t, a_t)`. See [concept page](concepts/world-models/world-model.md). *(Module 10.)*

### YOLO
**You Only Look Once** — Redmon et al. 2016; the single-stage real-time object-detector family. The modern lineage (…v8 / v10 / v11 / v26) is maintained as [Ultralytics YOLO](entities/ultralytics-yolo.md); YOLOv11n is the edge-sized variant used in [child detection](sources/ptit-yolov11n-child-detection.md). *(Perception.)*

---

## Mentioned in
- [Robot-learning curriculum](syntheses/curriculum/robot-learning-curriculum.md) — primary consumer.
- [Index](index.md).
- Linked from individual module synthesis pages as they're written.
