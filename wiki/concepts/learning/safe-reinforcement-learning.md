---
title: Safe reinforcement learning
type: concept
created: 2026-09-07
updated: 2026-09-07
sources: 1
tags: [safe-rl, cmdp, lagrangian, safety-critic, shielding, recovery-rl, safe-exploration, constrained-optimization, risk-sensitive, contact-rich]
---

# Safe reinforcement learning

## Definition

**Safe RL** is reinforcement learning where constraint satisfaction is a first-class objective rather than something the reward function is hoped to encode. In physical robotics it splits along a phase axis that the [contact-rich survey](../../sources/safe-learning-contact-rich-survey.md) makes its top-level organizing distinction:

- **Safe exploration** — don't break anything *while learning*. The hard problem, because the agent must visit states it has no model of in order to learn about them, and in a [contact-rich task](../robotics/contact-rich-manipulation.md) a bad rollout jams a part, scars a surface, wears a tool, or injures somebody.
- **Safe execution** — don't break anything *while deployed*, under distribution shift, disturbance, and unmodeled dynamics.

The tools differ by phase, and conflating them is the standard source of confusion about what a given method guarantees.

## The formalisms

**Constrained MDP (CMDP).** The standard formalism: maximize reward subject to the expected cumulative cost of unsafe states staying below a threshold. Solved in practice by **Lagrangian relaxation** — a dual variable weights the cost term and is adapted during training, so constraints are satisfied **asymptotically**. That word is load-bearing: a Lagrangian CMDP method is safe *in the limit*, not during the run that trains it.

**Safety critics and feasibility value functions.** Encode safety in a value function of its own: estimate the long-term probability of constraint violation from a state, and steer the policy toward margin. Pessimistic objectives downweight risky actions under uncertainty.

**Recovery RL.** Separate the task policy from a **recovery policy** that intervenes when the agent approaches a high-risk region, steers back to safety, and returns control. The separation is the point — one policy no longer has to be both ambitious and cautious.

**Risk-sensitive objectives.** Optimize a tail statistic (CVaR-style) rather than an expectation, so rare-but-damaging force spikes are penalized rather than averaged away.

**Shielding and action projection.** Wrap the policy in a runtime layer that vetoes or minimally modifies unsafe actions — CBF-QP, model-predictive shields that forecast violations and substitute goal-directed recoveries, reachability projection onto the nearest safe plan parameters. This gives **hard** online guarantees where the CMDP family gives expectation or probability bounds, and pays for them in conservatism and data efficiency. See [safety certificates](../robotics/safety-certificates.md) and [safety filters](../robotics/safety-filters.md).

**Interventions and abstractions for training-time safety.** *Advantage-based intervention* achieves safety through online interventions plus surrogate-MDP training (requires a safe backup policy); *AlwaysSafe* achieves it through a model-based abstraction of the safety dynamics (requires the abstraction to be correct). Both enable safe data collection; both move the assumption rather than removing it.

**Constraint via action space.** The most-used mechanism in contact-rich work isn't an algorithm at all — it is choosing an action space whose every element is safe. Learn **stiffness, damping, and force targets** rather than torques, and compliance bounds the interaction force by construction ([impedance control](../robotics/impedance-control.md)).

> [!note] The trade the whole field is making
> **Expectation/probability bounds are cheap and leak; hard bounds are expensive and conservative.** Constrained and risk-sensitive RL give bounds that "exhibit weakness under distribution shift"; shielding and projection layers "offer hard online guarantees, but typically depend on conservative uncertainty sets, limiting data efficiency" ([survey](../../sources/safe-learning-contact-rich-survey.md) §4.4). Nothing in the reviewed literature escapes this; methods choose a point on it.

## Measurement

Safe RL adds metrics that ordinary RL does not report, and the survey's §3.6 argues the important ones are **joint**:

- **Violation statistics or cost value** — the base safety metric, physically instantiated in contact tasks as force, acceleration, or velocity bounds.
- **The trade-off explicitly.** A ratio of safe-and-successful runs to violating ones; or successes and violations printed side-by-side; or — the strongest display — **learning curves of success, violation, and their ratio through training**, which shows how the two objectives move against each other rather than reporting their endpoint.
- **Robustness probes** — noise injected in observation space or action space, external disturbance, cluttered/changing backgrounds, non-stationary environments.

> [!warning] Safety objectives cost data
> "Having both task and safety objectives increases the optimization complexity, and consequently the amount of data to learn effective policies." Reported sample-efficiency numbers for unconstrained RL do not transfer to the constrained version of the same task. This compounds with the [real-world RL](real-world-robot-rl.md) cost structure, where the data is collected on hardware that the safety constraint exists to protect.

## Where it sits relative to the rest of this wiki

Most of the robot learning this wiki tracks is **imitation**, not RL — and the contact-rich survey excludes imitation learning by design, on the argument that IL "replicates demonstrated behaviors rather than actively managing safety." That argument is worth holding at arm's length: a demonstration set contains only safe episodes *by construction*, which is a distributional safety property rather than an absent one, and it is exactly the property the [runtime failure detection](../robotics/runtime-failure-detection.md) line exploits (train on successes only, flag departure).

The practical consequence is that safe RL and generalist manipulation policies are, at present, **two literatures that barely touch**. The bridge the survey proposes is architectural rather than algorithmic: let the large model plan and parameterize, keep a certified low-level layer, and use safe RL where online adaptation happens.

## Related concepts

- [Contact-rich manipulation](../robotics/contact-rich-manipulation.md) — the setting where exploration is physically destructive.
- [Safety certificates](../robotics/safety-certificates.md) — the hard-guarantee end of the spectrum.
- [Safety filters for learned policies](../robotics/safety-filters.md) — shielding as deployed, and its measured cost to the policy.
- [Impedance and admittance control](../robotics/impedance-control.md) — the safe action space.
- [Real-world robot RL](real-world-robot-rl.md) — the systems side of learning on hardware.
- [Multi-agent RL](multi-agent-rl.md) · [optimal control](../robotics/optimal-control.md) — neighbouring formalisms.
- [Robot policy evaluation](../robotics/robot-policy-evaluation.md) — why the reporting conventions above matter.

## Current state

Well-supplied with formalisms and poorly supplied with benchmarks. The dedicated safe-RL evaluation infrastructure the survey can name amounts to **Safety Gymnasium**, **Robust Gymnasium**, and **safe-control-gym** — none of which is contact-force-aware — against a general-manipulation benchmark landscape (RoboVerse, RoboCasa, robosuite, ManiSkill, Meta-World, RLBench) that has no safety instrumentation at all. There is **no standardized contact-force evaluation protocol**, which means violation rates, recovery latency, and generalization are not comparable across papers. That gap, not the algorithms, is what the survey's perspectives section leads with.

## Mentioned in

- [Safe Learning for Contact-Rich Robot Tasks (survey)](../../sources/safe-learning-contact-rich-survey.md) — the exploration/execution split and every method family above.
