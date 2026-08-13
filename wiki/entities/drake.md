---
title: Drake
type: entity
subtype: software-framework
created: 2026-08-13
updated: 2026-08-13
sources: 2
tags: [drake, tri, mit-csail, russ-tedrake, simulation, model-based-design, optimization, multibody-dynamics, contact-simulation, lcm, bsd-3-clause, cpp]
---

**Drake** — a C++/Python toolbox for **model-based design and verification for robotics**, started by the Robot Locomotion Group at **MIT CSAIL** and with **core development now led by [TRI](tri.md)**. BSD-3-Clause. [drake.mit.edu](https://drake.mit.edu) · [RobotLocomotion/drake](https://github.com/RobotLocomotion/drake) — **4,148★ / 1,383 forks**, created January 2014, pushed daily as of 2026-08-13. Name is Middle English for "dragon." Primary source: [Drake documentation](../sources/drake-documentation.md).

## The design thesis

Drake's own framing is an argument against how most simulators are built:

> *"Most of them function like a black box: commands go in, sensors come out. Drake aims to simulate even very complex dynamics … but always with an emphasis on **exposing the structure in the governing equations** (sparsity, analytical gradients, polynomial structure, uncertainty quantification) and making this information available for advanced planning, control, and analysis algorithms."*

A learned policy treats a simulator as a **data source**. Drake treats it as a **mathematical object you can differentiate, optimize over, and prove things about**. That distinction is the whole page.

## What it provides

| Pillar | Contents |
|---|---|
| **Modeling Dynamical Systems** | Composable systems framework — blocks, ports, continuous/discrete state, simulation |
| **Solving Mathematical Programs** | Unified interface over LP / QP / SOCP / SDP / **SOS** / NLP / MIP solvers |
| **Multibody Kinematics and Dynamics** | Rigid-body kinematics, dynamics, and **contact** — the manipulation-facing part |

Contact is treated as an open research problem, not a solved detail (see the project's own *"Rethinking Contact Simulation for Robot Manipulation"*).

**Integrations:** Python, **LCM**, ROS 2 *(unsupported)*, Julia *(unsupported)*.

## Why it matters in this wiki

Drake was the wiki's **largest single content gap** — mentioned in 16 pages with no page of its own — because it sits underneath several things already covered:

- **[TRI](tri.md) / [Russ Tedrake](russ-tedrake.md)** — Tedrake is the named author of Drake's canonical citation *and* the architect of TRI's [Large Behavior Models](../concepts/learning/large-behavior-models.md) program.
- **[DimOS](dimos.md)** — uses Drake for arm motion planning ([xArm](xarm-7.md), [AgileX Piper](agilex-piper.md), dual-arm coordinator).
- **[UMI](umi.md)**, **[Diffusion Policy](diffusion-policy.md)**, **[Walden Robotics](walden-robotics.md)** — the TRI/Columbia/Stanford manipulation lineage that grew up around it.
- The **[simulators survey](../syntheses/simulators/simulators-for-agentic-robotics-2026.md)** listed "Drake internals" as an explicit coverage gap.

> [!note] The model-based ↔ learned bridge, in one artifact
> Drake's philosophy — expose sparsity, gradients, and polynomial structure so you can *optimize and verify* — is close to the opposite of an end-to-end behavior-cloned policy, where dynamics are implicit and unverifiable. And the same person is behind both: [Tedrake](russ-tedrake.md) authors Drake and leads TRI's LBM program.
>
> That Drake is **still developed daily at TRI while TRI ships LBMs** is evidence the lab treats these as complementary rather than successive. Worth holding whenever this wiki's coverage tilts toward "learned policies replaced model-based control" — the people best placed to make that claim are still funding the alternative.

> [!note] Drake is not competing with Isaac Lab, and placing it there misreads it
> The simulators survey files Drake in the "classical / control-rigorous" tier beside Gazebo, Webots, CoppeliaSim, and PyBullet, noting the agentic center of gravity has moved to [Isaac Lab](nvidia-isaac-lab.md) / [MuJoCo Playground](mujoco-playground.md) / [Genie Sim](agibot-genie-sim.md). Fair for *policy training at scale*, misleading for what Drake is for.
>
> Drake is not trying to generate a million trajectories. It is trying to let you **write down and solve a trajectory-optimization or verification problem**. [Newton](newton-physics-engine.md)'s convergence story — one pluggable engine under both Isaac Lab and MuJoCo Playground — does **not** absorb Drake, because Drake's value is the *math interface*, not the contact solver. Its real comparison set is MATLAB/Simulink, CasADi, and OCS2 — none of which this wiki covers.

> [!note] LCM native, ROS 2 unsupported — a lineage, not an oversight
> Drake ships **LCM** as a first-class integration and marks **ROS 2 unsupported**. [DimOS](dimos.md) independently defaults to LCM and treats ROS 2 as one transport among five. Two MIT-adjacent projects, same choice. There is a real sub-tradition in robotics middleware that this wiki had been describing as though [ROS 2](ros2.md) were the only incumbent.

## Teaching

The substrate under two MIT courses that function as the field's standard texts: **Underactuated Robotics** and **Robotic Manipulation: Perception, Planning, and Control**. Python/Jupyter tutorials install via pip.

## Related

- [TRI](tri.md) · [Russ Tedrake](russ-tedrake.md) · [Walden Robotics](walden-robotics.md)
- [DimOS](dimos.md) — downstream user for motion planning
- [MuJoCo](mujoco.md) · [Newton](newton-physics-engine.md) · [NVIDIA Isaac Sim](nvidia-isaac-sim.md) — usually listed beside it, solving a different problem
- [Optimal control](../concepts/robotics/optimal-control.md) · [Motion planning](../concepts/robotics/motion-planning.md) · [Formal verification](../concepts/learning/formal-verification.md)
- [Large behavior models](../concepts/learning/large-behavior-models.md) — the other half of Tedrake's bridge

## Mentioned in

- [Drake documentation](../sources/drake-documentation.md)
