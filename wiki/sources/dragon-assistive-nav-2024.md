---
title: DRAGON — A Dialogue-Based Robot for Assistive Navigation with Visual Language Grounding (Liu et al. 2024)
type: source
url: https://doi.org/10.1109/LRA.2024.3362591
project_page: https://sites.google.com/view/dragon-wayfinding/home
arxiv: 2307.06924
local_path: raw/2307.06924v3.pdf
author: Shuijing Liu, Aamir Hasan, Kaiwen Hong, Runxuan Wang, Peixin Chang, Zachary Mizrachi, Justin Lin, D. Livingston McPherson, Wendy A. Rogers, Katherine Driggs-Campbell
published: 2024-02 (IEEE RA-L; accepted Jan 2024)
ingested: 2026-05-10
tags: [assistive-robotics, navigation, visual-impairment, clip, vqa, dialogue, turtlebot, uiuc]
---

## Summary

A dialogue-based guide robot for **persons with visual impairments (PwVI)**. The robot understands free-form spoken commands, grounds them to landmarks in the environment using **CLIP**, navigates to the requested destination, and verbally describes the surroundings (object detection) and answers questions about what it sees (VQA). Built on a [TurtleBot](../entities/turtlebot.md) 2i with a T-shaped holding handle, RPLIDAR A3 + RealSense D435i, and a wireless headset for private audio. User study with 5 blindfolded participants showed users could communicate smoothly, accept the kinesthetic guidance, and gain semantic awareness of their environment.

To the authors' knowledge it is the **first work to show that visual-language grounding via dialogue benefits robotic assistive navigation**.

## Key claims

- **Three integrated capabilities** beyond standard navigation guidance: (1) find a user's intended destination via dialogue + a CLIP-based landmark recognizer; (2) describe nearby objects on demand (object detector); (3) answer free-form visual questions (VQA model).
- **Landmark recognizer using CLIP** ([Radford et al. 2021]): image landmarks are stored on the map, and the user's free-form description is matched to the landmark whose stored image best aligns under CLIP embedding similarity. Handles **open-vocabulary** descriptions far better than closed-vocabulary object detectors with ~1200 classes.
- **Disambiguation dialogue**: if the user's description is ambiguous (e.g., "take me to the kitchen") or refers to a class with multiple instances ("a chair"), the robot generates clarification questions ("What object are you looking for in the kitchen?", "A dining chair, an office chair, or a sofa?"), then confirms the chosen goal before navigating.
- **Navigation stack**: ROS `move_base`, 2D occupancy from laser SLAM, AMCL localization, A* global + DWA local planner. Speed adjustable via voice (Accelerate / Decelerate / Pause / Resume) to match user pace.
- **Hardware choices motivated by PwVI users**:
  - **T-shaped handle** for kinesthetic guidance (rather than relying on audio direction cues alone, which suffer from delay and ambiguity).
  - **Wireless headset** (not speakers) for privacy and to avoid trip-hazard wires.
  - Sensor stack kept inexpensive (RPLIDAR A3 + RealSense D435i) so the system can replicate.
- **NLU**: Dual Intent and Entity Transformer trained on 1,092 author-collected sentences across intents: Greet, Object goal, Location goal, Describe, Ask, Accelerate, Decelerate, Pause, Resume. Includes misspelled and phonetically similar phrases ("a think" vs. "a sink") to handle ASR errors.
- **VQA fine-tuning**: 10,252 (image, question, answer) triplets collected with images from the robot's camera and questions hand-written by authors; fine-tuned 20 epochs. Specifically motivated by prior work showing PwVI ask different questions than sighted people about the same images.
- **User study**: N=5 blindfolded participants in an everyday indoor environment, three routes. Results: users could communicate with DRAGON smoothly, perceived guidance as natural, and felt the robot connected them to their surroundings.

## Limitations (acknowledged)

- Sample is **blindfolded sighted participants**, not actual PwVI users — primary acknowledged limitation.
- Object detector + VQA cannot use depth → no distance/depth information; cannot perceive anything outside the camera frame.
- NLU is a custom-trained model rather than a large LM; the paper notes "using better language models for the NLU is left for future work."

## Entities mentioned

- [Katherine Driggs-Campbell](../entities/katherine-driggs-campbell.md) — senior author / corresponding PI (UIUC ECE)
- [Shuijing Liu](../entities/shuijing-liu.md) — first author
- [TurtleBot](../entities/turtlebot.md) — TurtleBot 2i platform
- CLIP (OpenAI) — no entity page yet; foundational VL model

## Concepts touched

- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — navigation-domain PAR for visual impairment (one of the three "spikes" identified in the [Nanavati/Cakmak PAR review](nanavati2024-physically-assistive-robots-review.md))
- [Accessible robot communication](../concepts/robotics/accessible-robot-communication.md) — kinesthetic + verbal multimodal output; relates to monitoring/transparency strategies for non-visual users
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — dialogue intent recognition + module routing pattern (DRAGON predates LLM-as-router; intents go through a trained classifier instead)
- [VLA models](../concepts/learning/vla-models.md) — note: DRAGON is *not* a VLA in the modern sense; it composes a VL grounding model (CLIP) with a classical planner

## Open questions

- How does the CLIP landmark-grounding approach compare quantitatively to LLM-based grounders (e.g., ground via a VLM that reasons over scene descriptions)? Paper predates the LLM-as-scene-grounder pattern.
- The paper uses TurtleBot 2i with a tactile handle but doesn't quantify how much of the user experience benefit comes from kinesthetic guidance vs. dialogue. Worth following up.
- The Cakmak group's later finding that **mixed-initiative narration is preferred by blind users** ([Huh et al. 2026](huh2026-accessible-robot-comm.md)) suggests DRAGON's design — robot mostly silent during navigation, narrates only on user request — may underuse a key channel. No direct comparison made.
