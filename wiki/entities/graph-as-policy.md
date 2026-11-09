---
title: Graph-as-Policy (GaP)
type: entity
subtype: system
created: 2026-11-09
updated: 2026-11-09
sources: 2
tags: [graph-as-policy, gap, agentic-robotics, code-as-policy, variational-automation, multi-agent, uc-berkeley, nvidia]
---

**Graph-as-Policy (GaP)** — a multi-agent harness from UC Berkeley, NVIDIA and Bosch in which coding agents write a robot policy as a typed computation graph of skill nodes and improve it by rehearsing in simulation ([paper](../sources/gap-graph-as-policy-paper.md)). No agent is needed on the robot once the graph is deployed.

## How it works

Given a task description and object meshes, an orchestration agent splits the task and skill agents write sub-graphs from a 51-skill library, MORSL. The graph is type-checked and rehearsed in a simulator built directly from the meshes. Contact and state feedback localise failures to nodes, and agents edit the graph until it plateaus.

## Results

- 0.93–0.99 success in simulation under pose variation, where π0.5 and MolmoAct2 fall as low as 0.10–0.26.
- Real robot: groceries 25/25 and 28/30, popcorn 18/20, USB-C insertion 121/130.
- Crate washing in simulation: 0.953 vs 0.987 for an expert's hand-built graph.
- A first-graph cost of fewer than 30 LLM calls on Gemini-3.1-Flash-Lite.

The comparison has limits, recorded on the [source page](../sources/gap-graph-as-policy-paper.md): GaP is given geometry the VLAs aren't, and no VLA ran on the real robot.

## Why it matters in this wiki

GaP is a more structured entry in the [code-as-policy](../concepts/agents/code-as-policy.md) line, and it continues the [CaP-X](cap-x.md) and [ASPIRE](aspire.md) work from the same collaborators. Unlike those, it restricts the agent to wiring typed skills. It defines a target, [variational automation](../concepts/robotics/variational-automation.md), that doesn't require generality.

Its staging result is a useful hybrid: moving the wrist camera above the object with a graph, then handing off to a VLA, more than doubles VLA success.

## Related

- [Ken Goldberg](ken-goldberg.md) · [NVIDIA GEAR](nvidia-gear.md) · [CaP-X](cap-x.md) · [ASPIRE](aspire.md)
- [Code as policy](../concepts/agents/code-as-policy.md) · [Variational automation](../concepts/robotics/variational-automation.md)

## Mentioned in

- [GaP paper](../sources/gap-graph-as-policy-paper.md)
- [NVIDIA at CoRL 2026](../sources/nvidia-corl-2026-robotics-simulation-blog.md)
