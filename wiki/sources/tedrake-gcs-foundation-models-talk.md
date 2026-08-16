---
title: "Planning with Graphs of Convex Sets (in the age of foundation models) — Russ Tedrake, MIT Robotics Seminar"
type: source
url: https://www.youtube.com/watch?v=JZokn4Pc-YY
author: Russ Tedrake (MIT Robotics Seminar, host Luca Carlone)
published: 2024-04-07
ingested: 2026-08-16
venue: MIT Robotics Seminar (62 min, incl. ~12 min Q&A)
format: video (ingested via YouTube auto-captions)
tags: [graphs-of-convex-sets, gcs, motion-planning, iris, convex-optimization, planning-through-contact, semidefinite-relaxation, deployment, dexai-robotics, drake, russ-tedrake, large-behavior-models, diffusion-policy, planning-and-learning]
---

# Planning with Graphs of Convex Sets (in the age of foundation models)

## Summary

Tedrake's 2024 MIT Robotics Seminar is the talk where **[GCS](../concepts/robotics/graphs-of-convex-sets.md) stops being a paper and becomes a status report**. Two things happen in it that the [primary GCS paper](gcs-motion-planning-paper.md) could not supply. First, the deployment question is answered on the record: **[Dexai Robotics](../entities/dexai-robotics.md) replaced its tuned PRM planner with GCS in production food preparation** (33:54–34:34). Second, every one of the paper's stated limits — hand-placed IRIS seeds, no task-space constraints, no contact, plan-not-policy — is shown with a named student and a result attached, which reframes those limits as a work programme rather than a boundary.

The framing device is the title's parenthetical. Tedrake opens by saying he feels "a duty" to justify giving a planning talk while foundation models arrive, and answers with **AlphaGo as the template**: behavior cloning first, then search on top. TRI's [Diffusion Policy](../entities/diffusion-policy.md)/[LBM](../concepts/learning/large-behavior-models.md) work is step one; his claim is that robotics is **missing its MCTS** (10:21–11:28), and the whole talk is an argument that GCS is the candidate. He is explicit that it is not there yet: *"I don't think we can solve dexterous hands with GCS as it is. The graph gets too big. I need help"* (61:19).

> [!note] Ingested from auto-captions — names are unreliable
> Per the wiki's [YouTube ingest convention](automated-podcast-tedrake-rocket-ship.md), auto-captions garble proper nouns. "Tobias" is [Tobia Marcucci](../entities/tobia-marcucci.md); "ewa" is the KUKA **iiwa**; first names of students and collaborators (Alex, Pete, Tommy, Shruti, Bernard, Terry, Peng, Sava, Shao, Chung, Boyuan) are transcribed as heard and **surnames are not asserted here**. Technical content and quoted phrasing are reliable; attribution of a specific result to a specific full name is not, and is deliberately left incomplete.

## The finding: GCS is deployed, in one narrow regime

> *"GCS trajectory optimization by itself is kind of transitioning from basic research to real use cases. There's a lot more work to do, but we're actually trying to push this out. It's in [Drake](../entities/drake.md). It's, you know, pretty mature implementations. If you bang on it, you might break it. We'll fix it."* (33:54)
>
> *"Dexai is a local company. We had a project with them. They're doing food preparation… they make salad bowls and things like this with robots. And so they switched from their pretty optimized — this is like **time is money** for these guys — **PRM-based planner. Now they're using GCS in production**. And they were pretty happy with how that worked."* (34:13–34:34)

Corroborated independently, with numbers, by the [ARM Institute project page](arm-institute-gcs-dexai-project.md): commercial transition, "multiple customer sites across the nation," return exceeding **$10,000/robot/year**.

**The qualifying sentence is the important one**, because it states the deployment regime exactly:

> *"In a setting where you're going to be making plans all day long, you're willing to precompute once, it makes a lot of sense. I think it just really clobbers that problem."* (34:34)

Every restriction the paper lists is free in that regime: a fixed workcell amortizes the manual IRIS seeding to nothing; thousands of queries against one graph is what multi-query planning is *for*; utensils moving through free space need no dynamics, no contact, and no task-space constraint; and cycle time is already the customer's revenue metric, which is the axis on which GCS beat shortcut-PRM. Tedrake generalizes it as the **logistics-company case** twice more (36:49, 53:14) and contrasts it with the mobile manipulator that *"want[s] to not run into things, but I'm not trying to be time optimal"* — where he expects the answer to *"change completely,"* going *"directly from perception into approximate regions"* (53:14–53:34).

MIT is replicating the same setup in the lab — a pick-and-place clutter-clearing rig running all day, *"hammering on this and trying to make sure the solve times are small"* (34:55).

> [!warning] This is an April 2024 snapshot, and the wiki has nothing newer
> One named production user, stated once in a seminar, two years before ingest. Whether Dexai still runs GCS, whether other adopters followed, and what the ARM software modules became are all unverified here.

## Key claims

**On the framework (16:32–33:04)** — mostly restating the [paper](gcs-motion-planning-paper.md), with two additions worth keeping:

- **The thesis in one sentence**: motion planning conflates a **combinatorial** problem (left or right around the obstacle; which contact mode) with a **smooth optimization** over continuous curves, and *"the story today is going to be pulling those two apart and mak[ing] that separation explicit"* (17:45).
- **What is wrong with a roadmap, stated as a design complaint**: *"the knowledge you have, the checks you've made on your environment are limited to points and the line segments connecting them. So there's sort of no room left to deal with optimization"* — no room for dynamics, uncertainty, or robustness. GCS replaces *"a road map of points connected by line segments"* with *"a road map of convex sets… connected by continuity constraints"* (18:31–22:12).
- **Convexity is a starting point, not a creed**: *"I actually don't think the world is only convex… we've done the convex case first"* — with ongoing work on nonlinear versions that still benefit from the GCS decomposition (24:26).
- **Graph size, answered from the floor**: *"tens of regions cover a huge part of state space"* (33:26). The paper's 8-regions-for-15,000-samples is not a cherry-picked instance.

**Automatic region seeding — the paper's biggest practical hole, now closed (28:14–30:07)**

The paper placed IRIS seeds by hand. The talk describes a turnkey replacement:

1. Sample and build a **visibility graph** (edge between any two configurations connected by a straight collision-free line — *"a little different than a PRM"* in that distance does not matter).
2. **A clique in the visibility graph almost corresponds to a convex set in the original space**, so approximately solve a **minimum clique cover** on it to decide where the convex sets go.
3. Iterate to patch the gaps.

*"We've got some new algorithms now that explicitly try to optimize the convex cover of the space… almost turnkey convex decomposition algorithms."* Attributed to two students (heard as Pete and Alex). This is the direct answer to the [paper's](gcs-motion-planning-paper.md) *"automatic seeding of the regions is certainly possible"* — it was done.

He also pushes back on the fear itself: *"a lot of people are afraid of the convex decomposition. It is a little daunting, but it works really well"* — a random walk through one high-dimensional configuration-space polytope goes *"right up around the mug and back and out"* (27:52–28:14).

**Extensions that erase paper-stated limits (35:14–36:23)**

| Paper limit | Extension in the talk |
|---|---|
| Euclidean configuration space only | **Geodesic convexity** — planning on manifolds (SO(2) mobile bases, continuous-rotation wheel joints); PR2 demo where other planners take the silly route |
| No task-space constraints | **Analytical IK inside the region construction** — a bimanual "keep the hands together" end-effector constraint, nonconvex in configuration space, handled by building GCS regions on the constraint manifold |
| No contact | see below |
| Plan, not policy | see below |

**Planning through contact via semidefinite relaxation (37:09–44:32)** — the part Tedrake says he is actually excited about (*"if the promise was only collision-free motion planning, I wouldn't be as excited as I am"*, 36:49):

- Quasi-static planar pushing; plan over object poses, contact forces, contact locations. The nonconvexity is real: SO(2) constraints plus **force × distance** bilinear terms, i.e. a **QCQP**.
- Standard SDP relaxation of the QCQP **plus strengthening constraints exploiting SO(2) structure**. The feasible set of an SDP is a **spectrahedron** — a convex set — *"so now these are going to become the sets in our GCS."* One spectrahedron per contact mode.
- *"When Hongkai was here… we were hammering on trying to do semidefinite relaxations of contact. Never quite got it. This time we got it. I think we just tried a little harder."*
- **The key lowering of the bar**: the relaxation *"doesn't have to be perfect… it just has to be strong enough to help you know which path to take through the graph"* — push from this side or that side, pick the object up or not. *"Then the details you can fill in later. That's not the hard part."*
- **A correction to a decade of contact-graph papers**: the combinatorial hardness is **not** making and breaking contact — *"you can soften [that]… that's not where the discontinuities and the combinatorial complexity comes from. It's more about am I contacting on this side or am I contacting on this side"* (43:56–44:32).
- Closed loop back to learning: those planned contact trajectories were *"load[ed] into a diffusion policy"* overnight, as *"a curriculum for our co-training"* (42:38–43:04).

**From plans to policies, via the dual (46:22–49:07)** — the most underrated segment:

- In ordinary shortest-path LP, the **dual variables are the cost-to-go**. In GCS the dual is a **piecewise-affine lower bound on the value function** — *"when you solve the GCS problem, you're actually solving for a lower bound on the value function for all the sets."*
- Make the dual **quadratic or polynomial** → it becomes an **SOS** program → tighter lower bounds. One offline solve yields a collision-free trajectory from *any* initial condition, not one.
- Weak lower bounds plus a little online search already give *"incredibly strong players"* — the MCTS analogy made concrete.
- Move the piecewise-quadratic value function back to the primal and *"it looks like you're pushing probability distributions through the graph,"* higher-order polynomials ↔ higher-order moments — a route to **planning under uncertainty**, which also fixes optimized planners' habit of hugging obstacles.

**Beyond shortest paths (49:07–49:43)**: a box-moving TAMP instance where the right combinatorial object was not a shortest path but a **walk on the permutohedron**, because box order does not matter. Generalized advice, given twice: *"ask what's the right way to cast that into a network flow"* — if the network-flow problem has a good convex formulation, its GCS extension likely does too; if it is NP-hard (TSP), GCS will not save you (54:25–55:09).

**Where the relaxation is loose (57:12–58:32)**: *"symmetries in the graph are a natural thing that kills you."* Concrete failure: a UAV took a long path around instead of flying through one of **two near-identical windows**, because the relaxation split probability between them — the paper's footnote-3 argument, observed in the wild. And a genuine design tradeoff surfaced in Q&A: smaller regions make a convex approximation of nonlinear dynamics tighter but grow the discrete problem — *"you can move the work from the convex optimization into the discrete problem and vice versa."*

## The planning-and-learning argument (02:30–16:32, 55:37–57:12)

The frame, not a digression — it is where the talk says what GCS is *for*:

- **AlphaGo as template**: behavior cloning from human games → self-play + MCTS. Robotics has step one working (*"50 to 100, maybe 200 [demos] if it's an important skill"*, hundreds of skills, *"a lot of things that you can do with a two-finger gripper we've done with diffusion policy"*). Step two is missing: *"our planners, especially when you're planning through contact, are still very weak… I've been working on this for 20 years, so I'm just blaming myself."*
- **A worry about what the field dropped**: going from Go to StarCraft, *"the Monte Carlo tree search kind of fell out of the way and became just the more naive exploration from PPO… I feel like we're still missing that MCTS for robotics."*
- **Planning strengthens a policy with no additional learning**: *"just by virtue of looking ahead a few steps before you make your decision, you're immediately stronger"* — the case for online planning on top of a generalist policy in open-world zero-shot settings.
- **And the reverse, asked directly in Q&A**: how does learning help planning? Answer — the graph explodes for dexterous contact, *"I can't even put it in memory."* Roll out a reasonably strong generalist policy a handful of times; that **tells you which nodes of the graph to visit**, yielding a small graph (the MCTS move), and for each path *"now it's just a convex optimization."* The explicit graph representation also fixes rollout redundancy: *"once you've visited this path through the graph, you don't need to look at that one again."*
- **Why he prefers this to RL**, stated as an optimizer-strength argument rather than a tribal one: RL *"is still a weak optimizer"* and *"a lot of times there's some cost function tuning in the middle"* — whereas here *"we're trying to write down exactly the cost function we want. Minimum distance from here to here, plus maybe minimum energy. **No tuning.**"*
- **And on why the method progresses**: *"It is not throwing darts at the wall"* — the object is given by Newton, and the game is finding the most efficient approximation of its convex hull.
- **Sim-to-real, in passing but on the record**: *"the simulation just doesn't have to be perfect… The new thing is to **co-train in sim and real**, and admit that there's a gap"* — the transfer-learning bet, with data ranked robot-teleop → other robots → simulation → curated egocentric → YouTube (11:49–14:42).

## Entities mentioned

- [Russ Tedrake](../entities/russ-tedrake.md) — speaker.
- [Dexai Robotics](../entities/dexai-robotics.md) — **new page from this ingest**; the production GCS user.
- [Tobia Marcucci](../entities/tobia-marcucci.md) — named as the through-line on every GCS slide ("Tobias" in captions).
- [Drake](../entities/drake.md) — where the mature implementation ships.
- [TRI](../entities/tri.md) · [Diffusion Policy](../entities/diffusion-policy.md) · [UMI](../entities/umi.md) — the learning half; a UMI-style handheld-gripper collaboration was announced the same day (collaborator garbled in captions).
- [Spot](../entities/spot.md) — full-dimensionality GCS planning demoed on it.
- Without pages: **Dexai Robotics' Alfred** platform is not named in the talk; IRIS / C-IRIS; MOSEK; PR2; Kinova MOVO; Robin Deits (IRIS originator, named); Hongkai Dai (named); Luca Carlone (host).

## Concepts touched

- [Graphs of convex sets (GCS)](../concepts/robotics/graphs-of-convex-sets.md) — **major update**: deployment, automatic seeding, contact, policies.
- [Motion planning (classical)](../concepts/robotics/motion-planning.md) — the PRM-generalization argument, restated as a design complaint about roadmaps.
- [Task and motion planning](../concepts/robotics/task-and-motion-planning.md) — the permutohedron instance; GCS as a TAMP primitive.
- [Optimal control](../concepts/robotics/optimal-control.md) — the dual-as-value-function segment is GCS reaching into dynamic programming.
- [Large behavior models](../concepts/learning/large-behavior-models.md) · [Imitation learning](../concepts/learning/imitation-learning.md) — the AlphaGo-template argument for what planning adds on top.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — the co-train-and-admit-the-gap position.
- [Formal verification](../concepts/learning/formal-verification.md) — SOS lower bounds on value functions.

## Open questions

- **What happened after April 2024?** The single hardest gap. Is GCS still in Dexai's production stack; did any other company adopt it; what became of the five ARM software modules?
- **Are the extensions published and reproducible?** Geodesic-convexity GCS, analytical-IK regions on manifolds, clique-cover seeding, and the contact/spectrahedron work are all described from slides. Each is presumably a paper by now; none is ingested.
- **The dexterous-hand admission is the honest limit and it is unresolved**: *"the graph gets too big. I need help."* His proposed fix — a generalist policy proposing which nodes to expand — is a *plan*, not a result. Nobody in this wiki has demonstrated a learned policy pruning a planner's graph on a real dexterous task.
- **Does the deployment regime generalize at all?** Tedrake himself says the mobile-manipulator answer will *"change completely."* If GCS's industrial fit is precisely the fixed-workcell, time-is-money case, then it is a strong result in a narrow market, not general infrastructure — and the wiki should say so until evidence arrives.
- **Contact planning on real hardware**: "only simple hardware examples of it so far" (20:42). The planar-pushing result is on a real robot; contact-rich manipulation with a hand is not.
