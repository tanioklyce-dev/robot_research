---
title: Drake — official documentation and repository (drake.mit.edu / RobotLocomotion/drake)
type: source
url: https://drake.mit.edu/
author: Russ Tedrake and the Drake Development Team — Robot Locomotion Group (MIT CSAIL), core development led by Toyota Research Institute
published: 2014-01-26 (repo created; continuously developed — last push 2026-08-13)
ingested: 2026-08-13
license: BSD-3-Clause (Copyright 2012–2025 Robot Locomotion Group @ CSAIL)
tags: [drake, tri, mit-csail, russ-tedrake, simulation, model-based-design, optimization, multibody-dynamics, contact-simulation, lcm, cpp, primary-source]
---

## Summary

**Drake** ("dragon" in Middle English) is a C++/Python toolbox for **model-based design and verification for robotics** — started by the Robot Locomotion Group at MIT CSAIL, with **core development now led by [TRI](../entities/tri.md)**. BSD-3-Clause. **4,148★ / 1,383 forks**, created January 2014, **still pushed daily** as of ingest — twelve years of continuous development, which makes it one of the oldest actively-maintained artifacts in this wiki.

Ingested because it was the wiki's **largest content gap**: mentioned in 16 pages with no page of its own, including [Russ Tedrake](../entities/russ-tedrake.md), [TRI](../entities/tri.md), [UMI](../entities/umi.md), [xArm 7](../entities/xarm-7.md), and [DimOS](../entities/dimos.md)'s manipulation stack. The [simulators survey](../syntheses/simulators/simulators-for-agentic-robotics-2026.md) explicitly listed "Drake internals" as a coverage gap.

## The thesis: expose the structure, don't hide it

Drake's self-description is a direct argument against how most simulators are built, and it is the most quotable thing on the site:

> *"While there are an increasing number of simulation tools available for robotics, most of them function like a black box: commands go in, sensors come out. Drake aims to simulate even very complex dynamics of robots (e.g. including friction, contact, aerodynamics, …), but always with an emphasis on **exposing the structure in the governing equations** (sparsity, analytical gradients, polynomial structure, uncertainty quantification, …) and making this information available for advanced planning, control, and analysis algorithms."*

That is the whole design philosophy. A learned policy treats the simulator as a data source; Drake treats it as a **mathematical object you can differentiate, optimize over, and prove things about**. The emphasis on *analytical gradients* and *polynomial structure* is what makes trajectory optimization, sums-of-squares verification, and contact-implicit planning tractable inside it.

## Key claims

### Three core pillars (the documentation's own top-level organization)

| Pillar | What it provides |
|---|---|
| **Modeling Dynamical Systems** | A systems framework — composable blocks with continuous/discrete state, ports, and simulation. |
| **Solving Mathematical Programs** | A unified interface over convex and nonconvex solvers (LP/QP/SOCP/SDP/SOS/NLP/MIP). |
| **Multibody Kinematics and Dynamics** | Rigid-body kinematics, dynamics, and **contact** — the part the manipulation world uses. |

Contact simulation is treated as a research subject rather than a solved detail; the site's own reading list includes **"Rethinking Contact Simulation for Robot Manipulation."**

### Provenance and scale

- **Origin**: Robot Locomotion Group, MIT CSAIL. **Core development led by [TRI](../entities/tri.md)** today.
- **Canonical citation**: *"Russ Tedrake and the Drake Development Team, Drake: Model-based design and verification for robotics, 2019."*
- **Languages** (by bytes): C++ 40.7 MB, Python 2.8 MB, **Starlark 1.6 MB** (it builds with Bazel), Jupyter 524 KB.
- **Funding acknowledged**: TRI, DARPA, NSF, ONR, Amazon, MathWorks.
- **649 open issues** against 4,148 stars — a normal ratio for a twelve-year-old C++ library, and far healthier than [DimOS](../entities/dimos.md)'s 16%.

### Integrations — and one conspicuous status

Listed on the homepage: **Python**, **LCM**, **ROS 2 (unsupported)**, **Julia (unsupported)**.

### Teaching artifacts

Drake is the substrate under two well-known MIT courses, both listed as primary reading: **Underactuated Robotics** (walking, running, swimming, flying, manipulation) and **Robotic Manipulation: Perception, Planning, and Control**. Python/Jupyter tutorials are browsable online and installable via pip.

## Analysis

> [!note] ROS 2 is "unsupported" — and LCM is not
> The integration list quietly states a lineage. **LCM** (Lightweight Communications and Marshalling) is a first-class Drake integration; **ROS 2 is marked unsupported**, alongside Julia. For a toolbox this central to robotics research that is a striking position, and it is not an oversight — LCM came out of the same MIT DARPA-Robotics-Challenge lineage as Drake.
>
> The wiki has now met that lineage twice in one week from opposite directions: **[DimOS](../entities/dimos.md) also defaults to LCM** and treats ROS 2 as one interchangeable transport among five. Two independent projects, both MIT-adjacent, both choosing LCM as the native path and ROS 2 as optional. That is a real sub-tradition inside robotics middleware that this wiki had been describing as if ROS 2 were the only incumbent — see [ROS 2](../entities/ros2.md).

> [!note] The same person built the model-based stack and one of the leading learned-policy programs
> [Russ Tedrake](../entities/russ-tedrake.md) is the named author of Drake's citation *and* the architect of [TRI](../entities/tri.md)'s [Large Behavior Models](../concepts/learning/large-behavior-models.md) program. Drake's philosophy — expose sparsity, gradients, and polynomial structure so you can *optimize and verify* — is close to the opposite of an end-to-end behavior-cloned policy, where the dynamics are implicit and unverifiable.
>
> The wiki's [Tedrake page](../entities/russ-tedrake.md) already calls him "one of the field's rare model-based-control ↔ learning bridges." Drake is the concrete artifact on the model-based side of that bridge, and its continued daily development at TRI *while* TRI ships LBMs is evidence that the lab treats these as complementary rather than as a succession. Worth holding onto whenever this wiki's coverage tilts toward "learned policies replaced model-based control" — the people best placed to make that claim are still funding the alternative.

> [!warning] Where Drake sits among this wiki's simulators, and where it does not
> The [simulators survey](../syntheses/simulators/simulators-for-agentic-robotics-2026.md) files Drake in its "classical / control-rigorous" category alongside Gazebo, Webots, CoppeliaSim, and PyBullet, noting the agentic-robotics center of gravity has moved elsewhere ([Isaac Lab](../entities/nvidia-isaac-lab.md), [MuJoCo Playground](../entities/mujoco-playground.md), [Genie Sim](../entities/agibot-genie-sim.md)). That placement is fair for *policy training at scale* and misleading for what Drake is for.
>
> Drake is not competing to generate a million trajectories. It is competing to let you **write down and solve a trajectory-optimization or verification problem**. [Newton](../entities/newton-physics-engine.md)'s convergence story — one pluggable physics engine under Isaac Lab and MuJoCo Playground — does not absorb Drake, because Drake's value is the *math interface*, not the contact solver. Its natural comparison set is MATLAB/Simulink, CasADi, and OCS2, none of which this wiki covers.

## Entities mentioned

- [Drake](../entities/drake.md) · [TRI](../entities/tri.md) · [Russ Tedrake](../entities/russ-tedrake.md)
- [DimOS](../entities/dimos.md) — uses Drake for arm motion planning · [xArm 7](../entities/xarm-7.md) · [AgileX Piper](../entities/agilex-piper.md)
- [UMI](../entities/umi.md) · [Diffusion Policy](../entities/diffusion-policy.md) · [Walden Robotics](../entities/walden-robotics.md)
- [MuJoCo](../entities/mujoco.md) · [Newton](../entities/newton-physics-engine.md) · [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) — the simulators it is usually listed beside
- [ROS 2](../entities/ros2.md) — marked "unsupported" here

## Concepts touched

- [Optimal control](../concepts/robotics/optimal-control.md) · [Motion planning](../concepts/robotics/motion-planning.md) · [Task and motion planning](../concepts/robotics/task-and-motion-planning.md)
- [Large behavior models](../concepts/learning/large-behavior-models.md) · [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) · [Formal verification](../concepts/learning/formal-verification.md)

## Open questions

- **How much of TRI's LBM pipeline actually runs on Drake?** The [LBM paper](tri-lbm-paper.md) is a learned-policy result; whether Drake supplies its simulation, its evaluation harness, or neither is undocumented here. This is the single most useful thing to establish next.
- **Why is ROS 2 unsupported, in 2026?** Deliberate scoping, maintenance cost, or a technical mismatch with Drake's systems framework? The docs state the status without the reason.
- **Is Drake differentiable end-to-end?** The site emphasizes "analytical gradients," but how far that extends *through contact* — the hard case, and the subject of its own "Rethinking Contact Simulation" reading — is not established from the homepage.
- **No benchmark numbers of any kind** were read here. Drake's contact solver has published comparisons against MuJoCo and PhysX in the literature; none are ingested.
- The **Drake Gallery** and the two MIT courses are substantial secondary sources that would repay separate ingests.
