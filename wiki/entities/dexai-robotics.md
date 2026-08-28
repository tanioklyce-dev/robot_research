---
title: Dexai Robotics
type: entity
subtype: company
created: 2026-08-16
updated: 2026-08-16
sources: 3
tags: [dexai-robotics, food-robotics, gcs, graphs-of-convex-sets, motion-planning, deployment, boston, collaborative-robots, raas, arm-institute]
---

# Dexai Robotics

Boston-area food-preparation robotics company — **the wiki's only confirmed production user of [GCS](../concepts/robotics/graphs-of-convex-sets.md) trajectory optimization**, having replaced a tuned PRM planner with GCS in a shipping product.

## Why this page exists

Because it answers a question the [GCS paper ingest](../sources/gcs-motion-planning-paper.md) left open — *did GCS reach deployment?* — and answers it with a name, a predecessor, and a regime.

> *"Dexai is a local company. We had a project with them. They're doing food preparation… they make salad bowls and things like this with robots. And so they switched from their pretty optimized — this is like **time is money** for these guys — **PRM-based planner. Now they're using GCS in production**. And they were pretty happy with how that worked."*
> — [Tedrake, MIT Robotics Seminar, 2024-04-07](../sources/tedrake-gcs-foundation-models-talk.md) (34:13)

Corroborated by the [ARM Institute project page](../sources/arm-institute-gcs-dexai-project.md) (2024-02-26), which lists Dexai as **PI** on a 2023 Technology Project Call award with MIT, reports the work *"transitioned into commercial use"* on robots assembling meals *"in the lab and at multiple customer sites across the nation,"* claims a **return exceeding $10,000/robot/year**, and names five delivered modules: `RobotModel`, `RobotConstraints`, `IrisBuilder`, `GcsPlanner`, `WarmGcsPlanner`.

**The displaced baseline is what makes this a real datapoint.** GCS did not replace nothing; it replaced a *"pretty optimized"* PRM in a system where cycle time is revenue. That is the same comparison the paper ran on a 7-DoF iiwa — including against shortcut-PRM, the version practitioners actually deploy — and it survived contact with a customer.

## Why the fit is this good, and why that limits the lesson

Every restriction the [GCS paper](../sources/gcs-motion-planning-paper.md) states is free in a food-assembly cell:

| GCS limitation | Why it costs nothing here |
|---|---|
| Convex decomposition is a manual, offline **input** | Fixed workcell — seed once, amortize over months |
| Multi-query only pays with reuse | Thousands of bowls a day against one graph |
| **No dynamics** | Utensil transit at modest speed; kinematic plan + tracking controller suffices |
| **No contact**, **no task-space constraints** | Scooping is scripted at the endpoints; the planner handles the transit |
| Optimality is the selling point | Cycle time *is* the customer's metric |

Tedrake generalizes the regime as the logistics case — *"you're going to be making plans all day long, you're willing to precompute once"* — and says the answer *"change[s] completely"* for a mobile manipulator that is not chasing time-optimality. So Dexai is best read as **proof that the niche is real and monetizable**, not as evidence that GCS is becoming general infrastructure.

## Company facts

> [!note] Live-web facts, not from an ingested source
> Founded **2018** as a spin-out of **Draper** (Charles Stark Draper Laboratory, Cambridge MA) by David M.S. Johnson and Anthony Tayoun; headquartered in Boston. Product is **Alfred**, a collaborative arm that uses **standard kitchen utensils** as end effectors to assemble bowls and salads, sold **robotics-as-a-service** (per-dish fee) and pitched as drop-in for existing kitchens. Customers reported include restaurants, military bases, and corporate cafeterias; ~$12M raised. None of this is confirmed by an ingested source, and the ingested sources never name Alfred — they say only "robots assembling meals."

The **utensil-as-end-effector** detail, if accurate, is worth holding: it is a manipulation problem deliberately engineered so that the hard part is *reaching*, not *grasping* — which is precisely the problem GCS solves optimally and the one it cannot extend to.

## Related

- [Graphs of convex sets (GCS)](../concepts/robotics/graphs-of-convex-sets.md) — the planner it runs.
- [Drake](drake.md) — where the mature GCS implementation lives.
- [Russ Tedrake](russ-tedrake.md) — MIT side of the collaboration; the source of the deployment claim.
- [Motion planning (classical)](../concepts/robotics/motion-planning.md) — the PRM it replaced.
- [Collaborative robots](../concepts/robotics/collaborative-robots.md) — the product category.

## Mentioned in

- [Planning with Graphs of Convex Sets (in the age of foundation models)](../sources/tedrake-gcs-foundation-models-talk.md) — the production-use claim.
- [Time-Optimal Motion Planning Using Convex Sets (ARM Institute)](../sources/arm-institute-gcs-dexai-project.md) — project PI; ROI figure and module list.
