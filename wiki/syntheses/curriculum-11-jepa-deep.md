---
title: Curriculum Module 11 — JEPA in depth
type: synthesis
created: 2026-05-10
updated: 2026-05-10
tags: [curriculum, module-11, jepa, v-jepa, dino-wm, jepa-wms, latent-prediction, representation-collapse, action-conditioning, lecun]
prereqs: [curriculum-04, curriculum-10]
status: draft
---

> [!note] Curriculum context
> This is **Module 11** of the [Robot-learning curriculum](robot-learning-curriculum.md). It builds directly on **[Module 10](curriculum-10-world-models.md)** (world-model taxonomy) and **[Module 4](robot-learning-curriculum.md)** (SSL + collapse). It precedes **[Module 12](robot-learning-curriculum.md)** (the [LeWM](../entities/leworldmodel.md) deep-dive with full SIGReg math).
>
> Module 11 goes deep on **two of the four families from Module 10**: **JEPA / latent-prediction** (family 2) and **frozen-foundation-feature** (family 3). The other two families (generative-video, reward-conditioned MBRL) stay in Module 10.
>
> The SIGReg math itself is deliberately deferred to Module 12. This module sets up *why* SIGReg matters by walking the collapse-prevention zoo it replaces.
>
> Acronyms used here are also in the [Glossary](../glossary.md). First-mention links go there.

## What this module is

A close walk through the JEPA family circa 2024–2026: what "joint embedding" actually means as an architectural commitment, how the V-JEPA progression evolved over 18 months, the **collapse-prevention zoo** that every end-to-end JEPA needs to dodge representation collapse, and the **frozen-feature** alternative ([DINO-WM](../entities/dino-wm.md)) that sidesteps collapse by not training the encoder at all. We end with [JEPA-WMs](../entities/jepa-wms.md) — the first JEPA-for-real-robotics demonstration on Franka — and a concrete positioning of [LeWM](../entities/leworldmodel.md) against V-JEPA 2 as the bridge into Module 12.

By the end you should be able to:

1. Define "joint embedding" precisely and explain why representation collapse is a *first-order* failure mode, not a curiosity.
2. Walk the **V-JEPA 1 → V-JEPA 2 → V-JEPA 2-AC → V-JEPA 2.1** progression and name what each version added.
3. Read any JEPA-line paper's training section and identify which collapse-prevention mechanisms it uses (EMA target, stop-gradient, frozen encoder, multi-term loss, normality regularizer).
4. Distinguish **end-to-end JEPA** ([LeWM](../entities/leworldmodel.md), V-JEPA 2, [PLDM](../entities/pldm.md)) from **frozen-feature pseudo-JEPA** ([DINO-WM](../entities/dino-wm.md), [DINO-world](../entities/dino-world.md), [JEPA-WMs](../entities/jepa-wms.md)) and articulate the tradeoff.
5. Explain action conditioning in JEPA — including why pretraining is action-free and post-training adds actions.
6. Position LeWM against V-JEPA 2 axis-by-axis as the setup for Module 12.

## What "joint embedding" means

The JEPA name is loaded with technical content. Pull it apart:

- **Joint** — the *same* encoder embeds both the input (context) and the prediction target (future state) into the *same* shared latent space.
- **Embedding** — the prediction loss is computed in latent space, not pixel space.
- **Predictive Architecture** — there is a predictor `g` that maps `(z_t, a_t) → z_{t+1}`.

Concretely:

```
z_t     = encoder(x_t)               // current frame
z_{t+1} = encoder(x_{t+1})           // future frame, SAME encoder
ẑ_{t+1} = predictor(z_t, a_t)        // predicted next embedding
loss     = ‖ẑ_{t+1} − z_{t+1}‖²
```

This stands in contrast to **generative / autoregressive** world models where the target stays in pixel space:

| Architecture | Encoder applied to … | Target | Loss in |
| --- | --- | --- | --- |
| Generative / autoregressive | input only | raw pixels (not embedded) | pixel space |
| **JEPA** | both input and target (same encoder) | embedding | latent space |

The "Joint" property — both sides of the prediction live in one shared latent — is the architectural commitment. It's also the reason **representation collapse** is a *first-order* failure mode and not a curiosity: if `encoder(·)` collapses to a constant vector, both `z_t` and `z_{t+1}` are that constant, the loss is identically zero, and there's no pixel-level signal to expose the pathology. The training procedure converges to garbage with the lowest possible loss.

The whole technical apparatus that distinguishes one JEPA from another in 2024–2026 is essentially **how each design prevents collapse while letting the encoder still learn useful structure.**

## The collapse-prevention zoo

The central engineering problem in JEPA training. Roughly six families of fixes have been used:

### 1. EMA target encoder + stop-gradient (BYOL-line)

**Idea.** Maintain a *second* encoder, `target_encoder`, whose weights are an [exponential moving average](../glossary.md#ema) of the main encoder. Use the target encoder to compute `z_{t+1}` (the prediction target). Stop gradients through it.

```
z_t     = encoder(x_t)
z_{t+1} = target_encoder(x_{t+1})    // STOP GRAD; weights = EMA(encoder)
ẑ_{t+1} = predictor(z_t, a_t)
loss     = ‖ẑ_{t+1} − z_{t+1}‖²
target_encoder.weights ← τ · target_encoder.weights + (1−τ) · encoder.weights
```

**Why it works.** The target encoder is a *slowly-updating teacher*. The main encoder can't trivially lower the loss by collapsing both encoders together — the target encoder lags. Empirically prevents collapse without negative samples ([BYOL](../glossary.md#byol)-line: BYOL, [DINO](../glossary.md#dino), V-JEPA).

**Cost.** Hyperparameters: the EMA decay rate `τ`. Doubled forward-pass cost (two encoders). Conceptual complexity (now there are two networks, only one of which actually gets used at deploy).

**Used by.** [V-JEPA 2](../entities/v-jepa-2.md) (EMA + L1 loss). [BYOL](../glossary.md#byol). [DINO](../glossary.md#dino) / [DINOv2](../entities/dinov2.md).

### 2. Variance-covariance regularization (VICReg-line)

**Idea.** Add explicit penalties to the loss that *prevent* collapse:

- **Variance term** — penalize embeddings with low variance across a batch. Forces the encoder to produce diverse embeddings.
- **Covariance term** — penalize off-diagonal entries of the embedding covariance matrix. Forces feature dimensions to be decorrelated.
- **Invariance term** — the prediction loss itself.

```
loss = λ₁ · invariance + λ₂ · variance + λ₃ · covariance
```

**Why it works.** Hard to collapse to a constant when the loss explicitly punishes low variance. Also avoids the EMA / stop-gradient asymmetry.

**Cost.** Three hyperparameters (`λ₁`, `λ₂`, `λ₃`) plus the variance threshold.

**Used by.** [VICReg](../glossary.md#vicreg). [Barlow Twins](../glossary.md#barlow-twins) (cross-correlation-based variant).

### 3. Frozen pretrained encoder (DINO-WM-line)

**Idea.** Don't train the encoder at all. Load a strong pretrained encoder ([DINOv2](../entities/dinov2.md) is the canonical choice in 2024–2026) and freeze it. Train only the predictor.

```
z_t     = frozen_dinov2(x_t)         // no gradient
z_{t+1} = frozen_dinov2(x_{t+1})     // no gradient
ẑ_{t+1} = predictor(z_t, a_t)
loss     = ‖ẑ_{t+1} − z_{t+1}‖²
```

**Why it works.** The encoder *can't* collapse because it's not training. The latent space's quality is exactly DINOv2's quality. The predictor learns to predict in that space.

**Cost.** You're stuck with DINOv2's representational choices. DINOv2 was not trained on robot data; its features may not be ideal for control. End-to-end variants can be better when training data is on-task.

**Used by.** [DINO-WM](../entities/dino-wm.md). [DINO-world](../entities/dino-world.md). [JEPA-WMs](../entities/jepa-wms.md).

> [!note] Is "frozen-feature" really JEPA?
> Strictly, JEPA's defining commitment is *joint* embedding — same trainable encoder for both inputs. A frozen pretrained encoder is the same encoder for both inputs but it isn't trained, so the "predictive architecture" half is the only thing actually being trained. By 2026 the wiki and the field treat this as **JEPA-adjacent** rather than strict JEPA. Module 10's family 3 (frozen-foundation-feature) is the right home for these.

### 4. Asymmetric augmentation (SimCLR-line, less common in JEPA proper)

**Idea.** Apply different augmentations to context and target. The encoder must be *invariant* to those augmentations to lower loss; meanwhile the augmentations rule out trivial constant solutions because the input distribution is rich.

**Why it works.** Common in [SimCLR](../glossary.md#simclr) / [MoCo](../glossary.md#moco) contrastive SSL. Used in some early JEPA variants but generally combined with other tricks.

**Cost.** Augmentation choice becomes a hyperparameter. Domain-specific (image augmentations don't trivially translate to robot trajectories).

### 5. Multiple-fix soup (PLDM-class)

**Idea.** Combine several mechanisms — VICReg-style variance-covariance + similarity loss + inverse-dynamics auxiliary, sometimes with EMA or augmentation on top — and tune their relative weights. The pre-LeWM end-to-end JEPA literature mostly lives here. The canonical reference is [PLDM (Sobal et al. 2025)](../sources/pldm-paper.md), which combines a similarity loss + VICReg-inspired anti-collapse + inverse-dynamics modeling.

**Why it works.** Layered defense. Each mechanism addresses a slightly different failure mode.

**Cost.** **4–6 anti-collapse hyperparameters per design.** This is what [LeWM](../entities/leworldmodel.md) explicitly responds to — its critique of [PLDM](../entities/pldm.md) is that 6 hyperparameters is more knobs than the underlying problem requires.

**Used by.** [PLDM](../entities/pldm.md) and most pre-2026 end-to-end JEPAs.

### 6. SIGReg — single regularizer (LeJEPA / LeWM)

**Idea.** Project embeddings onto random univariate directions; run a normality test on the resulting 1D distribution; backprop the test statistic. Encourages the latent to be **isotropic Gaussian**, which is incompatible with collapse to a constant (a constant has zero variance, far from any reasonable Gaussian).

**Why it works.** Mathematical statement of "the latent should be diverse and Gaussian-shaped" with a provable anti-collapse guarantee — and only **one hyperparameter** (the SIGReg loss weight). The foundational paper, [LeJEPA (Balestriero & LeCun 2025)](../sources/lejepa-paper.md), proves that isotropic Gaussian is the optimal embedding distribution for minimizing downstream prediction risk.

**Cost.** SIGReg requires a random-projection step + a normality test + backprop through that test statistic. Computationally cheap. The math is non-trivial — Module 12's centerpiece.

**Used by.** [LeJEPA](../sources/lejepa-paper.md) (the SSL setting; ImageNet-1k linear-eval at 79% on ViT-H/14, validated across 10+ datasets / 60+ architectures); [LeWM](../entities/leworldmodel.md) (the action-conditioned WM setting).

### Side-by-side

| Mechanism | Hyperparameters | Used by | Pros | Cons |
| --- | --- | --- | --- | --- |
| EMA + stop-grad | 1 (`τ`) | [V-JEPA 2](../entities/v-jepa-2.md), [BYOL](../glossary.md#byol), [DINO](../glossary.md#dino) | Empirically robust; well-studied | Two encoders; ~2× FLOPs |
| Variance-covariance | 3 (`λ₁`, `λ₂`, `λ₃`) | [VICReg](../glossary.md#vicreg), [Barlow Twins](../glossary.md#barlow-twins) | No EMA needed | More knobs |
| Frozen encoder | 0 | [DINO-WM](../entities/dino-wm.md), [JEPA-WMs](../entities/jepa-wms.md) | Trivially stable; cheap | Stuck with off-the-shelf encoder |
| Multi-fix soup | 4–6 | [PLDM](../entities/pldm.md), pre-2026 end-to-end JEPAs | Layered defense | Hyperparameter hell |
| SIGReg | 1 | [LeJEPA](../sources/lejepa-paper.md) (SSL; up to 1.8B-param ViT-g; 10+ datasets / 60+ architectures); [LeWM](../entities/leworldmodel.md) (action-conditioned WM) | One knob; provable anti-collapse via hyperspherical Cramér–Wold + Epps–Pulley | Math is novel; two papers of evidence so far |

The LeWM contribution is exactly the bottom row: a *theoretical* simplification (one regularizer; one hyperparameter) that empirically beats the multi-fix soup on the same benchmarks. Module 12 derives the mathematics. Module 11's job is to make you ready to evaluate that contribution against the rest of the row above it.

## The V-JEPA progression

The flagship JEPA family from [Meta FAIR](../entities/meta-fair.md), led by Adrien Bardes (and many co-authors). Four canonical versions across roughly 18 months.

### V-JEPA 1 (Bardes et al., 2024)

- **Setup.** Image / video JEPA with EMA target + stop-gradient. Pretrained on internet video.
- **Demonstrated.** Strong representation-learning results — SSv2, Kinetics, ImageNet-class downstream tasks. Not yet a robotics-relevant capability claim.
- **Status in this curriculum.** Read once for context; V-JEPA 2 is the version this curriculum cares about.

### V-JEPA 2 (Bardes et al., June 2025)

- **Setup.** ViT-g (1B parameters) encoder. Pretrained on **22M videos / 1M+ hours of internet video**. Visual mask denoising in representation space (not pixel space). EMA target encoder, L1 loss. 3D-RoPE positions, progressive resolution.
- **Demonstrated.** SSv2 motion understanding (77.3 top-1). Epic-Kitchens-100 action anticipation (39.7 R@5, SOTA). LLM-aligned VQA (PerceptionTest 84.0, TempCompass 76.9 at 8B-parameter scale). The V-JEPA 2 encoder works as a vision backbone for multimodal LLMs.
- **Source.** [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md).

### V-JEPA 2-AC (action-conditioned post-training)

- **Setup.** Frozen V-JEPA 2 encoder. **300M-param transformer predictor** with block-causal attention. Autoregressively predicts the representation of the next video frame from past frames + actions + end-effector states.
- **Training data.** **62 hours of [DROID](../entities/droid.md) robot data** for the action-conditioned post-training stage.
- **Demonstrated.** **Zero-shot pick-and-place on Franka arms in two new labs.** Image-goal MPC. **No data, no training, no rewards from those robots.** This is the cleanest published demonstration of latent-prediction world models doing real-robot manipulation with minimal robot-specific data.
- **Why this matters.** The [generative-video vs JEPA synthesis](generative-video-vs-jepa-world-models.md) flags this as the strongest cross-paradigm validation in the literature. Internet-scale observation pretraining + tiny action-data post-training = a usable on-robot world model. The **two-stage recipe** (action-free pretraining → action-conditioned fine-tune) is the canonical V-JEPA-line workflow.

### V-JEPA 2.1 (Bardes et al., March 2026)

- **Setup.** Family of variants from ViT-B (80M) to ViT-G (2B). Key additions: **dense predictive loss**, **deep self-supervision**, **multi-modal tokenizers**.
- **Demonstrated.** **+20pt real-Franka grasping over V-JEPA 2-AC** per secondary citations. The "dense features" focus continues the JEPA representational-quality push.
- **Source.** [V-JEPA 2.1 Paper](../sources/v-jepa-2-1-paper.md).
- **Status in the curriculum.** Read for what V-JEPA 2 looks like 9 months later. Module 12's LeWM is contemporary with V-JEPA 2.1; the two represent different bets (tiny-end-to-end-task-specific vs huge-pretrained-generalist).

### Variant scale across the V-JEPA family

| Version | Params | Pretraining | Downstream / robot result |
| --- | --- | --- | --- |
| V-JEPA 1 | 100M–1B | internet image / video | representation benchmarks |
| V-JEPA 2 | 1B (ViT-g) | 22M videos, 1M+ hrs | SSv2 77.3; PerceptionTest 84.0 |
| V-JEPA 2-AC | + 300M predictor | + 62 hr DROID | zero-shot Franka pick-and-place |
| V-JEPA 2.1 | 80M–2B | + dense + multi-modal | +20pt real-Franka grasping |

## Frozen-feature variants

Family 3 from Module 10. **Don't train the encoder.** The simplification this enables is dramatic.

### DINO-WM (Zhou et al., NYU + FAIR, Nov 2024)

- **Setup.** Frozen [DINOv2](../entities/dinov2.md) encoder. Learned predictor only. ViT-L/14 backbone.
- **Benchmarks.** Lightweight MuJoCo / 2D — **PushT**, Wall, PointMaze, Rope, Granular, Reacher.
- **Demonstrated.** **Zero-shot planning on novel tasks.** The headline claim is that frozen-DINOv2 + predictor + MPC generalizes well to held-out tasks the predictor was never trained on.
- **Source.** [DINO-WM Paper](../sources/dino-wm-paper.md).

The DINO-WM bet: representation quality from a generic foundation encoder is *good enough* for closed-loop control on lightweight benchmarks, and the simplification it buys is worth the loss of task-shaped representation. LeWM's response is "for tasks where data is on-task, an end-to-end small encoder beats DINOv2."

### DINO-world (Baldassarre et al., FAIR, July 2025)

- **Setup.** Frozen DINOv2 encoder for *video* world models. Same family as DINO-WM but at video / FAIR scale.
- **Status.** Less robotics-direct; share Basile Terver as bridge author into JEPA-WMs.
- **Source.** [DINO-world Paper](../sources/dino-world-paper.md).

### JEPA-WMs (Terver et al., FAIR, December 2025)

- **Setup.** Frozen DINOv2 encoder + learned predictor. Architecturally a DINO-WM successor; published from the FAIR side of the JEPA program.
- **Benchmarks.** **[RoboCasa](../entities/robocasa.md)**, Metaworld, [DROID](../entities/droid.md), and **real Franka** — the first JEPA paper to evaluate at this breadth, and the first to *use [RoboCasa](../entities/robocasa.md)* in the JEPA literature.
- **Demonstrated.** Outperforms DINO-WM and V-JEPA 2-AC on the proposed setup.
- **Significance.** The first JEPA-for-robotics paper that doesn't artificially limit itself to lightweight benches. The [why JEPA research skips the simulator stack](why-jepa-research-skips-the-simulator-stack.md) synthesis was substantially revised after this and four other ingests in May 2026 — the JEPA literature is *fragmenting* across simulator weight classes, not avoiding sim wholesale.
- **Source.** [JEPA-WMs Paper](../sources/jepa-wms-paper.md).

## Action conditioning

JEPA started as a representation-learning idea — *no actions in pretraining at all.* Action conditioning is added in a second stage. Why this matters:

- **Pretraining at internet scale is action-free.** Web video doesn't come with action labels. JEPA's pretraining objective (predict next-embedding from past embeddings) doesn't *need* actions.
- **Action data is the bottleneck.** Per [Module 6](curriculum-06-imitation-learning.md), demonstrations are the limiting resource. Getting any action labels at all requires teleoperation or scripted demos.
- **The two-stage recipe.** [V-JEPA 2-AC](../entities/v-jepa-2.md) instantiates this: pretrain on 1M+ hours of action-free internet video → post-train a 300M-param predictor on 62 hours of [DROID](../entities/droid.md) action-labeled data. The post-training stage is **~16,000× smaller** than the pretraining stage.

What action conditioning looks like at the predictor level:

```
ẑ_{t+1} = predictor(z_t, a_t)              // basic
ẑ_{t+H} = predictor.rollout(z_t, a_{t..t+H−1})   // multi-step rollout for MPC
```

The predictor is typically a transformer with `(z_t, a_t)` as input tokens; in [LeWM](../entities/leworldmodel.md) it's a **causal autoregressive ([AR](../glossary.md#ar)) transformer** so multi-step rollouts can be done efficiently in one forward pass.

> [!note] Key implication for home robotics
> Action-free pretraining + small-action post-training is the most plausible path for JEPA to become useful in home environments where teleop data is scarce. [Module 13](robot-learning-curriculum.md) revisits this; [LeWM-on-Stretch feasibility](lewm-on-stretch-feasibility.md) and [DINO-WM-on-Stretch experiment plan](dino-wm-on-stretch-experiment.md) are the concrete artifacts.

## VLA-JEPA — JEPA-as-auxiliary

[VLA-JEPA](../entities/vla-jepa.md) (Sun et al., February 2026) — the cross-over point with [Module 9](robot-learning-curriculum.md).

- **Idea.** Don't replace the VLA. *Add* a JEPA-style next-embedding-prediction loss as an **auxiliary objective** during VLA training.
- **Setup.** A VLA policy is trained with the standard imitation loss + a JEPA auxiliary that predicts future visual embeddings.
- **Benchmarks.** [LIBERO](../glossary.md#libero), SimplerEnv, real robots.
- **Why it matters.** Suggests JEPA may not be the only WM family that wins; instead, JEPA-style losses may become a *component* of policy training across paradigms. Like contrastive learning's evolution from "the way you train" to "one term in your loss."
- **Source.** [VLA-JEPA Paper](../sources/vla-jepa-paper.md).

This is one of the more interesting recent results in the JEPA program — the implicit claim is that the JEPA pretext task is *useful* even when you're training a different model class. Modules 11 and 9 are both touched by it.

## Where LeWM fits — axis-by-axis vs V-JEPA 2

The bridge into [Module 12](robot-learning-curriculum.md). Module 10 had a similar table at higher level; Module 11 makes the comparison precise against V-JEPA 2 specifically.

| Axis | V-JEPA 2 / 2-AC | [LeWM](../entities/leworldmodel.md) |
| --- | --- | --- |
| **Encoder size** | ViT-g, 1B params | Small ViT, ~15M params |
| **Encoder training** | trained, with EMA target + stop-gradient | trained, **end-to-end, no EMA, no stop-grad** |
| **Pretraining data** | 22M videos / 1M+ hours of internet video | none — task-specific from raw pixels |
| **Action-conditioning stage** | 300M-param predictor post-trained on 62 hr DROID | predictor co-trained from start |
| **Predictor** | block-causal transformer | **causal AR transformer over `(z, a)`** |
| **Anti-collapse mechanism** | EMA + stop-gradient + L1 loss + (implicit) augmentation | **single SIGReg regularizer** |
| **Anti-collapse hyperparameters** | ~3 (EMA decay, L1 weight, optimizer) | **1 (SIGReg loss weight)** |
| **Planner** | image-goal MPC | image-goal MPC (CEM and gradient variants) |
| **Value function** | none | none |
| **Real-robot zero-shot** | Franka pick-and-place in two labs | not tested; sim-only paper |

The reading: **V-JEPA 2 is the maximal-pretraining-and-data-scale point** in the JEPA design space. **LeWM is the minimal-and-task-specific** point. They share the JEPA architectural commitment but make almost-opposite engineering choices everywhere else.

The two are not competing for the same job. V-JEPA 2 is a *generalist* pretrain-then-finetune model; LeWM is a *single-task* end-to-end one. The methodological contribution of LeWM is *not* that it scales better — it doesn't — but that it shows you can train a stable end-to-end JEPA from raw pixels with **one** hyperparameter, where the prior literature said you need 4–6.

## Anchor exercise

> **Annotate the LeWM architecture figure with which design choices match V-JEPA 2 and which differ.**

Concrete steps:

1. Pull the LeWM paper figure 1 from [`sources/leworldmodel-paper.md`](../sources/leworldmodel-paper.md) (re-reading is cheap; the paper is filed).
2. List the components: **encoder**, **predictor**, **action-conditioning path**, **loss terms**, **anti-collapse mechanism**.
3. For each component, write **same as V-JEPA 2** or **different** and one sentence on what changed.
4. Make a parallel list for [DINO-WM](../entities/dino-wm.md) — for each component, **same as V-JEPA 2** or **different** or **same as LeWM**.
5. Verify against the table in the previous section. Anything you find that contradicts the table is either a mistake (mine — file an issue), or a place the wiki is hedging on a detail you should chase down in Module 12.

If you want a deeper version: implement a **toy 2D JEPA** — a small encoder (2-layer MLP) + a small predictor + a *deliberate experiment* trying to make it collapse with no anti-collapse mechanism, then turning each one on and observing the loss / variance trajectory. The point is to see in your own training run that an end-to-end JEPA without any anti-collapse mechanism *will* collapse — and then watch, e.g., variance regularization rescue it. This makes the entire collapse-prevention zoo feel concrete.

## Recommended reading

In order:

1. **[`concepts/jepa.md`](../concepts/jepa.md)** — concept page; re-read for the joint-embedding definition and the collapse framing.
2. **[V-JEPA 2 paper](../sources/v-jepa-2-paper.md)** — §1–3 (architecture + zero-shot Franka result). Skip the LLM-aligned VQA section unless you care about that.
3. **[V-JEPA 2 GitHub](../sources/vjepa2-github.md)** — variant family table; what's published as weights.
4. **[V-JEPA 2.1 paper](../sources/v-jepa-2-1-paper.md)** — what changed in 9 months.
5. **[DINO-WM paper](../sources/dino-wm-paper.md)** — frozen-feature variant; PushT result.
6. **[JEPA-WMs paper](../sources/jepa-wms-paper.md)** — first real-Franka demonstration; first JEPA paper to use [RoboCasa](../entities/robocasa.md).
7. **[VLA-JEPA paper](../sources/vla-jepa-paper.md)** — JEPA-as-auxiliary; the cross-over with [Module 9](robot-learning-curriculum.md).
8. **[LeWM paper](../sources/leworldmodel-paper.md)** — read the architecture and design-choices sections; do **not** yet read the SIGReg derivation (that's [Module 12](robot-learning-curriculum.md)).

Useful cross-cutting:

- **[Generative-video vs JEPA world models](generative-video-vs-jepa-world-models.md)** — re-read for the cross-paradigm framing; this module zooms inside the JEPA half of that synthesis.
- **[Why JEPA research skips the simulator stack](why-jepa-research-skips-the-simulator-stack.md)** — the simulator-fragmentation thesis; useful background on which JEPA papers use which benchmarks.
- **[JEPA task capabilities](jepa-task-capabilities.md)** — reference index of seven task categories JEPA models demonstrate.

## What you should now be able to do

- Read any JEPA-line paper's training section and identify which collapse-prevention mechanisms it uses, and how many anti-collapse hyperparameters they imply.
- Argue *for* and *against* the frozen-feature approach (DINO-WM-class) versus end-to-end JEPA (LeWM-class), and predict which will win on a given dataset based on whether the data is on-task or off-task.
- Sketch the V-JEPA 2-AC two-stage recipe (action-free pretrain → action-conditioned fine-tune) and explain why each stage's data-scale ratio (~16,000×) is consistent with the action-data scarcity story from Module 6.
- Position any new JEPA paper on the "scale + pretraining" axis (V-JEPA 2-end vs LeWM-end) and on the "anti-collapse-mechanism" axis (EMA / variance-cov / frozen / SIGReg).

## Hand-off to Module 12

Module 11 has set up the entire LeWM contribution **except for the math**. By the time you start Module 12, you should believe:

1. End-to-end JEPAs are hard to train without collapsing.
2. The pre-LeWM literature responded with a 4–6-hyperparameter zoo of mechanisms.
3. LeWM claims to do it with **one regularizer (SIGReg) and one hyperparameter**.
4. Module 12 is the math derivation of why SIGReg works, and the empirical evidence that it does.

[Module 12](curriculum-12-lewm-deep-dive.md) will derive **SIGReg from random unit-norm projections + the Epps–Pulley univariate normality test (justified by Cramér–Wold) + backprop through the test statistic**, then walk the LeWM paper section-by-section through the architecture, planning protocol, surprise evaluation, latent probing, and four-environment results table (PushT, Reacher, OGBench-Cube, Two-Room) including the comparison columns against PLDM, DINO-WM, Dreamer, and TD-MPC.

## Related curriculum modules

- **[Module 4 — SSL and embeddings](robot-learning-curriculum.md)** — the broader SSL framing; collapse as a general failure mode.
- **[Module 5 — Generative models](robot-learning-curriculum.md)** — JEPA's *opposite* paradigm in Module 10's family-1 (generative-video) sense.
- **[Module 9 — VLAs](robot-learning-curriculum.md)** — VLA-JEPA is the cross-over.
- **[Module 10 — World models, broad](curriculum-10-world-models.md)** — direct prerequisite; the four-family taxonomy this module zooms inside.
- **[Module 12 — LeWM deep-dive](robot-learning-curriculum.md)** — the SIGReg math + LeWM paper section-by-section.

## Mentioned in

- [Robot-learning curriculum](robot-learning-curriculum.md)
- [Index](../index.md)

## Open questions / TBD

- ~~**PLDM source page.**~~ Filed: [PLDM Paper](../sources/pldm-paper.md) + [PLDM entity](../entities/pldm.md) (2026-05-10). LeWM-vs-PLDM comparison now backed by the primary source.
- **A worked toy-JEPA implementation page.** The anchor exercise's "implement a 2D JEPA and watch it collapse" extension would benefit from a sample notebook in the wiki.
- **DINOv2 paper** as a source page — the canonical pretrained encoder behind the entire frozen-feature family deserves its own primary-source ingest. ([DINOv2 entity](../entities/dinov2.md) exists.)
- **V-JEPA 1 source page** — useful for the progression history; lower priority since V-JEPA 2 superseded it as the canonical reference.
- **LeCun's "A Path Towards Autonomous Machine Intelligence" (2022)** — the original JEPA position paper; would anchor the LeCun stance behind the entire family.
- **Multiple-fix-soup quantitative comparison** — would be valuable to have a table comparing pre-LeWM end-to-end JEPAs on a single benchmark to make the "4–6 hyperparameters" claim concrete with numbers.
