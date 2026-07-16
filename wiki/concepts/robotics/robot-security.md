---
title: Robot Security (Robot Cybersecurity)
type: concept
created: 2026-07-15
updated: 2026-07-15
sources: 1
tags: [robot-security, cybersecurity, ros2, security-assessment, alias-robotics, rsf, misra, safety-vs-security]
---

# Robot Security (Robot Cybersecurity)

**Robot security** — protecting a robot *system* (its compute, OS, middleware, network, firmware, and control applications) against malicious actors. Distinct from **robot safety** (protecting people from the robot's physical action — [ISO 13482 etc.](robot-safety-standards.md)): safety asks "will it hurt someone by accident?"; security asks "can someone make it hurt someone on purpose, or exfiltrate/tamper with it?" The two increasingly interact — a security breach can defeat a safety function.

## The assessment view: RSF's four layers

The wiki's anchor source, the **[Robot Security Framework (RSF)](../../sources/aliasrobotics-rsf-github.md)** ([Alias Robotics](../../entities/alias-robotics.md)), organizes a robot security assessment into four layers:

1. **Physical** — exposed ports, tamper detection, physical access control.
2. **Network** — authentication, protocol safety, fingerprinting, monitoring (internal + external).
3. **Firmware** — secure OS/firmware update, middleware compliance.
4. **Application** — authorization, privacy, data integrity, encryption, third-party components.

It explicitly targets **[ROS 2](../../entities/ros2.md)** middleware and includes **MISRA** compliance criteria. RSF is a **checklist methodology**, not a quantitative score.

## Two threads that meet on the robot

This wiki tracks robot security from two directions that converge as robots get **LLM-agent brains on [ROS 2](../../entities/ros2.md)**:

- **Classical infosec (the RSF thread)** — securing OS/middleware/network/firmware; the traditional pentest surface.
- **AI-layer security (the agent thread)** — [prompt injection through the perception/instruction channel](../agents/llm-agent-architecture.md), the **input rail**, and [AI guardrails](../safety/ai-guardrails.md) ([NeMo Guardrails](../../entities/nemo-guardrails.md), [garak](../../entities/garak.md) red-teaming). A robot whose task planner is an LLM inherits both attack surfaces at once.

The wiki's own [ROS 2↔MCP server](../../entities/ros2-mcp-server.md) work sits exactly at this junction — an LLM agent issuing ROS 2 commands is both an RSF Application-layer concern and an input-rail concern.

## Related concepts

- [Robot safety standards (ISO 13482)](robot-safety-standards.md) — the *safety* neighbor (physical harm, not adversarial); its productized instance is **[NVIDIA Halos](../../entities/nvidia-halos.md)** (functional safety on IGX Thor). Halos hardens the robot against *accidents*; RSF hardens it against *attackers* — orthogonal layers on the same machine.
- [AI guardrails](../safety/ai-guardrails.md), [LLM-agent architecture / input rail](../agents/llm-agent-architecture.md) — the AI-layer security thread.

## Mentioned in

- [Robot Security Framework (RSF)](../../sources/aliasrobotics-rsf-github.md) — the anchor source.
