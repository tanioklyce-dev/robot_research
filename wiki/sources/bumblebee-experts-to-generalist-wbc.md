---
title: "From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots (BumbleBee)"
type: source
url: https://arxiv.org/abs/2506.12779
project_page: https://beingbeyond.github.io/BumbleBee/
author: Yuxuan Wang, Ming Yang, Ziluo Ding, Yu Zhang, Weishuai Zeng, Xinrun Xu, Haobin Jiang, Zongqing Lu (Peking University + BeingBeyond)
published: 2025-09-01
ingested: 2026-07-15
local_path: raw/2506.12779v3.pdf
sha256: e8174008815d00c53c87e25c06e538d581738bae527404352cfc7b22d3efdea1
venue: arXiv 2506.12779 (v3)
format: pdf (17 pp.)
tags: [bumblebee, beingbeyond, peking-university, zongqing-lu, whole-body-control, humanoid, unitree-g1, motion-tracking, sim-to-real, distillation, rl, amass]
---

# From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots (BumbleBee)

## Summary

**BumbleBee (BB)** is an **expert-to-generalist** learning framework for **agile [whole-body control](../concepts/robotics/whole-body-control.md) (WBC)** on humanoid robots, from [BeingBeyond](../entities/beingbeyond.md) + Peking University ([Zongqing Lu](../entities/zongqing-lu.md) corresponding). Its thesis: a single generalist WBC policy trained on the full [AMASS](https://amass.is.tue.mpg.de/) motion corpus suffers **gradient conflict** because different motion types demand opposite control (aggressive jumps need high-torque precision; conservative motions need balance/smoothness). BB **decomposes the complexity at the data level**: cluster motions into behaviorally coherent groups, train a specialized expert RL policy per cluster, refine each with real-world data via **iterative delta-action modeling** (the [ASAP](https://agile.human2humanoid.com/) sim-to-real trick), then **distill all experts into one Transformer generalist**. Result: **SOTA general WBC** on a real [Unitree G1](../entities/unitree-g1.md), beating OmniH2O/Ome-H2O, Exbody2, and [HOVER](../sources/nvidia-gear-publications.md) — with the gap widening in the more realistic MuJoCo evaluator.

## Key claims

**Framework (3 stages)**
- **Stage 1 — AE clustering**: an **autoencoder groups motions** using both **kinematic leg-specific features** (joint positions/velocities, root translation/velocity, binary foot-contact states, foot velocities) *and* **text descriptions** (BERT-encoded [HumanML3D](https://github.com/EricGuo5513/HumanML3D) annotations). Losses align the motion latent `z_m` and text latent `z_l` (InfoNCE + L2) plus Huber reconstruction of key joints (head, pelvis, hands, feet). K-means on the learned motion embeddings → **six clusters**: Jump, Walk-slow, Walk-fast, Stand-up, Stand-mid, Stand-low (Table 2).
- **Stage 2 — Experts**: per cluster, an **RL motion-tracking policy** (3-layer MLP, PPO) is trained, then a **delta-action model** `π_Δ(s,a)` is fit from **real-world rollouts** (a hundred-plus real G1 trajectories) and used to reshape the sim: `s_{t+1}=f_sim(s_t, a_t+π_Δ)`. Fine-tune → recollect data → refit `π_Δ` **iteratively**; cluster-consistent dynamics make expert delta-models far more accurate than one general delta-model.
- **Stage 3 — Generalist**: **DAgger distillation** of all experts into a single **Gated Transformer-XL** WBC controller (10-observation context, 1 block, 6 heads, hidden 128) that "inherits stable control behaviors from multiple experts."

**Data curation**: SMPL-format AMASS motions **retargeted** to the [Unitree G1](../entities/unitree-g1.md) (23-joint config), **PHC-filtered** → **8,179 high-quality trajectories**.

**Results (Table 1 — Success Rate ↑ / MPKPE ↓ mm / MPJPE ↓)**

| Method | IsaacGym SR | MuJoCo SR |
|---|---|---|
| OmniH2O | 85.65% | 15.64% |
| Exbody2 | 86.63% | 50.19% |
| HOVER | 63.21% | 16.12% |
| **BumbleBee** | **89.58%** | **66.84%** |

- The **MuJoCo gap is the headline**: BB 66.84% vs next-best Exbody2 50.19%, all others <40% — evidence the clustered-expert approach generalizes to more realistic dynamics.
- **Ablations**: vs. a generalist trained without experts (*General Init*, MuJoCo 33.01%) and with **randomly** partitioned clusters (*Random*, 35.36%) — **semantic clustering is what matters** (BB 66.84%). Iterative delta fine-tuning lifts expert SR **51.49% → 60.33% → 70.37%** over 3 iterations (Table 4); real-robot foot stability visibly improves per iteration.
- **Compute**: trained on 2× desktops (i9-13900 + RTX 4090 + 64 GB each) — notably modest.

## Entities mentioned

- [BeingBeyond](../entities/beingbeyond.md) — the company behind BB (new).
- [Zongqing Lu](../entities/zongqing-lu.md) — corresponding author (Peking Univ + BeingBeyond).
- [Unitree G1](../entities/unitree-g1.md) — the target humanoid.

## Concepts touched

- [Whole-body control](../concepts/robotics/whole-body-control.md) — BB is a general WBC method (new concept page).
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — delta-action modeling (ASAP-style).
- [Imitation learning](../concepts/learning/imitation-learning.md) — DAgger distillation; [self-supervised learning](../syntheses/curriculum/curriculum-04-self-supervised-learning.md) (autoencoder-based motion clustering).

## Open questions

- **AMASS-only skills** — no loco-manipulation / object interaction (unlike [MotionBricks](motionbricks-paper.md)'s smart primitives or SONIC's foot-pedal tasks). BB is a *tracking* controller, not a task policy.
- **Code/checkpoints** — project page listed ([beingbeyond.github.io/BumbleBee](https://beingbeyond.github.io/BumbleBee/)); release status not verified from the PDF.
- **Comparison basis** — baselines re-implemented/adapted to G1; not all data-matched to the original papers.
