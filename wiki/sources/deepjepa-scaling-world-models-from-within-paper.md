---
title: "DeepJEPA: Scaling World Models from Within (Jin, Zhang et al., 2026)"
type: source
url: https://arxiv.org/abs/2610.00368
local_path: raw/2610.00368v1.pdf
sha256: 05886ccdf02d98b4c48508613f410cb812b6619779479f15d7e529bb12e0f61a
author: Zijian Jin, Yunbei Zhang, Yuanzhe Liu, Ming Liu, Baian Chen, Weirui Ye, Shilong Liu, Marco Pavone
published: 2026-09-30
ingested: 2026-10-13
venue: arXiv (cs.RO), v1
format: "paper, 18 pp (11 main + appendices A–D). NYU, Tulane, UIUC, Princeton, MIT, Columbia, Stanford. Project site deepjepa.github.io."
tags: [deepjepa, jepa, world-model, leworldmodel, test-time-compute, adaptive-computation, cem, metareasoning, pusht, ogbench-cube, simulation-only]
---

# DeepJEPA: Scaling World Models from Within (Jin, Zhang et al., 2026)

## Summary

World-model planners usually spend extra test-time compute *outward*: more candidates, longer horizons, more CEM iterations. DeepJEPA adds an *inward* axis. Each imagined transition in a [LeWorldModel](../entities/leworldmodel.md)-style action-conditioned JEPA becomes a **weight-tied recurrent cell** that can refine its prediction up to K_max = 4 times. A learned **continue head** decides, for each candidate and rollout step, whether another update is worth computing. It is trained only on whether the next update reduces latent prediction error by more than a relative threshold; no reward or contact labels are used. The framing is **rational metareasoning**: an internal update is worth what it changes in the planner's chosen action. A simple result (Prop. 3.1) makes this concrete. If the largest cost correction from one more update is less than half the gap between the worst elite and the best non-elite, **CEM's elite set and next proposal are unchanged**, so the update had zero decision value. Empirically: (1) **uniformly deeper is not better**: K = 4 never beats K = 1 in aggregate across five tasks; (2) adaptive depth matches or edges out the best fixed depth at an average of **1.00–1.26 updates per transition**; (3) the extra updates **concentrate at contact onset and sustained contact**, which the head was never told about; (4) the gains come from **re-ranking candidates near the elite boundary**, not from better object-state decodability. All results are in simulation.

## Key claims

**Setup**: Reacher; visual OGBench Cube Single, Double and Triple; PushT at H = 10. Three train/eval seed pairs × 50 episodes = **150 episodes per cell**. The fixed-K arms and the adaptive arm share a checkpoint family, episode roots and CEM seeds. LeWM is a separate non-recurrent baseline, and candidates are scored exactly as in LeWM. Context L = 3, K_max = 4, τ_rel = 5×10⁻⁴.

**Table 1 (mean success %)**

| | Reacher | Cube Single | Double | Triple | PushT |
|---|---|---|---|---|---|
| LeWM | 81.3 | 72.0 | **74.7** | 74.0 | 10.4 |
| K=1 | 84.0 | 79.3 | 72.0 | 74.0 | 10.7 |
| K=4 | 82.7 | 78.0 | 72.0 | 74.0 | 9.8 |
| **DeepJEPA** | **85.3** | 79.3 | 74.0 | **77.3** | **11.6** |
| mean depth K̄ | 1.03 | 1.00 | 1.26 | 1.22 | 1.02 |

- **Uniform depth is non-monotonic**: e.g. Reacher 84.0 / 82.0 / 83.3 / 82.7 for K = 1–4.
- **The threshold controls allocation, not average depth**: on Cube Double, cutting K̄ from 1.78 to 1.26 *raises* success (Table 2).
- **Where it thinks** (100 roots/task, one checkpoint): on PushT, refinement beyond K = 1 jumps from **1.24% just before contact to 9.02% at onset** (95% CI 5.0–13.9). On Cube Triple, sustained contact gives **+12.5 pp** (CI 2.8–22.6), release −9.9 pp, onset +6.0 (CI crosses zero), after controlling for rollout step, distance and action norm.
- **How it changes decisions**: **93–99% of roots have the same outcome at K = 1 and K = 4**. On Cube Triple, 5 helped and 5 harmed out of 150. Re-running with three search seeds per root (450 pairs): K=4 − K=1 = **+1.1 pp, CI [−1.3, +3.6], p = 0.424**. On the ten discordant roots, re-sampling the search reversed the flip in 5 of 30 trials. The authors' reading: depth matters only when the sampled population sits near a ranking boundary, and **CEM amplifies small cost corrections into different actions**.
- **Not better state features**: MLP-probe object and pusher position errors move by **0.01 px** (PushT) and by **−1.7 µm** (Cube Triple, the wrong direction).

**Limitations (App. D, authors')**: halting thresholds are **selected on the test sweep, not on held-out validation**, so the numbers describe the attainable frontier, not a deployable rule. Contact and probe studies use one checkpoint. Mean depth is not wall-clock: under batched CEM, a few continuing candidates keep the cost of a synchronised update. PushT success is low in absolute terms.

## Reading it critically

> [!warning] The headline gains are inside the noise, and the paper's own replication says so
> At 150 episodes per cell, a 95% interval on a ~75% rate is about ±7 points. The adaptive gains over the best fixed depth are **+1.3, 0, +1.3, +3.3 and +0.9 points**, all inside it. The η threshold was then **chosen per task on the same evaluation sweep**, which inflates the adaptive arm by construction. On Cube Double, LeWM (74.7) beats DeepJEPA (74.0). The 450-pair replication of K = 4 vs K = 1 crosses zero (p = 0.42). Read "improves the fixed-depth frontier on four of five settings" as **"matches it at ~1.0–1.3× the compute of K=1"**: a compute-neutrality result, not a performance one. The authors' limitations section says nearly this.

- **The mechanism findings stand on their own and are the real contribution.** (a) **Uniform depth can hurt.** Extra predictor compute reorders CEM costs without making the ranking better; the K-sweep's non-monotonicity is clean evidence. (b) **Compute follows contact**, an unsupervised event detector learned from prediction-error improvement alone. (c) **Prop. 3.1** names a quantity, the **elite margin**, that any world-model planner could log to know when the model's precision can no longer change its decision.
- **PushT at ~10% is far below other LeWM PushT figures in the wiki** (for example, 50.8% base in [stable-worldmodel](stable-worldmodel-paper.md)). This is plausibly a harder variant (H = 10 with a different task construction), but the paper doesn't reconcile it. Don't compare these absolute numbers across papers.
- **Planner-relative evaluation of world models** is the transferable idea. It agrees with RoboJEPA's choice of downstream success over offline loss as the final arbiter, and with the [world-model evaluation](../concepts/world-models/world-model-evaluation.md) theme that average prediction error is the wrong target.

## Entities mentioned
- [DeepJEPA](../entities/deepjepa.md) · [LeWorldModel](../entities/leworldmodel.md) · [V-JEPA 2](../entities/v-jepa-2.md) · [Marco Pavone](../entities/marco-pavone.md)

## Concepts touched
- [Adaptive depth reasoning](../concepts/learning/adaptive-depth-reasoning.md) — the same "spend compute where the scene changes" principle, inside a world model.
- [JEPA](../concepts/world-models/jepa.md) · [World-model evaluation](../concepts/world-models/world-model-evaluation.md) · [Gradient-based planning](../concepts/world-models/gradient-based-planning.md) (the CEM side of the solver debate).

## Open questions
- With held-out threshold selection and more episodes, is there any success gain, or only compute neutrality?
- Wall-clock: can batched CEM exploit sparse depth (ragged batches, candidate compaction)?
- Training the continue head on the decision directly (elite-margin or action-sensitivity targets), which the authors propose.
- Does contact-aligned depth show up on real-robot data, where contact is where world models fail most?
