---
title: Operational space control (and the constrained-QP safety layer under learned policies)
type: concept
created: 2026-08-16
updated: 2026-08-16
sources: 4
tags: [operational-space-control, osc, khatib, control-barrier-functions, cbf, task-consistency, differential-inverse-kinematics, quadratic-program, null-space, joint-impedance, safety, constraint-enforcement, mid-level-controller, franka, tri, drake, diffusion-policy, lbm]
---

**Operational space control (OSC)** — Khatib (1987): control the robot in the **task ("operational") space** the job is defined in — end-effector position, orientation, force — rather than in joint space, by mapping the task-space objective through the robot's Jacobian and inertia into joint torques. For a redundant arm the map has a null space, so a **secondary objective** (posture, joint centering, obstacle clearance) can be pursued *without disturbing the primary task*.

Modern implementations pose it as a **quadratic program solved every control tick**: task objectives as **costs**, physical and safety limits as **hard constraints**.

That split — *objectives are negotiable, constraints are not* — is why this page exists in a wiki mostly about learned policies.

## Why this matters here: it is the layer that makes policy rollouts safe

A learned policy is an unconstrained function approximator. Nothing in a [diffusion policy](../../entities/diffusion-policy.md) or an [LBM](../learning/large-behavior-models.md) knows that the two arms can collide, that the table exists, or that joint 4 is 3° from its limit. In the MIT/[TRI](../../entities/tri.md) stack, **the policy never talks to the robot.** It emits desired end-effector poses into a **mid-level controller**, and that controller — a constrained QP — is the only thing that commands joints.

From the [Diffusion Policy paper](../../sources/diffusion-policy-paper.md)'s Franka-station appendix (D.1), which describes **two** such controllers:

**1. The one used for policy inference** — differential inverse kinematics as a QP:

> *"A custom mid-level controller is implemented to generate desired joint positions from desired end effector poses from the learned policies. At each time step, we solve a differential kinematics problem (formulated as a Quadratic Program) to compute the desired joint velocity to track the desired end effector velocity. The resulting joint velocity is Euler integrated into joint position, which is tracked by a joint-level controller on the robot. **This formulation allows us to impose constraints such as collision avoidance for the two arms and the table, safety region for end effector and joint limits.** It also enables regulating redundant DoF in the null space of the end effector commands. **This mid-level controller is particularly valuable for safeguarding the learned policy during hardware deployment.**"*

**2. The haptic-teleoperation one** — textbook OSC, as a torque QP:

> *"The controller is formulated using **Operational Space Control (Khatib 1987)** as a Quadratic Program operating at **200 Hz**, where position, velocity, and torque limits are added as constraints, and the primary spatial objective and secondary null-space posture objectives are posed as costs."*
>
> With a good Franka Panda model *"including reflected rotor inertias,"* this tracks well on pure spatial feedback and better with feedforward spatial acceleration. **Collision avoidance was not enabled in this mode**, and inference uses controller 1.

The same architecture reappears in the [TRI LBM paper](../../sources/tri-lbm-paper.md): *"We run the Franka robots using our custom joint impedance controller, with a differential inverse kinematics controller on top to translate end-effector relative SE(3) commands from the human teleoperator or the LBM policy… The differential inverse kinematics controller also handles collision avoidance."* Policies run at **10 Hz**.

And its value shows up in the task results, not just the methods section: on bimanual shirt folding, where the grippers must come *"very close towards each other,"* the paper notes that *"having our mid-level controller explicitly handling collision avoidance was especially important for both teleoperation and policy rollout"* (§7.5).

## The two properties that make it a safety mechanism

**Hard constraints, not penalties.** A QP either satisfies its constraints or is infeasible. Joint limits, velocity limits, the table, arm–arm collision, and an end-effector keep-out region are constraints; tracking the policy's requested pose is a *cost*. So when the policy asks for something unsafe, the controller does the **closest safe thing** and the robot slows or stalls rather than swinging through the table. [Tedrake's own teaching text](https://manipulation.csail.mit.edu/pick.html) makes the comparison explicit: the constrained solution *"can be much better than what you would get from solving the unconstrained optimization and then simply trimming any velocities to respect the constraints after the fact"* — clamping a bad answer is not the same as asking for the best answer inside the feasible set.

**A ~100× rate advantage over the thing it is guarding.** Teleop and learned policies run at **10 Hz**; the mid-level controller *"runs around 1 kHz"* and **interpolates** the commanded end-effector poses between policy ticks. The safety envelope is therefore re-solved on the order of **100 times per policy decision**. This is the same hierarchy the [control-rate ladder](../../syntheses/platforms/control-rate-ladder.md) documents for capability (Band C policy over Band A controller) — but the fast tier is doing **constraint enforcement**, not only tracking. The rate gap that looks like a *limitation* when you ask "why can't the VLA run at 1 kHz" is, from this angle, the **mechanism**: a slow policy is safe to deploy precisely because something fast and dumb sits under it.

## What it is not

> [!warning] This is a constraint envelope, not a certified safety filter
> It enforces **model-based, geometric, single-robot** constraints: the arms, the table, the joint limits, a hand-authored keep-out box. That is exactly the set of hazards you can write down in advance from a URDF.
>
> It does **not** provide: perception-driven avoidance of objects that were not modelled (a person leaning in, a cup out of place); any formal guarantee (no control barrier function, no reachability certificate, no proof of forward invariance); protection against a policy doing something *semantically* wrong at full speed inside the feasible set (crushing the object it is holding, knocking over what it should have grasped); or anything a standards body would accept as functional safety ([ISO 13482 and friends](robot-safety-standards.md) presume a risk assessment over specified behaviors, which a learned policy does not have).
>
> The honest description: **it prevents the failure modes of an unconstrained function approximator commanding a kinematic chain**, which is a real and frequently-hit class, and nothing beyond that. For the version with an invariance proof, see the [CBF section below](#the-formal-upgrade-control-barrier-functions-oscbf) — which closes the *guarantee* gap and none of the perception one.

The wiki's other safety threads sit at different layers, and none of them replaces this one: [predictive red-teaming](robot-policy-evaluation.md) estimates degradation *before* deployment; [safely learning dynamical systems](../../sources/safely-learning-dynamical-systems-paper.md) gives certificates for linear/polynomial systems only; DeepMind's [Swiss-cheese model](../../sources/deepmind-gemini-robotics-safety-page.md) names a "physical" layer without specifying it. **This is what actually occupies that physical layer in a working manipulation stack**, and it is documented in an appendix.

## The formal upgrade: control barrier functions ([OSCBF](../../sources/oscbf-paper.md))

Everything above describes an envelope with **no proof attached**. The Stanford version has one, and it is worth understanding as a modification of the same QP rather than a different architecture.

Replace each hand-written inequality with a **control barrier function**: define the safe set as the zero-superlevel set of `h(z)` and require `ḣ(z,u) ≥ −α(h(z))`. That single linear inequality makes the safe set **forward-invariant** — once inside, the dynamics cannot leave it — which is a statement about the *future*, where a per-tick feasibility check is only a statement about *now*. Under torque control most manipulator constraints have relative degree 2, so they need High-Order CBFs.

**The contribution beyond "put CBFs in an OSC" is the objective function.** A standard safety filter minimizes `‖u − u_nom‖²` — deviation in the raw control input. [Morton & Pavone](../../sources/oscbf-paper.md) argue that is wrong whenever there is a task hierarchy, and name three ways it goes wrong: optimizing a joint-space metric for an operational-space task; optimizing an operational-space metric while ignoring the null-space joint task; and optimizing a *torque* metric when the task is defined over *position*, since the inertial mapping puts distance between the two. **Task consistency** means the filter should *"minimally modify an output that reflects the task and hierarchy definition"* — so the objective becomes deviation in operational-space and null-space joint **accelerations**, separately weighted.

That idea generalizes past robotics: any minimally-invasive filter has to answer **"minimal in what?"**, and the default answer — the actuator command — is rarely the quantity the task lives in.

| | Deployed envelope (MIT/TRI) | OSCBF (Stanford) |
|---|---|---|
| Constraint form | Hard inequalities in a diff-IK QP | **CBFs** → forward invariance of the safe set |
| Objective | Track the commanded end-effector pose | **Task-consistent**: null-space + operational-space accelerations |
| Constraints covered | Arm–arm collision, table, EE keep-out box, joint limits | + **singularity avoidance** (manipulability index), whole-body containment, self-collision, velocity/torque limits, dynamic obstacles |
| Dynamics | Kinematic diff-IK (plus a joint-impedance layer) | Full second-order dynamics with Coriolis/gravity compensation |
| Rate | ~1 kHz | ~1–10 kHz; **168 constraints at ~3 kHz**, >400 at 1 kHz |
| Hardware | Franka, bimanual, running real learned policies | Franka, single arm, **teleop only — no learned policy is ever run** |
| Guarantee | None claimed | Forward invariance — **degrading to "enforces but does not guarantee" once many constraints and input limits conflict and the QP is relaxed** |

**The two halves have never been put together.** One stack has the policies and no guarantee; the other has the guarantee and no policy. OSCBF's own future work is precisely the missing experiment: *"deploying the learned policies with OSCBF maintaining whole-body safety of the robot."*

And one gap is common to both: **obstacles are given, not perceived.** Sphere decompositions and keep-out boxes are authored offline. Real-time perception is future work on the Stanford side and absent on the TRI side, which is the single thing separating either from safety in an unstructured home.

> [!note] Singularity avoidance is the constraint the deployed envelope does not have
> OSCBF treats a **kinematic singularity** as a safety constraint — `h = μ(q) − ε` on Yoshikawa's manipulability index — and demonstrates the arm moving in and out of near-singular configurations (`μ = 1e−2`) under teleoperation. Not "safety" in the collision sense, but exactly the failure mode where a diff-IK QP's commanded joint velocities blow up. Worth noting that the deployed stack handles this only implicitly, through joint and velocity limits.

> [!warning] And the guarantee is not the axis that predicts task success
> [PACS](../../sources/pacs-paper.md) (ICRA 2026) measured what these filters cost a diffusion policy, and the CBF version — the one *with* the invariance proof — scored **0.04 average task success on robomimic**, zero on two of three tasks, because a reactive filter pushes the policy **off the demonstration manifold into states it cannot recover from**. A filter that instead **brakes along the intended path** scored **0.72**, against 0.70 for the same pipeline unfiltered.
>
> So the ordering this page implied — hand-written constraints < CBFs — is wrong as a predictor of deployed performance. The ordering that holds is **path-deviating < path-consistent**, and it cuts across the guarantee axis. Note also that the same author ([Pavone](../../entities/marco-pavone.md)) is on both papers; this is a refinement within one research line, not a dispute between camps. Full taxonomy on [safety filters for learned policies](safety-filters.md).

## Relation to the rest of the stack

- **[Whole-body control](whole-body-control.md)** is the humanoid-scale sibling. Classical WBC is largely OSC plus null-space prioritization across a floating-base robot; the learned WBC policies this wiki tracks ([SONIC](../../sources/sonic-paper.md), BumbleBee) replace the QP with a trained network and, notably, **give up the hard-constraint property in doing so**.
- **[Control abstraction levels](control-abstraction-levels.md)** — the taxonomy's "level 3: policy control" quietly assumes something like this exists. Handing a model high-level commands is only safe because a constrained controller is between it and the actuators; the taxonomy scores the *model's* reach without crediting the layer that bounds it.
- **[Safety filters for learned policies](safety-filters.md)** — the hub page comparing all three filters this wiki has ingested, and where the path-consistency finding lives.
- **[Graphs of convex sets](graphs-of-convex-sets.md)** — the same group's other convex program, at the opposite time scale. GCS solves an SOCP **once per query** to get a globally optimal collision-free plan with a certificate; the OSC/diff-IK QP solves a small program **1,000 times a second** to keep whatever is being executed inside the feasible set. Planner and runtime guard, both convex, both in [Drake](../../entities/drake.md)'s mathematical-program interface.
- **[Optimal control](optimal-control.md)** — the QP-per-tick pattern is one-step MPC in task space; everything on that page about horizon, model quality, and constraint handling applies.
- **[Collaborative robots](collaborative-robots.md)** / **[robot safety standards](robot-safety-standards.md)** — the certification framing the constraint envelope does *not* satisfy.

## Key references

- [Diffusion Policy paper](../../sources/diffusion-policy-paper.md) Appendix D.1 — **the primary source on this page**: both mid-level controllers, their constraints, and the "safeguarding the learned policy" claim. 10 Hz policy, ~1 kHz controller, 200 Hz haptic OSC QP.
- [TRI LBM paper](../../sources/tri-lbm-paper.md) — the same architecture two years later at program scale: joint impedance + diff IK with collision avoidance, policies at 10 Hz.
- *Robotic Manipulation* (Tedrake), [Ch. 3 "Basic Pick and Place"](https://manipulation.csail.mit.edu/pick.html) — differential IK as a QP: least-squares baseline, then joint-position/velocity/acceleration limits as linear constraints, *"we can easily add more constraints to our QP, without significantly increasing the complexity, as long as they are linear."* Live-web reference, not an ingested source.
- Khatib, *A unified approach for motion and force control of robot manipulators: the operational space formulation* (1987) — the origin, cited by the Diffusion Policy appendix. Not ingested.
- [**OSCBF** — Safe, Task-Consistent Manipulation with Operational Space Control Barrier Functions](../../sources/oscbf-paper.md) — Morton & [Pavone](../../entities/marco-pavone.md), IROS 2025. **Ingested**: the CBF version of this envelope, plus the task-consistency argument, 168 constraints at ~3 kHz, and **CBFpy** (JAX) as open-source implementation.

## Mentioned in

- [Diffusion Policy paper](../../sources/diffusion-policy-paper.md) — Appendix D.1; §7.5 shirt folding.
- [TRI LBM paper](../../sources/tri-lbm-paper.md) — hardware controller stack.
- [OSCBF paper](../../sources/oscbf-paper.md) — the CBF formulation, task consistency, and the scaling numbers.
- [PACS paper](../../sources/pacs-paper.md) — what a filter costs a learned policy, and why path consistency is the axis that matters.
