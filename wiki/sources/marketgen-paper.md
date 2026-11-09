---
title: "MarketGen: A Scalable Simulation Platform with Auto-Generated Embodied Supermarket Environments"
type: source
url: https://arxiv.org/abs/2511.21161
fetch_url: https://arxiv.org/pdf/2511.21161v2
local_path: raw/marketgen-2511.21161v2.pdf
sha256: 13a16acf1f30ad7b674d17e6743abc32e73f435807afd69ba8684f209e79dbf3
author: Hu, Feng, Peng, He, Chen, Sui, Luo, Yin, Li, Zhang
published: 2026-03-05
ingested: 2026-11-08
tags: [retail, grocery, benchmark, simulation, isaac-sim, procedural-generation, sim-to-real]
---

# MarketGen: A Scalable Simulation Platform with Auto-Generated Embodied Supermarket Environments

## Summary

A supermarket scene generator built on [Isaac Sim](../entities/nvidia-isaac-sim.md) and Unreal Engine, which turns text or reference images into stores using an LLM planner plus procedural placement. Its benchmark has a cashier task and an aisle task. **Modular LLM-plus-affordance agents stayed below 15% overall.** The published date is v2; v1 appeared in November 2025.

## Key claims

- **Assets.** Over 1,000 goods in 10 categories and over 100 parameterized facilities.
- **Tasks.** Checkout Unloading is a long-horizon tabletop task for a Franka arm. In-Aisle Item Collection is mobile manipulation.
- **Table 2 success rate (%):**

| Planner | Checkout unloading | In-aisle collection | Overall |
|---|---|---|---|
| GPT-4o | 14.22 | 8.33 | 11.28 |
| Claude Sonnet 4.5 | 19.77 | 6.66 | 13.22 |
| Gemini 2.5 Pro | 17.32 | 10.41 | 13.87 |
| Qwen3-VL-Plus | 15.20 | 9.20 | 12.20 |

- **Scoring.** Success is partial credit per goal condition, so these numbers are not whole-task completion rates.
- **Real comparison.** 20 grasps per object shape, simulation against real: bottles 55/50%, cans 45/45%, boxes 25/15%, bags 0/0%.

> [!note] What the sim-to-real result covers
> The paper's "successful sim-to-real transfer" refers to one affordance model's grasp rates across four shapes in one arranged scene. It doesn't test the full benchmark tasks on a robot, and it reports no correlation statistic.

## Entities mentioned

- [MarketGen](../entities/marketgen.md)
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md)

## Concepts touched

- [Retail and grocery robotics](../concepts/robotics/retail-and-grocery-robotics.md)

## Open questions

- How do end-to-end policies score here? The paper tests only modular agents.
- Why do bags fail completely, in both simulation and the real world?
