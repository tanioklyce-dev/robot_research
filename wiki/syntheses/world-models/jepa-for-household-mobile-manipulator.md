---
title: "JEPA for a household mobile manipulator — where it fits, and where it doesn't"
type: synthesis
created: 2026-09-07
updated: 2026-09-07
tags: [jepa, world-model, household-robot, mobile-manipulation, dual-arm, assistive, safety, architecture, decision, synthesis]
---

# JEPA for a household mobile manipulator — where it fits, and where it doesn't

Written in answer to a query: *should a two-armed mobile robot doing household navigation and manipulation be controlled by a JEPA world model? If not now, eventually? And if not, what is a good approach for general, safe in-home robot AI?*

The wiki has held the pieces of this answer on a dozen pages for months without joining them. This page joins them, and the join changes the question. **"Is JEPA good for this" is the wrong unit.** The measured limits are about *roles* and *axes* — which job a learned world model is given, and which directions of variation its recipe declares irrelevant — and JEPA-vs-not is downstream of both.

> [!note] Short answer
> **Not as the controller, not today.** JEPA is a defensible bet for parts of the stack — representation, short-horizon subgoal planning, test-time adaptation — and a poor bet as the thing that drives two arms and a base around a kitchen. **"Eventually" resolves into three testable conditions**, none of which any current JEPA recipe meets. And the good approach for safe home use is **an architecture, not a model**: a deterministic physical envelope below, learned skills as primitives, an advisory orchestrator above, and authority held by the user.

## 1. Why not today — four measured limits

The wiki's one-line verdict on learned world models ([what world models are measurably good for](what-world-models-are-measurably-good-for.md)) still holds: **learned dynamics are good enough to shape a policy and not good enough to be one.** Four limits bear directly on a home robot.

### Planning horizon

[LeWorldModel](../../entities/leworldmodel.md) plans about **five prediction loops** before rollouts drift ([JEPA](../../concepts/world-models/jepa.md), H-JEPA section). Hierarchy helps, and it is the field's own prescribed fix:

| System | Result | Conditioning |
|---|---|---|
| [HWM](../../entities/hwm.md) over V-JEPA 2-AC | real Franka pick-and-place **0% → 70%** ([paper](../../sources/hwm-paper.md)) | single goal image |
| [WorldDP](../../entities/worlddp.md) | three-cube rearrangement **30%**, >2× next best ([paper](../../sources/worlddp-paper.md)) | goal state |
| Pixel world models as planner | **20–21%** vs [π0.5](../../entities/pi-zero-5.md) at 77–66% ([WorldArena](../../sources/worldarena-paper.md)) | language |

Both hierarchical systems are **two levels deep and goal-image conditioned**. Neither takes a spoken instruction. A household task — *"get my medication, open the bottle, put two pills on the tray"* — is 10+ steps with recovery, and no JEPA system in the wiki demonstrates that ([assistive landscape](../assistive/assistive-robotics-research-landscape.md), blocking problem 3).

### Robustness along the axes a home varies on

This is the limit that decides the question, and it is measured by the JEPA line's own group. [stable-worldmodel](../../sources/stable-worldmodel-paper.md) takes LeWorldModel from **50.8% to 6–26%** on Push-T under colour, size, and shape change, with distractor collapse *"quadratic across all baselines."*

[The abstraction tax](abstraction-tax.md) supplies the mechanism, and it generalizes past LeWM: a next-frame prediction objective is **paid to encode static scene attributes**, because they are the most predictable thing in the scene. Nothing in the recipe declares *this mug, not that mug* or *this lighting* irrelevant. The axes a household changes — object identity, layout, lighting, clutter, **this house not that house** — are exactly the undeclared ones.

> [!warning] The decisive point
> The relevant question for a home robot is not "JEPA or diffusion policy." It is **"what in this recipe tells the model that the kitchen is different from the one in the data?"** For every JEPA world model in this wiki the answer is *nothing about static appearance* — and, with one exception, nothing at all. [Demo-JEPA](../../sources/demo-jepa-paper.md)'s naive-reference ablation shows the same latent space failing across all tasks until a module explicitly declares embodiment a nuisance variable — one latent, two outcomes, and the difference is the declaration.
>
> **The exception, added 2026-09-07:** [SMWM](../../entities/smwm.md)'s inverse-dynamics term is a declaration by [the abstraction tax](abstraction-tax.md)'s own rule — it declares **uncontrollable variation** irrelevant, and it measurably ignores a randomly moving distractor object ([paper](../../sources/sensorimotor-world-models-paper.md)). That is a home-relevant axis: people and pets moving through the scene. What it does *not* declare is the static-attribute axis — the forward loss is still paid to encode a constant mug colour — so it does not touch the [stable-worldmodel](../../sources/stable-worldmodel-paper.md) collapse under colour, size, and shape. SMWM postdates that benchmark and **has not been run on its distractor or shift suite.** The prediction this page makes: SMWM should hold up where the distractors *move* and collapse where they are static. Untested.

### Contact and force

JEPA predicts in a **visual latent**. No JEPA model in the wiki models force, compliance, or tactile feedback ([JEPA task capabilities](jepa-task-capabilities.md)). The [contact-rich survey](../../sources/safe-learning-contact-rich-survey.md)'s definition — sustained contact with motion and force coupled — excludes simple pick-and-place and *includes* tool use and in-hand manipulation. Dishes, containers, and cleaning surfaces sit inside the included regime, where the wiki's VLA evidence is thin and its JEPA evidence is absent ([contact-rich manipulation](../../concepts/robotics/contact-rich-manipulation.md)).

On a low-cost dual-arm platform this is a cliff, not a slope. [UME](../../sources/ume-paper.md) ablates torque out of the observation and box flipping drops **0.85 → 0.00**, box pushing **0.90 → 0.50**, regardless of policy class — tasks where two visually identical states demand opposite actions are unlearnable without a force channel ([XLeRobot](../../entities/xlerobot.md), position-only ceiling).

### Language

Current JEPA models are vision-only or vision+state. [VLA-JEPA](../../entities/vla-jepa.md) and [VL-JEPA](../../entities/vl-jepa.md) exist and are immature. *"The blue mug, not the one with the chip"* is a VLA-shaped problem.

### Navigation — the half of the query this page had skipped

The query asked about navigation *and* manipulation, and the four limits above are all about manipulation. The navigation half is shorter. JEPA navigation evidence in this wiki is **2D toy mazes** — Two-Room, PointMaze, Wall, Diverse Maze ([JEPA task capabilities](jepa-task-capabilities.md) §2) — plus an unnamed real-robot result in [V-JEPA 2.1](../../sources/v-jepa-2-1-paper.md) and HWM's +39 on unseen maze layouts. Nothing at room scale, nothing with a lidar or depth map, nothing in a building.

Meanwhile household navigation is the **better-solved half already**, by classical means: a voxel map and an A\* path, which is exactly what makes [DimOS](../../syntheses/agents/dimos-as-home-ai-substrate.md) the most auditable stack in the wiki — its inferred state is readable because there is no learned world model in the loop. A JEPA has nothing to add to that layer today, and replacing it would trade an inspectable state for a latent vector on the one subsystem where the classical answer works. **Whatever role a JEPA earns on a home robot, it is in manipulation, not navigation.**

### And a sizing note

The 2026 probe evidence credits **most of V-JEPA's control advantage to temporal video pretraining**. The latent-prediction objective itself is worth about **+0.10 action R²** over pixel masked autoencoding (0.85 vs 0.75, [action-relevant latents](../../sources/action-relevant-latents-paper.md)). Real, concentrated on rotation, and smaller than the framing. [JEPA-WMs](../../sources/jepa-wms-paper.md) further finds DINO encoders beat V-JEPA encoders as the frozen backbone for control.

## 2. Will it eventually? Three conditions

Conditionally — and most likely **not in the form "JEPA as controller."** Each condition is testable, and none is met.

1. **Something in the recipe declares the home axes irrelevant.** Object identity, layout, lighting, clutter. [SIGReg](../../concepts/world-models/sigreg.md) declares a latent *shape*, not a relevance. [The declared-axis experiment](declared-axis-experiment.md) is the direct test of whether the recipe can be made to — ~1–2 GPU-days, with a stage-0 probe on the released checkpoint that costs nothing to train.
2. **Hierarchy grows past two levels and accepts language.** HWM and WorldDP are the first realizations of the 2022 vision, arriving four years later. The N-level emergent hierarchy is still a position paper.
3. **A force or tactile channel enters the latent.** [VTAM](../../entities/vtam.md) shows a video-action model ingesting tactile images and predicting them *"as faithfully as future video."* Nothing in the JEPA line has done the equivalent.

> [!note] LeCun's own answer to "eventually" is the same shape — a precondition, not a date
> Asked about humanoids in the [MIT Technology Review launch interview](../../sources/mit-tech-review-lecun-ami-labs-interview.md) (2026-01-22): *"nobody — absolutely nobody — knows how to make those robots smart enough to be useful,"* and *"if we want a generally useful domestic robot… that's not going to happen until we have good world models and planning."* He names the bar — *"a domestic robot that is as agile as a house cat"* — and gives **no year**. The dates he does give elsewhere are for the architecture (3–5 years) and for an industrial-first company plan that excludes robots. So the architect of the program and this page agree on the form of the answer, and neither supplies the number.

**The likelier landing is already visible.** A JEPA-style objective as an auxiliary loss or encoder inside a VLA — [FLARE](../../concepts/world-models/flare.md) in [GR00T N1.5](../../sources/groot-n1_5.md), [VLA-JEPA](../../entities/vla-jepa.md) — and a latent world model as **subgoal generator, policy evaluator, or RL environment above a learned skill**. [WorldDP](../../entities/worlddp.md) is LeCun's own group making a [Diffusion Policy](../../entities/diffusion-policy.md) the executor. That is the shape to build toward, not away from.

## 3. The good approach: an architecture, not a model

Every safety source in the wiki — the standards tradition, the safe-learning literature, the guardrail thread, and now the vendors in their own words — converges on the same layering.

| Layer | What it is | Evidence |
|---|---|---|
| **Physical envelope** | Deterministic, enforced *below* the learned stack, certifiable | The only layer an agent cannot reach ([guardrails](../agents/guardrails-for-robot-agents.md)). [PACS](../../sources/pacs-paper.md) holds a diffusion policy at **0.72** success where a CBF filter gives **0.04**, under ISO/TS 15066 energy thresholds at 1 kHz ([safety filters](../../concepts/robotics/safety-filters.md)). [Halos](../../entities/nvidia-halos.md) is the productized version; [ISO 13482 / 10218:2025](../../concepts/robotics/robot-safety-standards.md) the frame. |
| **Learned skills** | VLA or diffusion-policy primitives, evaluated in real homes | [RUM](../../entities/robot-utility-models.md): **90%** on five tasks across 25 homes with a retry loop, **74.4%** raw ([paper](../../sources/robot-utility-models-paper.md)). π0.5 the standing baseline. [SmolVLA](../../entities/smolvla.md)-class models fit the compute a dual-arm base can carry; 5B VLAs do not fit an Orin NX 16 GB ([onboard compute](../platforms/jetson-onboard-compute-xlerobot.md)). |
| **Orchestrator** | Decompose, refuse, ask, stop — **advisory** | [Gemini Robotics ER 2](../../sources/gemini-robotics-2-safety-report.md) consumes safety signals at 100% and misses **>40%** of human-proximity events at low false-positive rates. DeepMind's own conclusion: use it *alongside deterministic low-level guardrails*. [Semantic safety](../../concepts/safety/semantic-safety.md) is measured, sometimes predicted, not enforced. |
| **Authority** | User-programmed, variable autonomy, explicit input, risk-aware defaults | [Yang 2025](../../sources/yang2025-sense-of-agency.md): agency survives high autonomy when the user is the author, and third-party control erodes it more than autonomy does. [Nanavati 2025](../../sources/nanavati2025-feeding-out-of-lab.md): off-nominals will arise; users need to escalate mid-task. [Walker 2024](../../sources/walker2024-explicit-input-teleoperation.md): explicit pointing beats intent inference in clutter. ([Levels of autonomy](../assistive/levels-of-autonomy-in-assistive-robotics.md)) |
| **Execution rail** | Argument-level predicates on every tool call | The one thing playing that role in any ingested robot stack is the fleet's own [ros2-mcp-server](../../entities/ros2-mcp-server.md) policy layer — geofence, keep-outs, object-class refusals. Behavioral, not a boundary, and still the only rail that ships non-empty. |

Where a JEPA belongs in this table: **inside layer 2**, as encoder or auxiliary; **between layers 2 and 3**, as a subgoal generator or policy evaluator. Not as layer 2 itself.

### Two assumptions in the question, pushed on

**"Humanoid."** For a home, the wiki's evidence favours *two arms on a wheeled base* over legs — which is the form factor the question already described. [Tedrake's Walden argument](../../sources/ieee-spectrum-walden-practical-humanoids.md) is regulatory first: a wheeled base **piggybacks on existing AMR safety cases**, cannot fall over, and carries the batteries. The [Stretch-vs-G1 decision](../platforms/household-robot-decision-stretch-vs-g1.md) reaches the same place from the buyer's side; bipedal locomotion in cluttered homes is unsolved in 2026 and a fall is catastrophic. The [humanoid survey](../platforms/humanoid-platforms-survey.md) notes the safety-case problem is being solved only by companies selling into industry.

**"General."** Ackerman's word is *"multipurpose,"* and the [reliability gradient](../assistive/long-term-in-home-robot-deployments.md) says why:

| Setting | Success |
|---|---|
| RLBench, controlled sim | 89.4% |
| RUM, 25 homes, five tasks, with retry | 90% |
| OK-Robot, 10 homes, open-vocabulary | 58.5% |
| BEHAVIOR-1K, 1,000 household tasks | **12.4%** |

The 90% exists only after restricting to five well-shaped tasks. The [assistive landscape](../assistive/assistive-robotics-research-landscape.md) puts safe physical-contact assistance at **10–15 years** out. A deployable assistive robot needs reliability that compounds across steps, and no learned approach — JEPA, VLA, or world-action model — is near that today.

## 4. What to actually do on a dual-arm wheeled platform

Mapped onto the [fleet's build ladder](../projects/fleet-agentic-framework.md) rather than proposed as a new project:

1. **Build the WorldDP shape.** An [ACT](../../entities/act.md) or SmolVLA skill as executor; a [DINO-WM](../../entities/dino-wm.md)-class planner proposing goal-image subgoals above it. Cheap, uses what the fleet has, and measures the *shape a policy* role directly on real hardware.
2. **Run stage 0 of the [declared-axis experiment](declared-axis-experiment.md) first.** It answers whether a JEPA can be made home-robust at all, before any training.
3. **Add a torque channel before any contact-rich task.** [UME](../../entities/ume.md) at $1,900 or a low-cost alternative — the position-only ceiling is measured and it is a cliff. Keep the [bring-up plan](../projects/xlerobot-nav-manip-teleop-bringup.md)'s kinematically dominated task scoping until then.
4. **Keep growing the argument-level predicates.** Tier 3 — held-object provenance — is the open item. That rail is domain knowledge, and it is the part nobody sells.

## Where this could be wrong

- **The JEPA family has not been run through the WorldArena planner role.** The 3–4× planner gap is measured on pixel predictors; the JEPA-side evidence for the same role comes from Push-T and Franka, at 20–50 trials per cell. The *ordering* is consistent across instruments; the *magnitude* for a JEPA planner on a household task is unmeasured.
- **stable-worldmodel may be measuring weak models, not undeclared axes.** The distractor collapse is across all baselines. The declared-axis experiment is the discriminating test, and it has not been run.
- **The reliability gradient is Stretch-centric.** Every real-home number above is single-arm. Dual-arm household evidence in the wiki is [X-VLA](../../entities/x-vla.md)'s cloth folding at ~100%, from 1,200 curated demonstrations on a fixed rig — not a home.
- **The authority findings rest on small or non-disabled samples.** See the caveats on [levels of autonomy](../assistive/levels-of-autonomy-in-assistive-robotics.md).

## Related

- [What world models are measurably good for](what-world-models-are-measurably-good-for.md) — the role-by-role verdicts this page rests on.
- [The abstraction tax](abstraction-tax.md) · [The declared-axis experiment](declared-axis-experiment.md) — the mechanism behind the robustness limit, and its test.
- [JEPA](../../concepts/world-models/jepa.md) — the concept page, including H-JEPA and the probe evidence.
- [Assistive robotics — R&D landscape and JEPA applicability](../assistive/assistive-robotics-research-landscape.md) — the May-2026 version of this question; this page supersedes its JEPA section on robustness and horizon.
- [Guardrails for robot agents](../agents/guardrails-for-robot-agents.md) · [Safety filters](../../concepts/robotics/safety-filters.md) · [Robot safety standards](../../concepts/robotics/robot-safety-standards.md) — the layers.
- [Control abstraction levels](../../concepts/robotics/control-abstraction-levels.md) — why access level, not model class, is the safety variable.
- [Household robot decision — Stretch vs G1](../platforms/household-robot-decision-stretch-vs-g1.md) — the form-factor argument from the buyer's side.
