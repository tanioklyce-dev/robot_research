---
title: "H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning (Zhang, Terver et al., 2026)"
type: source
url: https://arxiv.org/abs/2610.06805
local_path: raw/2610.06805v1.pdf
sha256: 4a4a799c50d2d0acc52ba264410d5bbf7c54e1aba99a9a968886e84c0e43e4c2
author: Wancong Zhang, Basile Terver, Michael Rabbat, Yann LeCun, Randall Balestriero
published: 2026-10-05
ingested: 2026-10-13
venue: arXiv (cs.LG), v1
format: "paper, 40 pp (10 main + appendices A–M). Affiliations: NYU, Advanced Machine Intelligence, INRIA Paris, Brown. Code, website, and a re-encoded DROID corpus released."
tags: [h-jepa, jepa, hierarchical-world-model, hierarchical-planning, leworldmodel, hwm, sigreg, inverse-dynamics, slow-feature-collapse, gradient-based-planning, droid, antmaze, push-t, ogbench, lecun, balestriero, ami-labs]
---

# H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning (Zhang, Terver et al., 2026)

## Summary

The paper trains a **stack of action-conditioned JEPAs end to end**. Each level has **its own encoder, action encoder, predictor and latent space**, and each predicts farther ahead than the level below (stride 2 per level in simulation, 3 on DROID). The base level is **[LeWorldModel](../entities/leworldmodel.md)** unchanged, and every level carries [SIGReg](../concepts/world-models/sigreg.md). Gradients from upper levels flow down into the lower encoders. Planning runs **top-down with gradient descent at every level**: the top level optimises macro-actions toward the goal, and its first predicted latent becomes the subgoal for the level below. The lower level's rollout is re-encoded into the upper latent space to be scored. That **distinct latent space per level** is the step beyond [HWM](../entities/hwm.md) (April 2026, same first author), whose levels share one space. The paper takes the name **H-JEPA**, so this is the first instance of LeCun's 2022 hierarchy *with representational abstraction* rather than only temporal decomposition.

There are three results. (1) **Selective abstraction**: higher levels drop fast, unpredictable detail (ant leg pose, a teleporting distractor) and keep slow, task-relevant state (position), but **only when the data's fast and slow factors differ in frequency by more than about 2×**. (2) **Planning**: on Visual AntMaze a three-level model goes from **18% → 73%** success with **less** planner compute than flat LeWM. Ablations split the gain into an *abstract goal cost* and *temporal decomposition*. (3) **DROID**: on real teleop video with changing scenes, a JEPA **collapses onto scene identity** ("slow-feature collapse"). An appendix proves that **no regulariser on the marginal embedding distribution, SIGReg included, can rule this out**. An **inverse-dynamics** term is needed, which requires action labels. With it, a second level improves offline plan fidelity at lower compute. **There is no closed-loop real-robot result.**

## Key claims

**Method (§2)**
- Level ℓ>1 state encoder pools a window of lower-level latents (all experiments use window w=1, i.e. pointwise on every s-th latent); action encoder pools s lower-level action embeddings into a **macro-action**. Per-level loss = teacher-forced one-step latent prediction + λ·SIGReg.
- Planning: Eq. 4 (top level, terminal goal cost), Eq. 6 (lower level matches the upper level's predicted subgoals after re-encoding its own rollout upward). Closed-loop uses only the first subgoal (K=1). Solver: AdamW through the rollout, ≤90 iterations, early stopping, best-of-S candidates; upper-level candidates are initialised from and **clipped to the 2nd–98th percentile of the last 4,000 training macro-actions**, since macro-actions have no native bounds.

**Selective abstraction (§3)**
- MLP-probe NMSE on frozen latents (3 seeds): AntMaze body state and the FourRoom distractor become less recoverable with depth, while agent position stays recoverable (Fig. 4).
- **The frequency-gap condition** (Fig. 5): the loss of fast-entity information at level 2 tracks the ratio of spectral centroids between the fastest and slowest state components. **Below ~2× (Push-T, Cube, DROID) there is little selective abstraction.** Abstraction is a property of the data's timescale separation, not something the architecture produces regardless.

**Planning (§4.1–4.2)**: 50 held-out tasks per environment, 3 paired model and planner seeds, planner settings chosen under a 100-TFLOP budget on a separate sweep task set.
- **AntMaze: flat LeWM 18.0 ± 3.5% → three-level H-JEPA 73.3 ± 3.5%.** Four levels: 63.3 ± 7.7%. On FourRoom, AntMaze and Cube, each level up to three moves the success-vs-compute Pareto front **up and to the left**.
- **Push-T breaks at three levels**. The paper attributes this to clip starvation: a sample must fit inside one episode, Push-T episodes are short, so three- and four-level models see **58% and 14%** of LeWM's training transitions (Table 3).
- **vs HWM, re-implemented as H-JEPA with identity encoders above level 1** (same data and training): three-level H-JEPA reaches **nearly 2× HWM's success on AntMaze**, is moderately better on Cube, and **ties on FourRoom and Push-T**. HWM beats flat LeWM in all four environments.
- **Cost-only ablation (Table 1)**: keep level-1 dynamics and the planner fixed, and change only the space the goal distance is measured in. Projecting to a higher level's latent raises AntMaze success from 16.7% (native L1) to 22.0% (L3 projection, three-level model). For the four-level model it goes from 10.0% to 26.7%. Fig. 7 shows why: level-1 latent distance is **nearly flat away from the goal**, while higher levels grade smoothly along maze corridors. No gain on Push-T or Cube, where no abstraction emerged.
- **Temporal decomposition**: subgoal-tracking costs decrease monotonically along expert trajectories (Spearman 0.89–1.00) far more consistently than full-horizon goal costs (0.48–0.75) (Table 10).

**DROID (§4.3, App. J, K, L)**
- Offline only. **16 grasp-centred pick-and-place clips**, ~7.2 s each, held out from training. Plans are scored by **Fréchet fidelity** of the planned xyz path against the expert path (0% = arm stays still, 100% = expert path).
- **Without IDM: ~0% (collapse). LeWM+IDM: ~34%. HWM (2 levels): ~35%. H-JEPA (2 levels): ~40%** (Fig. 9b, read from the figure). H-JEPA's Pareto front sits above the flat model's at lower compute. Public frozen-encoder baselines (JEPA-WMs, V-JEPA 2-AC) need **orders of magnitude more planner compute for lower fidelity**.
- **The metric was validated in simulation (App. J.2).** On OGBench Cube it is **necessary but not sufficient**: no grasp succeeds below a fidelity floor, and most episodes above it still fail. On RoboCasa CloseDrawer, within-configuration rank correlation with graded progress is **+0.47**. The authors' own reading: a fidelity gap shows *which* planner is better, not *how much*.
- **Scene diversity → collapse.** 75% of latent variance is *between* episodes on DROID vs 28% on Cube (App. L.2).
- **Theory (App. L).** *Proposition 1*: any regulariser that only sees the marginal law of the embeddings (VICReg-style variance/covariance, whitening, entropy, SIGReg) is satisfied exactly by an encoder that reads only the background and is constant within each episode. Prediction loss is then zero. *Theorem 1*: that collapse is an optimum of the objective. *Proposition 2*: SIGReg grouped with time in the sample axis adds a real but small barrier; the paper's own (T, N, D) grouping adds none. *Proposition 3*: an inverse-dynamics term imposes an **Ω(1) loss floor on collapse** (= 1 per unit action variance; 50 at γ = 50). Table 12: every SIGReg-only run collapses whatever λ is, with action sensitivity below 0.05. **"Time repulsion"** (rewarding latent change, no labels needed) keeps the predictor off the identity map but never beats the zero-action floor. **Only IDM works, and it needs action labels.**
- **Fig. 17 grid**: SIGReg restores **representation rank**; IDM is what converts rank into **planning fidelity**.
- **Frame-rate gotcha**: DROID is recorded at 15 Hz but its video containers are **tagged 60 fps**, so a loader that derives stride from the tag samples at a quarter of the intended rate. The public frozen-encoder baselines are "configured at 4 fps with such a loader," which is **1 frame per second of real time**, and are evaluated at that native rate here.
- **Released**: a re-encoded DROID, **127.6 GB for 74,530 episodes** (three views at 256², libx264 CRF 18). That is ~45× smaller than raw (~5.5 TB) and decodes 17.9× faster, with trajectories bitwise identical and a median PSNR of 33.75 dB. Results trained on it match raw within noise.
- **Not used**: the wrist camera, proprioception and stereo. Each training window samples one exterior camera.

**Compute**: training on H200 GPUs. Planner cost is reported per episode in TFLOPs, which is better compute reporting than most of the planning literature in the wiki.

## Reading it critically

> [!note] The DROID result is small and offline, and the paper is careful about it
> H-JEPA's lead over HWM on DROID is about **5 points of Fréchet fidelity on 16 clips**, over 3 train × 3 planner seeds. The paper's own calibration says a gap shows ordering, not magnitude. LeWM+IDM → HWM is about +1, inside the error bars. The headline "hierarchy improves real-robot planning" therefore means **better offline path agreement**. Nothing was executed on a robot, and the conclusion's next step is "test whether these gains translate to closed-loop control on a physical robot." Compare HWM's April result, which *was* closed-loop on a real Franka (0% → 70%) but used a frozen V-JEPA 2-AC with CEM.

> [!warning] HWM is a re-implementation here, not the April paper's system
> The "HWM" baseline is H-JEPA with identity encoders above level 1, trained and planned with this paper's recipe: gradient descent, LeWM base. The [original HWM](hwm-paper.md) wrapped frozen DINO-WM, PLDM and V-JEPA 2-AC and planned with CEM. The comparison isolates the representational hierarchy cleanly. It does **not** say how H-JEPA compares with HWM as published.

- **Abstraction is conditional.** Selective abstraction needs a >2× timescale gap. The manipulation datasets, DROID included, fall below it, and abstract goal costs gave **no** gain on Push-T or Cube. On DROID the second level helps, but the representational mechanism shown cleanly in AntMaze isn't demonstrated there. The paper says that "both levers are active" on DROID, based on the H-JEPA-vs-HWM gap.
- **Depth is not free.** The best result is at three levels; four levels drops on AntMaze, and Push-T fails at three. The clip-length arithmetic means each extra level halves or worse the usable data from short episodes. That matters for household data, which is mostly short demonstrations.
- **Evaluation is held out**: compute sweep and final evaluation use different task seeds, settings are fixed before the final set, and the 16 DROID clips are excluded from training. That is unusually good practice for this literature.

## Why it matters here

- **It answers the wiki's longest-running open question on JEPA hierarchy.** The [JEPA concept page](../concepts/world-models/jepa.md) called HWM "the realized H-JEPA." By the definition in LeCun's own position paper (abstract levels, not only longer strides), HWM was half of it. This paper is the other half.
- **It answers an open question on the [SIGReg page](../concepts/world-models/sigreg.md)** (where to put SIGReg in a temporal model) with a proof as well as an experiment. The answer is that **no placement prevents slow-feature collapse in changing scenes**. Pooled grouping adds a small barrier; per-time grouping adds none.
- **It sets a constraint for any home-robot JEPA plan.** A home is the DROID case: changing rooms, lighting, objects and camera pose. A LeWM-style model trained on that needs **action-labelled data and an IDM term**, or it learns to recognise *which room it is in* and nothing about the arm. That bears on [LeWM on Stretch](../syntheses/projects/lewm-on-stretch-feasibility.md) and the [household JEPA synthesis](../syntheses/world-models/jepa-for-household-mobile-manipulator.md). See [slow-feature collapse](../concepts/world-models/slow-feature-collapse.md).

## Entities mentioned
- [H-JEPA](../entities/h-jepa.md) · [HWM](../entities/hwm.md) · [LeWorldModel](../entities/leworldmodel.md) · [PLDM](../entities/pldm.md) · [JEPA-WMs](../entities/jepa-wms.md) · [V-JEPA 2](../entities/v-jepa-2.md) · [DROID](../entities/droid.md)
- [Yann LeCun](../entities/yann-lecun.md) · [Randall Balestriero](../entities/randall-balestriero.md) · [Basile Terver](../entities/basile-terver.md) · [AMI Labs](../entities/ami-labs.md)

## Concepts touched
- [JEPA](../concepts/world-models/jepa.md) — the H-JEPA section.
- [SIGReg](../concepts/world-models/sigreg.md) — its formal limit.
- [Slow-feature collapse](../concepts/world-models/slow-feature-collapse.md) — new page.
- [Gradient-based planning](../concepts/world-models/gradient-based-planning.md) — gradient descent at every level, and abstraction as a fourth answer to "what makes a latent good for planning."

## Open questions
- Closed-loop on hardware. Does a 5-point offline fidelity gain change grasp success? The Cube calibration warns it may not, either way.
- Action-free video. Removing IDM removes the only working collapse barrier, and the paper's time-repulsion attempt fails. Is there a label-free barrier that acts on the joint law across time?
- Does the >2× timescale-gap condition hold for household tasks, such as navigation (slow) plus manipulation (fast) on a mobile manipulator? That combination plausibly clears it where tabletop manipulation does not.
- Variable-duration segments instead of fixed strides, and language-aligned upper levels (both listed as future work).
- Multi-view and wrist-camera encoding, which the authors flag as the clearest route to better DROID numbers.
