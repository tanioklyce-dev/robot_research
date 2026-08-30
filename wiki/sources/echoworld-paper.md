---
title: "EchoWorld: Learning Motion-Aware World Models for Echocardiography Probe Guidance (Yue, Wang, Jiang, Liu, Song, Huang, CVPR 2025)"
type: source
url: https://arxiv.org/abs/2504.13065
local_path: raw/2504.13065v1.pdf
sha256: b9880dddc26c9d294f11c5f991e590ec5fa4453123f71078d7208d6143d64b29
author: Yang Yue*, Yulin Wang*, Haojun Jiang, Pan Liu, Shiji Song, Gao Huang
affiliation: Tsinghua University (LeapLab); PLA General Hospital
venue: "CVPR 2025; arXiv 2504.13065"
published: 2025-04-17
ingested: 2026-08-30
tags: [jepa, action-conditioned, world-model, imitation-learning, probe-guidance, medical-robotics, 6-dof, motion-aware-attention, decision-transformer, tsinghua, cvpr-2025, open-source]
---

> [!note] Ingest depth
> Read from the **full PDF** (`raw/2504.13065v1.pdf`, 15 pages). Sections 1–6 read in full (task formulation, both world-modeling objectives, motion-aware attention, both evaluation protocols, results, ablations); appendix skimmed. Table 1 and the ablation tables re-extracted in layout mode. Code at [github.com/LeapLabTHU/EchoWorld](https://github.com/LeapLabTHU/EchoWorld).
>
> Surfaced via [EchoJEPA](echojepa-paper.md)'s related work. **This is a robot-learning paper in medical clothing** and belongs in this wiki on its own terms.

## Summary

**EchoWorld** — Yue, Wang, Jiang, Liu, Song & Huang (Tsinghua LeapLab + PLA General Hospital; CVPR 2025). An **action-conditioned [JEPA](../concepts/world-models/jepa.md)** trained on **teleoperated expert demonstrations**, used to guide an ultrasound probe to ten standard cardiac imaging planes.

Strip the medical framing and the setup is one this wiki knows well:

- **Demonstrations** collected by "professional sonographers manoeuvring an ultrasound probe **mounted on a robotic arm**," with image frames and **6-DOF probe pose** recorded synchronously — teleoperated robot demos with proprioception.
- **Policy**: given the history `{(I_t, p_t)}`, predict the **relative rigid-body movement** `a_t = p* · p_t⁻¹` that reaches a target plane. Behaviour cloning with an `L1` action loss.
- **Pretraining**: a JEPA over the same data, with an action-conditioned objective.

The authors say it outright: *"imitation learning — the approach adopted in our study — directly learns from expert demonstrations, presenting a scalable approach in line with advances in general-purpose robotic control."*

**Why it matters here.** Three things, and the second is the one worth arguing about:

1. **It is an action-conditioned JEPA published at CVPR 2025**, built explicitly on [LeCun's AMI paper](lecun2022-path-towards-ami.md) and I-JEPA — an independent instance of the [V-JEPA 2-AC](../entities/v-jepa-2.md) idea, in a real robotic domain, with code.
2. **It beats Decision Transformer by replacing interleaved image-action sequences with pose-conditioned attention** — a direct architectural argument against the token-interleaving convention that most [VLAs](../concepts/learning/vla-models.md) in this wiki use.
3. **Its evaluation is entirely open-loop**, which is a large caveat and an instructive one.

## The two world-modeling objectives (§4.1)

Both are JEPA: context encoder `f_θ`, EMA target encoder `f'_θ'`, predictor `g_φ`, prediction in feature space, EMA to prevent collapse.

**Spatial world modeling** — mask contiguous rectangular blocks of patches, encode only visible patches, predict the masked regions' *features*. `L1` loss over masked locations only. This is I-JEPA applied to ultrasound.

**Motion world modeling** — the interesting half. Given two frames `I_a, I_b` from the same scan and their **relative 6-DOF probe movement** `p_{a→b}`, encode the movement with a motion encoder `A_ψ` into `z_{a→b}`, and predict the average-pooled target features:

```
ĥ_y = g_φ( f_θ(I_a);  m + z_{a→b} )        h_y = AvgPool( f'_θ'(I_b) )
```

Trained with **InfoNCE** rather than a regression loss. Total: `L = L_spatial + 0.1 · L_motion`.

> [!note] The action is the latent variable — this is the JEPA formulation done properly
> In [LeCun's framing](lecun2022-path-towards-ami.md) a JEPA predicts target `y` from context `x` conditioned on a latent `z` capturing what the context does not determine. Here **`z` is literally the action**: the probe movement that produced the visual change. The paper states it in exactly those terms.
>
> That makes EchoWorld a clean instance of the thing the wiki's [world-model](../concepts/world-models/world-model.md) thread cares most about — *predict the consequence of an action in representation space* — in a domain with real actuators, real 6-DOF pose, and released code. [V-JEPA 2-AC](../entities/v-jepa-2.md) is the closer-to-home comparison and this is contemporaneous with it.

**Reading out the world model.** Because a JEPA has no decoder, they train one post-hoc — an **RCDM** diffusion model mapping predicted features back to pixels — purely to visualize. It recovers masked anatomy and, more interestingly, **simulates the visual result of a probe movement**. The authors note that so augmented, "it can potentially function as a simulator for free-hand cardiac ultrasound scanning."

## Motion-aware attention (§4.2) — the architectural claim

The standard formulation, and the one nearly every sequence-model policy in this wiki uses, is an **interleaved image-action token sequence** `{I_1, a_1, I_2, a_2, …}` consumed by a causal transformer — [Decision Transformer](https://arxiv.org/abs/2106.01345)'s design, inherited by most [VLAs](../concepts/learning/vla-models.md).

EchoWorld argues this is suboptimal and "fails to fully utilize the rich motion data available." Instead it injects **pairwise relative pose** directly into attention:

```
K_j^(i) = MLP( h_j , z_{i→j} )        V_j^(i) = MLP( h_j , z_{i→j} )
```

Every query token `i` sees a **different key/value pair for each `j`**, encoding the 3-D rigid transformation between those two frames. It is a relative positional encoding where the "position" is a full 6-DOF pose difference rather than a sequence index.

> [!note] Why this generalizes past ultrasound
> A camera on a moving arm has a pose. So does a wrist camera on a manipulator. The claim — *when you know the rigid transformation between two observations, put it in the attention rather than in the token stream* — is a general one about embodied sequence models, and this paper is the only source in the wiki that tests it head-to-head against the interleaving convention.
>
> The cost is `O(N²)` MLP evaluations for key/value construction rather than `O(N)`, which is fine at `N` ≈ 8 frames and would not be at `N` ≈ 1000 tokens.

## Data and setup (§3.2, §5)

- **356 routine clinical scans**, ~**1 million frames**, 30 fps, each frame paired with 6-DOF pose (x, y, z + yaw, pitch, roll) in an anatomical coordinate frame.
- **284 train / 72 test scans, no patient overlap.**
- **Ten standard planes** (PLAX, PSAX-AV/PV/MV/PAP/APEX, A4C, A5C, A3C, A2C).
- **ViT-Small** context/target encoders, 6-block transformer predictor, EMA target, batch 1024, **300 epochs on 4× A100**.

## Results (Table 1)

Mean absolute error; **Trans.** in millimetres, **Rot.** in degrees; "Avg" averages across the ten planes.

**Single-frame protocol** — one image, a two-layer MLP head, identical supervision for every backbone. This measures *representation quality*.

| Backbone | Avg |
|---|---|
| Scratch | 9.07 |
| DeiT | 8.63 |
| DINOv2 | 8.52 |
| BioMedCLIP | 8.74 |
| LVM-Med | 8.73 |
| US-MoCo | 8.71 |
| US-MAE | 8.46 |
| USFM | 8.42 |
| EchoCLIP | 8.37 |
| **EchoWorld** | **8.15** |

**Sequential protocol** — historical visual-motion data, **same visual backbone for every method**, so this isolates the guidance architecture.

| Framework | Avg |
|---|---|
| US-GuideNet | 7.72 |
| Decision Transformer | 7.44 |
| Sequence-aware | 7.42 |
| **EchoWorld** | **7.05** |

### Ablations

**World-modeling objectives** (single-frame): neither 8.62 (motion only) nor 8.38 (spatial only) matches both at **8.15**; no pretraining is 9.07. Spatial contributes more alone; they are complementary.

**Motion-awareness** (sequential), a clean 2×2:

| Backbone | Motion? | Avg |
|---|---|---|
| DeiT | ✗ | 8.62 |
| DeiT | ✓ | 7.53 |
| EchoWorld | ✗ | 7.98 |
| EchoWorld | ✓ | **7.05** |

> [!note] Motion information is worth more than the pretraining
> Adding motion buys **1.09** (DeiT) and **0.93** (EchoWorld). Swapping DeiT for the world-model backbone buys **0.64** (no motion) and **0.48** (with motion).
>
> So the headline contribution — the pretrained cardiac world model — is the **smaller** of the two effects, and the paper's own ablation says so. The larger effect is simply *giving the policy access to where the probe has been*. Worth holding next to any robot-policy result that reports a fancy pretraining objective without ablating proprioception.

> [!warning] The paper's in-domain-transfer claim is only half-supported by its own table
> §5.2 states that "ultrasound-specific pre-trained models, such as USFM, EchoCLIP, and US-MAE, generally outperform general-purpose models, emphasizing the importance of in-domain transfer."
>
> The three they name do. The other three do not: **DINOv2 (8.52) beats BioMedCLIP (8.74), LVM-Med (8.73) and US-MoCo (8.71)** — and so does plain **DeiT (8.63)**. Half the in-domain models lose to a general-domain backbone. The honest reading is that *good* in-domain pretraining beats general pretraining and *mediocre* in-domain pretraining does not, which is a weaker and more useful claim. Consistent with the wiki's [DINOv2](../entities/dinov2.md)-as-default-backbone thread.

## The evaluation caveat, which is the big one

> [!warning] Everything here is open-loop. Nothing is closed-loop, and no patient was ever guided.
> The authors are explicit about why: *"Evaluating different approaches in real-person experiments is both costly and time-consuming. To address this, we propose two evaluation protocols based on the collected scanning data."*
>
> Both protocols score **mean absolute error between the predicted movement vector and the expert's**, on recorded scans. Even the "sequential" protocol replays recorded histories — the model's predictions never affect what it observes next.
>
> So **7.05 does not mean the probe reaches the plane.** It means the policy's action prediction is off by ~7 (mm, degrees) on average against a recorded expert. Compounding error, recovery from off-distribution states, and whether the target view is actually acquired are all unmeasured. This is exactly the open-loop-BC-metric problem the wiki tracks under [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md), and it is the same class of gap as [LIBERO-PRO](libero-pro-paper.md)'s: a number that looks like performance and is not success.
>
> The honesty is real — they say why they did it — and the limitation is real too. **A closed-loop result on a phantom would be worth more than any of the offline deltas reported here.**

## Entities mentioned

- **[EchoWorld](../entities/echoworld.md)** — the model.
- **Gao Huang** (Tsinghua LeapLab, senior author; also DenseNet), Yang Yue, Yulin Wang, Haojun Jiang. No wiki pages.
- **PLA General Hospital** — clinical partner supplying the scans.
- **[Yann LeCun](../entities/yann-lecun.md)** — via the [AMI paper](lecun2022-path-towards-ami.md) and I-JEPA, the framework's stated basis.
- **[DINOv2](../entities/dinov2.md)**, DeiT, BioMedCLIP, LVM-Med, USFM, EchoCLIP — backbone baselines.
- **Decision Transformer** — the sequence-model baseline it beats.
- **[EchoJEPA](../entities/echojepa.md)** — the other echocardiography JEPA in this wiki; different task (diagnosis vs probe guidance), different group, contemporaneous.

## Concepts touched

- **[JEPA](../concepts/world-models/jepa.md)** — an action-conditioned instance with real actions.
- **[World models](../concepts/world-models/world-model.md)** — used as a pretext task for representation learning, and reads out as a scanning simulator.
- **[Imitation learning](../concepts/learning/imitation-learning.md)** — behaviour cloning from teleoperated demonstrations.
- **[Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md)** — the open-loop caveat.
- **[VLA models](../concepts/learning/vla-models.md)** — the interleaved-token convention it argues against.

## Open questions / TBD

- **Does motion-aware attention beat token interleaving on a standard robot benchmark?** The claim is general and the test here is one domain with `N` ≈ 8 frames. Running it against a [Decision-Transformer](../concepts/learning/vla-models.md)-style baseline on LIBERO or DROID would be a genuinely useful replication, and the code is released.
- **Closed-loop performance is unknown**, and is the number that matters.
- **The proprioception ablation deserves wider use.** "How much of my policy's performance is the fancy visual pretraining, and how much is just knowing where the arm has been?" is cheap to run and rarely reported.
- **Two independent echocardiography JEPAs** ([this](../entities/echoworld.md) and [EchoJEPA](../entities/echojepa.md)) now exist with no cross-comparison — different tasks, no shared benchmark, no shared checkpoint.
