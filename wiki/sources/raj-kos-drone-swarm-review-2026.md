---
title: "Recent Developments and Applications of Drone Swarm (Raj & Kos, 2026)"
type: source
url: https://doi.org/10.3390/s26102943
local_path: raw/sensors-26-02943.pdf
sha256: 3b7d2664080a6dae9ef95666d192fe5151039e306eabaabec850f2b9055a06f0
author: Ravi Raj, Andrzej Kos
affiliations: Universitat Politècnica de Catalunya (UPC, BarcelonaTech); AGH University of Kraków
published: 2026-05-08
ingested: 2026-05-31
venue: Sensors (MDPI), 2026, 26(10):2943
license: CC BY 4.0
format: pdf
tags: [uav, drone, swarm, swarm-intelligence, swarm-robotics, agentic-uavs, emergence, anti-drone, military, path-planning, trajectory-prediction, deep-learning, reinforcement-learning, pso, aco, review]
---

## Summary

A 21-page open-access **review of UAV / drone-swarm systems** — surveying how aerial swarms move from operator-piloted fleets toward **cooperative, autonomous, cognitive** collectives. It organizes the field into trajectory generation, trajectory prediction, counter-swarm ("anti-drone") techniques, and swarm-intelligence/optimal-control, with a strong **defense / military** emphasis throughout, framed by bio-inspired emergence (ant colonies, bee voting, flocking). The recurring thesis: AI/DL reallocates aerial power "from costly platforms to synchronized autonomy," and as offensive swarms mature, **anti-drone-swarm strategy becomes equally important**. The authors flag the dual-use nature explicitly (DURC statement).

## Key claims

- **A swarm ≠ a crowd.** "A multitude of uncoordinated unoccupied systems does not constitute a 'swarm'; it represents a flood." A swarm has components that synchronize/adjust into "a unified, emergent entity." Working definition adopted (from Price): an assembly functioning collaboratively under a single operator's directives via a shared architecture.
- **Four command-and-control models** (centralized → distributed):
  - **Coordination by consensus** — members settle via voting / auction mechanisms.
  - **Centralized control** — a central controller assigns each member's duties.
  - **Emergent coordination** — coordination arises naturally from local interaction, "as in animal swarms" (the [boids](../concepts/alife/flocking-and-boids.md) regime).
  - **Hierarchical control** — squad-agents governed by superior controllers.
  - Tradeoff: fully decentralized swarms find good solutions but slowly (ant-colony-like); centralized/hierarchical are faster but bandwidth-hungry; low-bandwidth settings push toward consensus or *stigmergy* (indirect, environment-mediated coordination).
- **Trajectory generation.** Optimal time-allocation for racing quadrotor swarms; **SARG** (Swarm Allocation and Route Generation) joins task assignment + collision-free 3D paths; **LEVIOSA** turns natural-language/audio commands into multi-UAV 3D trajectories via **multimodal LLMs**.
- **Trajectory prediction** (mostly graph + sequence DL): **DynGN** (graph-conv + GRU encoder-decoder) beats classical predictors and resists noise; **EvolveGCN + KKT-trained DMPC** for interaction-free near-optimal control; transformer/graph-attention encoder-decoder validated on infrared swarm + ETH/UCY pedestrian data; **LSTM** for swarm intention/early-warning in air defense.
- **Counter-swarm / anti-drone** (defensive): distributed **auction-based** target allocation under low comms; **ODCDM** offense-defense decision-making with **consensus-based auction (CBAA)** + social-force mobility; optimal **air-defense placement** via evolutionary algorithms; "**loyal wingman**" human-AI teaming. A swarm survives attrition by design ("if 10 drones attack and 7 are intercepted, 3 still succeed").
- **Swarm-intelligence metaheuristics** benchmarked: **PSO, ACO, ABC, FOA, Cuckoo Search, Grey Wolf Optimization, Elephant Herd Optimization, Salp Swarm, Monarch Butterfly** — for path planning and 6G/IoT network problems.
- **Robust guidance result:** a Markov-decision-process interacting-pattern controller steers **1000 drones at 99.95% route accuracy with only 5% "informed" agents**; validated on real Crazyflie micro-quadrotors.
- **LLM choreography:** **SwarmGPT** lets non-experts choreograph drone light shows from music via an LLM + an optimization-based safety filter; 200 drones in sim, 20 real.
- **Physics-regularized control: PRAC** embeds physical priors (equilibrium, stability, energy-dissipation) as regularizers in RBF neural networks via Lyapunov-guided constrained optimization.
- **Applications surveyed:** ISR/surveillance, environmental & flood monitoring, **drone light shows** (Intel records 100→500→2018 drones; Ehang 1000→1374, 2017), security/defense, **search-and-rescue**, emergency medical delivery.
- **Autonomy rationale (military):** removing the operator removes the swarm's single point of failure and speeds the OODA loop; raises the **lethal-autonomous-weapons** debate.
- **Stated research gap:** most solutions are simulation-only or limited to small uniform swarms; real-world resilience (comms failure, adversarial/environmental variance), joint comms-compute-energy optimization at scale, security/ethics/scalability frameworks, and explainable multi-agent RL under partial observability are all under-investigated.

## Entities mentioned
- Ravi Raj, Andrzej Kos — authors (UPC BarcelonaTech; AGH Kraków).
- Bonabeau, Dorigo, Theraulaz — *Swarm Intelligence: From Natural to Artificial Systems* (1999), cited foundational reference.
- Intel, Ehang — drone-light-show record holders.

## Concepts touched
- [Swarm intelligence](../concepts/robotics/swarm-intelligence.md) — the concept this source primarily anchors.
- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — the single-/multi-UAV autonomy framing this extends to the swarm level.
- [Flocking and boids](../concepts/alife/flocking-and-boids.md) — "emergent coordination" model behind the bio-inspired framing.

## Open questions
- Review is **citation-dense but light on its own benchmarks** — it characterizes the literature rather than re-evaluating it; per-method numbers (beyond the cited 99.95% / 1000-drone result) aren't independently verified here.
- Heavy **military/anti-drone** orientation; civilian-deployment resilience data is thinner.
- No treatment of how the surveyed DL predictors (DynGN, EvolveGCN) relate to the wiki's [world-model](../concepts/world-models/jepa.md) thread — both are learned-dynamics predictors, an unexplored bridge.
