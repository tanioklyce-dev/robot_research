---
title: "An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond (Zhang, Wang, Ouyang et al., 2026)"
type: source
url: https://arxiv.org/abs/2609.24170
local_path: raw/2609.24170v1.pdf
sha256: 6bb575e9327e6606c26fef453d19a5a1ece447eea3c83dc52e0b7d98509f3055
author: "Wenbo Zhang, Kaixuan Wang, Yutao Ouyang (equal contribution), Xiaoyu Huang, Liyang Li, Kailun Su, Weiyang Jin, Wenhao Chai, Haotian Liang, Zhiyang Dou, Yue Chen, Tianxing Chen — RoboProbe, RoboDojo, HKU, Tsinghua, UC Berkeley, Princeton, MIT, PKU"
published: 2026-09-21
venue: "arXiv preprint (cs.CV), v1; report at robodojo-benchmark.com/report/gpt-6-astra-eval; code github.com/RoboProbe/RoboProbe"
format: "24-page PDF: 7 sections + appendices A–I (prompt and tool interface, full 43-row board, ICL and perturbation protocols, real-robot diagnostics, humanoid, RoboPianist, limitations, ethics)"
tags: [gpt-6-astra, openai, gpt-5.5, deepseek, llm-as-policy, robodojo, xpolicylab, benchmark, leaderboard, direct-control, end-effector-control, zero-shot, in-context-learning, perturbation, active-perception, bimanual, arx-x5, piper, franka, humanoid, robopianist, shadow-hand, codex, hardware-damage, robot-safety, contamination]
ingested: 2026-11-07
---

# An Unexpected Robot Policy: GPT-6 Astra on RoboDojo

## Summary

The paper tests **"LLM as policy."** A frozen frontier language model picks every executable motion target itself. There is no pretrained motor policy in the loop and no task-specific fine-tuning, only non-learned inverse kinematics and joint-path planning between the model and the arm. It runs on all 42 [RoboDojo](../entities/robodojo.md) simulation tasks under the official protocol.

**[GPT-6 Astra](../entities/gpt-6-astra.md) scores 22.48% average success (28.97 Score) over 2,100 trials, ranking first against the 40 public policies** on the 2026-09-10 leaderboard. The best public entry, DM0.5, is at 19.34%. GPT-5.5 (0.88%) and DeepSeek-Flash (1.92%, 10 episodes per task) use the **same interface and post-processing**, roughly a 25-fold spread, so the conversion layer alone does not explain Astra's result.

The lead is uneven. Astra is far ahead on **Open** (31.0% vs ≤ 2.1% for the policies) and Generalization. It trails the fine-tuned policies on Precision, Long-Horizon and Memory, and scores 0% on several tasks where policies reach 60–90%.

Three further results:
- **One-shot demonstrations hurt.** Success falls from 22.9% to 17.9% with an image demonstration and to 12.9% with a text one.
- **It corrects itself within an episode.** Perturbation traces show it adjusting when its actions don't land.
- **Real hardware was stopped for safety.** The real-robot campaign was halted after the model *"repeatedly issued physically unreasonable or unsafe actions, including incidents that damaged hardware."*

The authors call it initial evidence for a general-purpose manipulation model, and are careful about the limits.

## Key claims

### Setup (§3, App. A)
- **Definition (§3.1).** There is no learned policy between the LLM and the robot, and the weights stay frozen. Cartesian targets may be converted by IK because *"this conversion is geometric only."*
- **Tools.** Every turn the model must call either `move_eef` or `give_up`.
  - `move_eef` sets any subset of 14 world-frame grasp-point dimensions: xyz, pitch/roll/yaw and gripper for each arm. Naming both arms moves them together. Every call must carry a `note`.
  - **No pick, place or pregrasp primitives**, *"because they would solve part of the task outside the model."*
  - Non-learned software validates the target, converts it to a flange pose, plans and time-aligns the joint paths, and plays them at 25 Hz. Gripper changes come after the arm motion.
  - A rejected target returns an error and the robot does not move. An accepted one reports its duration, then the next observation reports how far the arm landed from the target.
- **Inputs.**
  - Three RGB views (head and both wrists), the 14-D grasp-point state, 12 read-only joint angles and the remaining step budget.
  - **No depth, privileged object poses, reward or layout information.**
  - Images are kept only for the **two most recent turns**; all text history is kept.
- **Budgets.** 100 LLM calls per episode (one per turn) plus the environment's step limit; motions cost steps in proportion to how far they travel. All runs use medium reasoning effort and one evaluation seed.
- **Prompt content the public policies did not get.** The Goal message adds a *"task recipe derived from the RoboDojo wiki"*: the capability axis, a description, and the **process-score ladder** (e.g. *"100: The target object is lifted at least 10 cm"*). The system prompt includes geometry notes and generic advice, including to use an idle wrist camera to look around. The public policies were not re-run with this text (§3.3, App. H).

### The leaderboard (§4.1, Table 1; Score/SR%)
| Rank | Entry | Average | Gen. | Prec. | Long-Hor. | Memory | Open |
|---|---|---|---|---|---|---|---|
| 1 | **GPT-6 Astra** | **28.97/22.48** | 33.36/30.50 | 12.65/4.00 | 21.45/8.25 | 43.04/38.67 | 34.36/31.00 |
| 2 | DM0.5 | 24.90/19.34 | 15.77/10.95 | 24.82/16.75 | 33.70/19.50 | 47.74/47.44 | 2.43/2.08 |
| 3 | GalaxeaVLA (G0.5) | 20.23/14.88 | 18.46/12.83 | 28.25/20.42 | 44.12/32.25 | 8.61/7.33 | 1.73/1.58 |
| 4 | Xiaomi-Robotics-1 | 20.07/13.93 | 23.54/17.00 | 26.69/18.83 | 38.39/23.67 | 7.81/6.56 | 3.94/3.58 |
| 5 | OpenWAM-α | 17.18/11.92 | … | | | | |
| 7 | Hy-Embodied-0.5-VLA | 13.07/8.80 | | | | | |
| 9 | [π0.5](../entities/pi-zero-5.md) | 11.41/6.91 | | | | | |
| 28 | DeepSeek-Flash† | 2.99/1.92 | | | | | |
| 33 | GPT-5.5 | 1.13/0.88 | | | | | |

- **The board has moved since the RoboDojo paper.** Hy-Embodied-0.5-VLA's 8.80%, the best result when the paper was frozen on 2026-07-03, is now 7th. DM0.5, G0.5, Xiaomi-Robotics-1, OpenWAM-α and Meituan-Robotics-0 are newer entries.
- **Pooled micro-average:** 472/2,100 = 22.48%. The leaderboard Average is the unweighted mean of the five axes.

### Where it wins and where it fails (§4.2–4.4, Table 2)
- **Astra ≥ 20% where every policy is < 5%:** push_T 60 (best policy 0.7), arrange_largest_number 60, align_blocks 50, solve_equation 40, stack_blocks_by_language 40, imitate_sorting_sequence 36, classify_objects_by_language 30.
- **Policy ≥ 20% where Astra is < 5%:** make_kong 0 (G0.5: 90), build_tower 2 (78.7), insert_tubes 0 (59.3), play_tic_tac_toe 0 (58.7), the two pouring tasks 4 (46 and 42), store_laptop_and_headphones 0, fill_pen_holder 0.
- **Behaviours observed** (each shown to occur; how often is not measured):
  - **Semantic matching** (make_kong tile choice).
  - **Active perception:** repositioning the other wrist camera when a held tube blocks the view. This follows the system-prompt advice, so it is not a discovered strategy.
  - **Concurrent bimanual holding.**
- **Failures.**
  - It misses moving conveyor targets.
  - Two-hand transfers fail.
  - It **knocks over its own tower while reaching for the next block.**
  - Errors in lift height, approach angle and correction timing even when the task is understood. The authors call this a shortfall in physical commonsense, citing [Generalist](../entities/generalist-ai.md)'s framing, but cannot separate it from perception or interface limits.

### Context (§4.5, App. C–D)
- **One-shot demonstrations** (340 matched task–layout pairs, 34 tasks, examples taken from other layouts): zero-shot 22.9%, image plus EEF demonstration **17.9%**, text demonstration **12.9%**. Demonstrations almost never unlocked a task that had zero successes zero-shot (2/150 with images, 0/150 with text). The losses came on tasks Astra could already do.
  - **The authors' hypotheses:** precision, not interpretation, is the bottleneck; or Astra copies layout-specific geometry from the example.
  - **What the authors do not claim:** that few-shot ICL fails in general.
- **Perturbations** (8 general_pickup layouts Astra already solves, so the baseline is 8/8 by construction):
  | Condition | Success |
  |---|---|
  | Top–bottom image flip | 8/8 |
  | Left–right mirror | 6/8 |
  | No head camera | 6/8 |
  | Right wrist camera only | 3/8 |
  | ~10 cm random per-move pose jitter | 3/8 |
  | Negated Cartesian axes | 4/8 |

  - **Traces.** Some show explicit re-assignment (*"the right arm is the one beside the scissors"*) and a written note that its forward/back estimate had been reversed.
  - **The authors' reading:** *"consistent with within-episode adaptation,"* with no history ablation to separate it from ordinary feedback control.

### Real hardware (§5, App. E, Ethics)
- **The official RoboDojo-Real protocol was not completed.** Testing stopped after repeated unsafe actions, *"including incidents that damaged hardware; no person was injured."*
- **Retained diagnostic sample** (selected around the safety stop): 33 trials on 12 tasks across ARX X5, [Piper](../entities/agilex-piper.md) and Piper X. Pooled **Score 6.97, SR 3.03%**; the only full success is one stack_bowls trial on Piper. The official real board for comparison: OpenWAM-α 24.40%, π0.5 12.80%, InternVLA-A1 7.20%.
- **Separate joint-position deployments** on a [Franka](../entities/franka-panda.md) and a two-arm humanoid used a different interface and are qualitative only (pouring, shelf placement, shirt folding, drawing). Operators noted that the model sometimes described dynamic corrections *"too late to execute them."*
- **Ethics statement:** the incidents *"motivate independent safety checks and stopping mechanisms rather than reliance on the model's judgment alone."*

### Beyond tabletop (§6, App. F–G)
- **Mobile humanoid:** walking, then grasping; walking, sitting and picking. Recordings only, no score, and not claimed to satisfy the strict definition.
- **RoboPianist** (two Shadow hands, 88 keys). Astra, **driven through the Codex scaffold** at high reasoning effort, *writes* a `play.py` controller that emits 45-D joint targets every 50 ms. It refines the controller through simulated practice, with no RL, no behaviour cloning and no human fingering annotations.
  - **Results:** Twinkle F1 0.907 with one hand and **0.902 with two** (33 tries, 34 min), against **0.886 for the RL reference**. A Chopin nocturne excerpt reaches 0.599.
  - **Transfer:** unseen C-major scale 0.903, D-major scale 0.556; transpositions by +2/−3 semitones lose ~0.22–0.25 F1.
  - **Isolation was by rule and audit, not sandbox:** *"The host had user namespaces disabled, so no system-level sandbox was available."* The audit counted 201 shell commands and zero network calls.

### Stated limitations (App. H)
- **One seed, three models.** The detailed analysis covers one model.
- **The interface is part of the measurement.**
  - `move_eef` cannot express continuous contact or non-quasi-static motion.
  - The input is RGB only.
  - `image_horizon = 2` means *"the Memory axis measures the model together with this context policy."*
- **Unequal input information** (the recipe and score ladder) versus the public policies, whose cells come from a snapshot that was not re-run.
- **Contamination** for a closed-weight model is *"unquantified rather than ruled out."*
- **Everything rests on one simulator.** No transfer to another simulator or to the official real protocol is shown.

## Entities mentioned
- [GPT-6 Astra](../entities/gpt-6-astra.md) · [OpenAI](../entities/openai.md) (GPT-5.5, Codex) · DeepSeek-Flash (no page)
- [RoboDojo](../entities/robodojo.md) · [XPolicyLab](../entities/xpolicylab.md) (the adapter `GPT_6_Astra_Direct_EEF`, and the leaderboard citation)
- Policies on the board: [π0.5](../entities/pi-zero-5.md), DM0.5, GalaxeaVLA G0.5, Xiaomi-Robotics-1, OpenWAM-α, Meituan-Robotics-0, Hy-Embodied-0.5-VLA, InternVLA-A1/A1.5 (mostly no pages)
- Embodiments: ARX X5, [AgileX Piper](../entities/agilex-piper.md), Piper X, [Franka Panda](../entities/franka-panda.md), Shadow Hand (RoboPianist)
- Cited prior work in the wiki: [How Claude performs on robotics tasks](anthropic-how-claude-performs-on-robotics-tasks.md) (LIBERO 0–5.5%), [Project Fetch phase two](anthropic-project-fetch-phase-two.md), [Generalist GEN-1.5](generalist-gen-1-5-blog.md), [Skild S1](skild-s1-blog.md), [DreamZero](dreamzero-paper.md)

## Concepts touched
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md): per-turn EEF targets through a non-learned planner sit between level 1 and level 2. That is where the Frontier Red Team found models weakest, and Astra is the first strong result there.
- [Code as policy](../concepts/agents/code-as-policy.md): the piano runs are level 2; the RoboDojo runs deliberately are not.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md): a leaderboard comparison with unequal inputs, one seed, and unquantified contamination.
- [AI guardrails](../concepts/safety/ai-guardrails.md): an evaluation whose real-robot arm had to be stopped because the model damaged hardware.

## Open questions
- **How much of the 22.48% is the recipe?** The public policies never saw the score ladder. An ablation without the wiki recipe would show whether Astra's Open/Generalization lead is semantic competence or instruction access. Fine-tuned VLAs couldn't use the text anyway, so the comparison is partly between information regimes.
- **Why does GPT-5.5 collapse to 0.88% with the identical interface?** That spread is the paper's strongest evidence that the planner isn't doing the work. It is also an unexplained cliff between consecutive frontier generations.
- **The safety gap.** It ranks first in sim and was stopped for damaging hardware in the real world. What were the incidents (speed, collisions, force)? Would the real-robot campaign be safe with a constrained controller of the kind the [control-abstraction-levels](../concepts/robotics/control-abstraction-levels.md) note describes (keep-out regions, joint limits, clearance)?
- **Latency and cost are not reported.** Up to 100 reasoning calls per episode over 2,100 episodes, with no cost or wall-clock figure. Deployment viability depends on both.
- **Does the lead survive a second seed and another simulator?** The authors say these are untested.
