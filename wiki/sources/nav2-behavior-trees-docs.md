---
title: Nav2 Behavior Trees documentation (BT Navigator, Nav2-specific nodes, default tree)
type: source
url: https://docs.nav2.org/behavior_trees/index.html
author: Nav2 maintainers (Steve Macenski et al.)
venue: Nav2 1.0.0 documentation
published: 2026-01-01
ingested: 2026-08-04
format: html
tags: [nav2, ros2, behavior-trees, bt-navigator, recovery-behaviors, execution-rail, navigation, behaviortree-cpp]
---

# Nav2 Behavior Trees documentation

The **production instantiation** of everything the [behavior-trees book](behavior-trees-book.md) describes: [Nav2](../entities/nav2.md) — the ROS 2 navigation stack — is architected around a behavior tree, uses [BehaviorTree.CPP](behaviortree-cpp-docs.md) v4 (`BTCPP_format="4"`), and ships a default tree that has been run on a very large number of real robots.

This is the most valuable part of the BT thread for this wiki, because it is not a formalism or a proposal — it is a **shipped, inspectable, production control structure** with published XML.

## Nav2's own control nodes — the formalism was not enough

The book's classical vocabulary is Sequence / Fallback / Parallel / Decorator. Nav2 **added control node types**, which is the strongest available evidence about where the classical formulation falls short in practice. Exact semantics as documented:

| Node | Semantics | Why it exists |
|---|---|---|
| **PipelineSequence** | Ticks children in order, but **re-ticks all prior children** when a later one returns RUNNING — *"resembling the flow of water in a pipe."* FAILURE anywhere halts all and fails. | A plain Sequence stops re-evaluating earlier steps once it moves on. Navigation needs the planner to keep replanning *while* the controller is still following. *"The retick-ing of Action_A is what makes PipelineSequence useful."* |
| **RecoveryNode** | Exactly two children. Returns SUCCESS iff the first succeeds. On FAILURE of the first, ticks the second, then retries — bounded by `number_of_retries`. | Pairs a behavior with its remedy. *"Often, the ticking of the second child action will promote the chance the first action will succeed."* |
| **RoundRobin** | Cycles children until one returns SUCCESS; **retains state across ticks**, so the next entry resumes at the *following* child rather than restarting. Fails only if all children fail. | Escalating recovery — try a different remedy each time rather than the same one. |
| **NonblockingSequence** | Ticks **all** children while they return SUCCESS or RUNNING, re-ticking even already-successful ones — *"to ensure that successful nodes do not latch a stale state while waiting for another long running node to be complete."* | Stale-state avoidance under concurrency. |
| **PersistentSequence**, **PauseResumeController** | listed; semantics not captured at this depth | — |

Nav2 also adds decorators that are pure **rate control**: `RateController` (tick child at a fixed Hz), `DistanceController` (tick every N metres travelled), `SpeedController` (tick at a rate proportional to robot speed), `SingleTrigger`, `GoalUpdater`.

> [!note] The tell: three of Nav2's additions are about *time*
> RateController, DistanceController, SpeedController, and the re-ticking semantics of PipelineSequence/NonblockingSequence all exist because the classical BT assumes a single global tick and real robots do not. **The formalism's gap is temporal, not structural** — which is exactly what the book's own "checking all conditions can be expensive" disadvantage predicted, arrived at from the other direction.

## The default tree, in full

`navigate_to_pose_w_replanning_and_recovery.xml` — *"replans the global path periodically at 1 Hz and it also has recovery actions."* Structure:

```xml
<root BTCPP_format="4" main_tree_to_execute="NavigateToPoseWReplanningAndRecovery">
  <RecoveryNode number_of_retries="6" name="NavigateRecovery">
    <PipelineSequence name="NavigateWithReplanning">
      <ProgressCheckerSelector .../>  <GoalCheckerSelector .../>
      <PathHandlerSelector .../>      <ControllerSelector .../>  <PlannerSelector .../>
      <RateController hz="1.0">
        <RecoveryNode number_of_retries="1" name="ComputePathToPose">
          <Fallback name="FallbackComputePathToPose">
            <ReactiveSequence name="CheckIfNewPathNeeded">
              <Inverter><GlobalUpdatedGoal/></Inverter>
              <IsGoalNearby path="{path}" proximity_threshold="4.0" .../>
              <TruncatePathLocal input_path="{path}" output_path="{remaining_path}" .../>
              <ValidatePath path="{remaining_path}"/>
            </ReactiveSequence>
            <ComputePathToPose goal="{goal}" path="{path}" planner_id="{selected_planner}" .../>
          </Fallback>
          <Sequence>
            <WouldAPlannerRecoveryHelp error_code="{compute_path_error_code}"/>
            <ClearEntireCostmap name="ClearGlobalCostmap-Context" .../>
          </Sequence>
        </RecoveryNode>
      </RateController>
      <RecoveryNode number_of_retries="1" name="FollowPath">
        <FollowPath path="{path}" controller_id="{selected_controller}" .../>
        <Sequence>
          <WouldAControllerRecoveryHelp error_code="{follow_path_error_code}"/>
          <ClearEntireCostmap name="ClearLocalCostmap-Context" .../>
        </Sequence>
      </RecoveryNode>
    </PipelineSequence>
    <Sequence>
      <Fallback>
        <WouldAControllerRecoveryHelp .../>  <WouldAPlannerRecoveryHelp .../>
      </Fallback>
      <ReactiveFallback name="RecoveryFallback">
        <GoalUpdated/>
        <RoundRobin name="RecoveryActions">
          <Sequence name="ClearingActions">
            <ClearEntireCostmap name="ClearLocalCostmap-Subtree" .../>
            <ClearEntireCostmap name="ClearGlobalCostmap-Subtree" .../>
          </Sequence>
          <Spin spin_dist="1.57" .../>
          <Wait wait_duration="5.0" .../>
          <BackUp backup_dist="0.30" backup_speed="0.15" .../>
        </RoundRobin>
      </ReactiveFallback>
    </Sequence>
  </RecoveryNode>
</root>
```

### Two-tier recovery — the design worth stealing

- **Contextual recovery**, inside the Navigation subtree: each primary behavior (`ComputePathToPose`, `FollowPath`) is wrapped in its **own** `RecoveryNode number_of_retries="1"` whose remedy is guarded by a `WouldA…RecoveryHelp` condition reading that behavior's error code. **The remedy is chosen by the failure's cause, and only attempted if it could plausibly help.**
- **System-level recovery**, the second child of the top-level RecoveryNode: reached only when contextual recovery has failed. A `RoundRobin` escalates through **clear both costmaps → Spin → Wait → BackUp**, one new remedy per failure.
- The whole thing is bounded: `number_of_retries="6"` at the top.
- `ReactiveFallback` with `<GoalUpdated/>` as its **first** child means a new goal **preempts recovery immediately** — a one-line expression of "abandon what you're doing if the objective changed."

The docs' framing: *"The overall BT will (hopefully) spend most of its time in the Navigation subtree… If the contextual recoveries were still not enough, the Navigation subtree will return FAILURE. The system will move on to the Recovery subtree to attempt to clear any system level navigation failures."*

### Runtime plugin selection

`PlannerSelector`, `ControllerSelector`, `GoalCheckerSelector`, `ProgressCheckerSelector`, `PathHandlerSelector` each read a **ROS topic** and write the chosen plugin ID to the blackboard, consumed downstream as `planner_id="{selected_planner}"`. **The algorithm can be swapped at runtime without editing the tree** — the BT is the stable interface, the implementations are hot-swappable.

## Why this matters to this wiki

> [!note] Nav2 *is* a shipped execution rail
> The [guardrails synthesis](../syntheses/agents/guardrails-for-robot-agents.md) concluded that the **execution rail ships empty** across every stack examined — the layer that decides "is this action safe *right now*, given world state" has a hook and no policy. Nav2's default tree is a counterexample hiding in plain sight: **`ValidatePath`, `IsGoalNearby`, `WouldAControllerRecoveryHelp`, and `GoalUpdated` are exactly world-state preconditions gating actions**, with bounded retries and a declared escalation path, in XML anyone can read and diff.
>
> It is scoped to navigation rather than general manipulation, and it is safety-*adjacent* (recovering from failure) rather than safety-*enforcing* (refusing unsafe actions). But the claim that nothing ships at this layer needs qualifying: **the mechanism ships, applied to a different problem.**

The **1 Hz replanning rate** (`RateController hz="1.0"`) is also a concrete entry for the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) — a deliberate, shipped deliberative-tier rate sitting exactly where the wiki's Band C planner tiers live.

## Open questions

- **BT tick rate is not captured** — `RateController hz="1.0"` throttles *replanning*, but the rate at which the tree itself is ticked (and therefore how fast conditions are re-evaluated and preemption happens) was not found at this depth. That number is what determines the tree's reactivity, and belongs on the control-rate ladder.
- **PersistentSequence and PauseResumeController** semantics not captured.
- **No BT contains a learned policy anywhere in Nav2.** Every leaf is a classical planner, controller, or scripted behavior. The [BT-over-VLA](../concepts/robotics/behavior-trees.md) architecture remains unbuilt — but Nav2 demonstrates every piece of scaffolding it would need.
- **No safety argument is made in these docs.** The recovery structure is presented as robustness engineering, not as a guardrail. Whether Nav2's maintainers would accept the execution-rail framing above is unrecorded.
- The book's **formal analysis** (stochastic BTs → Markov chains → success probability, expected completion time) is not applied to this tree anywhere in the docs, despite the tree being exactly the object that analysis targets.

## Entities mentioned
- [Nav2](../entities/nav2.md) · [BehaviorTree.CPP](../entities/behaviortree-cpp.md) · [ROS 2](../entities/ros2.md)

## Concepts touched
- [Behavior trees](../concepts/robotics/behavior-trees.md) — the shipped instance, plus the control nodes the formalism lacked
- [AI guardrails](../concepts/safety/ai-guardrails.md) — world-state preconditions gating actions, in production
- [Action representation languages](../syntheses/agents/action-representation-languages.md) — readable composition over swappable implementations
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — the tree is the composition layer above primitives
