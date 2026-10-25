---
title: "Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents (Wang, Jiang, Deng, …, Abbeel, Qi, 2026)"
type: source
url: https://arxiv.org/abs/2610.02204
fetch_url: https://arxiv.org/pdf/2610.02204v1
local_path: raw/2610.02204v1.pdf
sha256: 93feecda4aa9f514398bf49f8e6494173cbfee6a6f6ca5e34520b1dd46efbffa
author: Yen-Jen Wang, Haozhe Jiang, Shuying Deng, Haoru Xue, Weirui Ye, Rocky Duan, Nika Haghtalab, S. Shankar Sastry, Pieter Abbeel, Haozhi Qi
published: 2026-10-01
ingested: 2026-10-24
venue: arXiv (cs.RO), v1
format: "paper, 17 pp (8 main + appendices). Affiliations: UC Berkeley, Amazon FAR, MIT, U. Chicago. Project: rpg-robot.github.io (not inspected)."
tags: [rpg, code-as-policy, agent-as-policy, self-improvement, skill-library, system-prompt, privileged-information, video-analysis, regression-gate, simulation-practice, mujoco, yam, aspire, cap-x, rats, bimanual, cloth-folding, sim-to-real, fable-5-1, gemini-3-8-flash]
---

# Reconstruct, Practice, Go Real (RPG) — guided self-improvement for embodied agents (2026-10-01)

## Summary

[RPG](../entities/rpg.md) improves a [code-as-policy](../concepts/agents/code-as-policy.md) robot system **without touching model weights**. What it edits is a **shared skill library** (Python) and the **runtime system prompt**, through autonomous practice in simulation. It runs in three stages:
1. **Reconstruct.** A Constructor agent reads videos and descriptions from an offline dataset (ABC, 193 tasks). It builds related **MuJoCo practice tasks** for a bimanual [YAM](../entities/yam.md) robot, each with a `check_success` evaluator that **humans verify** before practice begins.
2. **Practice.** The **Runtime Agent** (deployable observations only) and the **Privileged Agent** (same model and skills, plus simulator state) run the tasks. A **Video Analyzer** compares the two runs against dataset videos and pins down the first failure. An **Implementor** proposes skill and prompt revisions. A **Merger** combines the ones that pass a **cross-task regression gate**.
3. **Go Real.** The system is calibrated, frozen and deployed.

**Results:**
- On held-out seeds of 22 tasks, success rises from **28.6% after round 1 to 95.0% after round 15**. That beats [ASPIRE](../entities/aspire.md) (75.5%), RATs (41.8%) and [CaP-Agent0](../entities/cap-x.md) with every model tried; the best is GPT-6 Astra Pro at 60.0%.
- On the physical robot: **30/30 trials** on three tasks.

## Key claims

### The loop (§III)
- **Initial library:** 9 low-level CaP-X tools (state, perception, IK, motion, gripper) plus 6 skills built from dataset trajectories (pick, place, pick-and-place, table-supported transfer, move-above, push): 15 entries.
- **Practice tasks are not replays.** *"Organize sunglasses"* becomes *"close the case"* with opening and loading encoded in the initial state; *"Roll towels"* becomes *"fold once"*. The Constructor gets **7.5 min per source task** and searches online for assets.
- **Privileged execution as a diagnostic, not a teacher.** Unlike asymmetric actor-critic, privileged state is used in a *separate* rollout. Where the privileged agent succeeds, it shows what to fix. Where both fail, it exposes a shared-skill defect.
- **Candidate checks before testing:** the revision loads, has valid syntax and interfaces, and **uses only deploy-time observations**.
- **The gate (Eq. 2):** a candidate is eligible only if **mean success rises and no task drops by more than 20 pp** (one success in five) over the 22 × 5 = 110 development episodes. Merged revisions must pass the same gate again. Validation and feedback-held-out tasks act as regression checks only.
- **Humans** handle setup, evaluator checks, the decision to stop, and hardware adaptation.

### Results (§IV)
- **Models:** **Fable 5.1** does the offline code revision and video analysis; **Gemini 3.8 Flash** runs online. Baselines are reproduced from released code. Budgets: 30 model turns for RPG and ASPIRE, 50 for CaP-Agent0 and RATs; 1,200 s wall time.
- **The learning curve (Fig. 4):** 28.6% → 43.2% (r3) → **73.6% (r4)** → 78.2% (r5) → 95.0% (r15).
  - **The single largest jump, +30.5 pp in round 4, was a prompt-only change**: a bounded perception–action loop plus budget tracking, *"encouraging the agent to act on its current estimates instead of repeatedly requesting observations."*
  - After the prompt froze (r4), skills drove another +21.4 pp.
  - The library grew **15 → 38** (23 added, 66 modified).
  - The curve is not monotonic: −1 success at rounds 6 and 14, which passed the 5-seed gate but not the 10-seed held-out check.
- **Table II (10 held-out seeds × 22 tasks):**
  - RPG 209/220. ASPIRE 166. CaP-Agent0 with GPT-6 Astra Pro 132, Fable 5.1 108, Gemini 3.8 Flash 107, Opus 5 100. RATs 92.
  - **Model choice alone moves CaP-Agent0 by 32 successes; RPG's system revisions move the same Gemini Flash runtime by 102.**
  - Largest gains over ASPIRE: insert into fixture (10 vs 2) and place bottles in bin (10 vs 3).
- **Ablation (Table III, 5 rounds):** full 78.2%; no Video Analyzer 51.8%; no Privileged Agent 50.9%; neither 50.9%. **Each component alone is worth ~nothing; together they add ~27 pp.**
- **Library-only test (Table IV), runtime fixed:** 26/40 → 37/40. One repaired bug: the lift skill *reported the commanded 6 cm while moving only 4.6–5.1 cm*. 12/13 lift calls failed before the fix and 11/11 succeeded after. One local regression appeared: ABC sorting 6/6 → 5/6.
- **Deformables remain the hard case:** 7 of 11 RPG failures are towel folding (3/10 in Table II). The standard fold peaks at 5/10 in sim; a 1 cm-tolerance variant stays at **0/10 for all 15 rounds** (App. F).
- **Physical (Table V; YAM; 10 trials each; low reasoning effort; common calibration):**

  | Task | CaP Gemini | CaP GPT-6 | RPG |
  |---|---|---|---|
  | Store ball in drawer | 3/10 | 4/10 | **10/10** |
  | Fold towel | 0/10 | 9/10 | **10/10** |
  | Transfer bowl | 0/10 | 1/10 | **10/10** |

  Five more tasks (scissors, uncap marker, tissue, whiteboard, bottle cap) are shown qualitatively, zero-shot.
- **Limitations stated:** API rate limits constrain parallel rollouts; overlapping revisions to shared skills complicate integration as the task set grows.

## Reading notes (wiki inference)

> [!warning] The physical towel result uses an easier criterion
> The paper says so itself: *"the physical folding criterion is defined independently of the simulation criterion and is not intended to match its difficulty."* In sim, towel folding is RPG's worst task (3/10, peaking at 5/10). On hardware it is 10/10 under a footprint-ratio-and-parallel-sides check. Read the 30/30 as "three tasks pass their physical criteria", not as evidence that sim-hard deformable skills transferred.

- **The biggest single gain came from the prompt, not the skills.** The +30.5 pp prompt revision (act on current estimates, track the observation budget) is a harness fix. That is the same lesson as the wiki's [harness-design](../concepts/agents/local-model-harness-design.md) material: how the agent spends its turns matters as much as what tools it has.
- **The lift bug is the canonical case for "verify measured effects, not commands".** A skill that returns the commanded displacement as the achieved one makes every downstream decision wrong. The repaired skill checks actual displacement, grasp retention and levelness, the "precondition / verification / recovery" corrections in App. Table VIII. For the wiki's own skill-based stacks ([ros2-mcp-server](../entities/ros2-mcp-server.md), [stretch_ai](../entities/stretch-ai.md)), this is a cheap audit to run.
- **This is a research flywheel with a regression gate.** Fixed, human-checked evaluators; candidates that must improve the mean without dropping any task more than 20 pp; merged changes re-gated; held-out seeds kept out of checkpoint selection. It is the closest published template in the wiki for autonomous improvement loops, with the same guardrails [autoresearch](karpathy-autoresearch.md) uses (agent cannot edit the evaluator).
- **Model is not the bottleneck at this level.** Across four frontier models, CaP-Agent0 spans 45.5–60.0%. RPG on a Flash-class runtime reaches 95.0%. The persistent system (skills + prompt) is the lever, which bears on whether a smaller local model can run such a loop's *runtime*. The *improvement* side here used Fable 5.1.
- Evidence quality: one improvement run (the authors note rounds are not matched compute); 10 held-out seeds per task, paired across methods; baselines re-run from released code. The physical evaluation is 10 trials × 3 tasks with manually reproduced initial states.

## Entities mentioned
- [RPG](../entities/rpg.md) · [ASPIRE](../entities/aspire.md) · [CaP-X](../entities/cap-x.md) · [Voyager](../entities/voyager.md) (lineage) · [YAM](../entities/yam.md) (robot)

## Concepts touched
- [Code as policy](../concepts/agents/code-as-policy.md): agent-as-policy plus a self-revising skill library.
- [Agent skills](../concepts/agents/agent-skills.md): skills as persistent, regression-gated code.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md): six specialised agents (Constructor, Runtime, Privileged, Video Analyzer, Implementor, Merger).
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md): the system is frozen after sim practice; only calibration on hardware.

## Open questions
- Cost: tokens, API spend and wall-clock per practice round are not reported, only that rate limits bind.
- Would a regression gate stricter than "−20 pp per task" have prevented the round-6 and round-14 held-out drops, and at what cost to progress?
- How much of the 95% survives a **different** evaluator than the one the Constructor wrote and humans checked? The gate optimises against those evaluators.
- Deformables: the loop plateaus on folding. Is that a skill-abstraction limit (code can't express it) or a perception limit?
