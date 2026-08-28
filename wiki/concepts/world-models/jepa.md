---
title: Joint-Embedding Predictive Architecture
type: concept
created: 2026-05-07
updated: 2026-08-27
sources: 49
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
  - **Single distributional regularizer ([SIGReg](sigreg.md))** — [LeWorldModel](../../entities/leworldmodel.md) matches embeddings to an isotropic Gaussian; no EMA / stop-grad / frozen encoder. [Identifiability theory](identifiability.md) later shows the Gaussian is *uniquely* the right target.
  - **Sparse (non-Gaussian) distribution matching — RDMReg** — [LpWM](../../entities/lpwm.md) matches features to a *Rectified Generalized Gaussian*, giving non-negative exactly-sparse codes. This is the axis-shift worth noting: every mechanism above answers *how do you avoid collapse*; RDMReg is chosen to answer *what latent geometry makes the dynamics cheap to predict*. See [below](#a-second-axis-what-geometry-not-just-how-to-avoid-collapse).
  - **Stop-gradient + covariance regularization** — [DynaMo](../../entities/dynamo.md) (Cui, …, [Pinto](../../entities/lerrel-pinto.md), NeurIPS 2024) pairs SimSiam-style stop-grad with a VICReg-style covariance term (λ=0.04) over a joint **inverse + forward** latent-dynamics objective. Predates the rest of this ladder and sits at its heavy end; notable because it had inverse dynamics as *half the objective* two years before SMWM proposed it as the *sole* defence.
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

## A second axis: *what* geometry, not just *how* to avoid collapse

Anti-collapse mechanisms have been getting lighter (EMA + stop-grad + frozen encoder → VICReg → SIGReg → inverse dynamics). [LpWM](../../entities/lpwm.md) changes the question instead of the weight: given that you must shape the latent distribution somehow, **which shape makes the action-conditioned dynamics easiest to model?**

Its answer is **sparse**, and the claim is specifically about **predictor capacity**, not raw success:

| Predictor capacity | Sparse vs dense on PushT |
|---|---|
| Lowest (linear LTI(1)) | Both fail |
| **Intermediate** | **LpWM +24–57%** — "a shallow predictor plans over sparse codes where it fails over dense ones" |
| Highest (Deep-AdaLN) | Similar — complexity saturates |

Sparse codes also come out **mode-factored**: support encodes the discrete dynamics regime (94–99% decodable on a piecewise-affine navigation task, *even when the zones have no visual cues*), magnitudes encode continuous within-regime state. And the advantage widens with planning horizon.

> [!warning] Sparsity alone does not buy semantics
> On contact-rich OGBench-Cube the support is essentially a **motion detector** (r ≈ 0.87 with effector motion, r ≈ 0.05 with contact), because RDMReg constrains only the per-frame marginal. An added temporal-Jaccard prior makes the support track contact instead (0.05 → 0.61) **at unchanged planning success** — so the interpretable structure and the planning benefit are separable properties.

This sits in tension with the identifiability result below: see [identifiability](identifiability.md) for why the two are not formally contradictory and why the tension is nonetheless real.

## The prediction objective straightens latents on its own

[Temporal Straightening](../../sources/temporal-straightening-paper.md) (ICML 2026) reports that **the JEPA prediction objective alone induces *implicit straightening*** of latent trajectories — an explicit curvature regularizer "further strengthens and stabilizes this effect" rather than creating it. Trained projectors improve planning *even with the regularizer off*, and the authors attribute that to implicit straightening.

That is a claim about why latent prediction works, not just about a new loss term. Straight latent trajectories make **Euclidean distance a usable proxy for geodesic distance** and bound the conditioning of the planning objective — so an architecture trained only to predict next embeddings may be producing planning-friendly geometry as a side effect. See [gradient-based planning](gradient-based-planning.md).

## Adapting a JEPA after deployment

[AdaJEPA](../../entities/adajepa.md) makes the JEPA's own pretraining loss do double duty as a **[test-time adaptation](../learning/test-time-adaptation.md)** signal: inside an MPC loop, the observed next state is a free label for the prediction just made, so **one gradient step per replanning step** recovers much of the out-of-distribution collapse the wiki records for [LeWM](../../entities/leworldmodel.md). It is the first *online* answer here to a fragility every other source addresses offline.

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
- [SIGReg](sigreg.md) — the single-term anti-collapse regularizer, its uniqueness argument, and the three 2026 results that bound it.
- [Spectral theory of SSL](../learning/spectral-theory-of-ssl.md) — the mathematical backbone (SSL = spectral embedding) under the JEPA/LeJEPA anti-collapse machinery.
- [Instruction leakage](instruction-leakage.md) — an evaluation confound for goal-conditioned JEPA world models.
- [Meta FAIR](../../entities/meta-fair.md) — center of the JEPA research line.
- [Mila](../../entities/mila.md) — frequent contributor.

## Mentioned in

> [!note] Curated list — **49** source pages link here; the ones below are those that shaped this page.

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

## How much of the advantage is latent prediction, specifically? (2026 probe evidence)

Two 2026 studies put JEPA encoders and pixel-space models on **one shared axis** for the first time — a frozen-feature probe rather than a video-quality leaderboard. Both favour latent prediction; both qualify how much of the credit it deserves.

**The decomposition** ([action-relevant latents](../../sources/action-relevant-latents-paper.md), LIBERO task-OOD, inverse-dynamics probe R²):

| | Frozen | +ID | Δ |
|---|---:|---:|---:|
| V-JEPA 2 ViT-L (video + JEPA prediction) | 0.40 | **0.85** | +0.45 |
| VideoMAE V1 ViT-L (video + pixel MAE) | 0.46 | 0.75 | +0.29 |
| Web-DINO ViT-L (image SSL) | −0.01 | 0.16 | +0.17 |
| Cosmos-1 tokenizer (pixel reconstruction) | −0.36 | −0.29 | +0.07 |

Read the gaps: **natural-video temporal context** explains most of the distance from image-only SSL to VideoMAE; **the JEPA feature-level predictive objective is worth about +0.10** on top of pixel-level masked autoencoding. Real, and smaller than the JEPA literature's framing implies.

Three findings that sharpen the picture:

- **Pixel fidelity and action recoverability are orthogonal.** At ~20 dB PSNR, frozen action R² spans −0.01 to +0.46; the highest-PSNR backbones post the lowest action R². Optimizing appearance does not organize a latent space around what actions control.
- **The advantage is concentrated on rotation.** Translation and gripper state are recoverable from weak features; **rotation** collapses outside the video-predictive family — negative R² for image-SSL and reconstruction encoders even after inverse-dynamics tuning. Only V-JEPA sustains all three axes.
- **Action signal peaks mid-trunk.** A per-layer probe of V-JEPA 2 ViT-L peaks at **layer 14 (0.51)** and decays to **layer 22 (0.39)** — the JEPA objective pushes action-readout quality *away* from the final layers. Practical consequence for any VLA using a V-JEPA front-end: **final-layer features sample near the trunk's worst point for action decoding.**

> [!warning] Contradiction — is JEPA distinct from image-SSL, or is "semantic" one category?
> **[Action-relevant latents](../../sources/action-relevant-latents-paper.md) says distinct.** Web-DINO and SigLIP 2 stay at **0.16–0.17** action R² after the same inverse-dynamics tuning — clustered with reconstruction encoders, going *negative on rotation*, and a λ sweep across five orders of magnitude can't move them: "the limitation is representational rather than optimization-related." It states explicitly that the data "does not support grouping V-JEPA with image-only semantic SSL methods."
>
> **[Reconstruction or Semantics?](../../sources/latent-space-robotic-world-models-paper.md) says one category.** As latent spaces for a diffusion world model on Bridge V2, Web-DINO reaches IDM Pearson **r = 0.820** against V-JEPA 2.1's 0.829, and SigLIP 2 posts the best generated-latent success-classifier accuracy. All three are grouped as "semantic" and all three beat every reconstruction encoder.
>
> Candidate reconciliations: **Pearson r vs R²** (r ignores scale and bias errors that R² punishes); **spatial patch latents vs mean-pooled features**; **real Bridge V2 vs simulated LIBERO task-OOD**; and **aggregate-over-7-DoF masking a rotation-specific collapse**. None verified.
>
> **Identity resolved 2026-08-26**: **Web-DINO is the DINO member of the [Web-SSL](../../entities/webssl.md) family** ([paper](../../sources/webssl-paper.md)) — the same models [Patch Policy](../../entities/patch-policy.md) recommends as the *best* frozen backbone for robot learning. So the disagreement is not two encoders but **one encoder measured for three different jobs**: strong as a policy feature extractor, weak as an action-decoding substrate, decent as a rollout-success judge. That does not resolve the r-vs-R² question, but it removes the possibility that different models were being compared.
>
> Both agree on what matters most — reconstruction-aligned latents are the worst control substrate and V-JEPA is the best. They disagree on where **[DINO-WM](../../entities/dino-wm.md)**'s frozen image-SSL encoder sits, which is not a small disagreement for that design.

**Robustness** ([latent video prediction](../../sources/latent-video-prediction-better-world-models-paper.md), four matched-capacity ViT-Ls on SSv2): V-JEPA 2.1 leads on five of six corruption types; V-JEPA models uniquely encode the **arrow of time** (under reversal they flip to semantically antonymous classes — pushing ↔ pulling); and they detect *pretend* actions best precisely where the cue is **the absence of physical contact** — without ever reconstructing a pixel. A frozen V-JEPA 2 with a light probe beats a fully fine-tuned VideoMAE and a supervised TimeSformer on corruption and occlusion.

And the caution that generalizes beyond JEPA: **stable features are not usable features.** VideoPrism holds representational similarity above 0.98 under severe patch dropout while collapsing to **2.7%** top-1; V-JEPA 2.1 retains **46.1%**.

## Mentioned in (additional)

- [What Makes Video World Model Latents Action-Relevant](../../sources/action-relevant-latents-paper.md) — the shared inverse-dynamics probe; the ~+0.10 attribution; rotation; the per-layer profile.
- [Latent Video Prediction Learns Better World Models](../../sources/latent-video-prediction-better-world-models-paper.md) — five robustness axes; arrow of time; stable ≠ usable.
- [Reconstruction or Semantics?](../../sources/latent-space-robotic-world-models-paper.md) — V-JEPA 2.1 as the strongest latent space for a robotic diffusion world model; ~2× VLA-in-the-loop success over VAE latents.
- [LpWM paper (Kuang et al., 2026)](../../sources/lpwm-paper.md) — sparse latent geometry lowers predictor capacity needed to plan; mode-factored codes.
- [AdaJEPA paper (Wang, Bounou, LeCun, Ren 2026)](../../sources/adajepa-paper.md) — test-time adaptation of a latent world model inside MPC.
- [HP-JEPA paper (Xu et al., 2026)](../../sources/hp-jepa-paper.md) — JEPA on graphs with a bank of coarse-to-fine partition resolutions. A reminder that **"hierarchical JEPA" names two distinct programs**: temporal abstraction for planning ([HWM](../../entities/hwm.md)) and structural resolution for representation (this). Do not conflate them.
- [Music-JEPA paper (Wang, Fang, LeCun 2026)](../../sources/music-jepa-paper.md) — the action-conditioned formulation outside vision (audio = state, pianoroll = action); action conditioning is what makes the latent dynamics temporally discriminative (target-state win rate **0.991 vs 0.576** for a passive audio-only JEPA).
- [TDV paper (Daithankar, Gladstone, LeCun, Ji 2026)](../../sources/tdv-paper.md) — architectural cousin (`z_t + Δz_t = z_{t+1}`) with the scaling argument for *why* anti-collapse machinery should keep getting lighter: **optimal inductive-bias strength decreases as data grows.**- [Temporal Straightening paper (Wang, Bounou, Zhou, Balestriero, Rudner, LeCun, Ren — ICML 2026)](../../sources/temporal-straightening-paper.md) — curvature regularization; **the JEPA objective induces implicit straightening**; open-loop planning +20–60%.
- [Closing the Train-Test Gap paper (Parthasarathy et al., 2025)](../../sources/train-test-gap-world-models-paper.md) — why gradient-based planning through a JEPA-style world model behaves like an adversarial attack on it, and two train-time fixes.
- [DynaMo paper (Cui et al., NeurIPS 2024)](../../sources/dynamo-paper.md) — in-domain latent inverse+forward dynamics pretraining; a JEPA in everything but the label.
- [Scaling Language-Free Visual Representation Learning](../../sources/webssl-paper.md) — the Web-SSL / Web-DINO primary, resolving the identity above; language-free SSL matching CLIP at scale.
