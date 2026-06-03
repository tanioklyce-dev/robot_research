---
title: Artificial life and the emergence of self-replication
type: concept
created: 2026-05-31
updated: 2026-06-02
sources: 17
tags: [artificial-life, alife, self-replication, origins-of-life, emergence, complexity, open-endedness, kolmogorov-complexity, cellular-automata, game-of-life, flocking, boids]
---

**Artificial Life (ALife)** studies "life as it could be" — the general principles of living/complex systems abstracted away from biochemistry. A central question: **how does self-replication, and then open-ended complexity, arise from non-living "pre-life" dynamics?** This concept page anchors the wiki's ALife / emergence / complexity branch.

## Core finding (this wiki's anchor source)
[**"Computational Life" (Agüera y Arcas et al., 2024)**](../../sources/computational-life-self-replicating-programs-paper.md): in a soup of **random, interacting, self-modifying programs with no fitness function and no selection**, **self-replicators reliably emerge on their own**, triggering a sharp **pre-life → life state transition** after which complexity keeps increasing. Key points:
- **No objective required.** Replication is not selected for — it arises from random interaction + self-modification (with or without background mutation). This is the striking part: complexity without a designed reward.
- **Substrate-general.** Shown in **BFF** (an extended Brainfuck where programs share one read/write tape), **Forth**, and **real CPU instruction sets** (Zilog **Z80**, Intel **8080**) — not just toy languages.
- **A counterexample bounds the claim.** In **SUBLEQ** (a one-instruction set) spontaneous emergence is **not** observed, and the shortest hand-crafted self-replicator is much longer — implicating **reachability of short replicators under random self-modification** as the gating condition.
- **Independently reproduced.** [Jonas Werner's BFF reproduction (2026)](../../sources/jonas-werner-bff-emergent-complexity.md) reimplements the BFF soup from scratch (C+OpenMP) and confirms the spontaneous-replicator result and its sharp phase transition (he calls it **"gelation"**) — operations/interaction jumping ~700→6,000–12,000 as diversity collapses — on a commodity desktop in minutes, on multiple random seeds.

## Mechanism
The enabling ingredient is a **shared read/write substrate**: when randomly paired programs are concatenated and executed on a common tape, one program can rewrite another. Self-modification + this shared medium make self-replicating motifs reachable by random walk; once a replicator appears it spreads and **takes over the soup** (the "life" phase). Setup follows an isolated-system variant of **Fontana's Turing gas**.

## Detecting the transition — "high-order entropy"
The paper introduces **high-order entropy** = (Shannon entropy over tokens/bytes) − (**normalized Kolmogorov complexity**, i.e. Kolmogorov complexity ÷ length). Together with **tracer tokens**, it flags the state transition as a **collapse in unique tokens** and dominance by a few motifs — a quantitative signature of emergent order distinct from raw entropy.

## Why it matters
- A concrete, reproducible demonstration that **self-replication and rising complexity are generic outcomes** of simple interacting computation — relevant to Origins-of-Life debates and to "life as it could be."
- **Connects to the wiki's intelligence-paradigms thread.** It's the [Paradigms of Intelligence](../../entities/blaise-aguera-y-arcas.md) view: intelligence/life as **emergent from simple interaction**, a complement to [LeCun](../../entities/yann-lecun.md)'s world-models bet and [Michael I. Jordan](../../entities/michael-i-jordan.md)'s collectivist/economic view — see [critiques of the intelligence north star](../../syntheses/society/critiques-of-the-intelligence-north-star.md).
- **Methodological echo of [JEPA](../world-models/jepa.md)**: both get useful structure *without a hand-designed objective* — JEPA predicts in latent space instead of reconstructing pixels; this gets complexity with **no fitness function at all**.

## Self-replication in *living matter* — Xenobots
The wiki's code-substrate results have a striking **biological counterpart**. [Xenobots ("reconfigurable organisms")](../../entities/xenobots.md), built from frog (*Xenopus*) stem cells, exhibit **kinematic self-replication**: swarms push loose dissociated cells into piles that mature into new motile organisms ([Kriegman et al. 2021](../../sources/kriegman-2021-kinematic-self-replication.md)). Like the Computational Life soup, this replication **arises spontaneously, without selection or genetic engineering** — though here AI ([evolutionary computation](evolutionary-computation.md)) is used only to *amplify* it (the C-shaped semitorus triples replication rounds), not to originate it. The organisms themselves are **AI-designed in silico, built in vivo** ([Kriegman et al. 2020](../../sources/kriegman-2020-reconfigurable-organisms.md)).

> [!note] Two senses of "self-replication without selection"
> Both [Computational Life](../../sources/computational-life-self-replicating-programs-paper.md) (self-modifying code) and [Xenobots](../../sources/kriegman-2021-kinematic-self-replication.md) (frog cells) get replication with **no designed fitness function** — but via very different mechanisms (random self-modification on a shared tape vs. ciliary mechanics aggregating feedstock). A genuine cross-substrate parallel, not the same phenomenon.

## Related concepts
- **Synthesis:** [Local rules, global complexity: learned vs. evolved vs. emergent self-organization](../../syntheses/alife/local-rules-global-complexity.md) — the cross-cutting analysis of this whole branch (the "where does the local rule come from / what information becomes structure?" spectrum).
- [Neural Cellular Automata](neural-cellular-automata.md) — the learnable self-organization wing.
- [Evolutionary computation](evolutionary-computation.md) — gradient-free population search; the design engine behind Xenobots; a classic ALife tool.
- [Flocking and boids](flocking-and-boids.md) — sibling emergence model (continuous steering substrate).
- [JEPA](../world-models/jepa.md) — objective-light learning (different domain, same anti-hand-design spirit).
- [Cellular automata](cellular-automata.md) — the foundational substrate of this whole branch (now covered): grid + local rule → emergent global structure. [Conway's Game of Life](../../entities/game-of-life.md) is the canonical 2D CA; [NCA](neural-cellular-automata.md) is the learned-rule descendant.
- [Neural Cellular Automata](neural-cellular-automata.md) — the **learnable** self-organization sibling (learned local rule → morphogenesis); now covered.
- **Open-ended evolution** — substantially covered via [Tierra](../../entities/tierra.md) & [Avida](../../entities/avida.md) (see lineage below).

### Programming games
A related tradition: **programming games** where you write code for an autonomous agent and then watch it run unattended.
- **[Core War](../../entities/core-war.md)** ([Dewdney, 1984](../../sources/dewdney-1984-core-war-scientific-american.md)) is the **self-replication-relevant** member: Redcode "warriors" battle in a shared circular memory, and its canonical warrior — the **Imp** (`MOV 0 1`) — is a one-instruction program that **copies itself through memory**. Hand-written replicators, run on the [pMARS](../../sources/pmars-koth.md) simulator.
- **[CRobots](../../sources/crobots-github.md)** (Poindexter, 1985) is the **non-replicating** cousin — C-programmed battle robots in an instruction-limited VM; hand-coded and static.

### The digital-replicator lineage (now ingested end-to-end)
These hand-written replicators sit one step before **evolved/emergent** ones. The full chain:

**von Neumann**'s self-replicating-machine theory → **[Darwin](../../sources/darwin-1961-bell-labs-game.md)** (Bell Labs, 1961 — earliest digital-organism arena; *adapts within a round* but doesn't evolve code) → **[Core War](../../entities/core-war.md)** (1984 — hand-written self-replicating warriors, *no evolution*) → **[Tierra](../../entities/tierra.md)** ([Ray, 1991](../../sources/ray-1991-tierra-synthesis-of-life.md)) & **[Avida](../../entities/avida.md)** ([Adami & Brown, 1994](../../sources/adami-brown-1994-avida.md)) — *open-ended evolution from a hand-written ancestor*, with a whole ecology (parasites, hyper-parasites, sociality, cheaters) emerging → **[Computational Life / BFF](../../sources/computational-life-self-replicating-programs-paper.md)** (2024) — replicators that *emerge from random code with no ancestor and no fitness function at all*.

The chain has a clear **"how much is designed in?" gradient**: Core War (designed replicator, no evolution) → Tierra/Avida (designed *ancestor* + selection → evolution; Avida even rewards specified tasks) → Computational Life (nothing designed — no ancestor, no fitness, replication *and* its rise are emergent). Tierra→Avida itself trades Tierra's **global reaper** (which homogenizes the soup) for **local, cellular-automaton-style** interaction that sustains diversity.

**Evolution of complexity (the Avida capstone).** [Lenski, Ofria, Pennock & Adami (2003)](../../sources/lenski-2003-evolutionary-origin-complex-features.md) used Avida to show that a *complex* feature (the EQU logic function) **evolves from a replicate-only ancestor by building on simpler rewarded functions** — and crucially **fails to evolve at all (0/50 populations) when only the complex function is rewarded** (vs 23/50 in reward-all). Deleterious mutations can serve as **stepping-stones**. This is the strongest evidence in the lineage that **incremental Darwinian assembly** — not a designed endpoint — produces complexity, and it sets up the question Computational Life answers in the extreme: what if there's **no reward structure at all**?

### Cellular automata — the foundational substrate
Before the digital-replicator lineage and NCA, the simplest "complex behavior from a simple local rule" systems are **[cellular automata](cellular-automata.md)**. [Conway's Game of Life](../../entities/game-of-life.md) (1970) is the canonical case: one neighbor-count rule on a 2D grid yields gliders, glider guns, and Turing-completeness. [Stephen Wolfram](../../entities/stephen-wolfram.md)'s [50-year retrospective](../../sources/wolfram-2025-game-of-life-engineering.md) adds an axis the rest of this branch doesn't: given a *fixed* rule, the useful structures come either by **construction** (modular human "invention") or by **search** (algorithmic "discovery" — *mining the computational universe*), with search overtaking construction as compute grew. His **computational irreducibility** (no shortcut but to run the computation) and **Principle of Computational Equivalence** are the theoretical backdrop for why simple rules are inexhaustibly rich.

### Learnable self-organization — Neural Cellular Automata
A sibling of the digital-evolution line that *learns* rather than *evolves* its local rule: **[Neural Cellular Automata](neural-cellular-automata.md)** (NCA), where a shared neural update rule, trained by backprop, makes a grid of cells **self-organize into a target pattern** with regeneration and robustness ([Pajouheshgar et al. 2025](../../sources/pajouheshgar-2025-nca-cells-to-pixels.md)). Notably, **[Alexander Mordvintsev](../../entities/alexander-mordvintsev.md)** — who originated NCA — is also a co-author of [Computational Life](../../sources/computational-life-self-replicating-programs-paper.md), personally tying the **learned-rule** and **emergent-replicator** wings of this branch together.

## Mentioned in
- [Computational Life (Agüera y Arcas et al., 2024)](../../sources/computational-life-self-replicating-programs-paper.md)
- [cubff (paradigms-of-intelligence/cubff)](../../sources/cubff-github.md) — the runnable engine for the anchor result.
- [BFF — Emergent Complexity experiment (Jonas Werner)](../../sources/jonas-werner-bff-emergent-complexity.md) — independent CPU reproduction of the BFF result.
- [Kriegman et al. 2020 — A scalable pipeline for designing reconfigurable organisms](../../sources/kriegman-2020-reconfigurable-organisms.md) — AI-designed living machines (Xenobots).
- [Blackiston et al. 2021 — A cellular platform for synthetic living machines](../../sources/blackiston-2021-cellular-platform-synthetic-living-machines.md) — cilia-driven self-organizing "Xenobots 2.0".
- [Kriegman et al. 2021 — Kinematic self-replication in reconfigurable organisms](../../sources/kriegman-2021-kinematic-self-replication.md) — spontaneous kinematic self-replication in Xenobots.
- [AI-Designed Living Robots Can Self-Replicate (IEEE EMBS feature)](../../sources/embs-xenobots-self-replicate-feature.md) — secondary coverage of the self-replication result.
- [CRobots (troglobit/crobots)](../../sources/crobots-github.md) — non-replicating programming-game cousin (see Programming games note above).
- [An Approach to the Synthesis of Life (Ray, 1991)](../../sources/ray-1991-tierra-synthesis-of-life.md) — Tierra; open-ended evolution from a hand-written ancestor.
- [Evolutionary Learning in … 'Avida' (Adami & Brown, 1994)](../../sources/adami-brown-1994-avida.md) — spatial digital evolution; evolving computation.
- [The evolutionary origin of complex features (Lenski et al., 2003)](../../sources/lenski-2003-evolutionary-origin-complex-features.md) — Avida; complex features need rewarded simpler steps (0/50 vs 23/50).
- [Neural Cellular Automata: From Cells to Pixels (Pajouheshgar et al., 2025)](../../sources/pajouheshgar-2025-nca-cells-to-pixels.md) — learnable self-organization (Mordvintsev NCA line).
- [Game of Life engineering essay (Wolfram, 2025)](../../sources/wolfram-2025-game-of-life-engineering.md) — cellular automata; construction-vs-search; computational irreducibility.
- [Darwin (Bell Labs, 1961; McIlroy transcript)](../../sources/darwin-1961-bell-labs-game.md) — the earliest digital-organism arena; Core War's direct ancestor.
- [Dewdney 1984 — Core War (Scientific American)](../../sources/dewdney-1984-core-war-scientific-american.md) — the founding self-replicating programming game (the Imp).
- [pMARS — Portable Redcode Simulator (KOTH.org)](../../sources/pmars-koth.md) — the standard Core War simulator.
- [corewars.org — community hub](../../sources/corewars-org.md) — present-day Core War landing page.
