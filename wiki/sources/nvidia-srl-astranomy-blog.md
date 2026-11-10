---
title: "Astranomy: An Empirical Study of GPT-6 Astra as a Native Robot Policy"
type: source
url: https://research.nvidia.com/labs/srl/projects/astranomy/
author: "Jenai Xuning Yang, Ashna Khetan, Shun Zhang (NVIDIA Seattle Robotics Lab)"
published: 2026-10
format: "research blog post with interactive figures and appendix tables; arXiv version announced as coming soon"
tags: [gpt-6-astra, llm-as-policy, robolab, nvidia-srl, codex, agentic-policy, cosmos-3, world-action-model, end-effector-control, action-representation, prompting, latency, token-cost, simulation, droid]
ingested: 2026-11-10
---

# Astranomy: An Empirical Study of GPT-6 Astra as a Native Robot Policy

## Summary

The [NVIDIA Seattle Robotics Lab](../entities/nvidia-seattle-robotics-lab.md) runs [GPT-6 Astra](../entities/gpt-6-astra.md) as a robot policy on [RoboLab-120](../entities/nvidia-robolab.md), a simulated pick-and-place benchmark on the DROID Franka setup. It is tested in three roles, all zero-shot with no robot fine-tuning:

| Role | How it works | RoboLab-120 success / score |
|---|---|---|
| **Direct** | API calls returning absolute end-effector action chunks, with no memory between calls | 66.3% / 76.7 |
| **Agentic** | A persistent Codex session with full history, giving one end-effector target at a time | **74.8% / 83.6** |
| **Orchestrated** | Astra reviews proposals from Cosmos3-Nano-Policy, a world-action model, and can edit or override them | 66.5% / 79.1 |

For comparison, the best leaderboard entry, Lakeside, scores 51.0%. Cosmos3-Nano-Policy alone scores 36.8% and π0.5 28.0%.

**The capability is real in this setting and not yet usable in practice.** A Direct call takes 18.56 s on average, and inference is about 97% of each episode's time. The simulator pauses while the model thinks, so the benchmark doesn't penalise this. An Agentic success costs about 30.9 million tokens, roughly $36.40.

The authors state that they haven't established statistical significance for the differences between configurations.

## Key claims

### Setup (Sec. 2)

- **Protocol.** RoboLab's DROID robot at 15 Hz, three camera views at 384×216, medium reasoning effort. There is no time or retry limit, and each completion is capped at 8,192 tokens.
- **Sample size.** Five episodes per task with fixed seeds. The full 120-task benchmark was run only for the final configurations, and ablations used a 30-task subset of 150 episodes per condition.
- **Final configurations (Table 2).** Absolute end-effector poses, gripper and camera geometry in the prompt, and three recent observations for Direct. Agentic keeps full history, a planning instruction and motion feedback, with tools disabled.

### What the ablations show (Sec. 3, 30-task subset)

| Factor | Direct | Agentic |
|---|---|---|
| End-effector vs joint positions vs joint B-spline | 72.7 / 48.7 / 37.3% | 86.0 / 84.0% (B-spline not run) |
| Base prompt → plus gripper and camera geometry | 19.3 → 72.7% | 83.3 → 86.0% |
| Current frame only → three recent frames | 49.3 → 72.7% | — |
| Default → vague instruction ("Put it away") | 72.7 → 64.0% | 86.0 → 85.3% |
| Tools off → on | — | 86.0 → 88.0% |
| Motion-error feedback on → off | — | 85.9 → 85.2% |
| Planning instruction → none → discouraged | — | 86.0 / 90.0 / 81.0% |

- **The prompt is part of the policy.** In Direct mode, geometry in the prompt nearly quadruples success, and a minimal prompt produced no reasonable action. The agentic loop makes Astra much less sensitive to geometry, action type and wording, because it can correct over many small steps.
- **History matters most for the agent.** On a 23-task subset, full text and image history reached 100%, text history with current images 87.0%, and image history alone 56.5%.
- **Action horizon.** With a 16–32-action range, Astra made 62% fewer calls with similar completion time, but success fell 6 points.
- **Video demonstrations.** On 28 tasks, demonstration frames gave 87.9% against 90.0% for language alone, so in-context learning works but doesn't help.
- **Tools change the reasoning more than the outcome.** Every tool-enabled episode ran Python, at an average of 19.7 tool calls, and the model often reached the same conclusion it reached without tools.
- **Model comparison (Direct only).** GPT-6 Astra 72.7%, GPT-6 Sol 33.3%, GPT-6 Luna 2.0% and Claude Opus 5.5 25.3%. Raising Astra's reasoning effort to xhigh gave 74.5%, at 2.6× the latency and 2.2× the cost.
- **Orchestration (Sec. 3.3).** Astra intervened on 14.5% of steps, mostly for grasp failures (64.4%) and wrong targets or plans (20.2%). Orchestrated matches Direct, so in this study the world-action model adds nothing over Astra acting alone.

### Runtime (Sec. 4)

- **Latency.** 18.56 s per Direct call, 13.37 s per Agentic decision, and 11.50 s for Astra plus 2.74 s for the world-action model when orchestrated. One shown yogurt episode took 3 min 57 s, of which 5.2 s was robot motion. π0.5 is quoted at a median 47 ms per chunk, from Black Forest Labs' FLUX 3 Action report.
- **Cost.** Per successful episode: Direct about 160,000 tokens ($1.96), Orchestrated 11.0 million ($17.72), Agentic 30.9 million ($36.40), at prices of 2026-10-01. Output and reasoning tokens dominate.

### Failure modes (Sec. 6)

Grasps that never close on the object, objects knocked aside instead of placed, wrong receptacles, lost objects during transport, and recovery attempts that repeat the same failing motion. The agentic loop improves reliability overall without consistently fixing grasp errors.

### Limitations

**Stated by the authors.** Five episodes per task can't establish significance. Their one paired test, original against expanded agentic interface at 80.0% and 86.0%, gives McNemar p = 0.108. The study covers pick-and-place only, with no insertion, assembly or dynamic tasks, and runs only in simulation with pauses during inference. Serving infrastructure behind the API is invisible to them.

**Noted at ingest.**

- **Final configurations aren't always the best ablation arm.** Dropping the planning instruction scored 90.0% against the default's 86.0%, and enabling tools 88.0%, yet both defaults were kept. The gaps are within noise at 150 episodes.
- **The 100% history result is on a 23-task subset,** chosen because uncached runs were costly. It isn't comparable to the 86.0% on 30 tasks.
- **Cost is averaged over successful episodes only.** The takeaways section says "per episode." Failed episodes, which may run to the step limit, aren't counted.
- **The model comparison favours the model tuned for.** All defaults were chosen from Astra ablations, and Sol, Luna and Claude Opus 5.5 were run once, in that Direct configuration. The ranking is clear, but the gap may partly reflect the prompt.
- **The benchmark's own authors ran it.** Yang is RoboLab's first author, so harness knowledge is high and there is no independent replication.
- **No public code.** The code link points to an internal NVIDIA GitLab.

## Against the earlier Astra results

The [RoboDojo study](gpt-6-astra-robodojo-paper.md) found Astra at 22.48% on 42 bimanual tasks, ahead of all fine-tuned policies, and found that one-shot demonstrations lowered success. Here, with a single arm and pick-and-place, Astra reaches 66–75%, and demonstration frames are roughly neutral.

The two results agree on direction. Astra is above the fine-tuned policies on both boards, and weakest where precise grasping and contact matter. They also differ in interface: RoboDojo gave single targets turned into motion by inverse kinematics, while this study adds action chunks, geometry prompts and a Codex loop. **Neither tests a real robot at speed.** The RoboDojo real-robot run was stopped for safety.

## Entities mentioned

- [GPT-6 Astra](../entities/gpt-6-astra.md), [RoboLab](../entities/nvidia-robolab.md), [NVIDIA Seattle Robotics Lab](../entities/nvidia-seattle-robotics-lab.md), [NVIDIA Cosmos](../entities/nvidia-cosmos.md), [DROID](../entities/droid.md), [π0.5](../entities/pi-zero-5.md), [FLUX 3](../entities/flux-3.md)

## Concepts touched

- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — a frontier model choosing end-effector targets directly, and how the interface changes its success.
- [Code as policy](../concepts/agents/code-as-policy.md) — the agentic variant runs in Codex, though its best configuration disables code tools.

## Open questions

- **How much speed would make it usable?** Inference is about 97% of each episode, so the bottleneck is serving, not motion.
- **Do the rankings survive more episodes?** Most ablation gaps are 2–6 points on 150 episodes.
- **Would other models close the gap with their own tuned prompts?**
- **Real robot.** Everything here pauses the world during inference.
