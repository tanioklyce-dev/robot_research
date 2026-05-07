---
title: Genesis Project Page
type: source
url: https://genesis-embodied-ai.github.io/
author: Genesis Embodied AI consortium (20+ research labs)
published: 2024-12
ingested: 2026-05-06
tags: [genesis, physics-engine, generative-simulation, vlm]
---

## Summary
Project page for [[genesis|Genesis]], a generative and universal physics engine for robotics and embodied AI, released December 2024 after a 24-month collaboration across 20+ research labs.

## Key claims
- Headline benchmark: 43 million FPS simulating a Franka arm on a single RTX 4090.
- Claims 10–80× faster than Isaac Gym/Sim/Lab and MuJoCo MJX without sacrificing fidelity.
- Pythonic API; lightweight install.
- Includes a photorealistic renderer.
- Native generative simulation: a [[vla-models|VLM]]-based agent uses simulator APIs as tools to build 4D worlds from natural-language descriptions.
- Outputs include scenes, tasks, rewards, assets, motions, policies, trajectories, camera paths, and physically-accurate videos.

## Entities mentioned
- [[genesis|Genesis]]

## Concepts touched
- Generative simulation
- [[vla-models|VLM]] / LLM-driven scene authoring
- High-throughput parallel physics

## Open questions
- The 43M FPS claim is for a specific scenario (single Franka, no contact). What's typical throughput on contact-rich tasks?
- How widely is Genesis actually adopted in industry vs. research demos?
- How does it integrate with [[vla-models|VLA models]] beyond scene generation — is closed-loop policy training first-class?
