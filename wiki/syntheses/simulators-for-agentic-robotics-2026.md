---
title: Simulators for agentic robotics — 2026 landscape
type: synthesis
created: 2026-05-06
updated: 2026-05-07
tags: [simulation, agentic-robotics, vla, world-models, survey]
---

# Simulators for agentic robotics — 2026 landscape

The "agentic" framing matters. This survey filters for simulators that support closed-loop control by AI agents — primarily [VLA models](../concepts/vla-models.md) and [world models](../concepts/world-model-simulators.md) — not classical model-based controllers. Six categories worth distinguishing.

## 1. Core GPU physics platforms

The workhorses for training policies. All four are GPU-accelerated and support massively parallel environments.

| Simulator | Steward | Backend | Distinguishing feature |
|---|---|---|---|
| [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) / [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) | NVIDIA | PhysX, Newton, Warp, MuJoCo (pluggable) | Industry default; richest ecosystem |
| [Newton physics engine](../entities/newton-physics-engine.md) | Linux Foundation ([NVIDIA](../entities/nvidia.md) + [DeepMind](../entities/google-deepmind.md) + [Disney](../entities/disney-research.md)) | Warp + OpenUSD | New in 2025–26, becoming the shared substrate |
| [MuJoCo Playground](../entities/mujoco-playground.md) | Google DeepMind | MJX (JAX), Warp, Newton | Strongest sim-to-real research story |
| [Genesis](../entities/genesis.md) | 20+ lab consortium | Custom (Python-first) | Headline 10–80× speedup; built-in VLM-driven scene generation |

**The shared substrate trend**: [Newton](../entities/newton-physics-engine.md) (as backend) + OpenUSD (as scene format) are emerging as common ground across NVIDIA Isaac Lab and DeepMind's MuJoCo Playground. This reduces lock-in and lets researchers move policies across stacks ([NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)).

## 2. Embodied-AI / household-scale platforms

Built on top of category 1. Provide scenes, tasks, and evaluation suites for high-level agent behavior.

- **[AGIBOT Genie Sim 3.0](../entities/agibot-genie-sim.md)** — open-sourced at CES 2026. Runs on [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md). LLM-driven scene generation, 100k+ eval scenarios, 10k hours synthetic data. Benchmarks GR00T, Pi, GO-2 ([AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)).
- **[RoboCasa](../entities/robocasa.md)** / RoboCasa365 — UT Austin. 365 tasks across 2,500 kitchens ([RoboCasa365 Paper](../sources/robocasa365-paper.md)).
- **[ManiSkill](../entities/maniskill.md)** / ManiSkill-HAB — [Hillbot](../entities/hillbot.md), [SAPIEN](../entities/sapien.md)-based. Realistic low-level manipulation chains; >4,000 samples/sec on HAB ([ManiSkill-HAB Paper](../sources/maniskill-hab-paper.md)).
- **Older suites still cited**: Habitat (Meta), BEHAVIOR/iGibson (Stanford), AI2-THOR (Allen AI). Less central to the agentic VLA cycle in 2026.

## 3. World-model simulators — two paradigms

Both replace authored physics with learned models, but predict different things. See [World-model simulators](../concepts/world-model-simulators.md) for the full treatment.

### 3a. Generative-video world models
Generate next-frame *pixels*. Train and plan inside a learned video generator.
- **[NVIDIA Cosmos](../entities/nvidia-cosmos.md)** — world foundation model (Cosmos-Predict2-2B-Video2World powers downstream simulators).
- **[Genie Envisioner](../entities/genie-envisioner.md)** 2.0 / GE-Sim2 — built on Cosmos-Predict2. Treats action as first-class via the World Action Model framework. Minute-scale stable rollouts ([AGIBOT Genie Envisioner 2.0 Announcement](../sources/agibot-genie-envisioner-2-announcement.md), [Genie Envisioner Paper](../sources/genie-envisioner-paper.md)).

### 3b. JEPA / latent-prediction world models
Predict next-state *representations* in a learned latent space — no pixels generated. The [Meta FAIR](../entities/meta-fair.md) / Yann LeCun line. See [Joint-Embedding Predictive Architecture](../concepts/jepa.md) for the umbrella concept.
- **[V-JEPA 2 / V-JEPA 2-AC](../entities/v-jepa-2.md)** ([Meta FAIR](../entities/meta-fair.md) + [Mila](../entities/mila.md)) — 1B-param ViT-g encoder pretrained on 1M+ hours of internet video; 300M-param action-conditioned predictor post-trained on 62 hr of Droid robot data. **Zero-shot deployment on Franka arms in two new labs** for image-goal pick-and-place via MPC ([V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)).
- **[LeWorldModel](../entities/leworldmodel.md)** ([Mila](../entities/mila.md) + NYU + Samsung SAIL + Brown) — first stable end-to-end JEPA from raw pixels with only two loss terms; 15M params; single-GPU training; **48× faster planning** than foundation-model-based world models ([LeWorldModel Paper](../sources/leworldmodel-paper.md)).

This category does **not yet replace** physics engines — it complements them by enabling pretraining on observed data without a physics setup. Adoption is early but accelerating: **V-JEPA 2-AC's zero-shot Franka result** is a notable validation point that latent-prediction world models can produce real-robot capability with very little robot data.

## 4. Classic / ROS-native (mention, not focus)

Gazebo, Webots, CoppeliaSim, PyBullet, Drake. Still essential for ROS-based deployment and rigorous control work, but the agentic-robotics center of gravity has moved to categories 1–3.

## 5. Industry usage signals

- **Tesla Optimus**: in-house sim + sim-to-real + imitation from human video; no public stack.
- **VLA labs (typical pattern)**: Isaac Lab or MuJoCo Playground for training, Genie Sim or RoboCasa for eval. Genesis adopters claim faster iteration but production usage remains unproven.

## 6. Real-robot agentic stacks (the consumers)

The simulators in categories 1–3 train policies that ultimately run on hardware. Two notable real-robot stacks worth contrasting against the sim-heavy paths:

- **[stretch_ai](../entities/stretch-ai.md)** ([Hello Robot](../entities/hello-robot.md)) — open-source Python stack for the [Stretch](../entities/stretch.md) mobile manipulator. Includes a working **[LLM agent](../concepts/llm-agent-architecture.md)** (Qwen2.5-3B-Instruct / Gemma / GPT-4o-mini) that translates natural-language goals into tool calls dispatched to deterministic skills (mapping, grasping, perception). Notably skips simulation entirely — runs on the real robot ([Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)).
- **[Robot Utility Models](../entities/robot-utility-models.md)** (NYU / Meta) — generalist visuomotor BC policies achieving ~90% zero-shot success on Stretch in novel environments, with cross-embodiment transfer to xArm 7. Trained on real demos, not sim ([Robot Utility Models Project Page](../sources/robot-utility-models-website.md)).
- **[Hiwonder ROSOrin](../entities/rosorin.md) / [ROSOrin Pro](../entities/rosorin-pro.md)** ([Hiwonder](../entities/hiwonder.md), educational tier) — same [LLM-agent](../concepts/llm-agent-architecture.md) pattern as stretch_ai, packaged for classrooms. Cloud (GPT-4o, [Qwen-plus](../entities/qwen.md), StepFun VLM) and offline ([Ollama](../entities/ollama.md) + [qwen3:1.7b](../entities/qwen.md) + sherpa-onnx) variants on the base kit ([Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)). The Pro variant adds a 6-DOF arm + [OpenClaw](../entities/openclaw.md) — the same architecture extended to manipulation, with skill primitives `pick`, `place`, `voice_pick`, AprilTag pickup, depth-based interactive grasping ([Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md)).

Together these hint at a **sim-vs-real divide**: the NVIDIA / AGIBOT path optimizes for VLA training scale inside simulators; the Hello-Robot ecosystem optimizes for shipping deployable hardware that researchers can run real-data experiments on. The two paths are complementary — sim-trained policies need real targets like Stretch, and real-data corpora like RUM's 5,509 trajectories feed back into the simulators' synthetic-data pipelines.

## Recommendations by use case

- **Training a humanoid policy with physics fidelity** → [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) + [Newton physics engine](../entities/newton-physics-engine.md).
- **Benchmarking a VLA on household tasks** → [AGIBOT Genie Sim 3.0](../entities/agibot-genie-sim.md) or [RoboCasa](../entities/robocasa.md).
- **Manipulation research with strong sim-to-real story** → [MuJoCo Playground](../entities/mujoco-playground.md).
- **Generating synthetic training data at scale** → [Genesis](../entities/genesis.md) (high-throughput) or [Genie Envisioner](../entities/genie-envisioner.md) (learned-world rollouts).
- **Long-horizon multi-skill evaluation** → [ManiSkill](../entities/maniskill.md)-HAB or [AGIBOT Genie Sim 3.0](../entities/agibot-genie-sim.md).

## Contradictions and open questions

> [!warning] GR00T version inconsistency
> Sources reference both **GR00T N1.6** ([NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)) and **GR00T N1.7 Early Access** ([Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md)) as the current version. Likely a fast-moving GA-vs-EA distinction; verify when GR00T gets its own page.

- [Genesis](../entities/genesis.md)'s headline 10–80× speedup vs. Isaac/MJX is widely cited but real-world adoption signals are weaker than the marketing — needs validation on contact-rich workloads.
- Whether [World-model simulators](../concepts/world-model-simulators.md) (Cosmos, Genie Envisioner) can replace physics engines for full closed-loop training, or only complement them, is unsettled.
- **Coverage gaps**: Pi (Physical Intelligence) and Skild AI's simulation approaches, classic VLA benchmarks (LIBERO, RoboMimic), Drake internals — none covered here yet.

## Deeper dives (filed as separate syntheses)

This page surveys the landscape; four follow-up syntheses go deeper on specific structural questions raised here:

- [Newton + OpenUSD — the substrate convergence](newton-openusd-substrate-convergence.md) — deeper on §1's "shared substrate trend".
- [Generative-video vs JEPA world models](generative-video-vs-jepa-world-models.md) — deeper on §3's two-paradigm split.
- [LLM-agent architecture across stacks](llm-agent-architecture-across-stacks.md) — deeper on §6's stretch_ai / ROSOrin / OpenClaw convergence.
- [Sim-heavy vs real-data paths to generalist policies](sim-heavy-vs-real-data-paths.md) — deeper on §6's "sim-vs-real divide", reframed as three paths.

## Sources used in this synthesis
- [NVIDIA Newton Physics Engine Developer Page](../sources/nvidia-newton-physics-engine-developer-page.md)
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [MuJoCo Playground Paper](../sources/mujoco-playground-paper.md)
- [Genesis Project Page](../sources/genesis-project-page.md)
- [AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)
- [AGIBOT Genie Envisioner 2.0 Announcement](../sources/agibot-genie-envisioner-2-announcement.md)
- [Genie Envisioner Paper](../sources/genie-envisioner-paper.md)
- [RoboCasa365 Paper](../sources/robocasa365-paper.md)
- [ManiSkill-HAB Paper](../sources/maniskill-hab-paper.md)
- [Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md)
- [Stretch AI LLM Agent Documentation](../sources/stretch-ai-llm-agent-docs.md)
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
- [LeWorldModel Paper](../sources/leworldmodel-paper.md)
- [Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)
- [Hiwonder ROSOrin Pro User Manual](../sources/hiwonder-rosorin-pro-user-manual.md)
- [Hiwonder OpenClaw Practical Tutorial](../sources/hiwonder-openclaw-tutorial.md)
