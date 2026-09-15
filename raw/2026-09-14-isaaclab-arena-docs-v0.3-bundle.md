==================================================================
FILE: docs/pages/references_release_notes.rst
==================================================================
Release Notes
=============

v0.3.0
------

This release introduces:

- Prompt-first environment generation.
- Controlled randomization through variations.
- Sensitivity analysis.
- Multi-node evaluations.
- Expanded policy integrations.
- Task libraries, including RoboLab-style tasks and our own Kitchen Benchmark for tasks in
  realistic kitchens.

Details below:

**Features and improvements**

- **Agentic environment generation:** Added ``EnvironmentGenerationAgent`` for creating environments from
  natural-language prompts, with intent-to-graph conversion, SimReady asset search, composite-task
  support, configurable inference endpoints, and an interactive review GUI with simulation
  snapshots and relation-solver previews (#718, #770, #803, #804, #805, #868, #982, #1050).
- **Typed environment definitions:** Added Pydantic-based ``ArenaEnvGraphSpec`` YAML parsing and CLI
  bring-up, typed environment and policy configurations, a reusable environment factory, and a
  unified path for loading registered Python environments or graph YAML files
  (#690, #749, #757, #808, #858, #860, #862, #863).
- **Isaac Lab 3.0 workflow interoperation:** Updated the Isaac Lab submodule and moved
  demonstration recording, replay, and teleoperation to Isaac Lab's scripts through Arena's
  external environment registration callback (#960, #994, #1022).
- **Experiments and evaluation reports:** Replaced legacy evaluation jobs with typed YAML
  Experiments and Runs, including environment rebuilds, chunked and multi-node dispatch,
  combined JSON results, an experiment viewer, grouped success-rate plots, and generated
  evaluation reports (#751, #772, #802, #867, #873, #896, #1042, #1056, #1070).
- **Variations and sensitivity analysis:** Added Hydra-configurable variations with in-memory
  recording for lighting, camera intrinsics, and object mass, plus an MNPE/NPE sensitivity-analysis
  workflow, sample dataset, and plotting tools (#729, #746, #755, #775, #789, #913, #916, #1055).
- **Object placement and validation:** Added heterogeneous and deterministic placement,
  mesh-based non-collision constraints, ``NotNextTo`` and ``FaceTo`` relations, unified placement
  APIs, build-time physics settling, and pluggable validation checks (#676, #679, #732, #769,
  #771, #809, #888, #927).
- **Robot reachability validation:** Added a build-time, simulation-free cuRobo IK gate for
  task-relevant object layouts, including Droid and Franka embodiment placement, collision
  checking, and optional debug visualization (#914, #947, #954, #984, #1014).
- **Policy integrations:** Added OpenPI support for DROID and Pi0.5, GR00T remote closed-loop
  policies with pluggable action schedulers, Cosmos and DreamZero policies, and OSMO workflows
  for parallel and multi-policy evaluation (#595, #655, #658, #663, #688, #823, #843, #963,
  #991, #1005).
- **Task libraries:** Added the RoboLab catalog and more than 15 pick-and-place environments,
  plus Lightwheel and Replicator kitchen environments for pick-and-place, opening doors and
  microwaves, pressing buttons, and turning knobs (#845, #857, #962, #965, #966, #1048, #1149,
  #1155).
- **Progress tracking:** Added fine-grained subtask state, episode recording, order-independent
  composite tasks, unified success checks, and normalized progress scoring (#677, #758, #810,
  #822, #840, #1137).

**Documentation**

- **Agentic generation workflows:** Added concept, validation, tabletop, kitchen, GUI,
  reachability, and collision-handling documentation for prompt-first environment creation
  (#844, #1025, #1028, #1033, #1046, #1064, #1076, #1085, #1135).
- **Evaluation workflows:** Added documentation for Experiments and Runs, generated reports,
  multi-node execution, variations, sensitivity analysis, environment seeds, and
  ``RigidObjectSet`` (#1030, #1045, #1051, #1053, #1063, #1068, #1072).
- **Website and catalogs:** Added the Kitchen Benchmark and RoboLab catalogs, redesigned the
  overview and motivation pages, and updated the release documentation for Arena 0.3
  (#1041, #1048, #1089, #1126, #1217, #1222).

**Infrastructure and CI**

- **Native installation:** Added a fully source-based ``uv`` installation path with lightweight
  OpenPI and GR00T clients, runtime package configuration, and dedicated native-``uv`` CI
  validation (#908, #934, #938, #944, #1084, #1092, #1101).
- **Docker workflows:** Added per-clone container naming, host-user command execution, optional
  container suffixes, and improved Docker support for agent workflows (#643, #760, #762, #763).
- **CI coverage:** Added all-environment smoke testing, a GR00T closed-loop end-to-end job,
  camera test coverage, and improved Isaac Sim shader caching and subprocess isolation
  (#617, #618, #644, #675, #950).

**Assets and tests**

- **Kitchen assets:** Added Replicator kitchen examples, publicly hosted USD-randomizer kitchens,
  Lightwheel kitchen registration, mesh-placement examples, and kitchen task configurations
  (#962, #965, #1088, #1090).
- **RoboLab assets:** Added the RoboLab catalog, missing object assets, agent-generated
  pick-and-place environments, and OpenPI-versus-Cosmos experiment configurations
  (#815, #817, #820, #845, #857, #1020).

**Bug fixes**

- **Placement correctness:** Fixed relation-solver bounding-box scaling, rotation-around
  placement failures, IK reachability for relation-placed robots, and geometric pick-and-place
  success checks (#816, #921, #1081, #1132).
- **Rendering and cameras:** Fixed corrupt kitchen rendering, Droid camera quaternion ordering,
  review-GUI viewport setup, and viewpoint camera poses in parallel environments
  (#673, #941, #1043, #1223).
- **Evaluation correctness:** Fixed normalized progress scores, missing-video report handling,
  timeout termination semantics, and external environment registration for Isaac Lab workflows
  (#865, #994, #1017, #1137).
- **Background physics:** Fixed kitchen placement collisions, relation anchors in background
  collision meshes, and physics reset behavior for kitchen and other backgrounds
  (#988, #1003, #1102, #1180).

**Limitations**

- Installation from a published Python package is not yet supported; use the native ``uv`` source workflow or Docker.

**What's Next**

Future releases will focus on:

- Enhanced Newton support for benchmarks involving contact-rich insertion, cables, and deformables.
- Prompt-to-scene, robot, and task workflows.
- Improved performance for multi-node evaluation.


v0.2.0
------

This release introduces major new capabilities including Isaac Lab 3.0 (Newton) support,
a sequential task chaining framework, semantic object placement, teleoperation, GR00T N1.6
and DROID integration, RL workflows, and a large set of new tasks and embodiments.

**Features and improvements**

- **Isaac Lab 3.0 (Newton) upgrade:** Updated the framework to Isaac Lab 3.0 (Newton),
  including an updated interop layer (#464, #533).
- **Sequential task framework:** Added ``SequentialTaskBase`` class for chaining atomic
  skills into long-horizon tasks, with mimic and metrics support, user-specifiable
  final subtask success states, and an example that puts an object into a microwave and
  closes the door (#289, #323, #337, #365).
- **Semantic object placement:** Added a differentiable relation-based object placement
  solver supporting ``On``, ``NextTo``, ``AtPosition``, and ``PositionLimits`` relations,
  multiple anchors, ``RotateAroundSolution``, and full integration with ``ArenaEnvBuilder``
  and ``ObjectPlacer`` (#328, #354, #358, #362, #387, #574).
- **Teleoperation:** Added teleoperation support for G1 loco-manipulation and GR1 using
  Quest XR hand-tracking and CloudXR; updated to IsaacTeleop v1.1 (#286, #350, #577, #605).
- **GR00T N1.6 and DROID integration:** Upgraded GR00T to N1.6 and added DROID dataset
  support, local inference pipeline, and language instruction support for closed-loop
  evaluation (#334, #416, #418, #420, #519).
- **New tasks, embodiments, and evaluation capabilities:** Added Sorting, FactoryAssembly,
  TurnKnob, CloseDoor, and AdjustPose atomic tasks; Galbot and Agibot A2D embodiments;
  G1 WBC-AGILE end-to-end velocity policy; RSL-RL policy evaluation; distributed
  multi-GPU policy runner; multi-task evaluation job runner (#371, #285, #315,
  #295, #305, #391, #292, #489, #333, #411, #277, #445, #394).

**Documentation**

- **README and Getting Started overhaul:** Comprehensive README rewrite and full
  reorganization of the Getting Started section and navigation structure (#480, #505).
- **Concepts and placement docs:** Added a humanized concepts page and a dedicated
  object placement documentation page (#526, #511).
- **RL and evaluation workflows:** Added RL workflow docs, policy evaluation section,
  Newton evaluation example from IsaacLab DexSuite, and GTC DLI workflow docs
  (#363, #451, #536, #390).
- **External repository and advanced usage:** Added a dedicated page for using Arena
  from an external repository, an advanced custom task example, GR00T closed-loop
  docs, and DROID usage instructions (#518, #550, #519).

**Infrastructure and CI**

- **Docker and dependency improvements:** Moved Python dependencies from the Dockerfile
  to ``setup.py``; pinned Newton mujoco version; fixed docker pipx stall; added missing
  Arena package to NGC docker (#535, #629, #640, #578).
- **Repository governance:** Added CODEOWNERS, issue templates (brought over from
  IsaacLab), ``SECURITY.md``, ``AGENTS.md``, and ``CLAUDE.md`` (#583, #584, #585,
  #586, #492, #454).

**Assets and tests**

- **RoboLab objects and HDR library:** Added the RoboLab asset library and HDR lighting
  support for use in robolab scenes (#429, #428, #431).
- **New example environments:** Added GR1 DLI environment, G1 AGILE tabletop
  environment, and a Rubik's cube pick-and-place environment (#385, #562, #421).
- **USD asset paths:** Updated object library paths to use the ``ISAAC_NUCLEUS_DIR``
  prefix and updated USDs to reference the Isaac Sim 6.0 staging bucket (#291, #621).

**Bug fixes**

- **Sequential task metrics:** Fixed subtask success rate metric and
  ``desired_subtask_success_state`` check in sequential task evaluation (#405, #410).
- **RSL-RL evaluation metrics:** Fixed an extra episode appearing in policy evaluation
  metrics when using RSL-RL (#530).
- **Object placement correctness:** Fixed bounding box rotation in world frame, rejection
  of overlapping placements by ``ObjectPlacer``, and initialization of ``On``-relation
  objects within their parent's footprint (#400, #439, #538).
- **Recorder dataset filename collision:** Fixed filename collisions when multiple
  recorders write concurrently to a shared ``/tmp`` directory (#469).
- **Metrics serialization:** Sanitized NumPy types in metrics output to prevent
  serialization errors (#602).


v0.1.1
------

This release includes bug fixes, documentation improvements, CI and infrastructure
updates, and several API and workflow enhancements over v0.1.0.

**Features and improvements**

- **Object configuration:** Object configuration is now created as soon as an asset is
  called, so users can edit object properties before a scene is created (#239).
- **Scene export:** Added support for saving a scene to a flattened USD file (#237).
  Scene export now correctly handles double-precision poses and adds contact reporters
  when exporting rigid objects (#242).
- **Parallel environment evaluation:** Enabled parallel environment evaluation for
  GR00T policy runner, with documentation for closed-loop GR00T workflows (#231, #236).
- **Episode length:** Increased episode length for loco-manipulation to support
  rollout through box drop (#235).
- **Microwave example:** Increased reset openness for the microwave example (#311).

**Bug fixes**

- **Reference object poses:** Fixed reference object poses so they correctly account
  for the parent object’s initial pose; poses are now relative and composed at compile
  time (#232).
- **IsaacLab-to-stage path conversion:** Fixed a bug when the asset name appeared twice
  in the prim path (replaced both instances instead of one) (#241).
- **qpsolvers:** Patched breakage with Isaac Lab 2.3 due to ``qpsolvers`` upgrade by
  pinning to 4.8.1 (#252).
- **Parallel eval:** Removed comments that were breaking the parallel eval run
  commands (#262).

**Documentation**

- **Multi-versioned docs:** Documentation is now versioned so users can read docs that
  match their release (#272, #300).
- **Links and structure:** Updated README docs link to the public location (#270),
  corrected doc pointers (#301), and added release warnings (#303).
- **Installation:** Private Omniverse/Nucleus access is described on a separate page
  to clarify it is not required for normal installation (#261).

**Infrastructure and CI**

- **Runners:** Release 0.1.1 CI runners moved from local (Zurich) to AWS (#433).
- **CI workflow:** Added YAML anchors to reduce repetition in the CI workflow (#245).
- **Contribution guide:** Added signoff requirements for external contributions (#238).
- **Docker:** Fixed Dockerfile pip usage and added SSL certificate support for
  Lightwheel SDK (#449).
- **Tests:** Finetuned GR00T locomanip model is now generated on the fly in tests
  instead of mounting a pre-finetuned models directory, improving public CI
  compatibility and testing the fine-tuning pipeline (#247).

**Assets and tests**

- **G1 WBC:** Updated G1 WBC embodiment file paths to use S3 (#251).
- **Test assets:** Removed internal or custom-only assets from tests: custom cracker
  box (#234), custom USD in ObjectReference test (#240), internal asset from USD
  utils test (#244). ObjectReference test now composes USD on the fly via scene
  export (#240).


v0.1.0
------

This initial release of Isaac Lab Arena delivers the first version of the
composable task definition API.
Also included are example workflows for static manipulation tasks and loco-manipulation
tasks including GR00T GN1.5 finetuning and evaluation.

Key features of this release include:

- **Composable Task Definition:** Base-class definition for ``Task``, ``Embodiment``, and ``Scene``
  that can be subclassed to create new tasks, embodiments, and scenes.
  ``ArenaEnvBuilder`` for converting ``Scene``, ``Embodiment``, and ``Task`` into an
  Isaac Lab runnable environment.
- **Metrics:** Mechanism for adding task-specific metrics which are reported during evaluation.
- **Isaac Lab Mimic Integration:** Integration with Isaac Lab Mimic to automatically generate Mimic definitions for
  available tasks.
- **Example Workflows:** Two example workflows for static manipulation tasks and loco-manipulation tasks.
- **GR00T GN1.5 Integration:** Integration with GR00T GN1.5 including a example workflows for finetuning and evaluating
  the model on the static and loco-manipulation workflows.

Known limitations:

- **Number of Environments/Tasks:** This initial is intended to validation the composable task
  definition API, and comes with a limited set of tasks and workflows.
- **Loco-manipulation GR00T GN1.5 finetuning:** GR00T GN1.5 finetuning for loco-manipulation
  requires a large amount of GPU resources. (Note that static manipulation finetuning can be
  performed on a single GPU.)

==================================================================
FILE: docs/pages/motivation_motivation.rst
==================================================================
Why Isaac Lab-Arena
===================

.. _why-opportunity:

Opportunity
-----------

Simulation makes broad policy evaluation feasible before expensive deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generalist robot policies such as `GR00T <https://developer.nvidia.com/isaac/gr00t>`_ and
`π0 <https://www.physicalintelligence.company/>`_ aim to operate across many tasks, scenes, objects,
embodiments, and deployment conditions. Specialist policies must also remain reliable as deployment
conditions vary.

Evaluating policy robustness requires more than a fixed benchmark suite. Lighting, clutter, object
substitutions, and robot morphology can all change policy behavior; limited coverage can favor
policies tuned to benchmark-specific conditions rather than those that generalize.

Simulation makes policy evaluation at this breadth practical, revealing where a policy holds—and where it
breaks—while iteration is still fast and before real-world testing becomes slow and expensive.


.. _why-gap:

Gap
---

The evaluation space scales. Today's evaluation stack does not.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While coverage grows combinatorially, most tools still treat every variation as a standalone
environment, every benchmark as a new integration, and every run as a queue. Four bottlenecks
follow.

.. raw:: html

   <section class="arena-gap-story" aria-label="Four limitations of today's evaluation stack">
     <article class="arena-gap-story-row">
       <div class="arena-gap-story-copy">
         <span>01</span>
         <h3>Diversity requires redundant code and effort</h3>
         <p>Each new object or embodiment still means another task configuration—resulting in significant code duplication even when the scene setup, observations, actions, and task logic are largely unchanged.</p>
       </div>
       <div class="arena-gap-proof arena-gap-proof-01" role="img" aria-label="One task configuration grows to four when objects vary and eight when both objects and robot embodiments vary">
         <div class="arena-gap-redundancy">
           <span class="arena-gap-redundancy-label">MANUAL EFFORT + REDUNDANCY</span>
           <svg class="arena-gap-manual-curve" viewBox="0 0 280 130" preserveAspectRatio="none" aria-hidden="true" focusable="false">
             <defs>
               <linearGradient id="arena-manual-effort-area" x1="0" y1="0" x2="0" y2="1">
                 <stop offset="0%" stop-color="#d83b30" stop-opacity=".22" />
                 <stop offset="100%" stop-color="#d83b30" stop-opacity="0" />
               </linearGradient>
               <marker id="arena-manual-effort-arrow" markerWidth="5" markerHeight="5" refX="4.2" refY="2.5" orient="auto">
                 <path d="M0 0 L5 2.5 L0 5 Z" fill="#d32f25" />
               </marker>
             </defs>
             <path class="arena-gap-manual-area" d="M24 114 C108 114 164 108 201 79 C231 56 248 25 263 9 L263 116 L24 116 Z" />
             <path class="arena-gap-manual-line" marker-end="url(#arena-manual-effort-arrow)" d="M24 114 C108 114 164 108 201 79 C231 56 248 25 263 9" />
           </svg>
           <div class="arena-gap-config-cases">
             <section>
               <header><b>Fourier GR-1</b><span>Pick <strong>Banana</strong></span><small>in Kitchen</small></header>
               <div class="arena-gap-env-stack arena-gap-env-stack-1"><b>Isaac Lab<br>environment</b><i>Scene</i><i>Termination</i><i>Events</i><i>Observations</i><i>Actions</i></div>
               <em><strong>1×</strong> configuration</em>
             </section>
             <section>
               <header><b>Fourier GR-1</b><span>Pick <strong>Banana · Apple<br>Broccoli · Carrot</strong></span><small>in Kitchen</small></header>
               <div class="arena-gap-env-stack arena-gap-env-stack-4"><b>Isaac Lab<br>environment</b><i>Scene</i><i>Termination</i><i>Events</i><i>Observations</i><i>Actions</i></div>
               <em><strong>4×</strong> copied</em>
             </section>
             <section>
               <header><b>Fourier GR-1 + Franka</b><span>Pick <strong>Banana · Apple<br>Broccoli · Carrot</strong></span><small>in Kitchen</small></header>
               <div class="arena-gap-env-stack arena-gap-env-stack-8"><b>Isaac Lab<br>environment</b><i>Scene</i><i>Termination</i><i>Events</i><i>Observations</i><i>Actions</i></div>
               <em><strong>8×</strong> copied</em>
             </section>
           </div>
         </div>
       </div>
     </article>
     <article class="arena-gap-story-row">
       <div class="arena-gap-story-copy">
         <span>02</span>
         <h3>Every benchmark rebuilds the eval scaffold</h3>
         <p>Teams recreate policy adapters, inference loops, experiment definitions, recording, result collection, and reports—creating high overhead, fragmented results, and limited comparability.</p>
       </div>
       <div class="arena-gap-proof arena-gap-proof-02" role="img" aria-label="Behavior-1K and RoboDojo each rebuild a custom evaluation scaffold rather than sharing one evaluation framework">
         <div class="arena-gap-scaffolds">
           <section><header><span>BENCHMARK A</span><b>BEHAVIOR-1K</b></header><strong>Custom evaluation scaffold</strong><footer>Isaac Lab / Sim</footer></section>
           <div><b>Duplicated</b><strong>≠</strong><span>Shared</span></div>
           <section><header><span>BENCHMARK B</span><b>RoboDojo</b></header><strong>Custom evaluation scaffold</strong><footer>Isaac Lab / Sim</footer></section>
         </div>
       </div>
     </article>
     <article class="arena-gap-story-row">
       <div class="arena-gap-story-copy">
         <span>03</span>
         <h3>Leaderboards reward overfitting; results are not actionable</h3>
         <p>A frozen task-set score shows whether a policy passed a narrow set of conditions—not whether it is robust or generalizes. It shows what failed, but not where or which environment factor exposed the weakness.</p>
       </div>
       <div class="arena-gap-proof arena-gap-proof-03" role="img" aria-label="A frozen task set samples one point in a much larger operating envelope while GR00T and pi zero leaderboard scores leave why the policies failed and what to fix unknown">
         <div class="arena-gap-frozen-score">
           <section><span>POLICY OPERATING ENVELOPE</span><div class="arena-gap-envelope"><i></i></div><small><b></b> Frozen task set <b></b> Conditions untested</small></section>
           <section><header><span>LEADERBOARD</span><b>SUCCESS</b></header><div><i>GR00T</i><strong>51%</strong></div><div><i>π0</i><strong>50%</strong></div><footer>Frozen task set</footer></section>
           <aside><span><b>WHY IT FAILED</b>Unknown</span><span><b>WHAT TO FIX</b>Unknown</span></aside>
         </div>
       </div>
     </article>
     <article class="arena-gap-story-row">
       <div class="arena-gap-story-copy">
         <span>04</span>
         <h3>Sequential execution forces shallow coverage</h3>
         <p>Sequential runs take too long, so teams compromise on insights, tasks, variations, and seeds to get an answer on schedule.</p>
       </div>
       <div class="arena-gap-proof arena-gap-proof-04" role="img" aria-label="A sequential runner reaches the deadline after evaluating only three of thirty-two conditions">
         <div class="arena-gap-sequential">
           <header><span>SEQUENTIAL RUNS</span><b>DEADLINE</b><em>TIME BUDGET</em></header>
           <div class="arena-gap-runner"><strong>RUNNER</strong><i>01</i><i>02</i><i>03</i><i>04</i><i>05</i><i>06</i><i>07</i></div>
           <section><span>Coverage at deadline</span><div class="arena-gap-coverage"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div><strong>3 of 32<small>conditions evaluated</small></strong></section>
         </div>
       </div>
     </article>
   </section>


.. _why-solution:

Solution
--------

A shared evaluation framework
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your benchmark defines the tasks and metrics. Isaac Lab-Arena provides the shared system to author
benchmarks, execute policy evaluations, and analyze results, while extending the Isaac Lab
simulation framework and its physics solvers.

Three approaches to scalable, actionable benchmarking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compositional approach to environment authoring
"""""""""""""""""""""""""""""""""""""""""""""""

Isaac Lab-Arena defines scenes, embodiments, and tasks as reusable modules rather than creating a
standalone configuration for every environment variation. At run time, ``ArenaEnvBuilder`` composes
those modules into a standard Isaac Lab ``ManagerBasedRLEnvCfg``. Teams can swap the scene, robot
embodiment, or task independently while shared components remain unchanged—avoiding duplicate task
code for each new combination.

.. container:: arena-why-feature-links

   :doc:`Explore environment concepts <../quickstart/arena_env>`


Variational approach to robot policy evaluation
"""""""""""""""""""""""""""""""""""""""""""""""""

Move beyond frozen benchmark conditions by turning a base environment into a controlled sweep
across objects, placements, and other environment factors. Arena records the sampled values with
each episode and computes a joint posterior to analyze policy robustness and reveal which factors
impact policy performance.

.. container:: arena-why-feature-links

   :doc:`Explore variation concepts <../quickstart/environment_variations>`

   :doc:`Explore sensitivity analysis concepts <../concepts/concept_sensitivity_analysis>`


Parallel evaluation
"""""""""""""""""""""""""""""""""""""""""""""""""""

Run one policy concurrently across parallel environments, or distribute multi-policy, multi-task
experiments across nodes. Parallel execution makes broad task coverage and deep per-episode
analysis practical within reasonable time.

.. container:: arena-why-feature-links

   :doc:`Explore Arena experiments and parallel environments <../concepts/concept_arena_experiments>`

==================================================================
FILE: docs/pages/references_performance.rst
==================================================================
.. _performance-and-scaling:

Performance and scaling
=======================

Arena performance spans environment creation and evaluation execution. This page reports reference
measurements for three parts of that workflow:

* **Parallel environments within one Run:** advancing many environments together on one GPU to
  increase rollout throughput.
* **Independent Runs across GPUs:** using OSMO to execute Runs concurrently and reduce the time
  needed to finish an Experiment.
* **Agentic environment generation:** producing the first structured environment spec from a prompt,
  then resolving a valid spec into a pool of layouts.

An environment-step is one simulation step completed by one environment. A vectorized step
advances every parallel environment in a Run once. For example, one vectorized step with 256
parallel environments completes 256 environment-steps.

The two evaluation-execution benchmarks used the same camera-free workload: the DROID
Rubik's-cube-into-bowl task at the Maple table, the ``zero_action`` policy that sends zero-valued
actions, and 300 vectorized steps per Run. The agentic-generation benchmark uses the separate
workload described in its section.

.. note::

   These are preliminary reference measurements collected for this release. They show how the
   specified workloads performed on the named hardware and model; they are not performance
   guarantees for other tasks or systems.


.. _performance-parallel-environments:

Parallel environments within one Run
------------------------------------

The single-GPU benchmark ran a fresh Arena process for each environment count on one NVIDIA RTX
5880 Ada Generation GPU with 49,140 MiB of memory. Rollout throughput is the number of parallel
environments divided by the mean time for one vectorized step. It excludes process startup,
environment construction, report generation, and shutdown.

The host also used an Intel Core i9-10920X CPU with 12 cores and 24 threads, 62 GiB of system
memory, Ubuntu 22.04.5, and NVIDIA driver 560.35.05.

.. figure:: ../../images/performance/parallel_environment_throughput.svg
   :alt: Rollout throughput at 1, 64, 256, 512, and 1,024 parallel environments.
   :width: 100%
   :align: center

.. list-table:: Single-GPU rollout results
   :header-rows: 1
   :widths: 25 35 40

   * - Parallel environments
     - Mean vectorized step
     - Rollout throughput
   * - 1
     - 185.0 ms
     - 5.41 environment-steps/s
   * - 64
     - 200.0 ms
     - 319.93 environment-steps/s
   * - 256
     - 234.4 ms
     - 1,092.18 environment-steps/s
   * - 512
     - 280.6 ms
     - 1,824.90 environment-steps/s
   * - 1,024
     - 428.4 ms
     - 2,390.22 environment-steps/s


.. _performance-distributed-runs:

Independent Runs across GPUs with OSMO
--------------------------------------

The distributed benchmark used one Experiment containing eight identical Runs. Each Run created
256 parallel environments, advanced them for 300 steps, and used one NVIDIA L40 GPU. OSMO was
configured to execute at most 1, 2, 4, or 8 Runs at once.

With fewer than eight GPUs, OSMO executed the Runs in consecutive groups. The active Arena
execution time below is the sum of the active time for those groups, from the first Arena process
starting until the last process in each group exited. It includes Arena and Isaac Sim startup,
environment construction, rollout, and shutdown. It excludes OSMO queueing, container-image
downloads, inactive time between groups, and final output collection.

.. figure:: ../../images/performance/distributed_run_speedup.svg
   :alt: Arena execution speedup at 1, 2, 4, and 8 concurrent GPUs.
   :width: 100%
   :align: center

.. list-table:: OSMO distributed-Run results
   :header-rows: 1
   :widths: 20 27 23 15 15

   * - Concurrent Runs and GPUs
     - Scheduling of eight Runs
     - Active Arena execution time
     - Speedup
     - Mean Run duration
   * - 1
     - Eight consecutive Runs
     - 1,255.2 s
     - 1.00x
     - 156.9 s
   * - 2
     - Four groups of two
     - 621.0 s
     - 2.02x
     - 154.6 s
   * - 4
     - Two groups of four
     - 310.2 s
     - 4.05x
     - 154.3 s
   * - 8
     - All eight together
     - 157.8 s
     - 7.95x
     - 154.0 s

Executing all eight Runs at once reduced active Arena execution time from 20 minutes 55 seconds to
2 minutes 38 seconds, a 7.95x speedup. The mean duration of an individual Run changed by less than
2% across the four measurements. All 32 Runs completed successfully; the eight-GPU configuration
used six worker nodes.


Using both scaling axes
-----------------------

The two approaches address different parts of an evaluation and can be combined. Parallel
environments increase the amount of simulation work completed by each Run on its GPU. Distributing
independent Runs lets OSMO execute more of the Experiment at the same time across available GPUs
and worker nodes.


Rollout benchmark scope
-----------------------

* The single-GPU test ran on a local engineering workstation, not a controlled performance lab
  system.
* The workload did not render cameras or run policy inference. Cameras, policies, scene contents,
  and physics settings can change both throughput and capacity.
* The single-GPU and OSMO benchmarks used different GPU models and software builds. Their absolute
  step times should not be compared directly.
* Arena's component timers use CPU wall-clock time without explicit CUDA synchronization. They are
  rollout diagnostics, not GPU kernel measurements.
* Full OSMO submission time is not used for the distributed speedup because container-image cache
  state differed between submissions.


.. _performance-agentic-environment-generation:

Agentic environment generation
------------------------------

This benchmark measures the responsiveness and execution latency of Arena's agentic environment
generation pipeline. It answers two questions:

#. How long after a natural-language request does the agent return its first structured environment spec?
#. How long does Arena take to turn a valid environment spec into a resolved pool of Isaac Lab layouts?


Benchmark definition
^^^^^^^^^^^^^^^^^^^^

The benchmark reports wall-clock p50, p95, and p99 latency. Each environment and configuration was
measured 100 times.

**Time to first environment spec** is measured from the request being sent until the first parseable,
structured environment spec is available:

.. math::

   t_{\text{first spec}} = t_{\text{spec available}} - t_{\text{request sent}}

**Time from valid spec to resolved layouts** is measured from invoking the environment run command until
the layout pool and its object and robot placements are resolved and validated:

.. math::

   t_{\text{resolved layouts}} = t_{\text{layout pool ready}} - t_{\text{environment run command}}

A valid spec passes the fixed automated schema and semantic checks. SimulationApp startup is excluded from
layout-resolution latency.

The benchmark does **not** measure:

* Time to the first valid, repaired, or user-approved spec. The first-spec metric stops at the first parseable spec.
* Correctness, task fidelity, asset selection, semantic quality, or other model-dependent quality measures.
* Time spent reviewing or manually editing a generated spec, layout, task, asset choice, or placement.
* Human-assisted completion rate, review throughput, or time to a human-approved environment.


Benchmark coverage
^^^^^^^^^^^^^^^^^^

The environments vary scene complexity, object count, object source, and whether the objects are homogeneous
or heterogeneous. Layout resolution also varies the number of parallel environments. Each parallel environment
uses five cached layouts.

.. csv-table:: Agentic environment generation base environments
   :header: "Environment family", "Base request", "Variants"
   :widths: 24, 43, 33

   "Tabletop homogeneous pick and place", "DROID picks a banana to a plate on a maple tabletop.", "0, 6, or 14 fruit/vegetable distractors; SimReady beverage can and basket variant"
   "Tabletop heterogeneous pick and place", "DROID picks fruit to a plate on a tabletop.", "Heterogeneous fruit object set"
   "Kitchen homogeneous pick and place", "DROID picks a banana to a plate on a kitchen countertop. DROID is next to the countertop, on the floor.", "0, 6, or 14 fruit/vegetable distractors"
   "Kitchen open door", "DROID opens the fridge door in the kitchen. DROID is next to the fridge, on the floor.", "Referenced articulated fridge"

Factors expected to affect prompt-to-spec latency include the number of objects and relations, scene complexity,
SimReady Search API use, inference endpoint, and agentic model. Factors expected to affect layout resolution
include GPU, layout-pool size, the number of objects and relations, homogeneous versus heterogeneous geometry,
and scene complexity. See :ref:`agentic-env-gen-model-performance-effects` for how model and endpoint
selection affect generation latency and reliability.


Prompt to first environment spec
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The agentic model was ``openai/openai/gpt-5.6-terra`` on an internal endpoint. Requests used NVIDIA campus
Ethernet. Every environment returned a parseable first spec in all 100 trials.

.. figure:: ../../images/agentic_environment_generation/agentic_env_gen_first_spec_p50.png
   :width: 100%
   :align: center
   :alt: Median prompt-to-first-environment-spec latency for the benchmark environments.

   Median prompt-to-first-environment-spec latency. Hatching identifies the heterogeneous-object case.

.. csv-table:: Prompt-to-first-spec results
   :header: "Environment", "Scene", "Objects", "Heterogeneous", "Success", "p50 (s)", "p95 (s)", "p99 (s)"
   :widths: 32, 10, 8, 12, 9, 9, 9, 9

   "tabletop_banana_plate_distractors_0", "Tabletop", "2", "No", "100/100", "4.896", "10.020", "25.582"
   "tabletop_banana_plate_distractors_6", "Tabletop", "8", "No", "100/100", "7.010", "10.586", "15.180"
   "tabletop_banana_plate_distractors_14", "Tabletop", "16", "No", "100/100", "10.218", "14.985", "56.083"
   "tabletop_beverage_can_basket_simready", "Tabletop", "2", "No", "100/100", "9.927", "14.578", "26.546"
   "tabletop_heterogeneous_fruit_plate", "Tabletop", "2", "Yes", "100/100", "6.341", "10.693", "37.385"
   "kitchen_banana_plate_distractors_0", "Kitchen", "2", "No", "100/100", "12.704", "16.624", "27.293"
   "kitchen_banana_plate_distractors_6", "Kitchen", "8", "No", "100/100", "14.683", "20.607", "47.596"
   "kitchen_banana_plate_distractors_14", "Kitchen", "16", "No", "100/100", "18.105", "26.405", "74.618"
   "kitchen_open_fridge_door", "Kitchen", "0", "No", "100/100", "8.954", "18.527", "29.514"


Valid spec to resolved layouts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Layout resolution ran on an NVIDIA RTX 6000 Ada. The layout count is five times the number of parallel
environments.

.. figure:: ../../images/agentic_environment_generation/agentic_env_gen_layout_resolution_p50.png
   :width: 100%
   :align: center
   :alt: Median valid-spec-to-resolved-layout-pool latency by scene and number of parallel environments.

   Median valid-spec-to-resolved-layout-pool latency as parallel environment count increases.

.. dropdown:: Detailed results
   :icon: table

   .. csv-table:: Valid-spec-to-resolved-layout results
      :header: "Environment", "Scene", "Objects", "Heterogeneous", "Envs", "Layouts", "p50 (s)", "p95 (s)", "p99 (s)"
      :widths: 31, 9, 7, 11, 6, 7, 8, 8, 8

      "tabletop_banana_plate_distractors_0", "Tabletop", "2", "No", "1", "5", "2.390", "3.192", "3.527"
      "tabletop_banana_plate_distractors_0", "Tabletop", "2", "No", "16", "80", "2.598", "2.957", "3.315"
      "tabletop_banana_plate_distractors_0", "Tabletop", "2", "No", "64", "320", "3.441", "4.025", "4.377"
      "tabletop_banana_plate_distractors_0", "Tabletop", "2", "No", "256", "1280", "7.065", "8.606", "8.918"
      "tabletop_banana_plate_distractors_6", "Tabletop", "8", "No", "1", "5", "5.882", "6.175", "6.270"
      "tabletop_banana_plate_distractors_6", "Tabletop", "8", "No", "16", "80", "6.609", "7.113", "7.558"
      "tabletop_banana_plate_distractors_6", "Tabletop", "8", "No", "64", "320", "11.217", "11.759", "13.844"
      "tabletop_banana_plate_distractors_6", "Tabletop", "8", "No", "256", "1280", "29.394", "31.400", "31.907"
      "tabletop_banana_plate_distractors_14", "Tabletop", "16", "No", "1", "5", "8.757", "10.257", "12.556"
      "tabletop_banana_plate_distractors_14", "Tabletop", "16", "No", "16", "80", "11.775", "13.197", "15.087"
      "tabletop_banana_plate_distractors_14", "Tabletop", "16", "No", "64", "320", "21.933", "23.591", "24.842"
      "tabletop_banana_plate_distractors_14", "Tabletop", "16", "No", "256", "1280", "62.691", "64.580", "65.778"
      "tabletop_heterogeneous_fruit_plate", "Tabletop", "2", "Yes", "1", "5", "3.234", "3.834", "4.157"
      "tabletop_heterogeneous_fruit_plate", "Tabletop", "2", "Yes", "16", "80", "3.376", "3.627", "3.779"
      "tabletop_heterogeneous_fruit_plate", "Tabletop", "2", "Yes", "64", "320", "4.186", "4.623", "5.235"
      "tabletop_heterogeneous_fruit_plate", "Tabletop", "2", "Yes", "256", "1280", "7.696", "8.076", "9.833"
      "kitchen_banana_plate_distractors_0", "Kitchen", "2", "No", "1", "5", "6.990", "7.639", "7.957"
      "kitchen_banana_plate_distractors_0", "Kitchen", "2", "No", "16", "80", "13.820", "14.357", "14.510"
      "kitchen_banana_plate_distractors_0", "Kitchen", "2", "No", "64", "320", "36.388", "37.213", "37.648"
      "kitchen_banana_plate_distractors_0", "Kitchen", "2", "No", "256", "1280", "136.645", "139.830", "142.016"
      "kitchen_banana_plate_distractors_6", "Kitchen", "8", "No", "1", "5", "12.148", "13.674", "17.569"
      "kitchen_banana_plate_distractors_6", "Kitchen", "8", "No", "16", "80", "23.967", "24.519", "24.774"
      "kitchen_banana_plate_distractors_6", "Kitchen", "8", "No", "64", "320", "68.159", "69.435", "70.180"
      "kitchen_banana_plate_distractors_6", "Kitchen", "8", "No", "256", "1280", "244.293", "248.615", "250.726"
      "kitchen_banana_plate_distractors_14", "Kitchen", "16", "No", "1", "5", "21.098", "22.358", "24.218"
      "kitchen_banana_plate_distractors_14", "Kitchen", "16", "No", "16", "80", "36.449", "37.629", "39.016"
      "kitchen_banana_plate_distractors_14", "Kitchen", "16", "No", "64", "320", "139.507", "142.345", "146.770"
      "kitchen_banana_plate_distractors_14", "Kitchen", "16", "No", "256", "1280", "649.275", "661.445", "679.157"
      "kitchen_open_fridge_door", "Kitchen", "0", "No", "1", "5", "3.234", "3.834", "4.157"
      "kitchen_open_fridge_door", "Kitchen", "0", "No", "16", "80", "3.376", "3.627", "3.779"
      "kitchen_open_fridge_door", "Kitchen", "0", "No", "64", "320", "4.186", "4.623", "5.235"
      "kitchen_open_fridge_door", "Kitchen", "0", "No", "256", "1280", "7.696", "8.075", "9.833"


Tested revisions
----------------

* **Agentic environment generation benchmark, September 4, 2026:** Arena `f641fe9df
  <https://github.com/isaac-sim/IsaacLab-Arena/commit/f641fe9dff9492623ebd8a799d07924801a78ec2>`_.

* **Single-GPU benchmark at 1, 64, and 256 environments, August 27, 2026:** Arena `b0cd0b38e
  <https://github.com/isaac-sim/IsaacLab-Arena/commit/b0cd0b38e660637ee5bc7f8c962994cb1cac4852>`_,
  Isaac Lab `af1bab4dc
  <https://github.com/isaac-sim/IsaacLab/commit/af1bab4dc173ba69b08fab779c14ead61d13fd33>`_, and
  the `camera-free benchmark configuration
  <https://github.com/isaac-sim/IsaacLab-Arena/blob/b0cd0b38e660637ee5bc7f8c962994cb1cac4852/isaaclab_arena_environments/experiment_configs/perflab/camera_free_benchmark_experiment.yaml>`_.
* **Single-GPU follow-up at 512 and 1,024 environments, September 9, 2026:** the same Arena and Isaac
  Lab revisions and camera-free workload.
* **OSMO benchmark, September 6, 2026:** Arena `4ee056866
  <https://github.com/isaac-sim/IsaacLab-Arena/commit/4ee056866b0f222fa166561ed46e2b5bace39445>`_,
  Isaac Lab `bb0c8e1b9
  <https://github.com/isaac-sim/IsaacLab/commit/bb0c8e1b9af381bf13064ec3303e17db79e4b6ef>`_, and
  the `OSMO benchmark configuration
  <https://github.com/isaac-sim/IsaacLab-Arena/blob/4ee056866b0f222fa166561ed46e2b5bace39445/isaaclab_arena_environments/experiment_configs/perflab/osmo/camera_free_scaling_validation_experiment.yaml>`_.

==================================================================
FILE: docs/pages/concepts_policy_index.rst
==================================================================
Policy
======

A policy in Arena is a standard interface between your model and the evaluation
pipeline. You implement one method — ``get_action(env, obs)`` — and the policy
plugs into both the single-job runner and the Experiment Runner without any
changes to either. In bare IsaacLab you would write an ad-hoc inference loop
for each model; Arena's ``PolicyBase`` gives a consistent contract that all
runners depend on.

.. code-block:: python

   policy = ZeroActionPolicy(config=ZeroActionPolicyCfg())
   obs, _ = env.reset()
   action = policy.get_action(env, obs)

Built-in policies
-----------------

Arena ships with four policies:

**ZeroActionPolicy** (``"zero_action"``)
   Returns a zero-filled action tensor. Useful for validating an environment
   without a trained model.

**ReplayActionPolicy** (``"replay"``)
   Replays actions from a recorded episode stored in an HDF5 file.

**RslRlActionPolicy** (``"rsl_rl"``)
   Runs inference with a trained RSL-RL checkpoint. Loads the checkpoint and
   its accompanying ``params/agent.yaml`` automatically.


Writing a custom policy
-----------------------

Define a typed ``PolicyCfg``, subclass ``PolicyBase`` with that config, set a
``name``, register it with its config, and implement ``get_action``:

.. code-block:: python

   from dataclasses import dataclass

   import gymnasium as gym
   import torch
   from gymnasium.spaces.dict import Dict as GymSpacesDict

   from isaaclab_arena.assets.register import register_policy
   from isaaclab_arena.policy.policy_base import PolicyBase, PolicyCfg


   @dataclass
   class MyPolicyCfg(PolicyCfg):
       device: str = "cuda:0"


   @register_policy
   class MyPolicy(PolicyBase[MyPolicyCfg]):
       name = "my_policy"

       def __init__(self, config: MyPolicyCfg):
           super().__init__(config)

       def get_action(self, env: gym.Env, observation: GymSpacesDict) -> torch.Tensor:
           # Your model inference here
           return torch.zeros(env.action_space.shape, device=torch.device(env.unwrapped.device))

Construct the policy by passing its typed configuration directly:

.. code-block:: python

   policy_cfg = MyPolicyCfg(device="cuda:0")
   policy = MyPolicy(policy_cfg)

The typed registration lets the single-job runner generate CLI flags from
``MyPolicyCfg`` and lets the Experiment Runner convert the current
``Job.policy_config_dict`` representation into that same type. See
:doc:`Arena Experiments <../concept_arena_experiments>` for details.

Config fields named ``device`` or ``num_envs`` reuse the corresponding shared
runner flags, so their defaults must match the runner defaults.

.. note::

   ``policy_runner.py`` remains an argparse frontend, but policies do not
   implement argparse methods. The runner generates their flags from the
   registered config and reconstructs it before creating the policy.

==================================================================
FILE: docs/pages/concepts_concept_sensitivity_analysis.rst
==================================================================
Sensitivity Analysis
====================

The sensitivity-analysis toolbox answers a single question about a policy:
*which environment conditions drive success?* Given the per-episode results of an
evaluation sweep — where factors such as lighting, object mass, or table material were
varied — it fits a posterior over those factors conditioned on the outcome (e.g. success
rate) and renders one figure summarising which factor values are associated with success.

Two distinct ideas are at work. *Joint* means all factors are modelled together rather than
one at a time, which is what captures interactions and confounds (see the next section).
*Posterior* means the result is conditioned on the outcome: starting from the prior — the
factor values the sweep actually drew, uniform over their observed ranges — it reweights them
by how often each led to the chosen outcome. So the figure answers *given success, which
factor values were in play?*, not merely *how were the factors distributed in the sweep?*

Why a joint posterior, not a success rate per factor?
-----------------------------------------------------

The simplest analysis would chart a success rate for each factor independently. That hides
the two things that matter most in a multi-factor sweep:

- **Factors interact.** How much light a policy needs can depend on the object — a matte
  object may succeed at low light while a shiny one needs far more. A per-factor
  "success vs light" curve averages over objects and reports one blurry gate that is wrong
  for both. The joint posterior keeps the interaction, so you can condition on a specific
  object and see its gate.
- **Factors confound each other.** If bright-light episodes also happened to use an easy
  object, a per-factor light chart cannot tell which one drove success. Modelling all
  factors together attributes the effect to the factor that actually carries it.

The per-factor rate is a projection of the joint posterior — derivable from it, but not the
other way around. The toolbox therefore always fits the joint — via simulation-based
inference (MNPE or NPE) — and reads the per-factor marginals from it.

How it works
------------

The toolbox is a thin analysis layer over `sbi <https://sbi.readthedocs.io>`_'s
neural posterior estimators. The flow is:

1. **Per-episode input.** The analysis reads a single ``episode_results.jsonl`` — one row per
   episode, holding that episode's recorded variation draws and outcomes.
2. **Schema discovery.** The factors are discovered from the data: each entry in a row's
   ``variations`` block becomes a factor — a number is continuous, a numeric vector splits into
   one continuous factor per component, and a string is categorical (its choices are the labels
   observed across the sweep). Continuous ranges are taken from the data's min/max. There is no
   schema file to author; *which* outcome to condition on is chosen at analysis time.
3. **Inference.** ``SensitivityAnalyzer`` trains an estimator on the full ``(theta, x)`` jointly
   — sbi's terms for the factor values (``theta``) and the per-episode outcomes (``x``) — and
   samples the joint posterior conditioned on a chosen observation (by default, success).
4. **Report.** A probability density curve for each continuous factor and a probability bar
   chart for each categorical factor.

Input
-----

The analysis reads a single ``episode_results.jsonl`` written by the per-episode recorder —
one JSON object per episode. Each row's ``variations`` block holds the sampled factor draws,
and the top-level fields named by ``--outcome`` hold the outcomes (any other top-level fields
are ignored):

.. code-block:: json

   {"job_name": "pi0_sweep", "episode_in_env": 0, "success": true,
    "variations": {"light_intensity": 3200.0, "table_material": "oak",
                   "wrist_camera": [0.01, -0.02, 0.0]}}

The factor schema is discovered from these values, so there is no separate schema file: a
number becomes a continuous factor, a numeric vector splits into one continuous factor per
component (named ``key[0]``, ``key[1]``, …), and a string becomes a categorical factor whose
choices are the labels observed across the sweep. A factor that took a single value across
all episodes carries no information and is dropped.

Choice of estimator
-------------------

``SensitivityAnalyzer`` picks the estimator from the discovered factors automatically:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Schema
     - Estimator
     - Notes
   * - Any categorical factor
     - MNPE
     - Mixed density estimator; handles continuous + categorical factors together.
   * - All continuous factors
     - NPE
     - Models the joint posterior over the continuous factors.

Continuous factors are normalised to ``[0, 1]`` before fitting and de-normalised when
sampling, so factors on very different scales (e.g. light in the thousands, an offset in
the hundredths) train on equal footing. Outcomes are binary (0/1); the default query
conditions on success (1).

Running a report
----------------

Point the report generator at an ``episode_results.jsonl``. The output format follows the
file extension (``.png``, ``.pdf``, …); reports are written under ``eval/`` by default.

.. code-block:: bash

   python -m isaaclab_arena.analysis.sensitivity.generate_report \
     --episode_results episode_results.jsonl \
     --outcome success \
     --output eval/sensitivity_report.png

``--outcome`` selects which per-episode outcome(s) to condition on (top-level field(s) in
each row); it defaults to ``success``. Pass ``--observation`` to set the value per outcome —
since outcomes are binary, use ``1`` for success or ``0`` for failure; it defaults to ``1``
(success). ``--factors`` restricts the analysis to a subset of the recorded variations (by
their ``variations``-block names; a vector variation keeps all its components); by default
every recorded variation is analyzed.

Trying it on synthetic data
---------------------------

A synthetic simulator with a *known* ground truth lets you run the whole pipeline without
Isaac Sim — useful for seeing the output shape and for validating the toolbox
(the recovered posterior should reflect the planted relationship):

.. code-block:: bash

   python -m isaaclab_arena.tests.sensitivity_synthetic \
     --kind continuous \
     --output eval/sensitivity_synthetic_continuous_marginals.png

   NO_AT_BRIDGE=1 pqiv eval/sensitivity_synthetic_continuous_marginals.png

The continuous dataset contains three factors and exercises the NPE path. ``--kind`` also accepts
``mixed`` to exercise the MNPE path with three continuous and two categorical factors.

Reading the output
------------------

.. figure:: ../../images/sensitivity_synthetic_continuous_marginals.png
   :width: 100%
   :alt: Posterior marginals for light intensity, object mass, and camera distance conditioned on success
   :align: center

   Posterior marginals from the continuous synthetic dataset.

Each blue curve is the posterior density for one factor *conditioned on success*. The dashed grey
line is the uniform prior used to draw that factor. Where the posterior rises above the prior,
those values are more common in the success-conditioned samples than in the original sweep. The
shaded 5–95% interval contains the central 90% of the posterior samples.

Compare each curve with the prior in its own panel. Absolute density heights are not comparable
between panels because each factor has different units and a different range.

The three panels recover the relationships planted in the synthetic simulator:

* **Light intensity:** Density shifts toward higher intensities and peaks near the bright end of
  the range, so successful episodes favor brighter lighting.
* **Object mass:** Density shifts toward lower masses and falls toward the high end of the
  range, so successful episodes favor lighter objects.
* **Camera distance:** Density shifts toward shorter distances and peaks around 0.6, so successful
  episodes favor a closer camera.

These curves validate the analysis against known synthetic relationships. For evaluation data,
read the same shapes as associations with success within the sampled sweep, not as proof that a
factor caused the outcome.

Current scope
-------------

- Outcomes are treated as **binary** (0/1). Conditioning defaults to success; a continuous
  outcome is rejected with a clear error rather than silently averaged.
- A **vector** variation draw (e.g. a camera pose offset) is split into one scalar factor per
  component (``key[0]``, ``key[1]``, …), each analysed independently. Components are named by
  position; semantic names (e.g. a camera's lateral vs. depth axis) are a future extension.
- **Factors should be drawn from the prior** the analyzer assumes — uniform over each
  continuous range, and an equal number of episodes per categorical choice. The posterior is
  taken relative to how the sweep drew the factors, so uneven sampling leaks in: a factor with
  no real effect comes out flat only if it was sampled flat, otherwise its posterior tracks the
  sampling frequency. The analyzer warns when a categorical is sampled unevenly, but the clean
  fix is to balance the draws in the sweep.
- The estimators run on CPU and do not require Isaac Sim, so a report can be generated
  anywhere the evaluation JSONL is available.
- Every row in ``episode_results.jsonl`` must come from the same policy, task, and embodiment.

==================================================================
FILE: docs/pages/concepts_agentic_environment_generation_model_selection.rst
==================================================================
.. _agentic-env-gen-model-choice:

Inference Model and Spec Quality
================================

How Arena Uses the Model
-------------------------

Arena does not reason about the scene. It builds a prompt from the catalogs, asks the model for a
JSON object matching the :doc:`ArenaEnvGraphSpec <../environment/environment_definition>` schema,
and validates the result. The model decides
what the environment contains. Arena only checks that the answer is admissible: each
``registry_name`` is registered, each relation kind exists, and each ``prim_path`` is in the
background's prim tree. A bad answer is rejected and saved as ``invalid_<name>.yaml`` with trace
lines, but Arena cannot fix it. The model must support OpenAI-compatible structured outputs
(``response_format={"type": "json_schema", ...}``).

Why Spec Quality Varies
-------------------------

Spec quality tracks model capability. Context length is usually the limiting factor: each pass
sends the full catalog in one request, and a model that cannot hold it answers from the part it
saw. This shows up as an unregistered asset name or an out-of-tree ``prim_path``, not as a length
error. Weaker models also:

* invent asset names
* drop objects
* anchor the scene to the background instead of the counter
* collapse five parallel pick-and-places into one atomic task
* pick a plausible-but-wrong prim out of several similar ones

Prompt Size at Scale
----------------------

Spec inference sends roughly 15 000 characters of catalogs. Prim path resolution sends the
background's entire prim tree — about 30 000 characters (10 000 tokens) for
``lightwheel_robocasa_kitchen`` (886 prims) — so a short-context model fails on that pass first.
Print the current catalog with ``--mode catalog``.

Selecting the Model
-------------------

Each endpoint preset has its own default model, so switching endpoints switches models (see
:ref:`agentic-env-gen-prerequisites`). The CLI runner overrides it per run with ``--model`` and
``--temperature``; the GUI runner selects the endpoint in the generation panel and uses that
endpoint's default model. For the public endpoint, any model in the
`NVIDIA NIM LLM API reference <https://docs.api.nvidia.com/nim/reference/llm-apis>`_ works, as long
as it supports strict structured outputs — a larger context window buys more reliable prim path
resolution.

.. list-table::
   :header-rows: 1
   :widths: 18 16 28 18 14 14

   * - ``ARENA_INFERENCE_ENDPOINT``
     - Accessibility
     - Default model
     - API key variable
     - Pass rate
     - Mean runtime
   * - ``public`` (default)
     - Public (free)
     - ``deepseek-ai/deepseek-v4-pro-0813``
     - ``NVIDIA_API_KEY``
     - 15/15 (100%)
     - 150.66 s
   * - ``internal``
     - NVIDIA internal
     - ``openai/openai/gpt-5.6-terra``
     - ``NV_API_KEY``
     - 15/15 (100%)
     - 12.57 s
   * - ``openai``
     - Public (charged)
     - ``gpt-5.6-terra``
     - ``OPENAI_API_KEY``
     - 15/15 (100%)
     - 10.15 s

.. note::
   The benchmark ran each of five documented prompts three times. Pass rate is the fraction of
   generated specs that matched the expected structure; runtime is the mean end-to-end
   ``generate_spec`` runtime. These results are snapshots rather than guarantees: model output is
   non-deterministic, and service load affects runtime.

.. _agentic-env-gen-model-performance-effects:

How Model and Endpoint Affect Generation Metrics
------------------------------------------------

The model and endpoint both affect generation speed and reliability:

* **Model:** affects whether a spec passes validation and how often Arena must retry. Each retry adds another
  model call and increases runtime.
* **Endpoint:** affects response time through network and server performance. The same model can be faster or
  slower on different endpoints.

For example, Kimi K3 passed all 15 attempts without retries on both endpoints. Its mean runtime was 25.61 seconds
on the internal endpoint and 112.15 seconds on the public endpoint. Pass rates and retry counts also varied across
models.

.. list-table:: Model and endpoint comparison
   :header-rows: 1
   :widths: 13 42 13 16 16

   * - Endpoint
     - Model
     - Pass rate
     - Mean runtime
     - Validation retries
   * - Internal
     - ``azure/anthropic/claude-opus-5``
     - 15/15
     - 11.71 s
     - 0
   * - Internal
     - ``nvidia/zai-org/glm-5.2``
     - 15/15
     - 18.37 s
     - 5
   * - Internal
     - ``nvidia/moonshotai/kimi-k3``
     - 15/15
     - 25.61 s
     - 0
   * - Internal
     - ``nvidia/nvidia/nemotron-3-ultra``
     - 9/15
     - 24.92 s
     - 9
   * - Public
     - ``moonshotai/kimi-k3``
     - 15/15
     - 112.15 s
     - 0
   * - Public
     - ``deepseek-ai/deepseek-v4-pro-0813``
     - 15/15
     - 150.66 s
     - 1
   * - Public
     - ``nvidia/nemotron-3-ultra-550b-a55b``
     - 9/15
     - 149.86 s
     - 8
   * - Public
     - ``openai/gpt-oss-20b``
     - 7/15
     - 333.17 s
     - 4

Each row summarizes 15 attempts: five prompts run three times. The retry count is the total across those attempts.
Mean runtime covers the full ``generate_spec`` call, so it is different from the p50 time-to-first-spec metric on
the :ref:`performance-and-scaling` page. Results can change with model output and endpoint load.

Reviewing the Generated Spec
----------------------------

Output is non-deterministic, even at ``--temperature 0``. Validation only proves a spec is
admissible, not that it is the environment you asked for. Review every generated spec in the
:doc:`GUI live editor <gui_runner>` before generating data or
evaluating a policy against it:

* **Objects** — every object the prompt asked for is there, with no invented extras, and each
  ``registry_name`` is the asset you meant rather than a same-sounding sibling.
* **Anchor and relations** — the ``is_anchor`` subject is what the scene should be built around
  (the counter, not the background), and each ``on`` / ``next_to`` reference points at the
  intended node. This decides where the robot ends up.
* **Task** — the composition (``atomic`` / ``sequential`` / ``parallel``) matches the prompt, with
  one subtask per action and ``pick_up_object`` / ``destination_location`` not swapped.
* **Object references** — the resolved ``prim_path`` is the right prim out of the several similar
  ones a background offers, and an opened articulation carries the correct ``openable_joint_name``.
* **Sim preview** — run it. Objects intersecting geometry, or a robot that cannot reach the task
  objects, show up here and nowhere in validation.

The reviewed YAML can be used to reproduce the environment, but re-running the prompt to create the environment is not.

==================================================================
FILE: docs/pages/example_workflows_example_environments.rst
==================================================================
Example Environments
====================

Isaac Lab Arena ships a catalog of ready-to-run environments under
``isaaclab_arena_environments/``. Environments can be provided in two ways:

* **Python registered environments**: small compositions of the building blocks
  introduced in :doc:`../concepts/environment/index` — **Scene**,
  **Embodiment**, and **Task** — wrapped in an ``ExampleEnvironmentBase``
  subclass and registered with the global ``EnvironmentRegistry``. The
  registered ``Task ID`` is passed as the positional ``example_environment``
  argument to scripts such as ``isaaclab_arena/evaluation/policy_runner.py``.
* **Environment graph YAML specs**: ``ArenaEnvGraphSpec`` files that describe the same
  scene, embodiment, task, objects, and relations declaratively. These are
  passed with ``--env_spec`` and can be generated from prompts by the
  :doc:`agentic_env_gen/index` workflow.

The environments are grouped into three catalogs:

Robolab-Inspired Benchmark
--------------------------

RoboLab environment graph YAMLs live under
``isaaclab_arena_environments/robolab/``. They are generated from natural-language
prompts and consumed with ``--env_spec`` instead of the positional
``example_environment`` name.

See :doc:`robolab_task_catalog` for the list of RoboLab tasks
currently supported in Arena.

Kitchen Benchmark
-----------------

Kitchen benchmark environment graph YAMLs live under
``isaaclab_arena_environments/kitchen_bench/``. They define DROID manipulation
tasks across Lightwheel RoboCasa and Replicator kitchen layouts.

See :doc:`kitchen_bench_catalog` for all 31 environment specs and their Pi
policy executions.

Python Environment Catalog
--------------------------

Python registered environments wrapped in an ``ExampleEnvironmentBase`` subclass
and consumed via the positional ``example_environment`` name. They span
pick-and-place, articulated-object manipulation, sorting, assembly,
goal-pose / lift (RL), sandbox, and sequential / composite tasks.

See :doc:`python_environment_catalog` for the full list with per-environment
Key Specifications tables.



See Also
--------

- :doc:`../concepts/environment/index` — the Scene / Embodiment / Task building blocks used by every environment listed here.
- :doc:`../quickstart/arena_env` — walkthrough of the ``pick_and_place_maple_table`` environment.
- :doc:`../arena_in_your_repo/index` — how to register your own ``ExampleEnvironmentBase`` subclass alongside the built-in ones.

.. toctree::
   :maxdepth: 1
   :hidden:

   robolab_task_catalog
   kitchen_bench_catalog
   python_environment_catalog

==================================================================
FILE: docs/pages/example_workflows_kitchen_bench_catalog.rst
==================================================================
Kitchen Benchmark Catalog
=========================

The kitchen benchmark contains 31 DROID tasks defined as environment graph
YAML specs under ``isaaclab_arena_environments/kitchen_bench/``. Pass a spec
to ``policy_runner.py`` with ``--env_spec`` to run that environment.
Each row links to the source YAML and shows a Pi policy execution recorded from
the maintained DROID external camera.

.. list-table::
   :header-rows: 1
   :widths: 45 55
   :class: kitchen-bench-catalog

   * - Environment graph YAML
     - Pi policy execution
   * - `kitchen_bench_lightwheel_open_cabinet_u_shaped_with_island_farmhouse2.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_open_cabinet_u_shaped_with_island_farmhouse2.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_open_cabinet_u_shaped_with_island_farmhouse2.gif
          :alt: Pi policy opening a cabinet in the U-shaped farmhouse kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_open_freezer_g_shaped_large_scandinavian.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_open_freezer_g_shaped_large_scandinavian.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_open_freezer_g_shaped_large_scandinavian.gif
          :alt: Pi policy opening the freezer in the G-shaped Scandinavian kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_open_fridge.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_open_fridge.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_open_fridge_pi.gif
          :alt: Pi policy opening the refrigerator in the Lightwheel kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_open_fridge_g_shaped_large_scandinavian.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_open_fridge_g_shaped_large_scandinavian.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_open_fridge_g_shaped_large_scandinavian.gif
          :alt: Pi policy opening the refrigerator in the G-shaped Scandinavian kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_open_fridge_u_shaped_with_island_farmhouse2.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_open_fridge_u_shaped_with_island_farmhouse2.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_open_fridge_u_shaped_with_island_farmhouse2.gif
          :alt: Pi policy opening the refrigerator in the U-shaped farmhouse kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_open_microwave.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_open_microwave.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_open_microwave_pi.gif
          :alt: Pi policy opening the microwave in the Lightwheel kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_open_microwave_g_shaped_large_scandinavian.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_open_microwave_g_shaped_large_scandinavian.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_open_microwave_g_shaped_large_scandinavian.gif
          :alt: Pi policy opening the microwave in the G-shaped Scandinavian kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_open_oven_g_shaped_large_scandinavian.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_open_oven_g_shaped_large_scandinavian.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_open_oven_g_shaped_large_scandinavian.gif
          :alt: Pi policy opening the oven in the G-shaped Scandinavian kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_pick_and_place.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_pick_and_place.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_pick_and_place_pi.gif
          :alt: Pi policy placing mustard in a bowl in the Lightwheel kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_pick_lemon_shelf_on_plate_u_shaped_with_island_farmhouse2.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_pick_lemon_shelf_on_plate_u_shaped_with_island_farmhouse2.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_pick_lemon_shelf_on_plate_lightwheel_kitchen_u_shaped_with_island_farmhouse2.gif
          :alt: Pi policy picking a lemon from a shelf onto a plate in the U-shaped farmhouse kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_place_bananas_in_wooden_bowl_u_shaped_with_island_farmhouse2.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_place_bananas_in_wooden_bowl_u_shaped_with_island_farmhouse2.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_place_bananas_in_wooden_bowl_u_shaped_with_island_farmhouse2_pi.gif
          :alt: Pi policy placing bananas in a wooden bowl in the U-shaped farmhouse kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_place_ladle_in_plate_g_shaped_large_scandinavian.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_place_ladle_in_plate_g_shaped_large_scandinavian.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_place_ladle_in_plate_g_shaped_large_scandinavian_pi.gif
          :alt: Pi policy placing a ladle in a plate in the G-shaped Scandinavian kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_place_lime_in_wooden_bowl_l_shaped_scandinavian.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_place_lime_in_wooden_bowl_l_shaped_scandinavian.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_place_lime_in_wooden_bowl_l_shaped_scandinavian_pi.gif
          :alt: Pi policy placing a lime in a wooden bowl in the L-shaped Scandinavian kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_place_pepsi_in_basket_u_shaped_with_island_farmhouse2.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_place_pepsi_in_basket_u_shaped_with_island_farmhouse2.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_place_pepsi_in_basket_u_shaped_with_island_farmhouse2_pi.gif
          :alt: Pi policy placing a Pepsi can in a basket in the U-shaped farmhouse kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_press_left_toaster_cancel_button_g_shaped_large_scandinavian.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_press_left_toaster_cancel_button_g_shaped_large_scandinavian.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_press_left_toaster_cancel_button_g_shaped_large_scandinavian.gif
          :alt: Pi policy pressing the left toaster cancel button in the G-shaped Scandinavian kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_press_right_toaster_cancel_button_g_shaped_large_scandinavian.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_press_right_toaster_cancel_button_g_shaped_large_scandinavian.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_press_right_toaster_cancel_button_g_shaped_large_scandinavian.gif
          :alt: Pi policy pressing the right toaster cancel button in the G-shaped Scandinavian kitchen
          :width: 100%
   * - `kitchen_bench_lightwheel_turn_oven_temperature_knob_g_shaped_large_scandinavian.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_lightwheel_turn_oven_temperature_knob_g_shaped_large_scandinavian.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_lightwheel_turn_oven_temperature_knob_g_shaped_large_scandinavian.gif
          :alt: Pi policy turning the oven temperature knob in the G-shaped Scandinavian kitchen
          :width: 100%
   * - `kitchen_bench_replicator_g_shape_banana_bowl.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_g_shape_banana_bowl.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_g_shape_banana_bowl_pi.gif
          :alt: Pi policy placing a banana in a bowl in the G-shaped kitchen
          :width: 100%
   * - `kitchen_bench_replicator_g_shape_bowl_sink.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_g_shape_bowl_sink.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_g_shape_bowl_sink_pi.gif
          :alt: Pi policy placing a bowl in the sink in the G-shaped kitchen
          :width: 100%
   * - `kitchen_bench_replicator_g_shape_mustard_bowl.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_g_shape_mustard_bowl.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_g_shape_mustard_bowl_pi.gif
          :alt: Pi policy placing mustard in a bowl in the G-shaped kitchen
          :width: 100%
   * - `kitchen_bench_replicator_l_island_banana_bowl.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_l_island_banana_bowl.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_l_island_banana_bowl_pi.gif
          :alt: Pi policy placing a banana in a bowl in the L-shaped island kitchen
          :width: 100%
   * - `kitchen_bench_replicator_l_island_bowl_sink.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_l_island_bowl_sink.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_l_island_bowl_sink_pi.gif
          :alt: Pi policy placing a bowl in the sink in the L-shaped island kitchen
          :width: 100%
   * - `kitchen_bench_replicator_l_island_mustard_bowl.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_l_island_mustard_bowl.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_l_island_mustard_bowl_pi.gif
          :alt: Pi policy placing mustard in a bowl in the L-shaped island kitchen
          :width: 100%
   * - `kitchen_bench_replicator_l_shape_banana_bowl.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_l_shape_banana_bowl.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_l_shape_banana_bowl_pi.gif
          :alt: Pi policy placing a banana in a bowl in the L-shaped kitchen
          :width: 100%
   * - `kitchen_bench_replicator_l_shape_bowl_sink.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_l_shape_bowl_sink.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_l_shape_bowl_sink_pi.gif
          :alt: Pi policy placing a bowl in the sink in the L-shaped kitchen
          :width: 100%
   * - `kitchen_bench_replicator_l_shape_mustard_bowl.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_l_shape_mustard_bowl.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_l_shape_mustard_bowl_pi.gif
          :alt: Pi policy placing mustard in a bowl in the L-shaped kitchen
          :width: 100%
   * - `kitchen_bench_replicator_peninsula_bowl_sink.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_peninsula_bowl_sink.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_peninsula_bowl_sink_pi.gif
          :alt: Pi policy placing a bowl in the sink in the peninsula kitchen
          :width: 100%
   * - `kitchen_bench_replicator_peninsula_mustard_bowl.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_peninsula_mustard_bowl.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_peninsula_mustard_bowl_pi.gif
          :alt: Pi policy placing mustard in a bowl in the peninsula kitchen
          :width: 100%
   * - `kitchen_bench_replicator_u_shape_banana_bowl.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_u_shape_banana_bowl.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_u_shape_banana_bowl_pi.gif
          :alt: Pi policy placing a banana in a bowl in the U-shaped kitchen
          :width: 100%
   * - `kitchen_bench_replicator_u_shape_bowl_sink.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_u_shape_bowl_sink.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_u_shape_bowl_sink_pi.gif
          :alt: Pi policy placing a bowl in the sink in the U-shaped kitchen
          :width: 100%
   * - `kitchen_bench_replicator_u_shape_mustard_bowl.yaml <https://github.com/isaac-sim/IsaacLab-Arena/blob/main/isaaclab_arena_environments/kitchen_bench/kitchen_bench_replicator_u_shape_mustard_bowl.yaml>`_
     - .. image:: ../../images/kitchen_bench/kitchen_bench_replicator_u_shape_mustard_bowl_pi.gif
          :alt: Pi policy placing mustard in a bowl in the U-shaped kitchen
          :width: 100%

==================================================================
FILE: docs/pages/example_workflows_python_environment_catalog.rst
==================================================================
Python Environment Catalog
==========================

Python registered environments are small compositions of the building blocks
introduced in :doc:`../concepts/environment/index` — **Scene**,
**Embodiment**, and **Task** — wrapped in an ``ExampleEnvironmentBase``
subclass and registered with the global ``EnvironmentRegistry``. The
registered ``Task ID`` is passed as the positional ``example_environment``
argument to scripts such as ``isaaclab_arena/evaluation/policy_runner.py``.

The metadata below follows the same structure as the **Key Specifications**
tables in the :doc:`imitation_learning/index` and
:doc:`reinforcement_learning_workflows/index` workflow guides.

.. contents::
   :local:
   :depth: 1


Pick & Place
------------

kitchen_pick_and_place
^^^^^^^^^^^^^^^^^^^^^^

**Task ID:** ``kitchen_pick_and_place``

**Class:** ``KitchenPickAndPlaceEnvironment`` (``isaaclab_arena_environments/kitchen_pick_and_place_environment.py``)

**Task Description:** Pick an object off the kitchen counter top and place it
inside a kitchen cabinet. Supports a single object via ``--object`` or a
heterogeneous ``--object_set`` spawning a different object per environment.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Table-top manipulation
   * - **Skills**
     - Reach, Grasp, Pick & place
   * - **Embodiment**
     - ``franka_ik`` (default), configurable via ``--embodiment``
   * - **Scene**
     - ``kitchen`` background, counter top reference (anchor), cabinet destination
   * - **Objects**
     - Configurable via ``--object`` / ``--object_set`` (e.g. ``tomato_soup_can``, ``cracker_box``)
   * - **Task Class**
     - ``PickAndPlaceTask``
   * - **Object Placement**
     - Relations: ``On(table_top)``, ``AtPosition(x=0.4, y=0.0)``
   * - **CLI Args**
     - ``--object``, ``--object_set``, ``--embodiment``, ``--teleop_device``


pick_and_place_maple_table
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Task ID:** ``pick_and_place_maple_table``

**Class:** ``PickAndPlaceMapleTableEnvironment`` (``isaaclab_arena_environments/pick_and_place_maple_table_environment.py``)

**Task Description:** Tabletop pick-and-place on the maple Robolab table; used
as the introductory ``First Arena Environment`` walkthrough.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Table-top manipulation
   * - **Skills**
     - Reach, Grasp, Pick & place
   * - **Embodiment**
     - ``droid_abs_joint_pos`` (default), configurable via ``--embodiment``
   * - **Scene**
     - ``maple_table_robolab`` background, dome ``light`` (configurable HDR / intensity)
   * - **Objects**
     - Pick: ``rubiks_cube_hot3d_robolab`` (default); Destination: ``bowl_ycb_robolab`` (default); plus optional ``--additional_table_objects``
   * - **Task Class**
     - ``PickAndPlaceTask`` (episode_length_s = 20)
   * - **Object Placement**
     - Relations: ``On(table)``, ``PositionLimitsBox(x=0.55..0.70, y=-0.4..-0.1)``
   * - **CLI Args**
     - ``--pick_up_object``, ``--destination_location``, ``--additional_table_objects``, ``--embodiment``, ``--teleop_device``, ``--hdr``, ``--light_intensity``


galileo_pick_and_place
^^^^^^^^^^^^^^^^^^^^^^

**Task ID:** ``galileo_pick_and_place``

**Class:** ``GalileoPickAndPlaceEnvironment`` (``isaaclab_arena_environments/galileo_pick_and_place_environment.py``)

**Task Description:** Pick up an object in the Galileo lab environment and
place it into a small bin on the shelf.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Table-top manipulation, lab scene
   * - **Skills**
     - Reach, Grasp, Pick & place
   * - **Embodiment**
     - ``gr1_pink`` (default), configurable via ``--embodiment``
   * - **Scene**
     - ``galileo`` lab background; bin lid (``small_bin_grid_01/lid``) used as destination reference
   * - **Objects**
     - ``power_drill`` (default), configurable via ``--object``
   * - **Task Class**
     - ``PickAndPlaceTask``
   * - **CLI Args**
     - ``--object``, ``--embodiment``, ``--teleop_device``


galileo_g1_locomanip_pick_and_place
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Task ID:** ``galileo_g1_locomanip_pick_and_place``

**Class:** ``GalileoG1LocomanipPickAndPlaceEnvironment`` (``isaaclab_arena_environments/galileo_g1_locomanip_pick_and_place_environment.py``)

**Task Description:** The G1 humanoid navigates the lab, squats, and picks an
object off a shelf to place it into a bin on a table to its right. Featured in
the :doc:`locomanipulation/index` workflow.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Room-scale loco-manipulation
   * - **Skills**
     - Squat, Turn, Walk, Pick, Place
   * - **Embodiment**
     - ``g1_wbc_pink`` (default; whole-body controller w/ navigation P-controller in Mimic)
   * - **Scene**
     - ``galileo_locomanip`` background
   * - **Objects**
     - Pick: ``brown_box`` (default); Destination: ``blue_sorting_bin`` (default)
   * - **Task Class**
     - ``PickAndPlaceTask`` with ``G1PickAndPlaceMimicEnvCfg`` injected via ``mimic_env_cfg_factory`` (episode_length_s = 30, force / velocity success thresholds)
   * - **Interop**
     - Isaac Lab Mimic (legacy ``locomanip_pick_and_place_D0`` datagen for the brown-box → blue-bin pair)
   * - **CLI Args**
     - ``--object``, ``--destination``, ``--embodiment``, ``--teleop_device``, ``--task_description``


Articulated Object Manipulation
-------------------------------

gr1_open_microwave
^^^^^^^^^^^^^^^^^^

**Task ID:** ``gr1_open_microwave``

**Class:** ``Gr1OpenMicrowaveEnvironment`` (``isaaclab_arena_environments/gr1_open_microwave_environment.py``)

**Task Description:** The GR1T2 humanoid reaches with its upper body to open a
microwave door. Featured in the
:doc:`static_manipulation/index` workflow.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Table-top manipulation, articulated objects
   * - **Skills**
     - Reach, Open door
   * - **Embodiment**
     - ``gr1_pink`` (default) or ``gr1_joint`` via ``--embodiment``
   * - **Scene**
     - ``kitchen`` background, ``microwave`` placed on the packing table
   * - **Objects**
     - ``microwave`` (articulated); optional ``--object`` placed in front of the microwave
   * - **Task Class**
     - ``OpenDoorTask`` (openness_threshold = 0.8, reset_openness = 0.2, episode_length_s = 5)
   * - **CLI Args**
     - ``--object``, ``--teleop_device``, ``--embodiment``


gr1_turn_stand_mixer_knob
^^^^^^^^^^^^^^^^^^^^^^^^^

**Task ID:** ``gr1_turn_stand_mixer_knob``

**Class:** ``Gr1TurnStandMixerKnobEnvironment`` (``isaaclab_arena_environments/gr1_turn_stand_mixer_knob_environment.py``)

**Task Description:** GR1 humanoid turns the dial on a stand mixer to a
target level.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Table-top manipulation, articulated objects
   * - **Skills**
     - Reach, Grasp knob, Turn
   * - **Embodiment**
     - ``gr1_pink`` (default) or ``gr1_joint`` via ``--embodiment``
   * - **Scene**
     - ``kitchen`` background, ``stand_mixer`` on the packing table
   * - **Objects**
     - ``stand_mixer`` (articulated); optional ``--object`` placed in front
   * - **Task Class**
     - ``TurnKnobTask``
   * - **CLI Args**
     - ``--object``, ``--target_level`` (default 4), ``--reset_level`` (default -1), ``--embodiment``, ``--teleop_device``


press_button
^^^^^^^^^^^^

**Task ID:** ``press_button``

**Class:** ``PressButtonEnvironment`` (``isaaclab_arena_environments/press_button_environment.py``)

**Task Description:** Press the button on a coffee machine.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Table-top manipulation, articulated objects
   * - **Skills**
     - Reach, Press
   * - **Embodiment**
     - ``franka_ik`` (default) via ``--embodiment``
   * - **Scene**
     - ``packing_table`` background, ``coffee_machine`` placed on top
   * - **Objects**
     - ``coffee_machine`` (articulated)
   * - **Task Class**
     - ``PressButtonTask`` (reset_pressedness = 0.8)
   * - **CLI Args**
     - ``--embodiment``, ``--teleop_device``


Sorting
-------

tabletop_sort_cubes
^^^^^^^^^^^^^^^^^^^

**Task ID:** ``tabletop_sort_cubes``

**Class:** ``TableTopSortCubesEnvironment`` (``isaaclab_arena_environments/sorting_environment.py``)

**Task Description:** Sort two cubes into two color-matching containers on a
table.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Table-top manipulation, multi-object
   * - **Skills**
     - Pick, Place, Sort
   * - **Embodiment**
     - ``franka_ik`` (only supported value)
   * - **Scene**
     - ``table`` background (configurable), ``light``
   * - **Objects**
     - ``--objects`` (default ``red_cube green_cube``); ``--destinations`` (default ``red_container green_container``); exactly 2 of each required
   * - **Task Class**
     - ``SortMultiObjectTask`` (custom success force_threshold = 0.1)
   * - **CLI Args**
     - ``--objects``, ``--destinations``, ``--background``, ``--embodiment``, ``--teleop_device``


Assembly
--------

peg_insert
^^^^^^^^^^

**Task ID:** ``peg_insert``

**Class:** ``PegInsertEnvironment`` (``isaaclab_arena_environments/tabletop_peginsert_environment.py``)

**Task Description:** Assemble a peg into a hole on a tabletop.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Tabletop, contact-rich assembly
   * - **Skills**
     - Reach, Grasp, Insert
   * - **Embodiment**
     - ``franka_ik`` (default; assembly high-PD config) via ``--embodiment``
   * - **Scene**
     - ``table`` background (configurable), dome ``light``
   * - **Objects**
     - Pick: ``peg`` (default); Destination: ``hole`` (default)
   * - **Task Class**
     - ``AssemblyTask`` (min_separation = 0.1, randomized x/y/yaw pose range)
   * - **CLI Args**
     - ``--object``, ``--destination_object``, ``--background``, ``--embodiment``, ``--teleop_device``


gear_mesh
^^^^^^^^^

**Task ID:** ``gear_mesh``

**Class:** ``GearMeshEnvironment`` (``isaaclab_arena_environments/tabletop_gearmesh_environment.py``)

**Task Description:** Pick a medium gear and mesh it onto a gear base, with
small and large reference gears already mounted.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Tabletop, contact-rich assembly
   * - **Skills**
     - Reach, Grasp, Mesh
   * - **Embodiment**
     - ``franka_ik`` (default; assembly high-PD config) via ``--embodiment``
   * - **Scene**
     - ``table`` background (configurable), dome ``light``
   * - **Objects**
     - ``gear_base``, ``medium_gear`` (held), ``small_gear`` and ``large_gear`` (auxiliary)
   * - **Task Class**
     - ``AssemblyTask`` (held-fixed-and-auxiliary randomization, min_separation = 0.18)
   * - **CLI Args**
     - ``--background``, ``--embodiment``, ``--teleop_device``


tabletop_place_upright
^^^^^^^^^^^^^^^^^^^^^^

**Task ID:** ``tabletop_place_upright``

**Class:** ``TableTopPlaceUprightEnvironment`` (``isaaclab_arena_environments/tabletop_place_upright_environment.py``)

**Task Description:** Pick a tipped-over mug on the table and place it
upright.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Table-top manipulation, re-orientation
   * - **Skills**
     - Reach, Grasp, Re-orient, Place
   * - **Embodiment**
     - ``agibot`` (only supported value; ``ArmMode.LEFT``)
   * - **Scene**
     - ``table`` background (configurable), ``ground_plane``, ``light``
   * - **Objects**
     - ``mug`` (default) via ``--object``
   * - **Task Class**
     - ``PlaceUprightTask`` (custom event ``randomize_mug_positions``)
   * - **CLI Args**
     - ``--object``, ``--background``, ``--embodiment``, ``--teleop_device``


Goal-Pose / Lift (RL)
---------------------

cube_goal_pose
^^^^^^^^^^^^^^

**Task ID:** ``cube_goal_pose``

**Class:** ``CubeGoalPoseEnvironment`` (``isaaclab_arena_environments/cube_goal_pose_environment.py``)

**Task Description:** Reach a target 6-DoF pose with a cube (goal-conditioned
manipulation).

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Table-top manipulation, goal-conditioned
   * - **Skills**
     - Reach, Grasp, Re-orient
   * - **Embodiment**
     - ``franka_ik`` (default) via ``--embodiment``
   * - **Scene**
     - ``table`` background (configurable), ``light``
   * - **Objects**
     - ``dex_cube`` (default) via ``--object``
   * - **Task Class**
     - ``GoalPoseTask`` (target_z_range = [0.2, 1.0], target_orientation_xyzw = yaw 90°, tolerance = 0.2 rad)
   * - **CLI Args**
     - ``--object``, ``--background``, ``--embodiment``, ``--teleop_device``


lift_object
^^^^^^^^^^^

**Task ID:** ``lift_object``

**Class:** ``LiftObjectEnvironment`` (``isaaclab_arena_environments/lift_object_environment.py``)

**Task Description:** Reinforcement-learning task in which the Franka Panda
learns to grasp and lift an object to a commanded target position. Featured in
the :doc:`reinforcement_learning/index` workflow.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Table-top manipulation, RL training
   * - **Skills**
     - Reach, Grasp, Lift
   * - **Embodiment**
     - ``franka_joint_pos`` (default; joint-position control yields better RL success than IK) via ``--embodiment``
   * - **Scene**
     - ``table`` background, ``ground_plane``, ``light``
   * - **Objects**
     - ``dex_cube`` (default) via ``--object``
   * - **Task Class**
     - ``LiftObjectTaskRL`` (minimum_height_to_lift = 0.04, episode_length_s = 5)
   * - **Training Method**
     - Trained in Isaac Lab via Reinforcement Learning (RSL-RL PPO; ``rl_policy_cfg`` = ``base_rsl_rl_policy:RLPolicyCfg``)
   * - **CLI Args**
     - ``--object``, ``--embodiment``, ``--teleop_device``, ``--rl_training_mode``


dexsuite_lift
^^^^^^^^^^^^^

**Task ID:** ``dexsuite_lift``

**Class:** ``DexsuiteLiftEnvironment`` (``isaaclab_arena_environments/dexsuite_lift_environment.py``)

**Task Description:** Evaluation wrapper around the Isaac Lab
``Isaac-Lift-KukaAllegro`` MDP. The Kuka arm with an Allegro
dexterous hand lifts a procedurally generated cuboid to a commanded target
position. Featured in the
:doc:`dexsuite_lift/index` workflow.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Dexterous manipulation, contact-rich, RL evaluation
   * - **Skills**
     - Reach, Grasp, Lift (multi-finger)
   * - **Embodiment**
     - ``kuka_allegro`` (fixed)
   * - **Scene**
     - ``procedural_table`` background, ``ground_plane``, ``light``
   * - **Objects**
     - ``procedural_cube`` (randomized initial pose with a wide ``PoseRange``)
   * - **Task Class**
     - ``DexsuiteLiftTask`` (object_pose command, position-only, resampled every 2–3 s)
   * - **Training Method**
     - Pre-trained in Isaac Lab via ``KukaAllegroPPORunnerCfg`` (RSL-RL PPO)
   * - **Physics Backend**
     - PhysX (default) or Newton (``--presets newton``)
   * - **CLI Args**
     - *(none environment-specific; uses common ``ArenaEnvBuilder`` flags)*


Sandbox
-------

gr1_table_multi_object_no_collision
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Task ID:** ``gr1_table_multi_object_no_collision``

**Class:** ``GR1TableMultiObjectNoCollisionEnvironment`` (``isaaclab_arena_environments/gr1_table_multi_object_no_collision_environment.py``)

**Task Description:** Sandbox scene for testing the relation solver: an office
table with multiple objects placed via ``On(table)`` plus the built-in
no-overlap solver. No success task — useful for ``policy_runner`` smoke tests
with ``zero_action`` or any policy.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Sandbox, multi-object placement
   * - **Skills**
     - *(none — no task)*
   * - **Embodiment**
     - ``gr1_joint`` (default) via ``--embodiment``
   * - **Scene**
     - ``ground_plane``, ``office_table``, ``light``, table-top anchor
   * - **Objects**
     - Default set: ``cracker_box``, ``sugar_box``, ``tomato_soup_can``, ``dex_cube``, ``power_drill``, ``red_container`` (override via ``--objects``)
   * - **Task Class**
     - ``NoTask`` (optional time-out termination via ``--episode_length_s``)
   * - **CLI Args**
     - ``--objects``, ``--embodiment``, ``--teleop_device``, ``--episode_length_s``


Sequential / Composite Tasks
----------------------------

put_item_in_fridge_and_close_door
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Task ID:** ``put_item_in_fridge_and_close_door``

**Class:** ``GR1PutAndCloseDoorEnvironment`` (``isaaclab_arena_environments/gr1_put_and_close_door_environment.py``)

**Task Description:** GR1 humanoid sequentially picks an object, places it on
the refrigerator shelf, then closes the refrigerator door. Featured in the
:doc:`sequential_static_manipulation/index` workflow.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Sequential manipulation, articulated objects
   * - **Skills**
     - Pick, Place, Close door
   * - **Embodiment**
     - ``gr1_pink`` (default) via ``--embodiment``
   * - **Scene**
     - ``lightwheel_kitchen_one_wall_farmhouse1`` background, ``light``, kitchen counter anchor
   * - **Objects**
     - Pick: ``ranch_dressing_hope_robolab`` (default), or ``--object_set`` for heterogeneous spawning; Destination: refrigerator shelf reference; Container: ``refrigerator`` (articulated)
   * - **Task Class**
     - ``PutAndCloseDoorTask`` (sequential: ``PickAndPlaceTask`` → ``CloseDoorTask``, episode_length_s = 10)
   * - **Interop**
     - Isaac Lab Mimic (``put_and_close_door_task_D0`` datagen)
   * - **CLI Args**
     - ``--object``, ``--object_set``, ``--embodiment``, ``--teleop_device``


franka_put_and_close_door
^^^^^^^^^^^^^^^^^^^^^^^^^

**Task ID:** ``franka_put_and_close_door``

**Class:** ``FrankaPutAndCloseDoorEnvironment`` (``isaaclab_arena_environments/franka_put_and_close_door_environment.py``)

**Task Description:** Sequential pick-and-place of an object into a
microwave, followed by closing the microwave door.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Property
     - Value
   * - **Tags**
     - Sequential manipulation, articulated objects
   * - **Skills**
     - Pick, Place, Close door
   * - **Embodiment**
     - ``franka_ik`` (default) via ``--embodiment``
   * - **Scene**
     - ``kitchen`` background, ``microwave`` (articulated, starts open)
   * - **Objects**
     - Pick: ``dex_cube`` (default) via ``--object``; Container: ``microwave``
   * - **Task Class**
     - ``FrankaPutAndCloseDoorTask`` (sequential: ``PickAndPlaceTask`` → ``CloseDoorTask``)
   * - **CLI Args**
     - ``--object``, ``--embodiment``, ``--teleop_device``


See Also
--------

- :doc:`../concepts/environment/index` — the Scene / Embodiment / Task building blocks used by every environment listed here.
- :doc:`../quickstart/arena_env` — walkthrough of the ``pick_and_place_maple_table`` environment.
- :doc:`../arena_in_your_repo/index` — how to register your own ``ExampleEnvironmentBase`` subclass alongside the built-in ones.

==================================================================
FILE: isaaclab_arena_environments/robolab/task_catalog.md
==================================================================
# RoboLab Task Catalog

[120 Robolab tasks](https://github.com/NVlabs/RoboLab/blob/main/robolab/tasks/README.md) and their Arena counterparts when available. Arena specs are split into reusable scene YAMLs under `scenes/` and task YAMLs under `tasks/` that include the scene via a top-level `external_yaml:` path.

<style>
/* Fit the 3-column catalog within the Sphinx article width (no horizontal
   scroller). The theme wraps tables in .pst-scrollable-table-container. */
#robolab-task-catalog .pst-scrollable-table-container {
  overflow-x: visible;
}

#robolab-task-catalog table.table {
  width: 100%;
  table-layout: fixed;
}

#robolab-task-catalog table.table th:nth-child(1),
#robolab-task-catalog table.table td:nth-child(1) {
  width: 40%;
}

#robolab-task-catalog table.table th:nth-child(2),
#robolab-task-catalog table.table td:nth-child(2) {
  width: 30%;
}

#robolab-task-catalog table.table th:nth-child(3),
#robolab-task-catalog table.table td:nth-child(3) {
  width: 30%;
}

#robolab-task-catalog table.table td,
#robolab-task-catalog table.table th {
  white-space: normal;
  word-wrap: break-word;
  overflow-wrap: anywhere;
  vertical-align: top;
}

#robolab-task-catalog table.table img {
  max-width: 100%;
  width: 210px;
  height: auto;
}
</style>

| Arena task spec | RoboLab scene image | RoboLab task |
| --- | --- | --- |
| [banana_in_bowl.yaml](tasks/banana_in_bowl.yaml)<br>scene: [banana_bowl.yaml](scenes/banana_bowl.yaml)<br>prompt: droid Pick up the banana and place it in the bowl. Using maple table background. | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/banana_bowl.png" alt="banana_bowl.png" width="210" /><br>[banana_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/banana_bowl.png)<br>object count: 2 | BananaInBowlTask<br>Pick up the banana and place it in the bowl<br>subtask count: 1 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/bowls_2_table.png" alt="bowls_2_table.png" width="210" /><br>[bowls_2_table.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bowls_2_table.png)<br>object count: 2 | BowlStackingLeftOnRightTask<br>Stack the left bowl on the right bowl<br>subtask count: 1 |
|  | [bowls_2_table.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bowls_2_table.png) | BowlStackingRightOnLeftTask<br>Stack the right bowl on the left bowl<br>subtask count: 1 |
| [butter_above_raisin.yaml](tasks/butter_above_raisin.yaml)<br>scene: [butter_raisin_box.yaml](scenes/butter_raisin_box.yaml)<br>prompt: droid Pick up the butter box and place it on top of the raisin box. Using maple table background | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/butter_raisin_box.png" alt="butter_raisin_box.png" width="210" /><br>[butter_raisin_box.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/butter_raisin_box.png)<br>object count: 2 | ButterAboveRaisinTask<br>Pick up the butter box and place it on top of the raisin box<br>subtask count: 1 |
| [mustard_above_raisin.yaml](tasks/mustard_above_raisin.yaml)<br>scene: [mustard_raisin_box.yaml](scenes/mustard_raisin_box.yaml)<br>prompt: droid Place the mustard on the raisin box. Using maple table background | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/mustard_raisin_box.png" alt="mustard_raisin_box.png" width="210" /><br>[mustard_raisin_box.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/mustard_raisin_box.png)<br>object count: 2 | MustardAboveRaisinTask<br>Place the mustard on the raisin box.<br>subtask count: 1 |
| [rubiks_cube.yaml](tasks/rubiks_cube.yaml)<br>scene: [rubiks_cube_bowl.yaml](scenes/rubiks_cube_bowl.yaml)<br>prompt: droid put the rubiks cube in the bowl. Using maple table background | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/rubiks_cube_bowl.png" alt="rubiks_cube_bowl.png" width="210" /><br>[rubiks_cube_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/rubiks_cube_bowl.png)<br>object count: 2 | RubiksCubeTask<br>Put the cube in the bowl<br>subtask count: 1 |
| [larger_object_raisin_box_in_bin.yaml](tasks/larger_object_raisin_box_in_bin.yaml)<br>scene: [butter_raisin_box_grey_bin.yaml](scenes/butter_raisin_box_grey_bin.yaml)<br>prompt: droid place the raisin box into the grey bin on the maple table. Other objects on the table as distractors: butter | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/butter_raisin_box_grey_bin.png" alt="butter_raisin_box_grey_bin.png" width="210" /><br>[butter_raisin_box_grey_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/butter_raisin_box_grey_bin.png)<br>object count: 3 | LargerObjectRaisinBoxInBinTask<br>Place the larger object in the grey bin.<br>subtask count: 1 |
| [smaller_object_butter_in_bin.yaml](tasks/smaller_object_butter_in_bin.yaml)<br>scene: [butter_raisin_box_grey_bin.yaml](scenes/butter_raisin_box_grey_bin.yaml) | [butter_raisin_box_grey_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/butter_raisin_box_grey_bin.png) | SmallerObjectButterInBinTask<br>Place the smaller object in the grey bin.<br>subtask count: 1 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/rubiks_cube_banana_bowl.png" alt="rubiks_cube_banana_bowl.png" width="210" /><br>[rubiks_cube_banana_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/rubiks_cube_banana_bowl.png)<br>object count: 3 | RubiksCubeOrBananaTask<br>Put the cube or the banana in the bowl<br>subtask count: 1 |
| [banana_then_rubiks_cube.yaml](tasks/banana_then_rubiks_cube.yaml)<br>scene: [rubiks_cube_banana_bowl.yaml](scenes/rubiks_cube_banana_bowl.yaml)<br>prompt: droid put the banana then the cube in the bowl. Using maple table background | [rubiks_cube_banana_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/rubiks_cube_banana_bowl.png) | BananaThenRubiksCubeTask<br>put the banana then the cube in the bowl<br>subtask count: 2 |
| [rubiks_cube_and_banana.yaml](tasks/rubiks_cube_and_banana.yaml)<br>scene: [rubiks_cube_banana_bowl.yaml](scenes/rubiks_cube_banana_bowl.yaml) | [rubiks_cube_banana_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/rubiks_cube_banana_bowl.png) | RubiksCubeAndBananaTask<br>Put the cube and the banana in the bowl<br>subtask count: 2 |
| [rubiks_cube_then_banana.yaml](tasks/rubiks_cube_then_banana.yaml)<br>scene: [rubiks_cube_banana_bowl.yaml](scenes/rubiks_cube_banana_bowl.yaml) | [rubiks_cube_banana_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/rubiks_cube_banana_bowl.png) | RubiksCubeThenBananaTask<br>Put the cube then the banana in the bowl<br>subtask count: 2 |
|  | [rubiks_cube_banana_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/rubiks_cube_banana_bowl.png) | RubiksCubeBehindBowlTask<br>Put the rubiks cube behind the bowl<br>subtask count: 3 |
|  | [rubiks_cube_banana_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/rubiks_cube_banana_bowl.png) | RubiksCubeInFrontOfBowlTask<br>Put the rubiks cube in front of the bowl<br>subtask count: 3 |
|  | [rubiks_cube_banana_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/rubiks_cube_banana_bowl.png) | RubiksCubeLeftOfBowlTask<br>Put the rubiks cube to the left of the bowl<br>subtask count: 3 |
| [mustard_in_left_bin.yaml](tasks/mustard_in_left_bin.yaml)<br>scene: [two_bin.yaml](scenes/two_bin.yaml)<br>prompt: Two grey bins and a mustard on the maple table. Left grey bin is on the left of the right grey bin. Droid put the mustard in the left bin. | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/two_bin.png" alt="two_bin.png" width="210" /><br>[two_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/two_bin.png)<br>object count: 3 | MustardInLeftBinTask<br>Put the mustard in the left bin<br>subtask count: 1 |
| [mustard_in_right_bin.yaml](tasks/mustard_in_right_bin.yaml)<br>scene: [two_bin.yaml](scenes/two_bin.yaml) | [two_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/two_bin.png) | MustardInRightBinTask<br>Put the mustard in the right bin<br>subtask count: 1 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/blue.png" alt="blue.png" width="210" /><br>[blue.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/blue.png)<br>object count: 3 | PickUpBluePitcherTask<br>Pick up the large blue pitcher<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/rubiks_cube_3.png" alt="rubiks_cube_3.png" width="210" /><br>[rubiks_cube_3.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/rubiks_cube_3.png)<br>object count: 3 | Stack3RubiksCubeTask<br>Stack the rubiks cubes in a tower<br>subtask count: 2 |
| [sauce_bottles_crate.yaml](tasks/sauce_bottles_crate.yaml)<br>scene: [bottles_crate.yaml](scenes/bottles_crate.yaml)<br>prompt: Using maple table background. Droid place the bbq sauce bottle into the purple crate on the table. Other objects on the table as distractors: ceramic mug, salad dressing bottle | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/bottles_crate.png" alt="bottles_crate.png" width="210" /><br>[bottles_crate.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bottles_crate.png)<br>object count: 4 | SauceBottlesCrateTask<br>Put the red bbq sauce bottle in the crate<br>subtask count: 1 |
| [food_packing_1_boxes.yaml](tasks/food_packing_1_boxes.yaml)<br>scene: [foodpacking_1bin_1box_1can.yaml](scenes/foodpacking_1bin_1box_1can.yaml)<br>prompt: Using maple table background. Droid place the cheez it box into the bin a06 on the table. Other objects on the table as distractors: mustard, tomato soup can | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/foodpacking_1bin_1box_1can.png" alt="foodpacking_1bin_1box_1can.png" width="210" /><br>[foodpacking_1bin_1box_1can.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/foodpacking_1bin_1box_1can.png)<br>object count: 4 | FoodPacking1BoxesTask<br>Pack boxed foods into the bin<br>subtask count: 1 |
| [food_packing_1_cans.yaml](tasks/food_packing_1_cans.yaml)<br>scene: [foodpacking_1bin_1box_1can.yaml](scenes/foodpacking_1bin_1box_1can.yaml) | [foodpacking_1bin_1box_1can.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/foodpacking_1bin_1box_1can.png) | FoodPacking1CansTask<br>Pack canned foods into the bin<br>subtask count: 1 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/green.png" alt="green.png" width="210" /><br>[green.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/green.png)<br>object count: 4 | PickUpGreenObjectTask<br>Pick up the green vegetable block<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/colored_blocks.png" alt="colored_blocks.png" width="210" /><br>[colored_blocks.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/colored_blocks.png)<br>object count: 4 | BlockStackingOrderAgnosticTask<br>Stack the blocks into a tower<br>subtask count: 3 |
|  | [colored_blocks.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/colored_blocks.png) | BlockStackingSpecifiedOrderTask<br>Stack the blocks in the order from bottom to top: red, blue, green, yellow<br>subtask count: 3 |
| [banana_on_plate.yaml](tasks/banana_on_plate.yaml)<br>scene: [bagel_plate_banana_bowl.yaml](scenes/bagel_plate_banana_bowl.yaml)<br>prompt: droid pick up the banana and put it on the plate. Using maple table background. Other objects on the table as distractors: two bagels, bowl | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/bagel_plate_banana_bowl.png" alt="bagel_plate_banana_bowl.png" width="210" /><br>[bagel_plate_banana_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bagel_plate_banana_bowl.png)<br>object count: 5 | BananaOnPlateTask<br>Pick up the banana and put it on the plate<br>subtask count: 1 |
| [bagels_on_plate.yaml](tasks/bagels_on_plate.yaml)<br>scene: [bagel_plate_banana_bowl.yaml](scenes/bagel_plate_banana_bowl.yaml)<br>prompt: droid put the bagels on the plate. Using maple table background. Other objects on the table as distractors: banana, bowl | [bagel_plate_banana_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bagel_plate_banana_bowl.png) | BagelsOnPlateTask<br>Put the bagels on the plate<br>subtask count: 2 |
| [bowl_in_bin.yaml](tasks/bowl_in_bin.yaml)<br>scene: [bin_mug_mustard_marker_bowl.yaml](scenes/bin_mug_mustard_marker_bowl.yaml)<br>prompt: droid put the bowl in the grey bin. Using maple table background. Other objects on the table as distractors: mustard, dry erase marker, mug | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/bin_mug_mustard_marker_bowl.png" alt="bin_mug_mustard_marker_bowl.png" width="210" /><br>[bin_mug_mustard_marker_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bin_mug_mustard_marker_bowl.png)<br>object count: 5 | BowlInBinTask<br>put the bowl in the grey bin<br>subtask count: 1 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/shelf_mugs_jug_bowl.png" alt="shelf_mugs_jug_bowl.png" width="210" /><br>[shelf_mugs_jug_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/shelf_mugs_jug_bowl.png)<br>object count: 5 | PutBowlOnShelfTopTask<br>Put the serving bowl anywhere on the shelf in front of you<br>subtask count: 1 |
|  | [shelf_mugs_jug_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/shelf_mugs_jug_bowl.png) | PutMugsOnShelfTask<br>Put the two mugs on the shelf<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/mugs_on_shelf.png" alt="mugs_on_shelf.png" width="210" /><br>[mugs_on_shelf.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/mugs_on_shelf.png)<br>object count: 5 | TakeMugsOffOfShelfTask<br>Take the mugs off the shelf<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/rubiks_cube_banana_bowl_mug_bin.png" alt="rubiks_cube_banana_bowl_mug_bin.png" width="210" /><br>[rubiks_cube_banana_bowl_mug_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/rubiks_cube_banana_bowl_mug_bin.png)<br>object count: 5 | RedDishesInBinTask<br>Put the red dishware in the grey bin<br>subtask count: 2 |
|  | [rubiks_cube_banana_bowl_mug_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/rubiks_cube_banana_bowl_mug_bin.png) | RedItemsInBinTask<br>Put all the red things in the grey bin<br>subtask count: 2 |
|  | [rubiks_cube_banana_bowl_mug_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/rubiks_cube_banana_bowl_mug_bin.png) | RubiksCubeRightOfBowlTask<br>Put the rubiks cube to the right of the bowl<br>subtask count: 3 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/bananas_5_grey_bin.png" alt="bananas_5_grey_bin.png" width="210" /><br>[bananas_5_grey_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bananas_5_grey_bin.png)<br>object count: 6 | BananasInBinOneMoreTask<br>Put one (1) more bananas in the grey bin.<br>subtask count: 1 |
|  | [bananas_5_grey_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bananas_5_grey_bin.png) | BananasInBinThreeTotalTask<br>Make sure there are 3 (three) bananas in the grey bin.<br>subtask count: 1 |
|  | [bananas_5_grey_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bananas_5_grey_bin.png) | BananasOutOfBinTask<br>Take the bananas out<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/bananas_5_in_crate.png" alt="bananas_5_in_crate.png" width="210" /><br>[bananas_5_in_crate.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bananas_5_in_crate.png)<br>object count: 6 | BananasInCrateTask<br>Put 2 bananas in the crate<br>subtask count: 1 |
| [clamp_in_right_bin.yaml](tasks/clamp_in_right_bin.yaml)<br>scene: [tools_container.yaml](scenes/tools_container.yaml)<br>prompt: Two bins on maple table. container\_f24 bin is on the left of bin\_b04 bin. droid put the spring clamp in the right bin. Other objects on the table as distractors: two hammers, cordless drill | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/tools_container.png" alt="tools_container.png" width="210" /><br>[tools_container.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/tools_container.png)<br>object count: 6 | ClampInRightBinTask<br>Put the spring clamp in the right bin<br>subtask count: 1 |
| [hammers_in_left_bin.yaml](tasks/hammers_in_left_bin.yaml)<br>scene: [tools_container.yaml](scenes/tools_container.yaml) | [tools_container.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/tools_container.png) | HammersInLeftBinTask<br>Put the red hammer and black hammer in the left bin<br>subtask count: 2 |
| [non_hammer_tools_in_right_bin.yaml](tasks/non_hammer_tools_in_right_bin.yaml)<br>scene: [tools_container.yaml](scenes/tools_container.yaml) | [tools_container.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/tools_container.png) | NonHammerToolsInRightBinTask<br>Put the non-hammer tools in the right bin<br>subtask count: 2 |
|  | [tools_container.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/tools_container.png) | ToolOrganizationBothTask<br>Put hammers in the right bin and do not touch anything else<br>subtask count: 2 |
| [hammers_in_left_bin.yaml](tasks/hammers_in_left_bin.yaml)<br>scene: [tools_container.yaml](scenes/tools_container.yaml)<br>note: Original RoboLab ``ToolOrganizationTask`` is identical to ``HammersInLeftBinTask``; Arena keeps a single YAML. | [tools_container.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/tools_container.png) | ToolOrganizationTask<br>Put the red hammer and black hammer in the left bin<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/foodpacking_1bin_2box_2can.png" alt="foodpacking_1bin_2box_2can.png" width="210" /><br>[foodpacking_1bin_2box_2can.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/foodpacking_1bin_2box_2can.png)<br>object count: 6 | FoodPacking2BoxesTask<br>Pack boxed foods into the bin<br>subtask count: 2 |
|  | [foodpacking_1bin_2box_2can.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/foodpacking_1bin_2box_2can.png) | FoodPacking2CansTask<br>Pack canned foods into the bin<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/mugs4_measuringcup_drill_bowl.png" alt="mugs4_measuringcup_drill_bowl.png" width="210" /><br>[mugs4_measuringcup_drill_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/mugs4_measuringcup_drill_bowl.png)<br>object count: 7 | PickDrillTask<br>Pick up the cordless drill.<br>subtask count: 1 |
|  | [mugs4_measuringcup_drill_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/mugs4_measuringcup_drill_bowl.png) | ReorientRedMugTask<br>Put the red mug upright so that the opening is facing upwards.<br>subtask count: 1 |
|  | [mugs4_measuringcup_drill_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/mugs4_measuringcup_drill_bowl.png) | StackWhiteMugsTask<br>Stack the white mugs on top of each other.<br>subtask count: 2 |
|  | [mugs4_measuringcup_drill_bowl.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/mugs4_measuringcup_drill_bowl.png) | ReorientAllMugsTask<br>Reorient all the mugs upright so that the opening is facing upwards.<br>subtask count: 3 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/mugs4_measuringcup_drill_bowl_v2.png" alt="mugs4_measuringcup_drill_bowl_v2.png" width="210" /><br>[mugs4_measuringcup_drill_bowl_v2.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/mugs4_measuringcup_drill_bowl_v2.png)<br>object count: 7 | ReorientWhiteMugsTask<br>Make sure all the white mugs are upright so that the opening is facing upwards.<br>subtask count: 1 |
|  | [mugs4_measuringcup_drill_bowl_v2.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/mugs4_measuringcup_drill_bowl_v2.png) | TakeMeasuringSpoonOutTask<br>Take the white colored measuring spoon out of the red bowl and put it on the table.<br>subtask count: 1 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/shelf_with_cleaning_products.png" alt="shelf_with_cleaning_products.png" width="210" /><br>[shelf_with_cleaning_products.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/shelf_with_cleaning_products.png)<br>object count: 8 | OneBottleInSquarePailTask<br>Put any white plastic bottle in the square pail<br>subtask count: 1 |
|  | [shelf_with_cleaning_products.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/shelf_with_cleaning_products.png) | OneBottleOnShelfTask<br>Put any white plastic bottle on the shelf<br>subtask count: 1 |
|  | [shelf_with_cleaning_products.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/shelf_with_cleaning_products.png) | ReorientJugTask<br>Stand the jug upright<br>subtask count: 1 |
|  | [shelf_with_cleaning_products.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/shelf_with_cleaning_products.png) | JugsOnShelfTask<br>Put all the jugs on the shelf<br>subtask count: 2 |
|  | [shelf_with_cleaning_products.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/shelf_with_cleaning_products.png) | PlasticBottlesInSquarePailTask<br>Put all the small plastic bottles in the square pail<br>subtask count: 3 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/wire_shelf_mugs_plate_spatula.png" alt="wire_shelf_mugs_plate_spatula.png" width="210" /><br>[wire_shelf_mugs_plate_spatula.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/wire_shelf_mugs_plate_spatula.png)<br>object count: 8 | TakeSpatulaOffShelfTask<br>Take the spatula off the shelf and put it on the table<br>subtask count: 1 |
|  | [wire_shelf_mugs_plate_spatula.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/wire_shelf_mugs_plate_spatula.png) | PutTwoMugsOnShelfTask<br>Put two (2) mugs on the wire shelf<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/cartons_in_crate.png" alt="cartons_in_crate.png" width="210" /><br>[cartons_in_crate.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/cartons_in_crate.png)<br>object count: 8 | RecycleCartonTask<br>Put the recyclable cartons in the grey bin<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/cartons_in_vertical_crate.png" alt="cartons_in_vertical_crate.png" width="210" /><br>[cartons_in_vertical_crate.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/cartons_in_vertical_crate.png)<br>object count: 8 | RecycleCartonsVerticalCrateTask<br>Put the cartons that can be recycled in the vertical crate<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/cartons_on_box.png" alt="cartons_on_box.png" width="210" /><br>[cartons_on_box.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/cartons_on_box.png)<br>object count: 8 | RecycleCartonsOnBoxTask<br>Put the cartons that can be recycled on the box<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/mug_banana_ketchup_bowl_rubiks3_bin.png" alt="mug_banana_ketchup_bowl_rubiks3_bin.png" width="210" /><br>[mug_banana_ketchup_bowl_rubiks3_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/mug_banana_ketchup_bowl_rubiks3_bin.png)<br>object count: 8 | UnstackRubiksCubeTask<br>Unstack the rubiks cube tower<br>subtask count: 2 |
|  | [mug_banana_ketchup_bowl_rubiks3_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/mug_banana_ketchup_bowl_rubiks3_bin.png) | YellowAndWhiteObjectsInBinTask<br>Put all white objects and yellow objects in the grey bin<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/foodpacking_1bin_3box_3can.png" alt="foodpacking_1bin_3box_3can.png" width="210" /><br>[foodpacking_1bin_3box_3can.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/foodpacking_1bin_3box_3can.png)<br>object count: 8 | FoodPacking3BoxesTask<br>Pack boxed foods into the bin<br>subtask count: 3 |
|  | [foodpacking_1bin_3box_3can.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/foodpacking_1bin_3box_3can.png) | FoodPacking3CansTask<br>Pack canned foods into the bin<br>subtask count: 3 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/objects_around_table.png" alt="objects_around_table.png" width="210" /><br>[objects_around_table.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/objects_around_table.png)<br>object count: 8 | WhiteMugInCenterOfTableTask<br>Put the white mug in the center of the table.<br>subtask count: 3 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/food_packing.png" alt="food_packing.png" width="210" /><br>[food_packing.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/food_packing.png)<br>object count: 9 | FoodPackingByColorTask<br>Pack yellow objects in right container and blue object in the left container<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/mugs2_bananas2_ketchup_rubiks3_bin.png" alt="mugs2_bananas2_ketchup_rubiks3_bin.png" width="210" /><br>[mugs2_bananas2_ketchup_rubiks3_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/mugs2_bananas2_ketchup_rubiks3_bin.png)<br>object count: 10 | WhiteMugsInBinTask<br>Clean up the white mugs<br>subtask count: 2 |
|  | [mugs2_bananas2_ketchup_rubiks3_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/mugs2_bananas2_ketchup_rubiks3_bin.png) | DishesInBinTask<br>Put the dishware in the grey bin<br>subtask count: 3 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/tools_picking.png" alt="tools_picking.png" width="210" /><br>[tools_picking.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/tools_picking.png)<br>object count: 11 | ToolsPickingDrillTask<br>Select the cordless drill and put it on the table<br>subtask count: 1 |
|  | [tools_picking.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/tools_picking.png) | ToolsPickingHammerTask<br>Select the blue hammer and put it on the table<br>subtask count: 1 |
|  | [tools_picking.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/tools_picking.png) | ToolsPickingAllHammersTask<br>Take out all the hammers and put them on the table<br>subtask count: 4 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/toys_cleanup.png" alt="toys_cleanup.png" width="210" /><br>[toys_cleanup.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/toys_cleanup.png)<br>object count: 11 | AnimalsInBinTask<br>Put the lizards in the bin<br>subtask count: 2 |
|  | [toys_cleanup.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/toys_cleanup.png) | StackYellowOnRedTask<br>Stack the yellow block on the red block<br>subtask count: 2 |
|  | [toys_cleanup.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/toys_cleanup.png) | RubiksCubesInBinTask<br>Sort all rubiks cubes into the bin<br>subtask count: 3 |
|  | [toys_cleanup.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/toys_cleanup.png) | BlocksInBinTask<br>Sort all colored blocks into the bin<br>subtask count: 4 |
|  | [toys_cleanup.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/toys_cleanup.png) | CubesAndBlocksInBinTask<br>Put all the cubes and blocks in the bin<br>subtask count: 7 |
|  | [toys_cleanup.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/toys_cleanup.png) | CleanUpToysTask<br>Clean up all the smaller toys and leave the birdhouse on the table<br>subtask count: 9 |
| [canned_food_in_bin.yaml](tasks/canned_food_in_bin.yaml)<br>scene: [bin_condiments.yaml](scenes/bin_condiments.yaml) | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/bin_condiments.png" alt="bin_condiments.png" width="210" /><br>[bin_condiments.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bin_condiments.png)<br>object count: 12 | CannedFoodInBinTask<br>Put the canned food in the grey bin<br>subtask count: 1 |
| [coffee_pot_in_bin.yaml](tasks/coffee_pot_in_bin.yaml)<br>scene: [bin_condiments.yaml](scenes/bin_condiments.yaml)<br>prompt: Using maple table background: droid place the coffee pot into the grey bin on the table. Other objects on the table as distractors: mug, mustard, bowl, ranch dressing, two bbq sauce bottles, oatmeal raisin cookies, canned tuna, soft scrub, wood block | [bin_condiments.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bin_condiments.png) | CoffeePotInBinTask<br>Put the coffee pot in the grey bin<br>subtask count: 1 |
| [bbq_sauce_in_bin.yaml](tasks/bbq_sauce_in_bin.yaml)<br>scene: [bin_condiments.yaml](scenes/bin_condiments.yaml) | [bin_condiments.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bin_condiments.png) | BBQSauceInBinTask<br>Put the red BBQ sauce bottles in the grey bin<br>subtask count: 2 |
| [condiments_in_bin.yaml](tasks/condiments_in_bin.yaml)<br>scene: [bin_condiments.yaml](scenes/bin_condiments.yaml) | [bin_condiments.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/bin_condiments.png) | CondimentsInBinTask<br>Sort the sauce condiments into the grey bin<br>subtask count: 4 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/ladle_pot.png" alt="ladle_pot.png" width="210" /><br>[ladle_pot.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/ladle_pot.png)<br>object count: 13 | PinkSpoonInPotTask<br>Put the pink spaghetti spoon in the pot<br>subtask count: 1 |
|  | [ladle_pot.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/ladle_pot.png) | GreenSpoonsInPotTask<br>Put the green spoons in the pot<br>subtask count: 3 |
|  | [ladle_pot.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/ladle_pot.png) | SpoonsInPotTask<br>Put all of the serving spoons with no holes in the pot<br>subtask count: 3 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/workdesk_bin.png" alt="workdesk_bin.png" width="210" /><br>[workdesk_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/workdesk_bin.png)<br>object count: 13 | KeyboardOutOfBinTask<br>Take the keyboard out of the bin and put it on the table<br>subtask count: 1 |
|  | [workdesk_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/workdesk_bin.png) | PhoneOrRemoteInBinTask<br>Put the phone or the remote in the grey bin<br>subtask count: 1 |
| [smartphone_in_bin.yaml](tasks/smartphone_in_bin.yaml)<br>scene: [workdesk_bin.yaml](scenes/workdesk_bin.yaml) | [workdesk_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/workdesk_bin.png) | SmartphoneInBinTask<br>Put the smartphone in the grey bin<br>subtask count: 1 |
|  | [workdesk_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/workdesk_bin.png) | SpoonInMugTask<br>Put the metal spoon that's in the wooden bowl in the mug<br>subtask count: 1 |
| [toy_in_bin.yaml](tasks/toy_in_bin.yaml)<br>scene: [workdesk_bin.yaml](scenes/workdesk_bin.yaml)<br>prompt: Using maple table background. Droid place the lizard figurine into the grey bin on the table. Other objects on the table as distractors: ceramic mug, glasses, marker, remote control, smartphone, wooden bowl, spoon big, computer mouse, yogurt cup and granola bar. | [workdesk_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/workdesk_bin.png) | ToyInBinTask<br>Put the lizard away in the bin<br>subtask count: 1 |
| [electronics_in_bin.yaml](tasks/electronics_in_bin.yaml)<br>scene: [workdesk_bin.yaml](scenes/workdesk_bin.yaml) | [workdesk_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/workdesk_bin.png) | ElectronicsInBinTask<br>Put the electronic devices in the grey bin<br>subtask count: 4 |
| [black_items_in_bin.yaml](tasks/black_items_in_bin.yaml)<br>scene: [workdesk_bin.yaml](scenes/workdesk_bin.yaml) | [workdesk_bin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/workdesk_bin.png) | BlackItemsInBinTask<br>Put the black items in the grey bin<br>subtask count: 5 |
| [throw_away_apple.yaml](tasks/throw_away_apple.yaml)<br>scene: [workdesk_snacks.yaml](scenes/workdesk_snacks.yaml)<br>prompt: Using maple table background. droid place the apple into the plasticpail on the table. Other objects on the table as distractors: ceramic mug, glasses, keyboard, marker, remote control, smartphone, wooden bowl, spoon big, computer mouse, yogurt cup and pitcher | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/workdesk_snacks.png" alt="workdesk_snacks.png" width="210" /><br>[workdesk_snacks.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/workdesk_snacks.png)<br>object count: 13 | ThrowAwayAppleTask<br>Throw away the apple<br>subtask count: 1 |
| [apple_and_yogurt_in_bowl.yaml](tasks/apple_and_yogurt_in_bowl.yaml)<br>scene: [workdesk_snacks.yaml](scenes/workdesk_snacks.yaml) | [workdesk_snacks.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/workdesk_snacks.png) | AppleAndYogurtInBowlTask<br>Put the apple and yogurt in the bowl<br>subtask count: 2 |
| [throw_away_snacks.yaml](tasks/throw_away_snacks.yaml)<br>scene: [workdesk_snacks.yaml](scenes/workdesk_snacks.yaml) | [workdesk_snacks.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/workdesk_snacks.png) | ThrowAwaySnacksTask<br>Put away the snacks in the bin<br>subtask count: 2 |
| [marker_in_mug.yaml](tasks/marker_in_mug.yaml)<br>scene: [workdesk.yaml](scenes/workdesk.yaml) | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/workdesk.png" alt="workdesk.png" width="210" /><br>[workdesk.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/workdesk.png)<br>object count: 14 | MarkerInMugTask<br>Put the whiteboard marker in the mug<br>subtask count: 1 |
| [mouse_on_keyboard.yaml](tasks/mouse_on_keyboard.yaml)<br>scene: [workdesk.yaml](scenes/workdesk.yaml)<br>prompt: Using maple table background. Droid place the computer mouse into the keyboard on the table. Other objects on the table as distractors: ceramic mug, glasses, lizard figurine, marker, remote control, rubiks cube, smartphone, wooden bowl, big spoon, yogurt cup, oatmeal raisin cookies and granola bar | [workdesk.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/workdesk.png) | MouseOnKeyboardTask<br>Put the computer mouse on the keyboard<br>subtask count: 1 |
|  | [workdesk.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/workdesk.png) | PickGlassesTask<br>Pick up the eye glasses<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/cooking_table.png" alt="cooking_table.png" width="210" /><br>[cooking_table.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/cooking_table.png)<br>object count: 15 | CookingPickPastaToolTask<br>Move the pink tool from this utensil container to the other utensil holder<br>subtask count: 1 |
|  | [cooking_table.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/cooking_table.png) | CookingClearPlateTask<br>Put the two measuring cups outside of the plate<br>subtask count: 2 |
|  | [cooking_table.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/cooking_table.png) | PickOrangeObjectTask<br>Pick up the orange measuring cup<br>subtask count: 2 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/fruits_out_of_basket.png" alt="fruits_out_of_basket.png" width="210" /><br>[fruits_out_of_basket.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/fruits_out_of_basket.png)<br>object count: 15 | FruitsGreenLimesOnPlateTask<br>Put all the green fruit on the plate<br>subtask count: 2 |
|  | [fruits_out_of_basket.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/fruits_out_of_basket.png) | FruitsOrangesOnPlateTask<br>Put all the oranges on the plate<br>subtask count: 2 |
|  | [fruits_out_of_basket.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/fruits_out_of_basket.png) | FruitsOnPlate3Task<br>Put three (3) fruits on the plate<br>subtask count: 3 |
|  | [fruits_out_of_basket.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/fruits_out_of_basket.png) | FruitsOnPlateTask<br>Put all the fruits on the plate<br>subtask count: 7 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/fruits_in_basket.png" alt="fruits_in_basket.png" width="210" /><br>[fruits_in_basket.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/fruits_in_basket.png)<br>object count: 16 | FruitsMovingOrangeOrLimeTask<br>Move an orange or a lime to the wood bowl<br>subtask count: 1 |
|  | [fruits_in_basket.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/fruits_in_basket.png) | FruitsMovingTask<br>Move an orange to the white bowl<br>subtask count: 1 |
|  | [fruits_in_basket.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/fruits_in_basket.png) | FruitsOnionTask<br>Put the onion in the wood bowl<br>subtask count: 1 |
|  | [fruits_in_basket.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/fruits_in_basket.png) | FruitsOnionToPlateTask<br>Put the onion on the plate<br>subtask count: 1 |
|  | [fruits_in_basket.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/fruits_in_basket.png) | WoodSpatulaToBowlTask<br>Put the wooden spatula in the bowl<br>subtask count: 1 |
| [big_pumpkin_in_bin.yaml](tasks/big_pumpkin_in_bin.yaml)<br>scene: [clutter_fruit_bottle_bluebin.yaml](scenes/clutter_fruit_bottle_bluebin.yaml)<br>prompt: Using a maple table background. There are two pumpkins on the table, a larger one and a smaller one. Droid picks and places the pumpkin large into the blue bin on the table. Other objects on the table as distractors: two lemons, two limes, two oranges, a pomegranate, white packer bottle, avocado, crabbypenholder, serving\_bowl, utilityjug and red\_onion | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/clutter_fruit_bottle_bluebin.png" alt="clutter_fruit_bottle_bluebin.png" width="210" /><br>[clutter_fruit_bottle_bluebin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/clutter_fruit_bottle_bluebin.png)<br>object count: 17 | BigPumpkinInBinTask<br>Put the bigger pumpkin in the bin<br>subtask count: 1 |
| [small_pumpkin_in_bin.yaml](tasks/small_pumpkin_in_bin.yaml)<br>scene: [clutter_fruit_bottle_bluebin.yaml](scenes/clutter_fruit_bottle_bluebin.yaml) | [clutter_fruit_bottle_bluebin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/clutter_fruit_bottle_bluebin.png) | SmallPumpkinInBinTask<br>Put the small pumpkin in the bin<br>subtask count: 1 |
| [clutter_pumpkin.yaml](tasks/clutter_pumpkin.yaml)<br>scene: [clutter_fruit_bottle_bluebin.yaml](scenes/clutter_fruit_bottle_bluebin.yaml) | [clutter_fruit_bottle_bluebin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/clutter_fruit_bottle_bluebin.png) | ClutterPumpkinTask<br>Put all the pumpkins away in the bin<br>subtask count: 2 |
| [clutter_plastic.yaml](tasks/clutter_plastic.yaml)<br>scene: [clutter_fruit_bottle_bluebin.yaml](scenes/clutter_fruit_bottle_bluebin.yaml) | [clutter_fruit_bottle_bluebin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/clutter_fruit_bottle_bluebin.png) | ClutterPlasticTask<br>Put all plastic bottles away in the bin<br>subtask count: 3 |
| [clear_organic_objects.yaml](tasks/clear_organic_objects.yaml)<br>scene: [clutter_fruit_bottle_bluebin.yaml](scenes/clutter_fruit_bottle_bluebin.yaml) | [clutter_fruit_bottle_bluebin.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/clutter_fruit_bottle_bluebin.png) | ClearOrganicObjectsTask<br>Clear away the organic objects<br>subtask count: 11 |
|  | <img src="https://media.githubusercontent.com/media/NVlabs/RoboLab/main/assets/scenes/_images/breakfast_table.png" alt="breakfast_table.png" width="210" /><br>[breakfast_table.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/breakfast_table.png)<br>object count: 19 | GrabABagelTask<br>Grab a bagel<br>subtask count: 1 |
|  | [breakfast_table.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/breakfast_table.png) | GrabAFruitTask<br>Pick up a fruit<br>subtask count: 1 |
|  | [breakfast_table.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/breakfast_table.png) | YogurtInBowlTask<br>Put the small red yogurt in the red bowl<br>subtask count: 1 |
|  | [breakfast_table.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/breakfast_table.png) | MoveBananaToBagelPlateTask<br>Move the bananas to the bagel plate<br>subtask count: 2 |
|  | [breakfast_table.png](https://github.com/NVlabs/RoboLab/blob/main/assets/scenes/_images/breakfast_table.png) | UtensilsInMugTask<br>Put the fork and spoon in the ceramicmug<br>subtask count: 2 |
==================================================================
FILE: pyproject.toml (first 120 lines)
[build-system]
# >=66.1 for Python 3.12 compatibility, >=62.3 for the recursive `**` globs in
# [tool.setuptools.package-data].
requires = ["setuptools>=66.1"]
build-backend = "setuptools.build_meta"

[project]
name = "isaaclab_arena"
version = "0.3.0"
description = "Isaac Lab - Arena. An Isaac Lab extension for robotic policy evaluation."
readme = "README.md"
requires-python = ">=3.12,<3.13"
license = { text = "Apache-2.0" }
dependencies = [
    "typing_extensions",
    "onnxruntime",
    "vuer",
    # Arena imports isaacteleop directly; pin the validated prerelease so the
    # Docker and native uv environments do not float independently.
    "isaacteleop[retargeters,ui,cloudxr]==1.4.126rc1",
    "websockets==16.1.1",
    "lightwheel-sdk",
    "pytest",
    "pydantic>=2.0",
    "openai>=2.0",
    # Sensitivity analysis (isaaclab_arena.analysis.sensitivity), imported at module level.
    "sbi",
    "scipy",
    "matplotlib",
    "plotly",
    # MoviePy 1.x relies on decorator 4.x call semantics to propagate clip FPS.
    "moviepy>=1.0.3,<2.0.0.dev0",
    "decorator>=4.0.2,<5",
    # HDF5 -> LeRobot video conversion uses imageio with its FFmpeg backend.
    "imageio",
    "imageio-ffmpeg",
    # HDF5 -> LeRobot conversion (isaaclab_arena_gr00t.lerobot.convert_hdf5_to_lerobot), imported at module level.
    # Pinned to 2.2.3 to match the version used in GR00T.
    "pandas==2.2.3",
]

[project.optional-dependencies]
dev = [
    "jupyter",
    "debugpy",
    "tenacity",
    "streamlit>=1.56",
    "streamlit-ace>=0.1.1",
    # Asset search for agentic environment generation. Kept here rather than behind an extra of
    # its own: it adds one wheel, since Isaac Sim already brings everything it depends on, and an
    # extra only bought a way to install the review GUI with its asset search missing.
    "simready-search>=2026.4.2",
]

# PEP 735 dependency groups for the native uv install. pip (used by the Docker
# build) ignores these groups, so Docker continues to get Isaac Lab from its
# copied submodule and Isaac Sim from its base image.
[dependency-groups]
# Isaac Lab's root isaaclab-dev project is installed editable from the submodule
# checkout. Its extras provide Isaac Sim, OV backends, Mimic, Teleop, RSL-RL,
# and the Rerun visualizer. This group is selected by a bare `uv sync` through
# default-groups below.
isaaclab-from-source = [
    "isaaclab-dev[isaacsim,ov,mimic,teleop,rsl-rl,rerun]",
    # Keep the workspace members explicit as well. uv requires a package to be
    # named directly in this group before a group-gated path source can satisfy
    # the dependency declared by isaaclab-dev.
    "isaaclab",
    "isaaclab-assets",
    "isaaclab-contrib",
    "isaaclab-experimental",
    "isaaclab-mimic",
    "isaaclab-newton",
    "isaaclab-ov",
    "isaaclab-physx",
    "isaaclab-ppisp",
    "isaaclab-rl",
    "isaaclab-tasks",
    "isaaclab-tasks-experimental",
    "isaaclab-teleop",
    "isaaclab-visualizers",
    # Direct torch deps so [tool.uv.sources] routes them to the cu128 index.
    # These versions match the Isaac Lab source checkout.
    "torch==2.11.0",
    "torchvision==0.26.0",
    "torchaudio==2.11.0",
    # Keep an explicitly selected source group self-sufficient as well.
    { include-group = "openpi" },
]
openpi = [
    "openpi-client",
]
gr00t-client = [
    "gr00t==0.1.0",
]

[tool.uv]
# Arena supports Linux x86_64 only; resolve and lock for exactly that platform.
environments = ["sys_platform == 'linux' and platform_machine == 'x86_64'"]
# Install the source-based sim stack (Isaac Lab editable from the submodule)
# and the remote OpenPI client on a bare `uv sync`.
default-groups = ["isaaclab-from-source", "openpi"]
# Teleoperation requires a specific release candidate. Its exact requirement
# above opts that package into prerelease selection without allowing unrelated
# packages to float to prereleases.
prerelease = "if-necessary-or-explicit"
# Prefer the first index containing a compatible package. The explicit PyPI
# route below handles the one known NVIDIA/PyPI name collision without merging
# candidates from multiple indexes.
index-strategy = "first-index"
# Arena validates the pinned Isaac Lab source checkout against the newer public
# Isaac Sim release. Override Isaac Lab's exact 6.0 requirement without modifying
# the submodule so fresh checkouts resolve the same environment.
# Pin numpy to the exact version Isaac Sim requires: isaacsim-kernel needs
# ==2.3.1 and numba needs <2.5. An override (not a plain dep) is needed to also
# beat a transitive constraint that would otherwise pull numpy<2.
# Pin coverage and packaging to versions compatible with the Isaac Sim 6.1 wheel
# stack. These overrides resolve stricter transitive constraints that do not
# reflect the versions used successfully in the Docker runtime.
# Pin websockets to the Docker-validated 16.1.1. Isaac Sim 6.1's
==================================================================
FILE: CONTRIBUTORS.md
# Isaac Lab - Arena Developers and Contributors

This is the official list of Isaac Lab - Arena Project developers and contributors.

Guidelines for modifications:

* Please keep the **lists sorted alphabetically**.
* name <github_user and/or email> (optional institution)

## Core Team

* Alexander Millane <alexmillane, amillane@nvidia.com> (NVIDIA)
* Clemens Volk <cvolkcvolk, cvolk@nvidia.com> (NVIDIA)
* Peter Du <peter-NV, peterd@nvidia.com> (NVIDIA)
* Qian Lin <linqianqian-work, qianl@nvidia.com> (NVIDIA)
* Sangeeta Subramanian <sangeetas@nvidia.com> (NVIDIA)
* Vikram Ramasamy <viiik-inside, vramasamy@nvidia.com> (NVIDIA)
* Xinjie Yao <xyao-nv, xyao@nvidia.com> (NVIDIA)
* Zihao Xiao <zhx06, zihaox@nvidia.com> (NVIDIA)

## Robolab

* Fabio Ramos <ftozetoramos@nvidia.com> (NVIDIA)
* Xuning Yang <xuningy@nvidia.com> (NVIDIA)

## LightWheel AI

* Jay Yang <jay.yang@lightwheel.ai> (LightWheel)
* Ju Zheng <ju.zheng@lightwheel.ai> (LightWheel)
* Tianheng Wu <tianheng.wu@lightwheel.ai> (LightWheel)
* Xiaowei Song <xiaowei.song@lightwheel.ai> (LightWheel)

## Contributors

* Ashley Chow <ashchow@nvidia.com> (NVIDIA)
* Hui Kang <hkang@nvidia.com> (NVIDIA)
* Lance Li <Nyquist0, lancel@nvidia.com> (NVIDIA)
* Mikhail Yurasov <myurasov-nv, myurasov@nvidia.com> (NVIDIA)
* Rebecca Zhang <rebeccazhang0707, rebeccaz@nvidia.com> (NVIDIA)
* Shiwei Sheng <shiweis, shiweis@nvidia.com> (NVIDIA)
* Weihua Zhang <yami007007-weihuaz, weihuaz@nvidia.com> (NVIDIA)
