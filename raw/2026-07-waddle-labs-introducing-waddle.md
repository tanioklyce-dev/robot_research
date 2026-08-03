# Introducing Waddle: agents that control robots

**Source:** Waddle Labs Blog — https://waddlelabs.ai/research/introducing-waddle
**Author:** Waddle Team
**Published:** July 2026

---

## Problems with the current approach

Robot learning has largely converged on a single recipe: collect large datasets[1] and train an end-to-end model, such as a VLA[2] or a world action model (WAM)[3], to map camera frames and an instruction directly to motor commands. The results are impressive: the best current models fold laundry and clear tables[4], and they continue to improve.

But the recipe has problems:

1. It relies on huge amounts of robot data.
2. The models are difficult to steer.
3. They do not yet generalize across embodiments and environments.

These properties make large robot models difficult to deploy: adapting one to a new robot, a new workspace, or a new task typically means collecting data and finetuning. The abundance of applications built on top of LLMs is not yet seen in robotics.

## Our hypothesis

None of these problems is intrinsic to large models in general. LLMs train on data that already exists at internet scale, are steered by conversation, and transfer to new domains without finetuning.

LLMs are also uniquely capable of tool use, reasoning, and writing programs[5]. Our hypothesis is that these capabilities can be transferred into robotics by using LLM agents to control robots[6][7].

> **Fig. 1** — Left: the current robot learning pipeline, in which an action model maps instructions directly to actions. Right: the stack we propose, in which an agent uses code as policy while retaining the ability to call action models as tools.
> - Left pipeline: Instructions → Action model (e.g. VLAs, WAMs) → actions → Robot
> - Right pipeline: Instructions → Agent (code as actions) → subtask → Action model → actions → Robot

Our agents decompose goals into subtasks, and complete each one by viewing camera feeds, writing control code, and calling models like VLAs. The agent outputs a program that you can run and iterate on by talking to our agents.

## Capabilities

Because our agent is an LLM agent, it inherits the properties of the underlying model. We highlight three, each demonstrated on real hardware.

### Generalist

LLMs are inherently generalist. Our agents work with any arms, grippers, and camera setups without new data collection.

### Long-horizon planning

Planning is done by the reasoning model, not the policy. The agent decomposes long tasks into stages, verifies intermediate outcomes, and re-plans on failure.

### Multi-agent coordination

Controlling more robots does not require changes to the system. For Waddle, you simply hook up more agents: a master agent spawns subagents and coordinates multiple robots working concurrently. The same structure carries from a pair of arms to a fleet.

## Use cases

We highlight three use cases of the Waddle agent API.

- **Create a working policy in 20 minutes.** "Write a program to place one microswitch inside each slot"
- **Generate data for model training.** "Pick and place lego bricks at random positions 1000 times" — We asked our agent to collect data of picking and placing LEGO bricks at a variety of positions and orientations. The agent repeated this around a thousand times overnight and autonomously trained an ACT policy from scratch that could pick up LEGOs.
- **Facilitate robotics auto-research.** "I am tuning a policy overnight. Reset the scene after each trial"

## Our research

### Related work

Waddle builds on the code-as-policy line. Code as Policies[6] showed that language models can write executable robot programs, and successors had the model write value maps[8] or reward functions[9] for downstream optimizers; other systems instead use the model to map observations directly to motor commands[2][4] or to select which pretrained skill to run next[7][10]. In the code-writing line, the program was generated once per instruction, and revision, where it existed, came from human corrections[11] or from domains where trials are cheap, games[12] and software[5]. The most recent work closes the loop autonomously: CaP-X[13] benchmarks multi-turn coding agents that revise against execution feedback on real embodiments, and ASPIRE[14] pairs failure diagnosis and repair with a growing skill library, following the pattern Voyager[12] introduced in Minecraft. We see this convergence as evidence that code-as-policy has become viable as a path towards robot intelligence. Waddle runs the loop as a deployed system: robots connect through our API, agents run against them continuously, and every solved task adds skills to a library shared by all agents. Programs compose, and nothing retrains between tasks.

### A library of skills

The programs our agents write are not monolithic. Our agents continuously learn by creating then refining parametrized skills. These skills include grasping, aligning, or folding. Skills occupy the middle level of a hierarchy: programs are composed of skills, and skills are composed of a fixed set of primitives provided by the platform (Fig. 2).

> **Fig. 2** — Primitives compose into skills; skills compose into the program the agent writes for the task. The skill `fold_grasp` collapses into a single call at its exact use site.
>
> **PRIMITIVES** — Fixed vocabulary provided by the platform.
> - `bounding_box(·)` — perception: text query → box in frame
> - `detect_in_base(·)` — box → point in robot base frame
> - `approach_until(·)` — waypoints + stop criterion → trajectory
> - `reset_home(·)` — scene reset
>
> **SKILLS** — Created and refined by agents; shared in the library.
> - `servo_align(·)`, `orbit_view(·)`, `top_grasp(·)` … grows with every task
> - Example skill `fold_grasp`:
> ```python
> def fold_grasp(anchor):
>     box   = bounding_box(anchor)
>     point = detect_in_base(box)
>     wps   = preset("low sweep", at=point)
>     traj  = approach_until(wps, until="contact")
>     return traj
> ```
>
> **PROGRAM** — Written by the agent, per task — composed of skills. Example `fold_tshirt.py`:
> ```python
> # task: "fold the t-shirt and place it to the side"
> parallel(left, right):
>     traj = fold_grasp(anchor=f"{arm} sleeve")
>     robot[arm].execute(traj)
> barrier()
> fold_over(axis="midline", hold="left cuff")
> verify("sleeves folded")
> ...
> ```

Skills transfer across tasks. Our agent first created the `fold_grasp` skill when attempting to flip over a package. Then, another agent adapted this skill to fold a t-shirt (Fig. 3).

> **Fig. 3** — One parametrized skill, `fold_grasp`, reused across three tasks: flip the package, fold the towel, fold the shirt.

This skill library allows agents to learn from experience and learn from each other. We expect skills to drastically improve agents' ability to achieve new tasks as more agents become deployed.

### Scaling with foundation models

The skill library is one axis along which the system improves. The underlying foundation models are another. As foundation models improve, our agents will accomplish harder tasks. We evaluated three LLMs (Opus 4.8, Fable 5, and GPT 5.6 Sol) across a suite of manipulation tasks and observe a consistent trend: larger models, given larger budgets, produce better policies. All models were capable of achieving easy tasks, such as "pick up the lego", but only Fable 5 and GPT 5.6 with xhigh thinking accomplished harder tasks like "fold the t-shirt".

> **Fig. 4** — Average success rate across our manipulation task suite vs. cost per task. Bold curves: xhigh thinking; light curves: high thinking. Line chart across Opus 4.8, Fable 5, and GPT 5.6 Sol at high and xhigh thinking budgets: success rises with budget, and larger models reach higher plateaus.

## Next steps

- **Tools that agents prefer.** Agent performance depends heavily on the interfaces agents are given. VIA[15] shows that frontier models can control robots through purely visual interfaces, and Claude Plays Robotics[16] reports that adding a movable cursor the model could query for position and depth raised success on a manipulation suite from 6% to 32%. We will continue to work on designing tools that allow LLMs to best control robots.
- **Benchmarks and standardized evaluation.** Results in this area are difficult to compare: tasks, robots, and success criteria differ across labs. A shared benchmark for agent-controlled robots, with common tasks and success criteria, would make results comparable across systems.
- **Training more capable agents.** We have been using agents to control robots for the last six months, generating large amounts of data and intervention traces. We plan to use this data to train LLMs that excel at performing physical tasks.

## Our goal

We believe every robot will be directed by its own agent, and that we will collaborate with robots by communicating with their agents. There will be a billion robots. Our mission is to enable everyone to take part in building that future.

Request early access →

## References

- [1] Open X-Embodiment Collaboration. *Open X-Embodiment: Robotic Learning Datasets and RT-X Models.* arXiv:2310.08864, 2023.
- [2] A. Brohan et al. *RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control.* arXiv:2307.15818, 2023.
- [3] *World Action Models: The Next Frontier in Embodied AI.* arXiv:2605.12090, 2026.
- [4] K. Black et al. *π0: A Vision-Language-Action Flow Model for General Robot Control.* arXiv:2410.24164, 2024.
- [5] X. Wang et al. *Executable Code Actions Elicit Better LLM Agents.* arXiv:2402.01030, 2024.
- [6] J. Liang et al. *Code as Policies: Language Model Programs for Embodied Control.* ICRA 2023. arXiv:2209.07753.
- [7] M. Ahn et al. *Do As I Can, Not As I Say: Grounding Language in Robotic Affordances.* CoRL 2022. arXiv:2204.01691.
- [8] W. Huang et al. *VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models.* CoRL 2023. arXiv:2307.05973.
- [9] W. Yu et al. *Language to Rewards for Robotic Skill Synthesis.* CoRL 2023. arXiv:2306.08647.
- [10] W. Huang et al. *Inner Monologue: Embodied Reasoning through Planning with Language Models.* CoRL 2022. arXiv:2207.05608.
- [11] L. Zha et al. *Distilling and Retrieving Generalizable Knowledge for Robot Manipulation via Language Corrections.* arXiv:2311.10678, 2023.
- [12] G. Wang et al. *Voyager: An Open-Ended Embodied Agent with Large Language Models.* arXiv:2305.16291, 2023.
- [13] Fu et al. *CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation.* arXiv:2603.22435, 2026.
- [14] Lu et al. *ASPIRE: Agentic Skills Discovery for Robotics.* arXiv:2607.00272, 2026.
- [15] H. Hu et al. *VIA: Visual Interface Agent for Robot Control.* arXiv:2607.11119, 2026.
- [16] Anthropic. *Claude Plays Robotics.* anthropic.com/research/claude-plays-robotics, 2026.

## Citation

Waddle Team, "Introducing Waddle: Agents that Control Robots", Waddle Labs Blog, Jul 2026.

```bibtex
@article{waddle2026introducing,
  author = {Waddle Team},
  title = {Introducing Waddle: Agents that Control Robots},
  journal = {Waddle Labs Blog},
  year = {2026},
  note = {https://waddlelabs.ai/research/introducing-waddle},
}
```
