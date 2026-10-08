---
title: "Code World Models for General Game Playing (Lehrach et al., Google DeepMind, 2025)"
type: source
url: https://arxiv.org/abs/2510.04542
local_path: raw/2510.04542v1.pdf
sha256: 03ab77dca2b96d3cfa38edb605bb78721e16cbc5159391fdf07ff8b6bf696982
author: Wolfgang Lehrach, Daniel Hennes, Miguel Lázaro-Gredilla (equal contribution), Xinghua Lou, Carter Wendelken, Zun Li, Antoine Dedieu, Jordi Grau-Moya, Marc Lanctot, Atil Iscen, John Schultz, Marcus Chiam, Ian Gemp, Piotr Zielinski, Satinder Singh, Kevin P. Murphy (Google DeepMind)
published: 2025-10-06
ingested: 2026-10-07
venue: arXiv preprint 2510.04542v1 (cs.AI), 15 pp. main + appendices
tags: [code-world-model, world-model, program-synthesis, llm, mcts, ismcts, imperfect-information, partial-observability, belief-state, openspiel, game-playing, gemini, model-based-planning, deepmind]
---

# Code World Models for General Game Playing

> [!note] Not Meta's "CWM"
> Meta FAIR released a 32B open-weights LLM called **CWM ("Code World Model")** in the same month ([arXiv 2510.02387](https://arxiv.org/abs/2510.02387)). That is a *language model trained on code-execution traces*. This paper's CWM is a *Python program* that an LLM writes to simulate a game. They are unrelated. The wiki uses [code world model](../concepts/world-models/code-world-model.md) for this paper's sense.

## Summary

Instead of asking an LLM to **pick moves**, ask it to **write the game**. Given a game's rules as text and **5 random-play trajectories**, Gemini 2.5 Pro writes a Python implementation of the game against the [OpenSpiel](https://github.com/google-deepmind/open_spiel) API, covering state, legal moves, transitions, chance, observations, reward and termination. Unit tests generated from the trajectories check every transition, and failures are fed back for **iterative refinement**. The refinement either continues one conversation or runs a Thompson-sampled tree of candidate programs, as in REx/WorldCoder. A classical planner, MCTS or Information-Set MCTS, then plays inside the synthesized model. The paper's additions over prior code-world-model work are:
- two-player strategic games;
- **LLM-written value functions** to speed up search;
- **"inference as code"**: LLM-written samplers over hidden histories, for imperfect-information games;
- a **"closed deck" setting**, where hidden state is never revealed even in hindsight. Here the inference function (encoder) and the code world model (decoder) are trained as an **autoencoder regularized by the game rules and the API**.

Across 10 games, 4 of them new and invented for the paper, the agent **"outperforms or matches Gemini 2.5 Pro in 9 out of 10."** The appendix tables qualify that claim substantially; see below.

## Key claims

**Method (§4)**
- An episode starts with **random play to completion**. The agent synthesizes the model offline before playing, and does not update it during play (fn. 2).
- Transition accuracy is the pass rate of binary unit tests from offline trajectories. Refinement stops at 1.0 or when the budget runs out. **Tree search beats conversation** on accuracy and call count, and is used from §5.1.1 on.
- **Hidden-history inference** (§4.2): the LLM writes a sampler h̃ₜ ~ p(hₜ | own obs, own actions). Because all model functions are deterministic, replaying h̃ₜ through the model checks it against the evidence. Passing every test guarantees h̃ₜ is **in the posterior's support**, not that it is correctly distributed: *"the correct support is already very informative, given the extremely sparse support of state posteriors in games."* The alternative, direct *hidden-state* inference, is simpler but cannot guarantee valid or consistent states.
- **Value functions** (§4.3) are not refined, because there is no ground truth for them. Several are generated and the best is chosen by tournament. They helped only in Generalized tic-tac-toe and Bargaining (App. C.4).
- **Closed deck** (§4.4): drop every unit test that needs hidden information and keep only observation → latent history → observation reconstruction, plus checks that random play raises no execution errors. *"Instead of a bottleneck, or a regularization term, the game rules and the required OpenSpiel API… act as regularizers to prevent trivial latent spaces from being discovered."* A valid h̃ gives a likelihood lower bound p(o) ≥ p(h̃).
- **Bad-sample rejection** (App. E): for imperfect-information games, 5 models are synthesized and their agents play a round-robin **inside each other's models** (2 hosts × 5 × 5, 50 repeats). Any agent worse than the best by more than 10% of the utility range is rejected.

**Synthesis accuracy (§5.1, Tables 1, 2, 4)**
- **Perfect information: all five games learned exactly** (train transition accuracy 1.0, test ≥ 0.9993), in **2–17 LLM calls**. Generalized chess, an invented variant with 5,555 actions, takes 5.2 calls.
- **Imperfect information, open deck:** four games are near-perfect. **Gin rummy is the failure**: transition accuracy 0.78 train / 0.75 test, inference accuracy 0.59 / 0.54, with the full **500-call** budget used. The authors attribute this to its multi-stage scoring procedure (knock, lay off, deadwood, undercut).
- **Closed deck:** degraded. Bargaining test inference accuracy is 0.67. **Gin rummy train inference accuracy is 0.055**.

**Arena results (§5.2, App. C.2)**, from 100 matches per setting against Gemini 2.5 Pro used as a policy, against GT-(IS)MCTS (MCTS on the true game code) and against Random. All agents get the rules and 5 trajectories. (IS)MCTS runs 1,000 simulations per move.
- Perfect information: CWM-MCTS **beats Gemini in all five games** and *"Both agents are similarly good, without either of them clearly winning"* against GT-MCTS.
- Imperfect information: it beats or matches Gemini in all games except **Hand of war** (open deck). In closed deck, *"continues to beat or match"* Gemini.
- A PPO policy trained for 10M steps *inside* the learned model also beats or matches Gemini everywhere it was run (App. D). It was not run on Gin rummy.

## What the appendix tables show

> [!warning] Much of the margin over Gemini is forfeits, not play
> The arena does **not** show agents the legal-action list (App. C.2). An illegal move forfeits the game. Table 7 counts wins by forfeit separately:
> - **Backgammon: 100/100 wins in each seat, all by Gemini forfeiting.**
> - **Generalized chess: 92/100 and 97/100 by forfeit.**
> - Connect four: 2/100 and 1/100 by forfeit, so this one is a genuine win.
> - Tic-tac-toe: 95–100% draws.
> - **Gin rummy: Gemini forfeits 99–100% of games** (Table 14). The authors concede the result *"should be interpreted as Gemini 2.5Pro being a very weak player."*
>
> So in two of the five perfect-information games, Gemini's strategy is never tested, and what is measured is whether a prompted LLM can keep track of legality. That still supports the paper's **verifiability** argument, which is legality by construction. It does not support the **strategic depth** argument in those games. A baseline that gave Gemini the legal-move list would separate the two.

> [!warning] Internal inconsistency — "similarly good" vs. ground truth
> §5.2.1 says CWM-MCTS and GT-MCTS are similarly good *"without either of them clearly winning in any of the games."* Table 7 has **Backgammon at 0.08 W / 0.92 L and 0.07 / 0.93**. The CWM agent loses about 92% of games to search on the true rules, despite 0.9993 test transition accuracy. The other games are roughly even once first-mover advantage is accounted for (Connect four 0.69 / 0.28; Generalized tic-tac-toe 0.88 / 0.37). The paper does not discuss the Backgammon gap. A plausible cause is an error in the chance-node distribution (dice), which per-transition accuracy would barely register but which biases every rollout. That is this wiki's reading, not the paper's.

> [!note] Verifiability is conditional, and Gin rummy shows the failure
> The abstract hedges correctly: illegal moves are avoided *"contingent on the correctness of the synthesized model."* When the model is wrong, the agent loses that protection. In Gin rummy **the CWM agent itself forfeits 94% of games against GT-ISMCTS** (Table 14, open deck), and **97–99% against Random in closed deck** (Table 16). A wrong world model is worse than none: the planner confidently searches a game that is not the one being played.

## Entities mentioned
- [Google DeepMind](../entities/google-deepmind.md): all authors.
- Gemini 2.5 Pro: both the synthesizer and the baseline. No entity page; see [Gemini Robotics](../entities/gemini-robotics.md) for the robotics line.
- OpenSpiel (DeepMind's game framework), WorldCoder, GIF-MCTS, POMDP Coder: cited prior work, not filed.

## Concepts touched
- [Code world model](../concepts/world-models/code-world-model.md): new concept page, seeded by this paper.
- [World model](../concepts/world-models/world-model.md) · [World-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md): a CWM is a *simulator* in the taxonomy's terms (it outputs state) and can be checked against data.
- [Code as policy](../concepts/agents/code-as-policy.md): the paper inverts it. The LLM writes the *model*, and search supplies the policy.
- [Belief states and mixed states](../concepts/world-models/belief-states-and-mixed-states.md): inference-as-code guarantees posterior *support*, not posterior *weights*.
- [Generalized planning in PDDL with LLMs](generalized-planning-pddl-llm-paper.md): the sibling move, where the LLM writes a *planner* program and a validator debugs it.
- [SIGReg](../concepts/world-models/sigreg.md) / [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md): the closed-deck autoencoder's regularizer is symbolic, namely the rules plus a required API, not statistical.

## Open questions
- **The Gemini baseline without legality failures.** Rerun with the legal-action list given to the LLM policy. The perfect-information margins in Backgammon and Generalized chess are currently unmeasured.
- **Backgammon vs. GT-MCTS.** Why does a model with 0.9993 test transition accuracy lose about 92% of games to the true model? Is it the chance distribution? Per-transition unit tests weight a rare wrong dice probability no more than a correct move.
- **Where the method stops.** Gin rummy is the only game with procedural depth and it fails at a 500-call budget. Is the ceiling program length, the number of trajectories (5), or the absence of active data collection, which §6 names as future work?
- **Relevance to robotics.** Every game here has discrete actions, symbolic state and exact rules. A robot's world has none of these, but a robot *task layer* often does (PDDL-style object states, [behavior trees](../concepts/robotics/behavior-trees.md)). Is the transferable part the whole method or only the refinement loop?
