---
title: Open-source robot AI research projects — landscape
type: synthesis
created: 2026-05-17
updated: 2026-07-13
tags: [open-source, ecosystem, lerobot, jepa, simulators, fly, karpathy, landscape-survey]
---

A grouped catalog of the **open-source robot AI projects** tracked in this wiki — frameworks, simulators, datasets, model checkpoints, open hardware, and codebases that anyone can read, run, or fork. Internal-only / closed products (Tesla Optimus, Apptronik Apollo, Boston Dynamics Atlas) are excluded.

Each entry links to the wiki page that goes deeper. Where a project releases both *code* and *hardware* (LeKiwi, XLeRobot, SO-ARM, Reachy 2), both axes are open.

## Imitation learning + low-cost hardware (the LeRobot ecosystem)

The single most active open-source robotics-AI scene tracked in this wiki.

- [LeRobot](../../entities/lerobot.md) — [Hugging Face](../../entities/hugging-face.md)'s open imitation-learning framework; ACT default policy; 916-team Worldwide Hackathon (June 2025); the substrate underneath every kit below.
- [SO-ARM100 / SO-ARM101](../../entities/so-arm101.md) — [The Robot Studio](../../entities/the-robot-studio.md) open-hardware low-cost arm (Apache 2.0); the dominant low-cost manipulator in this wiki's coverage.
- [LeKiwi](../../entities/lekiwi.md) — [SIGRobotics-UIUC](../../entities/sigrobotics-uiuc.md) 3-wheel holonomic mobile manipulator; sub-$1k; 1,300+ GitHub stars.
- [XLeRobot](../../entities/xlerobot.md) — [Vector Wang](../../entities/vector-wang.md)'s $660 dual-arm household robot (two SO-ARM101s + LeKiwi base; 90% 3D-printed). Two-time Embodied AI Hackathon 2025 winner.
- [LeRobot Worldwide Hackathon 2025](../../entities/lerobot-worldwide-hackathon-2025.md) — the event that sized the ecosystem; ~400 submissions, 30 ranked winners.

## Open robot platforms (hardware + software stacks)

- [Stretch](../../entities/stretch.md) + [stretch_ai](../../entities/stretch-ai.md) — [Hello Robot](../../entities/hello-robot.md) mobile manipulator with open Python stack (LLM-agent included).
- [Reachy 2](../../entities/reachy.md) — [Pollen Robotics](../../entities/pollen-robotics.md) open-source bimanual mobile manipulator; ROS 2.
- [Yuri](../../entities/yuri.md) + **OpenArm+ / OpenBase** — [Sensori Robotics](../../entities/sensori-robotics.md)'s integrated bimanual Physical-AI rig; arm + base designs open (github.com/SensoriRobotics, docs.openarm.dev), but sold as a supported turnkey product with force-feedback teleop + LeRobot recording (quote-only price; "a complete robot, not a box of parts").
- [TurtleBot](../../entities/turtlebot.md) — Open Robotics-maintained; ROS 2 native in TurtleBot 4.
- [iRobot Create 3](../../entities/irobot-create-3.md) — Roomba-i3-derived ROS 2 mobile base under TurtleBot 4.
- [Hope Jr Arm](../../entities/hope-jr-arm.md), [Koch v1.1](../../entities/lekiwi.md) (Dynamixel-based, used as a LeKiwi arm variant) — additional open-arm options.

## Open educational kits with some open code

- [ROSOrin / ROSOrin Pro](../../entities/rosorin-pro.md) — [Hiwonder](../../entities/hiwonder.md) educational kits; the Hiwonder docs are open enough to read and adapt. The Pro ships upstream [OpenClaw](../../entities/openclaw.md) (MIT, 375K stars) plus Hiwonder's [`openclaw_controller`](../../entities/openclaw-controller.md) ROS 2 bridge module.
- [myBuddy 280](../../entities/mybuddy-280.md) — [Elephant Robotics](../../entities/elephant-robotics.md); open URDF + ROS 1 stack + myBlockly/myStudio tooling.
- [myAGV](../../entities/myagv.md) — Elephant mobile base with ROS / open Raspberry Pi pipeline.
- [TonyPi](../../entities/tonypi.md) — Hiwonder hobby-tier biped kit; open assembly + control reference.

## Open organizations maintaining the above

- [SIGRobotics-UIUC](../../entities/sigrobotics-uiuc.md) — student-led robotics SIG at UIUC; LeKiwi flagship + ~10 other GitHub repos (matcha-bot, F1Tenth racing, Mini Humanoid, etc.).
- [Farama Foundation](../../entities/farama-foundation.md) — non-profit RL-API steward; 19 projects.
- [The Robot Studio](../../entities/the-robot-studio.md) — open-hardware design authority for the SO-ARM lineage.
- [Hugging Face](../../entities/hugging-face.md) — LeRobot maintainer; HF Hub hosts model weights across JEPA / VLA / IL coverage.
- [NVIDIA GEAR](../../entities/nvidia-gear.md) — corporate lab whose open releases (GR00T, EgoScale, DreamDojo) anchor the embodied-AI scene's higher tier.

## JEPA / world-model open code

- [LeWorldModel](../../entities/leworldmodel.md) (Maes et al. 2026) — open code; first independent reproduction by [Onchain AI Garage](../../sources/onchain-ai-garage-lewm-reproduction.md) on a single RTX 3060.
- [V-JEPA 2 GitHub](../../sources/vjepa2-github.md) — [Meta FAIR](../../entities/meta-fair.md) open repo; ViT-B→g family; dual-licensed.
- [PLDM](../../entities/pldm.md) — Sobal-line end-to-end JEPA WM (NYU + FAIR); open code.
- [DINO-WM](../../entities/dino-wm.md), [DINO-world](../../entities/dino-world.md) — frozen-feature world models, open code.
- [LeJEPA](../../sources/lejepa-paper.md) — Balestriero & LeCun; SIGReg foundational paper, open code.
- [stable-worldmodel](../../entities/stable-worldmodel.md) — Python infrastructure under LeWM (env zoo + planning API + dataset format).

## Open VLAs / generalist policies

- [NVIDIA GR00T](../../entities/nvidia-groot.md) — open VLA bundled with [Isaac Lab](../../entities/nvidia-isaac-lab.md); winner of both sites of the October 2025 Embodied AI Hackathon.
- [OK-Robot](../../entities/ok-robot.md) — NYU zero-shot pick-and-drop; open code; 58.5% in 10 NYC homes.
- [Robot Utility Models](../../entities/robot-utility-models.md) — NYU/Meta zero-shot mobile manipulation; open code + data.
- [Dobb·E](../../entities/dobb-e.md) — NYU precursor to RUM; HPR encoder + Homes-of-New-York dataset; CC-BY-4.0.
- [π0](../../sources/pi-zero-paper.md) — [Physical Intelligence](../../entities/physical-intelligence.md)'s VLA flow-matching model.

## Behavior-cloning baselines (open code)

- [Diffusion Policy](../../entities/diffusion-policy.md) — Chi et al. 2023; conditional DDPM over actions; the BC-line state-of-the-art for the LeWM-comparison era.
- [UMI](../../entities/umi.md) — Universal Manipulation Interface; hand-held gripper data-collection system.
- [IBC](../../entities/ibc.md), [BET](../../entities/bet.md), [VQ-BeT](../../entities/vq-bet.md) — the BC-lineage on PushT.

## Karpathy's pedagogical + agent-research repos

Pedagogy-grade reference implementations that anchor multiple wiki curriculum modules.

- [karpathy/micrograd](../../sources/karpathy-micrograd.md) — scalar autograd engine (~100 LOC) + a 50-LOC PyTorch-style NN library.
- [karpathy/nanoGPT](../../sources/karpathy-nanogpt.md) — minimal GPT training repo; ~300-line decoder-only-transformer reference.
- [karpathy/nanochat](../../sources/karpathy-nanochat.md) — full end-to-end ChatGPT pipeline (~$48 / 8XH100); successor to nanoGPT.
- [karpathy/autoresearch](../../sources/karpathy-autoresearch.md) — agent-driven LLM training research; produced two nanochat speedrun-leaderboard gains.

## Whole-organism agentic AI (fruit fly)

Open-source biological-agent loops — different from robotics but the closest analogue this wiki tracks.

- [flybody](../../entities/flybody.md) — HHMI Janelia + DeepMind; Apache 2.0; MuJoCo-based whole-body *Drosophila* (102 DoFs).
- [NeuroMechFly / flygym](../../entities/neuromechfly.md) — NeLy-EPFL; Apache 2.0; v2 active 2026 with Warp/MJWarp GPU acceleration.
- [FlyWire](../../entities/flywire.md) — international consortium; complete adult *Drosophila* connectome.
- [Drosophila brain model](../../entities/drosophila-brain-model.md) — Shiu et al., MIT-licensed Brian 2 LIF on the FlyWire connectome.
- [flyvis](../../entities/flyvis.md) — TuragaLab; MIT-licensed connectome-constrained DMN of the fly visual system.

## Open simulators + physics engines

- [MuJoCo](../../entities/mujoco.md) — DeepMind-maintained; Apache 2.0; substrate for almost every other open robot-sim in this wiki.
- [MuJoCo Playground](../../entities/mujoco-playground.md) — DeepMind's MJX-based learning framework.
- [Newton physics engine](../../entities/newton-physics-engine.md) — Linux Foundation; NVIDIA + DeepMind + Disney co-development.
- [Genesis](../../entities/genesis.md) — generative + ultra-fast physics engine.
- [Isaac Lab](../../entities/nvidia-isaac-lab.md) — NVIDIA's open learning framework on Isaac Sim. (Isaac Sim itself is free-to-use, not formally open-source.)
- [AGIBOT Genie Sim 3.0](../../entities/agibot-genie-sim.md) — open embodied-AI sim on Isaac Sim.
- [ManiSkill](../../entities/maniskill.md) / [SAPIEN](../../entities/sapien.md) — UCSD-line GPU-parallel manipulation benchmark + sim framework.

## Open RL APIs + benchmarks

The [Farama Foundation](../../entities/farama-foundation.md) maintains 19 RL projects under one non-profit umbrella. The most-cited in this wiki:

- [Gymnasium](../../entities/gymnasium.md) — single-agent RL env API (OpenAI gym successor).
- [PettingZoo](../../entities/pettingzoo.md) — multi-agent RL env API.
- [Gymnasium-Robotics](../../entities/gymnasium-robotics.md) — MuJoCo-backed robotics envs (Fetch / Hand / Maze / Adroit / Franka Kitchen / MaMuJoCo).
- [Arcade Learning Environment (ALE)](../../entities/ale.md) — Atari 2600 RL benchmark.
- [DM Control Suite](../../entities/dm-control.md) — DeepMind continuous-control RL benchmark.
- [Metaworld](../../entities/metaworld.md) — Stanford/Berkeley 50-task manipulation meta-RL benchmark.
- [LIBERO](../../entities/libero.md) — lifelong-learning manipulation benchmark; de-facto VLA-eval.
- [RoboCasa](../../entities/robocasa.md) — household-manipulation benchmark (RoboCasa365 at ICLR 2026).
- [PushT](../../entities/pusht.md) / [PointMaze](../../entities/pointmaze.md) — default lightweight benches across LeWM / DINO-WM / JEPA-WMs.

## Open vision foundation models

- [DINOv2](../../entities/dinov2.md) — Meta FAIR self-supervised ViT (LVD-142M, ViT-S/B/L/g); Apache 2.0; substrate for DINO-WM / DINO-world / JEPA-WMs.
- [DINOv3](../../entities/dinov3.md) — 7B-parameter ViT SSL foundation; Gram anchoring; new SSL state-of-the-art on dense tasks.

## Open scene-description + formats

- [OpenUSD](../../entities/openusd.md) — open scene-description + physics-schema layer (UsdPhysics, MjcPhysics, NewtonSceneAPI); the substrate underneath Newton + Isaac Sim + several others.

## Open generative models

- [DDPM](../../entities/ddpm.md) — Ho, Jain, Abbeel (Berkeley, NeurIPS 2020); foundational denoising-diffusion class; substrate of [Diffusion Policy](../../entities/diffusion-policy.md) and [NVIDIA Cosmos](../../entities/nvidia-cosmos.md).

## What this list is not

- Not a buying guide (see [overview.md](../../overview.md) for the newcomer shortlist of acquirable robots).
- Not a quality ranking — appearing here just means the project is open-source and tracked in this wiki.
- Not exhaustive — a project's absence reflects "not yet ingested" more often than "deliberately excluded." Notable gaps the wiki could fill: OpenVLA, RLHF-line open implementations, Voyager, OpenAI's open envs.

## Related

- [Robot platforms comparison](robot-platforms-comparison.md) — narrower platform-by-platform comparison.
- [Simulators for agentic robotics — 2026 landscape](../simulators/simulators-for-agentic-robotics-2026.md) — narrower simulator-specific survey.
- [Wiki overview](../../overview.md) — newcomer entry-point and starter shortlist of acquirable robots.
- [awesome-physical-ai (GitHub list)](../../sources/awesome-physical-ai-github.md) — external solo-curated catalog of the same landscape; its source page carries a coverage-vs-this-wiki gap analysis (robot-safety standards, MBRL world models, locomotion corpus, evaluation methodology).
