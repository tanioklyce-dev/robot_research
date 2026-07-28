---
title: How Claude Performs on Robotics Tasks
type: source
url: https://www.anthropic.com/research/claude-plays-robotics
author: Shmuel Berman, Michael Ilie, Jia Deng, C. Daniel Freeman
affiliations: Anthropic Frontier Red Team
published: 2026-07-09
ingested: 2026-07-27
venue: anthropic.com — Frontier Red Team
format: web article (evaluation report)
code: https://github.com/safety-research/embody (stated as "once released")
tags: [anthropic, claude, frontier-red-team, evaluation, benchmark, quadruped, humanoid, manipulation, libero, mujoco, vla, unitree-go2, unitree-g1, franka-panda, molmoact, ai-safety]
---

## Summary

The **autonomy-side counterpart** to [Project Fetch](anthropic-project-fetch-robot-dog.md): where Fetch measured how much Claude helps *humans* do robotics, this measures what frontier models can do **driving robots themselves**, with no robotics-specific training. Anthropic's Frontier Red Team built an evaluation harness (**`embody`**) spanning classic control, quadruped and humanoid locomotion, and tabletop manipulation, crossed against **four levels of control abstraction** — from emitting raw joint torques to supervising a pretrained VLA. Eleven models were run, including six Claude generations.

The headline is a **capability profile, not a score**: models are improving fast at the *high* abstraction levels and remain close to useless at the *low* ones. No model ever stood a humanoid up from a collapsed pose. End-to-end LIBERO pick-and-place tops out around **5.5%**. But the same models can supervise a pretrained VLA competently enough to **beat that VLA alone on tasks it cannot do**, and can navigate a maze by writing their own tools.

The paper's most transferable claim is a safety one: **a model's real-world influence changes by orders of magnitude depending on the interface and information it is given**, so *access level must be treated as part of the system under evaluation*, not as deployment detail.

> [!note] Model names postdate this wiki's usual sources
> The evaluation covers **Claude Opus 4, 4.1, 4.5, 4.6, 4.7** and **Claude Mythos Preview**, compared against **GPT-5.1, GPT-5.4, Gemini 2.5 Pro, Gemini 3.1 Pro Preview, Kimi K2.6, Qwen 3.6+**. These are recorded as the source states them; the wiki has no independent page for any of these models.

## The evaluation harness

### Platforms

| Domain | Platform |
|---|---|
| Classic control | Inverted pendulum, hopper, and **TwinFlipper** — a custom task (flippers maximizing a ball's airtime) built specifically to be absent from pretraining corpora |
| Quadruped locomotion | **[Unitree Go2](../entities/unitree-go2.md)**, 12-DoF — simulated *and real hardware* |
| Humanoid locomotion | **[Unitree G1](../entities/unitree-g1.md)**, 29-DoF — simulated only |
| Manipulation | **[Franka Panda](../entities/franka-panda.md)** 7-DoF in kitchen scenes adapted from **[LIBERO](../entities/libero.md)** |

Physics throughout is **[MuJoCo](../entities/mujoco.md)**.

### The four control-abstraction levels

The organizing axis of the whole report — see [control abstraction levels](../concepts/robotics/control-abstraction-levels.md):

1. **Direct control** — the model picks low-level motor torques/forces every timestep.
2. **Programmatic control** — the model writes a Python controller mapping observations to actions.
3. **Policy control** — the model issues high-level commands to a **pretrained** policy.
4. **RL supervision** — the model trains an RL policy from scratch (PPO scaffold; `n_steps=256`, `batch_size=64`, `gamma=0.99`, `lr=3e-4`, policy network capped at 200k params; 1.5–4 h timeouts on a SLURM cluster).

### Trial counts and harness caveats

- **35 trials** for standard cells (classic control, locomotion, RL); **50** where tighter estimates were needed for model comparison; **200** for LIBERO-40 (40 tasks × 5 seeds); **100** for the high-level locomotion suite.
- **The simulator was paused between LLM calls** for direct and programmatic control, removing the real-time constraint. Manipulation was *not* paused (arm stability is less time-critical than legged balance). This is a deliberate and clearly-stated concession — see the latency gap below.
- Vision input: JPEG RGB frames in provider-native formats; up to three frames per turn (published cells used one); prior frames retained in context.

## Key claims

### The latency gap is two orders of magnitude

The single hardest number in the report:

> Real-time control would require roughly **83 Hz**; current non-reasoning inference runs at **~0.2–0.4 Hz**.

Measured end-to-end latencies: **2–8 s** text-only, **5–15 s** with one or two images, **15–180 s** with reasoning. Closing this needs **~100×** improvement. Everything the report shows about low-level control is therefore obtained with the physics clock stopped — the capability is real, the real-time deployment is not.

### Low-level control: still broadly failing

- **G1 humanoid** — *"No model successfully stood the robot up from a collapsed pose even once."* There is measurable progress between Opus 4 and 4.7 at **balancing a robot that is already standing**, but the hardest platform in the study stayed out of reach. Programmatic control was substantially better than direct.
- **Go2 quadruped** — best results balance for roughly **2 seconds**. Walking forward saw limited success; models struggle with open-loop plans needing sustained spatial memory. **Robustness collapses under randomization**: with the start pose randomized (e.g. on its back), Opus 4.6 could not stand up even once.
- **Manipulation (direct control)** — end-to-end LIBERO pick-and-place success ranges **from 0 to 5.5%** across models (Mythos Preview highest at 5.5%; Opus 4 at 0). Decomposed by subgoal, the newer models are **much more likely to reach and touch and grasp** the target; **placing** remains the bottleneck. Errors compound across reach → grasp → transport → place.
- **Code control beats direct control** for essentially every model on classic control. On the novel **TwinFlipper** task, all models do poorly at direct control while Opus 4.5/4.6 improve significantly over Opus 4/4.1 at code control.

### High-level control: where the gains actually are

**Navigation suite** — eleven navigation and spatial-reasoning tasks, composite score on a **0–100** scale. Mythos Preview leads at **~54** (adaptive-max reasoning); Opus 4.7 sits around **40**; intermediate Claude generations span roughly **30–40**, with task-specific reversals between 4.5–4.7 rather than a clean ladder.

Named tasks and their diagnostic value:
- `find_x` (locate a distant table), `visual_search` (arena maze), `return_home` (**path integration from memory** — Opus 4.7 gains ~+11 over 4.6), `drift_detection` (**notice that your own commands are being corrupted** — weak across all models; tests closed-loop self-monitoring), `explore_report` (build a spatial mental model), `oneshot_course` (**pre-plan from a map**).
- **`oneshot_course` hard variant: zero success for every model, even with 20 practice runs.** The report's reading is that models learn *specific sequences*, not general plans.

**Perceptual aids** — the cleanest lever in the whole study:
- **A compass** (heading in degrees) gave the **most consistent gains across models**.
- **Depth heatmaps and crosshair overlays were roughly neutral** — and in a real-world corridor run a model **disregarded the depth information entirely**, turning toward obstacles.
- **Third-person camera** helped self-localization tasks; **+10.7** for Mythos Preview.
- **Text descriptions vs raw RGB** is a generational tell: *older* models did **better** with VLM-generated text descriptions than with pixels; **Opus 4.6+ do slightly worse with text**, implying they now extract spatial detail from images that a text summary throws away.

### Supervising a VLA: the report's most interesting result

Models were given **[MolmoAct](../entities/molmoact.md)** as a pretrained manipulation policy on LIBERO-40 and allowed to override its 7-DoF actions.

- **On the VLA's own tasks, supervision *hurts*.** Every tested model performs substantially worse than MolmoAct running alone — but the best supervisors (Opus 4.5/4.6) close most of the gap.
- **On novel tasks the VLA cannot do alone, the sign flips.** Opus 4.5, 4.6 and Gemini 3.1 beat MolmoAct-alone; **Mythos Preview solves the largest share** of novel tasks.
- **The mechanism is deference calibration.** Claude models copy the VLA's exact action far more often than GPT-5.4 or Gemini 3.1. Opus 4.5/4.6 have the highest follow rates and the best in-distribution results; **Mythos Preview overrides more often** — which costs it on tasks MolmoAct already handles and wins it the novel ones. Opus 4/4.1 **defer indiscriminately**, failing to distinguish competent from incompetent VLA actions.

That is a clean statement of the supervision problem: **knowing when *not* to intervene is the skill**, and it trades off directly against novel-task capability.

### Reasoning budget does not unlock robotics

> "Additional reasoning alone, in current generation models, is unlikely to overcome the deficiencies that currently prevent models from performing general low-level robotics."

- Classic control: newer Claude models **regressed** with high reasoning budget (the report speculates overengineering of simple tasks).
- Manipulation: no major difference for Claude; **hurt** Gemini 3.1 and GPT-5.4.
- Locomotion: minimal effect for Claude (~2.6–4 point spread), significant for GPT-5.4. **Mythos Preview is the sole exception** — a 14-point spread (**40.2** adaptive-low → **54.1** adaptive-max), the only case where reasoning bought gains comparable to the perceptual aids.
- Cross-generation improvement is attributed instead to **better vision, numerical consistency, and 3D understanding**.

### Models operate on the recent past

Truncating context to discard distant history produced **minimal performance drop**. Models "reframe and adjust," but mainly off the last few steps — they do not build a running strategy across an episode. This is offered as the explanation for the sustained-spatial-memory failures (`return_home`, `oneshot_course`, corridor overshooting).

### Real-world runs

Small-N by necessity ("the serial nature of work in the real world"), on a real Go2, and broadly consistent with simulation. Two failures are worth recording because neither is a control problem:
- A model saw a **table reflected in a glass door** and charged the glass door instead of the table. An operator intervened.
- In a busy corridor with plants and a water cooler, a model **ignored the depth heatmap** and turned toward obstacles rather than open space.
- **No model ever completed the real office loop**, with failures traced to vision and memory rather than actuation.

## The safety argument

1. **"A VLM's real-world influence can change by orders of magnitude depending on the information it has access to."**
2. Therefore **"evaluations and deployments need to treat access level as a core part of the system, because small changes in tools or control can produce large changes in capability."**
3. Today's frontier models **cannot control humanoid robots without a pretrained policy** — but a general-purpose chat model with no robotics training can, on a good run, **write and download its own tools** to walk a quadruped through a maze or pick a plate off a counter.
4. Deployment direction: **better ways to grant physical access with clear limits** — a system able to affect certain objects while blocked from others. The pretrained-policy layer functions as a de-facto safety boundary, since models cannot reliably drive joints but *can* supervise controllers.
5. Legged locomotion is called out as carrying both a "higher ceiling of contribution and greater risk profile," where misaligned behavior "could enable serious physical harm."

## Limitations (as stated)

- **The paused simulator.** Real-time control is not demonstrated; the 83 Hz vs 0.2–0.4 Hz gap is unclosed.
- **Small real-world N** — could not run high-trial-count physical experiments.
- **Pretraining contamination** — classic RL tasks likely appear in training corpora; TwinFlipper exists specifically as the uncontaminated control.
- **Simplified environments** — more complex tasks and starting conditions "were generally beyond the reach of even frontier models."
- **The G1 result is weak but improving**; no successful standing policy.
- **MolmoAct is the ceiling** in the supervision experiments — the result is about supervision quality relative to one VLA, not about manipulation in general.
- **Reasoning effects are unexplained** — why extra reasoning helps some models and not others is open.

## Open questions

- **Why does supervision hurt in-distribution?** The report establishes that it does and that better models hurt less, but not what the overrides get wrong. This is the crux for any [LLM-agent robot](../concepts/agents/llm-agent-architecture.md) architecture, which is *structurally* the same setup: a language model sitting above a lower-level controller.
- **Does the `embody` harness ship?** The code URL is given as "once released." Not verified as live at ingest.
- **How does this interact with on-robot latency work?** The 83 Hz figure is for a *language model in the loop*; the wiki's edge-inference thread ([Jetson module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md), [XLeRobot onboard compute](../syntheses/platforms/jetson-onboard-compute-xlerobot.md)) measures VLAs at 1.4–27.8 Hz on Jetson hardware. Those are different systems at different abstraction levels, and nobody has put them on one axis.
- **Mythos Preview's profile is anomalous** — the only model where reasoning budget matters, the best novel-task supervisor, and the worst in-distribution supervisor. Whether that is one underlying trait (a stronger prior toward acting on its own judgment) is not analyzed.
- **No people pages filed** for the authors (Shmuel Berman, Michael Ilie, Jia Deng, C. Daniel Freeman) — see backlog.

## Entities mentioned

- [Anthropic Frontier Red Team](../entities/frontier-red-team.md) — authors.
- [Anthropic](../entities/anthropic.md).
- [Unitree Go2](../entities/unitree-go2.md) — real + simulated quadruped; **primary confirmation** that this is the Project Fetch robot.
- [Unitree G1](../entities/unitree-g1.md) — simulated humanoid; hardest platform in the study.
- [Franka Panda](../entities/franka-panda.md) — manipulation platform.
- [MolmoAct](../entities/molmoact.md) — the supervised VLA.
- [LIBERO](../entities/libero.md) — manipulation benchmark (LIBERO-40 used).
- [MuJoCo](../entities/mujoco.md) — physics throughout.

## Concepts touched

- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — the report's organizing axis, and its safety conclusion.
- [AI uplift studies](../concepts/safety/ai-uplift.md) — the complementary measurement; this is the autonomy half.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — policy-control and VLA-supervision *are* this pattern, measured.
- [VLA models](../concepts/learning/vla-models.md) — MolmoAct as the supervised policy layer.
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) — access level as a system property.
