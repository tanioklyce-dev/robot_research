---
title: Code world model
type: concept
created: 2026-10-07
updated: 2026-10-07
sources: 2
tags: [code-world-model, world-model, program-synthesis, llm, symbolic, model-based-planning, mcts, verifiability, partial-observability]
---

A **code world model (CWM)** is an environment model written as an executable program, typically by an LLM, rather than learned as network weights. It contains a state definition, legal-action enumeration, a transition function, chance and observation functions, reward and termination. A classical planner then searches inside it. The LLM's job changes from *choosing actions* to *inducing the rules from text and a few trajectories*. Since the result is code, every transition in the data becomes a pass/fail **unit test**.

> [!note] Name collision
> Meta FAIR's **CWM** ([arXiv 2510.02387](https://arxiv.org/abs/2510.02387), Sept 2025) is a 32B open-weights **LLM** trained on code-execution traces, a language model *of* code execution. It is not a code world model in this page's sense.

## How it works
1. **Collect** a few trajectories: [Lehrach et al.](../../sources/code-world-models-general-game-playing.md) use 5 random-play games.
2. **Synthesize** a program against a fixed API from the rules text plus the trajectories.
3. **Refine** by generating one unit test per observed transition and feeding failures (stack traces) back to the LLM. Either keep one running conversation, or keep a tree of candidate programs and pick which to repair by Thompson sampling (REx / WorldCoder).
4. **Plan** with MCTS (perfect information) or Information-Set MCTS (imperfect information) inside the program. Optionally, also have the LLM write a value function and a hidden-state sampler.

## Why it is interesting
- **The correctness check is exact.** A learned dynamics model is judged by a loss. A CWM is judged by the share of observed transitions it reproduces exactly, and 1.0 means it reproduces all of them. In the [functional taxonomy](world-model-functional-taxonomy.md) it is a **simulator** (it outputs state), and it is the only learned simulator in this wiki with a correctness check this strict.
- **Planning compute becomes playing strength.** If the model is right, more search approaches optimal play, which is not true of an LLM-as-policy. This is the "System 2" argument made concrete ([Lehrach et al. §4](../../sources/code-world-models-general-game-playing.md)).
- **Adapting to a new environment is cheap.** Perfect-information games, including two invented for the paper, were learned exactly in **2–17 LLM calls**.
- **Partial observability can be handled.** "Inference as code" means the LLM writes a sampler over hidden histories, and replaying a sample through the deterministic model checks it against the evidence. A sample that passes is guaranteed to be in the posterior's *support*. That is weaker than having the right [belief state](belief-states-and-mixed-states.md), but useful when posteriors are sparse.

## Where it fails
- **Procedural depth.** Gin rummy, with its multi-stage scoring, plateaus at about 0.75–0.78 transition accuracy after the full 500-call budget ([Lehrach et al.](../../sources/code-world-models-general-game-playing.md)).
- **Wrong models fail confidently.** The verifiability benefit holds only *"contingent on the correctness of the synthesized model."* When the model is wrong, the planner searches the wrong game, and the agent forfeits most Gin rummy games through moves its own model thinks are legal.
- **Accuracy per transition is not accuracy where it matters.** A Backgammon model with 0.9993 test accuracy still loses about 92% of games to search on the true rules. The paper does not explain this. One plausible cause is the dice distribution, which is the kind of error per-transition tests barely weigh.

## Relation to other approaches
- **[Code as policy](../agents/code-as-policy.md)** has the LLM write the *controller*. A CWM has it write the *model* and leaves control to search. The two are complementary, and the [compile-the-agent-out move](../agents/code-as-policy.md#explore-online-then-compile-the-agent-out-of-the-loop) on that page is the same instinct of turning reasoning into an inspectable artifact.
- **[Generalized planning in PDDL](../../sources/generalized-planning-pddl-llm-paper.md)** has the LLM write a *planner*, with the domain model given. A CWM writes the domain model and leaves planning to a generic algorithm. Both rely on a validator in the loop.
- **Latent world models** ([JEPA](jepa.md), [Dreamer](../../entities/dreamer.md)) sit at the opposite end: continuous, learned and unverifiable, but applicable to pixels and physics. The closed-deck CWM autoencoder makes the connection explicit. Its encoder is an inference program and its decoder is the CWM, and **the rules plus a required API do the anti-collapse work** that [SIGReg](sigreg.md) or EMA targets do for latent models ([anti-collapse lineage](../../syntheses/world-models/ssl-anti-collapse-lineage.md)).

## Current state

As of this ingest the wiki has one primary on CWMs: [Lehrach et al. 2025](../../sources/code-world-models-general-game-playing.md), which extends the method to two-player, stochastic and imperfect-information games. The prior work it builds on (WorldCoder, GIF-MCTS, POMDP Coder) is cited there but not ingested. Every demonstration so far uses **discrete, symbolic, exactly-ruled** environments. For robotics the plausible place for it is the **task layer**: object states, preconditions and effects, as in [symbolic task planning](../agents/symbolic-task-planning.md). Contact dynamics are not a plausible fit. No ingested source has tried this.

## Key references
- [Code World Models for General Game Playing (Lehrach et al., DeepMind 2025)](../../sources/code-world-models-general-game-playing.md)

## Related concepts
- [World model](world-model.md) · [World-model functional taxonomy](world-model-functional-taxonomy.md) · [World-model evaluation](world-model-evaluation.md)
- [Belief states and mixed states](belief-states-and-mixed-states.md)
- [Code as policy](../agents/code-as-policy.md) · [Symbolic task planning](../agents/symbolic-task-planning.md)

## Mentioned in
- [Code World Models for General Game Playing](../../sources/code-world-models-general-game-playing.md)
- [Generalized Planning in PDDL Domains with Pretrained LLMs](../../sources/generalized-planning-pddl-llm-paper.md): the planner-writing sibling.
