---
title: JEPA task capabilities
type: synthesis
created: 2026-05-08
updated: 2026-09-07
tags: [jepa, world-model, capabilities, manipulation, navigation, planning, hierarchical-planning, cross-embodiment, test-time-adaptation, video-understanding, time-series, medical, finance, taxonomy]
---

# JEPA task capabilities

What can a [JEPA](../../concepts/world-models/jepa.md)-style world model actually *do*? This page is a reference index — it answers "is there a JEPA paper that does X?" by pointing at the source. It does not argue that JEPA is the right approach for X; the decision-grade pages for that are [what world models are measurably good for](what-world-models-are-measurably-good-for.md), [the abstraction tax](abstraction-tax.md), and [JEPA for a household mobile manipulator](jepa-for-household-mobile-manipulator.md).

> [!note] Rebuilt 2026-09-07 — from seven papers to twenty-eight
> The May-2026 version indexed seven papers and seven categories. Since then the wiki has ingested the hierarchical planners ([HWM](../../entities/hwm.md), [WorldDP](../../entities/worlddp.md)), the cross-embodiment planner ([Demo-JEPA](../../sources/demo-jepa-paper.md)), the test-time adapter ([AdaJEPA](../../entities/adajepa.md)), three alternative-regularizer world models ([LpWM](../../entities/lpwm.md), [SMWM](../../entities/smwm.md), [PLDM](../../entities/pldm.md)), the SIGReg line on video and time series ([LeVJEPA](../../entities/levjepa.md), [LeNEPA](../../entities/lenepa.md)), two clinical JEPAs ([EchoJEPA](../../entities/echojepa.md), [EchoWorld](../../entities/echoworld.md)), a finance encoder ([Market-JEPA](../../entities/market-jepa.md)), the vision-language reframing ([VL-JEPA](../../entities/vl-jepa.md)), three shared-instrument probe studies, two theory papers, and the brittleness benchmark ([stable-worldmodel](../../sources/stable-worldmodel-paper.md)). Three things the May page listed under *"don't yet do"* are now demonstrated, with caveats, and are marked below. The categories are precise to ingested evidence, not a universal claim about the JEPA literature — [awesome-jepa](../../sources/awesome-jepa-github.md) indexes 248 papers, of which the wiki holds about thirty.

## 1. Real-robot manipulation

- **Zero-shot pick-and-place via image-goal MPC** — V-JEPA 2-AC on Franka arms in **two new labs** with no robot-specific data, training, or rewards ([V-JEPA 2](../../sources/v-jepa-2-paper.md)). Still the strongest evidence in either world-model paradigm that observation pretraining can substitute for interaction data.
- **Real-Franka grasping** — V-JEPA 2.1 reports **+20 pt** over V-JEPA 2-AC ([V-JEPA 2.1](../../sources/v-jepa-2-1-paper.md); secondary-sourced, unverified against the paper body — this caveat has stood since May).
- **Real Franka from the same recipe that beats V-JEPA 2-AC in sim** — [JEPA-WMs](../../sources/jepa-wms-paper.md): DROID **48.2 vs 42.9**, RoboCasa-Real 25.4 vs 16.2, plus a real-Franka unroll.
- **Multi-stage real-robot manipulation from one goal image** — [HWM](../../sources/hwm-paper.md) wraps V-JEPA 2-AC in a two-level planner: Franka pick-and-place **0% → 70%**, drawer **30% → 70%**, with no oracle subgoals. *New since May: this was the "long-horizon" gap.*
- **Cross-embodiment imitation on a real robot** — [Demo-JEPA](../../sources/demo-jepa-paper.md) translates a UR5e demonstration into Franka latent goals and plans to them under V-JEPA 2.1 dynamics: **0.25 vs 0.15** real zero-shot against trajectory learning, while *losing* in-domain 0.43 vs 0.65.
- **JEPA-augmented VLA on real hardware** — [VLA-JEPA](../../sources/vla-jepa-paper.md) evaluates on LIBERO, LIBERO-Plus, SimplerEnv and unnamed real-world manipulation, with JEPA as an auxiliary objective inside the policy.
- **Robotic ultrasound probe guidance** — [EchoWorld](../../sources/echoworld-paper.md) (CVPR 2025) is an action-conditioned JEPA over 6-DOF probe pose, trained on teleoperated demonstrations from a probe on a robot arm; beats Decision Transformer 7.44 → 7.05 by conditioning attention on relative pose instead of interleaving image and action tokens. **Evaluation is entirely open-loop.**

## 2. Robot navigation

- **2D maze / point-mass / wall** — [JEPA-WMs](../../sources/jepa-wms-paper.md) (PointMaze, Wall); [LeWM](../../sources/leworldmodel-paper.md) (Two-Room, Reacher); [DINO-WM](../../sources/dino-wm-paper.md) (Wall, PointMaze); [PLDM](../../sources/pldm-paper.md) (Diverse Maze).
- **Zero-shot on unseen maze layouts** — HWM over PLDM: D∈[13,16] **44% → 83%** ([HWM](../../sources/hwm-paper.md)).
- **Regime-switching navigation** — [LpWM](../../sources/lpwm-paper.md) on Piecewise (force-field zones with no visual cue): **84.7% vs 65.3%** for LeWM, with the sparse code's support decoding the zone at 94–99%.
- **Distractor-robust navigation** — [SMWM](../../sources/sensorimotor-world-models-paper.md) matches SIGReg on Two-Room (99 vs 94) while ignoring a randomly moving uncontrolled object by construction.
- **Independent reproduction** — LeWM on Two-Room reaches **92%** (paper: 97%) after four epochs on an RTX 3060 ([reproduction video](../../sources/onchain-ai-garage-lewm-reproduction.md)); the first non-author LeWM result on record.
- **Real-robot navigation** — V-JEPA 2.1 reports it; platform unnamed in the abstract ([V-JEPA 2.1](../../sources/v-jepa-2-1-paper.md)). Also [Genie Envisioner](../../entities/genie-envisioner.md)-class claims belong to the pixel camp, not here.

## 3. Planning — the world model as cost function

JEPA models are used **not as policies but as transition functions for a planner**, which optimizes action sequences against the learned latent dynamics. The planning toolkit has grown considerably since May.

- **Image-goal MPC with CEM** — the default that wins across the family: V-JEPA 2-AC, DINO-WM (zero-shot, "without expert demonstrations, reward modeling, or pre-learned inverse models"), LeWM (**up to 48× faster** than foundation-model world models). [JEPA-WMs](../../sources/jepa-wms-paper.md)' systematic ablation: **CEM with L₂ embedding distance** is the overall winner; gradient-based planners work only on smooth-cost environments and fail on 2D navigation and contact-rich manipulation.
- **Two-level hierarchical MPC** — [HWM](../../entities/hwm.md): a high-level model over latent macro-actions proposes subgoals, a low-level model reaches them. Push-T at the hardest horizon **17% → 61%**, with 3–4× less test-time planning compute. Model-agnostic across DINO-WM, PLDM, V-JEPA 2-AC.
- **World model over a diffusion policy** — [WorldDP](../../entities/worlddp.md): an object-centric JEPA proposes subgoals scored by object-embedding MSE plus a **contact-prediction cost**, optimized by a **particle filter** (multi-modal, unlike CEM), and a goal-conditioned [Diffusion Policy](../../entities/diffusion-policy.md) executes them. Three-cube rearrangement **30%**, more than double the next best; DINO-WM and LeWM score 0.
- **Test-time adaptation inside the MPC loop** — [AdaJEPA](../../sources/adajepa-paper.md): one gradient step per replan on the pretraining loss, using the observed transition as a free label. Nearly doubles planning success on unseen shapes; no harm in-distribution; success keeps rising over MPC steps where a frozen model saturates. *New since May: the first online answer to OOD collapse.*
- **Latent geometry that lowers planner requirements** — [LpWM](../../sources/lpwm-paper.md)'s sparse codes give **+24–57%** on PushT at intermediate predictor capacity and nothing at high capacity: sparsity lowers the capacity needed to plan, not the ceiling. [Temporal straightening](../../sources/temporal-straightening-paper.md) shows the prediction objective alone straightens latent trajectories, which is the condition under which LeWM's Euclidean plan-scoring is valid at all.
- **Transcription as planning** — [Music-JEPA](../../sources/music-jepa-paper.md) recovers a piano roll by searching for the action sequence that best explains a target sound: inverse dynamics run as search, with an exact ground-truth answer to score against.

## 4. Long-horizon and multi-stage manipulation

*Moved out of "don't yet do."* Two hierarchical systems now exist, both from LeCun-affiliated groups, with opposite low-level choices: [HWM](../../entities/hwm.md) puts a second world model below the subgoal planner; [WorldDP](../../entities/worlddp.md) puts a diffusion policy there and argues it is faster, more tolerant of imperfect subgoals, and sustains longer sequences. Both are **two levels deep and goal-image conditioned**, not the N-level emergent hierarchy of the [2022 position paper](../../sources/lecun2022-path-towards-ami.md). WorldDP's composite task (button-press prerequisite, then manipulate) reaches **20%**; nothing in the family demonstrates a 10-step task with recovery.

## 5. Cross-embodiment transfer

*New category.* [Demo-JEPA](../../sources/demo-jepa-paper.md) treats a demonstration from another robot as a statement of *what state to reach*, translates it through a cross-attention "Dreamer Predictor" into target-robot latents, and plans there. Sawyer → Franka in sim, UR5e → Franka real. The controlled finding inside it: planning directly toward the source robot's own V-JEPA 2.1 future latent **fails across all tasks** — the latent still encodes which robot you are, and an explicit translator is required ([abstraction tax](abstraction-tax.md)).

## 6. Video understanding (encoder downstream)

- **V-JEPA 2 encoder, frozen**: 77.3 top-1 SSv2 motion classification; 39.7 R@5 Epic-Kitchens-100 action anticipation (SOTA at release); 84.0 PerceptionTest / 76.9 TempCompass at 8B LLM-aligned scale ([V-JEPA 2](../../sources/v-jepa-2-paper.md)).
- **Same accuracy at 5.6–20.8× less compute** — [LeVJEPA](../../sources/levjepa-paper.md) trains a video encoder under SIGReg with no EMA, stop-gradient, or predictor; ViT-L consumes less than half the compute of V-JEPA 2's ViT-S. FLOP-matched it wins ImageNet **+7.6** and K400 **+3.9** over the strongest baseline and **loses SSv2 by 3.2** — appearance up, motion taxed, in one table. A **block-causal encoder costs nothing** (51.2 vs 50.7), so temporal ordering becomes a property of the encoder itself.
- **Robustness profile** — across four matched-capacity ViT-Ls, latent-prediction models lead on five of six corruption types, uniquely encode the **arrow of time** (reversal flips pushing ↔ pulling), and detect *pretend* actions best where the cue is the absence of contact ([latent video prediction](../../sources/latent-video-prediction-better-world-models-paper.md)). Measured on SSv2 classification, not control.
- **Ordered, salient target prediction** — DSeq-JEPA replaces I-JEPA's random independent target blocks with a saliency-ordered sequence; neither component works alone and random or inverse order actively hurts ([Day 2 lightning talk](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md)).

## 7. Dense vision tasks

V-JEPA 2.1's "dense features" framing: depth estimation and segmentation forecasting on Ego4D, EPIC-KITCHENS, SSv2, NYUv2, TartanDrive ([V-JEPA 2.1](../../sources/v-jepa-2-1-paper.md)). Unchanged since May.

## 8. Video prediction

Segmentation and depth forecasting as video-prediction benchmarks ([DINO-world](../../sources/dino-world-paper.md)). Next-frame representation prediction remains the substrate every other category sits on.

## 9. Representation substrate inside policies and other world models

*New category — the role the field is actually converging on.*

- **Auxiliary loss inside a VLA** — [VLA-JEPA](../../entities/vla-jepa.md) (USTC) and, independently, [FLARE](../../concepts/world-models/flare.md) (NVIDIA GEAR): future-latent alignment to an EMA teacher at λ=0.2, adopted in [GR00T N1.5](../../sources/groot-n1_5.md). Because the target needs no action labels, action-less human video can train it; human-video co-training roughly doubles novel-object success in the [FLARE paper](../../sources/flare-paper.md).
- **Latent space for a diffusion world model** — with the DiT backbone, data, and schedule fixed and only the frozen encoder varied, V-JEPA 2.1 latents roughly **double** VLA-in-the-loop policy-evaluation success against a VAE latent space (**0.362 vs 0.169**), with the widest OOD margin under distractors (0.575 vs 0.287) ([Reconstruction or Semantics?](../../sources/latent-space-robotic-world-models-paper.md)). This is a JEPA representation in the [WorldArena](what-world-models-are-measurably-good-for.md) *policy-evaluator* role; the *planner*, *data-engine*, and *RL-environment* roles remain untested for the family.
- **Action recoverability** — a frozen inverse-dynamics probe puts eight encoder families on one axis: V-JEPA 2 +ID reaches **0.85 R²** against VideoMAE +ID at 0.75 and image-SSL at 0.16–0.17; the advantage concentrates on **rotation**, and peaks at **layer 14 of 22**, so final-layer features are near the trunk's worst point for action decoding ([action-relevant latents](../../sources/action-relevant-latents-paper.md)).
- **Frozen backbone for a world model** — the reverse finding: as the *frozen encoder* under a JEPA-WM, **DINO beats V-JEPA** because fine object segmentation turns object motion into sparse localized token changes ([JEPA-WMs](../../sources/jepa-wms-paper.md)). Which encoder wins depends on which job it is given; see the contradiction on the [JEPA page](../../concepts/world-models/jepa.md).

## 10. Vision-language

*New category.* [VL-JEPA](../../entities/vl-jepa.md) (Meta / LeCun) reframes the entire VLM: predict the **embedding of the answer text** rather than generating tokens. A **1.6B** model beats 7B models on GQA; 50% fewer trainable parameters and 2.85× fewer decoding operations. Not generative by default — inference is by nearest-candidate embedding or a trained text decoder. **Distinct from VLA-JEPA despite the name.**

## 11. Non-visual modalities

*New category, and the one that most changes the picture of what the family is for.*

| Domain | Model | Result |
|---|---|---|
| Echocardiography video | [EchoJEPA](../../sources/echojepa-paper.md) — V-JEPA 2 adapted, 18M videos / 300K patients | **78.6% with 1% of labels** vs 42.1% for the best baseline at 100%; degrades **2.3%** under acoustic perturbation vs 16.8% next best |
| Time series (ECG, UCR-128) | [LeNEPA](../../sources/lenepa-paper.md) — SIGReg, no augmentation, causal backbone | Fixed recipe survives reuse across signal families; UCR-128 within 0.24 pt of MOMENT |
| Equity microstructure | [Market-JEPA](../../entities/market-jepa.md) — 22.3M-param LeJEPA encoder, MIT licence | Wins the *economic-organization* half of the [MarketOne](../../entities/marketone.md) 18-method bake-off, loses pure forecasting |
| Piano audio | [Music-JEPA](../../sources/music-jepa-paper.md) — audio as state, piano roll as action | Beat tracking, composer ID, key estimation; transcription as planning |
| Graphs | [HP-JEPA](../../sources/hp-jepa-paper.md) — coarse-to-fine partition bank | Multi-resolution graph representation |

[awesome-jepa](../../sources/awesome-jepa-github.md) adds EEG, hydrology, wireless channel state, PDE control, trajectory similarity, and radio astronomy. Two independent signals — that index, and [Balestriero's own listed domains](../../sources/randall-balestriero-personal-site.md) — say **the JEPA programme's centre of gravity is not robot control.** This wiki reads the line through robotics; the field does not.

## 12. Probing, interpretability, and theory

- **Physical structure in the latent** — LeWM latent probes surface interpretable physical structure; **surprise scores** detect physically implausible events ([LeWM](../../sources/leworldmodel-paper.md)).
- **Controllable structure recovered** — [SMWM](../../sources/sensorimotor-world-models-paper.md) recovers intrinsic dimension = controllable action dimension and represents actions as **latent translations** `g_a(z) ≈ z + ρ(a)`, an emergent homomorphism not enforced by any loss; beats SIGReg on 3D OGBench-Cube **84 vs 59**.
- **Mode-factored codes** — [LpWM](../../entities/lpwm.md)'s sparse support encodes the discrete dynamics regime (94–99% decodable), magnitude the within-regime state. Caveat: on contact-rich Cube the support is a motion detector (r≈0.87 with effector motion, 0.05 with contact) until a temporal prior is added.
- **Identifiability** — [When Does LeJEPA Learn a World Model?](../../sources/when-does-lejepa-learn-a-world-model-paper.md) proves **linear identifiability** under SIGReg and that the Gaussian target is uniquely the one for which it holds. Encoder only; population-level; dynamics unproved ([identifiability](../../concepts/world-models/identifiability.md)).
- **Generalization bound** — [Peking University theory](../../sources/jepa-generalization-theory-paper.md): JEPA pretraining as conditional spectral graph learning, connecting pretraining error to downstream planning regret with a latent-dimension trade-off.
- **A diagnostic failure** — [Sobal et al. 2022](../../sources/sobal2022-jepa-slow-features-paper.md): JEPA encodes the *slowest* feature, so with **fixed** distractor noise it latches onto the noise. The paper that motivates every anti-collapse mechanism since ([lineage](ssl-anti-collapse-lineage.md)).
- **Instruction leakage** — a goal-conditioned JEPA-plus-anchors model scores 0.90 on relation readout by *transcribing the instruction*, not perceiving the scene; fix by keeping the goal out of the dynamics ([compact spatial-relations WM](../../sources/grounding-spatial-relations-compact-wm-paper.md), [instruction leakage](../../concepts/world-models/instruction-leakage.md)).

## 13. Robustness and adaptation under shift

*New category, because the family's most consequential 2026 result is a negative one.*

- **Collapse under nuisance shift** — [stable-worldmodel](../../sources/stable-worldmodel-paper.md): LeWM **50.8% → 6–26%** on Push-T under colour, size, and shape change; distractor collapse quadratic across all baselines; prediction MSE correlates poorly with planning success.
- **Mechanism** — a next-frame objective is *paid* to encode static attributes, and no JEPA world-model recipe in the wiki declares a **static** input axis irrelevant ([abstraction tax](abstraction-tax.md); LeWM verified to use **no augmentation at all**). The one declaration that does exist is [SMWM](../../entities/smwm.md)'s inverse-dynamics term, which declares *uncontrollable* variation irrelevant and filters a moving distractor — but it has not been run on stable-worldmodel's shift suite, and its forward loss still rewards encoding a constant colour.
- **Partial recovery online** — [AdaJEPA](../../entities/adajepa.md) recovers most of the shape-shift loss and gains under blur, noise, lighting; **modest under recolouring**, because the identity signal itself is destroyed and adaptation cannot repair what is absent.
- **Where the thesis wins cleanly** — EchoJEPA's 2.3% vs 16.8% degradation, on a modality where the discarded pixels are *physically* meaningless speckle rather than arguably so.
- **The controlled test** — [the declared-axis experiment](declared-axis-experiment.md), designed 2026-09-07, not yet run.

## Cross-cutting structural notes

- **JEPA models are cost functions, not policies — still, with two exceptions.** No JEPA world model here exposes `policy.act(obs)`; actions come from a planner that queries the model. The exceptions are the auxiliary uses ([VLA-JEPA](../../entities/vla-jepa.md), [FLARE](../../concepts/world-models/flare.md)), where the JEPA objective shapes a policy that does emit actions — and that is where industrial adoption ([GR00T N1.5](../../sources/groot-n1_5.md)) actually landed.
- **The planner is now a design axis of its own.** CEM, MPPI, particle filter, gradient descent, hierarchical CEM, and test-time-adapted CEM all appear; [JEPA-WMs](../../sources/jepa-wms-paper.md) and [stable-worldmodel's repo](../../sources/stable-worldmodel-github.md) (seven solvers) are the systematic comparisons.
- **Anti-collapse mechanism and latent geometry are separate axes.** The ladder runs frozen encoder → EMA → VICReg → SIGReg → inverse dynamics ([JEPA](../../concepts/world-models/jepa.md)); LpWM then asks *which shape* rather than *how to avoid collapse*. [The lineage synthesis](ssl-anti-collapse-lineage.md) has the pre-2024 history.
- **JEPA models do not generate pixels.** That remains the [generative-video paradigm](generative-video-vs-jepa-world-models.md); the two literatures used incommensurable instruments until the 2026 probe studies ([evaluation](../../concepts/world-models/world-model-evaluation.md)).
- **Sim weight class still varies by paper** — [companion synthesis](why-jepa-research-skips-the-simulator-stack.md). Task and sim setup remain independent design axes.
- **Real-robot evaluation remains the robotics gold standard here** — V-JEPA 2, V-JEPA 2.1, JEPA-WMs, HWM, Demo-JEPA, VLA-JEPA, EchoWorld all report it. Rollout counts are small (HWM and Demo-JEPA at 20–50 per cell); see [robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md).

## Mapping: which model does which task

| Model | Real manip. | Nav. | Planning | Long-horizon | Cross-embod. | Video / dense | Inside a policy or WM | Non-visual | Probing / theory | Robustness |
|---|---|---|---|---|---|---|---|---|---|---|
| [V-JEPA 2 / -AC](../../entities/v-jepa-2.md) | ✓ Franka zero-shot | — | ✓ image-goal MPC | — | — | ✓ SSv2, EK-100, VQA | ✓ encoder in probes | — | — | ✓ arrow of time |
| [V-JEPA 2.1](../../sources/v-jepa-2-1-paper.md) | ✓ +20 pt grasp (unverified) | ✓ real (unnamed) | ✓ | — | (via Demo-JEPA) | ✓ dense: depth, seg | ✓ best latent for policy eval | — | — | ✓ 46.1% under dropout |
| [LeWorldModel](../../entities/leworldmodel.md) | — | ✓ 2D | ✓ 48× faster CEM | — | — | — | — | — | ✓ latent + surprise | ✗ 50.8 → 6–26% |
| [DINO-WM](../../entities/dino-wm.md) | — | ✓ 2D | ✓ zero-shot | (via HWM) | — | — | — | — | — | — |
| [DINO-world](../../entities/dino-world.md) | — | — | — | — | — | ✓ seg + depth forecasting | — | — | — | — |
| [JEPA-WMs](../../entities/jepa-wms.md) | ✓ Franka, DROID | ✓ PointMaze, Wall | ✓ systematic ablation | — | — | — | — | — | — | — |
| [PLDM](../../entities/pldm.md) | — | ✓ Diverse Maze | ✓ MPPI | (via HWM) | — | — | — | — | ✓ 23-dataset stress test | — |
| [HWM](../../entities/hwm.md) | ✓ Franka 0 → 70% | ✓ maze +39 | ✓ two-level CEM | ✓ | — | — | — | — | — | — |
| [WorldDP](../../entities/worlddp.md) | — (sim UR5e) | — | ✓ particle filter + contact cost | ✓ 3-cube 30% | — | — | ✓ WM over diffusion policy | — | — | — |
| [Demo-JEPA](../../sources/demo-jepa-paper.md) | ✓ UR5e → Franka | — | ✓ CEM to translated goal | — | ✓ | — | — | — | — | — |
| [AdaJEPA](../../entities/adajepa.md) | — | ✓ layout shifts | ✓ adapted MPC | — | — | — | — | — | — | ✓ recovers shape shift |
| [LpWM](../../entities/lpwm.md) | — | ✓ Piecewise 84.7% | ✓ sparse codes | — | — | — | — | — | ✓ mode-factored | — |
| [SMWM](../../entities/smwm.md) | — | ✓ Two-Room | ✓ Cube 84 vs 59 | — | — | — | — | — | ✓ actions as translations | ✓ filters distractors |
| [VLA-JEPA](../../entities/vla-jepa.md) | ✓ real (unnamed) | — | — | — | — | — | ✓ auxiliary in VLA | — | — | — |
| [FLARE](../../concepts/world-models/flare.md) | ✓ via GR00T N1.5 | — | — | — | — | — | ✓ auxiliary in VLA | — | — | — |
| [VL-JEPA](../../entities/vl-jepa.md) | — | — | — | — | — | ✓ video classif./retrieval | — | — | — | — |
| [LeVJEPA](../../entities/levjepa.md) | — | — | — | — | — | ✓ 5.6–20.8× cheaper; causal | — | — | — | — |
| [EchoWorld](../../entities/echoworld.md) | ✓ probe guidance (open-loop) | — | — | — | — | — | — | ✓ ultrasound | — | — |
| [EchoJEPA](../../entities/echojepa.md) | — | — | — | — | — | — | — | ✓ ultrasound | — | ✓ 2.3% vs 16.8% |
| [LeNEPA](../../entities/lenepa.md) | — | — | — | — | — | — | — | ✓ time series | — | — |
| [Market-JEPA](../../entities/market-jepa.md) | — | — | — | — | — | — | — | ✓ finance | ✓ factor structure | — |
| [Music-JEPA](../../sources/music-jepa-paper.md) | — | — | ✓ transcription as planning | — | — | — | — | ✓ audio | — | — |

## What JEPA models *don't yet* do (in this wiki)

- **Language-conditioned action emission.** VLA-JEPA and FLARE bolt JEPA onto a VLA, but the VLA does the language. VL-JEPA does language without actions. No JEPA-native language-conditioned policy or planner — and the one language-goal *world model* here turns out to be [leaking the instruction](../../concepts/world-models/instruction-leakage.md).
- **Force, compliance, or tactile.** Every JEPA here predicts in a visual (or audio, ECG, price) latent. Nothing models contact force. The [world-action model](../../concepts/world-models/world-action-model.md) camp has a tactile instance ([VTAM](../../entities/vtam.md)); the JEPA camp does not.
- **Robustness to undeclared nuisance shift.** See §13. No JEPA world-model recipe declares object identity, lighting, or layout irrelevant, and the one measured under those shifts collapses.
- **Hierarchy beyond two levels, or with language subgoals.** §4 is a partial close, not a full one.
- **Multi-robot / multi-agent control.** Nothing.
- **Open-world humanoid whole-body control.** Occupied by [GR00T](../../entities/nvidia-groot.md) and similar VLAs; the JEPA contribution there is FLARE's auxiliary loss, not control.
- **Real-home deployment.** Every real-robot result above is a lab Franka or UR5e. No JEPA system has been run in a home.

## Open questions / TBD

- **V-JEPA 2.1's +20 pt grasping number** is still secondary-sourced. Four months on, this is the longest-standing unverified number on the page.
- **Which encoder wins depends on the job** — DINO over V-JEPA as a frozen JEPA-WM backbone; V-JEPA over Web-DINO as an action-decoding substrate; roughly tied as a diffusion-WM latent. The [JEPA page](../../concepts/world-models/jepa.md) carries the unresolved contradiction.
- **The JEPA family has never been run through the WorldArena planner, data-engine, or RL-environment roles.** Only the policy-evaluator role has a JEPA data point.
- **LeWM at real-robot resolution** — still open per the paper; the only real-robot LeWM-family result is via HWM on V-JEPA 2-AC, not LeWM.
- **Does declaring an axis buy robustness along it?** [The declared-axis experiment](declared-axis-experiment.md) is designed and unrun.
- ~~DROID and Metaworld papers not yet source pages~~ — both filed 2026-05-16.
- ~~Long-horizon hierarchical JEPA planning not yet demonstrated~~ — [HWM](../../entities/hwm.md) and [WorldDP](../../entities/worlddp.md), 2026.

## Sources used in this synthesis

Robotics world models: [V-JEPA 2](../../sources/v-jepa-2-paper.md) · [V-JEPA 2.1](../../sources/v-jepa-2-1-paper.md) · [LeWorldModel](../../sources/leworldmodel-paper.md) · [DINO-WM](../../sources/dino-wm-paper.md) · [DINO-world](../../sources/dino-world-paper.md) · [JEPA-WMs](../../sources/jepa-wms-paper.md) · [PLDM](../../sources/pldm-paper.md) · [Sobal 2022](../../sources/sobal2022-jepa-slow-features-paper.md) · [HWM](../../sources/hwm-paper.md) · [WorldDP](../../sources/worlddp-paper.md) · [Demo-JEPA](../../sources/demo-jepa-paper.md) · [AdaJEPA](../../sources/adajepa-paper.md) · [LpWM](../../sources/lpwm-paper.md) · [SMWM](../../sources/sensorimotor-world-models-paper.md) · [stable-worldmodel paper](../../sources/stable-worldmodel-paper.md) and [repo](../../sources/stable-worldmodel-github.md) · [LeWM reproduction](../../sources/onchain-ai-garage-lewm-reproduction.md)

Inside policies and probes: [VLA-JEPA](../../sources/vla-jepa-paper.md) · [FLARE](../../sources/flare-paper.md) · [GR00T N1.5](../../sources/groot-n1_5.md) · [action-relevant latents](../../sources/action-relevant-latents-paper.md) · [latent video prediction](../../sources/latent-video-prediction-better-world-models-paper.md) · [Reconstruction or Semantics?](../../sources/latent-space-robotic-world-models-paper.md)

Encoders and other modalities: [LeJEPA](../../sources/lejepa-paper.md) · [LeVJEPA](../../sources/levjepa-paper.md) · [LeNEPA](../../sources/lenepa-paper.md) · [VL-JEPA](../../entities/vl-jepa.md) · [EchoJEPA](../../sources/echojepa-paper.md) · [EchoWorld](../../sources/echoworld-paper.md) · [Music-JEPA](../../sources/music-jepa-paper.md) · [HP-JEPA](../../sources/hp-jepa-paper.md) · [Market-JEPA](../../entities/market-jepa.md) · [awesome-jepa](../../sources/awesome-jepa-github.md) · [DSeq-JEPA (Day 2)](../../sources/chicago-booth-world-modeling-workshop-2026-day2.md)

Theory: [When Does LeJEPA Learn a World Model?](../../sources/when-does-lejepa-learn-a-world-model-paper.md) · [JEPA generalization theory](../../sources/jepa-generalization-theory-paper.md) · [temporal straightening](../../sources/temporal-straightening-paper.md) · [compact spatial-relations WM](../../sources/grounding-spatial-relations-compact-wm-paper.md)

## Related

- [Joint-Embedding Predictive Architecture](../../concepts/world-models/jepa.md) — the architecture family, anti-collapse ladder, and probe evidence.
- [What world models are measurably good for](what-world-models-are-measurably-good-for.md) — role-by-role verdicts; where the JEPA family has and hasn't been measured.
- [The abstraction tax](abstraction-tax.md) · [The declared-axis experiment](declared-axis-experiment.md) — why §13 looks the way it does, and the test.
- [JEPA for a household mobile manipulator](jepa-for-household-mobile-manipulator.md) — this index applied to one decision.
- [The anti-collapse lineage](ssl-anti-collapse-lineage.md) — the 2018–2026 history under the mechanisms.
- [Why JEPA research skips the simulator stack](why-jepa-research-skips-the-simulator-stack.md) — companion on simulator choice.
- [Generative-video vs JEPA world models](generative-video-vs-jepa-world-models.md) — paradigm contrast.
- [LeWorldModel — train and run howto](leworldmodel-howto.md) — the runnable entry point.
- [World model](../../concepts/world-models/world-model.md) · [World-model simulators](../../concepts/world-models/world-model-simulators.md) — broader and narrower concepts.
