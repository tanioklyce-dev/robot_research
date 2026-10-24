---
title: "Train in Simulation, Deploy on a Real Robot: Microduck with Isaac Lab 3.0 (NVIDIA on Hugging Face)"
type: source
url: https://huggingface.co/blog/nvidia/microduck-isaac-lab-sim-to-real
local_path: raw/2026-10-21-hf-nvidia-microduck-isaac-lab-sim-to-real.txt
sha256: 873faa38dbb0bca8e1337279b5c9523bffc6849be383e1379fd4c1ff01b81f02
author: Oluwaseun Doherty, Oyindamola Omotuyi, Antoine Richard, Asier Arranz (NVIDIA); written with Antoine Pirrone, Augustin Crampette, Matthieu Lapeyre, Coralie Deplanne, Anne-Charlotte Passanisi (Pollen Robotics) and Thomas Wolf (Hugging Face)
published: 2026-10-21
ingested: 2026-10-24
venue: Hugging Face blog (NVIDIA org, "Community Article")
format: "hands-on tutorial (~1,500 words body) with shell commands, 8 figures/GIFs not captured; body text extracted from HTML"
tags: [microduck, isaac-lab, isaac-lab-3, newton, mjwarp, bam, backlash, domain-randomization, sim-to-real, onnx, rsl-rl, locomotion, microduck-arena, hugging-face, pollen-robotics, nvidia, tutorial, vendor-source]
---

# Train in Simulation, Deploy on a Real Robot: Microduck with Isaac Lab 3.0 (2026-10-21)

## Summary

This is the hands-on half of NVIDIA's Microduck push, published on GTC Berlin day. The [agentic tutorial](nvidia-microduck-ai-agents-sim-blog.md) two days later is the showcase; this post gives the commands to:
- train a [Microduck](../entities/microduck.md) walking policy in [Isaac Lab](../entities/nvidia-isaac-lab.md) on [Newton](../entities/newton-physics-engine.md)'s MJWarp solver, with the native BAM servo model and a backlash preset;
- export it to ONNX;
- `scp` it onto the robot and hot-load it with `robotctl`;
- or race it in **[Microduck Arena](../entities/microduck-arena.md)**, Pollen's server-side policy leaderboard on Hugging Face.

It answers the two questions the agentic post left open:
1. **Interface.** The Isaac Lab policy has **61 observations → 14 joint-position actions**, the same contract Pollen's onboard runtime enforces. An Isaac-Lab-trained file therefore loads into the same `walk` slot as Pollen's own [mjlab](../entities/mjlab.md)-trained policy.
2. **Depth.** The perception extension renders **RGB, depth and segmentation from a simulated head camera**. It does not emulate the real robot's 8×8 ToF.

Pollen staff and Thomas Wolf co-wrote the post, so this is a joint NVIDIA/Pollen primary rather than NVIDIA alone.

## Key claims

### Setup
- Training needs Linux with a supported NVIDIA GPU, plus Git and `uv`. Deployment needs a configured Microduck with working onboard software and a paired gamepad.
- Install: `git clone --branch develop https://github.com/isaac-sim/IsaacLab.git && uv sync`, then `uv run isaaclab list_envs --keyword MicroDuck --show_presets`.

> [!warning] The install command fails as written (checked 2026-10-24)
> `git ls-remote` on `isaac-sim/IsaacLab` shows **no `develop` branch**, only `main`. GitHub `tree/develop/...` web links redirect to `main`, which is why the post's browser links work. A `git clone --branch develop` does not get that redirect. Clone `main`: the Microduck tasks are there (PR #8270, see the [agentic tutorial page](nvidia-microduck-ai-agents-sim-blog.md)).

### The environment
- Isaac Lab *"already provides Microduck's robot model, scene, observations, actions, rewards, and domain randomization."* There are two tasks: **`IsaacContrib-Velocity-Flat-MicroDuck`** and **`IsaacContrib-Velocity-Rough-MicroDuck`**. Rough adds *"stairs, slopes, and uneven terrain"* with a difficulty curriculum.
- *"The policy takes 61 observation values and outputs 14 joint-positions. Keep the observation order, normalization, and action scaling consistent when exporting and deploying."*

### Training
- Command: `uv run isaaclab train --rl_library rsl_rl --task IsaacContrib-Velocity-Rough-MicroDuck --num_envs 4096 presets=backlash`. **The deployed policy was trained on rough terrain.**
- Physics: *"Newton with the MJWarp solver and Newton-based Better Actuator Models (BAM)"*. Together with the backlash preset, it turns *"position targets into realistic servo torques by modelling the firmware controller, motor electrical limits, friction and delay."*
- **Domain randomization**, per duck:
  - mass / centre of mass;
  - ground friction;
  - joint inertia;
  - encoder offsets;
  - battery voltage / sag;
  - command latency;
  - terrain variation and pushes;
  - **backlash randomized independently per joint**, *"to represent uneven wear."*
- Throughput: *"training with 16 GPUs … we can reach up to 1.25M steps per seconds with rough terrain and backlash enabled."* No GPU model, wall-clock time or single-GPU figure is given.

### Export and deployment
- `uv run isaaclab play … --checkpoint latest --num_envs 16 --viz newton_gl presets=backlash`. RSL-RL playback **automatically exports** `exported/policy.pt` (TorchScript) and `exported/policy.onnx`.
- On the robot:
  - `scp policy.onnx microduck@ROBOT_HOST:…`
  - `robotctl policy list`
  - `sudo robotctl policy load walk <file>` (*"Support the robot on its stand"*)
  - `robotctl monitor`
  - `sudo robotctl policy reset walk` to restore the default.
- This matches the hot-swap design in the [runtime repo](microduck-runtime-repo.md): policies are validated at load and swapped per behaviour slot.
- Figure 5 claim: *"the deployed policy's robustness to falls: Microduck recovers its footing and resumes walking after being knocked over."*

> [!note] Who gets the duck back up?
> In Pollen's runtime, falls are handled **outside** the walking policy. `limp_fall` detects the fall from the gyro and goes limp, then a separate **standing policy** gets the robot up before handing back ([runtime repo](microduck-runtime-repo.md)). Replacing the `walk` slot does not replace either. "Recovers its footing … after being knocked over" is most plausibly the runtime's recovery path plus the new walker, not a property of the Isaac-Lab-trained policy alone. The post does not distinguish the two.

### Sharing and evaluation
- **[Microduck Arena](../entities/microduck-arena.md)** (`pollen-robotics/microduck-arena` Space): *"Arena accepts models with 61 observation values, 14 action values, and a maximum size of 64 MiB."* Policies can also be shared on the Hub with a model card and training config.
- Extensions are pointed to rather than shown:
  - rough-terrain curriculum;
  - **perception with head-camera depth + robot state**: Figure 8 shows *"RGB, depth, and segmentation views"* from the simulated camera, and Figure 7 is the ramp GIF reused in the [agentic tutorial](nvidia-microduck-ai-agents-sim-blog.md);
  - Kuka–Allegro dexterous tasks;
  - the project template generator;
  - SimReady assets.

### Attribution
- *"Builds on Pollen Robotics' Microduck hardware and software, the original Microduck reinforcement-learning project (`microduck_rl`), BAM actuator modeling work (Rhoban/bam), and the Isaac Lab and Newton integrations."* This answers the credit question raised on the [Rhoban](../entities/rhoban.md) page.

> [!warning] Contradiction — "open-source bipedal robot"
> The TL;DR calls Microduck *"a newly released affordable **open-source** bipedal robot."* Pollen's own press kit **asks press not to call it open-source hardware**; only the software is open. The `microduck_rl` README puts design files under CC BY-SA-NC ([launch source](pollen-robotics-microduck.md)). Pollen staff co-wrote this post, so the framing slipped even with the vendor in the room.

## Entities mentioned
- [Microduck](../entities/microduck.md), [Pollen Robotics](../entities/pollen-robotics.md), [Hugging Face](../entities/hugging-face.md)
- [NVIDIA](../entities/nvidia.md): [Isaac Lab](../entities/nvidia-isaac-lab.md), [Newton](../entities/newton-physics-engine.md)
- [MuJoCo Warp](../entities/mujoco-warp.md) (the solver), [Rhoban](../entities/rhoban.md) (BAM), [mjlab](../entities/mjlab.md) (via `microduck_rl`)
- [Microduck Arena](../entities/microduck-arena.md)

## Concepts touched
- [Actuator fidelity in sim-to-real](../concepts/learning/actuator-fidelity-sim2real.md): per-joint backlash randomization "for uneven wear"; encoder offsets.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md): a rough-terrain walker deployed on hardware.

## Open questions
- **Does an Isaac-Lab-trained walker score in Microduck Arena?** Arena times come from Pollen's own physics rig, not Isaac Lab/Newton. Interface compatibility is guaranteed (61/14), but how the policy scores in a second simulator is not reported. That would be a natural cross-simulator transfer test; see [Microduck Arena](../entities/microduck-arena.md).
- **1.25M steps/s on 16 GPUs** — which GPUs, and what is the single-GPU rate at 4,096 envs? Pollen's mjlab recipe quotes ~1–2 h to a usable gait; there is no comparable wall-clock figure here.
- **Observation-order parity.** Both stacks are 61-D, but whether the Isaac Lab ordering, normalization and action scale are *identical* to `microduck_rl`'s, or only shape-compatible, is left to the reader (*"keep … consistent"*). A shape-compatible but permuted observation vector would load and then fail on hardware.
- The perception task's depth is a rendered camera image. The robot has no IPC path for camera frames and a 64-zone ToF, so the perception extension stays sim-only on current hardware.
