---
title: "Prevention, detection, intervention: the runtime stack a deployed policy needs"
type: synthesis
created: 2026-08-16
updated: 2026-08-16
corrected: 2026-08-16
tags: [safety-filter, runtime-monitoring, failure-prediction, policy-steering, deployment, conformal-prediction, out-of-distribution, diffusion-policy, synthesis]
---

# Prevention, detection, intervention

A learned policy that works in a lab is not a deployable system. Six papers ingested on 2026-08-16 — from MIT/TRI, Stanford, CMU and TUM, published across 2023–2026 — turn out to be building **three different layers of the same missing stack**, mostly without citing each other's role in it.

This page states the stack, the one design rule that spans all three layers, and the four things that are wrong with all of them at once.

## The three questions

| Layer | Question it answers | Blind to | Ingested instances |
|---|---|---|---|
| **Prevention** | *Will this action hurt someone or break something?* | Whether the task is going well at all | [constrained diff-IK QP](../../concepts/robotics/operational-space-control.md) (TRI/MIT, deployed), [OSCBF](../../sources/oscbf-paper.md), [PACS](../../sources/pacs-paper.md) |
| **Detection** | *Is this rollout going to succeed?* | Physical hazards; the arm can be about to hit the table and every score stays green | [Sentinel](../../sources/sentinel-paper.md), [FAIL-Detect](../../sources/fail-detect-paper.md), [FIPER](../../sources/fiper-paper.md) |
| **Intervention** | *Which of the policy's own options should it take?* | Everything outside the K sampled plans | [FOREWARN](../../sources/forewarn-paper.md) |

They are not substitutes. A safety filter cannot see a policy confidently placing the object in the wrong location — every constraint is satisfied. A runtime monitor cannot stop an arm swinging through a table — it has no authority over actions. A steering module assumes the right behavior is already among the candidates.

**Nothing in this corpus runs more than one of them at once.**

## The rule that spans all three layers

Two independent lines — one from safety, one from intent-alignment — converged on the same constraint without either stating it in general form:

> **A runtime intervention that stays inside the policy's own output distribution costs almost nothing. One that leaves it costs almost everything.**

The evidence:

- [PACS](../../sources/pacs-paper.md): a control-barrier-function filter enforcing collision constraints by **deviating from the path** drops robomimic task success to **0.04**. The same constraints enforced by **braking along the intended path** hold **0.72** — against 0.70 for the identical pipeline unfiltered. The mechanism is explicit in the paper's own plots: the reactive filter pushes the robot into regions absent from the training distribution, and the policy cannot recover.
- [FOREWARN](../../sources/forewarn-paper.md): steering by **selecting among the K plans the policy already sampled** lifts base success 0.30/0.20/0.10 → 0.80/0.70/0.70. Nothing is edited, so nothing leaves the manifold.

Every classical safety mechanism is designed against a **dynamics** criterion — will the system remain in the safe set. None is designed against the criterion that actually decides task success when the controlled object is a learned policy: **will the policy still recognize the state it is in.** Those two criteria only come apart for learned policies, which is why the control literature never had to notice.

Three refinements of "minimally invasive" now exist, at three scopes, and they compose:

| Refinement | Source | Filter what? |
|---|---|---|
| **Task consistency** | [OSCBF](../../sources/oscbf-paper.md) | The task-hierarchy output (operational-space + null-space accelerations), not the raw control input |
| **Path consistency** | [PACS](../../sources/pacs-paper.md) | Speed along the intended trajectory, never direction |
| **Selection, not correction** | [FOREWARN](../../sources/forewarn-paper.md) | Nothing — choose among the policy's own samples |

## What is wrong with all of them at once

### 1. Every layer assumes perception it does not do

Keep-out boxes and arm/table geometry are authored from a URDF ([the deployed envelope](../../concepts/robotics/operational-space-control.md)). Sphere decompositions of robot and environment are inputs ([OSCBF](../../sources/oscbf-paper.md)). Object poses arrive with bounded measurement error and bounded velocity sets ([PACS](../../sources/pacs-paper.md)). FOREWARN's world model imagines outcomes for the objects it was trained on.

In a lab that is a modelling choice. In a home, **the hazards are precisely the things nobody modelled** — the cat, the child leaning in, the glass that was not there yesterday. Real-time perception → constraint geometry is named as future work by two of the six papers and simply absent from the rest. It is the single shared blocker.

> [!warning] Correction, 2026-08-16 — "the single shared blocker" overstates it; the research answer exists
> **Latent Safety Filters** (Nakamura, Bajcsy et al., arXiv 2502.00935) generalize **Hamilton–Jacobi reachability into the latent space of a generative world model**, so safety analysis runs on raw RGB observations and *"nuanced constraint specification"* becomes **a classification problem in latent space**. Its explicit target is failures *"hard — if not impossible — to write down by hand, but… intuitively identified from high-dimensional observations"*: on a Franka Research 3 it prevents **spilling the contents of a bag** and **toppling cluttered objects**, safeguarding generative policies and direct teleoperation. Follow-ups: **Uncertainty-aware Latent Safety Filters for Avoiding Out-of-Distribution Failures** (2505.00779) and **What You Don't Know Can Hurt You: How Well do Latent Safety Filters Understand Partially Observable Safety Constraints?** (2510.06492). **None ingested.**
>
> The honest form of this section is narrower: **the six sources synthesized here all consume hand-authored hazard geometry, and a separate line of work — from the same lab as [FOREWARN](../../sources/forewarn-paper.md) — is removing that assumption.** Whether latent reachability holds up beyond its demonstrated hazards is the open question; whether anyone is trying is not.

### 2. Every guarantee runs in the direction that protects throughput

[OSCBF](../../sources/oscbf-paper.md) proves forward invariance — and concedes that with many constraints and input limits the QP goes infeasible and the relaxed version *"enforces (but does not guarantee) safety in most cases."* All three detectors calibrate with conformal prediction, which bounds the **false-alarm** rate; bounding the **miss** rate would require failure data, the very thing they are built to avoid.

So the guarantees available at runtime say *"we will rarely stop you unnecessarily."* None says *"we will rarely fail to stop you."* That asymmetry is structural — it follows from having only successful data — and it is worth naming plainly, because a safety argument built on these guarantees is built on the wrong tail.

### 3. The numbers plateau in the same band, and the layers are not equally mature

Physical prevention is close to solved *for hazards you can write down*: [OSCBF](../../sources/oscbf-paper.md) holds 168 constraints at ~3 kHz; [PACS](../../sources/pacs-paper.md) reaches **zero** violations against 56% of timesteps unguarded. Task-level detection is not close: **~0.78 average accuracy** ([FIPER](../../sources/fiper-paper.md), beating 0.69 and 0.68 for the prior state of the art), ~0.72–0.78 for [FAIL-Detect](../../sources/fail-detect-paper.md), with Sentinel higher on its own domains. Three papers, three groups, same band.

The gap is informative. **Physics is enumerable and task success is not** — which is the same reason prevention can offer a proof and detection can only offer a calibrated threshold.

### 4. Sample sizes are too small to rank anything

20 trials per cell (FOREWARN), 30 (PACS), 50 real rollouts (FAIL-Detect), 10 calibration rollouts (Sentinel, FIPER real). Per the [success-rate audit](vla-success-rate-audit.md), ±2 pp needs ~1,000 rollouts. What survives at these n's are the **order-of-magnitude** effects — 0.04 vs 0.72, 0.00 vs 0.80 safe success, 0.00 vs 0.80 on novel task descriptions — and those are the ones this page relies on. The rankings among close cells do not survive, and no paper here claims otherwise loudly enough.

## The composition nobody has built — and a hazard in building it

Every one of the six papers names the missing piece, from its own side:

- [FOREWARN](../../sources/forewarn-paper.md) assumes a good plan is among its candidates, and names detecting *"if none of the policy's generated action plans are suitable"* as future work — that is a **monitor's** job.
- [FIPER](../../sources/fiper-paper.md) predicts failure so as to enable *"timely intervention or safe fallbacks or [asking] human experts"* — none implemented; **that is FOREWARN's job**, and the same first author wrote the intervention paper (PACS).
- [Sentinel](../../sources/sentinel-paper.md) and [FAIL-Detect](../../sources/fail-detect-paper.md) raise a flag and stop.
- [OSCBF](../../sources/oscbf-paper.md) and [PACS](../../sources/pacs-paper.md) never learn whether the task succeeded.

The obvious system is a loop: **monitor predicts trouble → steering picks a better mode → if no mode is acceptable, escalate → filter guarantees nothing catastrophic happens meanwhile.**

> [!warning] Correction, 2026-08-16 — one arc of that loop is already built
> **Rewind-IL** (Zheng, Seenivasan, Johnson-Roberson & Zhi, arXiv 2604.16683, April 2026) closes detection→recovery: **TIDE**, a temporal inter-chunk discrepancy score (the same action-chunk-overlap signal as STAC) calibrated by **split conformal prediction**, plus an offline **VLM-built database of recovery checkpoints** from the demonstrations — so on detection the robot **rewinds to the latest verified safe state** and restarts inference from a clean policy state. Real and simulated long-horizon manipulation, with transfer to flow-matching policies. **Not ingested.**
>
> It also answers the "nobody has crossed the two monitor designs" item elsewhere in this wiki: TIDE + conformal calibration *is* Sentinel's signal with better thresholding.

> [!warning] The layers can fight each other, and it looks like this
> **A path-consistent safety filter brakes to a stop when a human comes near. A task-progression monitor is built to detect a policy that has stalled and is making no progress.** These are the same observable behavior.
>
> [PACS](../../sources/pacs-paper.md)'s correct, safety-preserving action — slow to zero along the path — is indistinguishable from the exact failure mode [Sentinel](../../sources/sentinel-paper.md)'s VLM monitor is designed to catch (*"the robot is failing to make progress on the task"*), and from the *"prolonged high action uncertainty"* a policy exhibits when it is stuck. **Confidence: this is the one claim on this page that a targeted literature search did not falsify** — and that is weak evidence, since three neighbouring claims *were* falsified the first time they were checked. Published work recognizes the ingredients separately (safety filters are widely noted to be **overly conservative**, especially under partial observability — 2510.06492, 2606.02562; monitors are noted to fire on benign situations). What no source found names is the **composition**: that a filter's correct intervention is a monitor's positive class.
>
> The general form: **a monitor watching a filtered policy is not watching the policy.** It sees the composition, and the composition's healthy behavior includes states that look pathological in isolation. Any real stack needs the filter to *tell* the monitor when it is intervening — which is an interface neither literature has, and which is cheap to add only if someone notices before building it.

A second, subtler collision: [FIPER](../../sources/fiper-paper.md)'s ACE score fires on **prolonged high entropy in the action distribution**, and [Sentinel](../../sources/sentinel-paper.md)'s STAC fires when **consecutive action distributions diverge** — which FIPER argues happens exactly when a multimodal policy *commits to a mode*. But [FOREWARN](../../sources/forewarn-paper.md)'s steering deliberately samples 100 plans, clusters them into 6 modes, and forces a commitment every cycle. **A steered policy will look, to both monitors, like a policy in trouble.**

## What this implies for anyone building on top

1. **Pick your intervention so it never leaves the policy's output distribution.** Brake, or select among samples. Do not correct.
2. **Budget for perception separately.** Every layer here is a consumer of hazard geometry, not a producer of it, and that is where the deployment work actually is.
3. **Instrument the interfaces before you need them.** A filter that intervenes silently will be diagnosed as a failing policy.
4. **Report [safe success](../../concepts/robotics/safety-filters.md), not success.** Unguarded policies in [PACS](../../sources/pacs-paper.md) scored 0.79 task success and **0.00** success-while-safe. Every success rate in this wiki was collected with nothing being enforced.
5. **Do not read a conformal guarantee as a safety guarantee.** It bounds false alarms.

## Adjacent work this page does not draw on

Identified 2026-08-16 by targeted search, not ingested:

- **Deployment-Time Reliability of Learned Robot Policies** — **Christopher Agia's Stanford PhD dissertation** (2026-03, 182 pp), by [Sentinel](../../sources/sentinel-paper.md)'s first author. It cuts the problem differently: **runtime monitoring**, **policy interpretability** (tracing a runtime failure back to the influential *training data* via influence functions), and **long-horizon coordination**. The middle class is a mechanism this wiki has no coverage of at all.
- **Safe Embodied AI for Long-horizon Tasks: A Cross-layer Analysis of Robotic Manipulation** (2606.05660) — a survey organizing safety by **temporal locus** (planning-time / policy-time / execution-time) and arguing that *"semantic misgrounding, subtask-level error propagation, execution drift, and contact-rich physical risk **accumulate within the same closed-loop system**."* Same cross-layer instinct as this page, cut by *when* a mechanism acts rather than by *what question it answers* — **so this page is not the first to argue the layers interact.**
- **Formal Methods in Robot Policy Learning and Verification: A Survey** (2602.06971).
- The VLA-monitoring line — **SAFE** (NeurIPS 2025), **VLA-FAIL**, **Hide-and-Seek in Trajectories**, **VLAConf**, **ActProbe** — see [runtime failure detection](../../concepts/robotics/runtime-failure-detection.md).

## Sources synthesized

| Source | Layer | Venue |
|---|---|---|
| [Diffusion Policy App. D.1](../../sources/diffusion-policy-paper.md) / [TRI LBM](../../sources/tri-lbm-paper.md) | prevention (deployed, no guarantee) | RSS 2023 / Science Robotics 2026 |
| [OSCBF](../../sources/oscbf-paper.md) | prevention (forward invariance) | IROS 2025 |
| [PACS](../../sources/pacs-paper.md) | prevention (reachability, path-consistent) | ICRA 2026 |
| [Sentinel](../../sources/sentinel-paper.md) | detection (consistency + VLM) | CoRL 2024 |
| [FAIL-Detect](../../sources/fail-detect-paper.md) | detection (learned score + CP band) | RSS 2025 |
| [FIPER](../../sources/fiper-paper.md) | prediction (OOD ∧ action entropy) | NeurIPS 2025 |
| [FOREWARN](../../sources/forewarn-paper.md) | intervention (world model + VLM steering) | arXiv 2025 |

## Related

- [Safety filters for learned policies](../../concepts/robotics/safety-filters.md) — layer 1 in detail.
- [Runtime failure detection](../../concepts/robotics/runtime-failure-detection.md) — layers 2 and 3 in detail.
- [Operational space control](../../concepts/robotics/operational-space-control.md) — the control formulation underneath layer 1.
- [Robot policy evaluation](../../concepts/robotics/robot-policy-evaluation.md) · [success-rate audit](vla-success-rate-audit.md) — why the sample sizes matter.
- [Control-rate ladder](control-rate-ladder.md) — the frequencies these layers run at, and why the slow ones are safe.
- [Robot safety standards](../../concepts/robotics/robot-safety-standards.md) — what would have to be true for any of this to be certifiable.
