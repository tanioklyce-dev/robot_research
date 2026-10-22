---
title: "Toward Physically Grounded JEPA World Models for Goal-Conditioned Robotic Planning (Liu, Huang et al., 2026)"
type: source
url: https://arxiv.org/abs/2609.03565
local_path: raw/2609.03565v2.pdf
sha256: c9140dbeb1f5978c5a95362704c12a800ed57cfe68fa0f2ef7666725df45801b
author: Muyuan Liu, Yue Huang, Zheng Liang, Xiang Gao
published: 2026-09-03
ingested: 2026-10-22
venue: "IROS 2026 Workshop on Physical World Models for Scaling Embodied AI (PWMS 2026), per arXiv comments; arXiv cs.RO, v2 (2026-09-19; v1 2026-09-03)"
format: "workshop paper, 5 pp, 4 figures, 2 tables, no appendix. Affiliation: Genisom AI, Beijing. Code (MIT) + checkpoints released as GAWM: https://github.com/zsibot/gawm"
tags: [jepa, world-model, leworldmodel, inverse-dynamics, state-alignment, privileged-supervision, slow-feature-collapse, temporal-straightening, cem, push-t, ogbench, tworoom, reacher, gawm]
---

# Toward Physically Grounded JEPA World Models for Goal-Conditioned Robotic Planning (Liu, Huang et al., 2026)

## Summary

A five-page workshop paper that takes the [LeWorldModel](../entities/leworldmodel.md) architecture (ViT-Tiny/14 encoder, 192-d [CLS] latent, causal-transformer predictor with AdaLN action conditioning, CEM planning) and **replaces [SIGReg](../concepts/world-models/sigreg.md)** with two supervised auxiliary heads. The first is an **inverse-dynamics (IDM)** head that regresses the action chunk from (z_t, z_{t+1}). The second is a **state-alignment (SA)** head that regresses the **simulator's full physical state s_t**, velocities included, from (z_{t−1}, z_t). Total loss is L_pred + α·L_sa + β·L_idm, with α = β = 1. On LeWM's four-task benchmark it reports **TwoRoom 100%, PushT 98%, OGBench-Cube 87%, Reacher 85%**, against LeWM's published 87 / 96 / 74 / 86. SA+IDM beats IDM alone on all four tasks. A second analysis on OGBench-Cube argues that LeWM's higher **temporal straightening** (0.69 vs 0.55) comes from a **lower-dimensional transition subspace** (r95 = 17 vs 32.8), so straightening alone can mislead. The paper's code repository calls the model **GAWM** ("Geometry-Aware World Model"); the paper itself never uses the name. There is **no real robot** and no SIGReg+SA combination; the authors list that combination as future work.

## Key claims

**Method (§II)**
- Data tuples are (o_t, s_t, a_t), where s_t is "the corresponding physical measurements". **§III-A: "we use the full physical state provided by each task as supervision."** These labels are needed only at training time, and planning uses only E and F (§II-B).
- L_idm (Eq. 4) follows [PLDM](pldm-paper.md) and [SMWM](sensorimotor-world-models-paper.md). Its stated rationale is the same Ω(1) argument as [slow-feature collapse](../concepts/world-models/slow-feature-collapse.md): a collapsed encoder restricts H to the constant-action predictor.
- L_sa (Eq. 5) uses a *pair* of latents so that the head can recover velocities as well as configuration.
- Actions and Euclidean states are standardised per dimension. Angles are encoded in continuous coordinates. G and H are two-layer MLPs with hidden sizes 256 and 512.
- **No SIGReg and no VICReg term.** Anti-collapse comes entirely from the two supervised heads.

**What "full physical state" means in practice** (from the released `config/train/data/*.yaml`, not the paper):
- TwoRoom: 2 dims (agent position).
- PushT: 6 dims of configuration. This is the PushT state vector, which includes the **block's pose** as well as the agent's.
- Reacher: 8 dims (6 configuration + 2 velocity).
- OGBench-Cube: **33 dims**: configuration[0:21], arm velocity[21:27] and **cube velocity[27:33]**. Checkpoints are named `*_object`.
- SA therefore supervises with **privileged object state**, not proprioception.

**Planning (Table I, §III-B)**: CEM on terminal latent L2 distance (Eq. 7). 50 fixed start–goal problems per seed, goal 25 env steps ahead, budget 50 steps. Ours = mean of 3 training seeds, **no std reported**. α = β chosen from {0.01, 0.1, 1.0} on a PushT validation split and applied to all tasks.

| Method | TwoRoom | Reacher | PushT | OGB-Cube |
|---|---|---|---|---|
| DINO-WM (quoted) | 100 | 79 | 74 | 86 |
| PLDM (quoted) | 97 | 78 | 78 | 65 |
| LeWorldModel (quoted) | 87 | **86** | 96 | 74 |
| IDM only (α=0, β=1) | 94 | 63 | 83 | 85 |
| SA+IDM (ours) | **100** | 85 | **98** | **87** |

- Table I's caption says outright that baseline numbers are "taken from LeWorldModel". I checked them against LeWM's Fig. 6 ([LeWM paper](leworldmodel-paper.md)) and they match. The DINO-WM figures are LeWM's **no-proprioception** DINO-WM. LeWM's DINO-WM+prop variant scored 100 on TwoRoom and 92 on PushT.
- **SA adds to IDM on every task**: +6 TwoRoom, **+22 Reacher**, +15 PushT, +2 Cube.
- **IDM alone is the worst model on Reacher (63)** and is below LeWM on PushT (83 vs 96). Without state labels the IDM-only model does **not** beat SIGReg on two of the four tasks.

**Straightening and transition subspace (§III-C, Table II, Figs. 3–4)**: OGBench-Cube only, 100 fixed trajectories.
- Straightening (mean cosine between successive Δz, following [Temporal Straightening](temporal-straightening-paper.md)): **LeWM 0.69 ± 0.025, IDM 0.62 ± 0.029, SA+IDM 0.55 ± 0.034.** Adding SA *lowers* straightness.
- r95 is the number of components holding 95% of the energy in an uncentred SVD of Δz. **LeWM 17.0 ± 1.7, IDM 30.2 ± 2.6, SA+IDM 32.8 ± 3.0.**
- The paper's argument is that in the rank-one limit successive displacements are parallel or antiparallel. That gives mostly +1 scores, a few −1 reversals, and a high average with a polarised distribution, which matches LeWM's per-step profile in Fig. 3. Its conclusion: average straightening "can conceal the concentration of temporal variation in a low-dimensional subspace."

**Code / release** ([GAWM repo](https://github.com/zsibot/gawm), MIT, created 2026-09-14): training and eval for all four tasks, built on LeWM, stable-worldmodel and stable-pretraining, using LeWM's HF datasets. Checkpoints are on HF (`kikihuang/GA-WM`). The README reports **Cube 88%** (paper: 87) and a **"GAWM-Enhanced Cube" at 96%** that uses **BC-initialised CEM plus a smoothness cost**. The enhanced variant is **not in the paper**.

## Reading it critically

> [!warning] Not apples-to-apples with LeWM: privileged state supervision vs. pixels only
> LeWM trains on **pixels + actions only**. SA+IDM additionally regresses the simulator's **full state, including object pose and velocity**: the PushT block, and the Cube cube's configuration and velocity. That is the very information the planner's goal distance has to resolve. The comparison therefore shows that **privileged-state supervision helps a JEPA plan**, which is expected. It does not show a better self-supervised world model. LeWM's own Fig. 6 shows how much privileged input buys: DINO-WM goes from 74 → 92 on PushT when given proprioception. The fair baselines are missing: **LeWM + SA** (SIGReg kept), **LeWM + IDM**, and **SA alone**. The paper also never puts its probe-able state on a common footing with [LeWM's probing results](leworldmodel-paper.md), even though SA's training target *is* the probe target.

> [!warning] The TwoRoom protocol is easier than LeWM's
> §III-A says it adopts LeWM's protocol "with the goal 25 environment steps ahead and an interaction budget of 50 steps" for all four tasks, and the released `config/eval/tworoom.yaml` confirms `goal_offset_steps: 25, eval_budget: 50`. **LeWM's TwoRoom protocol (App. F.1) is goal 100 steps ahead with a 150-step budget.** LeWM's quoted 87% on TwoRoom therefore comes from a harder task than this paper's 100%. PushT, Cube and Reacher do use LeWM's 25/50 setting.

> [!note] The margins are small and there are no error bars
> Baselines are **quoted, not re-run**. "Ours" is 3 seeds × 50 problems with no std and no per-seed numbers. LeWM's own PushT is **96.0 ± 2.83** over 3 seeds (LeWM Table 5), so 98 vs 96 is within noise. Reacher 85 vs 86 is a tie. The one solid gain on a matched protocol is **Cube, 87 vs 74**, and that is the task where SA supervises 33 privileged dimensions including the cube's own velocity. The α=β=1 weights were tuned on PushT, the task where SA's gain is noisiest to judge.

> [!note] Is "higher transition dimension" good? This paper and SMWM disagree
> The paper treats LeWM's low r95 as a deficit. [SMWM](sensorimotor-world-models-paper.md) argues the opposite in its dot-world testbed: a good action-grounded latent's transition dimension should **equal the controllable DoF**, with everything else collapsed. A higher r95 for SA+IDM may reflect that it is *forced* to encode 33 regressed state dimensions (cube velocity included), not that it represents dynamics better. The paper shows that r95 and Cube success move together across **three models**, but that does not establish causation. r95 was measured only on Cube, and the latent scales differ visibly (LeWM's PCA axes span about ±10, the others about ±2). The straightening critique itself is sound and useful: a mean cosine can be high when transitions are almost one-dimensional. It is a **caveat on [Temporal Straightening](temporal-straightening-paper.md)-style metrics**, not evidence against SIGReg.

> [!note] Scope
> All four tasks are simulated, with no real robot. Fig. 1's arm is an illustration. Each task is trained and evaluated in-distribution on LeWM's datasets. There is no test of shift (cf. [stable-worldmodel](stable-worldmodel-paper.md)'s colour/shape collapse) and no multi-scene data (cf. DROID in [H-JEPA](h-jepa-hierarchical-world-models-paper.md)). The ingested copy is v2 (2026-09-19); what changed from v1 (2026-09-03, 359 KB vs 325 KB) has not been checked.

**How it fits the batch.** [H-JEPA App. L](h-jepa-hierarchical-world-models-paper.md) proves that marginal regularisers, SIGReg included, cannot block [slow-feature collapse](../concepts/world-models/slow-feature-collapse.md), and that **inverse dynamics is the only working barrier, at the price of action labels**. This paper is consistent with that. It drops SIGReg entirely and survives on IDM. It then adds a second, much costlier label stream: full simulator state. Action labels come from any teleop or play log. **Object-pose and velocity labels do not exist for real household data** without motion capture or a state estimator. The recipe is therefore a simulation result, or one that needs an external perception stack. That limits how much it helps the home-robot case where slow-feature collapse actually bites.

## Entities mentioned

- [LeWorldModel](../entities/leworldmodel.md): the architecture backbone, primary baseline, and the source of all quoted baseline numbers and datasets.
- [DINO-WM](../entities/dino-wm.md): quoted baseline (frozen [DINOv2](../entities/dinov2.md) patch features).
- [PLDM](../entities/pldm.md): quoted baseline. Its IDM term is the precedent for L_idm.
- [SMWM](../entities/smwm.md): the inverse-dynamics-only predecessor (ref. [10]).
- [PushT](../entities/pusht.md): benchmark task.
- Delta-JEPA (arXiv 2606.31232) is cited as an IDM-on-latent-difference variant. It has no wiki page.
- Genisom AI (Beijing) is the authors' affiliation. It has no wiki page.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md)
- [SIGReg](../concepts/world-models/sigreg.md): removed here. The conclusion frames SIGReg as a distributional safeguard that does not control transition-subspace structure.
- [Slow-feature collapse](../concepts/world-models/slow-feature-collapse.md): IDM as the anti-collapse term, with no marginal regulariser.
- [Latent space](../concepts/world-models/latent-space.md): transition-subspace (r95) analysis.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md): straightening vs. effective transition dimension as diagnostics.

## Open questions

- What does **LeWM + SA** (SIGReg kept) score? The authors' own future-work line points there, and it is the comparison that would separate "state labels help" from "SIGReg hurts".
- How much of the gain survives if SA is restricted to **proprioception only** (arm joints, no object state)? That is the label set a real robot actually has.
- What is TwoRoom success under LeWM's actual 100-step-goal / 150-step-budget protocol?
- Is a higher r95 good or bad? It is unclear whether 32.8 transition dimensions on a Cube task with a low-dimensional action space means richer dynamics or regressed nuisance dimensions. SMWM's controllable-DoF criterion predicts the opposite of this paper's reading.
- Does the "Enhanced Cube" 96% (BC-initialised CEM plus a smoothness cost, README only) come from the world model or from the BC prior?
- Does SA's advantage survive multi-scene data (DROID), where H-JEPA found IDM necessary but scene identity dominates latent variance?
