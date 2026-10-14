---
title: "Three ways to scale a JEPA world model — RoboJEPA, H-JEPA, DeepJEPA (autumn 2026)"
type: synthesis
created: 2026-10-13
updated: 2026-10-13
tags: [jepa, world-model, scaling-laws, hierarchical-planning, test-time-compute, robojepa, h-jepa, deepjepa, leworldmodel, v-jepa-2, cem, evaluation, synthesis]
---

# Three ways to scale a JEPA world model — RoboJEPA, H-JEPA, DeepJEPA (autumn 2026)

In the space of eight days (30 Sept – 7 Oct 2026), three groups in the LeCun lineage published three different answers to one question: **once an action-conditioned JEPA can plan, what do you scale to make it plan better?**

| | **[RoboJEPA](../../entities/robojepa.md)** | **[H-JEPA](../../entities/h-jepa.md)** | **[DeepJEPA](../../entities/deepjepa.md)** |
|---|---|---|---|
| Group | Meta FAIR (Zholus … Bohg, Ballas, Assran) | NYU / AMI (Zhang, Terver … LeCun, Balestriero) | NYU, MIT, Stanford … (Jin, Zhang … Pavone) |
| **What it scales** | **Predictor size and training compute**: 22M → 8B | **Depth of hierarchy**: 1 → 4 levels, each with its own latent | **Compute per imagined step**: 1 → 4 recurrent updates, chosen adaptively |
| Kind of scaling | training-time | architecture | test-time, inside the transition |
| Encoder | frozen V-JEPA 2.1-G | trained end to end (LeWM, ViT-Tiny/S) | trained end to end (LeWM-style) |
| Data | 2.87M episodes, 12 embodiments | one dataset per model (DROID for real) | simulated tasks |
| Planner | CEM, single goal image | gradient descent, top-down subgoals | CEM |
| Strongest result | fitted law extrapolates 2B → 8B; capabilities at compute thresholds | AntMaze **18% → 73%** at lower planner compute | uniform depth never helps; adaptive depth is compute-neutral |
| Real robot | **closed loop**, Franka, 3 tasks, n=30 | offline only (16 DROID clips) | none |
| Weakest point | Pick and Place flat with size and below π0.5 | abstraction needs a >2× timescale gap that manipulation data lacks | gains within noise; thresholds tuned on the evaluation sweep |

Sources: [RoboJEPA paper](../../sources/robojepa-scaling-robotic-latent-world-models-paper.md) · [H-JEPA paper](../../sources/h-jepa-hierarchical-world-models-paper.md) · [DeepJEPA paper](../../sources/deepjepa-scaling-world-models-from-within-paper.md).

## What all three found: scaling helps only when it matches how the model is used

Each paper's naive version of its own axis failed, and each fixed it the same way: by aligning what is scaled with what the **planner** consumes.

- **RoboJEPA.** With 2-step rollout training, more compute did **not** buy long-horizon planning; a 300M model beat a 1B model on obstacle-reach. Training on **10-step rollouts**, which is how the planner uses the model, restored a clean scaling curve and lowered the fitted error floor.
- **H-JEPA.** Stacking levels helps partly through **where goal distance is measured**. Level-1 latent distance is nearly flat far from the goal, which gives a planner nothing to descend. Scoring the *same* flat rollouts in a higher level's latent raises success with no change to the dynamics.
- **DeepJEPA.** More predictor depth everywhere **did not help, and sometimes hurt** (K = 4 never beat K = 1). The useful compute is the small fraction that can **change which CEM candidates make the elite set**. Its Prop. 3.1 makes this exact: if an update's largest cost correction is under half the elite margin, the planner's decision cannot change.

The common lesson: **"better prediction" is not the target, "a better decision" is.** RoboJEPA measures it as planning success tracking rollout error, H-JEPA as cost geometry, DeepJEPA as rank changes. All three find that average prediction quality is a weak proxy. DeepJEPA's probes show refinement leaves state decodability unchanged. H-JEPA's Fréchet metric is "necessary, not sufficient" for grasp success. RoboJEPA's loss law holds while Pick and Place success stays flat. This strengthens the [world-model evaluation](../../concepts/world-models/world-model-evaluation.md) position that a world model is graded by the planner it serves.

## What each found about its own ceiling

| | Ceiling | Evidence |
|---|---|---|
| RoboJEPA | **Data.** Fitted irreducible error ~0.2 (DROID), and the frontier nears it at 8B | Authors: *"more and more diverse interaction data rather than parameters alone"* |
| H-JEPA | **Timescale separation and episode length.** No abstraction below a ~2× fast/slow gap; deep levels starve on short episodes (Push-T at 3 levels sees 58% of the clips) | Fig. 5, Table 3 |
| DeepJEPA | **The search boundary.** 93–99% of episodes have the same outcome at any depth | Fig. 5 |

None of the three ceilings is model capacity. Robotics scaling pages have now reached this conclusion three times over: [EgoScale](../../sources/egoscale-paper.md) and X-VLA on the policy side ([scaling laws](../../concepts/learning/scaling-laws-vla.md)), and RoboJEPA on the world-model side.

## The encoder split, and the collapse each side hits

The deepest disagreement is whether the encoder is **frozen** or **trained**:

- **Frozen (RoboJEPA).** It inherits internet-scale video features and removes encoder collapse by construction, which is what lets the predictor reach 8B. But the predictor collapsed at scale when the frozen encoder was **V-JEPA 2**, and only V-JEPA 2.1, with far better *dense* features, scaled cleanly ([App. K](../../sources/robojepa-scaling-robotic-latent-world-models-paper.md)). The choice of frozen encoder decides whether scaling works at all.
- **Trained (H-JEPA, DeepJEPA).** Small, cheap and adaptable, with representation that can become abstract per level. But in scenes that change between episodes it falls into **[slow-feature collapse](../../concepts/world-models/slow-feature-collapse.md)**: it learns the room, not the arm. H-JEPA proves no distribution-level regulariser (SIGReg included) prevents this; only an inverse-dynamics term, which needs action labels, does.

So both sides need the same thing from data: **actions, and enough scene variety to be worth learning from**. The frozen side has to choose its encoder well. The trained side has to pay for action-labelled data and IDM.

## Do the axes compose?

In principle they are orthogonal: size per level × number of levels × compute per step. In practice nobody has combined them, and there are concrete obstacles:

- **RoboJEPA as H-JEPA's level 1.** H-JEPA's upper levels are trained *through* the lower encoder, end to end. A frozen 8B-predictor base would force the **stagewise** variant (train level 1, freeze it, train level 2 on its latents). H-JEPA used that variant only for analysis, not headline results. Whether a frozen V-JEPA 2.1 latent shows the >2× timescale separation that abstraction needs is unknown.
- **DeepJEPA depth inside each H-JEPA level** is architecturally easy. But H-JEPA plans by gradient descent, and DeepJEPA's mechanism and theory are about **CEM elite sets**, so the elite-margin argument doesn't transfer to a gradient planner directly.
- **DeepJEPA-style allocation inside RoboJEPA** is the most natural pairing, since both use CEM. Its value depends on wall-clock, and DeepJEPA states that sparse depth does **not** reduce wall-clock under batched CEM. At 8B and several seconds per plan, that is the binding constraint.

## Evidence quality

Read the three as one strong result, one strong-but-simulated result, and one mechanism paper.

- **RoboJEPA** has the largest evaluation (50,000+ planning episodes, held-out extrapolation, released checkpoints), but its real-robot cells are n=30, and only two of three tasks show the size trend ([success-rate audit](../platforms/vla-success-rate-audit.md)).
- **H-JEPA** has the cleanest protocol: separate sweep and evaluation task sets, settings frozen before evaluation, DROID clips held out of training, and metric calibration against simulated success. But the large effect (AntMaze) is simulated, and the real-data effect is ~5 offline points on 16 clips.
- **DeepJEPA** reports its own null (p = 0.42 on the 450-pair replication) and its threshold-selection caveat. Its value is the mechanism (contact-aligned compute, the elite-margin rule), not the scoreboard.

## What this changes in the wiki's open questions

- **[Open question #2, long-horizon hierarchical planning](open-questions-and-research-direction.md).** It moves from "HWM exists" to "the representational half exists, in simulation." The next experiment the field needs is the one H-JEPA's conclusion names: **closed-loop H-JEPA on hardware**.
- **Open question #7, evaluation.** All three give a reason to grade world models by **planner outcome or ranking** rather than prediction loss. DeepJEPA's elite margin and H-JEPA's action sensitivity (rollout change when actions are swapped) are two cheap diagnostics anyone can log.
- **For a small-budget, real-robot JEPA project**, the practical reading is:
  1. Record actions with every episode and use an IDM term, or a multi-room home will collapse the encoder.
  2. Train on rollouts as long as the planner's horizon.
  3. Measure goal distance in an abstract (upper-level or projected) latent before adding planner compute.
  4. RoboJEPA's released **small checkpoints** (22M–300M; Grasp 27–37% zero-shot on a Franka) are the only ones of the three trained on real multi-embodiment data, including SO-101 episodes. That makes them a candidate frozen base for fine-tuning, though not on-device at the large end.

  See [JEPA for a household mobile manipulator](jepa-for-household-mobile-manipulator.md).

## Related
- [JEPA](../../concepts/world-models/jepa.md) · [SIGReg](../../concepts/world-models/sigreg.md) · [Slow-feature collapse](../../concepts/world-models/slow-feature-collapse.md) · [Gradient-based planning](../../concepts/world-models/gradient-based-planning.md) · [Adaptive depth reasoning](../../concepts/learning/adaptive-depth-reasoning.md) · [Scaling laws](../../concepts/learning/scaling-laws-vla.md)
- [HWM](../../entities/hwm.md) · [LeWorldModel](../../entities/leworldmodel.md) · [V-JEPA 2](../../entities/v-jepa-2.md) · [JEPA-WMs](../../entities/jepa-wms.md)
- [Generative-video vs JEPA world models](generative-video-vs-jepa-world-models.md) · [What world models are measurably good for](what-world-models-are-measurably-good-for.md) · [The anti-collapse lineage](ssl-anti-collapse-lineage.md)

## Sources used in this synthesis
- [RoboJEPA: Scaling Robotic Latent World Models](../../sources/robojepa-scaling-robotic-latent-world-models-paper.md) (2026-10-07)
- [H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning](../../sources/h-jepa-hierarchical-world-models-paper.md) (2026-10-05)
- [DeepJEPA: Scaling World Models from Within](../../sources/deepjepa-scaling-world-models-from-within-paper.md) (2026-09-30)
- [HWM paper](../../sources/hwm-paper.md), [EgoScale paper](../../sources/egoscale-paper.md) — context.
