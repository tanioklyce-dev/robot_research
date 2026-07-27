---
title: Joint-Embedding Predictive Architecture
type: concept
created: 2026-05-07
updated: 2026-07-26
sources: 33
tags: [jepa, world-model, self-supervised, latent-prediction, lecun, adaln, rope, dinov3, cem, inverse-dynamics, object-centric, spectral-graph-theory, generalization-theory]
---

> [!note] Video overview
> [Welch Labs — "Yann LeCun's $1B Bet Against LLMs" (2026-05-01, ~37 min)](../../sources/welchlabs-lecun-1b-bet-against-llms.md) is the recommended popular-explainer for this page. It walks blurry-pixels → Siamese networks → representation collapse → Barlow Twins → DINO → JEPA with LeCun interview clips, and is a good first encounter with the JEPA story before the primary papers below.

**JEPA (Joint-Embedding Predictive Architecture)** — a family of world models that learn by **predicting the representation of a future state in a learned latent space**, rather than reconstructing pixels or generating video. Defined and named by Yann LeCun in **["A Path Towards Autonomous Machine Intelligence" (2022)](../../sources/lecun2022-path-towards-ami.md)**, the canonical reference for the entire JEPA program.

## What "Joint" means

The **J (Joint-Embedding)** and **A (Architecture)** halves of JEPA descend directly from the **[Siamese network](siamese-network.md)** family — two weight-tied encoders, embeddings compared in a shared latent space — introduced by [Bromley, Guyon, LeCun, Säckinger, Shah 1993](../../sources/bromley1993-siamese-signature-verification.md). JEPA's contribution is the **P (Predictive)**: a learned predictor between embeddings.

**Joint** refers to the fact that both the input (context) and the prediction target (future state) are embedded into the **same shared latent space** by the same encoder:

- `z_t = encoder(x_t)` — current frame
- `z_{t+1} = encoder(x_{t+1})` — future frame, *same encoder*
- Loss: `|| predictor(z_t, a_t) − z_{t+1} ||`

Both sides of the prediction live in the *jointly shared* embedding space. This contrasts with generative/autoregressive models, where the target remains in raw pixel space and the encoder only acts on the input side:

| Architecture | Target is… |
|---|---|
| Generative / autoregressive | Raw pixels — not embedded |
| JEPA | An embedding — same space as the input |

The term **Joint Embedding** names the architecture class defined by this property: all learning — both encoding and prediction — happens inside a single shared representation space. It is also why representation collapse is the central failure mode: if the encoder collapses to a constant, the loss is trivially zero, with no pixel-level signal to expose the problem.

## Core idea
- Encoder maps inputs to a latent embedding `z`.
- Predictor maps `z_t` (and optionally action `a_t`) to a prediction of `z_{t+1}`.
- Loss is computed in **latent space**, not pixel space — sidestepping the cost and ill-posedness of generating high-fidelity video.

## Why this matters for agentic robotics
- **Cost asymmetry**: video-generation world models ([NVIDIA Cosmos](../../entities/nvidia-cosmos.md), [Genie Envisioner](../../entities/genie-envisioner.md)) need to render every frame to compute losses; JEPAs only need a representation, which can be ~100× cheaper at training and inference time.
- **Planning speed**: latent-space MPC can run far faster than video-rollout MPC. [LeWorldModel](../../entities/leworldmodel.md) reports up to **48× faster planning** than foundation-model-based world models.
- **Internet-scale pretraining**: JEPAs can absorb action-free observation data (web video) at scale, then post-train action-conditioned predictors on small interaction datasets. [V-JEPA 2](../../entities/v-jepa-2.md) is the canonical demonstration: 1M+ hours pretraining → 62 hr post-training → zero-shot Franka manipulation.

## Common training challenges
- **Representation collapse** — without the right inductive biases, both encoder and predictor learn trivial constants. The wiki now tracks a **design space of anti-collapse mechanisms**, from heaviest to lightest:
  - **Frozen pre-trained encoder** — [DINO-WM](../../entities/dino-wm.md) sidesteps collapse by not training the encoder at all.
  - **EMA target encoder + stop-gradient** — [V-JEPA 2](../../entities/v-jepa-2.md).
  - **Multi-term variance–covariance regularizers** — [PLDM](../../entities/pldm.md).
  - **Single distributional regularizer (SIGReg)** — [LeWorldModel](../../entities/leworldmodel.md) matches embeddings to an isotropic Gaussian; no EMA / stop-grad / frozen encoder. [Identifiability theory](identifiability.md) later shows the Gaussian is *uniquely* the right target.
  - **Single inverse-dynamics regularizer** — [SMWM](../../entities/smwm.md) (Ivashkov, Balestriero, Schölkopf 2026) predicts the *action* from an embedding pair; recovering it forces the encoder to stay action-informative. Unlike SIGReg it **doesn't prescribe latent geometry** — it anchors the representation to a task-grounded quantity, biasing toward *controllable* degrees of freedom and filtering uncontrollable distractors (a "perception for action" / causal-representation framing).
- **State representation & hierarchy (2026 developments).** Beyond collapse, two other axes are moving: **object-centric states** — [WorldDP](../../entities/worlddp.md) replaces raw DINOv2 patches with slot-attention entity embeddings for better dynamics learning — and **hierarchy for multi-stage tasks** — both [HWM](../../entities/hwm.md) (WM-over-WM) and [WorldDP](../../entities/worlddp.md) (WM-over-diffusion-policy) wrap a JEPA planner in a two-tier subgoal structure to escape the single-stage ceiling.

## Notable instances
- **[V-JEPA 2 / V-JEPA 2-AC](../../entities/v-jepa-2.md)** ([Meta FAIR](../../entities/meta-fair.md) + [Mila](../../entities/mila.md), June 2025) — large-scale video pretraining + action-conditioned post-training; zero-shot Franka.
- **[V-JEPA 2.1](../../sources/v-jepa-2-1-paper.md)** (FAIR + Mila, March 2026) — successor; "dense features" focus; +20pt real-Franka grasping over V-JEPA 2-AC.
- **[LeWorldModel](../../entities/leworldmodel.md)** ([Mila](../../entities/mila.md) + NYU + Samsung SAIL + Brown, March 2026) — first stable end-to-end JEPA with two-term loss; single-GPU training.
- **[JEPA-WMs](../../entities/jepa-wms.md)** (Terver et al., FAIR, Dec 2025) — moves JEPA into [RoboCasa](../../entities/robocasa.md) + Metaworld + DROID + real Franka; outperforms DINO-WM and V-JEPA 2-AC on the proposed setup.
- **[VLA-JEPA](../../entities/vla-jepa.md)** (Sun et al., USTC, Feb 2026) — JEPA-as-auxiliary-objective inside a VLA policy; uses LIBERO + SimplerEnv + real.
- **[VL-JEPA](../../entities/vl-jepa.md)** (Chen et al., Meta/LeCun, Dec 2025) — JEPA reframing of a full **vision-language model**: predict the *embedding* of output text instead of generating tokens. **Different paper from VLA-JEPA despite the name** (see the warning on either entity). 1.6B beats 7B on GQA; ~50% fewer trainable params vs token-space VLM training.
- **JEPA-adjacent (frozen DINOv2 encoder, not co-trained):**
  - **[DINO-WM](../../entities/dino-wm.md)** (Zhou et al., NYU + FAIR, Nov 2024) — DINOv2 features + learned predictor; zero-shot planning. Lightweight benches (PushT, Wall, PointMaze, Rope, Granular, Reacher).
  - **[DINO-world](../../entities/dino-world.md)** (Baldassarre et al., FAIR, July 2025) — DINOv2 features for video world models; predates JEPA-WMs by 5 months and shares Basile Terver as a bridge author.
- Comparison points: [Dreamer / DreamerV3](../../entities/dreamer.md) (task-specific reward, generative WM); [TD-MPC](../../entities/td-mpc.md) (state-based, decoder-free MBRL); [PLDM](../../entities/pldm.md) (end-to-end JEPA with VICReg + inverse-dynamics, ~6 hyperparameters; [Sobal et al. 2025](../../sources/pldm-paper.md)).

## Design-axis lessons for JEPA-WM-style robot planning

The first systematic ablation across architectural / training / planning axes for JEPA-style world models came from [JEPA-WMs (Terver et al., TMLR 05/2026)](../../sources/jepa-wms-paper.md), which beat both [DINO-WM](../../entities/dino-wm.md) and [V-JEPA 2-AC](../../entities/v-jepa-2.md) on every evaluated environment. The findings have become load-bearing recommendations for anyone building this class:

| Axis | Finding |
| --- | --- |
| **Frozen encoder** | DINO ≫ V-JEPA. Fine object segmentation matters more than video pretraining for control. DINOv3 wins only on photorealistic envs (DROID, Robocasa); DINOv2 ties or wins on synthetic. |
| **Predictor conditioning** | **AdaLN+RoPE > sincos / sequence conditioning** on average; per-block AdaLN prevents action-information vanishing through depth. Task-dependent — Metaworld prefers sincos+ftcond. |
| **Multi-step rollout loss** | k = 2 helps in sim; **k = 6 helps on DROID**. Acts as data augmentation against compounding error (scheduled-sampling-analogous). The optimum shifts upward when the per-step error δ_K is dominated by the effective Lipschitz constant Λ_K — i.e., when horizons are long and dynamics are complex. |
| **Context length W** | Must satisfy planning context Wp ≤ training W. Optimal W = 3 in sim, **W = 5 on DROID**. Going higher reduces unique training slices and hurts. |
| **Proprioception** | Always helps when embodiments are aligned (vision alone can't resolve fine end-effector distance). Drop only when targets are misaligned (e.g. DROID → Robocasa zero-shot). |
| **Planner** | **CEM with L₂ embedding distance** is the default that wins overall. NG (Nevergrad NGOpt) ties on real-world manipulation with zero hyperparameter tuning. Gradient-based (Adam, GD) only works on smooth-cost envs like Metaworld; fails on 2D nav + contact-rich manip. L₂ > L₁ consistently. |
| **Model scaling** | Encoder + predictor scaling **only pays off on real-world data** (DROID); saturates at ViT-S, depth 6 on simulated benches. Practical rule: scale capacity only when dynamics are genuinely complex. |

These are the first published systematic ablations of these axes for JEPA-style world models and should anchor any JEPA-WM build that follows.

## Does a JEPA recover the *actual* world? — identifiability

The program's strongest formal result arrived in May 2026: [When Does LeJEPA Learn a World Model?](../../sources/when-does-lejepa-learn-a-world-model-paper.md) proves that [LeJEPA](../../sources/lejepa-paper.md) achieves **[linear identifiability](identifiability.md)** — the learned encoder recovers the true latents up to an orthogonal rotation — and that the **Gaussian latent distribution is uniquely the one for which this holds**. That elevates SIGReg's isotropic-Gaussian target from an anti-collapse trick to the load-bearing choice, and it upgrades the case for latent prediction from "more efficient than pixels" to "under these conditions, the latent space *is* the world's, rotated."

The conditions are strong (stationary additive-noise transitions, Gaussian latents, learned dimension = true dimension), the result is population-level, and it covers the **encoder only** — action-conditioned dynamics `p(z'|z,a)`, which is what a control world model needs, remain unproved.

> [!warning] The theory and the measurements point opposite ways
> Five days earlier, largely the same group published [stable-worldmodel](../../sources/stable-worldmodel-paper.md), showing [LeWorldModel](../../entities/leworldmodel.md) drops from **50.8 % to 6–26 %** on Push-T under color/size/shape shifts, with quadratic decay under distractors — and that **prediction MSE correlates poorly with planning success**. Neither paper addresses the other. Identifiability-under-assumption has not so far produced out-of-distribution robustness.

## Hierarchical JEPA (H-JEPA) — long-horizon planning
The single-level JEPA planning ceiling is short: [LeWorldModel](../../entities/leworldmodel.md) on push-t reliably plans only **~5 prediction loops** ahead before rollouts drift. LeCun's prescribed fix (from the [2022 position paper](../../sources/lecun2022-path-towards-ami.md), restated on camera in the [Welch Labs Part 2 explainer](../../sources/welchlabs-lecun-1b-bet-against-llms-part2.md)): a **hierarchy of predictors** — low levels make detailed short-term predictions; high levels make abstract long-term predictions (fewer details → slower divergence from reality). The **inter-layer interface is an embedding space, "not semantic, certainly not language"** ("your cat can do hierarchical planning"). LeCun's analogy: planning a NYU→Paris trip as sub-goals (airport → taxi → street), not millisecond muscle control.

**Realized as [HWM](../../entities/hwm.md) ("Hierarchical Planning with Latent World Models", [Zhang et al., arXiv 2604.03208, April 2026](../../sources/hwm-paper.md); senior authors LeCun + Ballas).** A **model-agnostic** two-temporal-scale latent MPC wrapper: a high-level planner optimizes latent **macro-actions** to the goal, its first predicted latent becomes a **subgoal**, and a low-level planner optimizes primitive actions toward it (CEM at both scales). Demonstrated on top of [DINO-WM](../../entities/dino-wm.md) (Push-T: **17% → 61%** at the hardest horizon d=75), [PLDM](../../entities/pldm.md) (Diverse Maze: **+39%**), and [V-JEPA 2](../../entities/v-jepa-2.md)-AC (real-Franka pick-&-place: **0% → 70%** from a single goal image). Fig. 6 gives the empirical case: low-level model wins at short horizons (≤1 s), high-level at long horizons (≥1.5 s). **Caveats:** only **two** levels (not the N-level *emergent* hierarchy of the vision) and **goal-image-conditioned** (not language). The Welch Labs video's "push-t 5 → 15 steps" was a simplification of the paper's d=25→75 task-horizon framing.

## Simulator stance — fragmenting, not avoiding
The original wiki synthesis observed [V-JEPA 2](../../entities/v-jepa-2.md) and [LeWM](../../entities/leworldmodel.md) both skipping heavy agentic-robotics sim. With five additional ingests in May 2026, the picture is more nuanced: [JEPA-WMs](../../entities/jepa-wms.md) uses [RoboCasa](../../entities/robocasa.md); [VLA-JEPA](../../entities/vla-jepa.md) uses SimplerEnv; [DINO-WM](../../entities/dino-wm.md) uses lightweight MuJoCo benches; [V-JEPA 2.1](../../sources/v-jepa-2-1-paper.md) continues the no-sim line. **The JEPA literature is fragmenting across simulator weight classes**, not avoiding sim wholesale. See [the revised synthesis](../../syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md).

## Related
- [Identifiability](identifiability.md) — whether a JEPA latent space recovers the world's actual latent variables (proved for LeJEPA under conditions).
- [Learned latent space](latent-space.md) — the substrate JEPAs predict in; the entire design choice rests on this.
- [World-model simulators](world-model-simulators.md) — JEPAs are one of two paradigms (the other being generative-video models).
- [FLARE](flare.md) — a JEPA-adjacent *auxiliary* loss (future-latent alignment with an EMA teacher) added inside a VLA policy; the same joint-embedding-of-the-future commitment applied as a policy co-training signal rather than a standalone WM.
- [Spectral theory of SSL](../learning/spectral-theory-of-ssl.md) — the mathematical backbone (SSL = spectral embedding) under the JEPA/LeJEPA anti-collapse machinery.
- [Instruction leakage](instruction-leakage.md) — an evaluation confound for goal-conditioned JEPA world models.
- [Meta FAIR](../../entities/meta-fair.md) — center of the JEPA research line.
- [Mila](../../entities/mila.md) — frequent contributor.

## Mentioned in
- [Bromley et al. 1993 — Signature Verification using a Siamese TDNN](../../sources/bromley1993-siamese-signature-verification.md) — eponymous Siamese-network paper; the J/A in JEPA descend from this architecture
- [A Path Towards Autonomous Machine Intelligence (LeCun, 2022)](../../sources/lecun2022-path-towards-ami.md) — canonical position paper / definition
- [Barlow Twins Paper (Zbontar et al., ICML 2021)](../../sources/barlow-twins-paper.md) — Joint-Embedding anti-collapse precursor (cross-correlation → I)
- [VICReg Paper (Bardes, Ponce, LeCun, ICLR 2022)](../../sources/vicreg-paper.md) — the regularizer LeCun 2022 endorses as JEPA's anti-collapse method
- [Barlow 1961 — sensory messages](../../sources/barlow1961-sensory-messages.md) — neuroscience origin of the redundancy-reduction principle behind both above
- [V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md)
- [V-JEPA 2.1 Paper](../../sources/v-jepa-2-1-paper.md)
- [LeWorldModel Paper](../../sources/leworldmodel-paper.md)
- [JEPA-WMs Paper](../../sources/jepa-wms-paper.md)
- [DINO-WM Paper](../../sources/dino-wm-paper.md)
- [DINO-world Paper](../../sources/dino-world-paper.md)
- [VLA-JEPA Paper](../../sources/vla-jepa-paper.md)
- [FLARE Paper](../../sources/flare-paper.md) — JEPA-adjacent future-latent-alignment auxiliary loss (NVIDIA GEAR; adopted by GR00T N1.5)
- [Welch Labs — Yann LeCun's $1B Bet Against LLMs Part 2 (video)](../../sources/welchlabs-lecun-1b-bet-against-llms-part2.md) — VL-JEPA, hierarchical JEPA, CEM latent-space planning
- [Hierarchical Planning with Latent World Models (HWM, paper)](../../sources/hwm-paper.md) — the realized H-JEPA
- [PLDM Paper](../../sources/pldm-paper.md)
- [Sobal et al. 2022 — JEPA slow features](../../sources/sobal2022-jepa-slow-features-paper.md)
- [LeJEPA Paper](../../sources/lejepa-paper.md)
- [Welch Labs — Yann LeCun's $1B Bet Against LLMs (video)](../../sources/welchlabs-lecun-1b-bet-against-llms.md)
- [WorldDP Paper (Goswami et al., 2026)](../../sources/worlddp-paper.md) — object-centric states + WM-over-diffusion-policy hierarchy for multi-stage manipulation
- [Sensorimotor World Models Paper (Ivashkov, Balestriero, Schölkopf 2026)](../../sources/sensorimotor-world-models-paper.md) — inverse-dynamics regularization as the sole anti-collapse mechanism
- [A Generalization Theory for JEPA-Based World Models (Cui et al., 2026)](../../sources/jepa-generalization-theory-paper.md) — first finite-sample generalization bound; JEPA pretraining = action-conditioned co-occurrence-matrix factorization ([spectral view](../learning/spectral-theory-of-ssl.md))
- [Grounding Spatial Relations in a Compact World Model (Wang et al., 2026)](../../sources/grounding-spatial-relations-compact-wm-paper.md) — the [instruction-leakage](instruction-leakage.md) evaluation confound in goal-conditioned JEPA world models
