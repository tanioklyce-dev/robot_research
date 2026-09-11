---
title: GNM — A General Navigation Model to Drive Any Robot (Shah, Sridhar, Bhorkar, Hirose, Levine; ICRA 2023)
type: source
url: https://arxiv.org/abs/2210.03370
fetch_url: https://arxiv.org/pdf/2210.03370v2
author: Dhruv Shah, Ajay Sridhar, Arjun Bhorkar, Noriaki Hirose, Sergey Levine
published: 2022-10-07
ingested: 2026-09-11
venue: ICRA 2023 (arXiv v2, 2023-05-22)
local_path: raw/2210.03370v2.pdf
sha256: 18b4f3c35feb35874d6db54d5f3f0eca9535c546877cfa747a3524fc5f841c3a
format: pdf (8 pp.)
tags: [gnm, navigation, visual-navigation, cross-embodiment, omnipolicy, image-goal, topological-memory, berkeley, rail, shah, hirose, levine, dataset-mixture, normalized-actions]
---

## Summary

The paper that started Berkeley RAIL's open navigation line and defined the **GNM dataset mixture** every successor trains on. Its question is whether one **"omnipolicy"** can be trained on navigation data from many structurally similar robots and drive new ones. The answer is yes, with two cheap design choices doing all the work: a **shared, normalized action space** (relative waypoints scaled by each robot's top speed, plus yaw and a predicted temporal distance) and an **embodiment context** (the last k = 5 frames, from which the policy infers what body it is in). Trained on ~60–70 h from six robots spanning 0.2–10 m/s, the same weights drive a LoCoBot, a Jackal, a custom Roomba-based Vizbot and — with no aerial data at all — a **DJI Tello quadrotor** constrained to a plane, beating the best single-robot policy on every platform and proving robust to clipped steering, a moved camera, and physical damage. The authors are explicit that the contribution is empirical, not algorithmic: "a set of relatively simple decisions… is sufficient to enable broad generalization from heterogeneous data."

## Key claims

### The dataset (Table I)

| Dataset | Platform | Top speed | Hours | Environment |
|---|---|---|---|---|
| GoStanford | TurtleBot2 | 0.5 m/s | 14 | office |
| RECON | Jackal | 1 m/s | 25 | off-road |
| CoryHall | RC car | 1.2 m/s | 2 | hallways |
| Berkeley | Jackal | 2 m/s | 4 | suburban |
| SCAND-S / SCAND-J | Spot / Jackal | 1.5 / 2 m/s | 8 / 1 | sidewalks |
| Seattle | Warthog | 5 m/s | 1 | off-road |
| TartanDrive | ATV | 10 m/s | 5 | off-road |
| NeBula | ATV | 10 m/s | 10 | off-road |

> [!note] 60 or 70 hours
> The abstract and text say "60 hours"; Table I's rows sum to **70 h** and its caption says 70. Later papers cite "~60 h." Forward-facing monocular RGB paired with commanded actions and local odometry is the only common denominator; camera intrinsics and mounting differ per robot and are not homogenized.

### Design choices and their ablations (Table V, LoCoBot, unseen robot)

- **Action space.** Normalized waypoints **1.0 / 0.95** (easy / moderate environments) vs raw velocities 0.73 / 0.54 vs unnormalized waypoints 0.42 / 0.26. Velocities work in easy rooms and fail on sharp turns; normalization by top speed is what lets a 0.5 m/s TurtleBot and a 10 m/s ATV share a policy.
- **Embodiment context.** On hard environments (up to 50 m, tight passages): none 0.36, static k past frames 0.5, **temporal k = 5 consecutive frames 0.7**. The temporal variant wins because speed and turning radius are visible in consecutive frames.
- **Goal-conditioning architecture.** Conditioned (separate MobileNetv2 encoders for {o_t, C_t} and goal, with an observation pathway to the head) **1.0 / 0.95** vs Siamese 0.73 / 0.26 vs channel-stacked 0.52 / 0.72.
- Images are **85 × 64**; the policy predicts τ = 5 normalized waypoints and a temporal distance used as the edge weight of a topological graph (ViNG-style), planned with Dijkstra.

### Results

- **Table II — one GNM-Mid policy vs the best single-robot policy (mean progress toward goal):** LoCoBot 0.96 vs 0.62; **Tello 0.99 vs 0.79** (no aerial training data); Vizbot 0.93 vs 0.51; Jackal 0.94 vs 0.68.
- **Data scaling (Tables III–IV, 20 environments):** on the LoCoBot, GoStanford-only 0.25 / 0.16 / 0.44 (indoor easy / moderate / outdoor) → GNM-Small (2 datasets) 0.82 / 0.59 / 1.0 → GNM-Large (6) 1.0 / 1.0 / 0.83. On the Jackal, RECON-only is 0.67 outdoor-easy but 0.36 indoor; GNM-Large 1.0 / 1.0 / 0.88. Adding off-road ATV data helps an indoor LoCoBot.
- **Robustness (Fig. 5):** clipped steering 0.89 vs 0.30 single-domain; perturbed camera 0.81 vs 0.17; physical damage during navigation 1.0 vs 0.81.
- ImageNet-pretrained single-dataset policies "improve a bit but still struggle" — task-relevant cross-robot data beats generic visual pretraining.

### Stated limitations

All robots are assumed to be ground robots with a forward RGB camera; capability differences beyond speed and steering (traversability, sensors) are not modeled; "our dataset could be much larger."

## Reading it against the wiki

- **The normalized-waypoint action space is the whole cross-embodiment trick**, and it is why navigation transfer is cheap where manipulation transfer is not — see [visual navigation policies](../concepts/robotics/visual-navigation-policies.md) and contrast with [latent action tokens](../concepts/learning/latent-action-tokens.md), which exist because manipulation has no such shared low-dimensional space.
- **Embodiment context from k past frames** is the navigation-side version of RMA's extrinsics-from-proprioception ([RMA](rma-paper.md)): infer the body from recent observations rather than declare it.
- The scaling table is an early **"more heterogeneous data beats more in-domain data"** result, three years before the same claim at VLA scale ([OXE](../entities/open-x-embodiment.md)).
- Success is "mean progress toward goal" — a partial-credit metric, the ancestor of MBRA's coverage rate.

## Entities mentioned

- [Dhruv Shah](../entities/dhruv-shah.md), [Noriaki Hirose](../entities/noriaki-hirose.md), [Sergey Levine](../entities/sergey-levine.md); Ajay Sridhar, Arjun Bhorkar.
- Platforms: [Spot](../entities/spot.md) (SCAND-S data), Clearpath Jackal and Warthog, TurtleBot2, LoCoBot, Vizbot, DJI Tello (no pages).

## Concepts touched

- [Visual navigation policies](../concepts/robotics/visual-navigation-policies.md), [imitation learning](../concepts/learning/imitation-learning.md), [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md).

## Open questions

- The 60-vs-70 h discrepancy is never resolved in later papers.
- Whether embodiment context actually encodes dynamics or just camera height — no probe.
