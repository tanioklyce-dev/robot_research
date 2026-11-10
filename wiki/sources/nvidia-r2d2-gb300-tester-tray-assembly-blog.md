---
title: "The Machines that Make the Machines"
type: source
url: https://developer.nvidia.com/blog/the-machines-that-make-the-machines/
author: "Iretiayo Akinola, Alperen Degirmenci, Yijie Guo, Hugo Hadfield, Lars Johannsmeier, Alexander Lefort, Yashraj Narang, Yichao Pan, Yixuan Wang (NVIDIA)"
published: 2026-10-07
format: vendor technical blog post (R²D² series)
tags: [nvidia, nvidia-research, r2d2, gb300, nvidia-srl, assembly, contact-rich-manipulation, connector-insertion, pose-estimation, doper, talos, sparr, residual-rl, impedance-control, flexible-automation, evaluation, inverse-bitter-lesson]
ingested: 2026-11-10
---

# The Machines that Make the Machines

## Summary

The [NVIDIA Seattle Robotics Lab](../entities/nvidia-seattle-robotics-lab.md) and the Isaac engineering team report on automating two steps of building GB300 tester trays: fitting a busbar and inserting four cable-mounted connectors. Unlike the rest of the [R²D² series](#the-r²d²-series), this is a first-hand engineering case study, not a summary of papers.

Its conclusion runs against the field's default. **A classical pipeline solved most of the job.** Learning was used only where classical methods failed, and end-to-end imitation learning failed outright on the connectors. Neither task yet meets the manufacturer's targets, and the post gives no trial counts.

## Key claims

### Targets

Targets were set with the NVIDIA Operations Team and Foxconn: **99.5% success, at most twice a skilled worker's time, and no unintended contact with the tray**. The authors contrast this with research norms, where *"50%-60% success rates are often sufficient"* and 10 to 20 trials per task are common.

| Task | Target | Reported |
|---|---|---|
| Busbar: fixture, busbar, 16 screws, clamp removal | 99.5%, ≤124 s | Above 95%, 160 s |
| Four connectors: lift cable, grasp connector, insert | 99.5%, ≤72 s for all four | 90–95%, about 40 s per cable |

The post says the team is *"rapidly approaching"* these thresholds. Read against the table, connector cycle time is about 160 s against 72 s, so more than double the target.

### Busbar: the classical pipeline was enough

- **Perception.** FoundationPose, extended to take several views and keep the most confident estimate, because single views could be off by 90 or 180 degrees. It was later replaced by DOPER.
- **Planning.** A fast waypoint planner, plus alignment moves along Lissajous curves.
- **Control.** A [high-performance impedance controller](../concepts/robotics/impedance-control.md) with automatic damping design and inertial compensation.
- **Hardware.** Three arms: two Flexiv Rizon 4S and a UR10e with a screwdriver. Screwdriving alone misses its time budget.

### Connectors: where learning helped and where it didn't

- **Cable grasp.** SAM3 segmentation plus a fitted centreline. It produced *"almost no observed failures."*
- **Connector grasp.** A general pose model failed on small, textureless parts. **Behaviour cloning with ACT and diffusion policies also had low success**, because each cable deforms after limited handling and only a few were available. The authors call this the **"inverse bitter lesson"**: when data can't be scaled, approaches using domain knowledge are worth revisiting.
- **DOPER** (Deep Object Pose Estimation Revisited). A per-part keypoint model trained on renders of the CAD model, then fine-tuned on pseudolabels from a 3D neural reconstruction of the real part. It runs at 30 Hz or faster.
- **Gripper fingers.** 3D-printed fingers shaped to constrain parts during closure made grasps repeatable without touch sensing or regrasping.
- **Insertion.** RL in [Isaac Lab](../entities/nvidia-isaac-lab.md) worked for the large connector and less well for the small one, where small pose errors caused slipping. **SPARR** then adds a residual policy trained by RL on the real robot, taking force-torque input because the connector is hidden during insertion.

### Infrastructure

- **Robotics services.** Libraries packaged as Docker containers with HTTP endpoints, including [cuRobo](../entities/curobo.md), FoundationPose and FoundationStereo.
- **TALOS.** The Task and Agent Lifecycle Orchestration System sits on ros2_control, sequences planners, controllers and learned policies, and runs control loops above 500 Hz. It supports Franka FR3, Flexiv Rizon 4S, UR10e and SO-101.
- **Agent access.** TALOS is exposed through web interfaces so coding agents can use it. The authors say this aligns with [Anthropic's Model Hardware Standard](../entities/model-hardware-standard.md), and point to their open DROID+ project.

### Deployment and evaluation

- **Evidence bar.** Showing 99.5% success with one-sided 95% confidence needs **zero failures in at least 598 trials**. That arithmetic is correct: 0.995 to the 598th power is just under 0.05. Wear means such a test could consume hundreds of duplicate GB300 parts.
- **Proposal.** Deploy with strong but imperfect performance, record human interventions and keep improving, as autonomous-vehicle programmes do, until enough deployment data exists to bound performance.
- **Long term.** Three paths are named: a deployment data flywheel, world models, and agent-driven robotics. The agent-driven examples cited include [GaP](gap-graph-as-policy-paper.md) and [ASPIRE](aspire-paper.md).

### Limitations noted at ingest

- **No trial counts.** Success rates are given as ranges, with no numbers of trials, so their precision is unknown. That matters given the post's own point about 10–20-trial evaluations.
- **The comparison with learning is anecdotal.** Low ACT and diffusion success is reported without numbers or data quantities.
- **Nothing is released yet.** A whitepaper and the DOPER and TALOS releases are announced as forthcoming.
- **One workcell.** Both tasks are specific to one product and partly adapted: the busbar clamp was modified so a single arm could unlatch it.

## The R²D² series

The Robotics Research and Development Digest is NVIDIA's developer-blog series summarising its robotics research. Ingested editions, oldest first:

1. [Mobility and whole-body control](nvidia-r2d2-mobility-whole-body-control-blog.md) (2025-03-27)
2. [Dexterous robots](nvidia-r2d2-dexterous-robots-blog.md) (2025-04-25)
3. [Robotic assembly](nvidia-r2d2-robotic-assembly-blog.md) (2025-05-16)
4. [3D perception and mapping](nvidia-r2d2-3d-perception-mapping-blog.md) (2025-06-17)
5. [Generalist robots and world foundation models](nvidia-r2d2-generalist-robots-wfm-blog.md) (2025-07-16)
6. [Cosmos workflows](nvidia-r2d2-cosmos-wfm-workflows-blog.md) (2025-08-08)
7. [Three neural methods from CoRL 2025](nvidia-r2d2-neural-robot-learning-blog.md) (2025-09-25)
8. [Perception-guided TAMP](nvidia-r2d2-perception-guided-tamp-blog.md) (2025-11-04)
9. [Manipulation with simulation and language models](nvidia-r2d2-manipulation-sim-language-blog.md) (2025-12-12)
10. [Isaac Lab](nvidia-r2d2-isaac-lab-multimodal-blog.md) (2026-02-10)
11. This post (2026-10-07), tagged with the series and pointing readers to it

Each post page also has an auto-generated summary labelled *"Powered by NVIDIA Nemotron."* The wiki pages are based on the authors' text, not those summaries.

## Entities mentioned

- [NVIDIA Seattle Robotics Lab](../entities/nvidia-seattle-robotics-lab.md), [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md), [cuRobo](../entities/curobo.md), [Model Hardware Standard](../entities/model-hardware-standard.md)

## Concepts touched

- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) — a classical-first case study with industrial targets.
- [Variational automation](../concepts/robotics/variational-automation.md) — low-volume, fast-changing products rule out fixed automation.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — the 598-trial bar.
- [Impedance control](../concepts/robotics/impedance-control.md) — the authors argue controller quality is underused in robot learning.
- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md) — a simulated base policy with a residual learned on the real robot.

## Open questions

- **How many trials are behind "above 95%" and "90–95%"?** The forthcoming whitepaper should say.
- **Does DOPER generalise beyond parts with CAD models?** It needs one per part, which suits this setting and few household ones.
- **What would close the connector cycle-time gap?** The bottleneck named is slow adjustment of connector poses before grasping.
