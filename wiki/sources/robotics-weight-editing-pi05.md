---
title: "We Asked Opus-5.5 to Edit π0.5's Weights. AutoResearch Made It Happen."
type: source
url: https://cuzyoung.github.io/robotics-weight-editing/en/
local_path: raw/2026-11-robotics-weight-editing-pi05.md
sha256: e2d63cf021ec219ec3343e186ce0ebe76c373c409e2a5e9713530d42a8e0957d
author: Ziyang Gong, Kaifeng Zheng, Yingrui Huang, Wendi Chen, Jiaguo Tian, Junkai Yang, Minghuan Liu, Zhenjie Yang (Shanghai Innovation Institute; SJTU; HKU)
published: 2026-11 (undated on the page; it cites the 2026-11-02 weight-space-programming post and is linked from that post's 2026-11-12 addendum)
ingested: 2026-11-14
format: blog post (not peer-reviewed); appends the full original research prompt given to the model
tags: [weight-space-programming, pi-zero-5, real-time-chunking, training-time-rtc, rope, yam, claude-opus-5-5, autoresearch, flow-matching, action-chunking, closed-form-editing]
---

## Summary

This is the first application in the wiki of [weight-space programming](../concepts/learning/weight-space-programming.md) to a **deployed VLA**. The authors gave Claude Opus 5.5, running in Claude Code, the following: a π0.5 **Training-Time RTC** checkpoint, its source code, recorded YAM demonstrations and rollouts, and one RTX 4090. The goal was to make the robot finish tasks faster by editing weights only. Backpropagation, optimisers and LoRA were forbidden. The production inference code had to stay unchanged, and the deliverable had to be a checkpoint that could be rolled back. In about 111 minutes of offline work, using recordings only, the model produced **two closed-form weight edits**:

1. **Prefix repair.** It found that the sampler lets the final flow-matching step perturb the conditioned RTC prefix, and returns it without restoring it. It then cancelled that update with a rank-one edit to one time-modulation matrix.
2. **Tempo acceleration.** It hypothesised that spreading RoPE action positions (P + i → P + 1.25i) would make the policy advance further per step. It confirmed the effect offline, then fitted it into the Q/K projections of layers 1–17 by ridge regression.

On real bimanual YAM arms, bottle placement got **4.3%, 7.4% and 12.0% faster at 30, 35 and 40 Hz**, with 100% success for both policies. Mean chunk jump fell **89.8%** (30.88 → 3.14 mm). Coin-insertion transport sped up by 20.7%, and block stacking showed **no speedup**. Every condition has **three trials**. The authors' own conclusion is that the result came less from "a moment of magic" in weight space than from the model's **research loop**: diagnose, hypothesise, test, and revise after failure.

## Key claims

**Setup (§1)**
- The policy is a π0.5 TT-RTC checkpoint. Chunks are 50 steps of 12 joint targets plus 2 gripper targets. It executes 32 steps per cycle at 30 Hz, and the first **6** steps of the old plan are the conditioning prefix.
- The model had access to 136 historical rollouts and 154 human demonstrations. Edits were fitted on 12 demonstrations and 12 rollouts covering 6 task types.
- **Allowed:** forward passes and closed-form fitting. **Forbidden:** gradients, LoRA, changes to runtime code, and robot execution without confirmation. The prompt also requires comparison against action-amplitude scaling, trajectory time scaling and random edits. It forbids "disguising runtime optimisation as weight editing" and presenting simple action scaling as a research method.

**Diagnosis (§2.1)**
- Inference takes about 105–109 ms against a plan-update period of about 1.073 s. Inference waiting is therefore *not* the bottleneck, and the time has to come from action execution. This is the first thing the model checked.

**Prefix repair (§2.2, §3.2)**
- In each denoising iteration the conditioned prefix is restored at the start, but the final iteration's update is returned without another restore. Deployment discards only the first **4** steps, the real latency, so steps 5–6 of the prefix, already drifted, reach the robot as a chunk jump.
- **The edit:** `final_norm_1.Dense_0.kernel` (1024 × 3072) receives ΔW = u dᵀ. At the prefix time condition t = 0 this sets scale to −1 and shift to s\*, where s\*W_out + b_out = 0, so the sampling update is zero. At the ten sampling times it leaves the update unchanged; this is solved by min-norm least squares, with c₀u = 1 and c_t u = 0. The result is a **rank-one** update.
- **Offline result.** Prefix joint error fell from 0.095 to 4.5 × 10⁻⁴ rad. Median transition distance fell from 19.16 mm to **1.80 mm**. The equivalent one-line code fix (restore the prefix after the loop) reached **1.88 mm**, so the two are roughly equivalent.

**Tempo acceleration (§2.3–2.6)**
- **RoPE scale sweep (offline, median of 58 observations).**

  | s | Path progress | Deviation |
  |---|---|---|
  | 0.8 | 0.851 | 0.79 mm |
  | 1.25 | **1.131** | 1.23 mm |
  | 1.5 | 1.175 | 1.94 mm |
  | 2.0 | 1.009 | 4.67 mm |

  The effect is non-monotonic. Compressing only the prefix in time did almost nothing (≈1.004).
- **First attempt failed.** Fitting only the 1024 × 14 action output head to the teacher's actions reconstructed well in-sample (0.005 rad). On held-out data the error was 0.024 rad, deviation 8.3 mm and the jerk ratio 3.2, so the model abandoned this approach.
- **Second attempt.** It constructed Q/K targets by applying the extra rotation R(0.25i) to the original projections. It ridge-fitted W toward W₀ in layers 1–17, keeping layer 0 fixed, over 3 rounds. On held-out time points from the *same trajectories* it reached progress 1.20, deviation 1.08 mm and a jerk ratio of 1.37.
- **Combined edit against baselines (offline, 35 to 36 observations).**

  | Method | Progress | Within-chunk jerk ratio | Chunk jump |
  |---|---|---|---|
  | Combined edit | 1.214 | 1.363 | 5.4 mm |
  | Trajectory time scaling | **1.257** | **0.827** | 44.2 mm |
  | Random weight edit | — | 31.07 (deviation 24.05 mm) | — |

  Time scaling beats the edit on progress and jerk; it just doesn't fix the chunk jumps. **The authors did not test prefix repair combined with time scaling.** They note this "does not establish that editing outperforms every post-processing alternative."
- **Deliverable.** A checkpoint with **1.16% of parameters modified**. The run took 1 h 50 min, 193 tool calls, about 185k output tokens and about 36.8M cache-read tokens.

**Real robot (§3.1)**
- **Bottle placement, mean time in seconds (3 successful trials each).**

  | Rate | Original | Edited | Change |
  |---|---|---|---|
  | 30 Hz | 22.42 ± 0.26 | 21.46 ± 0.88 | −4.3% |
  | 35 Hz | 19.43 ± 0.12 | 17.99 ± 0.77 | −7.4% |
  | 40 Hz | 17.99 ± 0.55 | 15.83 ± 0.66 | −12.0% |

  The headline "−29.4%" compares the edited policy at 40 Hz with the original at 30 Hz, so most of it comes from the faster execution clock.
- **Command quality at 30 Hz.** Chunk jump fell from 26.2 to 1.4 mm, command jerk P95 fell 77%, and end-effector tracking error was unchanged (19.6 vs 19.2 mm). At higher rates the edited policy's residual jumps grow: 1.4, 3.1 and 4.9 mm at 30, 35 and 40 Hz.
- **Coin insertion.** The post-grasp-to-handover stage went from 5.85 to 4.64 s (−20.7%). The approach stage was unchanged.
- **Block stacking.** 19.46 against 19.28 s, about −1%, with overlapping trial times. The original policy's mean excludes one retried run.

**Mechanism (§3.3)**
- The edited model's attention to context is closer to the RoPE teacher's than to the original's (JSD 0.0017 vs 0.0079). When only the **action-to-action** attention scores are edited, most of the progress gain survives (1.087 at step 37). When only the action-to-context scores are edited, the gain falls to 1.039. On this evidence the speedup lives mainly in how actions attend to other actions.

## Verification against the primary code

> [!note] Checked against Physical-Intelligence/real-time-chunking-kinetix @ `9296f31d62d5` (2025-12-08, the commit the post cites)
> The mechanism is **real**, and the post understates one point.
> - **Sampler.** In `src/model.py`, `realtime_action`'s `simulated_delay` branch (the training-time RTC path) overwrites the first `inference_delay` positions with the previous chunk *at the start of each step*. It then applies `x_t + dt * v_t` to the whole chunk, and after the last step returns `x_1` with no restore.
> - **Why the drift is arbitrary.** In `loss()`, those prefix positions are **excluded from the loss**: `loss_mask = logical_not(mask)`. So the velocity the network predicts there is never trained, and the final update to the prefix is unconstrained rather than near zero. The post does not mention this. It explains why a 6-step prefix can drift by 0.095 rad.
> - **Why the official eval is safe.** `src/eval_flow.py` executes `action_chunk[:, :inference_delay]` from the **previous** chunk, so the drifted prefix is never sent to the environment. The post's "discards the whole prefix, so this issue is not exposed" is accurate.
>
> So "bug" means a **latent hazard in porting the code**, not a defect in PI's experiment. It bites any deployment that conditions on more steps than it actually waits out. The authors' conservative 6-step prefix with about 4 steps of real latency is exactly that case, and the authors say IK-solver jitter (median 23 ms, max 921 ms in their OpenWAM stack) makes such margins normal. The code excerpt quoted in the post (`sampling_input`, `omega`) **does not appear in this repo**. It presumably comes from the authors' own π0.5 TT-RTC port, which this wiki has not seen.

## Assessment

- **The bug finding is the durable contribution.** It is verifiable, it has a one-line code fix, and it applies to anyone porting TT-RTC. The weight-space version of the fix is a demonstration, since a deployment would use the code fix. The interesting part is that the model *found* the bug unprompted, from logs and source code.
- **The speedup is small, thinly sampled, and partly matched by trivial baselines.** Three trials per condition, one layout per task, and no gain on stacking. Offline, plain trajectory time scaling advances further with *less* jerk. The edit wins only by also carrying the prefix repair, and the obvious control (time scaling plus the code fix) was not run.
- **"Held-out" is weak.** Tempo-edit validation used different time points from the *same* trajectories.
- **Compared with the MIT post, this is the more honest kind of result.** It reports a failed first attempt, makes negative and confounded comparisons explicit, publishes the prompt, and argues that the research loop matters more than weight-reading ability. That last point is a real refinement of the WSP claim: here the model used forward passes heavily, and the edits are classical closed-form solves.

## Entities mentioned
- [π0.5](../entities/pi-zero-5.md) is the edited policy, a Training-Time RTC checkpoint.
- [Physical Intelligence](../entities/physical-intelligence.md) wrote the π0.5 paper, the TT-RTC paper (Black, Ren, Equi, Levine; arXiv 2512.05964) and the `real-time-chunking-kinetix` reference code.
- [YAM](../entities/yam.md) is the real-robot platform (bimanual).
- [Anthropic](../entities/anthropic.md) makes Claude Opus 5.5, which did the editing through Claude Code.
- OpenWAM (arXiv 2609.07398) is the authors' IK and deployment stack; it has no wiki page.

## Concepts touched
- [Weight-space programming](../concepts/learning/weight-space-programming.md): its first deployed-robot instance.
- [Flow matching](../concepts/learning/flow-matching.md): the per-step velocity update and prefix conditioning are where the bug lives.
- [Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md): RoPE-position reasoning and attention-region ablation on a VLA action expert.
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md): an LLM editing a policy's parameters, with the policy still in charge of control.
- [Code as policy](../concepts/agents/code-as-policy.md): the agent's deliverable is a checkpoint rather than a script.

## Open questions
- Does time scaling plus the one-line prefix fix match or beat the combined edit? This is the missing control. If it does, the tempo edit buys nothing over post-processing.
- Do other TT-RTC ports, including openpi and LeRobot's `rtc` policy, carry the same unrestored final step when the prefix is longer than the delay? LeRobot's `rtc` appears to be the inference-time guidance variant, which never hard-restores the prefix. Its behaviour needs checking separately.
- Does a RoPE-spacing effect on tempo hold for other chunked policies? Is it a property of π0.5's action expert, or of RoPE action positions generally?
- Robustness: how does it do with more trials, other layouts, and out-of-distribution states? The prompt asked for generalisation across tasks and initial states, and the results only partly address that.
