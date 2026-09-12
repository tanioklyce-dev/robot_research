---
title: Safety certificates (Lyapunov, CBFs, contraction metrics, reachability)
type: concept
created: 2026-09-07
updated: 2026-09-12
sources: 3
tags: [control-barrier-functions, lyapunov, contraction-metrics, reachability, hamilton-jacobi, forward-invariance, passivity, formal-guarantees, provable-safety]
---

# Safety certificates

## Definition

A **safety certificate** is a mathematical object whose existence proves a property of a controlled system for all time — not just on the trajectories you tested. Four families dominate robotics, and they certify **different properties**, which is the distinction most casual use of "provably safe" loses ([Zhang et al.](../../sources/safe-learning-contact-rich-survey.md), §3.1.3).

| Family | Certifies | Object | Fails at |
|---|---|---|---|
| **Lyapunov** | stability / convergence to an equilibrium | scalar V(x), positive definite, non-increasing | finding V for high-DoF nonlinear systems; **hybrid** contact/non-contact modes; says nothing about the transient |
| **Control barrier functions (CBFs)** | **forward invariance** of a safe set | scalar h(x) ≥ 0 on the safe set, with ḣ ≥ −α(h) | model error; conflicting constraints; **high relative degree** constraints — i.e. contact and force |
| **Contraction metrics** | incremental stability — *any two* trajectories converge | Riemannian metric M(x) with a matrix inequality | finding M; addresses stability, not state constraints |
| **Reachability / invariant sets** | the set of states from which safety is achievable | value function solving an HJ PDE; or precomputed reachable tubes | **curse of dimensionality** — exact solutions only for simplified systems |

## Lyapunov versus barrier: the distinction that matters

Nearly every classical robot controller — PD, impedance, admittance — has an implicit Lyapunov function behind its stability proof, and **passivity-based control** is the Lyapunov-family argument specialized to interaction: design the closed loop to be passive and it cannot inject unbounded energy into the environment (see [impedance control](impedance-control.md)).

But stability is about the **destination**, and safety is about the **path**:

> A Lyapunov-stable controller may drive a robot back to its desired equilibrium after a disturbance but still **allow temporary violations of safe force or workspace limits.**
> — §3.1.3

Lyapunov sublevel sets are only safety certificates if they are *explicitly constructed* to be forward-invariant and contained in the safe set. Otherwise you have proved the robot recovers, not that it never crossed the line. **Barrier functions certify the line directly** — h(x) is built so that its derivative cannot carry it across zero, making the safe set forward-invariant regardless of where the system is heading. In practice CBFs are enforced as a hard constraint in a QP that minimally modifies the nominal control input.

The practical reading: **Lyapunov for long-term stability and boundedness, barriers for state constraints, and contact-rich systems need both.**

## Why contact is the hard case for every one of them

- **Lyapunov** — contact/non-contact switching makes the system *hybrid*, where standard Lyapunov theory does not directly apply and multiple Lyapunov functions may be required.
- **CBFs** — force and contact constraints have **high relative degree**: they depend on higher-order derivatives of the state, which is where CBF design becomes "significantly more involved." Contact-rich robotics is therefore the CBF literature's worst case, not its showcase. CBFs also need a reasonably accurate model, and robust/adaptive variants buy uncertainty tolerance with conservatism. And multiple CBFs, or a CBF against the task goal, can be **jointly infeasible** — the standard fix is to relax a constraint, at which point the guarantee weakens.
- **Contraction metrics** — powerful for robust trajectory tracking and disturbance rejection, but M(x) may be very complex or not exist in closed form, and contraction addresses stability rather than explicit state constraints.
- **Reachability** — the strongest runtime behavior with the most predictable cost, because the expensive computation is pushed offline into trajectory-parameterized reachable sets; the price is that those sets are only valid while the model is, so it degrades under mismatch or rapidly changing contact dynamics.

## Compute placement is the practical selector

The survey's most actionable comparison is not about guarantee strength — it is about **where the computation sits** (§3.1.1):

- **Reachability filters** precompute reachable sets offline and project the policy's plan parameters onto the nearest safe plan at runtime. Lightweight online, hard safety, **poor adaptivity** under model change. → *fixed platforms, stable dynamics, tight real-time budgets.*
- **CBF-in-QP and model-predictive shields** compute online over a receding horizon. Adaptive to changing constraints and intent, **expensive**, and feasibility becomes the bottleneck in high-dimensional contact settings. → *environments where constraints and intent change fast and online compute exists.*
- **Safe-set / certificate construction** (implicit safe sets from a black-box or digital-twin model; GP-learned stochastic barrier certificates) sits between: model-free or data-driven, with conservatism governed by certificate fidelity, and a permissible set that **grows toward the known-model benchmark as data accumulates**.

## The thing a certificate does not tell you

> [!warning] A guarantee about the *system* is not a guarantee about the *policy*
> Every certificate family above is designed against a dynamics criterion: will the system remain in the safe set. None is designed against the criterion that decides whether a learned policy still works: **will the policy recognize the state the filter just put it in.**
>
> The measurement is on [safety filters](safety-filters.md): identical constraints, identical robot, identical tasks — a CBF filter leaves a diffusion policy at **0.04** task success, a path-consistent reachability filter at **0.72** ([PACS](../../sources/pacs-paper.md)). Their guarantees are comparable; their effect on the policy is not, because one deviates from the intended path and pushes the robot out of the training distribution and the other brakes along it.
>
> The [survey's own six-axis comparison frame](../../sources/safe-learning-contact-rich-survey.md) has no axis that can see this. **A certificate is necessary and nowhere near sufficient when the thing being filtered is learned.**

## Learned certificates

The certificate families predate learning, but each has a learned variant, and this is where the two literatures meet: **learned barrier functions**, GP-based stochastic barrier certificates with probabilistic safety levels, **Lyapunov actor–critic** (policy optimization under an explicit Lyapunov constraint, executed through an adaptive impedance layer), safety indices synthesized by querying a black-box dynamics model, and latent-space barriers for high-dimensional visual tasks where no analytic state exists.

The survey's stated open problem for these is **failure detection and repair**: a learned certificate can degrade, and there is no established procedure for noticing (§5.6). Compare [runtime failure detection](runtime-failure-detection.md), which solves the analogous problem for policies rather than certificates.

## Related concepts

- [Safety filters for learned policies](safety-filters.md) — certificates as deployed runtime mechanisms, and the measured cost of each style.
- [Impedance and admittance control](impedance-control.md) — passivity as the Lyapunov-family certificate for interaction.
- [Contact-rich manipulation](contact-rich-manipulation.md) — why this task class is the hard case for all four families.
- [Safe reinforcement learning](../learning/safe-reinforcement-learning.md) — certificates embedded in training rather than deployment.
- [Optimal control](optimal-control.md) — HJ reachability is the same Hamilton–Jacobi machinery, used to compute a safe set instead of an optimal cost-to-go.
- [Formal verification](../learning/formal-verification.md) — the proof-assistant side of "provable"; a different tradition with the same word.
- [Robot safety standards](robot-safety-standards.md) — what a conformity argument would have to be built on.

## Current state

Mature theory, expanding into learning, and blocked in the same two places everywhere: **finding the certificate** (V, h, or M) for realistic high-DoF systems with contact, and **keeping it valid** under model error. Reachability is the most deployment-ready and the least adaptive; CBFs are the most active research area and structurally worst-suited to force constraints. The scalable-verification problem for diffusion, latent-variable, and residual policies is named as open (§5.6), with abstraction of the action space — certifying over *stiffness and damping* rather than torques — offered as the most promising handle.

## Mentioned in

- [Safe Learning for Contact-Rich Robot Tasks (survey)](../../sources/safe-learning-contact-rich-survey.md) — the four-family treatment and the compute-placement comparison.
- [PACS](../../sources/pacs-paper.md) — the measurement that a certificate's strength does not predict its effect on a learned policy.
- [FEARL — Verifiable Foundation Models for Robot Safety](../../sources/fearl-verifiable-foundation-models-robot-safety-paper.md) — a certificate of a different kind: a (δ, ρ)-probabilistic *verified input region* of a 2-layer MLP (ε-ProVe), not a barrier or Lyapunov function; the uncertified volume bounds both shield activation and value loss.
