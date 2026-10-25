---
title: "What the latent throws away — five fixes for dynamics collapse in JEPA world models (Sept–Oct 2026)"
type: synthesis
created: 2026-10-22
updated: 2026-10-24
tags: [jepa, world-model, slow-feature-collapse, anti-collapse, inverse-dynamics, sigreg, motionjepa, avl-jepa, gawm, hamiltonian-jepa, predictive-closure, ad-e2e-jepa, leworldmodel, smwm, evaluation, benchmarks, synthesis]
---

# What the latent throws away — five fixes for dynamics collapse in JEPA world models (Sept–Oct 2026)

Between 3 September and 19 October 2026, five groups published on the same failure. An action-conditioned JEPA world model can predict well in its latent space while the latent **drops what the planner needs**: the moving agent, the effect of an action, the fast part of the scene. A sixth paper, on driving, ran into the same failure without naming it. Each paper names the failure differently:

| Paper | Its name for the failure |
|---|---|
| [MotionJEPA](../../sources/motionjepa-temporal-feature-collapse-paper.md) | *temporal feature collapse*: "a strong inductive bias towards slow features" |
| [AVL-JEPA](../../sources/avl-jepa-causal-dynamics-collapse-paper.md) | *causal dynamics information collapse* |
| [GAWM](../../sources/physically-grounded-jepa-world-models-paper.md) ("Physically grounded JEPA WMs") | "latent prediction alone does not … retain information relevant to robotic control" |
| [Hamiltonian JEPA](../../sources/hamiltonian-jepa-control-state-paper.md) | "one embedding [asked] to serve both perception and control" |
| [Predictive Closure](../../sources/predictive-closure-jepa-feature-selection-paper.md) | none; it is the theory of *which* features survive |
| [AD-E2E-JEPA](../../sources/ad-e2e-jepa-autonomous-driving-paper.md) | none; LeWM's plans barely depend on the action, and the paper does not diagnose why |

The wiki already had a name and a theorem for the extreme case: **[slow-feature collapse](../../concepts/world-models/slow-feature-collapse.md)**, and the [hierarchical H-JEPA paper](../../sources/h-jepa-hierarchical-world-models-paper.md)'s App. L proof that no regulariser on the *marginal* distribution of embeddings, SIGReg included, can rule it out. This page reads the five new papers against that result. It matters for the wiki's [focus question](open-questions-and-research-direction.md): *what information does a robot world model need to preserve, and how can we tell before putting it on a robot?*

## The six papers at a glance

| | **MotionJEPA** | **AVL-JEPA** | **GAWM** | **Hamiltonian JEPA** | **Predictive Closure** | **AD-E2E-JEPA** |
|---|---|---|---|---|---|---|
| Group | Oxford / vivo / AMI … **Balestriero** | Qiao, Zhang, Song, Huang | Genisom AI | Tel Aviv (**Wolf**) | Bar-Ilan / Berkeley / Ai2 (**Y. Goldberg**) | NYU (**LeCun**, Choromanska) |
| Date | 09-20 | 10-02 | 09-03 (v2 09-19) | 09-27 | 10-19 | 09-28 |
| **Barrier** | predict an embedding of the **pixel difference** from (z_t, z_{t+1}) ("DISReg") | inverse dynamics on Δz, then noise-augmentation fine-tune | inverse dynamics + **state alignment** to sim state; SIGReg removed | **orthonormal action port** in a port-Hamiltonian predictor + tied inverse readout; BW prior instead of SIGReg | theory | frozen DINOv3 + small compressor with per-patch SIGReg |
| **Labels the barrier needs** | **none** (the predictor still takes actions) | actions | actions **+ full privileged sim state** (object pose, velocity) | actions only, which conditioning already uses | — | — (frozen encoder) |
| Acts on | joint law of (z_t, z_{t+1}) | joint | joint | predictor structure | — | — |
| Test regime | 3 synthetic games; LeWM suite **with a per-episode wood background** | LeWM suite + perturbed inputs | LeWM suite | LeWM suite | CIFAR collages, 3-d latent | NAVSIM driving, offline |
| Headline | 25-step mean **20.4 → 81.8%** (IDM 77.2, both 86.4) | PushT σ=0.10 noise **15.3 → 81.5%** | Cube **74 → 87** (quoted LeWM) | Cube **91.9** vs Delta-JEPA 79.3 | unpredictable features survive if they predict kept ones | LeWM 39.8 EPDMS vs 67.3 |
| Seeds / spread | 3 seeds on games; **none** on planning | one checkpoint per model | 3 seeds, **no std** | 3 seeds ± std | 1–3 runs per sweep | one seed |
| Real robot | no | no | no | no | no | no (open-loop replay) |
| Code | yes (no license) | "upon publication" | yes (MIT) + weights | yes | yes | yes, no weights |

## 1. The theory now explains why every fix has the same shape

Two results combine into one account.

- **H-JEPA Prop. 1 / Thm. 1** (hierarchical, App. L): an encoder that reads only what is constant within an episode has zero prediction error and satisfies any marginal regulariser exactly. In a scene-diverse dataset that collapse is an **optimum**, not a bad local minimum.
- **[Predictive Closure](../../sources/predictive-closure-jepa-feature-selection-paper.md)** generalises it. With latent entropy fixed by the regulariser, the ideal encoder keeps the **set** of features that best predicts its own next values. A within-episode-constant background costs nothing to predict, so a background set that fills the latent is a global optimum: the H-JEPA theorem restated in information terms. The new part is that **selection is set-level**. A feature that is unpredictable on its own is kept if it helps predict other kept features. Steering is also **indirect**: an auxiliary loss on feature C strengthens the features C predicts.

Put together, these say the bare JEPA objective has no reason to prefer the agent over the room. Action-conditioning alone can at best *tie* a zero-cost background, which is what H-JEPA's Table 12 measured (this "tie" reading is the Predictive Closure ingest's inference, not a claim in either paper). Something has to break the tie, and it must act on **pairs of timesteps**, not on single embeddings.

**Every new fix fits that description.** None contradicts the theorem.

| Fix | What grounds the extra term | What it is mechanistically |
|---|---|---|
| [SMWM](../../entities/smwm.md), [PLDM](../../entities/pldm.md), H-JEPA's IDM, AVL stage 1, GAWM's IDM | the executed **action** | inverse dynamics |
| GAWM's state alignment | the **simulator state** | supervised probing as a training loss |
| MotionJEPA's DISReg | the **pixel change** o_{t+1} − o_t | inverse dynamics with a learned motion target instead of the action |
| Hamiltonian JEPA's port | the **predictor's structure**: actions must move the state by a fixed, well-conditioned amount | an Ω(1) floor from architecture; its tied readout is provably a reweighting of the forward loss (Eq. 11) |

> [!note] The one label-free claim, and what it narrows
> MotionJEPA, which shares a senior author with the hierarchical H-JEPA and appeared two weeks earlier (uncited by it), is the only fix whose barrier needs **no labels**. It does not contradict App. L: DISReg acts on the joint law that App. L says a barrier must reach, and it is not the "time repulsion" that App. L found useless, because it rewards change that predicts a *specific target*. But its test background is **pixel-identical across frames under a fixed camera**, which is the easiest possible case for a difference image. The wiki's "only inverse dynamics works" therefore becomes **"only inverse dynamics has been shown on scene-diverse real data; a label-free barrier works with a fixed camera in simulation."** See the reconciliation on the [MotionJEPA page](../../sources/motionjepa-temporal-feature-collapse-paper.md#reading-it-critically).

### 1a. The proof for the inverse-dynamics rung (Toso et al., 2026-10-06)
The batch above argued from H-JEPA's theorem that every fix needs a grounded joint-in-time term. [Toso, LeCun, Anderson, Bounou](../../sources/preserving-unstable-modes-inverse-dynamics-paper.md) prove the inverse-dynamics case in control-theoretic terms, for linear systems:
- prediction + SIGReg admits an exact minimiser that discards **every unstable mode** (Lemma 2);
- **endpoint inverse dynamics** over H steps keeps the **H-step reachable subspace** (Theorem 1), which converges to the unstable subspace as H grows (Theorem 2).

On nonlinear MuJoCo tasks with proprioception in the encoder input:
- **CartPole:** latent-LQR goes 0% → 100%.
- **Walker2D:** the walking limit cycle survives only with EP-IDM, which reaches 2.91 m/s under iCEM against ~0.

**What the theorem adds to this synthesis is scope.** One-step IDM (SMWM, PLDM, GAWM, AVL stage 1) is the H = 1 case and protects only `range(B)`: what the action moves *directly*. See §4.

## 2. The labels ladder: what each fix costs a real robot

Ordered by what a deployment has to log:

1. **Privileged state** (GAWM's SA): object pose and velocity from the simulator. A real robot has none of this for objects, though a proprio-only variant is an obvious, untested reduction.
2. **Actions** (IDM in all its forms, AVL, Hamiltonian JEPA): teleop or play data with logged commands. This is the wiki's [standing recommendation](../../concepts/world-models/slow-feature-collapse.md#current-state-2026-10), now supported by four more papers.
3. **Nothing beyond video** (MotionJEPA's regulariser): works only while the camera is still. A **mobile manipulator's head camera or wrist camera moves**, and under ego-motion the difference image is mostly scene, so `d` can itself carry episode identity. `SIGReg(d)` is a marginal regulariser, so Prop. 1 applies to it. *This is the wiki's reasoning; no paper tests it.*

For the [household mobile manipulator](jepa-for-household-mobile-manipulator.md) the practical answer is unchanged: **log actions**. The new option is to **add DISReg on top of IDM** (MotionJEPA's best row, 86.4%) for the static-camera views. That costs one extra ViT-Tiny at training time and nothing at inference.

## 3. The benchmark problem: four of the papers test where the theorem says the failure is absent

MotionJEPA, AVL, GAWM and Hamiltonian JEPA all report on **LeWM's four simulators**: TwoRoom, Reacher, Push-T and OGBench-Cube. Each is a single scene with a fixed camera. In that regime the background is a point mass, and the [slow-feature-collapse page](../../concepts/world-models/slow-feature-collapse.md#when-it-bites) records that **SIGReg alone suffices**. Total collapse does not happen there. What these papers fix on the clean suite is a **graded** version: dynamics information that is *weakly* encoded, not absent. Two of them manufacture the hard case:

- **MotionJEPA** inserts a per-episode wood texture, which makes the background vary across episodes while staying constant within each one. Under that one change **LeWM falls to 20.4%**: Push-T 4.0%, Reacher 5.2%. That is the clearest simulated demonstration of slow-feature collapse in the wiki.
- **AVL** perturbs inputs at test time (noise, saturation, brightness). LeWM's Push-T drops from 96% to **14%** under +0.35 saturation. That is fragility, related to collapse but not the same thing.

The only paper here on genuinely scene-diverse data is **AD-E2E-JEPA**, and there LeWM is the one model that trains its own encoder across many scenes, and the one whose plans barely depend on the action (5.7% top-1 trajectory hit rate against 53.8%). That fits the slow-feature-collapse prediction. The paper never diagnoses it, and its LeWM is a ViT-L at **batch size 8**, far from the published ~15M-parameter recipe, so the evidence is suggestive only.

### LeWM's own score depends on whose paper you read

Every paper's headline is a delta over its own LeWM run, and those runs disagree by more than most of the deltas:

| LeWM baseline in … | TwoRoom | Reacher | Push-T | Cube |
|---|---:|---:|---:|---:|
| [LeWM paper](../../sources/leworldmodel-paper.md) (Fig. 6, as quoted by GAWM) | 87 | 86 | 96 | 74 |
| [SMWM](../../sources/sensorimotor-world-models-paper.md) | 94 | 67 | 87 | **59** |
| [Hamiltonian JEPA](../../sources/hamiltonian-jepa-control-state-paper.md) (Delta-JEPA protocol) | **74.9** | 79.9 | 84.5 | 64.1 |
| [AVL-JEPA](../../sources/avl-jepa-causal-dynamics-collapse-paper.md) (own runs) | 88.4 | 86.4 | 96.0 | 73.2 |
| [MotionJEPA](../../sources/motionjepa-temporal-feature-collapse-paper.md) (wood background) | 28.8 | 5.2 | 4.0 | 43.6 |

LeWM's Cube score ranges over **15 points (59–74) across papers on nominally the same task**. GAWM's TwoRoom also uses an easier goal protocol (25 steps ahead with a 50-step budget, against LeWM's 100 and 150). **Cross-paper comparison of these numbers is meaningless; only within-paper deltas count.** Even within papers, the strongest baselines are often the authors' own re-implementations (MotionJEPA's "IDM" is not SMWM as published), and AVL and MotionJEPA's planning tables have no spread at all.

> [!warning] Implied leaderboard — do not read it as one
> On Cube, the reported numbers are Hamiltonian JEPA 91.9, GAWM 87, GAWM IDM-only 85, SMWM 84, Delta-JEPA 79.3, AVL 78.2. Given the baseline table above, this ordering says almost nothing. A **single-protocol comparison** is the missing experiment (see §6).

## 4. A pattern worth testing: inverse dynamics keeps the arm and may lose the object

Inverse dynamics grounds the latent in **what the agent moves**. Predictive Closure predicts it will also pull in the agent's *predictive partners*, but a pushed object is a partner only through contact. Across the clean-suite numbers:

- SMWM (IDM as the only anti-collapse term): Push-T **83 vs 87** for SIGReg, while it wins Cube 84 vs 59.
- GAWM, IDM only: Push-T **83 vs 96** for quoted LeWM, Reacher 63 vs 86, while it wins Cube 85 vs 74.
- Hamiltonian JEPA's probes: best on the agent and end-effector, **worse than LeWM on the Push-T block** (location 0.152 vs 0.038 linear MSE). It still plans better.
- MotionJEPA's game probes: SMWM keeps *only* the action-driven variables (Pong bats, Golf ball) and drops the rest.

Against the pattern: in MotionJEPA's wood-background setting, IDM is the **best** method on Push-T (83.6%) and recovers the agent better than DISReg does. When the alternative is total collapse, an arm-only latent is a large improvement.

> [!note] A mechanism, from the control side (2026-10-24)
> [Toso et al.](../../sources/preserving-unstable-modes-inverse-dynamics-paper.md) Theorem 1, read with H = 1, gives `ker(F) ∩ range(B) = {0}`. **One-step IDM protects only the directly actuated directions.** A pushed object is reached through contact, through `AB, A²B, …`, so only **multi-step (endpoint) IDM with H spanning the contact** protects it. *Wiki inference* (linear theory carried over to hybrid contact dynamics): this predicts the §4 pattern, and predicts EP-IDM fixes it. Add an **EP-IDM arm with H ≥ a typical push duration** to the §6 shootout.

> [!note] Hedged reading
> On fixed-scene benchmarks, IDM-style terms tend to help the **actuation-dominated** task (Cube) and hurt or tie the **contact-dominated** one (Push-T). Hamiltonian JEPA's predictor audit supports that split: Push-T is dissipation-dominated, Cube actuation-dominated. For a household robot, the object is the point. The obvious counterweights are DISReg (pixel change includes the pushed object) and GAWM's state alignment (object pose, if you have it). That may be why the combined rows (MotionJEPA + IDM, GAWM SA + IDM) are best in their papers. **This is four papers' numbers under four protocols, not a controlled result.**

## 5. Evaluation: collapse stays invisible to the obvious checks, and the diagnostics disagree

- **Loss doesn't show it.** In MotionJEPA's Dino game, LeWM's dino-position probe falls to ~0.1 NMSE and then climbs back to ~1.0 by 20k steps, with no sign in the training loss (Fig. 3). That matches H-JEPA's account: collapsed models have *low* loss.
- **Probes don't track planning.** Hamiltonian JEPA plans on directions that physical probes cannot see. Ranking candidates by the probe-orthogonal remainder alone reproduces the full ranking (Spearman 0.997). It also decodes the Push-T block worse than LeWM and still plans better. AVL's counterfactual action-ranking Spearman for LeWM on Push-T is **0.19** while LeWM plans at 96%.
- **No two papers share a diagnostic.** H-JEPA uses action sensitivity and the share of latent variance that lies within episodes. MotionJEPA uses MLP probes against a random-init floor. AVL uses counterfactual Spearman and subspace erasure. Hamiltonian JEPA uses probe-orthogonal ranking. AD-E2E-JEPA uses trajectory hit rate.

So the wiki's [world-model evaluation](../../concepts/world-models/world-model-evaluation.md) advice, *measure action sensitivity, not loss*, still holds. But nobody has checked whether action sensitivity, probes and planning success agree on one model. That gap matters most for the focus question's second half, *how can we tell before putting it on a robot*.

- **Planning success can be perfect while a control-critical direction is gone.** In [Toso et al.](../../sources/preserving-unstable-modes-inverse-dynamics-paper.md), CEM and GBP reach 100% on CartPole with SIGReg models whose latent-LQR fails every time. The failure appears only when you design **feedback** from the latent.

## 6. The experiment this batch makes cheap

All four method papers build on LeWM's codebase and benchmark suite. A **one-protocol shootout** is single-GPU work, and it would settle most of §3–§5:

- **Arms:** LeWM; LeWM + IDM; LeWM + **EP-IDM (H spanning a push)**; LeWM + DISReg; LeWM + IDM + DISReg; LeWM + proprio-only state alignment; the Hamiltonian port.
- **Conditions:** clean suite; MotionJEPA's wood background; a **moving-camera** variant (random per-step crop jitter as a cheap ego-motion proxy).
- **Measures:** planning success over ≥3 seeds with spread; **latent-LQR or the log-det rollout volume** as the cheap extra diagnostics (§5, §7); action sensitivity (H-JEPA); an MLP probe of the agent *and* of the pushed object.

That tests three things together. Does the label-free barrier survive camera motion (§2)? Does IDM lose the object (§4)? Do the diagnostics agree (§5)? It belongs in the [backlog](../../backlog.md) next to the RankMe item.

## 7. Adjacent: the predictor can collapse too (LeHami, 2026-10-11)

Everything above concerns what the **encoder** keeps. [LeHami](../../sources/lehami-symplectic-latent-dynamics-paper.md) (Yalovetzky, Balestriero, LeCun) addresses the other component: an autoregressive predictor that **contracts the latent cloud a little at every step**. Its fix is architectural, not a loss term: an action-conditioned Hamiltonian flow with an exactly symplectic leapfrog step. Phase-space volume is then preserved for any parameters and any action sequence.

- **How it differs from Hamiltonian JEPA.** Both are "Hamiltonian JEPAs", and they are complements, not rivals. [Hamiltonian JEPA](../../entities/hamiltonian-jepa.md)'s port gives the *encoder* an action-grounded floor (a §1 barrier), with damping and a non-symplectic Euler step. LeHami gives the *predictor* a volume guarantee and says nothing about which features the encoder keeps. A background-only encoder rolls out perfectly symplectically.
- **The diagnostic it adds** (cumulative log|det J|) is the first in this batch to look at the rollout rather than the encoder (§5). LeWM's declines linearly on a pendulum.
- **Where it stops.** It was tested only on two **volume-preserving** pendulums. The authors concede a symplectic latent cannot represent **dissipation** (friction, contact), which is the manipulation regime. It **loses** LeWM's goal-reaching on position (0.48 vs 0.80), and on velocity to an untied 3-frame LeWM window (0.53 vs 0.80). It wins on compute and training efficiency.
- **For the §6 shootout:** add the log-det diagnostic as a fourth measure. It costs nothing, and would show whether the encoder barriers also change rollout contraction.
- **Theory to pair with §1:** now ingested as §1a ([Toso et al.](../../sources/preserving-unstable-modes-inverse-dynamics-paper.md)). Originally surfaced by a third-party feed, *Preserving Unstable Modes Through Inverse Dynamics in JEPA World Models* (LeCun et al., 2026-10-06; [via](../../sources/ami-labs-intelligence-hub-research.md)), which said it proves that exact action reconstruction makes the encoder injective on the finite-horizon reachable subspace. It does, for linear systems.

## Evidence quality

| Paper | Strongest evidence | Weakest point |
|---|---|---|
| MotionJEPA | game probes with 3 seeds and ± std; baselines get a 10-point weight sweep | planning table has no seeds or spread; its λ values come from nowhere stated; fixed camera only |
| AVL-JEPA | clear stage-1 × stage-2 interaction (10.0 / 31.3 → 81.5) | one checkpoint per model; λ tuned on TwoRoom success; no code |
| GAWM | ablation isolates SA vs IDM | 5-page workshop paper; baselines quoted, not re-run; privileged-state labels; easier TwoRoom protocol |
| Hamiltonian JEPA | 3 seeds ± std; clean PIC derivation; paired test against the official LeWM checkpoint | rank and checkpoint epoch picked per task; p ≈ 0.053 on Push-T; SMWM missing from the comparison |
| Predictive Closure | theorem + five controlled tests | 3-d latent on CIFAR collages; actions never tested |
| Toso et al. (§1a) | linear proofs (Lemmas 1–2, Thms 1–2); clean LQR diagnostic | 10 trials, no seed spread; proprio in the encoder input; three small MuJoCo tasks |
| LeHami (§7) | exact guarantee by construction; 3 seeds ± s.d.; full reproducibility release | 64×64 pendulums only, both volume-preserving by design; compute table one seed; loses position planning |
| AD-E2E-JEPA | full 12k-scene NAVSIM run | one seed; future-frame goal makes it close to an inverse problem; non-standard LeWM |

## What this changes in the wiki

- [Slow-feature collapse](../../concepts/world-models/slow-feature-collapse.md): "the only barrier that works" is softened to the scene-diverse case. DISReg, state alignment and the constrained action port are added as barriers, and Predictive Closure is added as the general frame.
- [JEPA](../../concepts/world-models/jepa.md#common-training-challenges): the anti-collapse ladder gains a "joint-in-time, grounded target" rung.
- [SIGReg](../../concepts/world-models/sigreg.md): necessary for rank, not sufficient for dynamics. Inside Hamiltonian JEPA's architecture it is also the wrong prior (36.7% vs 93.3%), because its restoring force fades as a direction dies.
- [H-JEPA](../../entities/h-jepa.md): name-collision note for Hamiltonian JEPA.

## Related

- [Three ways to scale a JEPA world model](three-ways-to-scale-a-jepa-world-model.md) — the preceding batch; its "encoder split" section is where AD-E2E-JEPA's frozen-DINOv3 route fits.
- [The anti-collapse lineage](ssl-anti-collapse-lineage.md) — the 2018–2026 history this batch extends; DISReg sits next to [TDV](../../sources/tdv-paper.md) on the temporal-difference branch.
- [JEPA for a household mobile manipulator](jepa-for-household-mobile-manipulator.md) — the deployment the labels ladder (§2) is about.
- [Open questions and research direction](open-questions-and-research-direction.md) — question #1, the representation question.
- [Identifiability](../../concepts/world-models/identifiability.md) — a different regime: it concerns latent geometry when the latent is large enough. Predictive Closure concerns content when it is not.

## Sources used in this synthesis

- [MotionJEPA](../../sources/motionjepa-temporal-feature-collapse-paper.md) · [AVL-JEPA](../../sources/avl-jepa-causal-dynamics-collapse-paper.md) · [Physically grounded JEPA WMs (GAWM)](../../sources/physically-grounded-jepa-world-models-paper.md) · [Hamiltonian JEPA](../../sources/hamiltonian-jepa-control-state-paper.md) · [Predictive Closure](../../sources/predictive-closure-jepa-feature-selection-paper.md) · [AD-E2E-JEPA](../../sources/ad-e2e-jepa-autonomous-driving-paper.md)
- Theory (§1a): [Toso et al. — Preserving unstable modes](../../sources/preserving-unstable-modes-inverse-dynamics-paper.md)
- Adjacent (§7): [LeHami](../../sources/lehami-symplectic-latent-dynamics-paper.md) · discovery via [AMI Labs Intelligence Hub](../../sources/ami-labs-intelligence-hub-research.md)
- Prior wiki material: [H-JEPA (hierarchical)](../../sources/h-jepa-hierarchical-world-models-paper.md) · [SMWM](../../sources/sensorimotor-world-models-paper.md) · [Sobal et al. 2022](../../sources/sobal2022-jepa-slow-features-paper.md) · [LeWorldModel](../../sources/leworldmodel-paper.md) · [PLDM](../../sources/pldm-paper.md)
