---
title: Lessons Learned from Designing and Evaluating a Robot-assisted Feeding System for Out-of-lab Use (Nanavati et al. 2025)
type: source
url: https://robotfeeding.io/publications/hri25a/
local_path: raw/nanavati2025lessons.pdf
author: Amal Nanavati, Ethan K. Gordon, Taylor A. Kessler Faulkner, Yuxin (Ray) Song, Jonathan Ko, Tyler Schrenk, Vy Nguyen, et al.; Maya Cakmak, Siddhartha S. Srinivasa
published: 2025 (HRI 2025 — Best Systems Paper Finalist)
ingested: 2026-05-09
tags: [assistive-robotics, feeding, out-of-lab, hcrlab, maya-cakmak, amal-nanavati, cbpr, hri2025]
---

## Summary

End-to-end open-source robot-assisted feeding system designed for out-of-lab use, co-developed with two community researchers (CRs) who both have quadriplegia from spinal cord injury. Addresses the gap between controlled lab evaluations and real-world assistive robot deployment. Key design principles: portability, safety, reliability, customizability, user control. Two studies: multi-user on-campus (5 participants + 1 CR; 3 locations) and in-home single-user (1 CR; 5 days; 10 meals). HRI 2025 Best Systems Paper Finalist.

## Key claims

- **System hardware**: 6-DOF Kinova JACO arm; Intel RealSense D415 RGBD eye-in-hand camera (Jetson Nano); custom 3D-printed fork with ATI Nano25 F/T sensor; ~$50,000 cost; portable; self-contained (no external wires); wheelchair or hospital table mountable.
- **Software stack**: ROS2 + ros2-control; web app (React) — users interact from any device browser using their own ATs; MoveIt2 + RRT-Connect for planning; behavior trees (py_trees); SegmentAnything (ViT-B) for food mask generation; online action selection via LinUCB bandit.
- **Community-based participatory research (CBPR)**: co-developed with CR1 since 2018, involving semi-weekly meetings, pilot studies, and co-design of off-nominal scenarios. CR1 passed away before publication; CR2 continued the work and is a paper co-author.
- **Three design principles implemented**: (1) Portability — no external wires; battery-powered; mounts to wheelchair or table; (2) Customizability — arm configurations, bite transfer distance/speed, auto-continue behavior, planning scenes are all user-adjustable via settings menu; (3) User Control — variable LoC: supervisory (pause), decision support (multiple options), or teleoperation (direct Cartesian/joint).
- **Study 1 results**: Bite acquisition success ≥80% for most food items for all 5 participants; bite duration 1:00–2:26 min (vs. 18–30 sec for non-disabled users); system rated average-or-above on usability by most users; outperformed caregiver feeding on independence and control metrics.
- **Study 2 results**: CR2 fed himself 10 meals across diverse contexts at home over 5 days — real in-home deployment.
- **Three key lessons**:
  1. Spatial contexts are numerous — customizability allows users to adapt to their specific environment.
  2. Off-nominals (unexpected events) will arise — variable autonomy lets users overcome them rather than ending the session.
  3. Assistive robots' benefits depend on context — the same system is more or less useful depending on environment, caregiver availability, and user state.

## Entities mentioned

- [Maya Cakmak](../entities/maya-cakmak.md)
- [HCR Lab](../entities/hcrlab.md)

## Concepts touched

- [Assistive robotics](../concepts/assistive-robotics.md) — the most detailed out-of-lab feeding deployment in the wiki
- [End-user robot programming](../concepts/end-user-robot-programming.md) — customizability and variable autonomy as key design choices

## Open questions

- Were the 3-location on-campus results broken down by location? (cafeteria vs. conference room vs. office likely differ in noise, space, lighting)
- What was the full list of off-nominal scenarios co-created with CR1? (Table II in paper shows examples)
- Long-term outcome: Does the system continue being used after the study period?
