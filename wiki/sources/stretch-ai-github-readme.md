---
title: stretch_ai GitHub README
type: source
url: https://github.com/hello-robot/stretch_ai
local_path: raw/2026-11-08-stretch-ai-github-readme.md
sha256: 436e73d4d200044024a3544f4bce7cc820ae6f023ec6a9a3df5d44bd086cbaea
author: Hello Robot
published: Unknown (retrieved 2026-11-08; last commit 2026-07-02)
ingested: 2026-11-08
tags: [stretch-ai, stretch-3, stretch-4, hello-robot, software-compatibility, primary-source]
---

# stretch_ai GitHub README

## Summary

The README of [stretch_ai](../entities/stretch-ai.md), checked on 2026-11-08 to see whether the stack covers [Stretch 4](../entities/stretch.md). **It names only Stretch 3**, with an upgrade path for the older Stretch 2. Stretch 4 is not mentioned. The last commit was 2026-07-02, seven weeks after Stretch 4 launched.

## Key claims

- The project "is designed to help researchers and developers build intelligent behaviors for the Stretch 3 mobile manipulator."
- Stretch 3 is the listed robot requirement, and a Stretch 2 Upgrade Kit is offered for older robots.

> [!note] What this does and does not show
> It shows the README does not claim Stretch 4 support. It does not show that the code cannot run there. Stretch 4 uses a new control stack and ROS 2 Jazzy ([launch post](hello-robot-stretch-4-launch.md)), so a port should be assumed necessary until someone demonstrates otherwise.

## Entities mentioned

- [stretch_ai](../entities/stretch-ai.md)
- [Stretch](../entities/stretch.md)

## Concepts touched

- [LLM agent architecture](../concepts/agents/llm-agent-architecture.md)

## Open questions

- Does Hello Robot plan a Stretch 4 port, or does its new documentation replace this stack?
