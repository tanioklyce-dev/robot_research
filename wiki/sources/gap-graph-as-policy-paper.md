---
title: "GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness for Variational Automation Tasks"
type: source
url: https://arxiv.org/abs/2607.05369
local_path: raw/gap-2607.05369v3.pdf
sha256: 05c3ed141a9dfef2913f9bc59477116d9d082460d725510ff8db82863811ac80
author: "Kaiyuan Chen, Shuangyu Xie, Letian Fu, Justin Yu et al.; senior authors include Yuke Zhu, Linxi 'Jim' Fan, Ken Goldberg"
affiliations: "UC Berkeley, NVIDIA, Bosch"
published: 2026-07-06
venue: "CoRL 2026 (spotlight, per project page); arXiv v3, 2026-11-04"
format: paper (53 pp; 12 pp body + appendices) plus project page
arxiv: 2607.05369
project_page: https://graph-robots.github.io/gap/
code: https://github.com/graph-robots/gap
tags: [graph-as-policy, gap, variational-automation, code-as-policy, agentic-robotics, multi-agent, morsl, self-learning, simulation-rehearsal, libero-pro, tamp, ros, benchmark]
ingested: 2026-11-09
---

# GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness for Variational Automation Tasks

## Summary

[Graph-as-Policy](../entities/graph-as-policy.md) has coding agents write a robot policy as a typed, directed graph of skill nodes, then improve it by rehearsing in a simulator built from known object meshes. No agent runs on the robot after deployment.

The paper also names a task class, [variational automation](../concepts/robotics/variational-automation.md): repeated work in a known workcell where objects vary within a known range. It is narrower than generalist robotics and broader than fixed automation.

GaP holds 0.93–0.99 success under pose variation in simulation, and matches an expert hand-built graph on a crate-washing task (0.953 vs 0.987). The result is strong for the setting it defines. **That setting supplies the object meshes and pose ranges, and the learned-policy baselines weren't trained on the varied distribution.** So the comparison shows the value of knowing the geometry, more than it shows graphs beating VLAs in general.

## Key claims

### Method (Sec. 3–4)

- **Task input.** Language, a fixed workcell, robot and camera specs, an object set with 3D models, and a distribution of poses. The authors call these part of the task, not oracle information. The simulator is built directly from them, *"without scene reconstruction, system identification, or domain randomization."*
- **Graph.** Nodes are typed operations such as a camera read, a perception call or a motion plan. Edges carry data or control. A static type check runs before execution.
- **Agents.** An orchestrator splits the task into segments and skill agents write sub-graphs. The separation limits context size and, the authors argue, reduces the incentive to "cheat."
- **MORSL.** A library of 51 skills, using agent-readable conventions such as Skill.md: 15 perception, 5 grasp planning, 8 motion planning, 15 vision utilities and 8 verification or control primitives.
- **Self-learning.** Parallel rehearsals record state before and after each node and contact queries localise failures to nodes. Agents may set inputs, rewire, rewrite inline scripts or swap skills. Updates that degrade success or cycle time on 100 fresh instances are rejected.
- **LLM.** Gemini-3.1-Flash-Lite at temperature 0.1 for the reported runs.
- **Cost.** Fewer than 30 LLM calls per graph, *"about $0.01 and 1 s latency"* (the paper doesn't say whether that is per call or per graph). Self-learning takes about 15 minutes per iteration, up to 150 minutes for Make Popcorn.

### Results

Simulation, 100 task instances per cell (Table 1):

| Method | LIBERO | LIBERO-Pro swap | X-Y 20×20 cm | Basket swap | Permutation | Mixed | Pack fixed | Pack varied |
|---|---|---|---|---|---|---|---|---|
| CaP-X | — | 0.22 | 0.07 | 0.05 | 0.11 | 0.10 | 0.01 | 0.01 |
| π0.5 | 0.96 | 0.24 | 0.78 | 0.15 | 0.20 | 0.20 | 0.17 | 0.18 |
| MolmoAct2 | 0.97 | 0.43 | 0.90 | 0.26 | 0.10 | 0.20 | 0.18 | 0.18 |
| TiPToP | 0.22 | 0.22 | 0.29 | 0.24 | 0.31 | 0.24 | 0.34 | 0.46 |
| π0.5 with GaP staging | 0.85 | 0.60 | 0.79 | 0.32 | 0.50 | 0.39 | 0.67 | 0.66 |
| MolmoAct2 with GaP staging | 0.70 | 0.62 | 0.84 | 0.58 | 0.39 | 0.66 | 0.59 | 0.59 |
| **GaP** | 0.95 | 0.95 | 0.95 | 0.97 | 0.93 | 0.97 | 0.99 | 0.98 |

Real robot (Tables 2, 4):

| Task | GaP | TiPToP |
|---|---|---|
| Fulfil grocery orders | 25/25 | 8/25 |
| Pack grocery items | 28/30 | 10/30 |
| Make popcorn, after self-learning | 18/20 | 0/20 |
| USB-C insertion, 130 trials | 121/130 | Not tested |

Wash Crates in simulation over 150 trials: GaP 0.953 at 179 s per cycle, expert hand-built graph 0.987 at 176 s.

- **Self-learning.** Make Popcorn goes from 33% to 94% in simulation over 10 iterations. A separate throughput run cuts cycle time by up to 57%. Grocery benchmarks skip self-learning because the first graph already scores high.
- **Ablations.** A single LLM emitting raw Python, or one LLM doing all agents' jobs, scores **zero**. Failures are interface mismatches and failed structural checks.

### Limitations

**Stated by the authors.** Reliability isn't at industry level. Execution is well short of the 500 units per hour standard. Benchmarks are quasi-static pick-and-place, and only cable insertion uses force. Deformables, dynamics and moving targets are future work.

**Noted at ingest.**

- **No VLA ran on the real robot.** The only real-robot baseline is TiPToP.
- **The VLAs were trained on LIBERO's narrow distribution** and tested on wider ones. Nobody fine-tuned them on the varied data GaP's simulator could generate.
- **CaP-X is admitted to be unfair.** The authors say so, because it gets only an image and instructions and no geometry. It serves as an ablation.
- **The two zero ablations are structural.** They show that free-form code fails against these low-level service interfaces, not that a good API would fail.

> [!warning] Contradiction: project page vs paper on speed
> The [project page](https://graph-robots.github.io/gap/) says *"cycle times remain below the ~7 s/instance industrial standard."* The [paper](https://arxiv.org/abs/2607.05369) says execution times *"are still well below industry standards of 500 units per hour (7 seconds per instance)."* The measured pick-and-place average is 67 s on the real robot, so the cycle takes far longer than 7 s. The page's wording reads backwards. Use the paper's.

## Project page

The [page](https://graph-robots.github.io/gap/) matches the paper's tables where checked. It adds links to the [code](https://github.com/graph-robots/gap) and the skill library. NVIDIA's [CoRL post](nvidia-corl-2026-robotics-simulation-blog.md) says Ambi Robotics, Bosch Research and Siemens are exploring it.

## Entities mentioned

- [Graph-as-Policy](../entities/graph-as-policy.md), [Ken Goldberg](../entities/ken-goldberg.md), [Jim Fan](../entities/jim-fan.md), [Yuke Zhu](../entities/yuke-zhu.md), [NVIDIA GEAR](../entities/nvidia-gear.md)
- [CaP-X](../entities/cap-x.md), [π0.5](../entities/pi-zero-5.md), [MolmoAct2](../entities/molmoact2.md), [GraspGen](../entities/graspgen.md), [cuRobo](../entities/curobo.md), [LIBERO](../entities/libero.md)

## Concepts touched

- [Variational automation](../concepts/robotics/variational-automation.md) — the task class this paper names.
- [Code as policy](../concepts/agents/code-as-policy.md) — constrains the generated program to a typed graph, and reports a cost figure.

## Open questions

- **Does the advantage survive when VLAs are fine-tuned on the varied distribution?** That test is cheap here, because the simulator already generates the variation.
- **How much mesh quality does it need?** Every result assumes accurate models. Off-model objects aren't tested.
- **Does the graph structure, or the skill library, carry the result?** TiPToP improves from 0.24 to 0.53 on groceries just by adopting MORSL perception and grasping (Table 3).
- **How does VABAR relate to these eight benchmarks?** NVIDIA's post announces a six-task benchmark under the same name family, without saying.
