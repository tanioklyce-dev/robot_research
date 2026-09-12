---
title: Towards Safe Robot Foundation Models (Tölle, Gruner, Palenicek, Günster, Liu, Watson, Tateo, Peters; 2025)
type: source
url: https://arxiv.org/abs/2503.07404
fetch_url: https://arxiv.org/pdf/2503.07404v1
author: Maximilian Tölle, Theo Gruner, Daniel Palenicek, Jonas Günster, Puze Liu, Joe Watson, Davide Tateo, Jan Peters
published: 2025-03-10
ingested: 2026-09-11
venue: arXiv (v1; 3 pp. + references; workshop-length)
local_path: raw/2503.07404v1.pdf
sha256: 449a63b374e750bded44667dff9abb43349bdb0056688616dc7d2bbd7eb81173
format: pdf
tags: [safety-filter, atacom, constraint-manifold, safe-rl, vla, octo, air-hockey, tu-darmstadt, peters, behavior-cloning, control-affine, physical-safety]
---

## Summary

A three-page argument with one experiment, from Jan Peters's group: **a robot foundation model trained by behavior cloning on safe demonstrations is not safe**, and the fix is a deterministic layer *outside* the policy. The layer is **ATACOM** (Liu, Tateo, Bou-Ammar, Peters; CoRL 2021 / 2024): given a control-affine model ṡ = f(s) + G(s)a and C¹ constraints g(x) ≤ 0, it constructs the manifold of safe configurations and projects any proposed action into its tangent space, so every state transition stays inside the constraints — a_safe = ψ(a, s, g) with a ∼ π_VLA. On a real air-hockey table, an **Octo** policy fine-tuned by BC on expert data "heavily violates the constraints" (table surface, arm–table collision, joint limits) — and its violations **increase with more fine-tuning** — while the same policy behind ATACOM has **zero violations across all checkpoints and a rising success rate**, without conservative behavior. No fine-tuning of the policy for safety is required.

## Key claims

- **Requirements:** (1) access to the system state and a control-affine dynamics model; (2) constraints as continuously differentiable functions. The authors argue most OXE manipulators satisfy (1) as rigid bodies, and that practitioners can write (2).
- **Mechanism:** actions are mapped into the tangent space of the constraint manifold (ATACOM's "acting on the tangent space"); the VLA's end-effector x-y velocities go through inverse kinematics to joint velocities, ATACOM maps those to safe joint velocities, then a joint-space controller executes.
- **Experiment (Fig. 2):** Octo fine-tuned in MuJoCo and on the real system with data from an expert policy that did *not* use ATACOM. Baseline: max constraint violation grows over training checkpoints (1–5 × 10⁴ steps) while success stays lower. ATACOM + Octo: violation flat at zero, success improving. "ATACOM does not generate overly conservative control actions."
- **The point about data bias:** "Given that expert data predominantly consists of safe demonstrations, RFMs may implicitly reflect a notion of safety… it does not provide any formal safety guarantees," and distribution shift can "catastrophically damage the robot."
- **Open direction:** automating constraint specification with VLMs; so far VLMs have only added *semantic* constraints ("keep the cup upright") to a hand-written set (Santos et al. 2024; Brunke et al. 2024). "How a more generalizable concept of safety can be formulated… across different embodiments, environments, and tasks" remains open.

## Reading it against the wiki

- **This is the loop's "act, through a physical safety filter," demonstrated on a VLA.** The [overview](../overview.md)'s reworded loop and the [safety-filter](../concepts/robotics/safety-filters.md) page both hold that safety is a deterministic veto outside the learned system; this paper is the first source in the wiki to put such a veto behind a *foundation-model* policy on hardware and show the policy's own "safety from safe data" is not real. The violation-increases-with-training observation is the sharpest version of that.
- **It is a filter of the "constraint manifold" type**, distinct from the CBF, reachability, and predictive filters on the [safety-filter](../concepts/robotics/safety-filters.md) page; its path-consistency behavior — the axis that page argues predicts whether a filter destroys the policy — is reported only as "not overly conservative," with no quantitative task-performance comparison against the unfiltered policy at matched safety.
- **Requirement 2 is the same wall the [semantic-safety](../concepts/safety/semantic-safety.md) page hits from the other side:** the physical veto works because its constraints are written by hand; the semantic veto has no enforcement because its constraints cannot be. The authors name VLM-authored constraints as the bridge and note it has only ever been done additively.
- Air hockey is a 2-D planar task with a fully known model; the requirements list is what will not survive contact with a home.

## Entities mentioned

- Jan Peters, TU Darmstadt / DFKI / hessian.AI (no pages); Octo (no page; see [OpenVLA](../entities/openvla.md) for the sibling); [Open X-Embodiment](../entities/open-x-embodiment.md) as the manipulator population the requirements are checked against.

## Concepts touched

- [Safety filters](../concepts/robotics/safety-filters.md), [safety certificates](../concepts/robotics/safety-certificates.md), [semantic safety](../concepts/safety/semantic-safety.md), [VLA models](../concepts/learning/vla-models.md), [imitation learning](../concepts/learning/imitation-learning.md) (the safe-data fallacy).

## Open questions

- Success-rate cost of the filter at matched checkpoints — Fig. 2 shows ATACOM+Octo *higher*, which needs explaining (the filter may be keeping the policy in-distribution).
- ATACOM's own papers (2021, 2024) are not ingested; the mechanism is summarized secondhand here.
