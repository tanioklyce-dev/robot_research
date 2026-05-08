---
title: FRC simulation & AI landscape
type: synthesis
created: 2026-05-08
updated: 2026-05-08
tags: [frc, simulation, ai, machine-learning, autonomous, pathplanning]
---

# FRC simulation & AI landscape

What simulation programs [[first-robotics-competition|FRC]] teams use for autonomous development and AI training, as of the 2026 REBUILT season. The landscape is stratified: most teams use trajectory-planning tools (no ML), a growing minority use physics simulators, and AI/ML remains a frontier pursued by elite teams.

## Tier 1: Trajectory planners (mainstream)

The vast majority of FRC teams develop autonomous routines by drawing paths in a GUI and having the robot follow pre-computed trajectories. No simulation physics or ML involved — the robot executes a deterministic plan.

| Tool | Approach | Status (2026) |
|------|----------|---------------|
| **[PathPlanner](https://github.com/mjansen4857/pathplanner)** | Bezier-curve paths in GUI → WPILib trajectory following. Events at waypoints. | Dominant tool. Swerve + holonomic support. |
| **[Choreo](https://choreo.autos/)** | Optimization-based: feed robot characteristics + constraints → mathematically optimal trajectory. | Rising. WPILib-endorsed. Replaces deprecated PathWeaver. |
| **WPILib PathWeaver** | Legacy trajectory tool. | Deprecated, removed in 2027. |

These tools produce **open-loop** trajectories. The robot uses odometry + [[apriltags|AprilTag]] pose estimation (via PhotonVision or Limelight) to correct drift, but the path itself is pre-planned, not learned.

## Tier 2: Physics simulators (growing adoption)

These tools simulate robot-field interactions with actual physics, enabling closed-loop testing of autonomous code without a physical robot.

### WPILib built-in simulation
- **HALSIM**: WPILib's Hardware Abstraction Layer Simulation. Lets robot code run on a desktop with simulated motors, encoders, gyros, and sensors.
- Physics models for drivetrains (differential, swerve), elevators, arms, flywheels.
- Dashboard tools (AdvantageScope, Glass, Shuffleboard) connect to `localhost` for visualization.
- Standard 20ms loop. No field-element collision physics.

### [Maple-Sim](https://github.com/Shenzhen-Robotics-Alliance/Maple-Sim) (Shenzhen Robotics Alliance)
- **Java library integrating the dyn4j 2D rigid-body dynamics engine** into WPILib's simulation framework.
- Simulates robot-obstacle, robot-game-piece, and robot-robot collisions. "Realistic enough to feel like a video game."
- Supports swerve drivetrains, intake systems, projectile mechanics, opponent robots.
- Integrates with CTRE Phoenix 6, YAGSL, AdvantageKit.
- Updated for REBUILT 2026 (WPILib 2026.2.1). **111 stars, 65 forks, 635 commits** — most active FRC physics sim.

### [FuelSim](https://github.com/hammerheads5000/FuelSim) (Team 5000 Hammerheads)
- Single-file Java library for REBUILT FUEL physics: fuel-fuel, fuel-field, fuel-net, fuel-trench, fuel-robot collisions + projectile motion + air drag.
- Logs fuel positions to NetworkTables as Translation3d arrays; works with AdvantageKit.
- Designed to complement Maple-Sim or standalone WPILib sim.

### [xRC Simulator](https://xrcsimulator.org/)
- Standalone 3D robot simulator (Unity-based). Multi-platform (Windows, Mac, Linux, headless server).
- Multiple robot models; 2026 KitBot added. Adjustable physics engine speeds.
- Used for driver practice and strategy testing, not code-in-the-loop simulation.
- Not integrated with WPILib — separate from the team's robot code.

### [frc2026sim.com](https://www.frc2026sim.com/)
- Web-based **match strategy simulator** for REBUILT. Not a physics sim — a scoring model.
- Configure robot roles (cycler, passer, shooter, stealer), intake/shooting rates, cycle times.
- Outputs fuel scored, cycles, window efficiency, expected points.
- Used for alliance strategy optimization before matches.

### Legacy/archived
- **FRCSim (Gazebo)**: WPI built an FRC-specific simulation on Gazebo ~2015–2016. Gazebo was included in the Kit of Parts. Now largely abandoned in favor of WPILib's built-in sim + Maple-Sim.
- **Unity-based FRC sims**: Several community projects ([FRC_Unity_Robot_Simulation](https://github.com/FaceInCake/FRC_Unity_Robot_Simulation), [FRC-2021-Starter-Project](https://github.com/kinahawi/FRC-2021-Starter-Project)). Allowed running Java robot code in a 3D Unity environment. Archived.
- **Unreal Engine VR sim** (2018): VR simulation of the Power Up game field. One-off project.

## Tier 3: AI / Machine Learning (frontier)

AI/ML in FRC is **emerging but not mainstream**. The landmark event was Team 254's (The Cheesy Poofs) 2026 Championship Conference presentation: **"The Next Revolution: AI in FRC."**

### [[team-254|Team 254]]'s presentation (April 2026) — [[team-254-ai-in-frc-presentation|full source page]]
- Presenters: Jared Russell, Tom Bottiglieri, and others from 254. [YouTube recording](https://www.youtube.com/watch?v=oTcimMwxRoM).
- Topics covered:
  1. **AI-assisted development ("vibe-coding")**: Using LLM coding agents (specifically **Claude Code**) as a core FRC dev workflow. Agent reads existing source + WPILib APIs, generates code, validates through compilation/tests, iterates.
  2. **AI-based computer vision**: Demystifying CV applications in FRC (YOLO on Jetson, RoboFlow annotation).
  3. **AI-augmented scouting**: Gemini for processing qualitative scouter comments → team profiles; Gemini video API at 1fps on match footage; Claude for picklist generation.
  4. **Closed-loop AI agent systems**: LLM agents that run simulations, read logs, SSH/deploy code to robots, and convert natural language requests (e.g., "extend the simulation to handle driving over the bump") into verified simulation code.
  5. **ClaudeScope**: Described as combining "SKILLS and a CLI" enabling "LLMs to interact with robots."
  6. **Power/performance analysis**: AI-written Python scripts for post-match power consumption → optimize load shedding, current limits, mechanism gearing. One team reported GPT 5.4 reduced p50 loop time from ~25ms to ~7ms fully closed-loop.
- Community reception was mixed: enthusiasm about practical AI applications vs. concerns about student learning outcomes, equity, age restrictions (Claude Code requires 18+), and environmental impact.

### wpilib-agent-tools ([GitHub](https://github.com/edanliahovetsky/wpilib-agent-tools))
- Experimental Python CLI enabling AI agents to interact with WPILib simulation in an evidence-driven loop.
- Workflow: create isolated sandbox → run WPILib sim → record NT4 output → analyze `.wpilog` (derivatives, integrals, statistics, settling metrics, matplotlib graphing) → review patch before applying.
- Supports Codex, Claude Code, and Cursor as agent platforms.
- Integrates with AdvantageKit-style robot repos, auto-converts to sim mode.
- Agent tasks: diagnose superstructure behavior, find root causes in autonomous routines, validate subsystem setpoint compliance across match logs.
- Acknowledged as experimental; all outputs require normal engineering review.

### FIRST Agentic CSA (FRC AI Coding Enhancer v2)
- MCP server designed to address WPILib API naming changes (e.g., `ChassisSpeeds` → `ChassisVelocities` in 2027).
- Keeps LLM agents current with latest WPILib documentation.

### Current AI/ML usage across FRC teams

| Application | Maturity | Tools |
|-------------|----------|-------|
| **Object detection** (game pieces) | Established | YOLOv5/v8 on Jetson Nano/Orin; RoboFlow for annotation; PhotonVision |
| **AprilTag localization** | Mainstream | PhotonVision, Limelight — not ML per se but vision-based |
| **LLM code assistance** | Growing rapidly | Claude, ChatGPT, Copilot for writing/debugging robot code |
| **Scouting analytics** | Experimental | LLM-based analysis of match data; proposed but few concrete deployments |
| **Reinforcement learning** | Proof-of-concept only | A few CD threads show RL for simple tasks (crossing auto line); no competition-winning RL deployments |
| **Full autonomous via ML** | Not practical yet | Human drivers still outperform ML in dynamic 3v3 match scenarios |

### Chief Delphi threads on AI/ML
- [Machine Learning for Autonomous Robot Actions](https://www.chiefdelphi.com/t/machine-learning-for-autonomous-robot-actions/145047) — early discussion; TensorFlow mentioned.
- [Deep Reinforcement Learning for FRC Proof of Concept](https://www.chiefdelphi.com/t/deep-reinforcement-learning-for-frc-proof-of-concept/164919) — RL to cross autonomous line.
- [Will We See Full Auto Robot With ML that Replaces Human Driver in Tele?](https://www.chiefdelphi.com/t/will-we-see-full-auto-robot-with-ml-that-replaces-human-driver-in-tele/404105) — consensus: not yet.
- [AI for FRC](https://www.chiefdelphi.com/t/ai-for-frc/363862), [FRC Machine Learning 2024](https://www.chiefdelphi.com/t/frc-machine-learning-2024/443325), [How much AI can and is being used in FRC?](https://www.chiefdelphi.com/t/how-much-ai-can-and-is-being-used-in-frc/483243) — survey threads.

### MathWorks / MATLAB & Simulink
- MathWorks sponsors FRC and provides free software + training for teams.
- MATLAB/Simulink supports "model-based design" of autonomous algorithms — state machines, PID tuning, trajectory optimization.
- Not ML in the deep-learning sense, but the closest FIRST-endorsed "simulation + design" tool.

## Gap analysis: FRC vs. research robotics simulation

| Dimension | FRC ecosystem | Research robotics |
|-----------|---------------|-------------------|
| **Physics fidelity** | 2D rigid-body (dyn4j in Maple-Sim) | Full 3D (MuJoCo, Isaac Sim, Newton) |
| **Rendering** | AdvantageScope 3D viz (no photorealism) | Photorealistic (Isaac Sim, Habitat) |
| **Policy learning** | Hand-coded trajectories; RL is proof-of-concept | RL, IL, VLA, JEPA — core workflow |
| **Sim-to-real gap** | Mitigated by AprilTag localization, not learned | Domain randomization, visual pretraining |
| **Cycle time** | 20ms (roboRIO FPGA) | 10–100ms typical |
| **Open-source tools** | WPILib, Maple-Sim, FuelSim, PathPlanner, Choreo | Gymnasium, MuJoCo, Isaac Lab, RoboCasa |
| **Co-processors for ML** | Jetson Nano/Orin, Raspberry Pi, Orange Pi | Same + high-end GPU clusters for training |

## Key takeaways

1. **FRC simulation is dominated by trajectory planners, not learned policies.** PathPlanner and Choreo are the workhorses; they produce deterministic trajectories, not learned behaviors.
2. **Maple-Sim is the closest thing to a "real physics simulator" for FRC**, and it's growing fast. Its 2D rigid-body approach is lightweight but enough for FRC's planar gameplay.
3. **AI in FRC is primarily vision (object detection + AprilTag localization) and LLM-assisted coding**, not policy learning. Team 254's 2026 presentation signals that LLM agents interacting with simulation code is the next frontier.
4. **No FRC team has won a competition using RL-trained autonomous policies.** The community consensus is that hand-tuned trajectories + AprilTag correction are still more reliable than learned policies for the 2:40 match format.
5. **The FRC simulation ecosystem is entirely separate from the research-robotics stack** (no MuJoCo, no Isaac Sim, no Gymnasium). WPILib's HALSIM + Maple-Sim + FuelSim is the FRC-specific equivalent.
6. **Bridge opportunity**: Maple-Sim's Java/dyn4j architecture could theoretically be wrapped with a Gymnasium-compatible Python API for RL training, but nobody has done this yet.
