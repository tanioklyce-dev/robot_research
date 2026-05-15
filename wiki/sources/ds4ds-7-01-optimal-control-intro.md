---
title: "DS4DS 7.01 — Optimal control, Introduction (Peitz & Wallscheid, YouTube, Jan 2024)"
type: source
url: https://www.youtube.com/watch?v=6GSHAoLMsXs
course_url: https://www.youtube.com/@DataScience4DynamicalSystems/playlists
course_repo: https://github.com/DS-4-DS/DS4DS_Course
author: Sebastian Peitz, Oliver Wallscheid
affiliation: Data Science for Dynamical Systems (DS4DS) — open-education initiative; Peitz at TU Dortmund, Wallscheid at U Siegen / Paderborn
published: 2024-01-21
ingested: 2026-05-14
created: 2026-05-14
updated: 2026-05-14
license: CC BY-SA 4.0 (course materials); Julia / Jupyter notebooks on GitHub
tags: [optimal-control, video, pedagogical, ds4ds, peitz, wallscheid, julia, jupyter, mpc, dynamical-systems, curriculum-module-10]
---

> [!note] Ingest depth
> Source-page metadata gathered from the YouTube URL, the DS4DS playlist page, and the [DS-4-DS/DS4DS_Course GitHub repo](https://github.com/DS-4-DS/DS4DS_Course) (CC BY-SA 4.0; Julia / Jupyter notebook companion materials). Video itself not transcribed in this ingest — this is a **summary-level pointer** to the canonical modern-pedagogy companion to the [Sussmann & Willems 1997 historical essay](sussmann-willems-1997-300-years-optimal-control.md).

## Summary

**"Optimal control - Introduction (DS4DS 7.01)"** — Sebastian Peitz and Oliver Wallscheid, *Data Science for Dynamical Systems*, YouTube, posted **2024-01-21**. The opening lecture of **Module 7 — Optimal Control** in the DS4DS open-education course. The course bridges classical control engineering and modern data-driven / machine-learning approaches; Module 7 is the seven-lesson optimal-control unit:

- **7.01 — Introduction** (this video — definitions, problem class, motivation)
- 7.02 — Optimal control in discrete time
- 7.03 — Optimal control of linear systems 1: Dynamics
- 7.04 — Optimal control of linear systems 2: (LQR / Riccati equation, per playlist context)
- 7.05 — Optimal control of linear systems 3: Example
- 7.06 — Linear model predictive control
- 7.07 — Data-driven model predictive control using DMD
- 7.08 — Differential predictive control: Introduction
- 7.09 — Differential predictive control: Global vs. local optima

Each lecture is paired with a Julia/Jupyter notebook in the [GitHub course repo](https://github.com/DS-4-DS/DS4DS_Course) under **CC BY-SA 4.0**. The eight-module course as a whole covers dynamical modeling, linear identification, ML optimization, nonlinear identification, feature engineering, model selection, control, and Koopman-operator methods.

## Why it matters to this wiki

- **The modern-pedagogy companion to [Sussmann & Willems 1997](sussmann-willems-1997-300-years-optimal-control.md).** Where the Sussmann–Willems essay is the **historical retrospective** (Bernoulli → Euler–Lagrange → Hamilton–Jacobi → Pontryagin), DS4DS 7.01–7.09 is the **forward-looking computational treatment** — discrete-time formulation, LQR, MPC (linear and data-driven), differential predictive control. Together they form a complete optimal-control orientation: history + theory + computational practice.
- **MPC primary-source pedagogy.** [MPC](../glossary.md#mpc) is invoked across the wiki — [LeWM](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md), [V-JEPA 2-AC](../entities/v-jepa-2.md), [TD-MPC2](td-mpc2-paper.md), [Curriculum Module 10](../syntheses/curriculum-10-world-models.md) — without a dedicated MPC pedagogical source. DS4DS 7.06 (Linear MPC) and 7.07 (Data-driven MPC via DMD) fill that gap.
- **Bridge to Koopman-operator methods.** The DS4DS course's Koopman module is relevant to the wiki's growing world-model / learned-dynamics thread — a candidate future ingest once Koopman comes up in a wiki-tracked paper.
- **Open-education provenance.** CC BY-SA 4.0 + Julia / Jupyter makes this resource directly usable for the wiki's curriculum-companion role (cf. [karpathy/nanoGPT](karpathy-nanogpt.md), [karpathy/micrograd](karpathy-micrograd.md), [karpathy/nanochat](karpathy-nanochat.md), [karpathy/autoresearch](karpathy-autoresearch.md) as the same archetype).

## Course context

**DS4DS — Data Science for Dynamical Systems** is an open-education initiative addressing the intersection of control engineering and machine learning. Course materials (videos + Jupyter notebooks + slides) are MIT-license-spirit (CC BY-SA 4.0) and hosted on YouTube + GitHub. The eight-module structure:

1. Dynamical modeling fundamentals
2. Linear system identification
3. Machine-learning optimization
4. Nonlinear system identification
5. Feature engineering
6. Model selection
7. **Optimal control** (this module — 7.01 is the introductory lecture)
8. Koopman-operator methods

Module 7 enters where it does because it depends on modules 1–6 (need a dynamical model + ML toolbox before you can do data-driven control).

## Authors

- **Sebastian Peitz** — TU Dortmund, Computer Science. Research focus: dynamical systems, control, ML for PDEs, Koopman operators.
- **Oliver Wallscheid** — U Siegen (formerly U Paderborn). Research focus: control engineering, electric drives, reinforcement learning for power-systems control.

Neither has a wiki entity page; candidate stubs if a future control-theory thread accumulates more sources from either author.

## Entities mentioned (in the broader DS4DS module 7 series)

- **LQR (Linear Quadratic Regulator)** — covered in 7.03–7.05; the canonical analytic solution for linear-dynamics + quadratic-cost optimal control. Not yet a wiki concept page; would hub from this source.
- **DMD (Dynamic Mode Decomposition)** — covered in 7.07; data-driven dynamics identification compatible with linear MPC. Methodologically adjacent to [TD-MPC](../entities/td-mpc.md)'s learned-latent-dynamics line.
- **Koopman operator** — the DS4DS course's module 8 topic; lifts nonlinear dynamics to a linear operator on an observable-function space. Increasingly relevant to ML-for-dynamics research; not yet on the wiki.

## Concepts touched

- **Optimal control** — already covered in [Sussmann & Willems 1997](sussmann-willems-1997-300-years-optimal-control.md). This video is the computational-pedagogy entry point.
- **[MPC](../glossary.md#mpc)** — receding-horizon optimal control; DS4DS 7.06 + 7.07 cover linear + data-driven variants.
- **LQR** — analytic optimal control for linear-quadratic problems. The "easy case" that motivates everything else.
- **DMD / Koopman** — data-driven dynamics identification.

## Curriculum hookup

This video and the surrounding DS4DS module 7 series are a strong **recommended-viewing companion** for [Curriculum Module 10 — World models, broad](../syntheses/curriculum-10-world-models.md), where MPC + CEM + gradient-based planning over a learned WM are covered conceptually but without a controls-theory pedagogical anchor. Module 10's existing "Recommended reading" list can pick up DS4DS 7.06 (Linear MPC) and 7.07 (Data-driven MPC) as the controls-side companions to the WM-side coverage.

Also relevant as background for [Module 8 — Reinforcement learning vocabulary](../syntheses/curriculum-08-rl-vocabulary.md), where MBRL / Dreamer-class methods can be framed as "RL doing approximate optimal control over a learned model."

## Position in the lineage

```
1696   Bernoulli — brachystochrone
1956   Pontryagin et al. — Maximum Principle
1960   Kalman — LQR + Kalman filter
1970s  Model Predictive Control as industrial-process technology
2000s  Nonlinear MPC, real-time MPC, NMPC software (CasADi, ACADO)
2014+  Koopman / DMD for data-driven dynamics
2022+  Learned-WM + MPC: TD-MPC, DreamerV3, LeWM, DINO-WM, V-JEPA 2-AC
2024   DS4DS 7.01 — this video; CC BY-SA 4.0 modern-pedagogy course
```

## Open questions / TBD

- **Detailed transcript / timestamp ingest.** This is a summary-level pointer. A future watch-through pass with timestamps would let the wiki cite specific definitions / formulas from the video (especially 7.06 LMPC for cross-linking with [TD-MPC2](td-mpc2-paper.md)).
- **The DS4DS Julia notebooks** are a candidate for a hands-on supplement to the curriculum — particularly Module 10's MPC section. Worth a follow-up evaluation pass.
- **Koopman operator methods (DS4DS module 8)** — not yet ingested but increasingly cross-relevant to the world-model literature. Logged.
- **An `entities/data-science-for-dynamical-systems.md` stub** — would let future ingests from the course attach cleanly. Defer until a second DS4DS lesson is ingested.
- ✅ **Resolved 2026-05-14:** A wiki [`concepts/optimal-control.md`](../concepts/optimal-control.md) hub page was created using this video as the modern-pedagogy companion, paired with [Sussmann & Willems 1997](sussmann-willems-1997-300-years-optimal-control.md) (historical anchor) and [Sutton & Barto](sutton-barto-rl-textbook.md) (RL bridge).
