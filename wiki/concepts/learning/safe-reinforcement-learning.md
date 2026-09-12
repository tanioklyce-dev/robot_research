---
title: Safe reinforcement learning
type: concept
created: 2026-09-07
updated: 2026-09-12
sources: 4
tags: [safe-rl, cmdp, lagrangian, safety-gymnasium, projection-methods, pid-lagrangian, safety-critic, shielding, recovery-rl, safe-exploration, constrained-optimization, risk-sensitive, contact-rich, vla, safety-alignment]
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

## Constrained optimization beats reward shaping — the measurement

The claim that "safety is a constraint, not a term in the objective" is stated everywhere in this literature and rarely tested against the obvious alternative. [SafeVLA](../../sources/safevla-paper.md) tests it, on a [VLA](vla-models.md), against the same RL fine-tuning pipeline in two configurations:

| Safety-ObjNav | success ↑ | cumulative cost ↓ |
|---|---|---|
| Task-only RL fine-tune (FLaRe) | 0.822 | 12.356 |
| **Reward shaping** — cost added as a reward penalty (FLaRe-RS) | 0.75 | 4.755 |
| **CMDP + adaptive Lagrangian** (ISA) | **0.865** | **1.854** |

The shaped variant loses on **both** axes, and on the hardest task it roughly halves success (0.45 vs 0.637). The paper closes the argument with the sweep that matters: **dynamic Lagrangian multipliers beat every fixed penalty coefficient that meets the same cost constraint.** A fixed coefficient sets an exchange rate between harm and reward in advance; an adapted multiplier finds the price of the constraint that is actually binding.

> [!note] But the ablation says the optimizer is not the load-bearing part
> Run the *identical* constrained recipe in simplified scenes without deliberately-placed hazards and cost goes **1.854 → 5.01** — worse than the reward-shaping baseline it just beat — with success falling to 0.645. **A constrained optimizer can only constrain behaviors it observes.** "We used safe RL" says close to nothing without "on data that contained the failures," which is the same dependency [safe exploration](#the-formalisms) has and the same reason the [contact-data problem](../robotics/contact-rich-manipulation.md#the-data-problem-which-is-structural) bounds this whole area.

## Which family of constrained optimizer, and what each costs

[Safety-Gymnasium](../../entities/safety-gymnasium.md)'s comparison of 16 algorithms across 54 environments gives the shape of the space, and it is not "Lagrangian vs the rest":

| Family | Members | Behavior |
|---|---|---|
| **Lagrangian** | PPO-Lag, TRPO-Lag, RCPO, MAPPO-Lag | tracks the constraint but **oscillates** around it — more time both *Strongly Unsafe* and *Strongly Safe* |
| **Projection** | CPO, PCPO, MACPO | stays **centered** on the constraint; PCPO gets lower cost *and* lower reward — *"an excessively cautious policy has the potential to undermine performance"* |
| **PID-Lagrangian** | CPPO-PID | a PID controller on the multiplier: **PPO-Lag's rewards with markedly fewer excursions into Strongly Unsafe** |

The scale of what constraining buys: unconstrained PPO runs **20–40× over the cost limit** (`HumanoidVel` 38.4, `DoggoCircle1` 33.1 normalized), and PPO-Lag cuts cost **98% for a 45% reward loss** on velocity tasks. That ratio is the strongest single argument in this wiki for putting safety in the constraint rather than the objective — the other being [SafeVLA](../../sources/safevla-paper.md)'s head-to-head against reward shaping.

> [!note] The oscillation result has a downstream consequence nobody acted on
> Safety-Gymnasium (2023) finds **PID-Lagrangian specifically fixes the oscillation that plain Lagrangian has**, at no reward cost. [SafeVLA](../../sources/safevla-paper.md) (2025, same group) runs on plain Lagrangian and relegates PID-Lagrangian to an appendix — where it posts **lower cost at equal success** (1.64 vs 1.854 on Safety-ObjectNav). Given the 2023 finding, that belonged in the main table.

## Measurement

Safe RL adds metrics that ordinary RL does not report, and the survey's §3.6 argues the important ones are **joint**:

- **Violation statistics or cost value** — the base safety metric, physically instantiated in contact tasks as force, acceleration, or velocity bounds.
- **The trade-off explicitly.** A ratio of safe-and-successful runs to violating ones; or successes and violations printed side-by-side; or — the strongest display — **learning curves of success, violation, and their ratio through training**, which shows how the two objectives move against each other rather than reporting their endpoint.
- **Robustness probes** — noise injected in observation space or action space, external disturbance, cluttered/changing backgrounds, non-stationary environments.

**Measure the policy on the trials it fails.** [SafeVLA](../../sources/safevla-paper.md) adds a protocol worth adopting generally: construct environments where the task is *impossible*, so success rate is ≈ 0 for every method and cannot confound the safety measurement. What it finds there is the most transferable result in that paper:

| Cumulative cost when success is impossible | |
|---|---|
| Task-only RL fine-tune (FLaRe) | **71.68** |
| IL base model (SPOC) | 14.63 |
| Constrained (ISA) | **2.20** |

The unconstrained policy is **32×** worse than the constrained one and **~6× worse than its own imitation-learned starting point** — RL fine-tuning for task performance made the *failure* behavior more dangerous. It thrashes: repeated collisions while making no progress. And in normal evaluation the baseline's cost is significantly negatively correlated with success (p < 0.01), so its unsafe behavior hides inside its failures; for the constrained policy that correlation is rejected — **it fails safely**.

The general point: **a success rate describes only the fraction of trials the policy won.** A policy reported at 60% is being characterized on 60% of its behavior, and the remaining 40% is where the damage is. Pairs with [PACS](../../sources/pacs-paper.md)'s **safe success** from the other end.

> [!warning] Half the standard benchmark reports a tie
> On Safety-Gymnasium's **velocity** tasks *every* safe-RL algorithm meets the cost limit, reward differences are *"negligible"* and optimal policies are *"tightly clustered."* Only the noisier **navigation** tasks separate methods. So a safe-RL result quoted from velocity tasks is quoted from the half of the benchmark that measures nothing — the [saturation](../robotics/robot-policy-evaluation.md) failure mode, arriving in this literature and stated by its own benchmark authors without being named.
>
> Note also that implementations of the *same* published algorithm disagree materially: CPO on `CarButton1` scores 1.75 normalized cost in SafePO and **3.65** in OpenAI's Safety-Starter-Agents. **A safe-RL number without its implementation is under-specified.**

> [!warning] Safety objectives cost data
> "Having both task and safety objectives increases the optimization complexity, and consequently the amount of data to learn effective policies." Reported sample-efficiency numbers for unconstrained RL do not transfer to the constrained version of the same task. This compounds with the [real-world RL](real-world-robot-rl.md) cost structure, where the data is collected on hardware that the safety constraint exists to protect.

## Where it sits relative to the rest of this wiki

Most of the robot learning this wiki tracks is **imitation**, not RL — and the contact-rich survey excludes imitation learning by design, on the argument that IL "replicates demonstrated behaviors rather than actively managing safety." That argument is worth holding at arm's length: a demonstration set contains only safe episodes *by construction*, which is a distributional safety property rather than an absent one, and it is exactly the property the [runtime failure detection](../robotics/runtime-failure-detection.md) line exploits (train on successes only, flag departure).

The practical consequence is that safe RL and generalist manipulation policies are, at present, **two literatures that barely touch**. The bridge the survey proposes is architectural rather than algorithmic: let the large model plan and parameterize, keep a certified low-level layer, and use safe RL where online adaptation happens.

[SafeVLA](../../sources/safevla-paper.md) is the wiki's one ingested instance of the *other* bridge — apply the CMDP machinery directly to the VLA's fine-tuning, no architectural split. It works, generalizes across base models and to unseen environments, and comes with the caveat that defines its scope: **its costs are discrete collision events with simulator ground truth, not forces.** A force limit is continuous, violated by degree, and unobservable without a sensor. Whether binary-cost CMDP transfers to force envelopes is untested and is the concrete open question at the boundary between these two pages.

## Related concepts

- [Contact-rich manipulation](../robotics/contact-rich-manipulation.md) — the setting where exploration is physically destructive.
- [Safety certificates](../robotics/safety-certificates.md) — the hard-guarantee end of the spectrum.
- [Safety filters for learned policies](../robotics/safety-filters.md) — shielding as deployed, and its measured cost to the policy.
- [Impedance and admittance control](../robotics/impedance-control.md) — the safe action space.
- [Real-world robot RL](real-world-robot-rl.md) — the systems side of learning on hardware.
- [Multi-agent RL](multi-agent-rl.md) · [optimal control](../robotics/optimal-control.md) — neighbouring formalisms.
- [Robot policy evaluation](../robotics/robot-policy-evaluation.md) — why the reporting conventions above matter.

## Current state

Well-supplied with formalisms and poorly supplied with benchmarks. The dedicated safe-RL evaluation infrastructure the survey can name amounts to **[Safety-Gymnasium](../../entities/safety-gymnasium.md)**, **Robust Gymnasium**, and **safe-control-gym** — none of which is contact-force-aware; Safety-Gymnasium's costs are **speed thresholds, region entry, contact events and joint limits**, with no wrench anywhere in a MuJoCo suite that computes them — against a general-manipulation benchmark landscape (RoboVerse, RoboCasa, robosuite, ManiSkill, Meta-World, RLBench) that has no safety instrumentation at all. [Safety-CHORES](../../entities/safety-chores.md) is the newest addition and the first that scores an *embodied generalist policy* on safety and task success together; it is also collision-based, so the **no standardized contact-force evaluation protocol** gap is still open. That gap, not the algorithms, is what the survey's perspectives section leads with.

## Mentioned in

- [Safe Learning for Contact-Rich Robot Tasks (survey)](../../sources/safe-learning-contact-rich-survey.md) — the exploration/execution split and every method family above.
- [Safety-Gymnasium](../../sources/safety-gymnasium-paper.md) — the benchmark: the algorithm-family comparison, the 98%-cost-for-45%-reward trade, the oscillation finding, and the velocity-suite tie.
- [SafeVLA](../../sources/safevla-paper.md) — the flagship application to a VLA: CMDP + adaptive Lagrangian, the reward-shaping comparison, the elicitation ablation, and the extreme-failure protocol.
- [FEARL — Verifiable Foundation Models for Robot Safety](../../sources/fearl-verifiable-foundation-models-robot-safety-paper.md) — verification-guided shielding applied to foundation-model policies trained with PPO+LoRA, SFT→PPO, or DAgger; the shield is a last resort, certification the primary goal.
