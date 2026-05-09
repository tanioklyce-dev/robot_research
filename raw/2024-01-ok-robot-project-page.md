---
source_url: https://ok-robot.github.io/
collected: 2026-05-09
published: 2024-01
author: Peiqi Liu, Yaswanth Orru, Jay Vakil, Chris Paxton, Nur Muhammad "Mahi" Shafiullah, Lerrel Pinto
affiliation: NYU (Pinto / Shafiullah lab)
arxiv: 2401.12202
---

# OK-Robot: Zero-Shot Pick-and-Drop in Homes

Open, modular framework for zero-shot, language-conditioned pick-and-drop tasks in arbitrary homes. Integrates existing open-knowledge systems without requiring robot-specific training.

## System architecture
Three integrated components:
- Vision-Language Models (VLMs) for object detection and recognition
- Navigation primitives for autonomous movement
- Grasping primitives for object manipulation

Emphasis: systems-level integration of existing modules, not novel algorithms.

## Results
- 58.5% success rate across 171 pick-and-drop tasks in 10 real-world NYC homes
- 82% in cleaner/uncluttered environments
- 1.8× improvement over prior OVMM work
- Top failure modes: semantic memory retrieval errors (9.3%), difficult manipulation poses (8.0%), hardware difficulties (7.5%)

## Key claims
"The critical role of nuanced details when combining Open Knowledge systems like VLMs with robotic modules" — careful engineering integration matters beyond algorithm selection.

## License
MIT (code). CC BY-NC-SA 4.0 (website).

## Resources
- ArXiv 2401.12202
- GitHub + Discord
