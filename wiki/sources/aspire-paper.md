---
title: "ASPIRE: Agentic Skills Discovery for Robotics"
type: source
url: https://arxiv.org/abs/2607.00272
author: "Runyu Lu, Yubo Wu, Ethan Kou, Letian Fu, Wenli Xiao, Ajay Mandlekar, Yinzhen Xu, Guanya Shi, Ken Goldberg, Ang Chen, Mosharaf Chowdhury, Yuke Zhu, Linxi \"Jim\" Fan, Guanzhi Wang"
affiliation: NVIDIA (GEAR), University of Michigan, UIUC, UC Berkeley, Carnegie Mellon University
published: 2026-06-30
ingested: 2026-08-03
venue: arXiv preprint (v1)
format: research paper (43 pp with appendices)
local_path: raw/2607.00272.pdf
tags: [code-as-policy, skill-library, continual-learning, llm-agent, evolutionary-search, libero-pro, behavior, robosuite, sim-to-real, cross-embodiment, nvidia-gear, claude-opus, primary-source]
---

## Summary

**ASPIRE** (*Agentic Skill Programming through Iterative Robot Exploration*) is a continual-learning system that autonomously writes and repairs robot control programs in the [code-as-policy](../concepts/agents/code-as-policy.md) paradigm while **compounding validated repairs into a reusable skill library**. It is the wiki's first ingested system to close [Voyager](../concepts/agents/code-as-policy.md)'s open-ended skill-library loop on *robotics* with measured results, and it is built directly on top of **[CaP-X](cap-x-paper.md)**, whose CaP-Agent0 is its primary baseline.

The paper's diagnosis of why prior robotic coding agents plateau is precise and is the actual contribution: **the feedback channel, not the model, is the bottleneck.** A failed rollout tells the agent the task failed but not *whether the root cause was perception, grasp stability, planning, or recovery*. ASPIRE replaces coarse rollout-level feedback with **per-primitive multimodal traces** — for every perception, planning, grasping, and control call it records inputs, outputs, return status, and visual evidence — letting the agent localize the failing subsystem the way a human robotics engineer would. Ablating this single component moves macro-average LIBERO-Pro success from **14% → 62%**; everything else in the system adds the last 10 points.

The framing sentence for the skill library: *"the agent solving its hundredth task is effectively no more experienced than the agent solving its first"* — the problem ASPIRE exists to fix.

## Key claims

### Three components (§2)

1. **Closed-loop robot execution engine** — per-primitive multimodal traces (RGB keyframes before/after each primitive call, perception overlays, grasp candidates, object poses, motion-planning results, return codes). The agent does *not* receive full video; it selectively inspects evidence around implicated calls. Repairs are re-executed for closed-loop validation.
2. **Continually expanding skill library** — stores *heterogeneous repair knowledge*, not whole task programs: localization heuristics, perception prompts, grasping constraints, navigation recovery, motion primitives, scene-understanding routines, debugging workflows. **The taxonomy is not prescribed in advance**; categories emerge. Each skill = failure signature + when-to-apply condition + repair strategy + optional code sketch.
3. **Evolutionary search** — proposes a population of *K* candidate programs conditioned on top performers and residual failure traces, to escape "local repair loops, where the agent repeatedly patches the same failed strategy."

**Architecture:** a **coordinator** spawns one **actor** coding agent per task. Actors never exchange chat histories or raw rollouts — only distilled skills flow through the shared library, keeping each actor's context focused. The coordinator audits actor findings, verifies API-policy compliance, and admits only validated reusable repairs.

**The worked example (Fig. 2)** — a BEHAVIOR-1K `navigate-and-pick-up-radio` failure — is the clearest illustration of trace-guided debugging in the wiki: perception *succeeds*, but `navigate_to_pose` repeatedly returns `PLANNING_ERROR` because sampled goals fall inside the table's collision-avoidance buffer (~20 cm of the edge). The agent diagnoses this from return values, writes a multi-angle approach routine that samples alternative directions around the object, and the validated fix is admitted as a general **Multi-Angle Approach** navigation skill — *not* a radio-pickup program.

### Setup (§3.1)

- Coding agent: **[Claude Code](../entities/anthropic.md) with Claude Opus 4.6 and a 1M-token context window**, fixed across all simulation experiments.
- Environment: **[CaP-X](cap-x-paper.md)**, on [MuJoCo Playground](../entities/mujoco-playground.md).
- Real-robot study: **OpenAI Codex GPT-5.5 in reasoning-xhigh mode** on a bimanual **[YAM](../entities/yam.md)** station — a *different* embodiment and API from simulation.

### Evaluation protocol — unusually well-disclosed, and asymmetric in ASPIRE's disfavor (§3.3)

Disjoint debug and evaluation seeds throughout:

| Benchmark | Learns on | Evaluates on | Programs generated |
|---|---|---|---|
| LIBERO-Pro | seeds 51–65 | seeds 1–50, ×10 tasks/suite | **one program per task** |
| Robosuite | seeds 101–125 | seeds 1–100 | **one program per task** |
| BEHAVIOR-1K | seeds 26–35 | seeds 1–25 | incremental block execution |

> [!note] The comparison is harder than it looks
> **ASPIRE generates one program per task and runs it across all held-out seeds. CaP-Agent0 regenerates a separate program for every seed, with test-time reasoning and retries.** The baseline gets per-instance adaptation that ASPIRE denies itself, so ASPIRE's wins are *understated* relative to a matched-compute comparison — the opposite of the usual direction.

### Results (§3.4)

**LIBERO-Pro**, macro-averaged over 10 tasks × 50 held-out seeds per suite/perturbation. Gains over the **strongest baseline in each suite**, averaging the Pos and Task axes:

| Suite | ASPIRE gain |
|---|---|
| Object | **+77 points** |
| Goal | **+41.5 points** |
| Spatial | **+42.5 points** |

[OpenVLA](../entities/openvla.md) and [π0](../entities/pi-zero.md) score **0** across these suites; π0.5 beats them on some position perturbations "but remains far below Aspire and largely collapses under task paraphrases" — independently reproducing [LIBERO-PRO](libero-pro-paper.md)'s central finding.

- **Robosuite** (100 held-out trials/task): near-saturated performance preserved on easier contact-rich tasks; **bimanual handover 20% → 92%**.
- **BEHAVIOR-1K** (25 seeds): outperforms *both* human experts and CaP-Agent0 on navigation and task success. Largest gain on `navigate-and-pick-up-radio`, **56% → 88%** task success. Several results across benchmarks "surpass programs written by human experts."

### Zero-shot cross-task transfer — the compounding claim, measured (§3.5)

Skill library accumulated on **LIBERO-90**, then applied to held-out **LIBERO-Pro Long** tasks with *no* additional debugging, retries, or library updates:

- ASPIRE **23%** on position perturbations, **38%** on task perturbations (≈31% overall) — **vs 4%** for prior methods "despite their reliance on test-time reasoning and retries."
- **Success rises with library size** across snapshots of N ∈ {0, 25, 50, 90} source tasks — the paper's direct evidence that "validated repairs from short-horizon tasks provide reusable robotic knowledge for longer-horizon compositions."

### Real-robot cross-embodiment skill transfer (§3.6, Table 1)

Three sim-discovered skills (soda-can pickup, bowl-on-plate, drawer push/pull) supplied as in-context guidance to a real bimanual YAM station with its own perception, calibration, and control stack. **20 evaluation trials per task**:

| Task | Total tokens w/o → w/ skills | Success w/o → w/ skills |
|---|---|---|
| Put bowl on plate | 8.65M → **5.11M** | 20/20 → 20/20 |
| Lift soda can | 61.94M → **6.58M** | 13/20 → **19/20** |
| Open/push drawer | 334.9M → **81.67M** | **0/20 → 11/20** |

The drawer row is the strongest single data point: without skill retrieval the agent **exhausts a larger token budget without ever producing a working program**. The paper is careful that this "is not a direct policy deployment" — the agent must still adapt programs through real-world execution feedback; what transfers is *guidance that reduces debugging*.

### Ablations (§3.7)

- **Robot execution engine: 14% → 62%** macro-average on LIBERO-Pro — by far the largest single component effect.
- **+ evolutionary search: → 72%.**
- Evolutionary search improves steadily over the first few rounds then shows **diminishing returns**.

## Entities mentioned
- [NVIDIA GEAR](../entities/nvidia-gear.md) · [NVIDIA](../entities/nvidia.md) · [Jim Fan](../entities/jim-fan.md) · [Yuke Zhu](../entities/yuke-zhu.md) · [Ken Goldberg](../entities/ken-goldberg.md) · [Letian (Max) Fu](../entities/letian-fu.md)
- [ASPIRE](../entities/aspire.md) · [CaP-X](../entities/cap-x.md) · [Robosuite](../entities/robosuite.md) · [LIBERO](../entities/libero.md) · [BEHAVIOR](../entities/behavior-benchmark.md) · [MuJoCo Playground](../entities/mujoco-playground.md)
- [Anthropic](../entities/anthropic.md) — Claude Code + Claude Opus 4.6 (1M context) is the coding agent for every simulation result.
- [YAM](../entities/yam.md) — the real bimanual platform · [OpenVLA](../entities/openvla.md) · [π0](../entities/pi-zero.md)

## Concepts touched
- [Code as policy](../concepts/agents/code-as-policy.md) — ASPIRE is the measured endpoint of the autonomous-revision branch.
- [Agent skills](../concepts/agents/agent-skills.md) — an *agent-authored* library, contrasted with hand-written SKILL.md bundles.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — coordinator/actor multi-agent structure.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — transfer of *debugging knowledge* rather than weights or trajectories.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — disjoint debug/eval seeds, one-program-per-task discipline.
- [Evolutionary computation](../concepts/alife/evolutionary-computation.md) — population-based search over programs.
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) · [VLA models](../concepts/learning/vla-models.md).

## Open questions

The paper's own **Limitations (§5)** are unusually candid and answer several questions the wiki was carrying:

- **Not a real-world lifelong learner yet.** Sim gives cheap programmatic success-checking and resets; real deployment "still requires robust success detection, safe reset, safety monitoring, and calibration maintenance." This is the concrete blocker between ASPIRE and anything like [Waddle](waddle-labs-introducing-waddle.md)'s claimed always-on deployed loop.
- **Depends on a frozen frontier LLM.** Claude Opus 4.6 with 1M context; "we have not verified that smaller or weaker LLMs can sustain the same debugging loop." Directly relevant to any on-robot or edge deployment.
- **The predefined API bounds expressible behavior.** "If a task requires sensing, control, or interaction capabilities outside the exposed primitives, the agent must either approximate them inefficiently or rely on humans to extend the API." → *This is the honest version of [Waddle](waddle-labs-introducing-waddle.md)'s "works with any arms, grippers, and camera setups" claim, and it confirms the wiki's standing suspicion that embodiment-specificity relocates into the primitive set rather than disappearing.*
- **Skill-library memory management is unsolved.** Entries "may become stale, overly specific, redundant, or misleading," which the authors offer as the explanation for **non-monotonic zero-shot transfer trends**. Retrieval, pruning, ranking, and re-validation are named as needed future work.
- **Compute-intensive.** Many LLM calls and rollouts per task; the real-robot table shows *hundreds of millions* of tokens for a single unaided drawer task.

Questions the wiki adds:

- **The token counts make the economics explicit and unflattering.** 81.67M tokens for an assisted drawer-opening program is the wiki's first hard cost figure for code-as-policy. Against a VLA that trains once and runs at inference for near-zero marginal cost, "training-free" is not "cost-free" — and no paper in this thread reports cost alongside success.
- **What is the human baseline here?** ASPIRE reports "several results surpassing programs written by human experts," but the human reference appears inherited from CaP-X, where it was **written by the authors** (N=7).
- **Does the skill library transfer across *model families*?** The library was built by Claude Opus 4.6 and consumed by GPT-5.5 on the real robot — which is suggestive evidence that it does, but the paper does not isolate it.

## Related sources
- [CaP-X](cap-x-paper.md) — the framework ASPIRE runs on and the baseline it beats.
- [Introducing Waddle](waddle-labs-introducing-waddle.md) — the commercial claim; ASPIRE's limitations section is the closest thing to an independent reality-check.
- [LIBERO-PRO](libero-pro-paper.md) — independently reproduced here (VLAs at 0 under perturbation).
- [Success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) — ASPIRE's gaps are large enough to survive it; see that page.
