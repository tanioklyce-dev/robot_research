---
title: NVIDIA Seattle Robotics Lab (SRL)
type: entity
subtype: lab
created: 2026-11-10
updated: 2026-11-10
sources: 3
tags: [nvidia, nvidia-srl, nvidia-research, manipulation, assembly, evaluation]
---

**NVIDIA Seattle Robotics Lab (SRL)** — NVIDIA Research's robotics lab in Seattle. The name and abbreviation are confirmed in its [GB300 assembly post](../sources/nvidia-r2d2-gb300-tester-tray-assembly-blog.md), which describes nine years of work.

## Work in this wiki

- **GB300 tester-tray assembly (2026).** A classical-first system with the Isaac engineering team, built to targets set with NVIDIA Operations and Foxconn: 99.5% success at twice a skilled worker's time. Reported results are above 95% for the busbar task and 90–95% for connectors, with both still short of target ([post](../sources/nvidia-r2d2-gb300-tester-tray-assembly-blog.md)).
- **Tools announced for release.** DOPER, a per-part pose estimator trained from CAD renders and fine-tuned on reconstructions. TALOS, an orchestration layer on ros2_control that agents can reach through web interfaces. The open DROID+ project.
- **Astranomy (2026-10).** GPT-6 Astra as a zero-shot policy on RoboLab-120, at 66–75% depending on its role, with ablations of prompt, history, tools and model ([post](../sources/nvidia-srl-astranomy-blog.md)).
- **[RoboLab](nvidia-robolab.md)**, a simulation benchmark for generalist policies ([evaluation post](../sources/nvidia-robolab-evaluation-blog.md)).
- **Sim-to-real assembly line.** The GB300 post cites the group's own sim-to-real series, which matches the Factory, IndustReal, AutoMate, TacSL and FORGE work summarised in the [assembly digest](../sources/nvidia-r2d2-robotic-assembly-blog.md). That digest doesn't name the lab, so the attribution rests on the shared authors and citations.

## Why it matters in this wiki

SRL's GB300 post is one of the few industrial case studies here that reports against a customer's targets and states the trial count needed to verify them. It argues for classical methods, mechanical design and controller quality where data can't be scaled, which it calls the "inverse bitter lesson."

## Related

- [NVIDIA](nvidia.md) · [NVIDIA GEAR](nvidia-gear.md) · [RoboLab](nvidia-robolab.md) · [cuRobo](curobo.md)
- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) · [Variational automation](../concepts/robotics/variational-automation.md)

## Mentioned in

- [NVIDIA — The Machines that Make the Machines (GB300)](../sources/nvidia-r2d2-gb300-tester-tray-assembly-blog.md)
- [RoboLab evaluation blog](../sources/nvidia-robolab-evaluation-blog.md)
- [Astranomy (NVIDIA SRL)](../sources/nvidia-srl-astranomy-blog.md) — the GPT-6 Astra policy study.
