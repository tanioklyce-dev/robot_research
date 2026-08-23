---
title: NVIDIA
type: entity
subtype: company
created: 2026-05-06
updated: 2026-08-23
sources: 53
tags: [nvidia, gpu, simulation, physical-ai]
---

GPU vendor and the dominant force in the agentic-robotics simulation stack as of 2026. Owns or co-owns most of the major substrate components: simulator ([NVIDIA Isaac Sim](nvidia-isaac-sim.md)), learning framework ([NVIDIA Isaac Lab](nvidia-isaac-lab.md)), physics engine ([Newton physics engine](newton-physics-engine.md), co-developed), world model ([NVIDIA Cosmos](nvidia-cosmos.md)), and a flagship open VLA ([NVIDIA GR00T](nvidia-groot.md)).

## What we know
- **Physical AI stack** announced/expanded at GTC 2026, with Newton 1.0 GA, Isaac Lab 3.0, Isaac Sim 6.0, GR00T N1.6 GA / N1.7 EA, and Omniverse NuRec ([NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md), [NVIDIA Newton Physics Engine Developer Page](../sources/nvidia-newton-physics-engine-developer-page.md)).
- **Linux Foundation collaboration**: contributed Newton to the Linux Foundation under joint stewardship with [Google DeepMind](google-deepmind.md) and [Disney Research](disney-research.md).
- **Ecosystem partnerships**: powers [AGIBOT Genie Sim 3.0](agibot-genie-sim.md) (built on Isaac Sim) and [GE-Sim2](genie-envisioner.md) (built on Cosmos-Predict2).
- **Research arm**: NVIDIA Research is co-authored on the [RoboCasa365](robocasa.md) paper through Yuke Zhu's dual UT Austin / NVIDIA appointment ([RoboCasa365 Paper](../sources/robocasa365-paper.md)).
- **Developer cloud**: owns [NVIDIA Brev](nvidia-brev.md), a cross-cloud GPU-instance broker for AI/ML dev work (acquired from brev.dev in 2024) ([NVIDIA Brev Docs](../sources/nvidia-brev-docs.md)).
- **Omnimodal world model**: **[Cosmos 3](nvidia-cosmos.md)** (June 2026) unified the Cosmos platform into a single Mixture-of-Transformers model spanning language/image/video/audio/action — #1 open-weight T2I + I2V (Artificial Analysis) and #1 RoboArena policy at launch ([Cosmos 3 technical report](../sources/cosmos-3-technical-report.md), led by [Ming-Yu Liu](ming-yu-liu.md)).
- **In-house research lab**: [NVIDIA GEAR](nvidia-gear.md) (Generalist Embodied Agent Research, founded Feb 2024) is the source of GR00T, the Dream*-world-model line (DreamGen / DreamZero / DreamDojo), the Eureka / DrEureka LLM-as-reward-designer line, the humanoid whole-body cluster (SONIC, HOVER, ASAP, Doorman, VIRAL), and much of the Isaac Lab + RoboCasa + MimicGen substrate ([GEAR Publications](../sources/nvidia-gear-publications.md)).
- **Edge AI compute**: the Jetson product line — [Jetson Orin Nano](jetson-orin-nano.md), Orin NX, AGX Orin, and the new **Blackwell-generation [Jetson Thor](jetson-thor.md)** (T5000 + T4000 modules, AGX Thor Dev Kit, launched 2025-08-25) — paired with [JetPack](jetpack.md) SDK (CUDA + TensorRT + DeepStream + VPI) on [Jetson Linux](jetson-linux.md) BSP. The substrate for most wiki-tracked educational and research robots that aren't running on an x86 workstation.
- **Agentic-AI safety stack**: NVIDIA also owns the *guardrail* layer — [NeMo Guardrails](nemo-guardrails.md) (programmable runtime rails + the NemoGuard content-safety / topic-control / jailbreak-detect NIMs) and [garak](garak.md) (open-source LLM vulnerability scanner), packaged as a build→deploy→run "safety recipe" ([NVIDIA safety recipe](../sources/nvidia-safety-recipe-agentic-ai.md), July 2025; blueprint deprecated 2026-04-22 in favor of NeMo Microservices). The same pattern reappears as NVIDIA OpenShell inside [NemoClaw](../sources/nvidia-nemoclaw-page.md). Notable as the one part of NVIDIA's agentic stack with **no robotics story yet** — every guard model classifies text, not tool calls.
- **Personal AI supercomputer**: [DGX Spark](dgx-spark.md) — desktop-form-factor GB10 Grace Blackwell box with 128 GB unified memory and RT cores; NVIDIA's prescribed workstation for the train-on-Spark, deploy-on-Thor split ([Jetson Thor vs DGX Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md)).

## Grasping

- **[GraspGen / GraspGen-X](graspgen.md)** — NVIDIA's 6-DOF grasp-generation line (SE(3) diffusion generator + discriminator). [GraspGen-X](../sources/graspgenx-paper.md) (CVPR 2026, with Princeton) makes it **cross-embodiment across gripper morphology**, trained on 350 M ACRONYM-labelled grasps in [Isaac Sim](nvidia-isaac-sim.md) using **procedurally generated grippers**. Model, code and dataset promised on NVlabs. It is the grasp module of the modular NVIDIA manipulation stack whose other pieces — [cuRobo](curobo.md), nvblox, FoundationStereo, FoundationPose — this wiki already tracks separately.

## Related
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md), [NVIDIA Isaac Lab](nvidia-isaac-lab.md), [Newton physics engine](newton-physics-engine.md), [NVIDIA Cosmos](nvidia-cosmos.md), [NVIDIA Brev](nvidia-brev.md) — products.
- [NVIDIA GEAR](nvidia-gear.md) — in-house research lab (Jim Fan + Yuke Zhu).
- [NeMo Guardrails](nemo-guardrails.md), [garak](garak.md) — the agentic-AI safety layer (runtime rails + red-team scanner).
- [Jetson Orin Nano](jetson-orin-nano.md), [Jetson Thor](jetson-thor.md), [JetPack](jetpack.md), [Jetson Linux](jetson-linux.md) — edge-AI hardware and software stack.
- [DGX Spark](dgx-spark.md) — desktop AI supercomputer; the workstation half of the Thor deploy / Spark train split.
- [AGIBOT](agibot.md) — major downstream user.

## Mentioned in
- [Cosmos 3 Technical Report](../sources/cosmos-3-technical-report.md)
- [Develop Physical AI with NVIDIA Cosmos 3 (HF blog)](../sources/nvidia-cosmos-3-hf-blog.md)
- [NVIDIA Newton Physics Engine Developer Page](../sources/nvidia-newton-physics-engine-developer-page.md)
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)
- [Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md)
- [RoboCasa365 Paper](../sources/robocasa365-paper.md)
- [OpenUSD Rigid Body Physics Proposal](../sources/openusd-rigid-body-physics-proposal.md)
- [Using OpenUSD for Modular and Scalable Robotic Simulation](../sources/nvidia-openusd-for-robotic-simulation.md)
- [Building CAD-to-USD Workflows with NVIDIA Omniverse](../sources/nvidia-cad-to-usd-jt-workflows.md)
- [NVIDIA Brev Docs](../sources/nvidia-brev-docs.md)
- [Safeguard Agentic AI Systems with the NVIDIA Safety Recipe](../sources/nvidia-safety-recipe-agentic-ai.md)
- [NVIDIA GEAR Lab — Publications](../sources/nvidia-gear-publications.md)
- [NVIDIA Jetson Orin Nano Dev Kit software setup](../sources/nvidia-jetson-orin-nano-devkit-software-setup.md)
- [JetPack 6.2.2 release](../sources/nvidia-jetpack-6-2-2-release.md)
- [JetPack docs index](../sources/nvidia-jetpack-docs-index.md)
- [Jetson Linux R36.5 release](../sources/nvidia-jetson-linux-r36-5-release.md)
- [Jetson Linux R36.5 update mechanism](../sources/nvidia-jetson-linux-r36-5-update-mechanism.md)
- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../sources/hai-world-model-spatial-intelligence-brief.md) — Omniverse cited as the reference point for *conventional* simulation ("slow, specialist work" per environment) against which learned world models are pitched; NVIDIA also named among the incumbents leading the world-model push, and among HAI's disclosed funders.
- [GraspGen-X: Cross-Embodiment 6-DOF Diffusion-based Grasping](../sources/graspgenx-paper.md)
