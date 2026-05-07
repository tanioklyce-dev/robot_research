# Index

## Sources (chronological)
- [[robot-utility-models-website|Robot Utility Models Project Page]] — NYU/Meta zero-shot generalist policies for Stretch. (2024-09)
- [[maniskill-hab-paper|ManiSkill-HAB Paper]] — GPU-parallel low-level manipulation chains for HAB. (2024-12)
- [[genesis-project-page|Genesis Project Page]] — generative + ultra-fast physics engine launch. (2024-12)
- [[mujoco-playground-paper|MuJoCo Playground Paper]] — DeepMind's MJX-based robot-learning framework. (2025-02)
- [[v-jepa-2-paper|V-JEPA 2 Paper]] — Meta FAIR's JEPA world model with zero-shot Franka. (2025-06)
- [[genie-envisioner-paper|Genie Envisioner Paper]] — unified world foundation platform for manipulation. (2025-08)
- [[hello-robot-stretch-docs|Hello Robot Stretch Documentation]] — Stretch 3 docs (ROS 2 + Python + MuJoCo/Gazebo). (2025)
- [[stretch-ai-llm-agent-docs|Stretch AI LLM Agent Documentation]] — concrete LLM-agent stack for the Stretch robot. (2024–2025)
- [[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]] — educational Jetson Orin Nano kit; Gazebo + cloud/offline LLM-agent curriculum. (2024–2025)
- [[hiwonder-rosorin-pro-user-manual|Hiwonder ROSOrin Pro User Manual]] — hardware spec sheet for the 6-DOF arm + base variant. (2024–2025)
- [[hiwonder-openclaw-tutorial|Hiwonder OpenClaw Practical Tutorial]] — Hiwonder's manipulation-aware LLM-agent framework. (2024–2025)
- [[robocasa365-paper|RoboCasa365 Paper]] — 365-task household manipulation benchmark. (ICLR 2026)
- [[agibot-genie-sim-3-announcement|AGIBOT Genie Sim 3.0 Announcement]] — open simulation platform launch at CES 2026. (2026-01)
- [[agibot-genie-envisioner-2-announcement|AGIBOT Genie Envisioner 2.0 Announcement]] — world model evolved into a "world simulator." (2026)
- [[nvidia-newton-physics-engine-developer-page|NVIDIA Newton Physics Engine Developer Page]] — Newton landing page; Linux-Foundation governance. (2026)
- [[nvidia-newton-contact-rich-manipulation-blog|NVIDIA Newton Contact-Rich Manipulation Blog]] — Newton 1.0 GA at GTC 2026 inside Isaac Lab. (2026)
- [[leworldmodel-paper|LeWorldModel Paper]] — first stable end-to-end JEPA from raw pixels. (2026-03)
- [[top-10-physical-ai-models-2026|Top 10 Physical AI Models 2026]] — VLA model survey including GR00T N1.7 EA. (2026-04)

## Entities

### Companies
- [[nvidia|NVIDIA]] — owns most of the agentic-robotics simulation substrate. (5 sources)
- [[hiwonder|Hiwonder]] — Chinese educational-robotics vendor; ROSOrin / ROSOrin Pro kits + OpenClaw. (3 sources) _stub_
- [[agibot|AGIBOT]] — Shanghai embodied-AI / humanoid company. Open-source-heavy. (3 sources)
- [[hello-robot|Hello Robot]] — Stretch mobile manipulator + stretch_ai stack. (3 sources)
- [[meta-fair|Meta FAIR]] — Yann LeCun's lab; JEPA research line. (1 source)
- [[google-deepmind|Google DeepMind]] — MuJoCo, Newton co-development. (2 sources) _stub_
- [[mila|Mila]] — Quebec AI Institute; frequent JEPA collaborator. (2 sources) _stub_
- [[hillbot|Hillbot]] — UCSD spinoff that maintains ManiSkill. (1 source) _stub_
- [[disney-research|Disney Research]] — Newton co-developer with NVIDIA + DeepMind. (1 source) _stub_

### Simulators / frameworks
- [[nvidia-isaac-sim|NVIDIA Isaac Sim]] — Omniverse-based robotics simulator. (2 sources)
- [[nvidia-isaac-lab|NVIDIA Isaac Lab]] — open-source learning framework on Isaac Sim. (3 sources)
- [[newton-physics-engine|Newton physics engine]] — Linux-Foundation, GPU-accelerated. (3 sources)
- [[mujoco-playground|MuJoCo Playground]] — DeepMind's MJX-based learning framework. (3 sources)
- [[genesis|Genesis]] — generative + ultra-fast physics engine. (2 sources)
- [[agibot-genie-sim|AGIBOT Genie Sim 3.0]] — open embodied-AI sim on Isaac Sim. (2 sources)
- [[robocasa|RoboCasa]] — household manipulation benchmark (RoboCasa365 at ICLR 2026). (1 source)
- [[maniskill|ManiSkill]] — [[sapien|SAPIEN]]-based GPU-parallel manipulation benchmark. (1 source)
- [[sapien|SAPIEN]] — UCSD robot simulation framework underlying ManiSkill. (1 source) _stub_

### Robot platforms
- [[stretch|Stretch]] — Hello Robot's mobile manipulator (Stretch 3). De-facto research platform. (3 sources)
- [[rosorin|ROSOrin]] — Hiwonder's Jetson Orin Nano educational mobile robot kit. (2 sources)
- [[rosorin-pro|ROSOrin Pro]] — Hiwonder's 6-DOF arm + base variant of ROSOrin. (2 sources)
- [[rosorin-pro-arm|ROSOrin Pro 6-DOF arm]] — HX-12H-servo manipulator on the ROSOrin Pro kit. (2 sources) _stub_

### Software stacks
- [[stretch-ai|stretch_ai]] — Hello Robot's open-source Python stack with an LLM agent. (4 sources)
- [[openclaw|OpenClaw]] — Hiwonder's manipulation-aware LLM-agent framework for ROSOrin Pro. (1 source)

### World models
- [[nvidia-cosmos|NVIDIA Cosmos]] — world foundation model + simulation engine (generative video). (4 sources)
- [[genie-envisioner|Genie Envisioner]] — AGIBOT's world simulator GE-Sim2 (generative video). (4 sources)
- [[v-jepa-2|V-JEPA 2]] — Meta FAIR's JEPA world model (latent prediction); zero-shot Franka. (1 source)
- [[leworldmodel|LeWorldModel]] — first stable end-to-end JEPA from raw pixels. (1 source)

### VLA models / generalist policies
- [[nvidia-groot|NVIDIA GR00T]] — open VLA bundled with Isaac Lab. (3 sources) _stub_
- [[robot-utility-models|Robot Utility Models]] — NYU/Meta zero-shot mobile-manipulation BC. (1 source)

### LLMs
- [[qwen|Qwen]] — Alibaba's open-weights LLM family. Default local LLM in both stretch_ai (3B) and ROSOrin (1.7B). (2 sources) _stub_

### Tools
- [[ollama|Ollama]] — local LLM runtime (used by ROSOrin offline curriculum). (1 source) _stub_
- [[mimicgen|MimicGen]] — synthetic-demo expansion tool used by RoboCasa365. (1 source) _stub_

## Concepts
- [[vla-models|VLA models]] — vision-language-action robot foundation models. (6 sources)
- [[sim-to-real-transfer|Sim-to-real transfer]] — bridging simulator-trained policies to real robots. (4 sources)
- [[world-model-simulators|World-model simulators]] — two paradigms: generative-video and JEPA latent-prediction. (4 sources)
- [[jepa|Joint-Embedding Predictive Architecture]] — predict next-state representations, not pixels. (2 sources)
- [[imitation-learning|Imitation learning]] — supervised learning from demonstrations. (2 sources)
- [[llm-agent-architecture|LLM-agent architecture]] — LLM-emits-tool-calls control pattern. (3 sources)

## Syntheses
- [[simulators-for-agentic-robotics-2026|Simulators for agentic robotics — 2026 landscape]] — full landscape survey, 6 categories. (updated 2026-05-07)
- [[llm-agent-architecture-across-stacks|LLM-agent architecture across stacks]] — three-way comparison of stretch_ai, ROSOrin, OpenClaw. (2026-05-07)
- [[generative-video-vs-jepa-world-models|Generative-video vs JEPA world models]] — what each predicts, costs, and demonstrates. (2026-05-07)

## Known gaps / TBD
- Drake (TRI/MIT) entity page
- Gazebo (the simulator itself) — referenced by both Hello Robot and Hiwonder docs; deserves its own entity page distinct from MuJoCo Playground
- Webots, CoppeliaSim, PyBullet entity pages (low priority — not agentic-robotics center of gravity)
- Pi (Physical Intelligence) entity + simulation approach
- Skild AI entity + approach
- LIBERO, RoboMimic benchmark concept/source pages
- TRI LBM (Toyota Research Institute Large Behavior Model) — referenced in RoboCasa365 paper as baseline
- Octo — referenced in RoboCasa365 paper as baseline
- Stretch Mujoco — Hello Robot's MuJoCo wrapper; thin or substantive?
- xArm 7 — UFactory manipulator used as cross-embodiment target by Robot Utility Models
- DINO-WM, Dreamer/DreamerV3, TD-MPC, PLDM — world-model baselines referenced in LeWorldModel paper
- Droid dataset — robot teleoperation dataset used by V-JEPA 2-AC
- Habitat (Meta) — embodied-AI sim, mentioned as legacy in synthesis
- TurtleBot — canonical educational ROS robot, useful comparison for ROSOrin
- StepFun — Chinese multimodal AI provider used by ROSOrin's Chinese-language fallback
- sherpa-onnx — offline ASR + TTS toolkit used by ROSOrin
- WonderEcho Pro — Hiwonder voice module accessory
- Hiwonder vision/CV chapter (YOLOv11 + TensorRT) — could warrant its own concept/source page on a deeper ingest
- HX-12H bus servo, COIN-D6 LiDAR, Deptrum Aurora930 depth camera, MPU6050 IMU — hardware-component pages on demand
- People pages (low priority): Yann LeCun, Aaron Edsinger, Mahi Shafiullah, Yuke Zhu, Mahmoud Assran
