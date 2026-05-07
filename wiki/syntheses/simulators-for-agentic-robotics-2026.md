---
title: Simulators for agentic robotics — 2026 landscape
type: synthesis
created: 2026-05-06
updated: 2026-05-07
tags: [simulation, agentic-robotics, vla, world-models, survey]
---

# Simulators for agentic robotics — 2026 landscape

The "agentic" framing matters. This survey filters for simulators that support closed-loop control by AI agents — primarily [[vla-models|VLA models]] and [[world-model-simulators|world models]] — not classical model-based controllers. Six categories worth distinguishing.

## 1. Core GPU physics platforms

The workhorses for training policies. All four are GPU-accelerated and support massively parallel environments.

| Simulator | Steward | Backend | Distinguishing feature |
|---|---|---|---|
| [[nvidia-isaac-sim|NVIDIA Isaac Sim]] / [[nvidia-isaac-lab|NVIDIA Isaac Lab]] | NVIDIA | PhysX, Newton, Warp, MuJoCo (pluggable) | Industry default; richest ecosystem |
| [[newton-physics-engine|Newton physics engine]] | Linux Foundation ([[nvidia|NVIDIA]] + [[google-deepmind|DeepMind]] + [[disney-research|Disney]]) | Warp + OpenUSD | New in 2025–26, becoming the shared substrate |
| [[mujoco-playground|MuJoCo Playground]] | Google DeepMind | MJX (JAX), Warp, Newton | Strongest sim-to-real research story |
| [[genesis|Genesis]] | 20+ lab consortium | Custom (Python-first) | Headline 10–80× speedup; built-in VLM-driven scene generation |

**The shared substrate trend**: [[newton-physics-engine|Newton]] (as backend) + OpenUSD (as scene format) are emerging as common ground across NVIDIA Isaac Lab and DeepMind's MuJoCo Playground. This reduces lock-in and lets researchers move policies across stacks ([[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]).

## 2. Embodied-AI / household-scale platforms

Built on top of category 1. Provide scenes, tasks, and evaluation suites for high-level agent behavior.

- **[[agibot-genie-sim|AGIBOT Genie Sim 3.0]]** — open-sourced at CES 2026. Runs on [[nvidia-isaac-sim|NVIDIA Isaac Sim]]. LLM-driven scene generation, 100k+ eval scenarios, 10k hours synthetic data. Benchmarks GR00T, Pi, GO-2 ([[agibot-genie-sim-3-announcement|AGIBOT Genie Sim 3.0 Announcement]]).
- **[[robocasa|RoboCasa]]** / RoboCasa365 — UT Austin. 365 tasks across 2,500 kitchens ([[robocasa365-paper|RoboCasa365 Paper]]).
- **[[maniskill|ManiSkill]]** / ManiSkill-HAB — [[hillbot|Hillbot]], [[sapien|SAPIEN]]-based. Realistic low-level manipulation chains; >4,000 samples/sec on HAB ([[maniskill-hab-paper|ManiSkill-HAB Paper]]).
- **Older suites still cited**: Habitat (Meta), BEHAVIOR/iGibson (Stanford), AI2-THOR (Allen AI). Less central to the agentic VLA cycle in 2026.

## 3. World-model simulators — two paradigms

Both replace authored physics with learned models, but predict different things. See [[world-model-simulators|World-model simulators]] for the full treatment.

### 3a. Generative-video world models
Generate next-frame *pixels*. Train and plan inside a learned video generator.
- **[[nvidia-cosmos|NVIDIA Cosmos]]** — world foundation model (Cosmos-Predict2-2B-Video2World powers downstream simulators).
- **[[genie-envisioner|Genie Envisioner]]** 2.0 / GE-Sim2 — built on Cosmos-Predict2. Treats action as first-class via the World Action Model framework. Minute-scale stable rollouts ([[agibot-genie-envisioner-2-announcement|AGIBOT Genie Envisioner 2.0 Announcement]], [[genie-envisioner-paper|Genie Envisioner Paper]]).

### 3b. JEPA / latent-prediction world models
Predict next-state *representations* in a learned latent space — no pixels generated. The [[meta-fair|Meta FAIR]] / Yann LeCun line. See [[jepa|Joint-Embedding Predictive Architecture]] for the umbrella concept.
- **[[v-jepa-2|V-JEPA 2 / V-JEPA 2-AC]]** ([[meta-fair|Meta FAIR]] + [[mila|Mila]]) — 1B-param ViT-g encoder pretrained on 1M+ hours of internet video; 300M-param action-conditioned predictor post-trained on 62 hr of Droid robot data. **Zero-shot deployment on Franka arms in two new labs** for image-goal pick-and-place via MPC ([[v-jepa-2-paper|V-JEPA 2 Paper]]).
- **[[leworldmodel|LeWorldModel]]** ([[mila|Mila]] + NYU + Samsung SAIL + Brown) — first stable end-to-end JEPA from raw pixels with only two loss terms; 15M params; single-GPU training; **48× faster planning** than foundation-model-based world models ([[leworldmodel-paper|LeWorldModel Paper]]).

This category does **not yet replace** physics engines — it complements them by enabling pretraining on observed data without a physics setup. Adoption is early but accelerating: **V-JEPA 2-AC's zero-shot Franka result** is a notable validation point that latent-prediction world models can produce real-robot capability with very little robot data.

## 4. Classic / ROS-native (mention, not focus)

Gazebo, Webots, CoppeliaSim, PyBullet, Drake. Still essential for ROS-based deployment and rigorous control work, but the agentic-robotics center of gravity has moved to categories 1–3.

## 5. Industry usage signals

- **Tesla Optimus**: in-house sim + sim-to-real + imitation from human video; no public stack.
- **VLA labs (typical pattern)**: Isaac Lab or MuJoCo Playground for training, Genie Sim or RoboCasa for eval. Genesis adopters claim faster iteration but production usage remains unproven.

## 6. Real-robot agentic stacks (the consumers)

The simulators in categories 1–3 train policies that ultimately run on hardware. Two notable real-robot stacks worth contrasting against the sim-heavy paths:

- **[[stretch-ai|stretch_ai]]** ([[hello-robot|Hello Robot]]) — open-source Python stack for the [[stretch|Stretch]] mobile manipulator. Includes a working **[[llm-agent-architecture|LLM agent]]** (Qwen2.5-3B-Instruct / Gemma / GPT-4o-mini) that translates natural-language goals into tool calls dispatched to deterministic skills (mapping, grasping, perception). Notably skips simulation entirely — runs on the real robot ([[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]]).
- **[[robot-utility-models|Robot Utility Models]]** (NYU / Meta) — generalist visuomotor BC policies achieving ~90% zero-shot success on Stretch in novel environments, with cross-embodiment transfer to xArm 7. Trained on real demos, not sim ([[robot-utility-models-website|Robot Utility Models Project Page]]).
- **[[rosorin|Hiwonder ROSOrin]] / [[rosorin-pro|ROSOrin Pro]]** ([[hiwonder|Hiwonder]], educational tier) — same [[llm-agent-architecture|LLM-agent]] pattern as stretch_ai, packaged for classrooms. Cloud (GPT-4o, [[qwen|Qwen-plus]], StepFun VLM) and offline ([[ollama|Ollama]] + [[qwen|qwen3:1.7b]] + sherpa-onnx) variants on the base kit ([[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]]). The Pro variant adds a 6-DOF arm + [[openclaw|OpenClaw]] — the same architecture extended to manipulation, with skill primitives `pick`, `place`, `voice_pick`, AprilTag pickup, depth-based interactive grasping ([[hiwonder-openclaw-tutorial|Hiwonder OpenClaw Practical Tutorial]]).

Together these hint at a **sim-vs-real divide**: the NVIDIA / AGIBOT path optimizes for VLA training scale inside simulators; the Hello-Robot ecosystem optimizes for shipping deployable hardware that researchers can run real-data experiments on. The two paths are complementary — sim-trained policies need real targets like Stretch, and real-data corpora like RUM's 5,509 trajectories feed back into the simulators' synthetic-data pipelines.

## Recommendations by use case

- **Training a humanoid policy with physics fidelity** → [[nvidia-isaac-lab|NVIDIA Isaac Lab]] + [[newton-physics-engine|Newton physics engine]].
- **Benchmarking a VLA on household tasks** → [[agibot-genie-sim|AGIBOT Genie Sim 3.0]] or [[robocasa|RoboCasa]].
- **Manipulation research with strong sim-to-real story** → [[mujoco-playground|MuJoCo Playground]].
- **Generating synthetic training data at scale** → [[genesis|Genesis]] (high-throughput) or [[genie-envisioner|Genie Envisioner]] (learned-world rollouts).
- **Long-horizon multi-skill evaluation** → [[maniskill|ManiSkill]]-HAB or [[agibot-genie-sim|AGIBOT Genie Sim 3.0]].

## Contradictions and open questions

> [!warning] GR00T version inconsistency
> Sources reference both **GR00T N1.6** ([[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]) and **GR00T N1.7 Early Access** ([[top-10-physical-ai-models-2026|Top 10 Physical AI Models 2026]]) as the current version. Likely a fast-moving GA-vs-EA distinction; verify when GR00T gets its own page.

- [[genesis|Genesis]]'s headline 10–80× speedup vs. Isaac/MJX is widely cited but real-world adoption signals are weaker than the marketing — needs validation on contact-rich workloads.
- Whether [[world-model-simulators|World-model simulators]] (Cosmos, Genie Envisioner) can replace physics engines for full closed-loop training, or only complement them, is unsettled.
- **Coverage gaps**: Pi (Physical Intelligence) and Skild AI's simulation approaches, classic VLA benchmarks (LIBERO, RoboMimic), Drake internals — none covered here yet.

## Deeper dives (filed as separate syntheses)

This page surveys the landscape; four follow-up syntheses go deeper on specific structural questions raised here:

- [[newton-openusd-substrate-convergence|Newton + OpenUSD — the substrate convergence]] — deeper on §1's "shared substrate trend".
- [[generative-video-vs-jepa-world-models|Generative-video vs JEPA world models]] — deeper on §3's two-paradigm split.
- [[llm-agent-architecture-across-stacks|LLM-agent architecture across stacks]] — deeper on §6's stretch_ai / ROSOrin / OpenClaw convergence.
- [[sim-heavy-vs-real-data-paths|Sim-heavy vs real-data paths to generalist policies]] — deeper on §6's "sim-vs-real divide", reframed as three paths.

## Sources used in this synthesis
- [[nvidia-newton-physics-engine-developer-page|NVIDIA Newton Physics Engine Developer Page]]
- [[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]]
- [[mujoco-playground-paper|MuJoCo Playground Paper]]
- [[genesis-project-page|Genesis Project Page]]
- [[agibot-genie-sim-3-announcement|AGIBOT Genie Sim 3.0 Announcement]]
- [[agibot-genie-envisioner-2-announcement|AGIBOT Genie Envisioner 2.0 Announcement]]
- [[genie-envisioner-paper|Genie Envisioner Paper]]
- [[robocasa365-paper|RoboCasa365 Paper]]
- [[maniskill-hab-paper|ManiSkill-HAB Paper]]
- [[top-10-physical-ai-models-2026|Top 10 Physical AI Models 2026]]
- [[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]]
- [[robot-utility-models-website|Robot Utility Models Project Page]]
- [[v-jepa-2-paper|V-JEPA 2 Paper]]
- [[leworldmodel-paper|LeWorldModel Paper]]
- [[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]]
- [[hiwonder-rosorin-pro-user-manual|Hiwonder ROSOrin Pro User Manual]]
- [[hiwonder-openclaw-tutorial|Hiwonder OpenClaw Practical Tutorial]]
