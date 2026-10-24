---
title: "NVIDIA Advances Isaac Platform for General-Purpose Robotics With New Reference Humanoid, Frameworks, Simulation Pipelines and Data (NVIDIA press release, GTC Berlin 2026)"
type: source
url: https://nvidianews.nvidia.com/news/nvidia-advances-isaac-platform-for-general-purpose-robotics-with-new-reference-humanoid-frameworks-simulation-pipelines-and-data
local_path: raw/2026-10-21-nvidia-isaac-platform-gtc-berlin.txt
sha256: 0588fb03e433842344f5285d0c8fbd537fd3219da19ab5d67da29743e349b0da
author: NVIDIA Newsroom (corporate press release; media contact Paris Fox)
published: 2026-10-21
ingested: 2026-10-22
venue: NVIDIA Newsroom, GTC Berlin keynote day
format: "corporate press release (~1,300 words body) with a partner roll-call; article-body text extracted from HTML"
tags: [nvidia, isaac, gtc-berlin, isaac-os, isaac-lab, isaac-lab-3, holoscan, gr00t, gr00t-1-7, jetson-thor, halos, igx-thor, cosmos, dgx-station, simready, human-1m-dataset, newton, agile-robots, agile-one-sn, reference-humanoid, europe, partners, vendor-source]
---

# NVIDIA Advances Isaac Platform for General-Purpose Robotics (GTC Berlin, 2026-10-21)

> [!note] Read with the partner primary
> The reference-humanoid half of this release is [Agile Robots' own launch post](agile-robots-agile-one-sn-launch.md), ingested alongside it. **They disagree on the robot's weight** (40 kg here vs 43 kg in Agile's release and product page) and **on how firm the Halos integration is** ("planned" here vs "exploring" there). See [Agile ONE SN](../entities/agile-one-sn.md).

## Summary

NVIDIA's GTC Berlin robotics release bundles five things under the [Isaac](../entities/nvidia.md) brand.
1. A **reference humanoid**, [Agile ONE SN](../entities/agile-one-sn.md) from [Agile Robots](../entities/agile-robots.md), preconfigured with [GR00T](../entities/nvidia-groot.md) on [Jetson Thor](../entities/jetson-thor.md). It is due early 2027.
2. A new runtime, **Isaac OS**, built on Holoscan.
3. **Isaac Lab 3.0 general availability.**
4. **Data and assets:** the SimReady Central Library (2,000+ assets) and the Human 1M Dataset, both on Hugging Face.
5. **Three DGX Station reference workflows:** GR00T 1.7 RL refinement, dexterous manipulation in Isaac Lab, and Cosmos post-training "using ChatGPT Astra".

[Halos](../entities/nvidia-halos.md) gains named robotics integrators. The rest is a European partner roll-call: ABB, KUKA, Sereact, Humanoid, Hexagon, NEURA, Flexion, Schaeffler, Franka, idealworks and others. The framing line is Huang's *"the ChatGPT moment for robotics is fast approaching."*

## Key claims

### Agile ONE SN (reference humanoid)
- *"a full-stack reference humanoid preconfigured with NVIDIA Isaac GR00T and powered by the NVIDIA Jetson Thor"*. It *"unifies these tools and workflows on a single platform, cutting setup time from weeks to days"* (no baseline given).
- **Body:** *"Agile ONE S humanoid body, standing 1.40 meters … and weighing 40 kilograms (88 pounds), with 31 degrees of freedom and a 3-kilogram payload per arm."*
- **Hands:** *"Dual WUJI Hand 2 five-finger hands, each offering 20 degrees of freedom, 1kHz force control and tactile sensing."* Only this release names the hand model and gives the 1 kHz figure.
- **Compute:** *"Jetson Thor … delivering 2,070 FP4 teraflops of compute and 128GB of unified memory."*
- **Sensing:** head and wrist cameras, lidar, IMUs.
- **Software:** the GR00T platform, *"the GR00T foundation model, a full workflow from data capture to deployment and whole-body control."*
- **Safety:** *"planned integration of on-robot safety protocols with the NVIDIA Halos full-stack safety system."*
- **Availability:** *"Scheduled to be available in early 2027"*, *"with interest from leading institutions such as Stanford University and ETH Zurich."* No price.

### Platform
- **Isaac OS**: *"an open source runtime framework built on NVIDIA Holoscan, [that] connects AI, sensors, controls and robot hardware for deterministic, real-time performance from simulation to physical robots."* It is new, and this release does not link a repo or docs for it.
- **Isaac Lab 3.0 is "now generally available"**: *"open source, agent-ready … from desktop to data center using multi-GPU workflows and physics engines including Newton and NVIDIA PhysX."* The release's own "dexterous manipulation" link still points at the `v3.0.0-EA` docs.
- **SimReady Central Library**: 2,000+ simulation-ready robotics and factory assets on Hugging Face, from Comau, FANUC, ForgeCAD, Franka Robotics, LG Electronics, Palatial, Robotiq, Standard Bots, Universal Robots and Vertiv.
- **Human 1M Dataset**: *"diverse human activities, synchronized three-view video and 3D hand tracking."* It is on Hugging Face, but **the full dataset is restricted to "Cosmos Coalition partners"**. Size and licence are not stated.
- **Three DGX Station reference workflows** (open source): refine **GR00T 1.7 with reinforcement learning** (linked repo: `nvidia-isaac/isaac-rlpt`), train dexterous manipulation in Isaac Lab, and *"post-train NVIDIA Cosmos world models for synthetic data generation using ChatGPT Astra."* Supporting partners named: 1X, Agile Robots, Humanoid, Maven Robotics, Mentee, MicroAGI, Rhoda, Sereact, Skild AI.
- **Halos**: *"a full-stack safety platform built on NVIDIA IGX Thor."* Integrating it are Agile Robots, Agility, Dexory, FORT Robotics and KION (warehouse safety). **SICK is "evaluating"** it for dynamic safety beyond fixed zones. Advantech and NexCOBOT are building IGX-based industrial computers. Reynolds & Moore, Accenture and TÜV SÜD are named on certification.

### Ecosystem (as NVIDIA reports it)
| Partner | Claim |
|---|---|
| ABB Robotics | Omniverse libraries in RobotStudio HyperReality, for virtual commissioning |
| KUKA | Omniverse in Visual Components FactoryLens |
| Sereact | GR00T + Cosmos Transfer to train its **Cortex** goods-handling platform on Universal Robots arms |
| Humanoid (UK) | Jetson Thor, Holoscan Sensor Bridge, Halos and **Isaac OS** to validate behaviours before industrial pilots |
| Hexagon Robotics | AEON perception: teleop video, localisation, mapping, object pose |
| Bear Robotics | KR1 perception; post-training GR00T through **Kino-2** |
| Toyota Material Handling Europe + SoftServe | Omniverse + Isaac Sim; *"reducing deployment time by up to 50%"* |
| idealworks | NVIDIA open models + Jetson for AMR **memory** |
| Analog Devices | Jetson AGX Orin + cuVSLAM AMRs |
| Hugging Face + Pollen | Isaac Lab, Isaac Sim and Newton for [Microduck](../entities/microduck.md) |
| Franka Robotics | NIM + Isaac Sim; natural language → actions on **FR3 Duo** |
| Bellboy | Jetson + GR00T for **Billie**, *"already deployed at hotels operated by Marriott, Hilton, IHG and OYO"* |
| [Flexion](../entities/flexion.md) | Isaac Lab + Newton to scale **Reflect**, its reasoning + whole-body model |
| Schaeffler | actuator technology as an *"exclusive foundational component for Newton"* |
| NEURA Robotics | Isaac Sim / Lab synthetic data for **Neuron AI** |

## Reading it critically

> [!warning] Contradiction: Agile ONE SN weight
> This release gives **40 kg (88 lb)**. [Agile Robots' release](agile-robots-agile-one-sn-launch.md) gives **43 kg (95 lb)**, and so does Agile's product page (captured the same day). The manufacturer's figure is preferred. Agile's product page puts an "Excluding hands" label next to its spec strip, so one possible reading is that the two numbers count the hands differently. Neither source says so.

> [!note] Scope loss on Thor's compute figure
> *"2,070 FP4 teraflops"* is the **sparse** FP4 number ([Jetson Thor](../entities/jetson-thor.md): 2070 TFLOPS FP4 sparse, 1035 dense FP8). The release drops the qualifier. This is the same pattern the wiki recorded in the [JetPack 7.2 correction](nvidia-jetpack-docs-index.md): a number kept, its binding lost.

> [!note] "Planned" Halos, and who the partners are
> "Planned integration" here is stronger than Agile's own *"exploring integration"*. Two of the ecosystem names, **Franka Robotics** and **idealworks**, are **Agile Robots subsidiaries**, per Agile's own boilerplate. This release presents them as independent partners.

- **"ChatGPT Astra"** is not defined anywhere in the release, and a web search on 2026-10-22 found no other reference to it. The wiki records the name verbatim and does not say what it is.
- **Isaac OS** is announced without a repo, docs link or version. Treat it as a name until a primary exists.
- **No numbers on any of the five platform items**, apart from asset count and "weeks to days".

## Entities mentioned
- [NVIDIA](../entities/nvidia.md) · [Agile Robots](../entities/agile-robots.md) · [Agile ONE SN](../entities/agile-one-sn.md) · [Agile ONE](../entities/agile-one.md) · [Isaac GR00T](../entities/nvidia-groot.md) · [Jetson Thor](../entities/jetson-thor.md) · [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) · [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) · [Newton](../entities/newton-physics-engine.md) · [NVIDIA Cosmos](../entities/nvidia-cosmos.md) · [NVIDIA Halos](../entities/nvidia-halos.md) · [Microduck](../entities/microduck.md) · [Flexion](../entities/flexion.md) · [Agility / Digit](../entities/digit.md)
- No pages: Isaac OS, Holoscan, SimReady Central, Human 1M Dataset, DGX Station, WUJI Hand 2, Sereact, Humanoid (UK), Hexagon AEON, Bear Robotics, Bellboy, NEURA, idealworks, Schaeffler, SICK, ABB, KUKA.

## Concepts touched
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — the Isaac Lab / Newton / SimReady pipeline.
- [Whole-body control](../concepts/robotics/whole-body-control.md) — GR00T WBC shipped on a third-party humanoid.

## Open questions
- **What is Isaac OS** relative to Isaac ROS and Holoscan? It is called "open source" with no repo given. Does it replace any part of [Isaac ROS](../entities/isaac-ros.md)?
- **What is "ChatGPT Astra"?** *Update 2026-10-24:* two days later NVIDIA's [Microduck tutorial](nvidia-microduck-ai-agents-sim-blog.md) shows an agent called just **"Astra"** in use. It takes a handoff from Hermes, uses *cloud* image editing, scripts FreeCAD and Blender, exports USD and assembles the scene in Isaac Sim. It is still not expanded or attributed there. The most likely reading is the same product, possibly OpenAI's, given the "ChatGPT" prefix, but no source says so.
- **Human 1M:** how many hours, what licence, and what does a non-Coalition user actually get?
- **Isaac Lab 3.0 GA vs EA:** what changed, and is the release's own linked docs path (`v3.0.0-EA`) stale?
- **Agile ONE SN price**, and which weight is correct.
