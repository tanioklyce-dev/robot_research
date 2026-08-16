---
title: Task and motion planning (TAMP)
type: concept
created: 2026-07-04
updated: 2026-08-16
sources: 3
tags: [tamp, task-planning, long-horizon, plan-skeletons, explicit-model, hybrid-planning]
---

**Task and motion planning (TAMP)** — solving long-horizon, multi-step robot tasks by combining high-level symbolic task planning (which subtasks, in what order) with low-level motion planning (how each subtask is physically executed). The classical answer to the long-horizon problem that both RL and behavior cloning still struggle with.

## Structure ([Bekris et al. 2024](../../sources/state-of-robot-motion-generation-2024.md) §2.2)

- Low-level **operators with motion constraints** + high-level **logical relationships**, **lifted variables**, and **plan skeletons**.
- Methods categorized by how they order sequencing vs satisfying: **sequencing-first**, **satisfying-first**, **interleaved**.
- Critical weaknesses: relies on human engineering of preconditions/effects; expensive combinatorial reasoning; struggles under partial observability; cannot anticipate unprogrammed changes (§4).

## The learned-stack echo

The TAMP decomposition keeps re-emerging inside learned systems:

- **LLM-as-task-planner** — SayCan / SayPlan-style stacks (and the wiki's own [Stretch AI LLM agent](../../sources/stretch-ai-llm-agent-docs.md), [Spot + Gemini Robotics](../../sources/bostondynamics-spot-gemini-robotics.md)) put an LLM in the symbolic-planner slot and skills/policies in the operator slot — TAMP with learned components. [Bekris et al. 2024](../../sources/state-of-robot-motion-generation-2024.md) cite SayPlan (LLM plans verified by a model with classical pose-level planning) and ReKep (VLM-generated 3D keypoint constraints guiding motion planning) as the existing hybrid successes.
- **Hierarchical world-model planning** — [HWM](../../entities/hwm.md)'s two-temporal-scale latent MPC (macro-actions → subgoals → primitive actions) is the TAMP shape rebuilt inside a learned latent space.
- **System 2 / System 1 VLAs** — [GR00T N1](../../sources/groot-n1-paper.md)-style dual systems put deliberative reasoning above a fast motor policy; the layering (deliberate → execute) is TAMP's, though without symbolic guarantees.

## Current state

Classical TAMP is mature but engineering-heavy and brittle under partial observability ([Bekris et al. 2024](../../sources/state-of-robot-motion-generation-2024.md) §4). The live research direction is hybridization: dynamically defined pre/postconditions, skill discovery, failure explanation, and LLM/VLM front-ends over classical motion-level guarantees. No pure-TAMP source is in the wiki yet; this page exists because the pattern keeps recurring in the learned stack.

## Key references

- [The State of Robot Motion Generation (Bekris et al. 2024)](../../sources/state-of-robot-motion-generation-2024.md) — §2.2 + §4.
- Garrett et al., "Integrated Task and Motion Planning" (Annual Review of Control 2021) — the standard dedicated survey; not in `raw/`.

## Related concepts

- [Motion planning](motion-planning.md) — the layer below.
- [LLM-agent architecture](../agents/llm-agent-architecture.md) — LLM-planner stacks as neo-TAMP.
- [Optimal control](optimal-control.md) — the control-theoretic substrate of the motion layer.

## TAMP inside a graph of convex sets

[GCS](graphs-of-convex-sets.md) is normally filed as a motion planner, but its combinatorial half is a task-planning surface. [Tedrake's 2024 seminar](../../sources/tedrake-gcs-foundation-models-talk.md) reports a box-shuffling instance where the right combinatorial object was **not a shortest path but a walk on the permutohedron** — because the order the boxes move in does not matter, so the network-flow problem underneath is a different one.

The generalizable move, stated twice in that talk: **shrink your sets to points and ask which classical network-flow problem you are left with.** If that flow has a strong convex formulation, its GCS extension — same combinatorics, now with continuous variables in each vertex — is likely to inherit the tightness. If it is NP-hard with only approximations (TSP), GCS will not rescue it.

That is a different integration story than the classical TAMP stack's: instead of a symbolic layer *calling* a motion planner, the discrete and continuous problems are **one optimization**, and the plan skeleton falls out of the same relaxation that produces the trajectory. It also inherits GCS's per-query optimality certificate, which is a rare thing for a task planner to be able to report.

## Mentioned in

- [The State of Robot Motion Generation (Bekris et al. 2024)](../../sources/state-of-robot-motion-generation-2024.md)
- [Planning with Graphs of Convex Sets (in the age of foundation models)](../../sources/tedrake-gcs-foundation-models-talk.md) — the permutohedron instance and the network-flow heuristic.
