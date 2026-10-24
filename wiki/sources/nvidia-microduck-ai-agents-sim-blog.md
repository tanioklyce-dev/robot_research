---
title: "Using AI Agents to Teach Robots Like Microduck to Walk in Simulation (NVIDIA Technical Blog)"
type: source
url: https://developer.nvidia.com/blog/using-ai-agents-to-teach-robots-like-microduck-to-walk-in-simulation/
local_path: raw/2026-10-23-nvidia-microduck-ai-agents-blog.txt
sha256: 26c49ce1a8112966d0ff59b43d915f50d3563e061a415935b0b63da98aba09b9
author: Gabriele Leone, Seun Doherty, Asier Arranz, Johnny Núñez, Asawaree Bhide (NVIDIA)
published: 2026-10-23
ingested: 2026-10-24
venue: NVIDIA Technical Blog (Robotics; tagged "Tutorial", "Intermediate Technical")
format: "vendor tutorial blog (~1,900 words body), 10 figures not captured; article-body text extracted from HTML"
tags: [nvidia, microduck, isaac-lab, isaac-sim, newton, mjwarp, bam, actuator-model, domain-randomization, sim-to-real, agentic-simulation, hermes-agent, nemotron, astra, rtx-spark, simready, freecad, blender, openusd, asset-generation, locomotion, perception, vendor-source]
---

# Using AI Agents to Teach Robots Like Microduck to Walk in Simulation (NVIDIA, 2026-10-23)

## Summary

NVIDIA's tutorial runs the whole prompt-to-policy loop on [Pollen Robotics](../entities/pollen-robotics.md)' [Microduck](../entities/microduck.md). An obstacle-course prompt goes in; a perception-and-locomotion policy that has been validated in simulation comes out. Agents do the front half:
- [Hermes Agent](../entities/hermes-agent.md) running **Nemotron 3.5 Bolt** ([Nemotron](../entities/nemotron.md)) plans locally on an **[RTX Spark](../entities/nvidia-rtx-spark.md)** PC.
- **Astra** builds the 3D assets, driving cloud image editing, FreeCAD and Blender, and exports to USD. It also assembles the course in [Isaac Sim](../entities/nvidia-isaac-sim.md).

Training is conventional: [Isaac Lab](../entities/nvidia-isaac-lab.md) on [Newton](../entities/newton-physics-engine.md), **4,096 parallel environments on one RTX PRO 6000 Blackwell**, fine-tuning a pretrained walker to traverse ramps using **head-camera depth plus robot state**. Validation runs back on the Spark.

The post's real news is in two links rather than its prose. **Isaac Lab now ships a Microduck task and a native port of Rhoban's BAM servo model**; both landed upstream on 2026-10-15. That makes Isaac Lab the second public training stack for Microduck, next to Pollen's own [mjlab](../entities/mjlab.md) recipe. The final figure shows a physical Microduck walking with an Isaac-Lab-trained policy, but hardware deployment is declared out of scope.

## Key claims

### The workflow (six stages)
1. **Plan (local, RTX Spark).** Hermes + *"NVIDIA Nemotron 3.5 Bolt"* turn a structured prompt into a project plan. The linked checkpoint is `nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB`, so 74B total / 9B active, sized for 24 GB. The plan reviews the [Microduck repo](microduck-runtime-repo.md) to list *"capabilities, constraints, and unknowns"*.
   - A **local image-generation model** renders a concept image of the course.
   - Hermes/Nemotron then inventory its *"visible, reusable assets"*. Each asset gets an ID, a description, a crop, and a note on where it is *"cut off or obscured so that later stages can distinguish visible details from assumptions."*
   - Hermes packages a handoff and *"automatically delegates the work to Astra."*
2. **Assets (Astra).**
   - Cloud image editing upscales and isolates the crops, then checks them against the originals for silhouette, proportion and colour.
   - **FreeCAD** builds base geometry and an editable CAD structure; **Blender** adds detail and materials. *"Both applications run locally through programmatic execution."*
   - Output is editable models plus exported USD. Unknown dimensions and hidden surfaces are *"recorded as modeling assumptions."*
   - Alternative or complement: the **SimReady Central Library**, *"free and ungated … more than 2,000 simulation-ready OpenUSD assets."*
3. **Assemble (Astra in Isaac Sim).** Omniverse libraries do rendering and sensor simulation; Newton models *"movement and balance."* *"AI agents can help configure"* links, joints and actuators. How much they did here is not said.
4. **Train (Isaac Lab, cloud).**
   - Starts from *"the Isaac Lab Microduck example environment"* with *"a locomotion policy pretrained in that environment"*.
   - Fine-tunes it for curved ramps and uneven surfaces with **head-camera depth and robot-state observations**.
   - *"This adaptation run used 4,096 parallel environments on an NVIDIA RTX PRO 6000 Blackwell Workstation Edition GPU."*
   - No wall-clock time, reward, success rate or step count is given.
5. **Validate (Isaac Sim, local RTX Spark).** Record *"course completion, falls, collisions, and the situations in which progress stops,"* paired with rollout videos. No numbers are reported.
6. **Prepare for real.**
   - **Better Actuator Models (BAM)** in Isaac Lab model *"command delays, mechanical backlash … and drops in voltage as motors draw power from a shared battery."*
   - Isaac Lab domain randomization varies physical parameters and observation noise.
   - *"Detailed hardware deployment is outside the scope."* Figure 10 nonetheless shows *"Physical Microduck walking with a locomotion policy trained in Isaac Lab"*. It is a walking policy, not the obstacle-course policy.

### Platform details stated in passing
- Isaac Sim on RTX Spark means installing the **Windows x86 binaries**, which run *"out of the box via Windows x86 emulation on Arm."* So there is no native Arm Isaac Sim build for this platform.
- Training runs *"in the cloud"* while planning and validation stay local. The split is local Spark ↔ cloud RTX PRO 6000.
- The links point at the Isaac Lab **`v3.0.0-EA`** docs, two days after the GTC Berlin release declared [Isaac Lab 3.0 GA](nvidia-isaac-platform-gtc-berlin-2026.md). The same stale-link pattern was noted there.

### Verified against the primary (2026-10-24)
The blog's environment link points at the `develop` branch, which **redirects to `main`**. There, `isaaclab_tasks/contrib/microduck/` contains `flat_env_cfg.py`, `rough_env_cfg.py`, `mdp/` and `agents/`. It was introduced by PR **#8270, *"[Newton] Add BAM servo actuator and MicroDuck walking tasks"***, authored by Antoine Richard (named in the post's acknowledgements) on **2026-10-15**. The [actuator docs](https://isaac-sim.github.io/IsaacLab/develop/source/concepts/actuators.html#bam-servo-model) say:

- `BamActuatorCfg` *"ports BAM (Better Actuator Models), whose parameters are identified from bench measurements."*
- **It requires Newton with `MJWarpSolverCfg` and `use_newton_actuators=True`.** *"Other backends and solvers raise an error."* PhysX cannot run it.
- Per physics step, as Warp kernels:
  - a randomly resampled command lag (one per env, shared across joints);
  - supply sag proportional to the summed joint torque, `vin_eff = max(vin − sag_gain·Σ|τ|, vin_min, 0)`;
  - firmware P-law → duty, clipped by the current limiter;
  - DC-motor torque with back-EMF as the damping;
  - BAM friction models **m1/m2/m5/m6** (Coulomb → Stribeck → directional load dependence → quadratic load coupling), applied as an MJWarp friction constraint via `dof_frictionloss`.
- **Backlash**: `backlash_joint_template` (e.g. `"passive_{}_backlash"`) names a passive revolute hinge in series with each servo. *"The firmware then reads servo angle plus play angle."* This is exactly the output-side-encoder construction in Pollen's [`microduck_rl`](pollen-robotics-microduck.md), now a first-class Isaac Lab feature.
- Per-robot `vin_range` and `vin_drop_gain_range` are the randomization hooks for battery voltage and sag.

## Entities mentioned
- [Microduck](../entities/microduck.md), [Pollen Robotics](../entities/pollen-robotics.md)
- [NVIDIA](../entities/nvidia.md): [Isaac Lab](../entities/nvidia-isaac-lab.md), [Isaac Sim](../entities/nvidia-isaac-sim.md), [Newton](../entities/newton-physics-engine.md), [Nemotron](../entities/nemotron.md), [RTX Spark](../entities/nvidia-rtx-spark.md), Omniverse, SimReady
- [Hermes Agent](../entities/hermes-agent.md) (Nous Research)
- **Astra**: an asset/simulation agent, not defined in the post. See the open questions.
- [Rhoban](../entities/rhoban.md), the origin of BAM (implicitly)
- [MuJoCo Warp](../entities/mujoco-warp.md), the solver BAM requires inside Newton
- [mjlab](../entities/mjlab.md), Pollen's own training stack, which this post does not mention

## Concepts touched
- [Actuator fidelity in sim-to-real](../concepts/learning/actuator-fidelity-sim2real.md): BAM becomes a stock Isaac Lab actuator.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md): domain randomization plus actuator modelling.
- [Simulators for agentic robotics](../syntheses/simulators/simulators-for-agentic-robotics-2026.md): LLM agents authoring the environment, not just the policy.

## Open questions
- **What is "Astra"?** The post never expands it. The GTC Berlin release, two days earlier, described *"reference workflows that combine **ChatGPT Astra** with NVIDIA Isaac and Cosmos"* ([release](nvidia-isaac-platform-gtc-berlin-2026.md)), and an OpenAI *"GPT-Astra"* appears in [Jalapeño](openai-jalapeno-first-results.md). The same OpenAI agent product is the most likely reading, but **neither NVIDIA source says so**. The role here is consistent with that reading: *cloud* image editing plus local tool orchestration.
- **Does the obstacle-course policy transfer?** Only a plain walking policy is shown on hardware. The depth-conditioned ramp policy has no reported real-world run. Microduck's depth sensor is an [8×8 ToF matrix](../entities/microduck.md), and its camera has no IPC path yet in the runtime. Which "head-camera depth" the sim policy consumes is unstated: a rendered depth image, or a 64-zone ToF emulation. That decides whether the policy could ever run on the robot.
- **Isaac Lab BAM vs mjlab BAM.** Do they yield interchangeable policies (same `obs[1,61] → actions[1,14]` contract)? Isaac Lab's port runs on the same MJWarp solver, so physics parity is plausible but untested.
- The companion **Hugging Face tutorial**, *"Microduck sim-to-real"* (`huggingface.co/blog/nvidia/microduck-isaac-lab-sim-to-real`), carries the deployment half. **Not yet ingested.**
- No training time, reward design, success rate or agent-cost figures are given. The value of the agentic front half is asserted, not measured.
