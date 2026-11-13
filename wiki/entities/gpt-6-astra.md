---
title: GPT-6 Astra
type: entity
subtype: model
created: 2026-11-07
updated: 2026-11-12
sources: 9
tags: [gpt-6-astra, openai, frontier-model, llm-as-policy, robodojo, code-as-policy, embodied-reasoning, robot-safety, closed-weights]
---

# GPT-6 Astra

**GPT-6 Astra** is [OpenAI](openai.md)'s frontier model, released in September 2026 (the paper cites OpenAI's *"GPT-6 Astra: A New Generation of Intelligence"*, which this wiki can't fetch because openai.com returns 403). In this wiki it matters as the **first language model to top a broad public manipulation leaderboard with no robot policy in the loop**: 22.48% average success on [RoboDojo](robodojo.md) sim, above all 40 public fine-tuned policies ([GPT-6 Astra on RoboDojo](../sources/gpt-6-astra-robodojo-paper.md)).

> [!note] Naming across sources
> The sources say "GPT-6 Astra", "GPT-6 Astra Pro" ([RPG](../sources/rpg-guided-self-improvement-paper.md)), "GPT-6-Astra" (Unitree's API tests), "GPT-Astra" ([Jalapeño](../sources/openai-jalapeno-first-results.md)) and "ChatGPT Astra" (NVIDIA GTC Berlin; [MicroDuck](../sources/nvidia-microduck-ai-agents-sim-blog.md)). This page treats them as one model family. The wiki has no OpenAI primary to say how the variants differ.

## As a direct robot policy (RoboDojo, 2026-09)
- **Setup.** Each turn the model calls `move_eef` with world-frame grasp-point targets for either or both arms. Non-learned IK and path planning turn those targets into joint commands. It gets RGB only, with no primitives, and is frozen and zero-shot.
- **Score.** **22.48% SR / 28.97 Score** over 2,100 trials, against **DM0.5 at 19.34%** and π0.5 at 6.91%. GPT-5.5 scores **0.88%** and DeepSeek-Flash **1.92%** on the same interface ([paper](../sources/gpt-6-astra-robodojo-paper.md)).
- **Strengths and weaknesses.** It is very strong on semantic and open tasks: push_T 60%, arrange_largest_number 60%, Open axis 31% against ≤ 2% for the policies. It is weak on Precision (4%), dynamic, contact-rich and coordinated bimanual work, and scores 0% on make_kong, where the best policy gets 90%.
- **Context use.** A one-shot demonstration *lowers* success (22.9% → 17.9% with images, 12.9% with text). Under perturbations, though, it corrects itself within an episode.
- **Real hardware.** The trial was **stopped for safety** after repeated unsafe actions that damaged equipment. On the 33 retained trials it scored 3.03% SR.
- **Caveats** (all stated by the authors):
  - one seed;
  - its task recipe included the score ladder, which the policies never saw;
  - contamination is unquantified;
  - only one simulator was used.

## As a direct robot policy (RoboLab, 2026-10)
- **Setup.** NVIDIA's Seattle Robotics Lab ran it zero-shot on [RoboLab-120](nvidia-robolab.md), 120 single-arm pick-and-place tasks on the DROID setup in simulation, with five episodes per task ([Astranomy](../sources/nvidia-srl-astranomy-blog.md)).
- **Score.** **66.3%** as a direct API policy, **74.8%** in a persistent Codex session and 66.5% supervising Cosmos3-Nano-Policy. The best leaderboard policy scores 51.0%, Cosmos3-Nano-Policy 36.8% and π0.5 28.0%.
- **The interface matters.** Absolute end-effector targets beat joint positions (72.7% vs 48.7%), and gripper and camera geometry in the prompt raise direct success from 19.3% to 72.7%. In the same direct setup, GPT-6 Sol scored 33.3%, GPT-6 Luna 2.0% and Claude Opus 5.5 25.3%, with defaults chosen from Astra's ablations.
- **Cost.** An average of 18.56 s per direct call, about 97% of episode time with the simulator paused, and about $36 in tokens per successful agentic episode.

## As a controller writer
- **RoboPianist.** Through the Codex scaffold, Astra writes a 20 Hz `play.py` for two Shadow hands and refines it by simulated practice. It reaches **F1 0.902 on two-hand Twinkle, against 0.886 for the RL reference**, but transfers unevenly to unseen pieces (C-major scale 0.903, D-major scale 0.556) ([paper](../sources/gpt-6-astra-robodojo-paper.md), App. G). This is level 2 of the [control-abstraction ladder](../concepts/robotics/control-abstraction-levels.md).
- **Code-as-policy baseline.** In [RPG](../sources/rpg-guided-self-improvement-paper.md)'s reproduction of CaP-Agent0, GPT-6 Astra Pro is the strongest base model (60.0%). The persistent-library system on Gemini Flash still reaches 95.0%.

## Elsewhere in the wiki
- **Embodied reasoning.** In Unitree's API tests it leads ERQA (77.7) and RefSpatial (79.6), and loses on pointing benchmarks to specialized open models ([UnifoLM-WLA-1](../sources/unifolm-wla-1-project-page.md)).
- **Agentic simulation.** It is linked as the system that *"created its own physics simulator"* in [Ai2's ToyBlocks](../sources/ai2-toyblocks-blog.md), where it *"struggles to simulate contact,"* and as the asset and scene agent in NVIDIA's [MicroDuck](../sources/nvidia-microduck-ai-agents-sim-blog.md) pipeline.
- **Infrastructure.** Used with Codex to write [Jalapeño](openai-jalapeno.md)'s kernels ([first results](../sources/openai-jalapeno-first-results.md)).
- **Against a fast policy.** On three YAM tasks at the same station, Astra took **15.6× longer** (4:13 vs 0:16) and cost **51× more per completed task** ($1.87 vs $0.04) than [Praxis-1](praxis-1.md). The comparison was run by Runway ([Praxis-1 report §7.3](../sources/runway-praxis-1-technical-report.md)). The same report says the RoboLab-120 board is now led by a different zero-shot frontier-model agent, **AMP1 at 86.0%**, under the official 10-trial protocol.
- **Benchmark adapter.** `GPT_6_Astra_Direct_EEF` in [XPolicyLab](xpolicylab.md), served through a third-party gateway ([XPolicyLab GitHub](../sources/xpolicylab-github.md)).

## Why it matters for this wiki
- **It overturns the measured pattern so far.** The [Frontier Red Team](frontier-red-team.md) found frontier models nearly useless at direct control (LIBERO 0–5.5%). Astra at per-turn end-effector control is the first contrary result at benchmark scale. It is also model-specific: GPT-5.5, one generation earlier on the same interface, is near zero.
- **Its capability profile is the inverse of a VLA's.** Fine-tuned policies win precision and long-horizon tasks. Astra wins language, symbol and generalization tasks with zero robot data. That makes it a natural System 2 for a VLA, rather than a replacement.
- **Benchmark rank and physical safety came apart in the same study.** First in sim, stopped for damaging hardware in the real world. This is the erosion the control-abstraction page predicted for the pretrained-policy layer as a de facto safety boundary.

## Related
- [OpenAI](openai.md) · [RoboDojo](robodojo.md) · [XPolicyLab](xpolicylab.md)
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) · [Code as policy](../concepts/agents/code-as-policy.md) · [Embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md)

## Mentioned in
- [GPT-6 Astra on RoboDojo (Zhang et al., 2026)](../sources/gpt-6-astra-robodojo-paper.md) — the primary for its robot-policy results.
- [XPolicyLab GitHub](../sources/xpolicylab-github.md) — the eval-only adapter.
- [RPG paper](../sources/rpg-guided-self-improvement-paper.md) — the strongest CaP-Agent0 base model (Pro).
- [UnifoLM-WLA-1 project page](../sources/unifolm-wla-1-project-page.md) — ERQA/RefSpatial leader in Unitree's tests.
- [ToyBlocks (Ai2 blog)](../sources/ai2-toyblocks-blog.md) — the agent-built simulator.
- [NVIDIA MicroDuck blog](../sources/nvidia-microduck-ai-agents-sim-blog.md) — the asset and simulation agent.
- [Jalapeño first results](../sources/openai-jalapeno-first-results.md) — kernel authoring with Codex.
- [Astranomy (NVIDIA SRL)](../sources/nvidia-srl-astranomy-blog.md) — 66–75% on RoboLab-120 in three roles; prompt geometry and history ablations; latency and cost.
- [Praxis-1 technical report](../sources/runway-praxis-1-technical-report.md) — 15.6× slower and 51× costlier per task than Praxis-1 on three YAM tasks.
