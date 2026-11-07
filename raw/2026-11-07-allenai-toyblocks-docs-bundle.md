# allenai/ToyBlocks — docs bundle

Captured 2026-11-07 at main head 931fd7a (2026-11-07). Apache-2.0, 36 stars, created 2026-11-04. Submodules: curobo (NVlabs, v2), maniflow-tb, molmo2, agentic_robotics. Pins: isaaclab[isaacsim,all]==2.3.2.post1 (Isaac Sim 5.1), lerobot==0.4.3, torch>=2.7 cu128. vecgen skills/flip.py and rotate.py module docstrings (scripted, ported from the TAMP executor) appended at the end.

---- FILE: CLAUDE.md ----

# CLAUDE Instructions for ToyBlocks

## Critical Rules for AI Code Changes

1. **Minimize file modifications.** Touch only the files strictly necessary to implement the requested change. Do not refactor, reorganize, or "improve" unrelated code. If a change can be accomplished by editing one file, do not edit two.
2. **Summarize every file change.** After making changes, provide a detailed summary listing each modified file with:
   - The file path
   - What was changed and why
   - Any side effects or dependencies introduced
3. **No speculative edits.** Do not modify files "just in case" or to preemptively fix issues that were not requested. Each file touched must be directly justified by the task.
4. **Preserve existing patterns.** When editing a file, match the surrounding code style, import conventions, and structure already present in that file. Do not introduce new patterns unless explicitly asked.
5. **Scope awareness.** Before editing, consider whether the change belongs in the file you're about to touch or whether it should go in a more appropriate location. Prefer surgical edits over sweeping refactors.
6. **No TAMP.** The TAMP submodule (`tmp3`) is gone: do not import `tmp3` / `evals` / `test_domains` (`tests/tamp/test_no_tamp_submodule.py` enforces it).
7. For all newley generated code, make sure the objects are properly typed.
---

## Running Commands

**Always run long-running commands inside a detached `tmux` session.** Never launch
them as a plain background shell job. A background job is a child of the calling
agent process, so it dies when that session disconnects or is torn down; a tmux
session reparents to pid 1 and survives independently.

```bash
LOG=/path/to/job.log
tmux new-session -d -s <session-name> "<command> > $LOG 2>&1; echo EXIT=\$? >> $LOG; sleep infinity"

# Then poll:
tail -f $LOG
tmux ls
```

- Keep `sleep infinity` at the end so the session stays alive after the command
  exits and the exit code remains readable.
- Verify detachment: the parent chain of the process should end at `tmux: server`,
  not at the agent process (`ps -o pid=,ppid=,comm= -p <pid>`).
- This applies to dataset merges, renders, large scans over shared storage, training runs —
  anything expected to outlive a few minutes.

---

## Project Overview
- **ToyBlocks** is a research codebase for robotic manipulation task generation, data collection, policy training, and evaluation. It integrates Isaac Lab simulation, symbolic task planning (FF) with CuRobo motion planning (the vecgen datagen engine), and policy serving infrastructure.
- The architecture is modular: simulation environments, datagen (vecgen), policy serving, and evaluation are separated into distinct packages.
- Key directories:
  - `src/toyblocks/`: Core Python package — tasks, blocks domain, datagen (vecgen), serving, evaluation, utilities.
  - `src/toyblocks/tamp/blocks/`: Blocks domain — PDDL domain + problems, action config, goal checks, env-package templates.
  - `src/toyblocks/vecgen/`: Datagen engine — FF planning, batched skills, cuRobo v2 planner pool, recording.
  - `src/toyblocks/tasks/`: Isaac Lab gymnasium environments (lift, flip, rotate, push, pile, etc.).
  - `src/toyblocks/serving/`: Policy server/client infrastructure (WebSocket + msgpack).
  - `src/toyblocks/eval/`: Evaluation utilities (replay, metrics, resets).
  - `scripts/`: Entry points for datagen, evaluation, task generation, and policy serving.
  - `curobo/`: NVIDIA CuRobo motion planning (editable dependency).
  - `maniflow-tb/`: ManiFlow low-level policy (installs as the `hvla` package; submodule of allenai/maniflow-tb).
  - `molmo2/`: Molmo2 high-level policy model (installs as `ai2-molmo2`, package `olmo`; submodule of allenai/molmo2).
  - `agentic_robotics/`: LLM agents driving the robot through MCP skill tools (installs as `agentic-robotics`, `agentic-robotics` CLI; submodule of allenai/agentic_robotics). Its scripted skills run vecgen's skills via `toyblocks.eval.ll_oracle`'s engine wiring, so changes there can affect it.
  - `data/`: Default pipeline output root (`--output-root`): `data/datasets/<folder>/<exp>`, merged sets under `data/datasets/merged/train/<exp>`.

## Critical Files & Data Flow

### Datagen Pipeline (vecgen)
Orchestrated by `scripts/datagen/run_datagen_pipeline.py` locally (one problem per GPU slot: `--local-gpus` x `--local-gpu-workers`; output under `--output-root`, default `data`; `--resume` skips stages marked done in `<base>/.pipeline_state/`):
1. **Task Generation** (`scripts/task_gen/*.py`): PDDL problems.
2. **Env** (`scripts/generate_task_from_pddl.py`): PDDL problem → autogen Isaac Lab env package + sampled reset states (`--randomize_robot_init`: collision-free cuRobo IK starts). With `--vecgen-problems-per-env G > 1` the vecgen jobs build multi-problem packages instead (`scripts/vecgen/make_superset_env.py`).
3. **Execution** (`scripts/vecgen/run.py`, `src/toyblocks/vecgen/`): FF plans per env (`symbolic/`), batched skills on a cuRobo v2 planner pool (`skills/`, `planner/`), verified effects and goals (`symbolic/predicates.py`), LeRobot recording → `execution/<slug>/`.
4. **Merge / annotate / plot** (`scripts/datagen/merge_datasets.py`, `src/toyblocks/data_annotation/annotate_target_xy.py`, `scripts/datagen/plot_episode.py`).

Play data and TAMPER (`scripts/datagen/run_tamper_pipeline.py`, `docs/tamper.md`) run on vecgen too. Rendering (`scripts/render/`) runs on `toyblocks.domain_randomization.render_sim.RenderSim`. It runs inside the datagen and play pipelines via `--render-pass FLAGS.yaml[:N]`, the only flag that turns the stage on (repeatable, one pass per look, no default YAML); datagen's `--render-schedule` picks whether each render is its own job or rides the execution job. HDRI backdrops: polyhaven comes with `asset_manifest.json`, the Laval indoor-2018 pool is installed separately; see `docs/source/user_guide/workflows/datagen/render.md`.

### Evaluation
- `scripts/evaluate.py`: Eval worker: remote policy server, LL oracle, dataset replay, or random actions.
- `src/toyblocks/serving/serve_maniflow_policy.py`: ManiFlow LL policy server (`--hl oracle`), or Molmo2 HL + ManiFlow LL (`--hl model`).
- `scripts/launch_eval.py`: Queue-driven eval launcher: policy server, episode queue and eval workers, all local.

### TAMP Domain (Blocks)
- `src/toyblocks/tamp/blocks/domain.pddl`: Symbolic domain definition.
- `src/toyblocks/tamp/blocks/action_config.yaml`: Per-action argument layouts (`HL_ARGS`).
- `src/toyblocks/tamp/blocks/pddl_goal_tensor_conversions.py`: Batched goal-predicate checks on the live sim (eval success gate, oracle step checks).
- `src/toyblocks/tamp/blocks/template/`: Codegen for autogen env packages from PDDL.
- `src/toyblocks/tamp/blocks/problems/`: Checked-in PDDL problem files.

### Serving
- `src/toyblocks/serving/base_policy.py`: `BasePolicy` interface all policy servers must implement.
- `src/toyblocks/serving/policy_server.py`: WebSocket+msgpack server.
- `src/toyblocks/serving/policy_client.py`: Client used by `evaluate.py`.
- `src/toyblocks/serving/obs_transforms/`: Observation transforms (maniflow, maniflow_blocks_table).

## Developer Workflows

### Environment & Install
- **Package manager**: `uv` (see `pyproject.toml`).
- **Python**: Requires >= 3.11.
- **Setup**: `uv venv --python 3.11` and `git submodule update --init --recursive`; install with `uv pip install -e .[...]`, not `uv sync` (see README).
- **Install with Isaac Lab**: `uv pip install -e .[dev,isaac,torch-cu128]`
- **Install for datagen (vecgen, builds cuRobo v2 from `./curobo`, no CUDA toolkit needed)**: `uv pip install -e .[dev,isaac,torch-cu128,vecgen]`
- **Install with ManiFlow**: `uv pip install -e .[dev,isaac,torch-cu128,maniflow]` (extras combine in one command)
- **Install agentic robotics**: `uv pip install -e .[dev,isaac,torch-cu128,vecgen,agentic]` (needs the `agentic_robotics` submodule and the user's own OpenRouter key; see `docs/source/user_guide/workflows/agentic_robotics.md`)
- **Linting**: `ruff check` / `ruff format` (config in `pyproject.toml`).

### Running the Datagen Pipeline Locally

```bash
# End to end (task gen -> env -> vecgen -> merge -> annotate), one problem per GPU
python scripts/datagen/run_datagen_pipeline.py --experiment-id oct31_stack3 \
    --output-root data --task-gen-script scripts/task_gen/stack_three.py --task-gen-count 2 \
    --env-per-problem 16 --num-envs 16 --exec-num-envs 16

# Or stage by stage for one problem
problem=src/toyblocks/tamp/blocks/problems/flip.pddl
task=$(basename "${problem}" .pddl | tr '-' '_')
python scripts/generate_task_from_pddl.py --domain_path src/toyblocks/tamp/blocks \
    --pddl ${problem} --num_reset_states 32 --num_envs 16 --seed 0 --output_dir outputs --headless
python scripts/vecgen/run.py --env-path outputs/${task} --pddl ${problem} \
    --domain src/toyblocks/tamp/blocks/domain.pddl --num-envs 16 --episodes 32 \
    --record datasets/flip/${task} --mark-complete --headless
```

### Evaluation (Molmo2 HL + ManiFlow LL)

```bash
# Starts the policy server, episode queue and eval worker locally
uv run python scripts/launch_eval.py --num-eval-gpus 1 \
    --dataset-path <merged LeRobot val set> --episode-indices 0-3 --queue-limit 4 \
    --model-path <run>/checkpoints/steps_N_model.safetensors --hl-model-path <molmo2 step dir> \
    --no-hl-prev-action
```

Add `--ll-oracle` (Molmo2 HL + oracle LL), `--policy maniflow` (oracle HL + ManiFlow LL), `--replay`
(recorded actions) or `--oracle-comparison --save-hl-overlay-video`. For pdb debugging, run
`scripts/eval/serve_local_server.sh` and `scripts/eval/serve_local_client.sh` in two terminals.

### PDDL Task Generation

```bash
# Atomic skills on block_r (with distractors): one flip, one rotate, one pick-and-place
python scripts/task_gen/flip.py --count 50 --out-dir outputs/flip/tasks --seed 42
python scripts/task_gen/rotate.py --count 50 --out-dir outputs/rotate/tasks --seed 42
python scripts/task_gen/pnp.py --count 50 --out-dir outputs/pnp/tasks --seed 42

# 3-block stacking in letter + digit + color scenes (--train / --val glyph splits)
python scripts/task_gen/stack_three.py --train --count 50 --out-dir outputs/stack3/tasks --seed 42

# Play-data scenes (used by scripts/datagen/run_playdata_pipeline.py)
python scripts/task_gen/play_scene.py --count 50 --out-dir outputs/play/tasks --seed 42
# ...and the search scenes the DFA goal policies run on (src/toyblocks/playdata/dfa/AUTHORING.md)
python scripts/task_gen/find_as.py --count 5 --out-dir outputs/find_as/tasks --seed 42
python scripts/task_gen/search.py --count 5 --out-dir outputs/search/tasks --seed 42
```

## Project-Specific Conventions
- **Isaac App Launch**: Always call `launch_app()` from `toyblocks.cli.isaac_app` before importing any Isaac Lab modules. This is a hard requirement.
- **Autogen Tasks**: Generated env packages go under `src/toyblocks/tasks/autogen/*/` (gitignored). They register as `<slug>-v0` gymnasium environments.
- **PDDL Naming**: PDDL problem basenames become task slugs via `task_slug_from_pddl_path` (hyphens → underscores).
- **Predicates / skills**: vecgen checks PDDL facts on the sim in `vecgen/symbolic/predicates.py` and executes each domain action with a batched skill in `vecgen/skills/`.
- **LeRobot Format**: All dataset recording (datagen and eval) uses the one `IsaacDataRecorderLeRobot` in `toyblocks.vecgen.recording` (LeRobot v3, parallel writers stitched at finalize); see `docs/lerobot_recording.md`.
- **Observation Transforms**: Policy servers and `evaluate.py` use pluggable obs transforms registered in `src/toyblocks/serving/obs_transforms/`.
- **`tyro`**: Most CLI scripts use `tyro` for argument parsing (dataclass-based configs).
- **`uv`**: Use `uv run` to execute scripts within the managed virtualenv.

## Integration Points
- **Isaac Lab**: All simulation via Isaac Lab's Python API (requires `--extra isaac`).
- **FF**: Symbolic planner, vendored (with its binary) in `src/toyblocks/vecgen/symbolic/ff_planner/`.
- **CuRobo**: Motion planning in `./curobo/` (editable install as `nvidia-curobo`).
- **ManiFlow**: Molmo2 HL in `./molmo2/`, ManiFlow LL in `./maniflow-tb/` (`hvla` package).
- **Agentic robotics**: `./agentic_robotics/` (`agentic-robotics` package): episodes, web UI (`agentic-robotics menu` / `portal`), task packages in `agentic_robotics/data/tasks/`.

## Key Entry Points

| Script | Purpose |
|--------|---------|
| `scripts/generate_task_from_pddl.py` | PDDL → autogen env package + reset states |
| `scripts/vecgen/run.py` | Datagen execution: FF + batched skills → LeRobot dataset |
| `scripts/evaluate.py` | Eval worker (policy server, LL oracle, replay, random) |
| `src/toyblocks/serving/serve_maniflow_policy.py` | ManiFlow / Molmo2 WebSocket policy server |
| `scripts/launch_eval.py` | Queue-driven eval launcher (local, single or multi GPU) |
| `scripts/task_gen/*.py` | PDDL problem generators (flip, rotate, push, etc.) |
| `scripts/datagen/run_datagen_pipeline.py` | End-to-end pipeline orchestrator |

---

For more details, see docstrings in the scripts and the documentation in `docs/`.

---- FILE: dev.md ----

# Development Setup (wip)


Isaac Lab isn't automatically discovered by Python language servers, so add this to .vscode/settings.json

```
{
    "cursorpyright.analysis.extraPaths": [
        "IsaacLab/source/isaaclab"
    ],
    "python.autoComplete.extraPaths": [
        "IsaacLab/source/isaaclab"
    ]
}
```


## Notes

`src/toyblocks/cli/base_args.py` contains a base arguments dataclass for use with tyro to replace any instance of argparse usage in Isaac. This means we have nicer and typed CLIs. See `scripts/random_actions.py` for example usage of tyro and typed CLI args.

---- FILE: docs_hvla_tamp_eval_tasks.md ----

# Evaluating the Hierarchical VLA on TAMP-Like Problems

This document proposes the task suite for training and evaluating our hierarchical VLA —
**Molmo2 finetuned on our data as the high-level (HL) planner** and **ManiFlow trained on our
data as the low-level (LL) policy** — on problems where success requires symbolic reasoning,
multi-step lookahead, and correct sequencing, not just reactive manipulation.

The central question: **can a hierarchical VLA solve problems that classically require a TAMP
planner?** Every task below is expressible in our existing blocks TAMP domain
(`pnp_table_table`, `pnp_table_block`, `pnp_block_block`, `pnp_block_table`, `push_to_right`,
`push_next_to`, `rotate`, `reorient`, `isolate`), so we can generate ground-truth demonstrations
and compute predicate-level success automatically.

Every task table carries a **Why it suits HL + LL** column. The neighbouring *Reasoning required*
column says what the task demands in the abstract; this one says why the task earns a slot in *this*
evaluation — which half of the hierarchy it loads, and what a failure on it would tell us. Tasks
that load only one half are as valuable as the hard ones: they are the controls that make failures
on the hard tasks attributable to the HL planner or the LL policy rather than to their combination.

---

## Scene Complexity Axis (applies to every task)

Every task family is evaluated in three scene settings:

| Setting | Description | What it tests |
|---|---|---|
| **Clean** | Only the blocks required by the goal are present | Pure planning + manipulation competence |
| **Few distractors** | 1–3 irrelevant blocks | Goal-relevant grounding; HL must identify which blocks matter |
| **Many distractors** | 6–12+ irrelevant blocks, cluttered workspace | Robust grounding, collision-aware placement, distractor blocks may occlude or physically obstruct the goal blocks |

In the *many distractors* setting, include variants where distractors **physically interfere**
(e.g., a distractor sits where the line must be built, or on top of a required block), so the
HL planner must emit clearing actions that are not part of the literal instruction. This is the
strongest test of lookahead — the required action sequence is longer than the instruction implies.

---

## TAMP Datagen Coverage

Every task below is marked with how far the datagen pipeline can take it. The distinction that
matters is **can the goal be written down at all** versus **can we build the starting scene** —
these are very different amounts of work, and the original version of this document conflated them.

| Mark | Meaning | Work needed |
|---|---|---|
| 🟢 | **Generable today.** A generator exists in `scripts/task_gen/`; most have produced data in `jul26_hvla`. | None |
| 🟡 | **Expressible, no generator yet.** The goal fits the supported predicates and the reset sampler can produce the initial state. | One new `task_gen` script |
| 🔵 | **Goal fine, initial state missing.** The goal is an ordinary predicate conjunction; the blocker is that the scene must *start* pre-arranged. | New reset-state sampler |
| ⛔ | **Not specifiable in the current system.** No way to write the goal, tagged with a blocker code below. | New predicate + vectorized checker, or a different supervision signal |

### What a goal can say

This is the hard constraint everything else follows from. A goal is a conjunction of literals
drawn from `SUPPORTED_GOAL_PREDICATES` in `src/toyblocks/tamp/blocks/pddl_goal_tensor_conversions.py`,
because `generate_task_from_pddl.py` needs a vectorized checker for every literal:

```
on   on_table   on_left   on_right   on_front   on_back   next_to   ori_of   clear   pick_obstructs
```

Every one of these is either **pairwise between two named blocks** or a property of a single named
block. There is no absolute position, no table region, no cardinality, and no size. `on_table_side`
is declared in `domain.pddl` but has no checker, so it cannot appear in a goal.

### Blocker codes for ⛔

- **G1 — no predicate for it.** The goal needs a spatial or quantitative relation outside the list
  above: table regions ("the left side", "the center"), 2D layouts and multi-block support
  (pyramid, square, grid), or comparisons over object properties. Needs a new predicate *and* a
  matching vectorized checker.
- **G2 — the goal is not a world state.** It counts actions ("flip it 3 times") or describes a
  process ("put everything back"). TAMP plans to a final state and will legitimately satisfy such
  a goal with fewer actions, or find it already satisfied.
- **G3 — the goal is open or disjunctive.** Goals of the form "any two red cubes" need `exists` or
  `or`. `generate_task_from_pddl.py` rejects quantified goals outright, and `(or ...)` is silently
  flattened into a conjunction by the goal parser, which is worse than failing. Verified against
  `scripts/task_gen/stack_red_blocks_v2.py`, whose `exists` goals fail this check while the
  concrete-block v1 generator passes.
- **G4 — the goal depends on reset-time randomization.** A PDDL goal is fixed per problem, but
  block size, table height, and friction are sampled *per env* from ranges. Worse, `block_size_range`
  yields **one size per env applied to every block** (`flip_env.py::_setup_scene_objects`), so blocks
  of differing sizes never coexist in a scene. Any goal referencing relative size is unwriteable.

### Note on "derived" goals

An earlier version of this document treated goals that must be *inferred* (alphabetical order,
arithmetic, largest digit, "spell an animal") as non-generable. That was wrong. The **generator**
computes the answer and emits concrete predicates; the instruction string carries the semantic
framing separately. Deriving the goal is the model's job at eval time, not the pipeline's. This is
exactly how `color_zebra_stack` already works — it is marked 🟢 and the HL must still induce the
alternation rule. These tasks are therefore 🟡, not blocked.

The one real constraint: the instruction template must not leak the answer, and the *held-out* split
has to be defined over the derivation (unseen digit sets, unseen words) rather than over goal syntax.

---

## 1. Letter-Block Spelling (stacks and lines)

Uses the full **A–Z letter block set** with orientation constraints (`OriOf`), building on
`scripts/task_gen/spelling.py`. The 26-letter vocabulary means the word space is effectively
unbounded — train on one word distribution and hold out words, letters, and word lengths for eval.

| Task | Goal | Example | Reasoning required | Why it suits HL + LL |
|---|---|---|---|---|
| 🟢 Spell word as a **stack** | Word bottom-to-top, each letter face-up/readable | Scene: C, A, T scattered flat. Instruction: *"Stack the blocks to spell CAT, reading top to bottom."* Expected: reorient each letter upright, stack T, then A, then C on top | Ordering + orientation; must reorient letters before stacking | HL owns the letter order and the reorient-before-stack dependency; LL owns placement on a rising tower where one bump erases every earlier subgoal. Both halves are loaded and the failures look different |
| 🟢 Spell word as a **line** | Letters left-to-right in reading order (`push_next_to` / `NextTo`) | Scene: D, O, G scattered. Instruction: *"Arrange the blocks in a row to spell DOG."* Expected: D leftmost, O next to D, G next to O, all readable from the front camera | Spatial ordering, left-right convention | Symbolic ordering over an error-accumulating non-prehensile execution. The measured 36–59% rate means the LL ceiling is already known, so HL gains are readable against it |
| 🟢 **Held-out words** from trained letters | Words never seen in training, spelled with letters that were | Training covered CAT, DOG, SUN. Eval: *"Spell TAG"* — T, A, G all appeared in training words, but TAG never did | Compositional generalization of the HL planner | The LL skill set is identical either side of the split, so any drop is HL composition failure and nothing else |
| 🟢 **Held-out letters** | Words containing letters that never appeared in training goals (but were seen as distractors) | Letters J, Z never appeared in any training goal. Eval: *"Spell JAZZ"* | Letter grounding generalization | Separates the VLM's visual vocabulary from the planner's goal vocabulary: the letters were seen, just never as targets |
| 🔵 **Re-spell** (anagram) | Rearrange an existing word into a new one | Scene: stack reading TAC (T bottom, C top). Instruction: *"Make it spell CAT."* Expected: full unstack to table, restack in the order T, A, C bottom-to-top | Must *unstack* first — classic non-monotonic TAMP structure | Demands deliberately taking apart a satisfied arrangement, which a reactive policy has no reason to do. The teardown has to come from the HL |
| 🔵 **Fix the word** | Correct a mostly-right arrangement; the error is not pointed out | Scene: line reads C, A, T but the A is upside-down. Instruction: *"Spell CAT."* Expected: flip only the A, leave C and T untouched | HL must diagnose the delta between current and goal state | The HL has to compare observation against goal before acting, and the LL cost is a single reorient — close to a pure perception-into-planning probe |
| 🟡 **Alphabetical order** | Line up scene letters alphabetically | Scene: K, B, F scattered. Instruction: *"Line these up in alphabetical order."* Expected: B, F, K left to right — the order is never stated | Goal ordering must be *derived*, not stated | The goal is never stated, so it tests precisely what Molmo2 adds over the TAMP planner: prior symbol knowledge used to synthesize the target |
| 🟡 **Semantic word choice** | Spell a word satisfying a category constraint | Scene: {C, A, T, X, Q}. Instruction: *"Spell the name of an animal."* Expected: CAT; X and Q must be left alone | Open-ended goal synthesis by the HL — VLM knowledge beyond TAMP | TAMP can verify this goal but could never invent it; the strongest argument in the suite for a VLM head instead of a symbolic planner |
| 🟢 Letter **orientation only** | Make all letters readable without relocating them | Scene: E, M, R placed correctly but M is rotated 180° (reads as W) and E lies face-down. Instruction: *"Make all letters readable from the front."* Expected: two `reorient` actions, zero pick-and-place relocations | Perceptual grounding of orientation, `reorient` action selection | No relocation keeps LL variance low, so this reads out orientation grounding directly. At 82% it is also the calibration point for every reorient-plus-stack family |

## 1b. Digit-Block Tasks

Uses the **1–9 digit block set**. Digits add a symbolic-numeric dimension that letters don't:
the block's *label* can interact with counting, ordering, and arithmetic.

> **Asset limit: there is no `0` block.** The `train_blocks` library ships `1.usd`–`9.usd` only,
> so any number containing a zero (2026, 10, 40) cannot be built. `scripts/task_gen/make_number.py`
> rejects these up front rather than failing later in the pipeline.

| Task | Goal | Example | Reasoning required | Why it suits HL + LL |
|---|---|---|---|---|
| 🟡 **Ascending / descending line** | Order the digit blocks present by value | Scene: 7, 2, 5 scattered. Instruction: *"Line the digits up from smallest to largest."* Expected: 2, 5, 7 left to right | Numeric ordering derived from labels | The ordering comes from label semantics rather than the instruction, while the LL side is plain pushes, so failures land on the HL by construction |
| 🟢 **Make a number** | Compose a multi-digit number as a line/stack | Scene: 1, 3, 7 plus distractor digits. Instruction: *"Spell 137 in a row."* Repeated digits need a second copy (121 uses `block_1` and `block_1_2`) | Multi-digit sequencing (digit blocks reused only if duplicates exist) | The instruction states the answer outright, making this the control condition against which the derived-goal digit tasks are scored |
| 🟡 **Digit-count matching** | Convert a displayed symbol into a cardinality | Scene: digit block 4 and six plain red cubes. Instruction: *"Stack as many red cubes as the digit shows."* Expected: a stack of exactly 4, two cubes left over | Reading a symbol and converting it to a cardinality — symbol/quantity binding | Binds a read symbol to a count and then requires stopping at it, two failure modes that flat policies show clearly and that the LL cannot cause |
| 🟡 **Arithmetic goal** | Select the block satisfying an arithmetic expression | Scene: digits 3, 5, 8. Instruction: *"Put the block that shows 2+3 on the green cube."* Expected: the 5 block moves; 3 and 8 stay | Simple arithmetic grounded in block selection | One pick-and-place with all the difficulty in selection: cheap to run, and essentially every failure is attributable to the HL |
| 🔵 **Sequence completion** | Extend a numeric sequence found in the scene | Scene: line already reads 2, 4, 6; digits 7, 8, 9 available nearby. Instruction: *"Continue the sequence."* Expected: 8 placed at the end | Rule inference over numeric labels | The rule lives in the scene rather than the prompt, so it tests whether the HL genuinely conditions on what it sees instead of on instruction templates |
| ⛔ **G1** **Odd/even sorting** | Partition digits by parity | Scene: 1, 2, 5, 8. Instruction: *"Put odd digits on the left side and even digits on the right."* Expected: {1, 5} left, {2, 8} right | Category derived from label semantics — but "left side" / "right side" are table regions, and no region predicate exists | Parity is knowledge only the HL can supply and the manipulation is trivial, so it would be a clean HL probe once a region predicate exists |
| 🟡 **Nearest / extreme selection** | Compare labels and act on the extreme | Scene: 3, 6, 9 and a red cube. Instruction: *"Put the largest digit on the red cube."* Expected: 9 on red; 3 and 6 untouched | Comparison across all visible labels | A comparison over every visible label resolved into a single action — the cheapest pure-HL probe in the suite |

## 2. Color-Pattern Construction

Uses uniform colored cubes (red, green, blue, plus extras if available).

| Task | Goal | Example | Reasoning required | Why it suits HL + LL |
|---|---|---|---|---|
| 🟢 **Alternating / zebra stack** | Stack alternating colors | Scene: 2 red + 2 green cubes. Instruction: *"Make a zebra stack."* Expected: R-G-R-G (or G-R-G-R) bottom-to-top; either is valid | Pattern rule induction; block *identity* doesn't matter, only color class | The rule generalizes over color classes rather than block identities, so it tests whether the HL abstracts; the LL side is ordinary stacking it already does well |
| 🟢 **Alternating line** | Same rule but horizontal, aligned row | Scene: 3 red + 3 blue cubes. Instruction: *"Line them up alternating red and blue."* Expected: R-B-R-B-R-B, aligned and touching | Pattern + spatial alignment | Currently an LL and executor probe more than a planning one — 4 episodes out of 256 means execution dominates the signal until the push executor improves |
| 🟢 **Rainbow / fixed color order** | Stack or line in a specified color order | Scene: red, green, blue cubes. Instruction: *"Stack them like a rainbow: red on the bottom, then green, then blue."* | Instruction-to-order mapping | The order is handed over in the instruction, making this the LL-isolating control for the two induced-pattern rows around it |
| 🔵 **Pattern completion** | Continue a partial pattern found in the scene | Scene: line already reads R-G-R; one green and one blue cube nearby. Instruction: *"Continue the pattern."* Expected: green appended (R-G-R-G); blue would be wrong | Rule inference from the *scene*, not the instruction | The HL must read the rule off the table and commit to the one correct continuation; picking the wrong color is an unambiguous planning error, not an execution slip |
| ⛔ **G3** **Pattern with choice** | Satisfy a pattern rule when multiple valid assignments exist | Scene: 3 red + 3 green cubes. Instruction: *"Make an alternating stack of 4."* Any of several block choices works, but the HL must not mix them mid-stack | HL must commit to a consistent assignment (any valid one) — needs `exists`, which the pipeline rejects | Tests plan coherence across time: the HL must hold one valid assignment instead of drifting mid-stack, which is the characteristic open-loop VLA failure |
| 🟢 **Symmetric / mirrored line** | Build a palindromic color sequence | Scene: 2 red, 2 green, 1 blue. Instruction: *"Make a line that reads the same from both ends."* Expected: e.g. R-G-B-G-R | Longer-horizon ordering with a non-trivial rule | A longer horizon under a rule constraining both ends, so subgoal-fraction metrics stay informative where binary success would sit at zero |
| ⛔ **G1** **2D shapes** | Arrange blocks in an L, a square, a 2x2 grid, or a pyramid | Scene: 3 cubes. Instruction: *"Build a pyramid."* Expected: two cubes placed touching side-by-side first, third centered on top — top-first ordering fails | Spatial layout planning; `on` is single-support, so "resting on two blocks at once" has no encoding, and a 2x2 grid needs simultaneous x and y relations | Support relations the symbolic vocabulary cannot express, forcing the HL to plan geometrically rather than over predicates — and the LL to place with real precision |

## 3. Counting & Numerosity

| Task | Goal | Example | Reasoning required | Why it suits HL + LL |
|---|---|---|---|---|
| 🟢 **Stack exactly N** | Stack N blocks with more than N available | Scene: 6 cubes. Instruction: *"Stack 3 blocks."* Expected: one 3-stack, 3 cubes untouched — stacking a 4th is a failure | Cardinality; knowing when to *stop* | Deciding when to stop is a call no reactive controller makes well, over-running is trivially detectable, and N extrapolates cleanly beyond the training range |
| 🟢 **Stack N of a color** | Count restricted to a category | Scene: 4 red + 3 blue cubes. Instruction: *"Stack 3 red blocks."* Expected: 3-stack of red only; any blue in the stack fails | Counting restricted to a category | Couples a count with a category filter, so grounding errors and counting errors leave distinguishable end states and can be scored apart |
| ⛔ **G2** **Flip a block N times** | Repeat `reorient` a fixed number of times | Scene: one red cube. Instruction: *"Flip the red block 3 times."* Expected: exactly 3 flips (odd count → net orientation change is checkable) | Counting *actions*, not objects — the goal is a trajectory property, and the planner will reach the same `ori_of` in one flip | Would test whether the HL can emit one subgoal repeatedly while tracking its own progress; the LL primitive is already solved, so the count is the whole task |
| ⛔ **G2** **Rotate N quarter-turns** | Repeat `rotate` with a specified increment | Instruction: *"Rotate the blue block 90° twice."* Expected: net 180° yaw; one 180° rotation also acceptable if action counting isn't enforced | Same as above: only the net `ori_of` is checkable, so "twice" is unsupervisable | The same repetition-tracking probe on a different primitive, with net orientation available as at least a partial check |
| ⛔ **G1** **Move N to a region** | Relocate a count of blocks to a spatial region | Scene: 5 cubes in the center. Instruction: *"Push 2 blocks to the right side of the table."* Expected: exactly 2 in the right region | **Was previously marked 🟢 in error.** "The right side of the table" is an absolute region; `on_table_side` has no vectorized checker and no generator emits it. Only block-relative encodings (`on_right(a, b)`) are available, which is a different task | Pairs a count with a destination, which is how most real household instructions are phrased, so it is worth having once regions exist |
| 🟢 **Split into groups** | Partition into equal groups | Scene: 4 cubes. Instruction: *"Make two stacks of 2."* Expected: two separate 2-stacks; one 4-stack fails | Partitioning; multiple simultaneous subgoals | Two subgoals advance in parallel, so the HL must remember which stack it is on — an interleaving test that single-goal tasks cannot produce |
| 🔵 **Numeric comparison** | Satisfy a relational cardinality constraint | Scene: 2-stack on the left, 2-stack on the right, 1 loose cube. Instruction: *"Make the left stack taller than the right one."* Expected: loose cube onto the left stack (or move one from right to left) | Relational, not absolute, cardinality. The generator can pin it to one concrete `on` literal, but the scene must start with two built stacks | The target depends on the scene, so the HL has to measure before acting rather than replaying a template, and more than one action sequence is correct |

## 4. Rearrangement Requiring Lookahead (the core TAMP stress tests)

These are the tasks where greedy/reactive policies fail and planning is mandatory.

| Task | Goal | Example | Reasoning required | Why it suits HL + LL |
|---|---|---|---|---|
| 🔵 **Buried target** | Move a block that is currently underneath others | Scene: stack is yellow-on-blue-on-**red** (red at the bottom); green cube on the table. Instruction: *"Put the red block on the green block."* Expected: unstack yellow, unstack blue, then move red onto green — 3 actions for a 1-action instruction | Must unstack blockers first (subgoal not in the instruction) | A one-clause instruction with a three-action solution: the most direct measure of whether the HL emits subgoals nobody asked for, on primitives the LL already has |
| 🔵 **Swap two blocks** | Invert a 2-block stack | Scene: red on blue. Instruction: *"Swap them so blue is on red."* Expected: red → table, blue → red. A policy that grabs blue first is stuck (red is under it) | Needs a temporary table placement — no single action achieves the goal | Requires a temporary placement that satisfies no goal literal, so the HL must accept apparent regression — exactly what imitation-trained flat policies avoid |
| 🔵 **Sussman-style anomaly** | 3-block goal where greedy subgoal order undoes progress | Scene: C is on A; B alone on the table. Instruction: *"Stack them so A is on B and B is on C."* Greedy trap: satisfying "A on B" first (move C off A, put A on B) must be undone to get B onto C. Correct plan: C → table, B → C, A → B | Goal-interaction reasoning; the hallmark TAMP benchmark | Greedy subgoal ordering fails by construction, so it separates genuine planning from plausible-looking action sequencing better than any other task here |
| 🔵 **Occupied destination** | Place a block at a location currently occupied | Scene: blue sits on the marked target region; red nearby. Instruction: *"Put red where blue is."* Expected: move blue aside first, then place red | Must move blue away first. Encode the destination as a third block rather than a marked region, or this becomes **G1** | The blocker is plainly visible and the fix is one extra action, making this the minimal lookahead probe — cheap enough to run at every checkpoint |
| 🔵 **Reversal** | Invert a full stack | Scene: stack reads A-B-C bottom-to-top. Instruction: *"Reverse the stack."* Expected: full teardown (C → table, B → table), then rebuild C, B, A — minimum 4–5 pick-and-places | Full teardown + rebuild, longest-horizon variant | The longest horizon in the suite over a fixed skill set, so success against stack height traces the point where the hierarchy stops holding its plan |
| 🟢 **Conditional goal** (`r_on_red.pddl` style) | Target chosen among candidates by a category condition | Scene: letter R block, two red cubes, one blue cube. Instruction: *"Put the R block on a red block."* Either red cube is valid; the blue one is not | Grounding a category-level goal to a specific object. Note the generator names *one* concrete red cube; the "either is valid" framing lives in the instruction only | Category-to-instance grounding resolved in a single action, isolating HL object selection from LL execution; at 200 episodes it is the best-supported task in this family |

Every goal in this family is already writeable — plain `on` / `on_table` conjunctions over named
blocks. The single blocker is uniform: the scene must **start pre-stacked**, and the reset-state
sampler does not produce that. One stacked-initial-state sampler turns this entire family 🟢, which
makes it the highest-value datagen extension in this document — five tasks for one piece of
infrastructure, and the planner already solves them.

## 5. Sorting & Spatial Organization

| Task | Goal | Example | Reasoning required | Why it suits HL + LL |
|---|---|---|---|---|
| ⛔ **G1** **Sort by color into regions** | Partition all blocks by color into table regions | Scene: 3 red + 3 blue cubes interleaved. Instruction: *"Put all red blocks on the left and all blue blocks on the right."* Expected: 6 relocations (minus any already in place) | Category-wise iteration over objects — blocked purely on the missing region predicate, not on the sorting itself | Iteration over a set until it is exhausted: the HL has to track which blocks it has already handled, which no single-object task exercises |
| 🟢 **Isolate** (`isolate.pddl`) | Move one block away from all others | Scene: 4 cubes clustered together. Instruction: *"Move the green block away from the others."* Expected: green ends up with clearance from every other block | Spatial predicate reasoning (negative constraints) via negated `pick_obstructs`. Generable in principle, but **the planner timed out on all 256 instances** in `jul26_hvla` — see the run notes | The one task where TAMP itself exhausts its budget, so a learned HL that solves it would beat the planner that supervises everything else. Needs a non-TAMP data source first |
| 🟢 **Push-align** (`push_align.pddl`) | Push blocks into an aligned row | Scene: 3 cubes at scattered y-offsets. Instruction: *"Push the blocks into a straight line."* Expected: pushes ordered so earlier-aligned blocks aren't knocked out of place | Non-prehensile planning, ordering pushes to avoid collisions | Non-prehensile and LL-dominated with a checkable ordering requirement — a useful counterweight to a suite otherwise heavy on pick-and-place |
| ⛔ **G1** **Clear a region** | Empty a marked region | Scene: 3 cubes in the table center, 2 outside it. Instruction: *"Clear the center of the table."* Expected: exactly the 3 center cubes move out; required action count depends on the scene, not the instruction | Goal defined by *absence* over a region — needs both a region predicate and negation support | The goal is stated as an absence, so the HL reasons about what should not be there instead of matching a target arrangement — and the action count comes from the scene |
| ⛔ **G4** **Line up by size** | Order blocks by physical size | Scene: 3-, 4-, 5-cm cubes scattered. Instruction: *"Line them up from smallest to largest."* Expected: 3-4-5 left to right | Not just a missing predicate: `block_size_range` samples **one size per env shared by all blocks**, so a scene containing differently-sized cubes cannot be built, and the correct ordering would not be known until reset time anyway | Ordering by a perceived physical property rather than a printed label, which tests visual estimation instead of symbol reading — the only task here that does |

## 6. Collision & Physical-Feasibility Reasoning

Tasks where the *symbolic* plan is trivial but geometric/collision reasoning determines success.
These probe whether the HL accounts for physical feasibility — the "motion" half of TAMP.

| Task | Goal | Example | Reasoning required | Why it suits HL + LL |
|---|---|---|---|---|
| 🔵 **Obstructed placement** | Place a block where the only valid spot is occupied | Scene: A and B near the table edge; the only free spot beside B holds a yellow distractor. Instruction: *"Put A next to B."* Expected: move yellow away first, then place A — the clearing action is never mentioned | Must move the distractor first — a clearing action derived from geometry, not the instruction. Goal is a plain `next_to` | The symbolic plan is one action and geometry forces a second, so it asks whether the HL reasons about feasibility at all — the cheapest test of the motion half |
| 🔵 **Pick order in clutter** | Retrieve a block tightly surrounded by others | Scene: target red cube boxed in by 4 touching neighbors, gripper can't descend. Instruction: *"Pick up the red cube and put it on the plate."* Expected: nudge/move one neighbor (or pick an angled approach) before grasping | Choosing which neighbors to move (or approach direction) to make the grasp feasible. Goal is a plain `on` | Loads both halves at once: the HL picks which neighbor to clear from geometry alone, and the LL still has to make a grasp with almost no margin |
| 🔵 **Blocked push path** | Push a block along a corridor containing an obstacle | Scene: cube A on the left, goal region on the right, cube B sitting midway on the straight-line path. Instruction: *"Push A to the right side."* Expected: move B out of the corridor first, or route the push around it | Corridor reasoning for non-prehensile actions. Express the destination as `on_right(A, ref_block)`; phrasing it as a table region makes it **G1** | The LL executes pushes essentially open-loop, so a bad HL choice fails visibly instead of degrading gracefully — a sharp, well-attributed signal |
| 🔵 **Build near existing structure** | Extend an arrangement without toppling completed work | Scene: a finished 3-stack; instruction: *"Place the yellow cube right next to the stack."* Expected: approach and placement that don't clip the stack — knocking it over fails even though the placement predicate would hold | Placement and approach must not topple prior work. Needs the pre-stacked sampler; the "don't topple" part is enforced by the existing `on` checks on the stack | LL precision dominates and the failure mode is unmistakable; the HL only has to recognize that nearby completed work is fragile, so this reads out the LL almost alone |
| ⛔ **G1** **Tight packing** | Fit N blocks into a region barely large enough | Scene: marked tray region fitting exactly 3 cubes; 3 cubes outside. Instruction: *"Put all three cubes in the tray."* Expected: fill back/corner slots first — placing the front cube first blocks access to the back slot | Placement ordering (insert from the back/corner first) — requires a bounded region predicate, and there is no tray asset | The clearest case of motion-level constraints dictating symbolic decisions: the correct order follows from reachability, not from the goal |
| ⛔ **G1** **Reachability-forced staging** | Goal location at the edge of the reachable workspace | Scene: goal region at the far edge; cube starts at the near edge on the opposite side. Instruction: *"Put the cube on the marked spot."* Expected: an intermediate re-grasp/staging placement mid-table when a single carry is kinematically infeasible | Recognize kinematic limits and re-stage. The goal is an absolute table pose, which no predicate can express | Forces the HL to model its own embodiment limits — something a symbolic planner gets for free from the motion layer but a learned planner must acquire from data |
| ⛔ **G4** **Unstable intermediate states** | Stack where base choice determines stability | Scene: one large flat block and one small block. Instruction: *"Stack these two."* Expected: small on large; large on small topples | Requires two differently-sized blocks in one scene, which the shared per-env `block_size_range` cannot produce | Needs a physical stability prior that no predicate encodes, which is exactly the kind of common sense a pretrained VLM should contribute over a planner |

Most of this family is **goal-writeable but scene-blocked** (🔵): the goals are ordinary `on` /
`next_to` literals, and the missing piece is an **adversarial initial-state sampler** that places an
obstacle at the goal spot, in the push corridor, or surrounding the pick target. CuRobo already does
the collision checking, so the planner would solve these scenes if we could sample them.

The three ⛔ entries are different in kind and will not be fixed by a sampler: they need an absolute
position or region predicate (tight packing, reachability staging) or heterogeneous block sizes
(unstable stacking), neither of which the current system has.

The clean / few / many distractor axis interacts strongly with this family: with many distractors,
*every* task from families 1–5 gains an implicit collision-reasoning component. This means TAMP
datagen on green tasks with many distractors **already produces collision-reasoning supervision
organically**, even though the targeted probes above are eval-only.

## 7. Compositional / Chained Instructions

Concatenate primitives to test long-horizon instruction following:

- 🟢 "Spell CAT, then flip the Q block." (independent subtasks — order-free; the combined goal is
  still a single predicate conjunction, so TAMP datagen works)
  *Why it suits HL + LL:* both skills are trained and the clauses do not interact, so a failure
  here is multi-clause language parsing rather than planning — the lowest rung of composition.
- 🟢 "Stack 3 red blocks, then put the A block on top." (dependent ordering, but still expressible
  as one final-state goal)
  *Why it suits HL + LL:* the second clause is only executable after the first, so the HL must
  sequence rather than interleave, and per-clause scoring localizes exactly where the chain breaks.
- ⛔ **G1** "Sort blocks by color, then make a zebra stack from the left group." (the zebra half is fine;
  "the left group" is a table region, which has no predicate)
  *Why it suits HL + LL:* the second clause refers to a set the first clause created, forcing the
  HL to plan against its own predicted future state rather than the observed one.
- 🟡 "Line up the digits ascending, then put the letter matching the count on top of the last one."
  (cross-family: digits + counting + letters. The generator computes both the ordering and the
  matching letter, then emits one `on_right` chain plus one `on` literal — a single conjunction)
  *Why it suits HL + LL:* fuses three families never paired in training, with each component
  independently measurable, so compositional failure can be separated from component failure.
- ⛔ **G2** "Undo": build a stack, then "put everything back on the table." (temporal goal; the final
  state is just `on_table` for everything, which the initial state already satisfies, so a
  state-goal planner emits the empty plan and supervises nothing)
  *Why it suits HL + LL:* reverting requires remembering what was done, which is the one place a
  learned HL with episode context could outperform the state-goal planner that supervises it.

---

## Blocker Summary

Across the 53 tasks in this document:

| Mark | Count | Meaning |
|---|---|---|
| 🟢 | 18 | Generable today |
| 🟡 | 7 | Expressible; needs one new generator script |
| 🔵 | 14 | Goal is writeable; needs a new initial-state sampler |
| ⛔ | 14 | Not specifiable in the current system |

**The single highest-leverage change is an initial-state sampler that can start a scene pre-arranged**
(blocks already stacked, a distractor already occupying the goal spot). That one piece of
infrastructure unlocks 14 tasks — the entire lookahead family plus most of the collision family —
without touching the predicate vocabulary or the planner. Writing the 7 🟡 generators is cheaper per
task but adds no new capability.

The 14 ⛔ tasks break down by what they would actually require:

| Code | Count | Tasks | What would unlock them |
|---|---|---|---|
| **G1** — no predicate | 8 | Odd/even sorting, 2D shapes, move N to a region, sort by color into regions, clear a region, tight packing, reachability staging, "sort then zebra" | A region / absolute-pose predicate with a vectorized checker. Six of the eight are blocked *only* on the phrase "left side" / "the center" / "the tray" — a single `in_region(?b, ?r)` predicate plus region objects would clear them. 2D shapes additionally need multi-block support |
| **G2** — not a world state | 3 | Flip N times, rotate N quarter-turns, "undo" | A different supervision signal entirely — action-sequence or trajectory-level goals rather than state goals. Not a predicate problem |
| **G3** — open / disjunctive | 1 | Pattern with choice | `exists` / `or` support in the goal parser *and* the vectorized success check. Currently `exists` is rejected and `or` is silently flattened, which is the more dangerous failure |
| **G4** — reset-time randomization | 2 | Line up by size, unstable intermediate states | Per-block size control. Today `block_size_range` samples one size per env shared by every block, so heterogeneous-size scenes cannot be built at all |

Worth noting that G1 dominates, and most of it is one missing concept: **the system has no way to
refer to a place on the table**, only to other blocks. Every spatial goal is pairwise-relative. Adding
region objects would be a larger win than any individual generator.

---

## Generalization: Interpolative vs. Extrapolative

Define the training distribution explicitly per task family so every eval condition can be
labeled **in-distribution**, **interpolative** (inside the convex hull of training values, but
unseen), or **extrapolative** (outside it). Suggested splits:

| Family | Training set | Interpolative eval | Extrapolative eval |
|---|---|---|---|
| Spelling | Words of length 3 and 5, from 20 of 26 letters | Unseen length-4 words from trained letters | Length 6–7 words; words using the 6 held-out letters |
| Digits | Sequences/orderings over digits {0–5, 8, 9} | Unseen orderings of trained digits | Sequences involving 6, 7; 4-digit numbers when training used ≤3 |
| Counting | Stack N for N ∈ {2, 3, 5} | N = 4 | N = 6, 7 (also stresses LL: taller stacks, higher grasps) |
| Patterns | 2-color alternation, 3-block mirrors | 2-color alternation with unseen color pair | 3-color cycles, longer mirrors, patterns over *letters* instead of colors |
| Repetition | Flip 2 or 3 times | — (integer gap too small) | Flip 5 times |
| Distractors | 0–4 distractors | 5 | 8–12 |
| Scene scale | 4–8 total blocks | 6 (unseen combos) | 12–15 total blocks |

Report interpolation and extrapolation success **separately per family** — averaging them hides
the most informative signal. Extrapolative counting and word length are the clearest tests of
whether the HL learned a *rule* versus memorized goal templates.

## Composition

Composition is evaluated at three levels, in increasing difficulty:

1. **Within-family recombination.** Novel combinations of trained atoms: unseen words from
   trained letters, unseen color orders from trained pattern rules, trained counts applied to
   unseen block categories. (Cheapest; covered by the held-out splits above.)
2. **Cross-family single instruction.** A goal that fuses two trained families never paired in
   training: "spell a word using only red letter blocks" (spelling × color), "stack digits in
   ascending order" (digits × ordering × stacking), "make an alternating stack of exactly 4"
   (pattern × counting).
3. **Sequential chaining** (Section 7). Multi-clause instructions where later clauses depend on
   earlier outcomes. Score per-clause to localize where the chain breaks.

Key control: verify each component is individually solved (≥ some threshold in isolation)
before attributing compositional failures to composition itself.

## Additional Evaluation Axes

Beyond distractors, generalization, and composition:

1. **Horizon-length scaling.** Report success as a function of minimum plan length (1, 2, 4, 6, 8+
   actions). TAMP-competence shows up as a slower success decay with plan length.
2. **Instruction phrasing.** Paraphrase goals ("stack them like a rainbow" vs. "red on green on
   blue") to test language robustness independent of planning.
3. **Initial-state adversity.** Same goal, initial states ranked by difficulty: blocks free on
   table → goal blocks pre-stacked wrongly → goal blocks buried under distractors.
4. **Mid-episode perturbation (recovery).** Knock over the stack or teleport a placed block back
   to the table partway through; measure whether the HL replans. This directly tests closed-loop
   reasoning vs. open-loop plan memorization.
5. **Distractor confusability.** Distractors visually similar to goal blocks (same color, glyphs
   like O/0, I/1, 6/9, M/W) vs. clearly distinct — separates grounding errors from planning
   errors. The letter/digit set makes this especially sharp: O-vs-0 and 6-vs-9 (orientation-
   dependent identity) are adversarial grounding probes.
6. **Ablation baselines.** For each task, also run: (a) LL-only with oracle HL subgoals
   (upper-bounds LL execution), (b) TAMP replay (`scripts/evaluate.py` replay mode, oracle
   upper bound), (c) random/zero action floors. This decomposes failures into
   *HL planning error* vs. *LL execution error*.

## Metrics

- **Task success rate** — all goal predicates satisfied at episode end (existing predicate
  checkers: `On`, `OnTable`, `OriOf`, `NextTo`, isolation).
- **Subgoal completion fraction** — partial credit as the fraction of goal predicates satisfied;
  essential for long-horizon tasks where binary success saturates at 0.
- **Progress-over-time** — max predicates satisfied at any point vs. at episode end; a gap
  indicates the policy *undoes* its own progress (a lookahead failure signature).
- **Action efficiency** — executed HL steps ÷ minimum plan length (from the TAMP planner).
- **Failure taxonomy** — wrong object grounding / wrong action choice / correct plan but LL
  execution failure / no-op or dithering. Attributable via the ablation baselines above.
- **Recovery rate** — success after perturbation ÷ success without perturbation.

## Suggested Priority

If compute-constrained, the highest-signal subset is:

1. **Held-out words as stacks** (clean / few / many distractors) — composition + orientation, with
   the interpolative/extrapolative word-length split.
2. **Buried target + swap** — minimal, unambiguous lookahead tests.
3. **Stack exactly N with excess blocks**, N extrapolated beyond training — stopping condition +
   rule extrapolation, cheap to generate.
4. **Ascending digit line** — numeric ordering derived from labels; unseen digit subsets give
   interpolation for free.
5. **Obstructed placement** — the cheapest pure collision-reasoning probe.
6. **Mid-episode perturbation on any of the above** — closed-loop replanning.

## Mapping to Existing Infrastructure

| Task family | Existing generator / needs new |
|---|---|
| Spelling (stack, line, distractors) | `scripts/task_gen/spelling.py` (generalize `LETTER_BLOCKS` / `WORD_ASSIGNMENTS` to the full A–Z set and arbitrary word input) |
| Digit tasks (ordering, sequences, numbers) | **New generator** (same structure as spelling, goal ordering computed from labels) |
| Stack N (colored) | `scripts/task_gen/stack_red_blocks*.py`, `any_on_any.py` |
| Flip / rotate N times | `scripts/task_gen/flip.py`, `rotate.py`, `pnp_flip_back.py` (extend for repetition counts) |
| Conditional goals | `scripts/task_gen/r_on_red.py`, `random_n_goal_pred.py` |
| Isolate / push-align | `scripts/task_gen/isolate.py`, `problems/push_align*.pddl` |
| Zebra / rainbow / mirrored patterns | **New generator** (straightforward `On`/`NextTo` chains over color classes) |
| Swap / reversal / buried target (🔵) | **New initial-state sampler** (pre-stacked scenes); goals themselves need nothing new |
| 2D shapes, region-based sorting (⛔ G1) | **New predicate + vectorized checker** — `in_region` / pose-target goals. A generator alone is not enough |
| Collision-reasoning scenes (🔵) | **New initial-state sampler** (place distractors at goal locations, in push corridors, or surrounding pick targets; goals reuse existing predicates) |
| Derived-goal tasks: alphabetical, arithmetic, extreme digit (🟡) | **New generator** only — the generator computes the answer and emits concrete literals |
| Perturbation protocol | **New eval hook** in `scripts/evaluate.py` (mid-episode state reset of one object) |

Distractor counts are already supported via `DistractorPool` in the task specs, so the
clean / few / many axis is a sweep over `--distractors` ranges in existing generators.

---

## First Datagen Run (`jul26_hvla`)

16 families x 8 PDDL problems x 32 reset states = 256 attempts each, run (Jul 2026) through
the legacy three-stage TAMP pipeline, which is not part of this release. Every one of the 95
jobs exited 0 — the shortfalls below are task attrition, not infrastructure failure.

| Family | Plans / 256 | Episodes | vs 128 |
|---|---|---|---|
| stack_exactly_n | 255 | 249 | ok |
| split_into_groups | 220 | 220 | ok |
| letters_orientation | 250 | 206 | ok |
| conditional_r_on_red | 254 | 200 | ok |
| color_zebra_stack | 199 | 189 | ok |
| make_number_line | 256 | 150 | ok |
| color_rainbow | 152 | 137 | ok |
| push_next_to | 195 | 92 | short |
| spell_line | 232 | 84 | short |
| make_number | 206 | 71 | short |
| chained_conjunctions | 121 | 59 | short |
| spell_stack | 113 | 30 | short |
| spell_stack_distract | 83 | 21 | short |
| color_alternating_line | 256 | 4 | **executor limit** |
| color_mirror_line | 222 | 3 | **executor limit** |
| isolate | 0 | 0 | **no plans** |

Three findings worth knowing before generating more data:

1. **Chained `on_right` does not survive past ~3 blocks.** Execution success falls off a
   cliff with the length of the `on_right` chain — 3-block lines (`spell_line`,
   `make_number_line`) reach 36–59%, but 4- and 5-block color lines collapse to ~1.5%,
   failing with `EFFECT_CHECK_FAILED` on `push_to_right`. Each push disturbs blocks placed
   earlier, and the goal check requires every `on_right` to hold at once. Keep line layouts
   at 3 blocks, or add an executor that places rather than pushes.
2. **`reorient` is the bottleneck for glyph blocks.** Every letter/digit family fails
   predominantly with `EFFECT_CHECK_FAILED: ori_of(<block>, oN) not satisfied after
   reorient`. Note this is *not* caused by the `block_letter` / `block_digit` types: those
   subtypes (like the legacy `block_r_e` / `block_o_b` / `block_t_g`) are declared in
   `domain.pddl` but referenced by no action precondition and nowhere in `tmp3`, so they
   are inert labels. Reorient-only tasks on the same assets (`letters_orientation`) reach
   82%, so it is the reorient-plus-stack combination that attrites.
3. **`isolate` never plans.** All 256 instances exhaust the planner's search budget at
   ~470s each with no error emitted, so the family produced nothing to execute.

---- FILE: docs_lerobot_recording.md ----

# LeRobot dataset recording

ToyBlocks has one LeRobot recorder,
[`IsaacDataRecorderLeRobot`](../src/toyblocks/vecgen/recording/lerobot_recorder.py) in
`toyblocks.vecgen.recording`. It is a port of TAMP's `tmp3.DataRecorder` recorder (the one
TAMP stage 3 uses) and needs nothing from TAMP. Eval (`scripts/evaluate.py --save_lerobot`)
records with it, so an eval rollout and a datagen episode have the same schema, the same row
layout and the same video formats.

## Row layout

Each row holds an observed state and the action taken *in* it:

    row t:  observation.* = s_t,  action.* = a_{t+1}  (drives s_t -> s_{t+1})
    row N:  observation.* = s_N,  action.* = 0, action.is_valid = False

Recording samples the sim after a step, so a sample carries s_k beside the command that produced
it; the recorder holds each frame one record call and moves the next call's action block onto it.
The PD-gain columns (`observation.state.current_*`) and `action.pd_mode` move with the action.
The recorder supports per-step gain switching. Current datagen uses one uniform gain profile,
so within a dataset these columns stay constant. Every dataset's `meta/info.json` carries `toyblocks_row_layout`.

Eval envs auto-reset inside `env.step`, so the sample taken on an episode's last step is already
the next episode's s_0. `record_step_batched(reset_env_ids=...)` holds that sample as the next
episode's row 0 and the finished episode's last held frame becomes its terminal row;
`capture_reset_frames` records the first episode's s_0 after `env.reset()`.

## Output layout

    <data_dir>/<name>_success/     LeRobot v3 dataset of the successful episodes
    <data_dir>/<name>_failure/     ... and of the failed ones
        data/chunk-000/file-000.parquet
        meta/{info.json, stats.json, tasks.parquet, episodes/, recording_config.json, provenance.json}
        videos/observation.images.<cam>/chunk-{ep // 1000:03d}/file-{ep % 1000:03d}.mp4
        videos/observation.depth.<cam>/chunk-.../file-....mp4

One video file per episode and camera. RGB is encoded with the `rgb_codec` constructor argument.
Its default, `libsvtav1`, is what datagen uses. Eval passes `libx264` (`--video_codec`), because
an eval run keeps hundreds of streams open at once and x264 needs far less native memory per
stream: measured 5–14 MiB, against 27–57 MiB for SVT-AV1.
Depth is lossless 12-bit millimetres (`gray12le` HEVC, GOP 2, so a training reader decodes at
most one extra frame per random access). The render pipeline's `rg8_55_224` depth is a
separate, lossy stream: 224×224, clipped at 1,023 mm, 5+5-bit RG packing. The recorder can add
it alongside the main depth with the `extra_depth` argument, but eval does not set that. Eval
writes under `<output_dir>/lerobot_dataset/` and records,
per episode, `output_lerobot_dataset_dir` / `output_lerobot_episode_index` in
`eval_episodes.json`.

## Schema

The datagen schema: robot state (`observation.state.*`: joints, gripper, EE pose, wrench, gains,
torques), actions (`action.joint_target`, `action.relative_joint_target`, `action.ee_target` =
FK of the joint target, `action.relative_ee_target`, `action.gripper_position` binarised,
`action.gripper_raw`, `action.pd_mode`, `action`), poses of every object
(`observation.state.object_pose.*`), robot link (`robot.poses.*`) and camera
(`observation.camera_pose.*`, `observation.camera_intrinsics.*`), scene profile
(`cube_scale`, `table_height_delta`, `table_friction`, `friction_properties`, `profile_id`),
symbolic actions/state, `pddl_goal`, `task`, `glyph_map`, `block_variable_map`,
`source_problem`, `instance_id`, `is_episode_successful`, `error`.

Optional columns (constructor flags, off for datagen, on for eval):

| Flag | Columns |
|---|---|
| `action_dim` | `action.policy`, the raw policy action (staged with `set_pending_actions_batched`) |
| `record_hl_model` | `action.hl_model_output`, `action.hl_prev_action`, `action.hl_input_prompt`, `action.hl_done` (`set_hl_model_outputs_batched`) |
| `query_physx_properties` | `observation.state.object_mass`, `table_mass`; friction columns from the live PhysX materials |

`set_pending_pd_modes_batched` overrides the stiffness-derived `action.pd_mode` for a step.
Eval computes `action.ee_target` with
[`ArticulationEEFK`](../src/toyblocks/vecgen/recording/articulation_fk.py) (the sim robot's own
kinematics, checked against the observed EE pose); datagen passes its cuRobo FK.

## Throughput and memory

What recording costs the simulation thread is one batched snapshot per record call: robot state
copied to the host in one transfer, camera images converted to their recorded dtypes and copied
*on the GPU*. Everything else runs elsewhere:

- **Frame builder thread.** Copies the camera snapshot to the host on a side CUDA stream (it
  waits only for the snapshot, never for later simulation work), builds the rows and hands them
  to the writers.
- **Shared-memory frames.** Camera images go to their writer through a shared-memory slot
  arena (`_shm_slots.py`); only a descriptor is queued, so the images are never pickled in the
  simulation process. Falls back to the queue when `/dev/shm` is too small.
- **Writers.** `num_writers` encoder subprocesses (eval: `--num_shards`, default 8); env `i`
  goes to writer `i // ceil(N / K)`. Each stages a private dataset pair that `finalize` stitches
  into the published pair, so the layout does not depend on `K`. A writer encodes on a pool of
  `cores / K` threads, one codec thread per stream.
- **Small encoder processes.** They fork from a forkserver that preloads only the encoder
  module and never re-import the caller's script (which launches Isaac): ~0.35-0.65 GB each.
- **Bounded RAM.** Frames in flight may take `TMP3_RECORDER_INFLIGHT_GB` (default
  min(4 GiB, RAM / 4)), split across the writers; with an arena, half of a writer's share is the
  arena. Past the budget, frames are spilled to node-local disk (`TOYBLOCKS_RECORDER_SPILL_DIR`,
  else the video staging root, else `/tmp`; never network storage) and read back in order. The caller only
  waits when that disk is short of space (`TOYBLOCKS_RECORDER_SPILL_MIN_FREE_GB`, default 20).
  The spill is a burst buffer: an encoder that is slower than the simulation for good fills it.
- **Encode cost.** Depth (lossless 12-bit, GOP 2) is the expensive stream; x265 runs it at
  `ultrafast`, which changes speed and memory, not the decoded values (640x360: 273 fps per
  core and <1 MiB per stream vs 52 fps / 85 MiB at x265's default). x264 RGB takes ~14 MiB per
  open stream at 640x480 against SVT-AV1's ~57 MiB.

Measured on one RTX 5090 box (32 cores, 60 GB), stub policy, 2 cameras at 640x360, 10 s
episodes, 8 writers:

| 64 envs | wall | lowest available RAM | caller thread per record call |
|---|---|---|---|
| no recording | 100 s | 36.7 GB | - |
| previous eval recorder | 137 s | 28.3 GB | - |
| this recorder | 115 s | 30.6 GB | 4 ms |

At finalize the recorder prints the caller-thread cost (`[recorder] caller thread: ...`) and any
waits on the encoder budget.

## Eval flags

| Flag | Default | |
|---|---|---|
| `--save_lerobot` | off | record |
| `--lerobot_dataset_name` | run name | `<name>_success` / `<name>_failure` |
| `--num_shards` | 8 | encoder subprocesses |
| `--video_codec` | `libx264` | RGB codec (`libx264` / `libsvtav1`) |

## Tests

`tests/vecgen/test_recorder_rows.py` (row layout, auto-reset rows, captured s_0, staged extras,
discards, writer routing and the episode index map, spilling) and
`tests/vecgen/test_recorder_stitch.py` (stitching writer datasets) run without Isaac.

---- FILE: docs_render_DETERMINISM.md ----

# Determinism in render and `toyblocks.domain_randomization`

What is reproducible, what is not, and which changes moved the line. Every number here was
measured on this repo (aug24_bigblocks_flip_a, one problem, RTX 5090), not asserted.

## The contract

**Same params, same output — going forward.** `--dr_seeding hash` is the anchor and the main
supported mode. Under it every per-episode value derives from `md5(seed | concern |
episode_index)`, so an episode's draw does not depend on how many episodes preceded it.

**Backward compatibility with already-rendered datasets is explicitly NOT a goal.** A bug fix may
change what a given yaml renders. When it does, it is listed below.

## What is bit-reproducible, and what is not

Two runs of the same renderer with byte-identical inputs:

| artifact | reproducible |
|---|---|
| every `.parquet` (all recorded DR parameters) | **yes, bit-exact** |
| every `observation.depth.*` video | **yes, bit-exact** |
| every `observation.images.*` (RGB) video | **no** |

RGB self-noise, front camera: **mean 1.8/255, max 55, ~87% of pixels differ** — between render
and *itself*. So "pixel-exact RGB" is not a meaningful acceptance criterion for anything.

Useful reference scales, all measured the same way:

| comparison | mean abs diff |
|---|---|
| renderer vs itself, identical inputs | 1.8 |
| same scene, two different construction paths | 2.1 |
| same scene, DR off vs full `allrand` | 21.0 |
| different scenes entirely | 86.7 |

Anything at ~2 is noise. Anything at ~20+ is a real difference.

**Consequence for verification:** compare parquet + depth, never RGB. Concretely: hash every
`*.parquet` and every `observation.depth.*` mp4 under the output root and compare those digests
between two runs. An RGB diff proves nothing, and an RGB *match* is luck. Guard the comparison
against empty inputs -- comparing two failed renders that produced no files reports a false
match.

## Seeding modes

| mode | per-episode value depends on | prefix-free |
|---|---|---|
| `hash` (default, supported) | `md5(seed \| concern \| episode_index)` | yes |
| `indexed` | `SeedSequence(seed, episode_index)` | yes |
| `stream` (legacy) | position in one advancing stream | **no** |

Under `stream`, sampling a subset returns different values than sampling the whole list.
`interpreter.sample_episodes()` therefore refuses `stream` rather than silently returning numbers
that do not match a bulk call.

## Statefulness that is NOT covered by seeding

`SkyBuckets` (skybox and `env_sphere` texture choice) is a **without-replacement queue**. It is
stateful by design — that is what stops an HDRI repeating before the pool is exhausted — and no
seeding mode makes it order-independent. Sampling one episode at a time restarts the queue and
returns its first entry every time.

Both callers must therefore sample the FULL episode list in one call:

* **render** does this already via `--fragment_invariant` (default ON): a fragment keeps the
  whole per-problem episode list so its DR matches a single-machine run.
* **a gym wrapper** must pass `episode_keys=` up front (see
  `toyblocks_dagger/.../dr_wrapper.py`), after which each reset only *applies* values already
  drawn. Without it the wrapper warns.

This is pinned as a strict `xfail` in
`tests/env_randomization/test_sample_episodes_incremental.py` — a documented property, not a
regression.

## Per-wave levers

Dome/skybox intensity, exposure ISO, sun, fill and the scenario pick are drawn once per wave from
rngs seeded in `setup()` (`rseed+12345` light, `+4242` fill, `+777` exposure,
`sky.seed|rseed_base +999+prob_salt`, scenario `_sseed+31337`). They depend on wave grouping, so a
caller whose batching differs from render's waves gets different globals even at `hash`.

## The salt

`prob_salt = _stable_seed_salt(Path(job["out_dir"]).name)` — the basename of the **output**
directory, not the problem or env directory. A caller with no output directory (a gym wrapper)
must be handed the same string; nothing in the env or the yaml reveals it. Getting it wrong
produces a completely different scene with no error.

## Changes that affect output

| change | breaks old-dataset determinism? | rendered pixels |
|---|---|---|
| `setup()` no longer dies on a yaml without `scenarios:` (67 of 106 yamls) | no | those yamls previously **crashed**; there is no old output to differ from |
| same for `missing` / `desc` | no | as above |
| `apply_wave(active=)`, `setup(salt=/episode_keys=)`, `sample_episodes()`, `apply_wave_cameras()`, `DRSession` | no | verified byte-identical on parquet + depth |
| removal of `orchestrator.py` / `randomizers.py` / `scene_context.py` | no | 516 lines with zero importers, and they crashed on first call |
| `--material_baseline_revert` | **only if enabled** | OFF by default = today's behaviour. ON reverts every library-writable key to the asset before each draw, so materials stop inheriting the previous episode's values. Applies 12 keys where OFF applies 8; the four added (`enabled`, `metallic_constant`, `reflection_roughness_constant`, `specular_level`) are exactly the ones that used to carry over |
| `table_height_delta` now recorded per episode | no | additive metadata; pixels byte-identical. Fixes `render_from_params`, which read it back with a `0.0` fallback and so replayed a **flat table** |
| `--dr_seeding hash` as the default | **yes, vs pre-hash datasets** | intentional: hash is the anchor. Datasets rendered under `stream` will not reproduce under the default |
| `--camera_base data` as the default | **yes, vs datasets rendered before it** | intentional: extrinsics now come from the recorded data rather than `SceneConfig` constants |

## Known non-determinism, unresolved

`render_from_params.py` does **not** reproduce the render it replays: depth differs by mean
2076.7 (16-bit), 76% of pixels, on the aug24 reference. Eliminated as causes: camera pose
(verified live against the record), `--reproduce_placement`, episode pairing, depth encoding,
recorded trajectory state, build args, `skip_initial_step`. The divergence is invariant across all
of those, which points at a structural difference between the two replay loops rather than data.
Since this tool backs the orchestrator's patch path, it matters for future runs.

---- FILE: docs_source_index.md ----

# ToyBlocks Docs

Documentation on the ToyBlocks project and its toy-blocks domain.

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} {octicon}`download;1.2em;sd-text-primary` Installation and Setup
:link: user_guide/workflows/installation_and_setup_instructions
:link-type: doc

Set up ToyBlocks, its submodules and the assets with `uv`, then verify the installation.
:::

:::{grid-item-card} {octicon}`database;1.2em;sd-text-primary` Automatic Data Generation
:link: user_guide/workflows/data_generation
:link-type: doc

Turn a symbolic PDDL task description into a large, automatically-labelled dataset of robot
demonstrations in simulation.
:::

:::{grid-item-card} {octicon}`mortar-board;1.2em;sd-text-primary` Training ManiFlow Policies
:link: user_guide/workflows/imitation_learning
:link-type: doc

Train ManiFlow policies on a merged LeRobot dataset with `scripts/train_maniflow.py`.
:::

:::{grid-item-card} {octicon}`graph;1.2em;sd-text-primary` Policy Evaluation
:link: user_guide/workflows/evaluations
:link-type: doc

Measure how well a trained policy performs in closed loop in simulation.
:::

:::{grid-item-card} {octicon}`hubot;1.2em;sd-text-primary` Agentic Robotics
:link: user_guide/workflows/agentic_robotics
:link-type: doc

Put a frontier vision-language model in charge of the robot, acting through MCP skill tools.
:::

::::

```{toctree}
:maxdepth: 4
:caption: Contents:
:hidden:

user_guide/index
```

---- FILE: docs_source_user_guide_index.md ----

![ToyBlocks](../_static/ToyBlocksLogo_new.svg)

# Workflows

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} {octicon}`download;1.2em;sd-text-primary` 1 · [Installation and Setup](workflows/installation_and_setup_instructions.md)

- [Prerequisites](workflows/installation_and_setup_instructions.md#prerequisites)
- [Setup](workflows/installation_and_setup_instructions.md#setup)
- [Download the assets](workflows/installation_and_setup_instructions.md#download-the-assets)
- [Verify the installation](workflows/installation_and_setup_instructions.md#verify-the-installation)
- [Docker images](workflows/installation_and_setup_instructions.md#docker-images)
:::

:::{grid-item-card} {octicon}`database;1.2em;sd-text-primary` 2 · [Automatic Data Generation](workflows/data_generation.md)

- [Running Pipeline Locally](workflows/datagen/local.md)
- Stages: [1 Tasks](workflows/datagen/task_generation.md) · [2 Environments](workflows/datagen/env_generation.md) ·
  [3 Execution](workflows/datagen/execution.md) · [4 Rendering](workflows/datagen/render.md) ·
  [5 Merge](workflows/datagen/merge.md) · [6 Annotation](workflows/datagen/annotate.md)
- [Recorded Dataset Fields](workflows/datagen/dataset_fields.md)
:::

:::{grid-item-card} {octicon}`mortar-board;1.2em;sd-text-primary` 3 · [Training ManiFlow Policies](workflows/imitation_learning.md)

- [Training on a generated dataset](workflows/imitation_learning.md#training-on-a-generated-dataset)
- [Choosing GPUs and nodes](workflows/imitation_learning.md#choosing-gpus-and-nodes)
- [Resuming and fine-tuning](workflows/imitation_learning.md#resuming-and-fine-tuning)
- [`train_maniflow.py` Reference](workflows/imitation_learning/train_maniflow.md)
- [Setting up a new policy server](workflows/imitation_learning/new_policy_server.md)
:::

:::{grid-item-card} {octicon}`graph;1.2em;sd-text-primary` 4 · [Policy Evaluation](workflows/evaluations.md)

- [Quick start with `launch_eval.py`](workflows/evaluations.md#quick-start-with-launch_evalpy)
- [Replaying Actions from a Dataset](workflows/evals/replay.md)
- [Eval Metrics](workflows/evals/metrics.md)
- [`launch_eval.py` Reference](workflows/evals/launch_eval.md) ·
  [`evaluate.py` Reference](workflows/evals/evaluate.md)
:::

:::{grid-item-card} {octicon}`hubot;1.2em;sd-text-primary` [Agentic Robotics](workflows/agentic_robotics.md)
:columns: 12

[Setup](workflows/agentic_robotics.md#setup) ·
[Run an episode](workflows/agentic_robotics.md#run-an-episode) ·
[Web UI](workflows/agentic_robotics.md#web-ui-the-episode-pages-and-the-portal) ·
[Create a new task](workflows/agentic_robotics.md#create-a-new-task) ·
[ManiFlow skills](workflows/agentic_robotics.md#maniflow-skills)
:::

::::

```{toctree}
:maxdepth: 2
:hidden:

workflows/installation_and_setup_instructions
workflows/data_generation
workflows/imitation_learning
workflows/evaluations
workflows/agentic_robotics
```

---- FILE: docs_source_user_guide_workflows_agentic_robotics.md ----

# Agentic Robotics

The `agentic_robotics/` submodule ([allenai/agentic_robotics](https://github.com/allenai/agentic_robotics))
puts a frontier vision-language model in charge of the robot. The model sees the front camera
image and acts only through MCP tools, one per skill: `pick`, `stack`, `place_on_table`,
`rotate`, `flip`, `return_home`, the gripper, and a zoomed view. Nothing tells it whether it
succeeded; it decides from the images when the task is done or impossible. Every run is recorded
(video, transcript, final-state score) so it can be browsed afterwards.

Two skill backends execute the tools:

| Backend | What runs the skill | Needs |
|---|---|---|
| `oracle` (default) | ToyBlocks's scripted vecgen skills (the ones that record the training demonstrations), planned with cuRobo v2 on privileged simulator state | the `vecgen` extra |
| `maniflow` | a trained ManiFlow low-level policy, through its policy server | the `maniflow` extra and a checkpoint |

## Setup

This is the [Installation](installation_and_setup_instructions.md) sequence with the `vecgen`
and `agentic` extras and the `agentic_robotics` submodule; it needs an NVIDIA GPU (driver 570 or
newer) and [`uv`](https://docs.astral.sh/uv/getting-started/installation/):

```bash
git clone https://github.com/allenai/ToyBlocks.git && cd ToyBlocks
uv venv --python 3.11 && source .venv/bin/activate
git submodule update --init curobo agentic_robotics
uv pip install -e ".[dev,isaac,torch-cu128,vecgen,agentic]"
export OMNI_KIT_ACCEPT_EULA=YES
get-toyblocks-assets --asset-manifest asset_manifest.json   # the robot, block and scene assets
```

The assets are downloaded once per machine into `~/.toyblocks` and symlinked into `assets/`; without
them the first task build fails with a missing robot USD. `pytest tests/install` checks the install,
the submodule pins and the assets (see [Verify the installation](installation_and_setup_instructions.md#verify-the-installation)).

The `agentic` extra installs the `agentic-robotics` package (editable, from the submodule) and
its `agentic-robotics` command. Its MCP SDK needs newer `starlette`, `fastapi`, `uvicorn` and
`idna` than Isaac Sim pins; `pyproject.toml` overrides those four (they serve Isaac's livestream
and web services, which headless runs do not use).

### Your own OpenRouter key

Episodes call the model through [OpenRouter](https://openrouter.ai), and **you need your own
OpenRouter API key**: none ships with the repository, and every episode is billed to the key it
runs with. Create one at <https://openrouter.ai/keys>, then either export it or store it in a file
only you can read:

```bash
export OPENROUTER_API_KEY=sk-or-...
# or
echo "sk-or-..." > ~/.openrouter_key && chmod 600 ~/.openrouter_key
```

`agentic_robotics/scripts/openrouter_spend.sh` prints the key's remaining budget. The model is the
experiment file's `model` (default `fable-5.1`); `--model` picks another key from the adapter's
model table (`opus-5.5`, `sonnet-5.5`, `haiku-4.5`, `gpt-6.1-sol-pro`, `qwen-3.8`). An unknown
key fails with the list of known ones.

Runs are written under `$AGENTIC_ROBOTICS_RUNS_DIR`, or `agentic_robotics/runs/`.

## Build a task's environment packages

A task's scenes are ordinary ToyBlocks env packages, generated with ToyBlocks's codegen the first
time they are needed and kept in `agentic_robotics/data/tasks/` (not tracked in git). A task key
names a family of PDDL variants, and a run draws one; a variant's slug names that scene alone.

This walkthrough runs `spell_hen_patterned_0_feasible_0`, one variant of the Search & Spell family
`spell_hen_patterned` from the released experiments: ten blocks on the table, some stacked, some
letters hidden, and the goal of spelling HEN in a tower. It is a feasible variant, its letters are
ones the released ManiFlow checkpoint trained on, and its blocks come from that checkpoint's
library, so the same scene runs under both skill backends. List what is defined and what is built
locally, then build the scene (a family key would build every variant, twelve here, one
Isaac boot each):

```bash
agentic-robotics tasks
agentic-robotics generate-env --task spell_hen_patterned_0_feasible_0
```

Passing `--generate-env` to `episode`, `page` or `human` builds a missing package on the spot.

## Run an episode

```bash
# One headless, model-driven episode with the scripted skills
agentic-robotics episode --task spell_hen_patterned_0_feasible_0 --backend oracle
```

The run directory holds the video (`video.mp4`), the model's transcript, the resolved
`config.json`, and `evaluation_summary.json`: whether the final scene satisfies the task's PDDL
goal (scored with the package's goal classifier), the tool calls made and the model cost.

## Web UI: the episode pages and the portal

The commands below start local web pages. Open <http://127.0.0.1:8083> for the interactive pages
(the task menu, a model-driven episode, the human-controller interface, the mock page) and
<http://127.0.0.1:8082> for the portal, which browses the logs of current and previous runs; the
two ports differ so the portal can stay open while an episode runs.

```bash
agentic-robotics menu --backend oracle                       # Isaac starts with no scene; pick tasks one after another, watch the model act, interject
agentic-robotics page --task spell_hen_patterned_0_feasible_0 --backend oracle    # one model-driven episode with the interjection page around it
agentic-robotics human --task spell_hen_patterned_0_feasible_0 --backend oracle   # the same episode with you in the model's chair: call the skills yourself
agentic-robotics portal                                      # browse finished runs (videos, transcripts, scores); no Isaac, no model
agentic-robotics portal --static                             # or write the portal as static pages under <runs dir>/portal/
agentic-robotics mock                                        # the page alone, without Isaac or a GPU, for working on the UI
```

An episode page embeds the simulator's 3D viewer, which listens on its own port (8080, or the next
free one) and must be reachable from the browser too. The pages bind to localhost; on a remote
machine either forward the ports or pass `--lan` to bind every interface:

```bash
ssh -L 8083:localhost:8083 -L 8080:localhost:8080 -L 8082:localhost:8082 <gpu-machine>
```

`--port` changes the page's port.

## Create a new task

A task is a PDDL problem (or a directory of variant problems) plus an entry giving the model its
prompt and tool-call budget.

1. **Write the problem.** Problems use ToyBlocks's blocks domain
   (`src/toyblocks/tamp/blocks/domain.pddl`). Put one problem at
   `agentic_robotics/data/problems/<slug>.pddl`, or several variants in
   `agentic_robotics/data/problems/<slug>/*.pddl` (a run draws one at random). Each variant's file
   stem becomes its env-package name, so it must be a valid Python identifier once hyphens become
   underscores. ToyBlocks's task generators write suitable problems. This one writes three
   variants of the scene the ToyBlocks quick start generates training data for, the letter-M
   block beside a red block, each with the goal of one flip of the M block that brings the face
   on its top around to the front:

   ```bash
   python scripts/task_gen/flip.py --direction backward --target-block block_m \
       --distractor-blocks block_red --distractor-count-min 1 \
       --count 3 --seed 0 --out-dir agentic_robotics/data/problems/flip_m
   ```

   See [Task generation](datagen/task_generation.md) for the generators and the PDDL comments
   that randomize the scene.

2. **Register it.** Add a `TaskConfig` to `TOYBLOCKS_TASKS` in
   `agentic_robotics/src/agentic_robotics/adapters/toyblocks/config.py`:

   ```python
   "flip_m": TaskConfig(
       name="Flip M",
       task_slug="flip_m",            # data/problems/flip_m(.pddl | /)
       prompt=PROMPT_PREFIX
       + (
           "The letter block has the letter 'M' on one of its faces. Your task is to flip "
           "that block once so that the face now on its top ends up facing the camera.\n\n"
       )
       + PROMPT_SUFFIX,
       max_tool_calls=10,             # the model's budget of MCP tool calls
   ),
   ```

   `PROMPT_PREFIX` and `PROMPT_SUFFIX` frame every task (the robot's role, how pixel coordinates
   work, how to end the episode); the middle is what the model is asked to do, and it should say
   in words what the problem's PDDL goal checks: a run is scored by the package's goal classifier,
   so a prompt that asks for more or less than the goal scores wrongly. An optional
   `glyph_library` field names the asset library the letter and digit blocks are drawn from,
   `train_blocks` or `train_blocks_large` (ToyBlocks's `GLYPH_LIBRARIES`); leave it out for the
   default, `train_blocks_large`.

3. **Build and run it.**

   ```bash
   agentic-robotics generate-env --task flip_m
   agentic-robotics human --task flip_m --backend oracle       # try it yourself first
   agentic-robotics page --task flip_m --backend oracle        # then watch the model try, and interject
   ```

   `generate-env` builds one package per variant, so a task with many variants takes a while;
   `page` serves the episode with the chat page around it (`episode` runs it headless).

   `generate-env` reports reset states with unreachable or overlapping blocks; adjust the
   problem's ranges if many are flagged.

## ManiFlow skills

The `maniflow` backend runs a trained ManiFlow policy instead of the scripted skills. It needs the
`maniflow` extra, which builds the `maniflow-tb` and `molmo2` submodules, and a checkpoint
directory in the layout a training run writes (`checkpoints/steps_N_model.safetensors`,
`config.yaml`, `stats.json`; see [Imitation learning](imitation_learning.md)). The released
checkpoint, [allenai/maniflow-tb](https://huggingface.co/allenai/maniflow-tb), has that layout:

```bash
git submodule update --init maniflow-tb molmo2
uv pip install -e ".[dev,isaac,torch-cu128,vecgen,maniflow,agentic]"
hf download allenai/maniflow-tb --local-dir checkpoints/maniflow-tb
```

The adapter's checkpoint table (`maniflow_config.py`, `MANIFLOW_CONFIGS`) names each checkpoint
directory relative to `$MANIFLOW_CHECKPOINT_ROOT` (default: `checkpoints/` under the working
directory); `maniflow-tb` is the entry for the released checkpoint. Start the policy server in its
own shell, then run the episode against it:

```bash
agentic-robotics serve --maniflow maniflow-tb        # the policy server, on port 8000; leave it running

# In a second terminal. A new shell starts without this one's environment, so restore it:
cd ToyBlocks && source .venv/bin/activate
export OMNI_KIT_ACCEPT_EULA=YES                      # and OPENROUTER_API_KEY, unless it is in ~/.openrouter_key
agentic-robotics page --task spell_hen_patterned_0_feasible_0 --backend maniflow --maniflow maniflow-tb
```

Without `--maniflow`, both use the experiment file's `maniflow` key; without `--backend`, the
episode uses its `skill_backend`. A missing checkpoint file is reported by name before Isaac starts.

## Experiments and further reading

What a run holds fixed -- backend, model, checkpoint, camera, seed, the scripted skills'
parameters -- comes from an experiment file,
`agentic_robotics/src/agentic_robotics/adapters/toyblocks/experiments/<name>.toml`, chosen with
`--experiment <name>` (`default.toml` otherwise). `agentic-robotics --help` lists every mode and
flag. The submodule's README covers the evaluation suites and the Search & Spell experiments.

---- FILE: docs_source_user_guide_workflows_data_generation.md ----

# Automatic Data Generation

The data generation pipeline turns a symbolic PDDL description of a task into a large,
automatically-labelled dataset of robot demonstrations in simulation. You describe what should be
true at the end of the task, for example "the red block is on the green block", and the
pipeline does the rest: it samples scenes in which the task can start, plans every
episode with a symbolic planner, carries the plan out with motion-planned skills on
hundreds of simulated environments at once, checks every step against the simulator,
and records the demonstrations in LeRobot format, including sensor observations, ready for training.

Because tasks are written as goals rather than as simulation code, the same pipeline
produces data for stacking, flipping, rotating, pick-and-place and other task
families, and it runs the same way on a single GPU or across every GPU of one machine.

## Design goals for the datagen system

- **Declarative tasks.** A task is a Planning Domain Definition Language (PDDL)
  problem: a set of initial facts and a goal over predicates such as `on`, `on_table`
  and `ori_of`. Task generators in `scripts/task_gen/` produce whole task families, and
  the simulation environment and its reset states are generated from the PDDL
  automatically. Adding a task means writing a goal, not simulation code.
- **Correct by construction.** The FF symbolic planner plans each environment from its
  own symbolic state. After every skill, the skill's effects are checked against the
  live simulation. If a check fails, the environment returns to its pre-skill snapshot
  and retries; once the retries run out, the planner re-plans from the current state.
  An episode is labelled successful only if the PDDL goal holds in the final state, and
  failed episodes are stored in a separate failure split instead of being mixed in.
- **Scalable, with CPU and GPU parallelization.** One Isaac process per GPU runs hundreds of
  environments at once (eg. 256 per GPU in measured runs). Skills run as batched tensor
  operations on a pool of cuRobo inverse-kinematics and trajectory-optimization solvers,
  with a separate collision world per environment, while each environment's FF plan
  takes milliseconds on the CPU. Finished environments stream straight into their next
  episode, and several problems share one process (8 by default) so the Isaac start-up
  cost is paid once per group.
- **Diverse tasks on simple assets.** Scene randomization covers block size, table height, friction,
  distractor blocks and block placement, and the robot's starting pose can be randomized
  (always collision-free).
- **Rendering, with visuals separate from physics.** Execution records the
  trajectory states; the camera videos come from a separate rendering stage. It replays
  each recorded episode by placing the robot and objects frame by frame, with no physics
  stepping, and renders it under domain randomization: lighting and sky images, table
  materials, camera poses and field of view, and block letters and colours. This means:
  - one expensive planning-and-physics run can be rendered many times with different
    visuals, for example several copies per episode, or separate train and test letter
    sets, without re-planning;
  - rendering is scheduled separately from data generation: as its own job in the
    pipeline's GPU-slot pool, appended to each execution job, or run again later on the
    stored states;
  - the render settings sampled for each episode are recorded, so evaluation can
    reproduce an episode's look.

  Rendered pixels match the original rendering closely but not exactly: driver and
  scene-version differences remain.
- **Rich, training-ready output.** Episodes are written in LeRobot v3 format. Alongside
  the robot state, camera streams and actions, every frame records the symbolic state,
  the current high-level and low-level action labels, and the goal. A merge and an
  annotation step produce one training dataset.
- **Reproducible and traceable.** Each run pins the git commit, saves its full
  configuration, and writes provenance into the dataset (the commit, checksums of the
  source files, copies of the PDDL files). An interrupted run can be resumed, skipping
  the stages that already finished.
- **One command, one machine.** The orchestrator runs every stage on the machine you
  launch it on, spreading problems over the visible GPUs. The same command works on a
  single-GPU workstation and on a multi-GPU node (see [Running the pipeline locally](datagen/local.md)).

## What can you do with the datagen pipeline?

- **Generate a demonstration dataset for a task family**, such as 3-block stacking,
  flipping, rotating or pick-and-place: pick a generator in `scripts/task_gen/` and run
  `run_datagen_pipeline.py` (see [Full data generation pipeline](#full-data-generation-pipeline)).
- **Generate a single task end to end on one GPU** for debugging, with
  `generate_task_from_pddl.py` followed by `scripts/vecgen/run.py` (see
  [Env generation](datagen/env_generation.md) and
  [Execution](datagen/execution.md)).
- **Randomize the physical scene** (block size, table height, friction, distractors and
  robot start pose); scene randomization is on by default, and `--randomize-robot-init`
  adds the robot start pose.
- **Render a dataset** with new lighting, materials, cameras, and block letters or
  colours, as many times as you like, without re-planning (see
  [Rendering](datagen/render.md)).
- **Generate play data**, where each scene plays a chain of goals with no reset in
  between, with `scripts/datagen/run_playdata_pipeline.py` or
  `scripts/vecgen/run.py --play`.
- **Relabel a policy's failures**: turn the states where a policy failed during
  evaluation into new expert demonstrations, with
  `scripts/datagen/run_tamper_pipeline.py`
  ([TAMPER](https://github.com/allenai/ToyBlocks/blob/main/docs/tamper.md)).
- **Produce training-ready output**: one merged, annotated LeRobot dataset, ready for
  imitation learning and for [evaluation](evaluations.md).

## How to get started

`scripts/datagen/run_datagen_pipeline.py` runs the stages below in order, all on your machine.
Each stage can also be run on its own, as its page (linked under "Datagen Pipeline Steps" below)
shows.

```text
run_datagen_pipeline.py
  ├─ task-gen    scripts/task_gen/*.py           PDDL problems
  ├─ env         generate_task_from_pddl.py      env package + sampled reset states
  ├─ execution   scripts/vecgen/run.py           FF per env -> batched skills -> verify -> record
  ├─ render    (optional, --render-pass)      new visuals from the recorded states
  ├─ merge       merge_datasets.py               one training dataset
  └─ annotate    annotate_target_xy.py           target annotations
```

If you simply want to generate some example datasets with already tested scripts, start from these entry points in the [scripts/datagen folder](https://github.com/allenai/ToyBlocks/tree/main/scripts/datagen):

- [run_datagen_pipeline.py](https://github.com/allenai/ToyBlocks/blob/main/scripts/datagen/run_datagen_pipeline.py): the end-to-end pipeline described on this page; its docstring lists ready-to-run example commands.
- [run_playdata_pipeline.py](https://github.com/allenai/ToyBlocks/blob/main/scripts/datagen/run_playdata_pipeline.py): the same pipeline for play data, where each scene plays a chain of goals without resetting.
- [run_tamper_pipeline.py](https://github.com/allenai/ToyBlocks/blob/main/scripts/datagen/run_tamper_pipeline.py): turns states where a policy failed during evaluation into new expert demonstrations.
- [merge_datasets.py](https://github.com/allenai/ToyBlocks/blob/main/scripts/datagen/merge_datasets.py): merges per-problem LeRobot datasets into one.
- [plot_episode.py](https://github.com/allenai/ToyBlocks/blob/main/scripts/datagen/plot_episode.py): plots every signal of one episode, a quick way to check a generated dataset.



## Full Data Generation Pipeline

The `scripts/datagen/run_datagen_pipeline.py` script orchestrates the entire data generation process end-to-end. It runs every stage locally, one problem per GPU slot (all visible GPUs by default), pins the git commit for reproducibility, and saves a full config JSON alongside the output. How the GPU slots, logs and resume work is described in [Running the pipeline locally](datagen/local.md).

### Datagen Pipeline Steps

1. **[Task generation](datagen/task_generation.md)**: runs a task gen script (default `scripts/task_gen/stack_three.py --train`) to produce randomised PDDL problem files.
2. **[Env generation](datagen/env_generation.md)**: builds one env package per problem and samples its reset states (`generate_task_from_pddl.py`). Skipped when `--vecgen-problems-per-env` > 1 (the default is 8): the execution step then builds one multi-problem package per group itself.
3. **[Execution](datagen/execution.md)**: runs vecgen on each problem or group (`scripts/vecgen/run.py`): FF planning per environment, batched skills, verification, and LeRobot recording.
4. **[Rendering](datagen/render.md)** (optional): renders each problem's episodes as soon as its execution finishes. Each `--render-pass FLAGS.yaml[:N]` is one look, rendered over every episode into its own output directory, and the flag can be repeated. `--render-schedule` places each render either in the shared GPU-slot pool or inside the execution job.
5. **[Merge](datagen/merge.md)**: merges all successful per-problem LeRobot datasets (the rendered ones when the render stage ran) into a single LeRobot training dataset (`merge_datasets.py`).
6. **[Annotate](datagen/annotate.md)**: adds per-frame goal columns to the merged LeRobot dataset (`annotate_target_xy.py`): `goal.action` (the current action as text, e.g. `pick`, `push left`) and `goal.position` (the target object's pixel coordinates in the front camera). It needs camera data, so it is skipped with a warning unless the episodes were rendered or recorded with `--vecgen-record-videos`.


### Basic Usage

```bash
# Full pipeline with the defaults, on every visible GPU
python scripts/datagen/run_datagen_pipeline.py --experiment-id nov05_stack3

# The same, rendered: the camera videos come from the render stage
python scripts/datagen/run_datagen_pipeline.py --experiment-id nov05_stack3 \
    --render-pass src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml

# A small run: 2 problems, 16 episodes each, rendered, outputs under ./outputs
python scripts/datagen/run_datagen_pipeline.py --experiment-id nov05_stack3_small \
    --output-root outputs \
    --render-pass src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml \
    --task-gen-count 2 --env-per-problem 16 --num-envs 16 --exec-num-envs 16 \
    --vecgen-problems-per-env 1

# Another task generator
python scripts/datagen/run_datagen_pipeline.py --experiment-id nov05_rotate \
    --task-gen-script scripts/task_gen/rotate.py --task-gen-count 100

# Interactive mode: choose which steps to run and edit parameters
python scripts/datagen/run_datagen_pipeline.py --experiment-id nov05_stack3 -i

# Quick smoke test (1 problem, 16 envs, no randomization)
python scripts/datagen/run_datagen_pipeline.py --experiment-id nov05_smoketest --smoke-test

# Continue an interrupted run: finished stages are skipped
python scripts/datagen/run_datagen_pipeline.py --experiment-id nov05_stack3 --resume
```

### Key Options

| Flag | Default | Description |
|------|---------|-------------|
| `--experiment-id` | (required) | Name for this experiment run. Used for directory naming. |
| `--interactive` / `-i` | off | Interactively select steps and edit parameters before running. |
| `--resume` | off | Skip stages already marked complete and restart the first unfinished one. |
| `--smoke-test` | off | Override to minimal params: 1 problem, 16 envs, no distractors, no scene randomization. |
| `--task-gen-script` | `scripts/task_gen/stack_three.py --train` | Which task generator to use (`flip.py`, `rotate.py`, `pnp.py`, `stack_three.py`, ...), optionally with its own flags. |
| `--task-gen-count` | 1000 | Number of PDDL problems to generate. |
| `--task-gen-seed` | 6303 | Task generation seed. |
| `--randomize-scene` / `--no-randomize-scene` | on | Block size, table height, and friction randomization. |
| `--randomize-robot-init` | off | Give each reset state a random collision-free arm configuration and gripper state. |
| `--num-distractors` | 0 | Distractor objects per problem (passed to the generator as `--num_distractors`; see [Task generation](datagen/task_generation.md#common-pitfalls)). |
| `--domain-path` | `src/toyblocks/tamp/blocks` | Path to the PDDL domain directory. |
| `--usd-library` | `train_blocks_large` | Glyph asset library that block names resolve against at code generation. |
| `--skip-task-gen`, `--skip-env`, `--skip-execution`, `--skip-merge`, `--skip-annotate` | off | Skip individual steps for re-runs or debugging. |

### Scene Randomization

The pipeline can randomize the following parts of the physical scene:

| Randomization | Flags | Default | Notes |
|---------------|-------|---------|-------|
| Block size | `--block-size-range MIN MAX` | `0.03 0.05` | Ignored with `--no-randomize-scene`. |
| Table height | `--table-height-range MIN MAX` | `-0.05 0.05` | Height offset; ignored with `--no-randomize-scene`. |
| Friction | `--friction-range MIN MAX` | `0.5 0.5` | Ignored with `--no-randomize-scene`. |
| Distractor objects | `--num-distractors N` | `0` | Extra blocks that are not part of the goal. |
| Block placement | `--block-x-range SPEC`, `--block-y-range SPEC` | PDDL value, else `[-0.1, 0.25]` / `[-0.30, 0.30]` | Table-frame window for on-table block spawns; accepts one interval or several disjoint intervals. |
| Robot start pose | `--randomize-robot-init` | off | Collision-free random arm configuration per reset state. |
| Robot start pose ranges | `--robot-init-ee-x-range`, `--robot-init-ee-y-range`, `--robot-init-ee-z-min` | `0.25 0.65`, `-0.35 0.35`, `0.20` | End-effector window in the robot base frame. |
| Gripper start state | `--robot-init-gripper-closed-prob` | `0.5` | Probability a reset state starts with the gripper closed. |

Block size, table height and friction are not sampled per episode: each env package bakes in `--num-scene-profiles` (default 8) profiles drawn from the ranges, so `--num-envs` and `--exec-num-envs` must be multiples of it. How the ranges travel through the PDDL file to the simulator is in [How scene randomization reaches the simulator](datagen/task_generation.md#how-scene-randomization-reaches-the-simulator). Visual randomization (lighting, materials, cameras, block letters and colours) happens at render time; see [Rendering](datagen/render.md).

Scene randomization is on by default, over the ranges above. With `--no-randomize-scene` (and with `--smoke-test`), block size, table height and friction are fixed: block size = 0.04, table height delta = 0, friction = 0.4. To use other ranges:

```bash
python scripts/datagen/run_datagen_pipeline.py \
    --experiment-id nov05_stack3_rand \
    --block-size-range 0.03 0.05 \
    --table-height-range 0.0 0.04 \
    --friction-range 0.1 0.4
```

### Output and GPU Options

| Flag | Default | Description |
|------|---------|-------------|
| `--output-root` | `data` | Root for every dataset the pipeline writes, relative to the working directory (resolved to an absolute path). |
| `--dataset-folder` | `unmerged` | Subfolder of `<output-root>/datasets/` for the per-problem outputs. |
| `--merge-output-dir` | `<output-root>/datasets/merged/train/<experiment-id>` | Where the merged dataset goes. |
| `--local-gpus` | every visible GPU | GPU ids the stages may use, e.g. `--local-gpus 0 1`. |
| `--local-gpu-workers` | 1 | Concurrent problems per GPU. Host RAM is usually the limit; validate videos when raising it. |

See [Running the pipeline locally](datagen/local.md) for how the GPU slots are filled, where logs go,
and what `--resume` deletes.

### Rendering

Execution records state and actions only, and the videos come from the optional render stage.
Turn it on with `--render-pass`:

| Flag | What it does |
|------|--------------|
| `--render-pass FLAGS.yaml[:N]` | Render every episode with this flags YAML, optionally `N` copies of each, into its own output directory. Repeat the flag for more looks. The merge takes them all. |
| `--render-schedule` | `coupled` (default) appends each render to its execution job, holding one slot across both, and with `--local-gpu-workers 2` that is the faster choice. `pipelined` queues each render as its own item in the GPU-slot pool so it can overlap the next execution, at some throughput cost. |

There is no default YAML, so every pass names the look it renders, and the pipeline records that
file in the problem's `render_params.json`. [`src/toyblocks/domain_randomization/flags/render_flags_plain.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_plain.yaml)
is the plain baseline and [`src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml)
adds lighting, material, camera, glyph and colour randomization.

A pipeline render defaults to one copy per episode, the 224 RGB and depth sidecars,
`left_camera` skipped and failure episodes skipped. The `allrand` flags draw HDRI backdrops from
polyhaven (part of the base asset download) and the separately licensed Laval indoor set. See
[HDRI backdrops](https://github.com/allenai/ToyBlocks/blob/main/docs/source/user_guide/workflows/datagen/local.md#hdri-backdrops).
Every render flag is described in [Rendering](datagen/render.md).

### Per-Stage Parameters

Flags that set one stage's options are listed on that stage's page, with the stage flag each
one becomes: [env generation](datagen/env_generation.md#through-the-pipeline),
[execution](datagen/execution.md#through-the-pipeline), [rendering](datagen/render.md),
[merge](datagen/merge.md#flags) and [annotation](datagen/annotate.md#running-it).

### Execution Settings Without a Pipeline Flag

Some execution settings are `scripts/vecgen/run.py` flags that the pipeline does not forward: the
motion profile (`--profile`, default `medium`) and the arm dynamics (`--friction-comp`,
`--arm-joint-friction-scale`, `--arm-armature-scale`). Their defaults are the frictionless,
armature-free arm without friction compensation that the RI training set was generated with, so
a pipeline run always uses them. To change them, run the execution stage by hand; see
[Execution](datagen/execution.md#flags).

A few recording settings are read from environment variables. The pipeline's stages inherit your
shell's environment, so export them before launching. They are listed in
[Execution: Environment variables](datagen/execution.md#environment-variables).


### Datagen Output Structure

If successful, all outputs of the script `scripts/datagen/run_datagen_pipeline.py` will be written
under `<output-root>/datasets/<dataset-folder>/<experiment-id>/` (by default
`data/datasets/unmerged/<experiment-id>/`), containing the following:

```
<experiment-id>/
├── tasks/                    # Generated PDDL problem files
├── envs/                     # Env packages + reset states, one per problem or problem group
├── execution/                # Per-problem LeRobot datasets (success + failure splits)
├── render/                 # Rendered datasets (only with --render-pass), one job_<name> dir per pass
├── local_logs/               # Per-problem logs, only when more than one GPU slot runs at a time
├── .pipeline_state/          # <stage>.done markers read by --resume
└── run_datagen_pipeline_config_<timestamp>.json  # Full reproducibility config
```

The final merged dataset is written to `<output-root>/datasets/merged/train/<experiment-id>/` (or `--merge-output-dir`). Every column it contains is described in [Dataset fields](datagen/dataset_fields.md).

```{toctree}
:hidden:

datagen/task_generation
datagen/env_generation
datagen/execution
datagen/adding_a_skill
datagen/render
datagen/merge
datagen/annotate
datagen/dataset_fields
datagen/local
```

---- FILE: docs_source_user_guide_workflows_datagen_adding_a_skill.md ----

# Adding a skill to vecgen

[Execution](execution.md) can only demonstrate what it has a **skill** for. The FF planner plans
over every action in `src/toyblocks/tamp/blocks/domain.pddl`, but each planned action is carried
out by a vecgen skill: a small Python class that turns "rotate `block_r` clockwise" into joint
targets, runs them on every environment at once, and then checks the result against the
simulation. When FF plans an action that has no skill, the environment gets no program and the
episode is recorded as a failure with reason `"no program"`.

The domain already contains actions that have no skill: `push_to_right` and `push_next_to`.
That is why the pipeline excludes them by default (`--vecgen-exclude-actions`). This page walks
through every place a new skill has to be wired in, from the PDDL action to the annotated
dataset.

The worked reference throughout is the **`rotate`** skill (`src/toyblocks/vecgen/skills/rotate.py`).
It maps one PDDL action to one skill, uses derived facts to keep FF away from rotates it cannot
do, and checks its effect with its own tolerance. Its grasp-and-twist geometry comes from scripted
helpers in `rotate_trajectory.py`, which a new skill does not need. `Pick`
(`src/toyblocks/vecgen/skills/pnp.py`, about 90 lines) is the smallest complete skill, and a good
template for a new one.

## Where it fits

A skill sits in the middle of a chain. Each link is a separate piece of code:

```text
domain.pddl action        FF plans it per environment
  -> symbolic/programs.py  skills_for_action(): PDDL action -> SkillCall(s)
  -> run.py skills dict    SkillCall name -> Skill instance
  -> Skill phases          begin / request / after_phase, resolved by the engine (IK, cuRobo, rows)
  -> Skill.verify()        effect check on the live sim: advance, retry, or re-plan
  -> recorder              action.high_level_* and action.low_level_* columns
  -> annotation            goal.action text and goal.position pixel
```

These are the files you may have to touch, in the order this page covers them:

| Step | File | When |
|---|---|---|
| Skill class | `src/toyblocks/vecgen/skills/<name>.py` | Always. |
| PDDL action | `src/toyblocks/tamp/blocks/domain.pddl` | Unless the action already exists. |
| Predicates | `src/toyblocks/vecgen/symbolic/derived.py`, `predicates.py`, `state.py`, and others | Only for predicates whose truth value must come from the scene. |
| Action to skill | `src/toyblocks/vecgen/symbolic/programs.py` | Always. |
| Registration | `scripts/vecgen/run.py` | Always. |
| Annotation | `src/toyblocks/data_annotation/annotation_utils.py` | When the action should get `goal.action` text and a target pixel. |
| Task generator | `scripts/task_gen/<name>.py` | When you want a family of problems, not one hand-written file. |

There is no plugin registry. Every link above is a hard-coded `if` branch, `dict` or `frozenset`,
so the work is editing these files directly.

## The skill interface

A skill subclasses `Skill` from `src/toyblocks/vecgen/skills/base.py` and lives next to the
existing ones in `src/toyblocks/vecgen/skills/`. The whole base class is this:

```python
class Skill:
    """Base class; subclasses set ``name`` and ``phases`` and implement the hooks."""

    name: str = ""
    phases: list[str] = []
    #: retry from the live state (no snapshot restore), e.g. a flip that moved the block
    retry_from_live: bool = False
    #: phases whose request() is expensive per env (scripted searches): built on a worker
    #: thread while the sim keeps stepping the other envs
    async_phases: frozenset[str] = frozenset()

    def begin(self, ctx: EngineContext, env_ids: Tensor, args: list[tuple[str, ...]]) -> Tensor:
        """Sample per-env parameters for a fresh attempt; return ``ok [B]``."""
        return torch.ones(int(env_ids.numel()), dtype=torch.bool, device=ctx.device)

    def request(self, ctx: EngineContext, phase: str, env_ids: Tensor) -> PhaseRequest:
        raise NotImplementedError

    def skips(self, ctx: EngineContext, phase: str, env: int) -> bool:
        """True when ``phase`` is a no-op for env ``env`` this attempt (e.g. an optional
        sub-step it does not need): the engine moves past it without a segment, so no tick
        is spent or recorded and neither ``request`` nor ``after_phase`` runs for it."""
        return False

    def after_phase(self, ctx: EngineContext, phase: str, env_ids: Tensor) -> None:
        """Bookkeeping once the phase's segment finished (attach/detach, cached poses)."""

    def verify(self, ctx: EngineContext, env_ids: Tensor) -> Tensor:
        """Effect check on the live state after the last phase; ``ok [B]``."""
        return torch.ones(int(env_ids.numel()), dtype=torch.bool, device=ctx.device)

    def hl_name(self) -> str:
        return self.name
```

The engine (`src/toyblocks/vecgen/engine.py`) calls the hooks in this order for each attempt of a
skill:

1. **`begin(ctx, env_ids, args)`** runs once, when an environment starts the skill's first phase.
   `args` holds each environment's `SkillCall` arguments, for example `("block_r", "cw", "o1", "o2")`
   for a rotate. Sample the attempt's parameters here (grasp pose, start pose, place spot), check
   them with IK, and store them for the later phases. Return a `[B]` bool mask. An environment
   whose entry is `False` fails this attempt with reason `"<name> begin: no feasible parameters"`.
2. **`request(ctx, phase, env_ids)`** runs once per phase. It returns one `PhaseRequest` that says
   what that group of environments should do next. The engine resolves it into one
   **segment** per environment, a table of joint targets that is played back one row per tick.
3. **`skips(ctx, phase, env)`** is asked before each phase after the first. Returning `True`
   skips the phase entirely: no segment, no recorded frame, and no `request` or `after_phase`
   call.
4. **`after_phase(ctx, phase, env_ids)`** runs when a phase's segments have finished playing. Use
   it for bookkeeping such as attaching a grasped block to the cuRobo robot model.
5. **`verify(ctx, env_ids)`** runs after the last phase, on the live simulation state, and returns a
   `[B]` bool mask. This is the skill's effect check; see
   [Effect checks, retries and re-planning](#effect-checks-retries-and-re-planning).

`hl_name()` is only a fallback for the recorded high-level action name. Skills planned from a
PDDL action always record that action's name instead (see
[Labels recorded for the dataset](#labels-recorded-for-the-dataset)).

### The batched contract

Skills are written for a batch of environments, not for one:

- `env_ids` is a `[B]` long tensor of environment indices: the group of environments that
  reached the same phase of the same skill on this tick. Every tensor a hook returns is `[B]` (or
  `[B, ...]`) in the same order as `env_ids`. `B` changes from call to call.
- `ctx` is the `EngineContext`. Its scene reads cover **all** `N` environments, so index them with
  `env_ids`: `ctx.block_poses()` is `[N, K, 7]`, `ctx.sim.ee_pose()` is `[N, 7]`,
  `ctx.sim.joint_pos()` is `[N, 7]`, `ctx.sizes` is `[N, K, 3]` (the measured collider edge
  lengths), and `ctx.held` is `[N]` (the index of the block in hand, `-1` for none). Poses are in
  the robot base frame as `[x, y, z, qw, qx, qy, qz]`. `ctx.block_index` maps a PDDL block
  name to its index along the `K` axis.
- `ctx.geo` is the batched cuRobo `Geometry`. `ctx.geo.ik(env_ids, goals, seeds=...)` returns
  `(ok, q, pos_err, rot_err)`, `ctx.geo.update_worlds(...)` refreshes the collision worlds, and
  `ctx.geo.attach(...)` / `ctx.geo.detach(...)` add or remove a held block from the robot model.
- Per-environment state lives in `ctx.params[e]`, a plain dict. One skill instance serves every
  environment and episode, so keep nothing per-environment on `self`. The engine clears
  `ctx.params[e]` when an episode starts and when it re-plans, but **not** between the skills of
  one program, so `begin` should set every key that the later phases read. The keys `_special`,
  `_outcome` and `_attempt` belong to the engine; `_attempt` holds the current attempt number,
  which `flip` uses to escalate its retries.
- Skills never step the simulation or write joint targets themselves. They only read the scene,
  run IK and planning through `ctx.geo`, and return requests.

### Phases and `PhaseRequest`

`phases` is the skill's state machine: a fixed list of phase names that every attempt walks
through in order. Each phase is one `PhaseRequest` (`src/toyblocks/vecgen/skills/base.py`), and
its `kind` says how the engine turns it into a segment:

| `kind` | What the engine does |
|---|---|
| `"plan"` | Plans a collision-free cuRobo trajectory to `goals` (`[B, 7]` end-effector poses). Plan requests from every group are batched into one pool call, which runs on a planner thread while the simulation keeps stepping. |
| `"ik_interp"` | Solves IK for `goals`, then interpolates `ticks` joint rows from the current joints. A goal is accepted when IK succeeds, or when it lands within 5 mm and 0.05 rad. |
| `"rows"` | Plays `rows[i]`, a `[T_i, 7]` joint-target tensor per environment, as given. Use it for scripted motions. |
| `"gripper"` | Holds the current arm target for `ticks` ticks while commanding the gripper `closed` (or to `gripper_target`). |
| `"hold"` | Holds the current arm target for `ticks` ticks. |
| `"policy"` | Hands the environments to a closed-loop runner in `extra["runner"]` until it reports done. No shipped skill uses it. |

The other fields apply to several kinds:

- `label` is the low-level action name recorded on every frame of the segment.
- `hold` adds ticks at the last row. On a `plan` or `rows` request, `settle_tol` ends the hold
  early once every joint is within `settle_tol` radians of the last row, so `hold` becomes a cap.
- `closed` or `gripper_target` on a `plan`, `ik_interp` or `rows` request also commands the
  gripper when the segment starts.
- `exclude` (`[B, K]` bool) removes blocks from the collision world for this phase, for example
  the block being grasped. `pad_fraction` and `no_pad` widen the remaining blocks in XY.
- `ok` (`[B]` bool) marks environments whose request could not be built. They fail the attempt
  with reason `"<name>/<phase>: request not formed"`, without touching the simulation.

A segment holds at most `EngineConfig.segment_capacity` rows (1500 ticks, 60 s). Installing a
longer one raises a `ValueError`, so split long scripted motions over several phases.

Here is how `rotate` declares its phases. A rotate may need two sub-steps (an alignment correction
plus the 90° turn), so it lists the sub-step phases twice:

```python
class Rotate(Skill):
    """``rotate(block, direction, ori, ori2)``."""

    name = "rotate"
    phases = ["open", "start", *_substep_phases(0), *_substep_phases(1)]
    async_phases = frozenset({"descend_0", "descend_1"})
```

Its `begin` looks for a start pose above the block that IK can reach, trying nine small XY
offsets for every environment in the batch at once:

```python
        ctx.geo.update_worlds(ctx.block_poses(), ctx.table_pose(), env_ids=env_ids)
        ok = torch.zeros(b, dtype=torch.bool, device=dev)
        chosen = torch.zeros(b, 7, device=dev)
        for dx, dy in START_OFFSETS:
            todo = ~ok
            if not bool(todo.any()):
                break
            sub = ar[todo]
            goal = torch.zeros(int(sub.numel()), 7, device=dev)
            goal[:, 0] = blk[sub, 0] + dx
            goal[:, 1] = blk[sub, 1] + dy
            goal[:, 2] = blk[sub, 2] + START_HEIGHT
            goal[:, 3:7] = start_q[sub]
            ok_c, _q, perr, rerr = ctx.geo.ik(env_ids[sub], goal, seeds=q_now[sub])
            acc = ok_c | ((perr <= 0.005) & (rerr <= 0.05))
            chosen[sub[acc]] = goal[acc]
            ok[sub[acc]] = True
```

`request` then reads the stored pose back from `ctx.params` and returns one request per phase.
The first two phases open the gripper and plan to the start pose:

```python
        if phase == "open":
            return PhaseRequest("gripper", "init_gripper_open_traj", closed=False, ticks=6)
        if phase == "start":
            # The descend anchors take the gripper's yaw from the CURRENT pose: arriving with the
            # wrist still lagging (~15-40 deg) grasps the block skewed and the fingers twist it.
            goals = torch.stack([ctx.params[e]["start_pose"] for e in envs])
            return PhaseRequest(
                "plan",
                "rotate_start_traj",
                goals=goals,
                hold=WRIST_SETTLE_MAX_TICKS,
                settle_tol=WRIST_SETTLE_TOL,
            )
```

When a block is grasped or released, `after_phase` keeps the cuRobo model and `ctx.held` in step,
so the next plan treats the block as part of the robot:

```python
    def after_phase(self, ctx: EngineContext, phase: str, env_ids: Tensor) -> None:
        kind = phase.rsplit("_", 1)[0]
        if kind == "close":
            envs = [e for e in env_ids.tolist() if ctx.params[e].get("_twist_rows") is not None]
            if not envs:
                return
            ids = torch.tensor(envs, dtype=torch.long, device=ctx.device)
            j = torch.tensor(
                [ctx.params[e]["block"] for e in envs], dtype=torch.long, device=ctx.device
            )
            poses = ctx.block_poses()[ids]
            blk = poses[torch.arange(len(envs), device=ctx.device), j]
            ctx.geo.attach(ids, j, ctx.sim.ee_pose()[ids], blk)
            ctx.held[ids] = j
        elif kind == "release":
            ctx.geo.detach(env_ids)
            ctx.held[env_ids] = -1
```

A rotate that needs only one sub-step skips the second sub-step's phases, so they record no idle
frames:

```python
    def skips(self, ctx: EngineContext, phase: str, env: int) -> bool:
        """Sub-step 1's phases are no-ops for a rotate that was not split (one sub-target):
        skipped, they record no idle frames after the retreat."""
        if phase in ("open", "start"):
            return False
        return len(ctx.params[env]["subs"]) <= int(phase.rsplit("_", 1)[1])
```

### Expensive phases: `async_phases`

A phase whose `request` does slow per-environment work, such as a scripted IK search, can be listed
in `async_phases`. The engine then calls `request` on a worker thread (`--async-workers`, default
4) and keeps stepping the other environments meanwhile. IK called from a worker thread goes to a
separate cuRobo build pool (`--build-slots`). Because several worker threads may run the same
skill at once, `request` must not mutate shared state on `self`. `rotate` builds its descend rows
this way. An exception raised on the worker fails those environments' attempts with reason
`"<name>/<phase>: build error"`.

### How a skill finishes

A skill succeeds for an environment when its last phase finishes, or is skipped, and `verify`
returns `True`. The environment then moves to the next `SkillCall` of its program. An attempt
fails in any of these ways, each with its own recorded reason:

| Failure | Reason string |
|---|---|
| `begin` returned `False` | `<name> begin: no feasible parameters` |
| `PhaseRequest.ok` was `False` | `<name>/<phase>: request not formed` |
| IK failed on an `ik_interp` request | `<name>/<phase>: IK failed (<err> m)` |
| cuRobo found no plan | `<name>/<phase>: plan <status>` |
| A `rows` request had an empty row tensor | `<name>/<phase>: no rows` |
| An async build raised | `<name>/<phase>: build error` |
| `verify` returned `False` | `<name> effect check failed` |

A skill cannot abort halfway through a phase: once a segment is installed, it plays to the end.
To fail early, return `False` from `begin` or mark the environment in a request's `ok` mask.

## Effect checks, retries and re-planning

`verify` is what makes the data [correct by construction](execution.md#correct-by-construction).
It reads the live simulation and checks that the PDDL effect of the action actually holds.
`rotate` checks the block's orientation against the target, with a tighter yaw tolerance (15°)
than the 40° of the shared `ori_of` predicate:

```python
    def verify(self, ctx: EngineContext, env_ids: Tensor) -> Tensor:
        envs = env_ids.tolist()
        j = torch.tensor(
            [ctx.params[e]["block"] for e in envs], dtype=torch.long, device=ctx.device
        )
        idx = torch.tensor([ori_index(ctx.params[e]["ori2"]) for e in envs], device=ctx.device)
        poses = ctx.block_poses()[env_ids]
        q = poses[torch.arange(len(envs), device=ctx.device), j, 3:7]
        target = ORI_QUATERNIONS.to(ctx.device)[idx]
        return check_quat(q, target, VERIFY_YAW_TOL_DEG, AXIS_TOL_DEG)
```

The batched predicate functions in `src/toyblocks/vecgen/symbolic/predicates.py` (`on`,
`on_table`, `clear`, `ori_of`, `next_to`, `on_right` and the others) are the usual building blocks
for a check. Use them, or something stricter, so that a verified skill also satisfies the goal
check at the end of the episode.

Every failure from the table above goes through the engine's `_retry_or_fail`:

1. **Retry.** Up to `--max-attempts` attempts (default 3) per skill. Before each attempt the engine
   snapshots the environment: the simulation state, the held block, its cuRobo attachment, and the
   recorder's frame position. A failed attempt restores that snapshot and **drops the attempt's
   frames from the dataset**, then `begin` runs again with fresh samples.
2. **Retry from the live state.** A skill that sets `retry_from_live = True` (`flip` does, because
   the block has already moved) is retried without a restore, and its failed attempt's frames are
   **kept**.
3. **Re-plan.** Once the attempts run out, the engine drops any held block, reads the symbolic state
   back from the scene, and runs FF again toward the original goal. This happens at most twice per
   episode (`EngineConfig.max_replans`, no CLI flag).
4. **Fail.** If re-planning is exhausted or FF finds no plan, the episode ends as a failure with the
   last reason, and goes to the `blocks_failure` split.

After the last skill of a program, the PDDL goal is checked once more against the scene. An episode
is recorded as successful only if that check passes too; otherwise the reason is
`goal not satisfied: [...]`.

Re-planning reads back only a fixed set of facts (`derive_init_facts` in
`src/toyblocks/vecgen/symbolic/state.py`): `on`, `on_table`, `clear`, `ori_of`, `handempty`,
`gripper_at_init`, plus the derived facts (see [The PDDL side](#the-pddl-side)) and any
`next_to` / `on_right` / `on_left` / `on_front` / `on_back` / `pick_obstructs` fact the problem
declares and that still holds. If your action's effect is some other predicate, a re-plan does not
see it, and there is no hook for that: you have to extend `derive_init_facts` yourself.

## The PDDL side

### Adding the action

If the action is new, add an `(:action ...)` block to `src/toyblocks/tamp/blocks/domain.pddl`. The
`rotate` action takes the gripper, the block, a direction and the two orientations:

```text
  (:action rotate
    :parameters (?g - gripper ?b - block ?d - rot_dir ?o - ori ?o2 - ori ?table - table)
    :precondition (and 
      (initialized)
      (at ?g ?b)
      (handempty ?g)
      (on_table ?b ?table)
      (clear ?b)
      (ori_of ?b ?o)
      (yaw_next ?d ?o ?o2)
      (not (cant_rotate ?b))
      (not (on_table_side ?b ?table))
      (forall (?b2 - block) (not (rotate_obstructs ?b2 ?b ?d)))
```

The rest of its precondition rules out blocks that were pushed against a neighbour, and its effect
swaps the orientation:

```text
    :effect (and 
      (not (ori_of ?b ?o)) 
      (ori_of ?b ?o2)
    )
```

Three conventions are worth keeping:

- **Put the gripper first and the manipulated block second.** FF's argument list is recorded
  verbatim (lowercased) as `action.high_level_args`, and the annotator reads `args[1]` as the target
  object and, for direction actions, `args[2]` as the direction.
- **Require `(initialized)` and `(at ?g ?b)`.** Every manipulation action does. FF's `init` and
  `move_to` actions establish these facts, and vecgen ignores both, so they cost nothing at run
  time.
- **Reuse existing constants and predicates** (`ori_of`, `yaw_next`, `flip_next`, the `dir`
  types) where they fit, since every predicate you add may need Python code, as described next.

To check the action, run FF on a problem whose goal needs it. The vendored FF binary is in the
repository, so this needs no GPU:

```python
from pathlib import Path

from toyblocks.vecgen.symbolic.ff import run_ff
from toyblocks.vecgen.symbolic.pddl import parse_problem, render_problem

problem = parse_problem("src/toyblocks/tamp/blocks/problems/rotate.pddl")
result = run_ff(Path("src/toyblocks/tamp/blocks/domain.pddl"), render_problem(problem))
print(result.ok, [str(a) for a in result.actions])
# True ['(init)', '(move_to robot block_r block_r)', '(rotate robot block_r cw o1 o2 workspace_table)']
```

### Predicates

A predicate that only appears in the domain and is set by action effects or by the `init` action
(like `yaw_next`) needs nothing else. A predicate whose truth value comes from the scene needs
Python code, and where that code goes depends on who reads it:

| The predicate is used in... | Add it to |
|---|---|
| A precondition, true or false depending on the scene before planning | `derived_facts` in `src/toyblocks/vecgen/symbolic/derived.py` |
| A goal | `GEOMETRIC_PREDICATES` and `goal_facts_satisfied` in `src/toyblocks/vecgen/symbolic/predicates.py` (checked by vecgen), **and** `SUPPORTED_GOAL_PREDICATES` in `src/toyblocks/tamp/blocks/goal_predicates.py` with its tensor check in `TENSOR_GOAL_DISPATCH` in `pddl_goal_tensor_conversions.py` (compiled into the env package; the two are asserted equal at import) |
| A problem's `:init`, for which env generation samples poses | `SAMPLERS` in `src/toyblocks/vecgen/sampling/predicates.py` |
| A state that must survive a re-plan | `derive_init_facts` in `src/toyblocks/vecgen/symbolic/state.py` |
| A goal written by a task generator | A `Pred` subclass in `src/toyblocks/task_gen/predicates.py` |

`run.py` calls `assert_goal_supported` on every problem before it starts, so a goal predicate
missing from `GEOMETRIC_PREDICATES` fails immediately rather than at the first episode end.

### Facts derived from the scene

The most useful predicates for a new skill are usually **derived facts**: geometric conditions under
which the skill would fail, computed from the live scene before FF runs, so that FF plans around
them (for example, by moving an obstructing block first) instead of planning an action the skill
cannot carry out. `rotate` has two, `cant_rotate` (the block is out of the rotate workspace or out
of view) and `rotate_obstructs` (a neighbour is too close):

```python
    cant_rot = (
        (xy[..., 0] < ROTATE_X_RANGE[0])
        | (xy[..., 0] > ROTATE_X_RANGE[1])
        | (xy[..., 1] < ROTATE_Y_RANGE[0])
        | (xy[..., 1] > ROTATE_Y_RANGE[1])
        | ~in_view
    )
    for e in range(b):
        for j in range(k):
            if bool(cant_rot[e, j]):
                out[e].append(Fact("cant_rotate", (blocks[j],)))
        for x, j in rot_obs[e].nonzero().tolist():
            for d in ROTATE_DIRS:
                out[e].append(Fact("rotate_obstructs", (blocks[x], blocks[j], d)))
```

`derived_facts` runs for every environment when its episode is assigned, and again on every
re-plan, unless `--no-derived` is passed. Keep its limits and the skill's `begin` in agreement:
every fact that rules out an action here is one less attempt that fails at run time.

## Mapping the action to the skill

`skills_for_action` in `src/toyblocks/vecgen/symbolic/programs.py` turns each action of an FF plan
into one or more `SkillCall`s. It unpacks the action's positional arguments and keeps the ones the
skill needs. `rotate` maps one-to-one:

```python
    if name == "rotate":
        _, b, d, o, o2, _t = a
        return [SkillCall("rotate", (b, d, o, o2))]
```

One action may also expand into several skills. `pnp_table_block`, for example, becomes
`pick(b1)` followed by `place_on(b1 b2 o2)`. The module docstring lists every mapping. Two sets at
the top of the file matter too:

```python
IGNORED = {"init", "move_to", "done", "reach-goal", "stop"}
UNSUPPORTED = {"push_to_right", "push_next_to", "isolate"}
```

If you write a skill for an action in `UNSUPPORTED`, add its branch and remove it from the set.
Play mode (`--play`) uses the set to strip actions from the domain before FF ever sees them.
Datagen mode does not filter the domain with it: when FF plans an action that is in the set, or
that has no branch, `skills_for_action` raises `UnsupportedAction` and the environment gets no
program.

`program_from_plan` copies the PDDL action's name, its full argument list and FF's symbolic state
before the action onto every `SkillCall` the action produces (`hl_name`, `hl_args`, `hl_state`).
These are what the recorder writes, so you do not set them yourself.

## Registering the skill

The engine looks a skill up by the `SkillCall` name. The table is a plain dict in `main()` of
`scripts/vecgen/run.py`, and the same dict is used for play data:

```python
    skills: dict[str, Skill] = {
        "pick": Pick(),
        "place_on": Place("on"),
        "place_table": Place("table"),
        "place_side": Place("side"),
        "flip": Flip(profile=args.profile),
        "rotate": Rotate(),
    }
```

Import your class at the top of `run.py` and add it under the name `skills_for_action` uses. Keep
the dict key and the class's `name` the same: some failure reasons are built from the key and
others from `name`. A `SkillCall` whose name is not in the dict ends its episode with reason
`unsupported skill <name>`.

Evaluation's low-level oracle, `src/toyblocks/eval/ll_oracle.py`, builds its own skill dict for the
commands it parses. Add the skill there only if that oracle should be able to run it.

## Labels recorded for the dataset

Whenever a segment is installed, the engine tells the recorder which action is running:

```python
                self.rec.symbolic(
                    e, cur.hl_name or skill.hl_name(), cur.hl_args or cur.args, req.label, cur.hl_state
                )
```

From then on, every frame of that segment carries these labels:

| Column | Value |
|---|---|
| `action.high_level_action` | The PDDL action name, for example `rotate`. |
| `action.high_level_args` | FF's argument list as JSON, for example `["robot", "block_r", "cw", "o1", "o2", "workspace_table"]`. |
| `action.low_level_action` | The `label` of the phase's `PhaseRequest`, for example `rotate_start_traj`. |
| `action.low_level_args` | `{"ll_action_name": <label>}` as JSON. |
| `observation.state.high_level_state` | FF's symbolic state before the action, one fact per line. |

`pddl_goal`, the episode's goal text, is the problem's `:goal` block as written in the PDDL file;
it does not change from skill to skill. Every recorded episode ends with a 25-tick hold, which is
labelled `done` when the episode succeeded. All columns are described in
[Dataset fields](dataset_fields.md).

The skill only chooses the low-level labels. Reuse the existing ones where a phase means the same
thing, for example `init_gripper_open_traj` for an opening gripper or `gripper_close_traj` for a
grasp, because the annotator keys on them.

## Annotation: goal text and target pixel

[Annotation](annotate.md) turns the labels into the `goal.action` text and the `goal.position`
pixel. Both come from `build_action_goal_str` in
`src/toyblocks/data_annotation/annotation_utils.py`, which looks at a frame's high-level action,
low-level action and high-level arguments, and returns the text and the object to project. For
`rotate` and `reorient`, the verb comes from the action and the direction from `args[2]`:

```python
    elif hl_action in _DIRECTION_VOCABULARY and len(hl_args) > 2:
        parsed = _parse_reorient_direction(hl_action, str(hl_args[2]))
        if parsed is not None:
            verb, direction = parsed
            primary_str = f"{verb} {direction}"
            secondary_str = (
                "gripper_open" if ll_action in _GRIPPER_OPEN_LL_ACTIONS else "move_robot"
            )
        else:
            target = None
```

so every frame of a clockwise rotate of `block_r` reads `rotate cw`, with `goal.position` on
`block_r`.

The annotator knows only the actions it has a branch for. **A frame of any other action gets an
empty `goal.action` and a NaN `goal.position`, and annotation still exits 0.** For a new action,
add:

- an entry in `_HL_ARG_COUNTS` with the action's argument count, so that a frame whose arguments
  fell out of sync with its action name is left unlabelled instead of mislabelled;
- a branch in `build_action_goal_str` that names the action and picks the target object. By default
  the target is `args[1]`. Return a second object as `target_obj2` if the action has one, as the
  push actions do for `goal.position_target`;
- if the target pixel should be taken at the end of the action rather than on each frame (as for a
  place on the table), add the text to `SEGMENT_END_TARGET_LABELS`.

The branches match low-level labels by name, so check every label your skill emits against them.

## A problem to exercise it

The quickest test case is one hand-written problem whose goal can only be reached through the new
action. `src/toyblocks/tamp/blocks/problems/rotate.pddl` is the one for `rotate`: one block at `o1`,
goal `(ori_of block_r o2)`. Build its env package with [env generation](env_generation.md):

```bash
python scripts/generate_task_from_pddl.py \
    --domain_path src/toyblocks/tamp/blocks \
    --pddl src/toyblocks/tamp/blocks/problems/rotate.pddl \
    --output_dir outputs \
    --num_reset_states 32 --num_envs 16 \
    --seed 0 --headless
```

For a whole family of problems, write a generator in `scripts/task_gen/` (see
[Task generation](task_generation.md)). `scripts/task_gen/rotate.py` builds a `ProblemSpec` whose
goal is computed from each sampled initial orientation:

```python
        def rotate_goal(init):
            init_ori = init.arg("ori_of", target_block)
            goal_o = yaw(init_ori, random.choice(directions))
            assert goal_o != init_ori, (
                f"yaw produced a no-op: {init_ori} -> {goal_o}"
            )
            return And(Clear(target_block), OriOf(target_block, goal_o))

        spec.goal = rotate_goal
```

Run it with `--preview` to print one problem without writing anything. Through the pipeline, pass
the script with `--task-gen-script`. If your skill implements `push_to_right` or `push_next_to`,
also override `--vecgen-exclude-actions`, whose default excludes both.

Play data does not pick up a new skill automatically: the balanced goal policy
(`src/toyblocks/playdata/skill_balance.py`, the `--balanced-skills` default of the play pipeline)
only proposes pick-and-place, flip and rotate goals.

## Testing it

### Unit tests, on the CPU

The symbolic layer runs without a GPU. `tests/vecgen/test_symbolic.py` plans a checked-in problem
with FF and checks the resulting program, and the same pattern covers a new mapping:

```python
from pathlib import Path

from toyblocks.vecgen.symbolic.ff import run_ff
from toyblocks.vecgen.symbolic.pddl import parse_problem, render_problem
from toyblocks.vecgen.symbolic.programs import program_from_plan

ROOT = Path(__file__).resolve().parents[2]


def test_rotate_problem_maps_to_one_rotate_skill():
    p = parse_problem(ROOT / "src/toyblocks/tamp/blocks/problems/rotate.pddl")
    res = run_ff(ROOT / "src/toyblocks/tamp/blocks/domain.pddl", render_problem(p))
    assert res.ok, res.error
    prog = program_from_plan(res.actions, p.name, 0, res.states)
    assert [str(s) for s in prog.skills] == ["rotate(block_r, cw, o1, o2)"]
```

`tests/vecgen/test_predicates.py` shows how to test a geometric predicate on hand-built poses. Run
the CPU tests with:

```bash
pytest tests/vecgen/test_symbolic.py tests/vecgen/test_predicates.py
```

A skill class itself cannot be imported without cuRobo: every skill module imports
`toyblocks.vecgen.engine`, which imports the cuRobo-backed `Geometry`. Test the skill in a short
run instead.

### A short run

Run the new env package with a handful of environments, then look at the log and the
`results.json`:

```bash
python scripts/vecgen/run.py \
    --env-path outputs/rotate \
    --pddl src/toyblocks/tamp/blocks/problems/rotate.pddl \
    --num-envs 16 --episodes 32 \
    --record outputs/rotate_rec --mark-complete --headless
```

In the log:

- `FF plan (... ms): rotate(block_r, cw, o1, o2)` is printed once at start-up, from the problem's
  `:init`. If FF cannot plan the problem, the run stops right there with `FF failed`.
- `env N: retry K of <skill call> (<reason>)` and `env N: re-planned from live state after <reason>`
  show the retries and re-plans as they happen.
- `env N episode M: SUCCESS` or `FAILURE <reason>` closes each episode, and the
  `RESULT episodes=... success=...` line and `failure reasons: {...}` sum them up.

`results.json` holds the same failure reasons per episode. A high share of `<name> effect check
failed` points at the skill's motion or at a too-strict `verify`. `begin: no feasible parameters`
points at the start-pose search, or at derived facts that let FF plan actions the skill cannot
reach. `no program` means FF planned an action with no skill, or found no plan at all.

To watch the skill, add `--record-videos --enable_cameras`, which records the scene cameras as well
(see [What a recorded episode contains](execution.md#what-a-recorded-episode-contains)).

### Checking the recorded data

Check that every frame of the new action carries the labels you expect:

```python
import glob

import pandas as pd

cols = ["action.high_level_action", "action.low_level_action"]
files = sorted(glob.glob("outputs/rotate_rec/blocks_success/data/chunk-*/file-*.parquet"))
df = pd.concat(pd.read_parquet(f, columns=cols) for f in files)
print(df.groupby(["action.high_level_action", "action.low_level_action"]).size())
```

Each of your phases' labels should appear under your action. Expect a few `init` frames at the
start of each episode, the `done` hold at the end, and an empty label on each episode's terminal
row. For a whole episode at a glance, `scripts/datagen/plot_episode.py` plots every signal of one
episode. Finally, annotate a
copy of a dataset that has camera data (one recorded with `--record-videos`, or rendered) and check
that `goal.action` is non-empty and `goal.position` is not NaN on the new action's frames, as
described under [Annotation's output](annotate.md#output).

---- FILE: docs_source_user_guide_workflows_datagen_annotate.md ----

# Stage 6: Annotation

A merged dataset records what the robot did, but a vision-language policy also needs to know, at
every frame, *what it is currently trying to do* and *where in the image to look*. Annotation adds
that information. It writes **per-frame goal columns** into a merged dataset, in place: the
current action as text, such as `pick` or `push left`, and the target object's pixel coordinates
in the front camera image.

The goal text comes from the high-level action labels recorded during execution, and the pixel
coordinates come from projecting the recorded object poses through the recorded front camera.

## Where it fits

- **Input:** a merged dataset from [stage 5, merge](merge.md), with recorded front-camera poses
  and intrinsics (normally from [rendering](render.md)).
- **Output:** the same dataset, with the `goal.*` columns added to its parquet files and to
  `meta/info.json`.

The pipeline runs this stage automatically. It is the last stage: after it, the dataset is ready
for training.

## Running it

Point the annotator at the merged dataset and give it a number of parallel workers:

```bash
python src/toyblocks/data_annotation/annotate_target_xy.py \
    data/datasets/merged/train/<experiment-id> -j 64
```

Run the file by its path like this; the pipeline does the same. There is no console script for it.

## Through the pipeline

The pipeline runs annotation automatically unless you pass `--skip-annotate`. Its
`--annotate-num-workers` flag (default `64`) becomes `-j`, and it annotates the merged dataset
in place at `<output-root>/datasets/merged/train/<experiment-id>/` (or `--merge-output-dir`). A
non-zero exit from the annotator fails the run.

The pipeline also skips this stage on its own, with a warning, when the render stage did not run
and `--vecgen-record-videos` was not set. Pixel goals need a camera, and
[execution records none by default](execution.md#what-a-recorded-episode-contains).

## Output

Annotation adds these columns, and declares them in `meta/info.json` as well:

- `goal.action` and `goal.action_secondary`
- `goal.position` and `goal.position_target`
- `goal.position_gripper` and `goal.position_target_gripper`
- `goal.hl_prompt`, when `--hl-prompt` is given

Their shapes and meanings are listed in the
[Annotation Columns table](dataset_fields.md#annotation-columns) of the dataset field reference.

A successful exit does not guarantee the columns are filled in, so check a parquet file after a
run: the `goal.action` strings should be non-empty and `goal.position` should not be all NaN. See
[Common pitfalls](#common-pitfalls) for why.

## Flags

| Flag | Default | Meaning |
|---|---|---|
| `path` (positional) | (required) | The merged dataset root, a directory of datasets (each is annotated), or a bare name resolved under `datasets/unmerged/` **at the repository root**. That is not the pipeline's `data/datasets/unmerged/`, so pass a real path for pipeline output. |
| `--workers`, `-j` | `os.cpu_count()` | The number of parallel workers. |
| `--skip-existing` | off | Skip datasets whose first data parquet already has the goal columns. |
| `--hl-prompt` | `None` | A high-level prompt string, written to a `goal.hl_prompt` column on every row. |
| `--allow-nominal-camera` | off | Annotate even when the dataset records no front-camera pose or intrinsics, falling back to built-in constants. Only correct for a few legacy presets; see [Common pitfalls](#common-pitfalls). |

## Common pitfalls

### Annotation refuses to run without a recorded front camera

By default the annotator **refuses** to run unless the sample parquet has **both**
`observation.camera_pose.camera:front_camera` and
`observation.camera_intrinsics.camera:front_camera`. Either one missing is enough to refuse. The
pipeline treats that non-zero exit as a hard failure of the run.

The two values fall back independently, so a dataset can be half fallen back while still
reporting `recorded`. Catching that case is exactly what this check is for.

`--allow-nominal-camera` bypasses the check, and is correct **only** for the legacy `table` and
`color_only_blocks_table` presets. On any other preset it annotates against the wrong camera, so
render the dataset instead.

### Annotation can succeed and write nothing useful

The only hard requirement is that the parquet has `observation.state.object_pose.*` columns. If
`action.high_level_action` or `action.high_level_args` is missing, the computation returns
immediately with **empty strings and all-NaN positions**. The goal columns are still written,
`info.json` still declares them, and the run still exits 0.

So "annotation succeeded" does not mean "the goals are populated". Check a parquet, as described
under [Output](#output).

### An interrupted annotation can corrupt the dataset

Each parquet file is rewritten in place with a plain `pq.write_table`. There is no temp file, no
atomic rename and no footer check, unlike the merge's own writer. **An interrupted annotation
leaves a truncated data file in the merged dataset.** If a run is interrupted, re-merge before
annotating again, or keep a copy of the merged dataset first.

### The goal columns are not covered by validation or stats

Annotation runs after the merge's LeRobot validation, so that check never sees the `goal.*`
columns, and `meta/stats.json` has no entries for them.

## Next

The dataset is now ready for training and for [evaluation](../evaluations.md).

---- FILE: docs_source_user_guide_workflows_datagen_dataset_fields.md ----

# Recorded Dataset Fields

Datasets are stored in [LeRobot v3 format](https://github.com/huggingface/lerobot). Execution records one row per engine tick (4 physics steps, 0.04 s), so episodes are written at 25 fps. All pose and motion quantities are expressed in the **robot base frame** (local frame) unless stated otherwise. The local frame is defined by the robot's base link position and orientation at the time of recording, with poses transformed via `world_to_local`.

Quaternions use `[qw, qx, qy, qz]` (scalar-first) convention. Euler angles use intrinsic ZYX (roll, pitch, yaw) in radians.

## Episode Metadata

| Field | Shape | Dtype | Description |
|-------|-------|-------|-------------|
| `is_first` | (1,) | bool | True for the first frame of the episode. |
| `is_last` | (1,) | bool | True for the last frame of the episode. |
| `is_episode_successful` | (1,) | bool | Whether the episode achieved the PDDL goal (set on last frame). |
| `pddl_goal` | (1,) | string | The PDDL goal expression for this episode. |
| `task_index` | (1,) | int64 | Index into `meta/tasks.parquet`, which holds the task description text (`"failed"` for failed episodes). |
| `glyph_map` | (1,) | string | JSON `{original_block_name: glyph}` for this episode. `pddl_goal` and the task text use the swapped glyphs, while the pose columns keep the original names; this map reconciles the two. Empty when no glyphs were swapped. |
| `block_variable_map` | (1,) | string | JSON `{rewritten_name: provenance}` covering both glyph blocks and colour cuboids, keyed by the rewritten name used in `pddl_goal` and the task text. Empty when nothing was rewritten. |
| `scene_id` | (1,) | string | Identifier for the scene configuration (table/object layout). |
| `robot_id` | (1,) | string | Identifier for the robot configuration used. |
| `source_problem` | (1,) | string | Name of the PDDL problem directory this episode originates from. |
| `instance_id` | (1,) | int64 | Index of the problem instance within the generated task. |
| `error` | (1,) | string | Error description if the episode failed (empty on success). |

## Robot State Observations

All state observations are in the **robot base frame**.

| Field | Shape | Dtype | Axes | Description |
|-------|-------|-------|------|-------------|
| `observation.state` | (8,) | float32 | `[joint_0..joint_6, gripper]` | Compact state: 7 joint positions (rad) + gripper position. |
| `observation.state.joint_position` | (7,) | float32 | `[joint_0..joint_6]` | Joint positions in radians. |
| `observation.state.joint_velocity` | (7,) | float32 | `[joint_0..joint_6]` | Joint velocities in rad/s. |
| `observation.state.joint_acceleration` | (7,) | float32 | `[joint_0..joint_6]` | Joint accelerations in rad/s². |
| `observation.state.joint_effort` | (7,) | float32 | `[joint_0..joint_6]` | Applied joint torques in Nm. |
| `observation.state.gripper_position` | (1,) | float32 | `[gripper]` | Gripper joint position (raw value from 8th joint). |
| `observation.state.ee_position` | (6,) | float32 | `[x, y, z, roll, pitch, yaw]` | End-effector pose: position (m) + Euler angles (rad), in robot base frame. |
| `observation.state.wrench` | (6,) | float32 | `[fx, fy, fz, tx, ty, tz]` | Wrist wrench: forces (N) and torques (Nm) at the wrist link. |
| `observation.state.current_stiffness` | (13,) | float32 | `[joint_0..joint_12]` | Active PD stiffness gains for all joints (arm + gripper). |
| `observation.state.current_damping` | (13,) | float32 | `[joint_0..joint_12]` | Active PD damping gains for all joints. |
| `observation.state.current_effort_limit` | (13,) | float32 | `[joint_0..joint_12]` | Current effort (torque) limits per joint in Nm. |
| `observation.state.current_velocity_limit` | (13,) | float32 | `[joint_0..joint_12]` | Current velocity limits per joint in rad/s. |
| `observation.state.current_torque` | (13,) | float32 | `[joint_0..joint_12]` | Applied torques for all joints (arm + gripper). |
| `observation.state.high_level_state` | (1,) | string | — | The symbolic (PDDL) state the current high-level action starts from, one ground fact per line, e.g. `(on block_k block_z)`. |

## Robot Link Poses

| Field | Shape | Dtype | Axes | Reference Frame | Description |
|-------|-------|-------|------|-----------------|-------------|
| `robot.poses.<link>` | (7,) | float32 | `[x, y, z, qw, qx, qy, qz]` | Robot base frame | Pose of each robot body, one field per link. `meta/recording_config.json` records the frame as `robot_link_pose_frame: robot_base`. |

## Scene Property Observations

| Field | Shape | Dtype | Axes | Description |
|-------|-------|-------|------|-------------|
| `observation.state.friction_properties` | (3,) | float32 | `[static_friction, dynamic_friction, restitution]` | Physics material properties of the manipulated object. |
| `observation.state.scale_properties` | (3,) | float32 | `[sx, sy, sz]` | Scale factors applied to the manipulated object. |
| `observation.state.cube_scale` | (1,) | float32 | — | Uniform scale factor of the cube (if applicable). |
| `observation.state.table_height_delta` | (1,) | float32 | — | Delta from default table height in metres. |
| `observation.state.table_friction` | (1,) | float32 | — | Friction coefficient of the table surface. |
| `observation.state.profile_id` | (1,) | int64 | — | Scene-profile slot the env was spawned in (see [env generation](env_generation.md)). |

## Object Pose Observations

| Field | Shape | Dtype | Axes | Reference Frame | Description |
|-------|-------|-------|------|-----------------|-------------|
| `observation.state.object_pose.<name>` | (7,) | float32 | `[x, y, z, qw, qx, qy, qz]` | Robot base frame | 6-DoF pose (position in m, quaternion) of each tracked object, transformed to the robot base frame. One field per object in the scene (e.g. `block_r`, `block_red1`). |

## Contact Force Observations

| Field | Shape | Dtype | Axes | Reference Frame | Description |
|-------|-------|-------|------|-----------------|-------------|
| `observation.state.contact_force.<sensor>` | (3,) | float32 | `[fx, fy, fz]` | Robot base frame | Net contact force vector (N) from the named contact sensor, rotated into the robot base frame. Present only when the scene defines contact sensors; the shipped datagen scenes define none. |

## Camera Observations

[Execution records no cameras by default](execution.md#what-a-recorded-episode-contains), so none of these columns exist in an executed dataset unless it was run with `--record-videos`. They normally come from [rendering](render.md).

| Field | Shape | Dtype | Description |
|-------|-------|-------|-------------|
| `observation.images.<cam>` | (H, W, 3) | video (uint8 RGB) | RGB image from the named camera, encoded as AV1 video at dataset fps. The resolution comes from the scene's camera config: 360×640 (H×W) for the shipped scenes' cameras. Camera names carry a `camera:` prefix, e.g. `observation.images.camera:front_camera`. |
| `observation.depth.<cam>` | (H, W, 1) or (H, W, 3) | video (uint16) | Depth map in millimetres (0–4095), divide by 1000 for metres. Stored as 12-bit `gray12le` (1 channel, the default) or as `rg8` (the same value packed into 3-channel 8-bit RGB: R = low byte, G = high byte). Read `video.depth_encoding` (`gray12le_mm` or `rg8_mm`) in the feature's `info` in `meta/info.json` before decoding. Source is Isaac Lab `distance_to_image_plane`. |
| `observation.images.<cam>_<variant>` | (224, 224, 3) | video (uint8 RGB) | Optional RGB sidecar from `--extra_rgb`, e.g. `_224`. |
| `observation.depth.<cam>_<variant>` | varies | video | Optional depth sidecar from `--extra_depth`, e.g. `_g12_224`, `_rg8_224` or `_rg8_55_224`. Has its own resolution, channel count and `video.depth_max_mm`; read them from `meta/info.json`. `rg8_55_224`, the pipeline default, packs depth as `(R << 5) \| G` and saturates at 1023 mm, unlike `rg8`'s `R + (G << 8)`, yet both record `video.depth_encoding: rg8_mm`; tell them apart by the key suffix or by `video.depth_max_mm` (1023 vs 4095). |
| `observation.camera_pose.<cam>` | (7,) | float32 | Camera extrinsic pose `[x, y, z, qw, qx, qy, qz]` in the robot base frame. Constant per episode for a scene-mounted camera; per frame for one mounted on a robot link, such as the gripper camera, which moves with the arm. |
| `observation.camera_intrinsics.<cam>` | (9,) | float32 | Flattened 3×3 camera intrinsic matrix `[fx, s, cx, 0, fy, cy, 0, 0, 1]` (row-major). |

Tactile cameras (if present) follow the same `observation.images.<cam>` convention but may have different resolution.

## Actions

All action fields represent **per-timestep commands** sent to or derived from the controller.

Row *t* holds the observation of state *t* together with the action that drives state *t* to state *t+1*. The last row of an episode is the terminal state: its action columns are zero and `action.is_valid` is `False`. Train on `action.is_valid` rather than testing for zeros, since an all-zero `action.joint_target` is itself a reachable pose.

| Field | Shape | Dtype | Axes | Description |
|-------|-------|-------|------|-------------|
| `action` | (9,) | float32 | `[joint_0..joint_6, gripper, hard_config]` | Primary action vector: `action.relative_joint_target` (7, rad) + `action.gripper_position` + `action.pd_mode` (labelled `hard_config`). This is the field typically consumed by policies. |
| `action.is_valid` | (1,) | bool | — | `False` only on the terminal row, whose action columns are zero. |
| `action.joint_position` | (7,) | float32 | `[joint_0..joint_6]` | Delta joint position: `current_pos - previous_pos` (rad). |
| `action.joint_target` | (7,) | float32 | `[joint_0..joint_6]` | Absolute joint position target commanded by the controller (rad). |
| `action.relative_joint_target` | (7,) | float32 | `[joint_0..joint_6]` | Joint target relative to previous joint position: `target - previous_pos` (rad). |
| `action.ee_target` | (7,) | float32 | `[x, y, z, qw, qx, qy, qz]` | End-effector pose of the commanded joint target (forward kinematics of `action.joint_target`), in robot base frame. |
| `action.relative_ee_target` | (7,) | float32 | `[x, y, z, qw, qx, qy, qz]` | `action.ee_target` relative to the previous end-effector pose: position difference (m) + rotation-difference quaternion. |
| `action.gripper_position` | (1,) | float32 | `[gripper]` | Binarized gripper command: 1.0 = open, 0.0 = closed (threshold at 0.3 by default). |
| `action.gripper_raw` | (1,) | float32 | `[gripper_raw]` | Raw continuous gripper target value before binarization. |
| `action.ee_position` | (6,) | float32 | `[x, y, z, roll, pitch, yaw]` | Delta end-effector pose: position change (m) + Euler angle change (rad), computed from consecutive EE poses in robot base frame. |
| `action.pd_mode` | (1,) | float32 | — | PD controller mode, from the stiffness profile closest to the current joint-0 stiffness: 0.0 for `soft` / `softer`, 1.0 for `stiff` / `medium` / `flip` (see `src/toyblocks/utils/stiffness_profiles.py`). |
| `action.high_level_action` | (1,) | string | — | Name of the current high-level (PDDL) action (e.g. `pick`, `place`, `reorient`). |
| `action.high_level_args` | (1,) | string | — | JSON list of the current high-level action's arguments, e.g. `["robot", "block_w", "right_flip", "o7", "o19", "workspace_table"]`. |
| `action.low_level_action` | (1,) | string | — | Name of the current low-level skill executor. |
| `action.low_level_args` | (1,) | string | — | JSON-encoded arguments of the current low-level executor. |

## Annotation Columns

[Annotation](annotate.md) adds these columns to a merged dataset, in place. They are not written during execution.

| Field | Shape | Dtype | Description |
|-------|-------|-------|-------------|
| `goal.action` | (1,) | string | The current action as text, e.g. `pick`, `place`, `flip right`, `rotate cw`, `push left`. |
| `goal.action_secondary` | (1,) | string | A secondary action string for the same frame. |
| `goal.position` | (2,) | float32 | `(u, v)` pixel coordinates of the current action's target object in the front camera. NaN when the frame has no target. |
| `goal.position_target` | (2,) | float32 | For push/align actions only: pixels of the block being pushed against. NaN otherwise. |
| `goal.position_gripper` | (2,) | float32 | `goal.position` in the gripper-camera image. NaN when the target is outside that image or the dataset has no gripper-camera columns. |
| `goal.position_target_gripper` | (2,) | float32 | `goal.position_target` in the gripper-camera image. |
| `goal.hl_prompt` | (1,) | string | Only with `--hl-prompt`: the given prompt, on every row. |

## Other Recording Paths

Datasets recorded outside vecgen, by evaluation or the `RecordEpisode` wrapper (`src/toyblocks/wrappers/record_episode.py`), can carry extra columns:

- `action.policy`: the raw policy action, sized to the env's action space.
- `action.hl_input_prompt`, `action.hl_model_output`, `action.hl_prev_action` (strings) and `action.hl_done` (bool), when a high-level model chooses the actions.
- `observation.state.object_mass` and `observation.state.table_mass`: live PhysX masses, NaN when the query fails.
- `observation.images.<cam>_hl_overlay`: the camera stream with the high-level prediction drawn on it.

## USD Assets and Provenance

**USD assets are not saved in the dataset.** Object meshes (e.g. letter-shaped toy blocks) and robot models are loaded at simulation time from the `assets/` directory (gitignored, distributed separately) via `OBJECT_ASSET_DIR` and `ROBOT_ASSET_DIR`. The dataset only contains rendered camera images, numeric state, and actions — not the raw 3D geometry.

However, the dataset does include **provenance metadata** under `meta/` that records what was used to generate the data:

| File | Description |
|------|-------------|
| `meta/recording_config.json` | Recording parameters: gripper binarize threshold, gripper type (`robotiq`), open/close commands, joint velocity limits, `record_videos`, and `robot_link_pose_frame`. |
| `meta/provenance.json` | Git commit/remote, the `recording_provenance` dict used at creation, and SHA-256 checksums of every file copied into `meta/extra/`. In a merged dataset it is one aggregate: the git metadata of the merge, `merged_from_n_datasets`, and one `sources[]` entry per source dataset (its path, `problem_name`, `extra_dir` and files). |
| `meta/extra/` | Copies of the files that define the task, each checksummed in `provenance.json`: `domain.pddl`, and from the env package every `problems/*.pddl` (a multi-problem package contributes all of its members) plus `problems.json`, `profiles.json` and `non_sim_state_randomizations.json`. A merged dataset keeps one `domain.pddl` at `meta/extra/domain.pddl` and each source's other copies under `meta/extra/<problem>/`. The directory is created only when something is copied into it. |
| `meta/render_params.json` | Rendered datasets only, before merge: how each split was rendered and every per-episode randomization value; see [Rendering](render.md#output). Merge does not carry it into the merged `meta/`. |

Vecgen forwards the domain and the env package, so a dataset from [execution](execution.md) carries its own PDDL and scene tables. `provenance.json` additionally records the git commit, which pins `domain.pddl` since that file is checked in. What it does **not** pin is anything uncommitted: there is no dirty-checkout flag, and in a merged dataset the git block is the merge's, not each source's. To reproduce such a dataset's simulation environment, you also need:
1. The ToyBlocks repository at the recorded git commit (from `meta/provenance.json`).
2. The `assets/` directory with the matching USD meshes and robot models.
3. The PDDL problem and the env package it was generated from. The problem is named by the `source_problem` column; the dataset does not carry copies.

---- FILE: docs_source_user_guide_workflows_datagen_env_generation.md ----

# Stage 2: Environment generation

A PDDL problem says what the task is, but the simulator needs much more: which blocks to spawn,
how big they are, where they may sit, and what a valid starting scene looks like. Environment
generation fills that gap. It turns one PDDL problem into **a self-contained Isaac Lab env
package plus a set of sampled reset states**, and it is the only stage that writes simulation
code.

`scripts/generate_task_from_pddl.py` does two jobs:

1. **Code generation (always).** It renders the domain's `template_env.py` and
   `template_env_cfg.py` into `<output_dir>/<slug>/` and registers the gym id `<slug>-v0`. The
   *slug* is the task's name, taken from the PDDL file name. The scene randomization tables are
   baked into the generated source at this point.
2. **Reset-state sampling (when `--num_reset_states > 0`).** A *reset state* is one concrete
   starting scene that satisfies the problem's `:init` facts: exact block positions,
   orientations and, optionally, a starting arm pose. Execution starts each episode from one of
   them, so sampling many gives the dataset many different starting scenes. The script launches
   Isaac, creates the generated env with `--num_envs` parallel copies, and runs the `:init`
   predicates through vectorized samplers. Any env whose blocks land outside the front camera's
   view is resampled. The result is pickled to `reset_states.pkl`.

With `--num_reset_states 0` no simulation runs at all: you get code generation plus a
`compileall` pass, which is a quick way to check that a problem produces valid code.

## Where it fits

- **Input:** one PDDL problem file, from [stage 1](task_generation.md) or from the checked-in
  problems.
- **Output:** an env package directory, read by [stage 3, execution](execution.md).

The pipeline runs this stage once per problem when `--vecgen-problems-per-env` is `1`. With its
default of `8`, the pipeline skips this stage and builds one multi-problem package per group of
problems inside the execution jobs instead; see [Through the pipeline](#through-the-pipeline).
Run it by hand to debug a single problem, or to look at the scenes it samples.

## Running it

A typical run generates 32 reset states for the checked-in flip problem, using 16 environments
in parallel:

```bash
python scripts/generate_task_from_pddl.py \
    --domain_path src/toyblocks/tamp/blocks \
    --pddl src/toyblocks/tamp/blocks/problems/flip.pddl \
    --output_dir outputs \
    --num_reset_states 32 --num_envs 16 \
    --seed 0 --headless
```

`--pddl` can be a checked-in problem from `src/toyblocks/tamp/blocks/problems/` or one written
by [stage 1](task_generation.md), for example
`outputs/rotate/tasks/problem_declarative_8_20260602_171400_1234.pddl`. Of the checked-in ones,
`flip.pddl` has cube and table randomizations and `rotate.pddl` has none. The package lands in
`<output_dir>/<slug>/`, where the slug is the file's basename with hyphens replaced by
underscores. In a shell script you can compute it like this:

```bash
task=$(basename "${problem}" .pddl | tr '-' '_')
```

The script parses its arguments with `tyro`, so **every flag accepts both spellings**:
`--num_reset_states` and `--num-reset-states` are the same flag. The Isaac flags inherited from
`BaseArgs` are the one exception; see [Common pitfalls](#common-pitfalls).

To also give each reset state a random, collision-free starting arm pose, add
`--randomize_robot_init`. The three range flags limit where the end effector may start:

```bash
python scripts/generate_task_from_pddl.py \
    --domain_path src/toyblocks/tamp/blocks \
    --pddl src/toyblocks/tamp/blocks/problems/flip.pddl \
    --output_dir outputs --num_reset_states 32 --num_envs 16 \
    --randomize_robot_init \
    --robot_init_ee_x_range 0.25 0.65 --robot_init_ee_y_range -0.35 0.35 \
    --robot_init_ee_z_min 0.20 --seed 0 --headless
```

## Through the pipeline

When `run_datagen_pipeline.py` runs this stage, it sets the flags above from its own:

| Pipeline flag | Default | Becomes | Notes |
|---|---|---|---|
| `--env-per-problem` | `32` | `--num_reset_states` | Despite the name, this is the number of **reset states** per problem, not environments. It must be divisible by `--num-envs`. |
| `--num-envs` | `16` | `--num_envs` | Parallel envs during reset-state sampling. |
| `--num-scene-profiles` | `8` | `--num_scene_profiles` | Baked into the package. |
| `--usd-library` | `train_blocks_large` | `--usd_library` | Glyph asset library. |
| `--block-x-range`, `--block-y-range` | `""` | `--block_x_range`, `--block_y_range` | Only forwarded when set. |
| `--randomize-robot-init` and its range flags | off | `--randomize_robot_init` and the matching `--robot_init_*` flags | Only forwarded with `--randomize-robot-init`. |
| `--num-reset-states` | — | — | **Removed from the pipeline** (the standalone script below still has it). The pipeline always passed `--env-per-problem`, so this is now rejected with an error instead of ignored. |
| `--seed` | `42` | — | Does not reach this stage. The env-generation seed is always `0`, so a different `--seed` regenerates identical reset states. |

The pipeline runs one env-generation process per problem, spread over the GPU slots (see
[Running the pipeline locally](local.md)), and skips any problem whose `reset_states.pkl` already
exists.

With `--vecgen-problems-per-env > 1` (the default is `8`) this stage is skipped. Each execution
job first builds one multi-problem package for its group of problems with
`scripts/vecgen/make_superset_env.py`: the union of the group's blocks, the blocks a problem does
not use parked out of the way, `--env-per-problem` reset states per problem, and a
`problems.json` that lists each problem's PDDL and reset-state range. The package lands in
`envs/problem_grp_<first slug>/`. `--block-x-range` / `--block-y-range` are forwarded and resolved
per problem exactly as on the per-problem path (the flag, else that problem's `;block_x_range` /
`;block_y_range` comment, else the default window). `--seed` behaves differently: it does reach
this path (the package for the group starting at problem *g* is sampled with seed `--seed + g`).
See
[Flags that do not do what their name suggests](local.md#flags-that-do-not-do-what-their-name-suggests).

## Output

The package directory `<output_dir>/<slug>/` contains six files:

| File | Contents |
|---|---|
| `env.py` | The generated env class, with the block names and specs, the randomization dict and `MAX_NON_SIM_STATE_RANDOMIZATIONS` written inline. It starts with `# GENERATED CODE`. |
| `env_cfg.py` | The generated config class, with `scene_preset_id` and `robot_id` overridden if you passed them. |
| `__init__.py` | A `gym.register` call for the id `<slug>-v0`. |
| `non_sim_state_randomizations.json` | The raw randomization tables: per-block `block_sizes`, `table_height` and `friction`. |
| `profiles.json` | The same values seen per scene-profile slot, plus a `codegen_version` provenance stamp. |
| `reset_states.pkl` | The sampled snapshots, with a `profile_ids` array recording which scene profile each was sampled under. Only written when `--num_reset_states > 0`. |

An env package is tied to the code that generated it. `profiles.json` carries a
`codegen_version`, and evaluation **refuses** a package whose version does not match the current
checkout, so regenerate packages after updating the code.

Watch the log for the sampling warnings described under [Common pitfalls](#common-pitfalls).

## Flags

| Flag | Default | Meaning |
|---|---|---|
| `--pddl` | `toyblocks/tamp/blocks/problems/pnp_on_table.pddl` | The problem file. Its basename becomes the task slug. The default no longer works: that file does not exist any more, and the path is missing the leading `src/`. Omitting `--pddl` therefore raises `FileNotFoundError`, so always pass it. |
| `--domain_path` | `src/toyblocks/tamp/blocks` | The folder holding `template/template_env.py` and `template_env_cfg.py`. |
| `--output_dir` | `.` | The directory that will **contain** `<slug>/`. An existing `<slug>/` is deleted first; see [Common pitfalls](#common-pitfalls). |
| `--num_reset_states` | `1` | The number of snapshots to sample. It must be an exact multiple of `--num_envs`. `0` means code generation only. |
| `--num_envs` | `1` | The number of parallel envs used for sampling. |
| `--num_scene_profiles` | `8` | The number of distinct (block size, table height, friction) profiles baked into the package. |
| `--seed`, `-s` | `0` | Seeds both code generation and sampling. |
| `--block_x_range` | `""` | The table-frame x window for blocks spawned on the table, overriding `;block_x_range` in the PDDL. Give one interval, `"[-0.2, 0.58]"`, or several disjoint ones, `"[[-0.2,-0.1],[0.3,0.5]]"`. |
| `--block_y_range` | `""` | The same for y. The sampler defaults are `[-0.1, 0.25]` for x and `[-0.30, 0.30]` for y. |
| `--randomize_robot_init` | off | Give each reset state a random collision-free arm configuration and gripper state. |
| `--robot_init_ee_x_range` | `(0.25, 0.65)` | The end-effector x window, in the robot base frame. |
| `--robot_init_ee_y_range` | `(-0.35, 0.35)` | The end-effector y window. |
| `--robot_init_ee_z_min` | `0.20` | The lowest end-effector height. There is no flag for the upper bound: it is the end-effector height of the home configuration. |
| `--robot_init_candidates` | `32` | The number of poses tried per env before falling back to the home pose. |
| `--robot_init_gripper_closed_prob` | `0.5` | The probability that a reset state starts with the gripper closed. |
| `--scene_preset_id` | `""` (template: `sim2real`) | The scene preset baked into the generated `env_cfg.py`. |
| `--robot_id` | `""` (template: `fr3_robotiq_gripper_sysid`) | The robot baked into the generated `env_cfg.py`. |
| `--usd_library` | `""` (→ `train_blocks_large`) | The glyph asset library that bare block names resolve against. The only other value is `train_blocks`. |
| `--my_verbose` | off | Print per-predicate sampling details. This is a different flag from `--verbose`. |
| `--headless` | off | Inherited from `BaseArgs`; turns the display off. |

Only `--block_x_range` and `--block_y_range` can be overridden here. There is **no**
`--block_size_range`, `--table_height_range` or `--friction_range` flag, because those values
come from the PDDL comment lines written by
[stage 1](task_generation.md#how-scene-randomization-reaches-the-simulator).

## Common pitfalls

### Re-running env generation deletes the previous output

If `<output_dir>/<slug>` already exists, it is removed with `shutil.rmtree` before anything is
written. There is no `--force` flag and no confirmation, so re-running the same problem throws
away the previous `reset_states.pkl`. Copy it elsewhere first if you want to keep it.

### Reset-state and env counts must line up

Two size constraints apply, and they are easy to mix up:

- `--num_reset_states` must be an **exact multiple** of `--num_envs`, enforced by a bare
  `assert`. For example, 8 reset states with 16 envs fails rather than running one partial batch.
- `--num_envs` must be **a multiple of the profile count, or strictly smaller than it**. With the
  default 8 profiles, `1`–`7`, `8`, `16` and `24` are all valid, but `12` and `20` are not. A value
  below the profile count simply spawns only the lower profile slots.

### Changing the profile count does not affect existing packages

`--num_scene_profiles` is a property of the **package**, not of a run. Isaac cannot reconfigure
assets at runtime, so a new value only affects packages generated from then on. Every later stage
also inherits the `--num-envs` constraint from the value baked into the package.

### `--enable-cameras` is silently ignored

`tyro` accepts both spellings, but the Isaac flags inherited from `BaseArgs` are parsed *twice*.
Isaac's own `AppLauncher` runs first, with `parse_known_args`, and declares them with
underscores. So `--enable-cameras` is **silently discarded** and cameras stay off, while
`--enable_cameras` works. The same applies to `--kit_args` and `--rendering_mode`. Always use the
underscore spelling for Isaac flags.

This stage does not need cameras anyway: the front-view visibility check is pure projection
maths, not rendering.

### `--help` takes tens of seconds

`launch_app()` runs at import time, before `tyro` parses anything, so asking for help starts the
simulation app first. Expect a few seconds on a warm cache (much longer on a cold one), a GPU
allocation, and the need for `--headless` on a machine without a display, just to see the usage
listing. The [Flags](#flags) table above is the faster reference.

### Sampling can give up without an error

Each predicate gets at most 200 sampling rounds, and envs that never satisfy it are dropped from
the pending list **with no error**. Separately, envs whose blocks land outside the front camera
view are resampled at most 20 times. After that the script prints
`Warning: N env(s) still have a block outside the front camera view` and keeps those states
anyway. Watch the output for that warning, and for
`[on_table] WARNING: only N% of the spawn window ... is usable`, which fires when less than 20% of
the window is usable.

Not every `:init` predicate is sampled. `at` and `clear` are skipped outright, and a predicate
with no registered sampler is skipped with only a `--my_verbose` message. The samplers that exist
are `on_table`, `on`, `ori_of`, `next_to`, `on_right`, `on_left`, `on_front` and `on_back`.

## Next

Feed the env package to [stage 3, execution](execution.md), which plans and records episodes
starting from these reset states.

---- FILE: docs_source_user_guide_workflows_datagen_execution.md ----

# Stage 3: Execution (vecgen)

Execution is where the demonstrations are actually produced. Given an env package and its reset
states, the robot has to work out how to reach the goal from each starting scene, carry out that
plan in simulation, and have every step recorded as training data.

`scripts/vecgen/run.py` does all of this in **one Isaac process**. It loads the env package,
plans every environment with the FF symbolic planner, runs the planned skills as batched cuRobo
motion plans, checks each skill's effect against the live simulation, and records a LeRobot v3
dataset. Planning happens inside the same process, per environment, so there are no
pre-computed plan pickles and no TAMP checkout to manage.

## Where it fits

- **Input:** an env package with `reset_states.pkl`, from [stage 2](env_generation.md), plus
  the PDDL problem and domain.
- **Output:** a LeRobot dataset split into successful and failed episodes, read by
  [rendering](render.md) or directly by [merge](merge.md).

This stage always runs. By default it records state and actions only; the camera videos come
from rendering, as explained in [What a recorded episode contains](#what-a-recorded-episode-contains).

## Correct by construction

The point of this stage is that every episode it labels successful really is a success. That
guarantee comes from a plan, act and verify loop:

1. FF plans each environment from its own symbolic state.
2. After every skill, that skill's `verify()` runs **against the live simulation**.
3. If the check fails, the environment is restored to its pre-skill snapshot (sim state, held
   block and cuRobo attachment), the retried frames are **dropped from the dataset**, and the
   skill is retried with freshly sampled parameters.
4. After `--max-attempts` failed attempts, FF re-plans from the live state, at most twice.
5. If that also fails, the episode ends as a failure.
6. At the end of the program the PDDL goal facts are checked again, so an episode is labelled
   successful **only if the goal actually holds**.

Failed episodes go to a separate `blocks_failure` split rather than being mixed in or discarded,
so you can study them later.

Each skill and its `verify()` live in `src/toyblocks/vecgen/skills/`. To teach vecgen a new PDDL
action, see [Adding a skill to vecgen](adding_a_skill.md).

## Running it

To run the flip env package from stage 2 and record 32 episodes with 16 environments in
parallel:

```bash
python scripts/vecgen/run.py \
    --env-path outputs/flip \
    --pddl src/toyblocks/tamp/blocks/problems/flip.pddl \
    --domain src/toyblocks/tamp/blocks/domain.pddl \
    --num-envs 16 --episodes 32 \
    --record datasets/flip --mark-complete --headless
```

The two counts mean different things:

- `--num-envs` is **concurrency**: how many environments run side by side on the GPU.
- `--episodes` is the **total number of episodes to finish**, successes and failures together.

When an environment finishes an episode, it is immediately reset onto the next reset state of
its own scene-profile slot and starts planning again. Environments keep recycling like this until
the episode target is met.

`--record` names the output directory, and creates `blocks_success/` and `blocks_failure/`
underneath it. `--mark-complete` writes a summary and a completion marker when the run finishes
cleanly; see [Output](#output).

## Through the pipeline

When `run_datagen_pipeline.py` runs this stage, it sets `run.py`'s flags from its own:

| Pipeline flag | Default | Becomes | Notes |
|---|---|---|---|
| `--exec-num-envs` | `128` | `--num-envs` | Must be a multiple of `--num-scene-profiles`. |
| `--vecgen-episodes` | `--env-per-problem` | `--episodes` | Episodes to run. Left unset, a multi-problem job runs one episode per reset state across the group (`members x --env-per-problem`) and a single-problem job runs `--env-per-problem`. Set it explicitly and that count is used on either path — it used to be silently replaced on the multi-problem path, which is the default. |
| `--seed` | `42` | `--seed` | |
| `--vecgen-exclude-actions` | `push_to_right,push_next_to` | `--exclude-actions` | Domain actions FF may never plan, also when re-planning. |
| `--vecgen-pool-slots` | `32` | `--pool-slots` | cuRobo planner pool slots per process. |
| `--vecgen-record-videos` | off | `--record-videos --enable_cameras` | Normally videos come from [rendering](render.md); this cannot be combined with a `--render-pass`. |
| `--vecgen-problems-per-env` | `8` | — | The number of problems sharing one multi-problem env package and process. Above 1 the env stage is skipped: each execution job builds its group's package with `scripts/vecgen/make_superset_env.py` (unless it already exists) and then streams every episode of the group through one `run.py` process, which reads the problems from `problems.json` instead of `--pddl`. |

The pipeline always passes `--record <base>/execution/<slug> --mark-complete --headless`, where
`<slug>` is the problem's slug, or `problem_grp_<first slug>` for a group. It skips any problem
whose `.execution_complete` marker already exists. Each problem (or group) is one job in the
pipeline's GPU-slot pool; see [Running the pipeline locally](local.md).

The pipeline does **not** forward `--profile`, `--max-attempts`, `--friction-comp`,
`--arm-joint-friction-scale` or `--arm-armature-scale`, so a pipeline run always uses their
defaults (see [Flags](#flags)). To change them, run `run.py` by hand.

## Environment variables

A few recording settings have no flag at all and are read from environment variables. The
pipeline's stages inherit your shell's environment, so export them before launching, or set them
on the `run.py` command line:

```bash
TMP3_RECORDER_INFLIGHT_GB=8 python scripts/datagen/run_datagen_pipeline.py --experiment-id ...
```

| Variable | Default | Effect |
|---|---|---|
| `TMP3_RECORDER_INFLIGHT_GB` | 4 GiB or a quarter of RAM, whichever is smaller | How much un-encoded video may be queued before recording pauses the simulation. Only matters with `--record-videos`. |
| `TMP3_ENCODER_THREADS` | all available cores | The size of the video encoder's thread pool. When more than one GPU slot runs at a time, the pipeline sets it to the cores divided by the number of slots, unless you set it yourself. |

The arm dynamics and the motion profile are flags, not environment variables; see [Flags](#flags).
The flip and rotate skill tuning and the cuRobo collision settings are fixed in code.

## Output

Everything is written under the `--record` directory:

| Path | Contents |
|---|---|
| `<--record>/blocks_success/` | Episodes whose PDDL goal held at the end. |
| `<--record>/blocks_failure/` | Every episode the engine ended as a failure, with the reason. |
| `<--record>/results.json` | Only with `--mark-complete`: per-episode records, failure reasons and wall time. |
| `<--record>/.execution_complete` | Only with `--mark-complete`. The pipeline uses it to decide whether to resume or skip this problem. |
| `<--record>__s001/`, `__s002/` | Shards written when a preempted run resumes; see [Common pitfalls](#common-pitfalls). |

To check a run, look for `RUN_OK` and the `RESULT ...` line in the log, and read the failure
reasons in `results.json`.

## What a recorded episode contains

**By default this stage records no cameras at all.** The env is built with `cameras=False`, so
the camera prims are never spawned, and the recorder leaves out every video feature. There is no
`observation.images.*` and no `observation.depth.*`, and also **no `observation.camera_pose.*` or
`observation.camera_intrinsics.*` columns**. The output is Parquet only.

This keeps execution fast; the pixels normally come from [the render stage](render.md)
instead. It is also why the render's `--camera_base data` cannot work on a dataset this stage
recorded: there is no recorded camera pose to start from, so the pipeline renders with
`--camera_base scene`.

Each row is one engine tick, written at 25 fps. A row holds `is_first` and `is_last`;
`observation.state` and the per-joint position, velocity, acceleration and effort vectors; the
gripper, `ee_position` and wrench; the 13-DoF stiffness, damping, effort-limit, velocity-limit
and torque vectors; `observation.state.object_pose.<name>` for every rigid object;
`observation.state.contact_force.<sensor>` per contact sensor; `robot.poses.<link>` for every
robot body; the scene parameters; the provenance columns (`scene_id`, `robot_id`,
`source_problem`, `instance_id`); `pddl_goal`; the symbolic state; the action block, including
`action.joint_position` and `action.joint_target`; and the high- and low-level action labels.

Every column is described in [Dataset fields](dataset_fields.md).

If you do want video from this stage, `--record-videos` is not enough on its own. Isaac also has
to be told to render, so pass `--enable_cameras` as well:

```bash
python scripts/vecgen/run.py \
    --env-path outputs/flip \
    --pddl src/toyblocks/tamp/blocks/problems/flip.pddl \
    --domain src/toyblocks/tamp/blocks/domain.pddl \
    --num-envs 16 --episodes 32 \
    --record datasets/flip_videos --record-videos --enable_cameras --mark-complete --headless
```

This adds `observation.images.camera:<camera>` and `observation.depth.camera:<camera>` videos
for the front and gripper cameras (640x360) to the dataset.

## Flags

These are the flags you are most likely to need:

| Flag | Default | Meaning |
|---|---|---|
| `--env-path` | (required) | The autogen env package directory. |
| `--pddl` | `None` | The problem file. Omit it only when `<env-path>/problems.json` exists, which is the case for multi-problem streaming. |
| `--domain` | `src/toyblocks/tamp/blocks/domain.pddl` | The domain that FF plans over. |
| `--num-envs` | `16` | The number of environments stepped in lockstep. |
| `--episodes` | `16` | The total number of episodes to finish. |
| `--seed` | `0` | Seeds the engine RNG and the geometry sampler. |
| `--record` | `None` | The output directory for the LeRobot dataset. |
| `--record-videos` | off | **Opt-in.** Also spawn and record the scene cameras. |
| `--mark-complete` | off | Write `results.json` and `.execution_complete` when the run finishes cleanly. |
| `--max-attempts` | `3` | Attempts per skill before the engine gives up on it. |
| `--exclude-actions` | `""` | A comma-separated list of domain actions FF may never plan, for example `reorient,rotate` for pick-and-place-only data. |
| `--init-from-scene` | off | Plan each episode from its live scene rather than from the PDDL `:init`. |
| `--no-derived` | off | Plan from the PDDL `:init` only, without facts derived from the live scene. |
| `--reset-states-once` | off | Start every reset state at most once; the run ends when all of them have run. |
| `--reset-state-ids` | `None` | Run only these reset-state ids, each once. |
| `--cut-tail` | off | Keep every env busy until the episode target is reached, then close the episodes still running as failures. |
| `--profile` | `medium` | The motion and stiffness profile: the arm gains, and the press depth of the scripted flip. |
| `--friction-comp` / `--no-friction-comp` | off | Joint-friction compensation of motion-planned arm targets. |
| `--arm-joint-friction-scale` | `0.0` | Scales the arm's static, dynamic and viscous joint friction in sim. `0` gives a frictionless arm, `1` the robot model's friction. |
| `--arm-armature-scale` | `0.0` | Scales the arm's joint armature in sim. `0` removes it, `1` keeps the robot model's armature. |
| `--no-ff` | off | Disable the target feed-forward. |
| `--max-ticks` | `None` | Stop after this many engine ticks. One tick is 4 physics steps, or 0.04 s. |
| `--play` | off | Collect play data instead: each reset state plays a chain of policy-chosen goals, with no reset between plans. |

The arm-dynamics defaults are the frictionless, armature-free arm without friction compensation
that the Nov 2026 training sets (e.g. RI) were generated with.

Performance knobs (`--async-workers`, `--pool-slots`, `--build-slots`, `--plan-gather-ticks`,
`--plan-gather-min`, `--sync-plans`, `--sync-programs`, `--pool-ik-seeds`,
`--pool-trajopt-seeds`, `--build-ik-seeds`), the play-data options, and debugging aids
(`--log-level`, `--profile-out`) are listed by `python scripts/vecgen/run.py --headless --help`.

## Common pitfalls

### A mistyped flag is ignored, or quietly does something else

`run.py` uses `parse_known_args`, which it needs for Isaac's AppLauncher, so a flag it does not
define is dropped without a word.

There is a subtlety. The parser leaves `allow_abbrev` at its default, so any **unique prefix** of
a real flag is accepted as that flag. `--record-video` is therefore not ignored: it turns video
recording *on*. `--num-env 4` and `--pool-s 8` work too, while an ambiguous prefix such as `--pool` is an error. A typo is either silently ignored or
silently honoured, depending on whether it happens to be a prefix, so double-check flag names
against the table above.

### Some limits cannot be changed from the command line

Three limits live in `EngineConfig` and have no CLI flag: `max_replans = 2`,
`max_episode_ticks = 6000` (the episode is ended with reason `"episode tick limit"`), and
`done_hold_ticks = 25` (the hold recorded after the last skill).

### A run aborts because a scene profile has no reset state

Reset states are bound to scene profiles, not to environments. Environment *i* spawns in slot
`i % MAX_NON_SIM_STATE_RANDOMIZATIONS` and may only run reset states whose block sizes and
friction match that slot. If a spawned slot has **no** compatible reset state, the run aborts
with a `RuntimeError`.

Without `--reset-states-once`, a profile's reset states **cycle**, so asking for more episodes
than there are reset states replays some of them.

### `--mark-complete` does not notice lost videos

It writes `.execution_complete` without consulting the video encoder's defect counter, so a
`--record-videos` run that lost videos can still be marked complete. Only the render tooling
checks `video_defects()`.

### Episodes go missing at merge time because of the directory name

Merge only picks up `base_dir/problem_*/blocks_success`, and the `source_problem` column is taken
from the **deepest** path component starting with `problem_`, falling back to the directory's own
name. For a nested path like `.../problem_grp_flip/problem_0007` that is `problem_0007`, not the
group. Name the `--record` directory accordingly.

An *empty* directory still counts as shard 0, which is why the pipeline creates the problem
directory before launching. `run.py` never scans for shards itself, so a retried attempt
leaves the previous partial shard on disk.

### The process seems to hang after finishing

After the run, `run.py` arms a 15 s timer and calls `os._exit(rc)`, because
`simulation_app.close()` can hang when headless. So the process may take a while to go away.
**Poll the log for `RUN_OK` / `RESULT ...` rather than waiting for the process to exit.**

### `results.json` counts more episodes than the dataset

If FF fails, or the plan uses an action vecgen has no skill for, the episode is counted in
`results.json` as a failure with reason `"no program"`, but it produces **no dataset episode**,
because `start_episode` was never called. Episodes with zero frames are also skipped at save
time. So the two counts can legitimately differ.

## Next

[Render](render.md) the episodes to produce camera videos, then [merge](merge.md) them into
one training dataset.

---- FILE: docs_source_user_guide_workflows_datagen_local.md ----

# Running Pipeline Locally

`scripts/datagen/run_datagen_pipeline.py` runs the whole data generation pipeline on the machine
you launch it on: PDDL problems, env packages, executed episodes, rendered videos and a merged
LeRobot dataset, all on local disk and local GPUs. The same command works on a single-GPU
workstation and on a multi-GPU node. The pipeline spreads problems over every GPU it can see.

This page covers what is specific to running it: asking for renders, choosing GPUs and
concurrency, where outputs and logs go, resuming, and checking the result. For the
stage-by-stage reference, see [Automatic Data Generation](../data_generation.md).

| Stage | How it runs |
|---|---|
| task-gen | one subprocess, on the CPU |
| env | one process per problem, across the GPU slots (skipped with `--vecgen-problems-per-env` > 1, the default) |
| execution | one process per problem or problem group, across the GPU slots |
| render | one render per problem per pass (`--render-pass`), scheduled into the shared GPU-slot pool or inside each execution job |
| merge | one subprocess, on the CPU |
| annotate | one subprocess, on the CPU |

The pipeline needs no network access once the assets are installed. Run it from the root of the
checkout: the stage scripts are called by relative path (`scripts/...`), and the pipeline runs
`git rev-parse HEAD` to pin the commit into the run config for reproducibility.

## Before you start

Follow [the installation instructions](../installation_and_setup_instructions.md). With the
virtual environment active, install the datagen (vecgen) extra and fetch the assets:

```bash
uv pip install -e ".[dev,isaac,torch-cu128,vecgen]"
```

```bash
get-toyblocks-assets --asset-manifest asset_manifest.json
```

Randomized rendering draws HDRI backdrops from the polyhaven pool, installed with the base
assets, and from the separately licensed Laval indoor set. See
[HDRI backdrops](#hdri-backdrops).

Rendering needs real disk. A few problems rendered three times over write several GB of video,
so check free space before a long run rather than discovering it mid-encode.

## A complete run

This generates 4 stacking problems, executes 16 episodes each, renders them with domain
randomization, and merges the result into one LeRobot dataset under `./outputs`:

```bash
python scripts/datagen/run_datagen_pipeline.py \
    --render-pass src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml \
    --experiment-id my_run --output-root outputs \
    --task-gen-script scripts/task_gen/stack_three.py --task-gen-count 4 \
    --env-per-problem 16 --num-envs 16 --exec-num-envs 16 \
    --vecgen-problems-per-env 1
```

The merged dataset is annotated at the end, because the render supplies the camera data that
annotation projects goals into. Drop the `--render-pass` to stop after execution and merge the
raw parquet, which holds state and actions but no video. The pipeline then logs a warning and
skips annotation, which needs video.

With no flags beyond `--experiment-id` the pipeline runs its full default configuration: 1000
`stack_three.py --train` problems, randomized scenes, 32 reset states per problem and 8 problems
per env package at 128 envs. That is a large run, so pass the task-gen and env flags above for
something smaller.

Each stage also runs on its own. See [task generation](task_generation.md),
[env generation](env_generation.md), [execution](execution.md), [rendering](render.md),
[merge](merge.md) and [annotate](annotate.md).

## Rendering locally

Execution records state and actions only, because vecgen spawns no cameras. The videos come from
the render stage, which replays the recorded states with no physics and draws them under the
settings in a flags YAML. See [Rendering](render.md) for what that stage does and every flag it
takes, and the
[YAML reference](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/YAML_REFERENCE.md)
for how to write one.

**`--render-pass FLAGS.yaml[:N]` is how you ask for a render.** Repeat the flag for more looks:

```bash
python scripts/datagen/run_datagen_pipeline.py \
    --render-pass src/toyblocks/domain_randomization/flags/render_flags_plain.yaml \
    --render-pass src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml:3 \
    --experiment-id my_run --output-root outputs
```

Each pass renders **every** source episode under one YAML, into its own
`render/out/job_<name>/` directory named after that YAML. The optional `:N` renders N copies of
each episode within the pass, resampling the randomization for each copy. The merge reads every
`job_*` directory, so the run above ships 1 + 3 = 4 merged episodes per executed episode.

Each pass is a separate renderer invocation rather than extra copies inside one, because the
per-wave settings (dome, skybox, exposure) are global to the scene, so two differently-flagged
looks cannot share a wave. [Render passes](render.md#render-passes) covers this in more detail.

### What the other render flags do

`--render-pass` is the only flag that turns the stage on. Every other `--render-*` flag applies
to **every** pass the run produces, so a run cannot give two passes different cameras, different
sidecars or different schedules.

| Flag | Default | What it does |
|---|---|---|
| `--render-pass FLAGS.yaml[:N]` | none | Adds one pass, optionally `N` copies of each episode. Repeatable. |
| `--render-schedule` | `coupled` | How every render is scheduled against the executions. |
| `--render-skip-cameras` | `left_camera` | Cameras no pass renders. |
| `--render-skip-failure-episodes` | on | Render only successful episodes, in every pass. |
| `--render-extra` | none | Extra `render.py` options for every pass. |

**With no `--render-pass` the stage is off.** The merge then takes the execution data
directly, the dataset holds state and actions with no video, and annotation is skipped with a
warning, because projecting goals into the front camera needs a camera.

**A YAML that is not readable here stops the run before any work**, rather than failing minutes
into Isaac startup once the GPU is already busy. Every pass is checked.

A render cannot be combined with `--vecgen-record-videos`. Recording in-physics video and then
overwriting it pays the slow physics-render cost for frames nothing reads.

### Parity across passes

Passes are symmetric over episodes. Every pass renders the same source episodes, so the merged
dataset holds (sum of the copies across passes) x (source episodes), and every output episode
records the `src_episode_index` it came from. A problem counts as rendered only when **every**
pass has landed on disk, checked by the gate in
[What counts as "rendered"](#what-counts-as-rendered). Without that check a half-finished
problem would contribute 3 copies where 4 were promised and nothing would report it.

Two passes whose YAML file names reduce to the same `job_<name>` would write to the same
directory, so the pipeline keeps the first and warns.

### How renders are scheduled

`--render-schedule` chooses how renders are scheduled against the executions. Both modes run
locally and produce **the same pixels**, because the renderer argv, the staged source layout and
the per-problem output directory name (which seeds the randomization) are identical.
The choice is about throughput and observability.

- `coupled` (the default) appends the render to that problem's execution job, holding one slot
  across both phases. Exec and render are one process span, so they share a log and an exit code.
- `pipelined` queues each render as its own item in the shared GPU-slot pool once that problem's
  execution finalizes, so it can overlap the next execution and gets its own log, timing and
  exit status.

Measured on one RTX 5090 over 4 problems, timing the execution and render window only:

| | 1 slot | 2 slots (`--local-gpu-workers 2`) |
|---|---|---|
| coupled | 921 s | **667 s** |
| pipelined | 906 s | 733 s |

**For throughput, add `--local-gpu-workers 2`**, which is 28% faster than a single coupled slot
and needs none of the scheduler. Pipelining costs nothing at one slot but loses about 10% at
two, because its render-first ordering pairs render against render, two GPU-saturating
processes, whereas the coupled chains naturally pair one problem's execution against another's
render.

Use `pipelined` when you want separable exec and render timings and logs, failure isolation
between the two, or a first finished problem early rather than at the end of a chain.

### Options that matter on one machine

| Flag | Default | Meaning |
|---|---|---|
| `--render-num-envs` | `8` | Envs per render wave, under either schedule. A **floor**, not a preference: the render spawns env *i* at block-size slot *i* % *profiles*, so a value below `--num-scene-profiles` leaves the high slots without an env and **every problem is skipped**. The pipeline refuses that pairing up front. 8 keeps the encoder's memory use survivable beside Isaac. |
| `--render-stall-timeout` | `3600` | SIGKILL the render if it prints nothing for this many seconds. |
| `--render-fail-on-video-defects` | off | Fail a problem whose encoder could not publish every video. Off by default because a failed problem renders whole, and `scripts/render/fast_patch.py` fills video holes afterwards. |

`--render-skip-cameras` and `--render-extra` are described in [Rendering](render.md).

### Render arguments the pipeline pins for you

The pipeline builds its own `render.py` command line, and three of its arguments differ from
`render.py`'s own defaults. They are worth knowing if you are comparing a pipeline render
against one you ran by hand:

| Argument | Pipeline passes | `render.py` default |
|---|---|---|
| `--env_spacing` | `60` | unset (scene default `5.0`) |
| `--camera_base` | `scene` | `data` |
| `--rtx_warmup_frames` | `16` | `1` |

`--num_envs` comes from `--render-num-envs`. `--render-extra` is appended after these and
wins over them, apart from the exceptions noted under
[`--render-extra` needs the `=` form](#troubleshooting).

## HDRI backdrops

The `allrand` flags light each episode with an HDRI backdrop sampled from two pools:
`env_sphere.sets: [polyhaven/all, indoor-2018/all]`. The base asset download includes polyhaven,
and indoor-2018 is installed separately. Each pool is a folder `<root>/<pool>/` holding the
`.hdr` files plus a `dataset.json` that lists the files in each named set (`all`, `rooms`, and
so on). `<root>` is `assets/environments/`, or the directory in `RENDER_HDRI_DIR` when that is
set.

| pool | what | size | license | how to get it |
|---|---|---|---|---|
| `polyhaven` | 299 Poly Haven HDRIs at 2k (`all` = 134 of them) | 1.8 GB | CC0 (credits in its `ATTRIBUTION.md`) | included in `get-toyblocks-assets --asset-manifest asset_manifest.json` |
| `indoor-2018` | Laval Indoor HDR Dataset (Gardner et al. 2017), 2,113 panoramas as 4096x2048 `.hdr` | 44 GB | research / non-commercial | request it from Université Laval ([indoor.hdrdb.com](http://indoor.hdrdb.com)), it is not redistributed |

`get-toyblocks-assets` installs the polyhaven pool under `assets/environments/polyhaven`. For
indoor-2018, convert the panoramas to 4096x2048 Radiance `.hdr` and put them in
`<root>/indoor-2018/` together with a `dataset.json` whose `sets.all` lists the file names:

```json
{"source": "Laval Indoor HDR Dataset 2018", "format": "hdr", "sets": {"all": ["9C4A0003-e05009bcad.hdr", "..."]}}
```

With only polyhaven installed the render still runs. The indoor-2018 bucket resolves to nothing
(`[dr] WARNING skybox bucket resolved 0 textures`), so every backdrop comes from polyhaven and
the images differ from data rendered with both pools. The log line `[render] asset map:` shows
which pools were found.

## Choosing GPUs and how many problems run at once

| Flag | Default | Meaning |
|---|---|---|
| `--local-gpus ID [ID ...]` | every GPU visible to the process | Which GPU ids the stages may use. |
| `--local-gpu-workers N` | `1` | Concurrent problems **per GPU**. `1` is a strict no-op. |

The pipeline builds one *slot* per GPU per worker, so `len(gpus) * workers` problems run at once.
Each slot owns one `CUDA_VISIBLE_DEVICES` value, so every job sees a single GPU. A stage scales
out by spreading problems over more slots, never by giving one problem several GPUs. Listing a
GPU id twice in `--local-gpus` gives it two slots, like `--local-gpu-workers 2` does.

GPU discovery honours an existing `CUDA_VISIBLE_DEVICES`. Failing that it asks `nvidia-smi`, and
if that is unavailable it runs one problem at a time on the default GPU.

A failing problem does not abort the stage. The stage keeps going and reports the failure count
at the end, and the next stage works with the problems that succeeded.

### How much fits

Measured on one RTX 5090 (32,607 MiB) at `--render-num-envs 8`:

| | peak VRAM | peak GPU util | mean util while busy |
|---|---|---|---|
| render | 7,673 MiB | 76% | — |
| vecgen execution | 5,198 MiB | 88% | 61% |

Two concurrent processes fit comfortably on a 32 GiB card and one does not saturate it, so
`--local-gpu-workers 2` is usually free throughput. Host RAM and disk, not VRAM, are what bind
first, so validate the videos afterwards (see [Troubleshooting](#troubleshooting)).

## Logs

With a single slot, every job's output is streamed to your console. With more than one slot, each
problem's output goes to its own log file instead, because concurrent Isaac Sim logs are
unreadable interleaved:

```text
<base>/local_logs/env/<slug>.log
<base>/local_logs/execution/<slug>.log
<base>/local_logs/render/<slug>.log
```

The pipeline logs the directory when it does this, and a `FAILED <stage>: <slug> (see ...)` line
names the log of each problem that failed. `[sched] <stage> start|end <slug> slot=... t=...` lines
record when each job ran, which is how per-stage timings are measured. The pipeline's own log goes
to the console only, so pipe it through `tee` if you want to keep it.

## Outputs

| Flag | Default | Meaning |
|---|---|---|
| `--output-root` | `data` | Root for every dataset the pipeline writes. A relative path is taken from the working directory and resolved to an absolute one. |
| `--dataset-folder` | `unmerged` | Subfolder of `<output-root>/datasets/` for the per-problem outputs. |
| `--merge-output-dir` | `<output-root>/datasets/merged/train/<experiment-id>` | Where the merged dataset goes. |

Everything else lands under `<base>` = `<output-root>/datasets/<dataset-folder>/<experiment-id>/`:

```text
<experiment-id>/
├── tasks/              # generated PDDL problem files
├── envs/               # env packages + reset states, one per problem or problem_grp_<slug>
├── execution/          # per-problem LeRobot datasets (blocks_success + blocks_failure)
├── render/
│   ├── src/            # per-problem staging links the renders read from
│   └── out/            # one job_<name> directory per render pass, named after its flags YAML
├── local_logs/         # per-problem logs, only when >1 slot runs at a time
├── .pipeline_state/    # <stage>.done markers that --resume reads
└── run_datagen_pipeline_config_<timestamp>.json
```

A pass run with [`render_flags_plain.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_plain.yaml) lands in `render/out/job_plain`, and one run with
[`render_flags_allrand_texcache.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache.yaml) lands in `render/out/job_allrand_texcache`. The merged
dataset gets a copy of the run config and a plot of its first episode, `episode_0.png`.

## What counts as "rendered"

Once the render stage is marked complete, **merge reads only `render/out/job_*`**. A problem
that executed but was never rendered would simply vanish from the merged dataset. To stop that
being silent, a post-stage sweep classifies every problem on disk into three states:

| State | Meaning | Retried? |
|---|---|---|
| `RENDER_SHIPPED` | finalized under `blocks_success` **and** merge can read it (`info.json` present) | no, it is done |
| `RENDER_UNRENDERABLE` | finalized, but it can never ship: it declared itself empty, recorded zero episodes, or finalized with only a `blocks_failure` split | no, it is permanent, and failing on it would wedge every later run |
| `RENDER_ABSENT` | not finalized, or finalized without a readable dataset | yes, the run exits non-zero and a later run or `--resume` finishes it |

Two of these are worth understanding. `completed: true` in `render_params.json` means *terminal*,
not *has data*. And a problem whose episodes all failed finalizes with `blocks_failure` alone, so
no `blocks_success` is ever created. Re-running cannot change that, because the source has no
successful episodes.

With more than one pass a problem takes the worst state across its passes, so every pass has to
land before that problem ships.

Both schedules report from this sweep rather than from the job list, so it also covers problems
the execution loop skipped and runs with `--skip-execution`. Pass
`--merge-allow-missing-problems` to merge what rendered and drop the rest.

## Flags that do not do what their name suggests

| Flag | What actually happens |
|---|---|
| `--num-reset-states` | **Removed.** It never had an effect, because the env stage passes `--env-per-problem` through as the generator's `--num_reset_states`, so passing it is now an error rather than a silent no-op. Use **`--env-per-problem`** (default `32`). |
| `--env-per-problem` | Despite the name, this is the number of **reset states** per problem, not a number of environments. The environment count is `--num-envs` (sampling) or `--exec-num-envs` (execution). |
| `--num-scene-profiles` | The count is **baked into the env package at codegen time**, so changing it does nothing for a problem whose package already exists. See below. |
| `--seed` | With `--vecgen-problems-per-env 1`, it does not reach env generation: the env stage is hard-wired to `ENV_GEN_SEED = 0`, so re-running with a different `--seed` regenerates **identical reset states** and `--seed` affects execution only. With multi-problem packages (the default), the package for the group starting at problem *g* is sampled with `--seed + g`, so `--seed` changes the reset states too. |
| `--vecgen-episodes` | Only used with `--vecgen-problems-per-env 1`. A multi-problem job runs `--env-per-problem` episodes per problem in its group. |

The env-count constraint is "a multiple of the profile count, **or** strictly smaller than it".
`--num-envs 4` against 8 profiles is legal and spawns only the low slots. It is not "must be a
multiple".

With `--vecgen-problems-per-env > 1` the env stage is **switched off entirely**, because the
execution jobs build the multi-problem packages themselves with
`scripts/vecgen/make_superset_env.py`.

Env generation also **skips any problem whose `reset_states.pkl` already exists**, and a
multi-problem job skips building a package whose `problems.json` exists. That is what makes
re-running cheap, and what makes a stale env package silently survive a parameter change.
Delete the problem's env directory, or use a fresh `--experiment-id`, when you change env-stage
parameters. This applies to `--num-scene-profiles` in particular: the profile count is a property
of the package, not of the run, so re-running an existing experiment with a new count keeps the
old bake.

## Resuming

`--resume` continues a previous run of the same `--experiment-id`. Stages already marked complete
in `<base>/.pipeline_state/` are skipped, and the first unfinished stage is rerun **from scratch,
deleting its outputs** first. It is a no-op if the experiment directory does not exist.

What that deletes matters for long runs. If the execution stage was interrupted, `--resume`
deletes `execution/` and `render/`, including the problems that had already finished. The
render stage is the exception: it deletes nothing, and `render.py --resume` renders only the
problems not yet completed, pass by pass. A run interrupted after its executions finalized
therefore resumes straight into `render` instead of silently merging raw parquet.

A stage is marked complete when it finishes, even if some of its problems failed, so `--resume`
does not retry failed problems. To keep the finished problems and run only the missing or failed
ones, rerun the same command **without** `--resume` and with `--skip-task-gen`, otherwise task
generation writes a fresh batch of problems next to the old ones. Each stage then skips the
problems it already has.

## Verify the output

**Metadata cannot see a broken render.** A dataset can carry `completed: true` and still contain
videos no decoder will open. A host-RAM OOM mid-encode produces `moov atom not found` mp4s behind
a perfectly healthy-looking marker. Validate the pixels after any run above one worker, once per
pass:

```bash
python scripts/render/validate_dataset_videos.py <base>/render/out/job_<name> --frames
```

`--frames` is what decodes the videos and compares their frame counts to the episode lengths.
Without it only the structural check runs, which catches an unopenable file but passes a short
one.

To confirm that a `:N` suffix genuinely multiplied, count episodes, frames and distinct video
files, never bytes. Merge hardlinks videos into the merged tree, so `du` of the merged directory
is meaningless, and different random draws compress differently. See [Rendering](render.md).

## Troubleshooting

### Rendering segfaults at startup on some GPU and driver combinations

On an RTX 5090 with driver 595.99.02, every local render died about 7 s into Isaac startup with
a SIGSEGV in `librtx.scenedb.plugin.so`, while env generation and execution ran fine on the same
GPU. This is an Isaac Sim 5.1 RTX-renderer problem, not a ToyBlocks one. Check your machine with:

```bash
python -c "from isaaclab.app import AppLauncher; AppLauncher(headless=True, enable_cameras=True)"
```

If that crashes, the machine cannot render. Run the pipeline without a render pass and render the
executed episodes on a machine that can (see [Rendering](render.md)). The same crash affects
`--vecgen-record-videos` and eval video capture. Kit logs are under
`.venv/lib/python3.11/site-packages/isaacsim/kit/logs/Kit/Isaac-Sim/5.1/`.

### Harmless PhysX errors

Some otherwise clean runs print
`PxDirectGPUAPI::getRigidDynamicData(): not allowed while simulation is running`. The episodes
still succeed, so ignore it.

### Isaac hangs after it finishes

`render.py` prints `all jobs done` and then hangs in Isaac teardown, observed holding a GPU for
53 minutes after finalizing all 16 episodes. Every pipeline render therefore runs through
`scripts/render/run_local_render.py`, which watches for the marker and kills the process group
after a grace period. **Never key completion on an exit code** here. Key it on the log.

### Host RAM and disk, not VRAM, are the limits

VRAM is not the binding constraint when raising `--local-gpu-workers`. Host RAM is, and a
host-RAM OOM mid-encode corrupts videos behind a `completed: true` marker. Raise the worker count
only if you validate the output afterwards.

### A job directory from an earlier run is merged again

The merge globs every `job_*` directory under `render/out/`, not only the passes this command
asked for. Re-running an experiment with fewer passes therefore still ships the older pass, and
the merged dataset stays larger than the command says. Delete the job directory you no longer
want, or use a fresh `--experiment-id`.

### Concurrent slots share Isaac's caches

The pipeline sets `KIT_CACHE_ROOT`, `KIT_LOG_DIR` and `OMNI_USER_CONFIG_DIR` per slot, but the
installed Isaac Sim **does not read any of them**. Concurrent slots still share `~/.cache/ov`,
`~/.local/share/ov` and `~/.nvidia-omniverse`. The one per-slot variable that does take effect is
`TMP3_ENCODER_THREADS`, which stops N processes each sizing an encode pool from the whole CPU set.

### `--camera_base data` does nothing here

It tells the renderer to base each static camera on the pose the *dataset* records. The execution
stage records no camera pose at all, because vecgen is parquet-only, so there is never a recorded
pose to base on. `render.py` detects this, warns loudly, and falls back to `--camera_base scene`.
The pipeline passes `scene` explicitly and drops a `data` arriving through `--render-extra`. Same
outcome, said at argv-build time instead of minutes into Kit startup.

### `--render-extra` needs the `=` form

Argparse reads a space-separated value starting with `-` as an option of its own:

```bash
--render-extra="--extra_rgb 224 --extra_depth g12_224 --depth_gop 1000"   # works
--render-extra "--skip_failure_episodes"                                  # rejected
```

It is appended after the pipeline's own arguments, so it beats `--depth_gop`, `--dr_seeding`,
`--env_spacing` and the default sidecars. Three things it cannot change. `--output`,
`--envs_dir`, `--episodes_file`, `--episode_offset` and `--max_episodes` are dropped with a
warning, because they break the pipeline's accounting rather than the render.
`--camera_base data` is dropped for the reason above. And each pass re-applies its own `--flags`
and `-N` afterwards, so an extra carrying either cannot rewrite one pass into another.

## See also

- [Automatic Data Generation](../data_generation.md) for the pipeline overview and every pipeline flag
- [Rendering](render.md) for the render stage, render passes and every render flag
- [Merge](merge.md) for how the rendered passes become one dataset
- [YAML reference](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/YAML_REFERENCE.md) for writing a randomization YAML

---- FILE: docs_source_user_guide_workflows_datagen_merge.md ----

# Stage 5: Merge

By this point the pipeline has produced one small LeRobot dataset per problem, from
[execution](execution.md) or [rendering](render.md). Training wants a single dataset
instead. Merge combines the per-problem datasets into **one training dataset**: it re-indexes
episodes, frames and tasks so they are contiguous, writes the data into parquet files of about
100 MB each, links every source video into place, and writes the merged metadata.

The videos are hardlinked rather than copied, so the merged dataset's videos take no extra disk
space. The flip side of that choice is covered under [Common pitfalls](#common-pitfalls).

The command-line tool is `scripts/datagen/merge_datasets.py`, a thin wrapper around
`toyblocks.vecgen.recording.merge`.

## Where it fits

- **Input:** a root directory containing per-problem datasets, from rendering (the usual
  case) or straight from execution.
- **Output:** one merged LeRobot dataset, read by [annotation](annotate.md) and then by training.

The pipeline always runs this stage. Run it by hand to re-merge after a patch, or to combine
datasets from several runs.

## Running it

Point `--input_dirs` at the directory that contains the `problem_*` directories, and
`--output_dir` at where the merged dataset should go:

```bash
python scripts/datagen/merge_datasets.py \
    --input_dirs data/datasets/unmerged/<experiment-id>/render/out/job_plain \
    --output_dir data/datasets/merged/train/<experiment-id> \
    --cameras all --num_workers 16
```

Pass the **root** that contains the `problem_*` directories, not a single dataset. Discovery
expands each input directory itself, as described in
[How sources are discovered](#how-sources-are-discovered). `--cameras all` keeps every video
stream, and `--num_workers` sets how many processes share the work.

## Through the pipeline

The pipeline exposes this stage through four wrapper flags: `--merge-cameras` (default `all`),
`--merge-num-workers` (default `16`), `--merge-output-dir` and `--merge-allow-missing-problems`.
The last one is not evaluated here but in the render stage; see
[Common pitfalls](#common-pitfalls).

The pipeline merges `<output-root>/datasets/unmerged/<experiment-id>/render/out/job_*` when the
render stage ran, and `.../execution` otherwise. The merged dataset lands in
`<output-root>/datasets/merged/train/<experiment-id>/` unless `--merge-output-dir` says otherwise
(`--output-root` defaults to `data`). The pipeline then copies its run config
(`run_datagen_pipeline_config_<timestamp>.json`) into the merged directory, and writes
`episode_0.png`, a plot of episode 0, next to it.

`run_datagen_pipeline.py` also hardcodes `--union_schema` on every merge invocation, so its own
`--merge-union-schema` flag is never read. `--merge-depth-frames` is read by nothing anywhere:
the merge does no `.npy` depth extraction.

## Output

The output directory holds one LeRobot v3 dataset, with re-indexed `data/` parquet files,
hardlinked videos and merged `meta/`.

To confirm it loads, open it with LeRobot:

```python
from lerobot.datasets.lerobot_dataset import LeRobotDataset
ds = LeRobotDataset(repo_id="local", root=str(merged_dir))
```

`LeRobotDataset(..., episodes=[0])` is the cheap version of this check. Loading a subset of
episodes requires the feature **order** in `info.json` to match the parquet column order, which is
why the merge reorders the non-video features.

Merge does its own LeRobot check when you pass `--validate` or `--union_schema`, but a failed
check does not fail the merge; see [Validation is advisory](#validation-is-advisory).

## How sources are discovered

You give merge a root directory, and it finds the datasets inside on its own. Discovery is
automatic and **keeps successes only**: for the vectorized layout, the merge takes
`base_dir/problem_*/blocks_success` and never `blocks_failure`.

**Merge reads the rendered tree, not the execution tree.** Once the render stage is marked
complete, the pipeline merges **`render/out/job_*` and nothing else**, and the execution tree is
no longer read. A problem that was executed but never rendered therefore vanishes from the
merged dataset. The local flow has [a three-state gate](local.md#what-counts-as-rendered) to
stop that from happening silently.

The glob is deliberately wide, so that every [render pass](render.md#render-passes) is picked up.
That means a `job_*` directory left by an **earlier** run is merged again, whether or not this run
produced it: dropping a `--render-pass` from an otherwise identical command keeps shipping that
pass's copies. The pipeline only warns about it, so clean up old job directories before
re-running.

## What `--union_schema` actually does

Different problems can record slightly different columns, and `--union_schema` controls how the
merged metadata describes them. It does **not** change which columns the merged parquet has:
that union always happens. It changes what `meta/info.json` *declares*, and it turns validation
on.

It can still change parquet *content* at the margin. When a source lacks a column, the merge
fills it with NaN, and the width of that fill is read from the declared features, so declaring
more can change the shape of those filled values.

Two consequences are worth knowing:

- **It decides whether LeRobot validation runs at all.** Without `--validate` and without
  `--union_schema`, the check is skipped, and the log says so.
- **The pipeline always passes it**, as described under [Through the pipeline](#through-the-pipeline).

## Validation is advisory

**A failed LeRobot validation never fails the merge.** The exception is caught, turned into a
warning, and `main()` still returns 0. So a merged dataset that no `LeRobotDataset` can open
still exits successfully, and you should read the warnings.

These are the obstacles to a `LeRobotDataset` load, in the order you are likely to hit them:

1. Without `--union_schema`, columns that some problems have but the template does not declare
   make the cast fail (`column names don't match` / `CastError`).
2. `dataset[0]` needs a working video backend. A torchcodec or ffmpeg failure is reported as
   "validation skipped, video decoding unavailable", not as a data defect.
3. Merged episodes whose clip was never rendered resolve to **zeros** rather than raising an
   error.

Consumers that read the parquet directly, such as HVLA's dataloader or pyarrow, are not affected
by the first one.

### Coverage warnings that do not fail the merge

| Warning | Meaning |
|---|---|
| `INCOMPLETE VIDEO COVERAGE` | A `(dataset, video key)` pair has more than zero but fewer clips than that dataset's `total_episodes`. Those episodes declare a video that is not on disk, **which a path-resolving dataloader reads as zeros**. |
| `present in N/M datasets` | A video key exists in some sources and not others. With `--cameras all`, the merged `info.json` can declare a key that only some problems rendered. |
| stray files | Files in a video directory not named `file-NNN.mp4`, such as an abandoned encode temp file, are reported and skipped. |

All three are log warnings only. Merge also does **not** check that the source and the render have
the same number of episodes.

Two checks *do* fail the run. After the data pass, the merge verifies every `data/` and `meta/`
parquet footer, and it checks that every planned data file and video link exists, with no
unplanned file present.

## Flags

| Flag | Default | Meaning |
|---|---|---|
| `--input_dirs` | (required) | One or more roots holding the datasets to merge. |
| `--output_dir` | (required) | The destination. It is **deleted before writing**; see [Common pitfalls](#common-pitfalls). |
| `--cameras` | `all` | The video feature keys to keep, or `all` / `*` for every video feature any source declares. Naming cameras silently drops all the others, including depth streams and the `--extra_rgb` / `--extra_depth` sidecars. |
| `--num_workers` | `16` | The process-pool size for the data pass. |
| `--max_datasets` | `None` | Merge only the first N source datasets. `--episodes` is a backward-compatible alias. |
| `--union_schema` | off | Declare in `info.json` every non-video column that any source declares, plus columns present in the parquet that no source declared. **Implies `--validate`**, at `--validate_mode`'s default of `fast`. |
| `--validate` | off | Run the LeRobot loadability check after the merge. |
| `--validate_mode` | `fast` | `fast` checks the footers, `LeRobotDataset(episodes=[0])` and `dataset[0]`. `full` checks every frame. |
| `--validate_timeout` | `900` | Seconds before validation is abandoned; `0` means no limit. |

## Common pitfalls

### The output directory is deleted first

The merge `rmtree`s `--output_dir` before it starts, so never point it at anything you want to
keep. It also takes an exclusive lock at `<output_dir>.merge.lock`, a sibling of the output so its
own rmtree cannot remove it. A second merge into the same output refuses to start while the
lock's heartbeat is under 600 s; an older lock is taken over.

### `du` and deleting the source do not behave as expected

Because videos are hardlinked, `du -sh` on the merged directory tells you almost nothing about
real disk use, and deleting the unmerged source does not free that space while the merged tree
exists. Only a merge across filesystems copies. Because the links share inodes with the source,
the merge **raises an error rather than overwrite** an existing destination: overwriting would
write straight through into the source dataset.

This is also why you must never check `-N` multiplication by comparing bytes; see
[Rendering](render.md).

### An unreadable source disappears from the merge

A source dataset with any unreadable data parquet is dropped entirely, with a warning listing its
episode count, before offsets are assigned, so merged indices stay contiguous. The merge still
succeeds and those episodes are silently absent. Search the log for that warning.

### Offsets follow `info.json`, not the parquet footers

`info.json total_frames` decides the offsets. When it disagrees with the actual number of footer
rows, the merge warns ("offsets follow info.json") and continues.

### `--merge-allow-missing-problems` drops episodes permanently

This flag is evaluated in the render stage, not in the merge. Without it, a problem with a
finished execution but no render makes the run return 1 and leaves the render marker unset,
so `--resume` renders that problem. **With** it, the stage is marked complete and those
episodes are gone from the dataset permanently.

## Next

[Annotate](annotate.md) the merged dataset to add the goal columns that vision-language policies
train on.

---- FILE: docs_source_user_guide_workflows_datagen_render.md ----

# Stage 4: Rendering

Execution records what the robot and the blocks did, but it records no camera images. This stage
produces them, by replaying each recorded episode frame by frame: the robot and objects are
placed at their recorded poses, with no physics stepping and no replanning, and each frame is
rendered.

A render is described by a **flags YAML**: how the scene is set up and how it is drawn. The
file is recorded in every problem's `render_params.json`, so a dataset always carries the look
it was made with. There is no default, so the look is always named.

The simplest one is
[`render_flags_plain.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_plain.yaml),
which ships with the repo. Every key in it is fixed, so each episode renders identically:

```yaml
carb_settings: {...}     # RTX path tracing
env_spacing: 500         # how far apart the envs sit
texture_cache: {...}     # where decoded textures are kept
hide_objects: [backdrop] # the backdrop geometry is hidden...
skybox:                  # ...because this sky replaces it
  names: [abandoned_bakery_2k]
  rotation_deg: 0
  intensity: 800
  visible_background: true
```

Render a pass with it:

```bash
--render-pass src/toyblocks/domain_randomization/flags/render_flags_plain.yaml
```

Add sampled sections to that file and the same renderer produces a different look per episode:
see [Domain randomization](#domain-randomization). Ask for more than one look in a run with
[render passes](#render-passes).

The renderer is also a plain script you can run on a single GPU, either on a dataset that has no
images yet or on one that does, replacing them. To run it as part of a pipeline run, see
[Through the pipeline](#through-the-pipeline) and
[Running the pipeline locally](local.md).

## Why the pixels are a separate stage

Keeping rendering apart from execution has several benefits:

- One expensive planning-and-physics run can be rendered many times with different visuals, for
  example N copies per episode or separate train and test letter sets, **without re-planning**.
- Rendering can run later, or on a different GPU, separately from data generation.
- The render settings sampled for each episode are recorded, so evaluation can reproduce an
  episode's look.

Because execution does not spawn cameras by default, rendering is not an optional extra for a
dataset with video: it is **where the video comes from**.

### What rendering does not change

The state and action trajectory is identical across renders, and only the pixels and the camera
columns differ. Rendering cannot fix a bad episode, change what the robot did, or alter the
success labels.

Rendered pixels match an original in-physics rendering closely but not exactly, because
driver and scene-version differences remain. See
[DETERMINISM.md](https://github.com/allenai/ToyBlocks/blob/main/docs/render/DETERMINISM.md)
for exactly what is bit-reproducible and what is not.

## Where it fits

- **Input:** the recorded datasets from [stage 3, execution](execution.md), the env packages
  they were recorded with, and a flags YAML describing the look.
- **Output:** a rendered copy of each dataset, with camera videos, read by [merge](merge.md).

The stage is optional in the pipeline, and `--render-pass` is the only flag that turns it on.
It is the only way to get camera videos without recording them during execution.

## Running it

The quickest way to try it is to render a handful of episodes from an existing dataset on your
own GPU. This is also the best way to preview a flags YAML before committing to a large run:

```bash
python scripts/render/render.py <dataset_dir> \
    --env_file <env_package>/env.py \
    --output <out_dir> \
    --max_episodes 20 --num_envs 8 \
    --flags src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml
```

For an *unmerged* dataset, with one directory per problem, drop `--env_file`. The env is then
matched automatically per problem from `<datasets_dir>/envs/<problem_name>/env.py`. Use
`--envs_dir` when the env packages live somewhere other than next to the data. For a pipeline run
that is the experiment's own `envs/` directory:

```bash
python scripts/render/render.py data/datasets/unmerged/<experiment-id>/execution \
    --envs_dir data/datasets/unmerged/<experiment-id>/envs \
    --output <out_dir> --max_episodes 20 \
    --flags src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache.yaml
```

`render.py` often hangs during Isaac teardown after it finishes. See
[Common pitfalls](#common-pitfalls) for how to run it safely.

## Through the pipeline

Add a `--render-pass` to a pipeline run. Each problem is rendered as soon as its execution
finishes, and the merge then uses the rendered episodes instead of the execution data:

```bash
python scripts/datagen/run_datagen_pipeline.py \
    --render-pass src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml \
    --experiment-id my_run --output-root data \
    --task-gen-script scripts/task_gen/flip.py --task-gen-count 4 \
    --vecgen-problems-per-env 1 --exec-num-envs 8 --vecgen-episodes 16 \
    --local-gpu-workers 2
```

Repeat `--render-pass` for more looks, and give each one a `:N` for several copies of every
episode. See [Render passes](#render-passes) for the rules and
[Running the pipeline locally](local.md#rendering-locally) for how those renders are scheduled.

Every pass names a YAML, and the pipeline records that file in the problem's
`render_params.json`, so a dataset always says which look it was made with. With no other render
flags the pass above renders [`render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml)
once per episode, with `left_camera` skipped, failure episodes skipped, and the 224-px RGB and
`rg8_55_224` depth sidecars
(`--extra_rgb 224 --extra_depth rg8_55_224 --extra_rgb_GOP 2 --rgb_GOP 2`). Override most
`render.py` options with `--render-extra`, in the `=` form:

```bash
--render-extra="--extra_depth g12_224"
```

`--render-schedule` chooses how renders are scheduled against the executions. `coupled`, the
default, runs each render inside that problem's execution job. `pipelined` queues it in the
shared GPU-slot pool so it can overlap the next execution. Both run the same renderer with the
same arguments and produce identical pixels, so this is a throughput and observability choice.
[Running the pipeline locally](local.md#rendering-locally) has the measured difference, and
[what counts as "rendered"](local.md#what-counts-as-rendered) is the gate that decides what the
merge ships.

The `allrand` flags YAMLs draw HDRI backdrops from the `polyhaven` and `indoor-2018` pools.
Where to get each, and what happens when one is missing, is in
[HDRI backdrops](local.md#hdri-backdrops).

The pipeline flags for this stage are:

| Flag | Default | Description |
|------|---------|-------------|
| `--render-pass FLAGS.yaml[:N]` | none | Add one render pass with this flags YAML, optionally `N` copies of every source episode. Repeatable. **The only flag that turns the stage on.** The path must be readable on the machine you launch the run from, and every pass is checked before any work starts. |
| `--render-schedule` | `coupled` | `coupled` runs each render inside the problem's execution job, `pipelined` queues it in the shared GPU-slot pool. Identical pixels either way. |
| `--render-skip-cameras` | `left_camera` | Cameras not to render. Pass the flag with no names to render every camera. |
| `--render-skip-failure-episodes` | on | Render only successful episodes. The merge keeps only those anyway. `--no-render-skip-failure-episodes` renders both splits. |
| `--render-extra` | none | Extra `render.py` options, appended after the pipeline's own defaults so they override them, written as one quoted `=` string. Three exceptions: `--output`, `--envs_dir`, `--episodes_file`, `--episode_offset` and `--max_episodes` are dropped with a warning because the pipeline owns them, `--camera_base data` is dropped because the execution stage records no camera pose, and the pass's own `--flags` and `-N` are re-applied afterwards so an extra cannot rewrite one pass into another. |
| `--render-num-envs` | 8 | Envs per render wave. Must be at least `--num-scene-profiles`. |
| `--render-stall-timeout` | 3600 | Kill a render that prints nothing for this many seconds. |
| `--render-fail-on-video-defects` | off | Fail a problem whose encoder could not publish every video, instead of finalizing it as `incomplete_videos`. |

Every flag above except `--render-pass` applies to **every** pass, so one run cannot give two
passes different cameras, sidecars or schedules. Only the YAML and the copy count vary per pass,
and both live in the `--render-pass` value itself.

A render cannot be combined with `--vecgen-record-videos`.

## Output

Every rendered split gets a `meta/render_params.json` describing how it was rendered. Its
top-level keys are:

| Key | Meaning |
|---|---|
| `rendered_at`, `render_script` | When the render ran, and which script ran it. |
| `completed` | Whether the render reached a final state, **not** whether it succeeded. See [Common pitfalls](#common-pitfalls). |
| `status` | `complete`, `incomplete_videos` or `failed`. |
| `video_defects` | The exact `(episode, feature)` videos that are missing, for a patch pass. |
| `empty_reason` | Why a finished render recorded nothing, when it recorded nothing. |
| `episodes_recorded` | The number of episodes in **this split**. |
| `episodes_total` | The problem's **source** episode count, across all splits. With N copies per episode the splits together hold N times this many. |
| `mode`, `fps` | `render-only` or `physics-step`, and the recording rate. |
| `env_file`, `source_datasets` | What was rendered, and from where. |
| `args` | The run's own arguments: the flags file, `num_envs`, `renders_per_episode`, `camera_base`, `env_spacing`, the codecs and the rest. `scripts/render/fast_patch.py` rebuilds the render command from it. |
| `flags`, `flags_sha256`, `flags_resolved_sha256` | The randomization, the digest of the literal file, and the digest of the resolved dict. Group shards by the **resolved** digest. |
| `dr_seeding` | Which seeding mode produced these values. A consumer must branch on it. |
| `initial` | The scene as actually built: cameras, materials and lights. |
| `episodes` | Per-episode records, including `src_episode_index`, the split, and the batch placement. `iter`, which of the N copies this is, appears only above one copy per episode. |
| `split_group` | Present only for a `--split_groups` member. |

`completed` and `video_defects` together give three states, so a gap in the output is neither
silently accepted nor treated as a total failure:

| `completed` | `video_defects` | Meaning |
|---|---|---|
| `true` | `[]` | Terminal with no known holes. Check `episodes_recorded` before trusting it, because a problem that can never render finalizes here too, with `0` and an `empty_reason`. |
| `true` | non-empty | Usable but incomplete. The listed videos are missing and need a patch pass. |
| `false` | any | The render did not finish. This is also the live state of a render still running, because `render.py` rewrites the file after every wave as a crash checkpoint. |

### Validating the output

Metadata alone cannot prove a render is good, so check the videos themselves:

```bash
python scripts/render/validate_dataset_videos.py <out_dir> --frames
```

Without `--frames` only the structural check runs, which catches an unopenable file but passes a
short one. Either way it can only inspect videos that exist, so a video that was never written is
caught by `video_defects` instead.

## Domain randomization

The plain YAML above fixes every value. Replace any of them with a **set** or a **range** and
the renderer samples instead, giving each episode its own look from the same file:

```yaml
skybox:
  set: polyhaven/rooms        # a pool of skies, not one name
  rotation_deg: [0, 360]      # a range, not 0
  intensity: [500, 1000]
materials: {...}              # table and block surfaces
scene_lights: {...}           # fill, local lights, the sun
env_sphere: {...}             # the visible backdrop sphere
randomize: {...}              # camera pose and field of view
randomize_task_letters: {...} # the glyph on each block
randomize_block_colors: {...} # cuboid colours
```

```bash
--render-pass src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache.yaml
```

Nothing else changes: same renderer, same stage, same output layout. The whole file is recorded
in every problem's `render_params.json` as the dataset's visual provenance.

Five flags YAMLs ship in `src/toyblocks/domain_randomization/flags/`:

| File | Use |
|---|---|
| [`render_flags_plain.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_plain.yaml) | One fixed look, nothing sampled. The plain baseline. |
| [`render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml) | All-random lighting, materials and cameras, plus the train glyph split (symmetry-preserving) and per-env block colours. |
| [`render_flags_allrand_texcache.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache.yaml) | All-random lighting, materials and cameras, without glyph or colour swaps. |
| [`render_flags_camtest.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_camtest.yaml) | A small camera preset for quick tests. It randomizes nothing. See [Common pitfalls](#common-pitfalls). |
| [`render_flags_open_hybrid_camera_rand_only.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_open_hybrid_camera_rand_only.yaml) | Camera randomization only. |

The two `allrand` files sample HDRI backdrops from the `polyhaven` and `indoor-2018` pools. See
[HDRI backdrops](local.md#hdri-backdrops).

To write your own, see the
[YAML reference](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/YAML_REFERENCE.md).
It covers every top-level key, the value forms the resolver accepts, and, importantly, *when*
each value is drawn: per wave, per episode or per env.

## Render passes

One run can produce several looks of the same episodes. Each **pass** is one YAML, rendered over
every source episode into its own `job_<name>/` directory, where `<name>` is the YAML's file name
with any `render_flags_` prefix stripped. The merge takes them all:

```bash
--render-pass src/toyblocks/domain_randomization/flags/render_flags_plain.yaml
--render-pass src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache.yaml:3
```

That renders the plain look once into `job_plain` and the randomized look three times into
`job_allrand_texcache`, so the merged dataset is 4x the source episodes. The `:N` suffix is per
pass, and without it a pass renders once.

Passes are keyed by that `job_<name>`, so two YAMLs whose names reduce to the same one are not
both rendered. The run keeps the first and warns. The merge also reads every `job_*` directory
under `render/out/`, not only the passes this command asked for, so a directory left by an
earlier run of the same experiment is merged again. Delete it, or use a fresh `--experiment-id`.

Each pass is a separate renderer invocation rather than extra `-N` iterations within one,
because a process applies one flags dict before the sim is built, and the per-wave levers (dome,
skybox, exposure) are scene-global, so a differently-flagged episode sharing a wave would still
be lit by that wave's draw. Separate job directories also mean each pass resumes independently,
and a problem counts as rendered only when **every** pass has landed. Otherwise a failed pass
would contribute 3 copies where 4 were promised and nothing would report it.

**A plain pass keeps the scene and drops the draws.** The point of rendering one beside
randomized passes is that they are comparable: same backdrop, same renderer, only the sampling
gone. That is why it takes a YAML rather than rendering with no flags at all. Dropping the YAML
would bring the backdrop geometry back and change the render mode, giving a different scene
rather than the same one unrandomized. [`render_flags_plain.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_plain.yaml) is that baseline, and any YAML of your own can
take its place.

### N copies within one pass

Often you want several visual variants of the same trajectory, for example to make a policy
robust to lighting. A pass written `FLAGS.yaml:N` replays each source episode N times, each time
with freshly sampled randomization. The state and action trajectory is identical across the
copies and only the pixels and camera columns differ, so the pass has **N times** the source's
episodes and frames. Each output episode records the `src_episode_index` it came from, and its
`iter` when there is more than one copy.

Running `render.py` by hand, the same multiplier is `-N` / `--renders_per_episode`.

A plain pass beside a randomized one makes the merged dataset **(N+1) times** the source:

```bash
--render-pass src/toyblocks/domain_randomization/flags/render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml:3 \
--render-pass src/toyblocks/domain_randomization/flags/render_flags_plain.yaml
```

That gives `job_allrand_texcache_glyphs_trainsplit_symmetric` with 3 copies per episode and
`job_plain` with 1, so the merge ships 4x the source episodes.

## Reproducing a recorded look

Because each episode's sampled settings are recorded, a render can be reproduced later:

```bash
python scripts/render/render_from_params.py --help
```

Pass the `dr_seeding` mode recorded in the dataset's own `render_params.json`.

## Flags

These are `render.py`'s own options. `datasets_dir` is positional and `--output` is required,
and everything else has a default. Isaac Lab's `AppLauncher` adds its own on top, such as
`--device`, `--kit_args` and `--rendering_mode`. `--headless` and `--enable_cameras` are forced
on after parsing, so passing them changes nothing.

### Source and output

| Flag | Default | Meaning |
|---|---|---|
| `datasets_dir` | (positional, required) | The root containing the recorded dataset or datasets. |
| `--output` | (required) | The output directory. It mirrors the structure of the input. |
| `--env_file` | `None` | The env package's `env.py`. For an unmerged dataset it is only the fallback, used when no per-problem env matches. |
| `--envs_dir` | `None` | A root holding per-problem env packages as `<envs_dir>/<problem>/env.py`. Tried first, then `<datasets_dir>/envs/<problem>/env.py`, then `--env_file`. |
| `--assets_paths` | `None` | Extra asset search roots for HDRIs and skyboxes, searched in order before the repo default (`assets/environments`). Use it when the HDRI pools live somewhere else, for example on another disk. The `RENDER_HDRI_DIR` environment variable does the same for the default root. |
| `--copy_source_data` | off | Replace the recorder's re-derived `data/` with a copy of the source's. Off by default, because the source data is canonical and can be copied or symlinked instead. |

### Episode selection

| Flag | Default | Meaning |
|---|---|---|
| `--max_episodes` | all | The maximum number of episodes rendered per source dataset. |
| `--skip_failure_episodes` | off | Render only `blocks_success`. The merge keeps only that split anyway, so for a merge-bound run the failure split is pure cost. This **renumbers the global episode index**, so such a run cannot resume an output built without it. |
| `--episodes_file` | `None` | Render only the listed episodes, for a targeted patch. Output episodes are renumbered per split, but each records its `src_episode_index`. Refused when the flags YAML sets `randomize_task_letters`, as the `glyphs` file does. Use `--episode_offset` there. |
| `--episode_offset` | `None` | Select a fragment for parallel rendering: the global slice `[offset, offset+max_episodes)`. Overrides `--episodes_file`. |
| `--fragment_invariant` | **on** | Keep the full per-problem episode list inside a fragment, so render-uids, wave grouping and randomization draws match a single-process run. Reassembling the fragments then gives a merge that is byte-identical to one big run. |
| `--split_groups` | off | Render each member of a vecgen `problem_grp_*` directory as its own unit, and a no-op on a source that has none. Alongside `--episode_offset` it must match the enumeration the offsets were planned with, or every slice misaligns. |

### Cameras and video streams

| Flag | Default | Meaning |
|---|---|---|
| `--skip_cameras` | `None` | Cameras **not to spawn**. They are dropped before the scene is created, so both their RGB and depth are absent and their render cost is never paid. Names work with or without the `camera:` prefix. |
| `--skip_depth` | off | Do not render or record the main depth stream. Cannot be combined with `--extra_depth`. |
| `--depth_format` | `12bit` | How the main depth is stored. `12bit` is native `gray12le`. `rg8` is the same uint12 packed into lossless 8-bit RGB, about 3x larger but much faster to read at random positions. Neither loses precision. |
| `--depth_codec` | `hevc` | `hevc` encodes about 15x faster, `av1` produces smaller files. Both are lossless 12-bit millimetres. |
| `--depth_gop` | `1` | The keyframe interval for the main depth. `1` is the friendliest for random access and the largest. Higher values are smaller and faster to encode, at the cost of seeking. |
| `--rgb_GOP` | `2` | The keyframe interval for the main RGB. `0` lets SVT-AV1 choose. |
| `--extra_rgb` | `None` | Also write a 224-px RGB video per camera, in the training sidecar layout. It is resized with Pillow BILINEAR, and ffmpeg `scale` is **not** equivalent. |
| `--extra_depth` | `None` | Also write a 224-px depth video per camera: `rg8_224`, `g12_224` or `rg8_55_224`. `g12_224` and `rg8_224` are lossless and decode to identical depth, `g12_224` at a fraction of the size. `rg8_55_224` packs 10 bits (R = mm >> 5, G = mm & 31) and **clips at 1023 mm**, and it is what the pipeline passes by default. |
| `--extra_rgb_GOP` | `0` | The keyframe interval for the `--extra_rgb` sidecars. `0` lets SVT-AV1 choose. The pipeline passes `2`. |
| `--render_scale` | `None` | Scale the preset cameras' resolution while keeping the field of view. Requires `--skip_cameras gripper_camera left_camera`, because robot-mounted cameras are not scaled, and cannot be combined with `--match_recorded_cameras`, whose recorded intrinsics are at the old size. |
| `--camera_base` | `data` | Where each camera's starting pose comes from before randomization. `data` reproduces the calibration the source was captured with, `scene` uses the built SceneConfig. Unusable recorded values fall back to `scene` **with a warning**, never silently. |
| `--match_recorded_cameras` | off | (Experimental.) Override extrinsics and intrinsics with the recorded values. Camera overrides in the flags YAML always take precedence. |

### Randomization and seeding

| Flag | Default | Meaning |
|---|---|---|
| `--flags` | `None` | The flags YAML. |
| `-N`, `--renders_per_episode` | `1` | The number of renders per source episode. See [render passes](#render-passes). |
| `--dr_seeding` | `hash` | How per-episode draws are seeded: `hash` (the default), `indexed`, or the legacy `stream`. |
| `--material_baseline_revert` | off | Reset every writable material key to the asset's own value before each draw. Without it, a key the chosen material leaves out keeps the previous episode's value, so materials bleed across episodes. Off by default because it changes the rendered output. |
| `--enable_gi` | off | Turn on RTX global illumination and reflections. Enabled automatically when the YAML has a `skybox` block, which [`render_flags_plain.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_plain.yaml) and both `allrand` files have. |

The seeding modes differ in how an episode's values are derived. `stream` seeds one RNG over the
whole episode list, so an episode's values depend on how many episodes come before it. `indexed`
and `hash` derive each episode independently, which is what lets a patch jump straight to a
missing episode.

### Performance and rendering

| Flag | Default | Meaning |
|---|---|---|
| `--num_envs` | `8` | The number of parallel envs, which is also the replay batch size. Use a multiple of 8, or fewer than 8. |
| `--num_writers` | `1` | Encoder processes per render process. Raise it when the encoder, not the GPU, is the bottleneck. |
| `--wave_sort_block` | `10` | Group episodes of similar length into a *wave* (a batch of episodes rendered together), within blocks of this many waves. A wave renders every env until its longest episode ends, so rendering in source order wasted about 36% of rendered env-frames on measured runs. |
| `--scene_swap` | **on** | At each problem boundary, make the live scene match that problem's block set. Costs nothing when consecutive problems share a set. `--no-scene_swap` skips mismatched problems instead. |
| `--scene_swap_warmup` | `0` | Extra RTX passes after a scene swap, so the denoiser can converge. |
| `--rtx_warmup_frames` | `1` | Extra render passes at `t==0` of each batch, so temporal renderers converge and frame 0 has no warm-up artifact. Try 8 to 16 if artifacts persist. The pipeline passes `16`. |
| `--antialiasing` | preset (DLSS) | `Off`, `FXAA`, `TAA`, `DLSS` or `DLAA`. `Off` and `FXAA` work on single frames, the others carry a temporal history that is empty on frame 0. Has no effect under the shipped path-tracing files. See [Common pitfalls](#common-pitfalls). |
| `--disable_dlss` | off | A shortcut for `--antialiasing FXAA`. Ignored if `--antialiasing` is given. |
| `--skip_initial_step` | off | Skip the physics settle at construction time. Safe, because the replay overrides all state on every frame. |
| `--physics_step` | off | Run one physics step per frame instead of rendering only. This removes occasional duplicate frames at the cost of slight drift. The default is to place everything and render, with no physics. |
| `--env_spacing` | `None` (5.0) | Override the scene's env spacing. Larger spacing stops a neighbouring env's backdrop from leaking into a camera's peripheral view when a skybox is used. **A YAML `env_spacing` wins over this flag**, so a file that sets one, as [`render_flags_plain.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_plain.yaml) and both `allrand` files do, decides the spacing. |

### Resume, integrity and debugging

| Flag | Default | Meaning |
|---|---|---|
| `--resume` | off | Skip problems whose output already has `render_params.completed == true`. See [Common pitfalls](#common-pitfalls) before using it. |
| `--fail_on_video_defects` | off | Mark a problem incomplete, forcing a full render, if any video could not be published. Off by default: the problem stays complete with `status=incomplete_videos` and an exact list of missing videos for a patch pass (`scripts/render/fast_patch.py`). |
| `--passthrough_source_columns` | **on** | Copy every column from the matching source episode, so the two datasets differ only where the render is authoritative. |
| `--patch_actions_from_source` | **on** | Copy the source's `action.*` columns. Superseded by the flag above. |
| `--dump_scene` | off | Print the stage layout and exit. |
| `--dump_probe` | `None` | Write the applied material values, live carb settings and render products to JSON after the first wave, then continue. |
| `--show_gizmos` | off | Keep debug visualization markers in the render. Hidden by default. |

## Common pitfalls

### `render.py` hangs after it finishes

`render.py` prints `all jobs done` and then often **hangs in Isaac teardown**. Run it through
`scripts/render/run_local_render.py`, which watches for that marker and kills the process group
30 s later, as the pipeline always does. Never judge success from the exit status. Judge it from
the marker and the result on disk.

```bash
python scripts/render/run_local_render.py -- python scripts/render/render.py <dataset_dir> ...
```

### `completed: true` does not mean the render produced data

`completed: true` means the render reached a final state, not that it *has data*. It is written
so that a re-run does not retry the problem forever, so it is also written when the recorded block
size is not in the problem's size table, or when every source parquet is unreadable. Those cases
write a `render_params.json` but **no `info.json`**, and `info.json` is what merge actually needs.
Note also that there is no `total_episodes` key, because the problem-wide count is
`episodes_total`.

### A broken render can still look complete

**Metadata cannot see a broken render.** A host-RAM out-of-memory error during encoding produces
videos that fail with `moov atom not found`, inside a dataset whose `render_params.json` still
says `completed: true`. Always run `validate_dataset_videos.py`, shown under [Output](#output),
before using a rendered dataset.

### [`render_flags_camtest.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_camtest.yaml) produces identical copies

[`render_flags_camtest.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_camtest.yaml) has **no random section at all**. A `:4` pass with it produces four
copies of the same look, identical in depth and differing in RGB only by renderer noise, while
every size-based check still reports 4x. Use it only to test the camera rig, never to check that
randomization works.

### `--antialiasing` has no effect under the shipped path-tracing files

[`render_flags_plain.yaml`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/flags/render_flags_plain.yaml) and both `allrand` files select RTX Real-Time 2.0 path tracing through
their `carb_settings`, and that renderer does not let antialiasing be turned off.
`--antialiasing` and `--disable_dlss` set the simulation's antialiasing mode, which the YAML's
render mode then overrides, so the log prints the mode you asked for and the pixels do not
change. Verify any antialiasing change with a pixel difference, never with the log line. To get
a genuinely different mode, change the render mode in the YAML.

### Mixing seeding modes in one dataset

**Never mix two `--dr_seeding` modes within one dataset**, because each produces different
values. To reproduce or patch an existing dataset, pass the mode recorded in its
`meta/render_params.json`.

### Two renders into the same output delete each other's work

`render.py` **deletes a non-finalized `<output>/<problem>` before rendering it**, on every run
and not only under `--resume`, because partial output can never be appended to safely. A
finalized directory is left alone. So two renders pointed at the same problem directory delete
each other's work rather than failing. Never run two renders against the same output problem
directory.

### Checking a multiplier by file size gives the wrong answer

To confirm that `:N` really multiplied the dataset, count episodes, frames and distinct video
files, **never bytes**. Merge hardlinks videos into the merged tree, so `du` of the merged
directory is meaningless, and different draws compress differently (measured at 2.055x for N=2,
not 2x).

The failure a size check cannot catch is N copies that are pixel-identical because nothing was
randomized. Check that the copies actually *differ*: there should be distinct
`observation.camera_pose.*` values per episode under camera randomization, and differing
**depth** frames. Depth is deterministic and RGB is not, so RGB can prove a change but never its
absence.

## Next

[Merge](merge.md) the rendered problems into one training dataset. Once this stage is marked
complete, the merge reads `render/out/job_*` and nothing else, so a problem that was never
rendered simply will not appear. See
[what counts as "rendered"](local.md#what-counts-as-rendered) for how the local flow guards
against that.

## See also

- [Running the pipeline locally](local.md): the local pipeline, the render schedules, HDRI backdrops, and the gate that decides what gets merged
- [Execution](execution.md): the stage that produces the trajectories this stage replays
- [Merge](merge.md): how rendered problems become one training dataset
- [YAML reference](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/domain_randomization/YAML_REFERENCE.md): every randomization key
- [DETERMINISM.md](https://github.com/allenai/ToyBlocks/blob/main/docs/render/DETERMINISM.md): what is reproducible, and what is not

---- FILE: docs_source_user_guide_workflows_datagen_task_generation.md ----

# Stage 1: Task generation

Before the simulator can produce any demonstrations, the pipeline needs to know what task to
solve. Task generation answers that question by writing **PDDL problem files**. PDDL (Planning
Domain Definition Language) describes a task as two lists: the facts that are true at the start,
and the goal that must be true at the end. Both are written with predicates such as `on`,
`on_table` and `ori_of`, so a goal like "the red block is on the green block" becomes one line
of PDDL.

Each generator in `scripts/task_gen/` describes a whole *family* of tasks, such as "flip one
block" or "stack three blocks". It builds a declarative `ProblemSpec` (the blocks, distractor
pools, init rules and goal), and `ProblemSpec.generate()` then samples `--count` concrete problems
from it, writing one `.pddl` file per problem into `--out-dir`. This stage is pure CPU: it needs no
Isaac and no USD assets, and finishes in a few seconds of Python.

Usually the pipeline runs this stage for you. Run it by hand when you want to inspect the
problems a generator produces, or to build a problem set once and reuse it.

## Where it fits

- **Input:** nothing but the generator's own flags.
- **Output:** a directory of `.pddl` problem files, read by [stage 2, env generation](env_generation.md).

The stage is optional. You can skip it and feed stage 2 the checked-in problems in
`src/toyblocks/tamp/blocks/problems/`, or PDDL you wrote by hand.

## Running it

The smallest useful run picks a generator and tells it how many problems to write and where:

```bash
python scripts/task_gen/flip.py --count 50 --out-dir outputs/flip/tasks --seed 42
```

`--count` is the number of problems, `--out-dir` is where the `.pddl` files go, and `--seed` makes
the sampling reproducible. Always pass `--out-dir`, for the reason explained under
[Common pitfalls](#common-pitfalls).

To look at what a generator produces without writing anything, add `--preview`. It prints one
sampled problem to the terminal:

```bash
python scripts/task_gen/stack_three.py --train --seed 42 --preview
```

### Examples

One command per task family, ready to copy:

```bash
# Flip block_r once (any direction, goal from the flip table)
python scripts/task_gen/flip.py \
    --count 50 --out-dir outputs/flip/tasks --seed 42

# Rotate block_r by one yaw step to o2
python scripts/task_gen/rotate.py --goal-ori o2 \
    --count 50 --out-dir outputs/rotate/tasks --seed 42

# Pick-and-place block_r onto block_green, or off it onto the table
python scripts/task_gen/pnp.py \
    --count 50 --out-dir outputs/pnp/tasks --seed 42

# 3-block towers in letter + digit + colour scenes (--train or --val glyph pools)
python scripts/task_gen/stack_three.py --train \
    --count 50 --out-dir outputs/stack3/tasks --seed 42

# Play-data scenes (used by scripts/datagen/run_playdata_pipeline.py)
python scripts/task_gen/play_scene.py \
    --count 50 --out-dir outputs/play/tasks --seed 42

# Search scenes for the DFA goal policies (src/toyblocks/playdata/dfa/AUTHORING.md)
python scripts/task_gen/find_as.py --count 5 --out-dir outputs/find_as/tasks --seed 42
python scripts/task_gen/search.py --letter R --distractors 2 4 \
    --count 5 --out-dir outputs/search/tasks --seed 42
```

## Through the pipeline

In `run_datagen_pipeline.py` you choose the generator with `--task-gen-script` (default
`scripts/task_gen/stack_three.py --train`). The string can carry the generator's own flags as well:

```bash
python scripts/datagen/run_datagen_pipeline.py --experiment-id nov04_stack3 \
    --task-gen-script "scripts/task_gen/stack_three.py --num-blocks 4 6 --glyph-ori o2" \
    --task-gen-count 50 --task-gen-seed 42
```

The pipeline splits that string with `shlex.split` and then **appends** its own values for
`--count`, `--out-dir`, `--seed`, `--block-size-range`, `--table-height-range`, `--friction-range`
and `--num_distractors`. If you also set one of those inside the string, it is passed twice, and
argparse keeps the last one, which is the pipeline's. So set them with the pipeline's flags
(`--task-gen-count`, `--task-gen-seed`, `--num-distractors` and so on) rather than inside the
string.

## Output

Each problem is one file, named `problem_<internal problem name>.pddl`. For the declarative
generators that is `problem_declarative_<n_blocks>_<timestamp>_<random>.pddl`. The body is a
standard PDDL problem:

```text
(define (problem ...) (:domain blocks-tamp) (:objects ...) (:init ...) (:goal ...))
```

The scene-randomization comment lines described below are appended after the goal.

To check a run, open one of the files, or rerun the same generator with `--preview` and read the
`:init` and `:goal` sections.

## The generators

There are 7 generators. They fall into three families.

**Single-block skills.** One target block performs one skill.

| Script | Task family |
|---|---|
| `flip.py` | One contact flip of a target block (default `block_r`). `--direction` constrains the flip, and `--goal-ori` pins the target face. |
| `rotate.py` | One yaw step (clockwise or counter-clockwise) of a target block. `--direction cw|ccw` and `--goal-ori` work as on `flip.py`. |
| `pnp.py` | One pick-and-place of `block_r`, keeping its orientation: onto a support block (default `block_green`), or off it onto the table. `--mode stack|unstack|all`. |

**Stacking.**

| Script | Task family |
|---|---|
| `stack_three.py` | 3-block towers in a mixed letter, digit and colour scene of 4–10 blocks, with `--train` and `--val` glyph pools. Every glyph block in the tower must end readable; symmetric letters also accept the orientations that show the same glyph. `--init-readable`, `--init-flip-unreadable` and `--init-ori` control the starting orientations. This is the default generator, and the one the RI training set was made with. |

**Play and search scenes.** The PDDL goal exists only to satisfy code generation; the play
pipeline picks its own goals per episode.

| Script | Task family |
|---|---|
| `play_scene.py` | A few glyph blocks (`--blocks`, default `A I 2 E`) on the table, clear, at random orientations. |
| `search.py` | One target letter (`--letter`, default `R`) that starts non-readable, among `--distractors MIN MAX` (default 2–4) distractors. |
| `find_as.py` | Four `A` blocks plus six distractor letters, flat on the table; five fixed distractor sets. |

## How scene randomization reaches the simulator

The pipeline can vary block size, table height and friction from one environment to the next.
These are physical properties rather than facts about the task, so they are **not** PDDL
predicates. Instead, the generator writes them as comment lines at the end of the problem file:

```text
    ;block_size_range = [0.03, 0.05]
    ;table_height_range = [-0.05, 0.05]
    ;friction_range = [0.5, 0.5]
```

[Stage 2](env_generation.md) reads these lines back and bakes a set of scene profiles from them.
Two details of the format matter if you ever edit these lines by hand; both are covered under
[Common pitfalls](#common-pitfalls).

No generator writes `;block_x_range` or `;block_y_range`. The window where blocks may spawn on
the table is set by a stage 2 flag instead.

Through the pipeline, scene randomization is on by default (`--randomize-scene`), and the ranges
above are the pipeline's defaults. With `--no-randomize-scene` or `--smoke-test`, the pipeline
**overwrites** whatever ranges you passed with the fixed values `[0.04, 0.04]`, `[0.0, 0.0]` and
`[0.4, 0.4]` after parsing. So `--no-randomize-scene --block-size-range 0.03 0.05` discards the
range rather than honouring it.

## Flags

Most generators share these flags. Each generator also has its own, listed by `--help`.

| Flag | Usual default | Meaning |
|---|---|---|
| `--count` | `5` | The number of problems to write. `play_scene.py` defaults to `1`. |
| `--out-dir` | `None` | The directory the `.pddl` files go into. Always pass it; see [Common pitfalls](#common-pitfalls). |
| `--seed` | `None` | The seed for `random.seed()`. `find_as.py` defaults to `42`, and `play_scene.py` to `0`. |
| `--preview` | off | Print one sampled PDDL problem and write nothing. Available on every generator except `play_scene.py`. |
| `--block-size-range MIN MAX` | `[0.03, 0.05]` | The cube edge length range, written as a `;block_size_range` comment. |
| `--table-height-range MIN MAX` | `[0, 0.04]` | The table height offset range, written as `;table_height_range`. |
| `--friction-range MIN MAX` | `[0.1, 0.4]` | The friction range, written as `;friction_range`. |

`stack_three.py` and `play_scene.py` have no default for the three range flags: run by hand
without them, they write no randomization comment at all, and stage 2 uses its fixed fallbacks.
The pipeline always passes all three.

## Common pitfalls

### Problems land in `src/toyblocks/Tasks/` when `--out-dir` is omitted

You might expect a missing `--out-dir` to mean `./outputs`. The generators instead fall back to
`src/toyblocks/Tasks/`, inside the source tree. The exception is `play_scene.py`, which makes
the flag required. Always pass `--out-dir` so the files end up where you expect.

### A hand-edited randomization line is silently ignored

The parser in stage 2 looks for the exact text `;block_size_range = [`, so **the ` = [` spacing
matters**. A line written as `;block_size_range=[0.03,0.05]` does not match and is ignored without
a warning. You then get the fixed fallbacks instead: block size `0.04`, table delta `0` and
friction `0.3`. Keep the spacing exactly as the generators write it.

### Problem files from elsewhere are executed as code

The randomization values are parsed with `eval()`, so a hand-edited PDDL comment is run as
Python. Treat problem files from someone else as code, not data, and read them before using them.

### `--num_distractors` needs an underscore, and its meaning varies

Every generator spells the flag with an underscore and rejects the hyphenated
`--num-distractors`. The pipeline passes the underscore form, which is why it works there. Use
`--num_distractors` when you run a generator by hand.

What the number means also depends on the generator:

- **The maximum of a 0..N range** (default `5`): `flip.py`, `rotate.py`, `pnp.py`. Set
  `--distractor-count-min` to the same value for an exact count, and `--distractor-blocks` to
  replace the built-in pool.
- **Ignored**: `stack_three.py`, `play_scene.py`, `search.py`, `find_as.py`. `search.py` takes
  its distractors from `--distractors MIN MAX` instead; the others have fixed scene recipes.

Through the pipeline, `--num-distractors` defaults to `0`, and it is always passed. So a
pipeline run with `flip.py`, `rotate.py` or `pnp.py` produces scenes **without distractors**
unless you pass `--num-distractors N`, even though the generator on its own defaults to up to 5.

### `flip.py` and `rotate.py` do not target `o2` by default

Without `--goal-ori`, both generators run in *dynamic-goal* mode. The initial orientation is drawn
uniformly from all 24, and the goal is computed forward through the flip or yaw table, so **every
problem gets a different goal face**. `flip.py` also flips in any of the four directions. If you
want every problem to end on the same face, pass `--goal-ori o2`; the generator then fixes the
goal and works backwards to the initial orientation.

### Renaming a problem file renames its task

Downstream stages name a task after its file, not after the `(problem ...)` name inside it.
`task_slug_from_pddl_path` takes the file's basename stem and replaces hyphens with underscores.
So renaming a generated `.pddl` file silently renames the task, and two problems with the same
basename collide in one output directory.

### `--block` is misread on `rotate.py`

argparse accepts any unique prefix of a flag name, and `--block` is a prefix of
`--block-size-range`. `flip.py` and `pnp.py` turn this off with `allow_abbrev=False` (and
`flip.py` accepts `--block` as an alias of `--target-block`), but `rotate.py` does not, so on
`rotate.py` `--block foo` is taken as `--block-size-range` and fails with "expected 2
arguments". Use `--target-block` there.

## Next

Feed the problems to [stage 2, env generation](env_generation.md), or let
[the pipeline](../data_generation.md) run every stage for you locally
([Running the pipeline locally](local.md)).

---- FILE: docs_source_user_guide_workflows_evals_evaluate.md ----

# `evaluate.py` Reference

[`scripts/evaluate.py`](https://github.com/allenai/ToyBlocks/blob/main/scripts/evaluate.py)
is the eval worker: `launch_eval.py` runs one per eval GPU, each pulling episodes from the
episode queue. You can also run it by hand, for example to debug one worker against a
policy server you started yourself. This page covers its action sources, how to run it
against a server, the observation transforms, its flags and its outputs. For the full
pipeline, see [Policy Evaluation](../evaluations.md).

`evaluate.py` parses the `Args` dataclass in
[`src/toyblocks/eval/args.py`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/eval/args.py)
with `tyro`, and hands it to `toyblocks.eval.run_eval.evaluate`. `Args` also inherits the
Isaac launcher options of
[`BaseArgs`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/cli/base_args.py)
(`--device` (default `cuda:0`), `--headless` (on for eval), `--enable_cameras`,
`--kit_args`, `--rendering_mode`) and the nested env-config overrides `--env-cfg.<field>`
(for example `--env-cfg.robot-id droid_franka`). Flags accept `-` or `_` between words,
and boolean flags are turned off with `--no-<flag>`. Isaac starts before the arguments
are parsed, so even `--help` launches it.

Before the run starts, `evaluate.py` also:

- adds `--enable_cameras` when `--obs_mode` contains `rgb`;
- snaps `--num_envs` to a value the task accepts (`reconcile_num_envs_with_task`), since
  autogen block tasks bake a fixed number of cube-size slots;
- with `--dataset_path`, defaults the eval `robot_id` and `scene_preset_id` to the
  dataset's recorded provenance, warning on a mismatching override and failing when the
  provenance is missing and no override was given (see
  [Dataset scene provenance](launch_eval.md#dataset-scene-provenance)).

## Action sources

`evaluate.py` picks where actions come from based on its flags:

| Source | Selected by | Use for |
|---|---|---|
| Remote policy server | `--policy_host` (+ `--policy_port`, default `8000`) | Evaluating the served ManiFlow / Molmo2 policies, or any model behind the `BasePolicy` interface. |
| Random actions | `--random_actions` | Sanity checks: uniform in `[-1, 1]`. |
| Zero actions | none of the above | Sanity checks of task spawning and metrics. |
| Dataset replay | `--replay` with `--queue_url`, `--dataset_path` and `--num_envs 1` | Playing back each queued episode's recorded actions and reporting how far the simulation diverges from the recording. |

`--obs_mode state` raises when combined with `--policy_host` (see the flag table below).
`--random_actions` raises when combined with `--policy_host`, and `--replay` raises when
combined with either.

### Random and zero actions

```bash
python scripts/evaluate.py --task ToyBlocks-Lift-v0 \
    --random_actions --num_envs 4 --num_eval_steps 200
```

`--random_actions` samples every action component uniformly from `[-1, 1]`; with no
action source at all, every step gets a zero action. Both are handy for confirming that a
task spawns correctly and that recording and metrics work before plugging in a policy.

### Dataset replay

Replay is easiest through the launcher, which also starts the queue:

```bash
python scripts/launch_eval.py --replay \
    --dataset-path data/datasets/my_dataset --episode-indices "0"
```

See [Dataset Replay](replay.md) for how replay works, its metrics and its requirements.

## Running against a policy server by hand

Running the server and the eval worker in two terminals is the easiest way to debug
either side with breakpoints.

**1. Start a policy server** (terminal 1),
[`serve_maniflow_policy`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/serving/serve_maniflow_policy.py).
`--hl oracle` serves the ManiFlow LL alone (the client supplies the high-level commands);
`--hl model` serves Molmo2 + ManiFlow:

```bash
export H_VLA_PATH=$PWD/maniflow-tb PYTHONPATH=$PYTHONPATH:$PWD/maniflow-tb

# ManiFlow, with the high-level oracle on the client
python -m toyblocks.serving.serve_maniflow_policy --port 8000 --hl oracle \
    --checkpoint data/checkpoints/my_maniflow_run/checkpoints/steps_400000_model.safetensors \
    --config data/checkpoints/my_maniflow_run/config.yaml \
    --train_config maniflow-tb/examples/Franka/train_maniflow_multimodal.yaml

# Molmo2 high level + ManiFlow low level
python -m toyblocks.serving.serve_maniflow_policy --port 8000 --hl model \
    --checkpoint data/checkpoints/my_maniflow_run/checkpoints/steps_400000_model.safetensors \
    --hl_checkpoint data/checkpoints/my_molmo2_run \
    --config data/checkpoints/my_maniflow_run/config.yaml \
    --train_config maniflow-tb/examples/Franka/train_maniflow_multimodal.yaml
```

**2. Run the eval worker** (terminal 2). Prompts and per-episode setups come from the
episode queue (`--queue_url`, started with
`python scripts/serve_episode_queue.py --dataset-path <root> --port 8001`) and the
dataset (`--dataset_path`), and the task must already be generated (see
[Policy Evaluation](../evaluations.md)):

```bash
python scripts/evaluate.py \
    --task <task-slug>-v0 \
    --policy_host localhost --policy_port 8000 \
    --queue_url http://localhost:8001/next --dataset_path data/datasets/my_dataset \
    --control_mode arm_joint_gripper_binary \
    --obs_mode rgb+state --obs_transform maniflow_blocks_table \
    --action_horizon 25 --sync_action_chunks --num_envs 2 \
    --use_oracle --save_lerobot
```

Drop `--use_oracle` against the `--hl model` server; `launch_eval.py` passes
`--hl_from_model` there instead.

**Split-terminal scripts.** `scripts/eval/serve_local_server.sh` (terminal 1) and
`scripts/eval/serve_local_client.sh` (terminal 2) wrap these steps and match
`launch_eval.py`'s ManiFlow and Molmo2 inputs. Both run in the foreground with plain
`python`, so a `breakpoint()` in the server, the eval client or an obs transform is hit
interactively (`launch_eval.py` backgrounds everything with redirected output). Activate
the venv first:

```bash
# Terminal 1: policy server (POLICY_NAME=maniflow serves --hl oracle)
MODEL_PATH=data/checkpoints/my_maniflow_run/checkpoints/steps_400000_model.safetensors \
HL_MODEL_PATH=data/checkpoints/my_molmo2_run \
    bash scripts/eval/serve_local_server.sh

# Terminal 2: task generation + episode queue + evaluate.py
DATASET_PATH=data/datasets/my_dataset EPISODE_INDICES=0,3 \
    bash scripts/eval/serve_local_client.sh
```

Their configuration (policy, checkpoints, dataset, ports, `num_envs` cap) lives once in
`scripts/eval/_common.sh`, sourced by both; override any variable inline. `POLICY_NAME`
defaults to `molmo2_maniflow` (`--hl model`). `MODEL_PATH` (and `HL_MODEL_PATH` for
`molmo2_maniflow`) and `DATASET_PATH` (or `PDDL_PROBLEM_FILE`, to generate the task from
a PDDL problem instead) have no defaults, and the scripts exit with a message when one is
missing. The client waits for the server's port, then either runs one batched pass sized
to the queue (`PER_EPISODE=0`, the default with `--hl oracle`) or one task generation,
queue and single-environment `evaluate.py` per episode (`PER_EPISODE=1`, the default with
`--hl model`). Results go under `runs/` (`OUT_PATH`). Note that both scripts first kill
your own stale servers, queues and `evaluate.py` processes.

Key flags:

- `--obs_transform`: how observations are converted for the policy (see
  [Observation transforms](#observation-transforms)).
- `--unbatched`: call the server once per environment instead of once per step with a
  batch of all environments, for servers that add their own batch dimension.
  `launch_eval.py` always runs batched.
- `--action_horizon N`: the server returns chunks of actions and one is applied per
  step; `--sync_action_chunks` puts all environments on the same chunk boundary so the
  server is queried once per chunk (the pipeline always sets it).
- `--save_lerobot`: record the rollouts as a LeRobot dataset, including the raw policy
  actions.

A policy that returns 9-dim actions (7 arm joints, gripper, `pd_mode`) switches the
controller gains through its trailing `pd_mode` channel; no flag is needed. The channel
drives the same PD-mode controller as replay, and is stripped before `env.step`. Depth
images are added to the observations automatically when the served checkpoint expects
them.

Any model can be served by implementing the small `BasePolicy` interface; see
[Setting up a new policy server](../imitation_learning/new_policy_server.md).

## Observation transforms

Registered in
[`src/toyblocks/serving/obs_transforms/__init__.py`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/serving/obs_transforms/__init__.py)
and selected with `--obs_transform` (default `none`, which sends the raw observations):

| Name | Use for |
|---|---|
| `maniflow` | ManiFlow Franka policies. |
| `maniflow_blocks_table` | Same as `maniflow`, mapping the blocks-table cameras (`front_camera` / `gripper_camera`) onto the policy's `front_rgb` / `gripper_rgb`. The default of `launch_eval.py`. |

The ManiFlow `agent_pos` width is the served checkpoint's, not a flag: the server
advertises `state_dim` in its metadata, and the client builds the state from
`STATE_DIM_LAYOUTS` (`obs_transforms/maniflow.py`): 8 (7 arm + 1 gripper), 9 (+ `pd_mode`)
or 19 (+ 7 joint velocities and 3 EE xyz). Without metadata it defaults to 19; any other
width raises.

These flags apply to the ManiFlow transforms only, and raise with any other transform:

| Flag | Default | Description |
|---|---|---|
| `--center_crop_ratio` | none | After the resize to 224, centre-crop RGB, depth and `target_heatmap` to `int(224 * ratio)` and resize back (inference counterpart of `random_crop_ratio`, e.g. `0.95`). |
| `--enable_crop` | off | Build `target_front_crop_rgb` on the client from the native front camera and target pixels. Needs a checkpoint with `use_target_front_crop >= 0`. |

To add a transform, subclass `BaseObsTransform`, override `transform` (and optionally
`action_postprocess`), and register it in `_lazy_registry`.

## Flags

The tables below list the user-facing flags with their defaults. Every flag's docstring in
`args.py` has the full details.

### Run and environment

| Flag | Default | Description |
|---|---|---|
| `--task` | `ToyBlocks-Lift-v0` | Gymnasium task id. Queue evals use the autogen `<slug>-v0` task generated from the dataset. |
| `--num_envs` | `4` | Parallel environments (snapped to the task's slot count). |
| `--num_eval_steps` | `200` | Maximum environment steps. Ignored under `--queue_url`, where the run ends when the queue is exhausted. |
| `--num_episodes` | none | Stop after this many finished episodes; with `--num_eval_steps`, whichever comes first. |
| `--obs_mode` | `state` | `state`, `rgb` or `rgb+state`. A `depth` component is added automatically when the served checkpoint takes depth. **Not combinable with `--policy_host`:** `state` flattens the observation into one tensor, while the server protocol needs a dict of named keys, so the pair is rejected up front. Use `rgb+state` (add `--obs_transform none` to send the raw keys). |
| `--control_mode` | env default | Control mode override, e.g. `arm_joint_gripper_binary` (needed for absolute joint targets: replay, `--dataset_path` runs, `--sync_action_chunks`, `--wave_resets`, `--ll_oracle`, play-mode checkpoints). |
| `--seed` | none | Random seed; no fixed seed when unset. |
| `--deterministic_cuda` | off | Deterministic cuDNN plus PhysX enhanced determinism and a single solver partition; slower, and still not bit-for-bit across hardware. |
| `--exp_name` | auto | Name of the run. |
| `--env_spacing` | env default | Grid spacing (m) between parallel envs. |

### Policy server

| Flag | Default | Description |
|---|---|---|
| `--policy_host`, `--policy_port` | none, `8000` | WebSocket policy server. Without a host, no server is contacted (zero actions, unless `--random_actions` or `--replay`). |
| `--action_key` | `actions` | Key of the server response that holds the actions. |
| `--unbatched` | off | One server call per environment instead of one batched call per step. |
| `--obs_transform` | `none` | See [Observation transforms](#observation-transforms). |
| `--action_horizon` | `0` | Actions per server chunk, one applied per step; `0` disables chunking. |
| `--sync_action_chunks` | off | Batched chunked evals: one shared chunk boundary for all environments, so the server is queried once per horizon. An environment whose episode ends mid-chunk holds its reset pose, hidden from the episode clock and the recording, until the boundary. |

### Queue and dataset

| Flag | Default | Description |
|---|---|---|
| `--queue_url` | none | Episode-queue URL (e.g. `http://localhost:8001/next`) the per-episode setups come from. |
| `--dataset_path` | none | LeRobot dataset root: reconciles robot and scene with its provenance, overlays its targets on plots, and enables the dataset PD-switch settle. Pass the dataset the queue serves. |
| `--expert_timeout_scale` | `0` | End each episode after this multiple of its expert demonstration's duration (needs `--queue_url` and `--dataset_path`; `0` disables). Such episodes end as truncations, so they keep their full metrics and TAMPER tags them `timeout`. |
| `--use_calibrated_cameras` | on | Use the fixed sim2real + FR3 gripper camera intrinsics instead of the dataset's. Disables the two options below. |
| `--ingest_camera_intrinsics` | on | Apply each episode's recorded camera intrinsics (needs `--no-use_calibrated_cameras`). |
| `--use_render_params` | off | On a rendered dataset, reproduce each episode's recorded camera pose, HDRI, materials and lights (needs `--no-use_calibrated_cameras`). See also `--render_replay_assets_paths` (extra HDRI roots), `--render_replay_warmup_frames` (default `16`) and `--wave_resets`. |
| `--replay_block_identity` | on | On glyph/colour-rendered datasets, paint each episode's recorded block letters and colours and prompt with the rendered goal. |
| `--verify_scene` / `--verify_scene_strict` | off | After the first queue reset, compare the scene with the recording and write `scene_verification.json`; strict aborts on hard mismatches. |

### High-level conditioning

| Flag | Default | Description |
|---|---|---|
| `--use_oracle` | off | Drive `task_name` and `target_heatmap` from the client-side symbolic oracle instead of a learned HL. Needs `--policy_host`, a ManiFlow transform and a PDDL problem per episode: `--pddl_problem_file`, or the queue (each setup's `pddl_problem_file`, else a problem rebuilt from its `pddl_goal` and recorded high-level state). The oracle re-plans from the live state (up to 3 times) when the next step's preconditions no longer hold. |
| `--pddl_problem_file` | none | One PDDL problem for every environment; a queue setup's own problem overrides it. |
| `--async_hl`, `--async_hl_call_scale` | off, `0` | Molmo2 HL with a play-mode LL: query the HL only at episode start and when the LL ends a skill; optionally cap HL calls at a multiple of the expert's. |
| `--ll_oracle`, `--ll_oracle_hl_call_scale` | off, `3.0` | Run Molmo2's commands with the vecgen motion-planned skills instead of the served LL (needs `--action_horizon 0`). |
| `--go_home` | off | With `--async_hl` or `--ll_oracle`: drive the arm home after a place, flip or rotate, before the next HL query. |
| `--post_place_lift` | `0` | Play-mode LL: lift the end effector this many metres after a release before the next LL query. |
| `--oracle_comparison` | off | Also run a client-side oracle (not fed to the LL) and show it next to the model in the HL overlay video. |
| `--hl_update_interval_ms`, `--hl_update_interval_jitter_ms`, `--estimated_hl_inference_time_ms` | `0` | Simulated HL latency: update interval K (with jitter) and inference time M. Must match training for checkpoints that use the previous front frame; see [HL latency](launch_eval.md#hl-latency). |

`--hl_from_model` is set by `launch_eval.py` for `--policy molmo2_maniflow`; it is not
meant to be passed by hand.

### Episode end and scoring

| Flag | Default | Description |
|---|---|---|
| `--episode_end` | `goal` | `goal` ends on the goal predicate (oracle runs: plan completion), `horizon` runs to `episode_length_s`, `ll_done` ends on a play-mode LL's -1. A stuck oracle plan and a learned HL's `done` end the episode in every mode. |
| `--collision` | `end` | A non-target block moving more than 2 cm or 15 deg fails the episode; `end` also ends it, `penalize` lets it run, `off` ignores collisions. |
| `--goal_ori_yaw_tol_deg` | `40.0` | Yaw tolerance of the goal's orientation atoms when judging goal success. |

A place-on-table sub-goal counts only within 25 front-camera pixels of the HL's table
point (a fixed tolerance, not a flag).

### Recording and video

| Flag | Default | Description |
|---|---|---|
| `--output_dir` | `runs/<run_name>` | Where everything is written. |
| `--save_lerobot` | off | Record the rollouts as a LeRobot dataset (scene data and raw policy actions), with the datagen recorder; see [LeRobot recording](https://github.com/allenai/ToyBlocks/blob/main/docs/lerobot_recording.md). |
| `--lerobot_dataset_name` | run name | Name of that dataset. |
| `--num_shards` | `8` | Parallel LeRobot writer processes, stitched into one `<name>_success` / `<name>_failure` pair at the end. |
| `--video_codec` | `libx264` | LeRobot RGB codec: `libx264` or `libsvtav1`. |
| `--video_fps` | control rate | Frame rate of saved videos and LeRobot datasets. |
| `--save_sensor_obs_video` | off | One MP4 per finished episode from the RGB observations (needs `rgb` in `--obs_mode`). |
| `--video_env_ids`, `--save_video_all_envs` | `(0,)`, off | Which envs the videos record. |
| `--video_camera` | all, tiled | Camera used for videos. |
| `--drop_cameras` | `left_camera` | Scene cameras not spawned for a policy eval; pass it with no names to keep every camera. |
| `--save_hl_overlay_video`, `--hl_overlay_camera` | off, `front_camera` | With `--save_lerobot` and an HL, also record the frame with the HL heatmap and text drawn on it. |
| `--save_hl_latency_video` | off | With `--save_sensor_obs_video` and HL conditioning, a side-by-side of the fresh HL view and the aged one the LL acted on. |
| `--save_expert_video` | off | Extract each episode's expert demonstration video for the W&B episodes table (set by `launch_eval.py --wandb`). |

### Metrics

`--track_metrics`, `--track_joint_metrics` and `--track_ee_metrics` are on by default;
`--save_step_metrics` (per-step CSVs) is off. Contact-force tracking is an env-config
option (`--env-cfg.track-collisions`). See [Metrics](metrics.md) for every metric and
output format.

### Replay

`--replay` and `--replay_clip_stats`; see [Dataset Replay](replay.md).

### TAMPER

`--tamper_output_dir` captures the terminal sim state of every unsuccessful episode as a
vecgen env package, so new expert demonstrations can be planned from those states.
`--tamper_capture_successes`, `--tamper_max_states` and `--tamper_source_env_path` refine
it. See [TAMPER](https://github.com/allenai/ToyBlocks/blob/main/docs/tamper.md).

### W&B

`--wandb` mirrors throughput, per-episode metrics and videos to a W&B run (needs
`WANDB_API_KEY`). `--wandb_project` (default `toyblocks-eval`), `--wandb_entity`,
`--wandb_group` (none by default), `--wandb_name`, `--wandb_job_type`, `--wandb_tags` and
`--wandb_log_interval_seconds` configure it. Pipeline runs leave it off and merge all
workers into one run instead (see [`launch_eval.py` outputs](launch_eval.md#outputs)).

### Debugging

| Flag | Default | Description |
|---|---|---|
| `--debug` | off | t=0 sim-vs-training comparison, per-episode seed logs, and per-step action prints. |
| `--save_diagnostic_plots` | off | Live-rollout diagnostics for the env `video_env_ids` names: policy-input panels in `policy_input_debug/`, HL staleness plot, and server-side LL / HL input traces. The per-step comparison plots are offline: run `scripts/plot_diagnostics_from_eval_run.py --eval-dir <output_dir>` on a `--save_lerobot` run. |
| `--save_first_batch_data` | off | On step 0, have the (ManiFlow) server dump the model-ready batch to `first_batch_data/` for comparison with training. |
| `--enable_viewer` | off | Launch the viser 3D viewer. |

**Policy-input verification** (`--save_diagnostic_plots`) answers "is the policy being
fed what it was trained on?" rather than "did it succeed". For every environment at the
first reset, then for the followed video environment at each episode start, it renders
two PNGs into `policy_input_debug/` from the live obs transform's own output:

- per depth camera: the raw sim depth, the depth the model receives (after
  `process_depth`, optional depth augmentation, point-map Z masking and the centre crop),
  the episode's recorded frame-0 depth, their signed difference and both histograms. A
  constant offset is a calibration or units mismatch; structured residue is a scene
  mismatch.
- the state panel (`*_state.png`): each `agent_pos` dimension against the `[q01, q99]`
  band the server normalizes it into. Dimensions drawn in red are outside the training
  band.

The panels are capability-gated: a run with no policy server, no ManiFlow transform, or
a server that advertises no normalization bands prints why it skipped them and carries
on. On its first inference the server also logs, per depth camera, how much of the
back-projected point map its clamp saturates (`ptmap saturation ...`); high saturation
means the scene sits outside the checkpoint's point-map bounds even when both depth
columns look healthy. The server-side traces (`ll_policy_input_trace/`, and
`hl_policy_input_trace/` for Molmo2) are rendered inside the policy server just before
the model call, one PNG per handover, so they show the tensors the model actually
receives.

## Outputs

Everything is written under `--output_dir`:

| Path | When written |
|---|---|
| `eval_results.json` | Every run: arguments, git checkout, per-episode values and aggregates. |
| `eval_episodes.json` | Every run: one record per episode (prompt, setup, metrics, goal progress, video paths). |
| `step_metrics/env{idx}_episode_NNNN.csv` | `--save_step_metrics` |
| `sensor_obs_videos/` | `--save_sensor_obs_video` |
| `hl_latency_videos/` | `--save_hl_latency_video` |
| `source_episode_videos/` | `--save_expert_video` |
| LeRobot dataset | `--save_lerobot` |
| `policy_input_debug/`, `first_batch_data/`, `scene_verification.json` | The debugging and verification flags above |

See [Metrics](metrics.md) for the fields of the two JSON files. Aggregated results are also
printed at the end of every run:

```text
============================================================
  Evaluation complete  |  episodes: 50  |  time: 312.4s
============================================================
metric                     mean       std       min       max    count
------------------------------------------------------------
return                   0.7854    0.4108    0.0000    1.0000       50
success_once             0.7800    0.4143    0.0000    1.0000       50
...
```

---- FILE: docs_source_user_guide_workflows_evals_launch_eval.md ----

# `launch_eval.py` Reference

[`scripts/launch_eval.py`](https://github.com/allenai/ToyBlocks/blob/main/scripts/launch_eval.py)
is the recommended entry point for evaluation. It does not run anything itself: it turns
its flags into the environment variables of
[`scripts/eval/run_eval_pipeline.sh`](https://github.com/allenai/ToyBlocks/blob/main/scripts/eval/run_eval_pipeline.sh),
the one pipeline that starts the policy server, generates the gym task from the dataset,
serves the episode queue, runs the eval workers and merges the results (see
[Policy Evaluation](../evaluations.md)). This page lists every flag it accepts.

Everything runs as local subprocesses, from your working tree as it is:

- **GPU layout.** GPU 0 runs the policy server and GPUs 1..N run the N eval workers
  (GPUs 0..N-1 under `--replay`, which has no server). With fewer GPUs than that, the
  workers share the visible GPUs round-robin; on a one-GPU workstation the single
  worker shares GPU 0 with the policy server.
- **`--dry-run`** prints the `env VAR=... bash scripts/eval/run_eval_pipeline.sh`
  invocation instead of running it (`--output` writes it to a file), so you can inspect,
  edit and rerun it by hand.
- **Submodules.** Policy evals need the `maniflow-tb` (package `hvla`) and `molmo2`
  (package `olmo`) submodules, installed by the `maniflow` extra (see
  [Installation and setup](../installation_and_setup_instructions.md)). The pipeline
  refuses to start if either is missing, or if `maniflow-tb` is not checked out at the
  commit this checkout pins; fix it with `git submodule update --init maniflow-tb molmo2`.
  `--replay` needs neither.

The gym task is generated from `--dataset-path`: its slug is the dataset directory's
basename with `-` replaced by `_` (gym id `<slug>-v0`), unless `--task-name` overrides it.

Flags are spelled with hyphens (a few also accept an underscore alias), and on/off flags
marked "on" below are turned off with `--no-<flag>`. Only the flags on this page reach
`evaluate.py`; there is no pass-through for other [`evaluate.py` flags](evaluate.md).

## Run profiles

By default a run uses the default profile (the full queue on one eval GPU);
`--smoke-test` switches to a small validation profile. Each value can still be
overridden by its own flag:

| Setting | Default | `--smoke-test` | Flag |
|---|---|---|---|
| Queue size | unlimited | 10 episodes | `--queue-limit` |
| Queue log level | `INFO` | `DEBUG` | `--queue-log-level` |
| Parallel envs per eval GPU | 50 | 2 | `--num-envs` |
| Eval GPUs | 1 | 1 | `--num-eval-gpus` |
| Episode timeout (sim seconds) | 30.0 | 3.0 | `--episode-length-s` |
| Output subdirectory | `evals` | `queue_test` | `--out-subdir` |

Pass `--num-eval-gpus N` to spread the queue over N eval workers (`--policy maniflow`
and `--replay` only; see the limits below).

## Per-policy defaults

`--policy` (or `--replay`) sets these defaults; the matching flags override them:

| Setting | `molmo2_maniflow` (default) | `maniflow` | `--replay` |
|---|---|---|---|
| High level / low level | Molmo2 / ManiFlow (`--ll-oracle`: Molmo2 / motion-planned skills) | symbolic oracle / ManiFlow | recorded actions |
| Policy server | `serve_maniflow_policy --hl model` | `serve_maniflow_policy --hl oracle` | none |
| `--obs-transform` | `maniflow_blocks_table` | `maniflow_blocks_table` | none |
| `--action-horizon` | 25 (0 with `--ll-oracle`) | 25 | 0 |
| `--action-mode` | auto-detected from `config.yaml` | auto-detected | none |
| `--robot-id`, `--scene-preset` | the dataset's recorded provenance | same | same |
| `--center-crop-ratio` | 0.95 | 0.95 | none |
| `--use-oracle` | not applied (Molmo2 is the HL) | on | not applied |

`molmo2_maniflow` needs both `--model-path` (the low-level ManiFlow, also required with
`--ll-oracle`) and `--hl-model-path` (the Molmo2 high level). `maniflow` needs
`--model-path`. `--replay` takes no checkpoint.

**Limits of `molmo2_maniflow`.** Its server accepts a single eval-client connection and
pre-registers 128 HL-latency slots, so the launcher rejects `--num-eval-gpus` above 1
and `--num-envs` above 128. The launcher currently applies this check under `--replay`
too while `--policy` is left at its default, so pass `--policy maniflow` together with
`--replay --num-eval-gpus N`.

## The episode queue

Every eval episode starts from a recorded episode of `--dataset-path`. The pipeline starts
[`scripts/serve_episode_queue.py`](https://github.com/allenai/ToyBlocks/blob/main/scripts/serve_episode_queue.py),
a small HTTP server (port 8001) that loads one setup per dataset episode at startup and
hands them out one at a time. All eval workers pull from this one queue, so each episode
runs exactly once across all GPUs:

```text
LeRobot dataset ──> serve_episode_queue.py ──GET /next──> evaluate.py (worker 1)
                         │                  ──GET /next──> evaluate.py (worker N)
                         └──GET /size──> run_eval_pipeline.sh (sizing)
```

**What a setup holds.** `load_setups` in `utils/episode_dataset.py` builds one setup per
episode from the LeRobot parquet columns. Among other things:

- the episode's `pddl_goal`, and its `hl_prompt` when one is recorded;
- the robot's starting joint and gripper positions, and every block's pose;
- the table height or pose, the camera intrinsics, the block size (`cube_scale`) and friction;
- the expert episode's length and videos, and the frame it starts from (`init_frame_index`).

A trimmed example:

```json
{
  "episode_id": "ep_000001",
  "pddl_goal": "(and (on block_b block_a))",
  "robot_joint_positions": [0.0, -0.785, 0.0, -2.356, 0.0, 1.571, 0.785],
  "robot_gripper_position": 0.04,
  "objects": {
    "block_a": {"position": [0.5, 0.0, 0.05], "quaternion": [1.0, 0.0, 0.0, 0.0]}
  },
  "table_height_delta": 0.0,
  "expert_episode_length": 310
}
```

Whenever environments reset, the worker fetches the next setup for each of them
(`EpisodeQueueClient.fetch_reset_states`) and writes it into the simulation
(`apply_setup`). Joints and objects a setup does not list keep their reset values, but
`apply_setup` raises instead of guessing on a setup/scene mismatch: an object the scene
does not spawn, a missing gripper joint, or a table with neither a recorded pose nor a
height delta. One step later, the worker checks that the simulation state matches the
setup; with `--queue-log-level DEBUG` the client also logs every fetched setup and every
joint and object write.

**Prompt resolution.** The language instruction sent to the policy (and logged as the
episode's `prompt`) is the setup's `hl_prompt` (parquet `goal.hl_prompt`) when present;
otherwise the setup's `pddl_goal` is turned into English by `pddl_goal_to_prompt` (for
example `(and (on block_b block_a))` becomes "put the B block on the A block"). Each environment
gets its own episode's prompt. For `molmo2_maniflow` the same string is the Molmo2 task;
`--hl-prompt "stack 2 blocks"` forces one fixed goal for the whole run.

**Which episodes are queued.**

- `--episode-indices` (with `--allow-duplicate-episodes` to repeat an episode) selects the
  episodes, as `0,3,5,10-19` or `@file.txt` (a file of the same entries). The pipeline
  passes the same selection to task generation and to the queue.
- `--init-after-hl-action` moves each episode's start to just after a given high-level
  action. The robot and block poses, the expert first frames and the
  `--expert-timeout-scale` budget then come from the cut (the remaining expert length).
- `--queue-limit` caps how many are queued.

The queue hands out the longest expert demonstrations first, so the episodes likely to run
longest start early and the last stragglers are short ones.

**Sizing from the queue.** Before starting the workers, the pipeline reads `GET /size`:

- Each worker gets `min(ceil(queue size / --num-eval-gpus), --num-envs)` parallel
  environments, so a small queue does not spawn idle environments.
- With `--expert-timeout-scale`, `episode_length_s` is raised to cover that multiple of
  the queue's longest expert demonstration (`expert_seconds_max`), so each episode's own
  budget is the timeout that binds.

**Block-size slots.** Block size cannot change after spawn, so when the dataset records a
`cube_scale` per episode, the generated task spawns one slot per distinct size and the queue
serves each environment only episodes of its slot's size. A worker spreads its environments
over the slots in proportion to each slot's queued workload, which it reads from `/size`
(`slot_counts`, `slot_expert_frames`). Every fetch also sends the task's slot ordering,
and the queue fails if it differs from its own. That catches a task generated from
different `--episode-indices` than the queue was started with. The queue also refuses to
start if only some of the episodes record a `cube_scale`.

**When the queue drains.** An environment whose fetch comes back empty keeps stepping on
the task's default randomization. These "phantom" episodes are never scored or recorded,
but they still cost policy inference and physics. A worker stops once all of its
environments have drained, and the pipeline prints the queue's final status at the end.

**Endpoints:**

- `GET /next`: `{"setup": ...}`, or `null` once drained. With block-size slots, add
  `?slot=<i>&slot_scales=<s0,s1,...>`.
- `GET /size`: `remaining`, `total`, `expert_seconds_max`, `slot_counts` and
  `slot_expert_frames`. The queue fails at startup if the dataset's `meta/info.json`
  has no `fps`, since `expert_seconds_max` needs it.
- `GET /healthz`: `{"ok": true}`.

## Dataset requirements

A run consumes one artifact, the LeRobot dataset at `--dataset-path`. It is the source of
truth for:

1. **The per-episode setups** above. Each needs at least
   `observation.state.joint_position` and `pddl_goal`; the other columns
   (gripper position, block poses, table pose, friction, intrinsics, ...) are used when
   present.
2. **The gym task.** `generate_task_from_dataset.py` reads the block list from the
   `observation.state.object_pose.<name>` columns and every distinct `pddl_goal`
   (quantified, typed goals such as `(exists (?b1 ?b2 - block_red) ...)` are grounded
   against the scene's blocks). Block names resolve to assets by name: a glyph name
   (`block_a` .. `block_z`, `block_1` .. `block_9`) spawns that glyph block from
   `--usd-library`, a name in `USD_OVERRIDES` (in `tamp/blocks/template/codegen.py`) its
   USD, and anything else a cuboid coloured by the colour word in its name.
3. **The scene.** See [Dataset scene provenance](#dataset-scene-provenance).

If the dataset has `observation.images.*` videos, the queue also resolves each episode's
expert clips, which the W&B episodes table shows next to the rollout.

## Dataset scene provenance

The goal is to rebuild a recorded episode's scene from the dataset path and episode index
alone. The rebuild has two halves: the **scene config** (robot, scene preset, table,
cameras, lighting, physics) comes from code and flags, and the **per-episode state**
(joints, gripper, block poses, table height) comes from the data through `apply_setup`. If
the scene config does not match the one datagen used, the state lands on the wrong scene,
so eval pins the scene to the dataset's recorded provenance:

- Datagen records `scene_id` and `robot_id` (per-step columns, or `meta/info.json`).
  `generate_task_from_dataset.py` bakes them into the generated `env_cfg.py`, and
  `evaluate.py --dataset_path` defaults the eval robot and scene preset to them
  (`reconcile_env_cfg_with_dataset` in `utils/dataset_provenance.py`).
- A dataset that records neither, with no `--robot-id` / `--scene-preset` override, is
  rejected rather than run on a possibly wrong scene. An explicit override that disagrees
  is honoured with a warning; regenerating the task from the dataset (or dropping the
  override) is the usual fix.
- The recorded block heights and `table_height_delta` are relative to the datagen
  preset's table, so `apply_setup` restores the table from `table_pose` (absolute) or
  `table_height_delta` and fails rather than inferring it from block positions.

What each part of the scene is rebuilt from:

| Input | Recorded in the dataset | Used by eval |
|---|---|---|
| Robot joints and gripper | `joint_position`, `gripper_position` | written at reset |
| Block poses | `object_pose.<block>` | written at reset (the block must be spawned) |
| PDDL goal | `pddl_goal` | selects each environment's goal at reset |
| Table height | `table_pose` or `table_height_delta` | written at reset |
| Block size | per-episode `cube_scale` | one spawn slot per distinct size |
| Block and table friction | `block_friction`, `table_friction` | written at reset when recorded |
| `scene_id`, `robot_id` | per-step columns | default the eval scene (see above) |
| Camera intrinsics | `camera_intrinsics.<camera>` | off by default: `--use-calibrated-cameras` uses one fixed sim2real set; `--no-use-calibrated-cameras` applies each episode's recorded intrinsics |
| Camera poses and look | `camera_pose.<camera>`, `meta/render_params.json` on rendered datasets | checked by scene verification; reproduced only with `--use-render-params` |
| Actuator gains | `current_stiffness` / `current_damping` / `current_effort_limit` | read by replay and the dataset PD-switch settle (see [Dataset Replay](replay.md)) |
| Block glyphs and colours | glyph/colour renders: `block_variable_map` / `glyph_map` | painted with `--replay-block-identity` (on) |

## Validating dataset loading

To confirm that the eval scene matches the dataset it was generated from:

- [`scripts/eval/verify_dataset_loading.py`](https://github.com/allenai/ToyBlocks/blob/main/scripts/eval/verify_dataset_loading.py)
  (standalone, needs a GPU) applies each requested episode's setup to a freshly reset
  environment, all in one Isaac session, and writes a scene diff (table height, blocks
  present, block and table poses, block sizes, camera intrinsics and pose), first-frame
  MAE / MSE / SSIM with side-by-side PNGs, and a check of the policy input built from
  the reset observation. It exits non-zero on any hard mismatch; each camera's SSIM has a
  hard floor (`--min-first-frame-ssim`, default 0.90). Generate the task package first:

  ```bash
  python scripts/generate_task_from_dataset.py --dataset-path data/datasets/my_dataset --headless
  python scripts/eval/verify_dataset_loading.py \
      --dataset-path data/datasets/my_dataset --task my_dataset-v0 --episode-indices 0 4 \
      --obs-mode rgb+state --output-dir runs/verify --headless --enable_cameras
  ```

- `evaluate.py --verify_scene` runs the same scene checks on the first batch of queue
  setups during a live eval and writes `scene_verification.json` with comparison PNGs.
  Hard mismatches are only logged; `--verify_scene_strict` aborts the run after the
  report is written. Use strict whenever the numbers will be reported. These two flags
  are not exposed by `launch_eval.py`.

## Evaluating on rendered datasets

The [render stage](../datagen/render.md) gives every episode its own look:

- its own camera offsets, HDRI sky, table material, lights, exposure and backdrop, recorded
  in `meta/render_params.json` (for a merged dataset, one file per source, reached through
  `meta/provenance.json`);
- on glyph and colour renders, its own block letters and colours (`block_variable_map` /
  `glyph_map`).

By default, eval reproduces only the block identities. Everything else is the single
calibrated sim2real scene. Four flags control how much of the recorded look is
reproduced:

| Flag | Default | Effect |
|---|---|---|
| `--use-calibrated-cameras` | on | Fixed sim2real camera intrinsics for every environment; also turns the render replay off. `--no-use-calibrated-cameras` gives each environment its episode's recorded intrinsics instead. |
| `--use-render-params` | off | Reproduce each episode's camera poses (and the wrist camera's mount offset), HDRI sky, table material, lights, exposure and backdrop. Does nothing on datasets without `render_params.json`. |
| `--wave-resets` | off | Start episodes in waves, so all environments in a wave share one episode's lighting (see the caveats below). |
| `--replay-block-identity` | on | Paint each episode's recorded block letters and colours, and prompt the policy with the goal as rendered. Success is always graded on the source block names. `--no-replay-block-identity` keeps the original look and the source-name prompts. |

To evaluate with the full recorded look:

```bash
python scripts/launch_eval.py --policy maniflow \
    --model-path data/checkpoints/my_maniflow_run/checkpoints/steps_400000_model.safetensors \
    --dataset-path data/datasets/my_rendered_dataset \
    --no-use-calibrated-cameras --use-render-params --wave-resets
```

With `--replay`, drop `--wave-resets`, since replay runs a single environment per GPU.

**What the launcher checks** before it starts anything:

- `--use-render-params` needs `--no-use-calibrated-cameras`.
- `--wave-resets` needs `--use-render-params` and more than one environment, so it cannot
  be combined with `--replay` or with calibrated cameras.

**Caveats:**

- **Lighting is shared by the whole scene.** The sky, lights and exposure are one setting
  for all environments. Without `--wave-resets` they are set once at the first reset, so
  with several environments most episodes run under another episode's lighting.
- **Tiled rendering uses one set of intrinsics.** Every environment is drawn with
  environment 0's intrinsics, so an environment whose episode recorded different ones
  reports intrinsics that don't match its pixels.
- **A mismatched record is skipped, not fatal.** An episode whose render record fails the
  lookup checks (the episode count per source problem, the front camera position, the
  table height) runs with nothing applied, and the run carries on.

To check what was applied, look at each episode's `render_replay_status` and
`block_identity_status` (`applied` or `none`) in `eval_episodes.json`; see
[Metrics](metrics.md).

## HL latency

The four HL latency flags decouple the high-level conditioning (the oracle for
`--policy maniflow`, the Molmo2 forward for `--policy molmo2_maniflow`) from per-step
low-level inference, in milliseconds of sim time
(`sim_time_ms = step * step_dt * 1000`; see `src/toyblocks/serving/hl_latency.py`). All
default to 0, which runs the HL on every LL inference with no delay:

- **K** (`--hl-update-interval-ms`): invoke the HL at most once per K ms and buffer its
  output in between. `--hl-update-interval-jitter-ms j` adds `U(-j, +j)` ms to each
  interval to mimic HL timing variance.
- **M** (`--estimated-hl-inference-time-ms`): feed the LL the freshest HL output at
  least M ms old, faking the arm and physics advancing during HL inference.

The Molmo2 server only sees observations at action-chunk boundaries, so a K below
`action_horizon * step_dt` is a no-op there; the client-side oracle buffer ticks every
control step.

**Checkpoints that read the previous front frame.** A ManiFlow checkpoint trained with
`use_previous_front_frame` also takes the aged HL frame as `prev_front_rgb`. There is no
flag for it: the server advertises the input and the client sends it. M and K then have
to match training: the dataloader pairs each frame with one
`n_action_steps * U{1,2,3,4}` steps back (`n_action_steps` is in the checkpoint's
`config.yaml`), while the conditioning age cycles within `[M, M + K]`. So set
`M ≈ n_action_steps * step_dt * 1000` and size K so the age reaches about 4x that. Two
settings print a loud startup warning naming the resulting age (neither is fatal, since
each is also how a synchronous HL is configured on purpose):

- `M = 0`: the conditioning frame is the current one at every chunk boundary.
- K an integer multiple of the action-chunk period (`action_horizon * step_dt * 1000`):
  the HL commits phase-lock with the inferences, so the age is a constant M instead of
  sweeping `[M, M + K)`. Offset K or add jitter to break the lock.

`--save-diagnostic-plots` writes `hl_conditioning_staleness.png` (client-side oracle HL
only), the quickest check of what actually happened: K is the sawtooth period of the
conditioning age and M its floor, and LL calls and HL commits are drawn as event lines.
For the Molmo2 HL, the server-side HL input trace is the equivalent record.

## Outputs

Results go under `RUNS_ROOT`, which defaults to `runs/` in the repository root (set
`RUNS_ROOT=/path` in the environment of `launch_eval.py` to change it). Each eval worker
`N` (seed `N`, from 1) writes to

```text
runs/<task>-v0/<policy>/<out_subdir>/<problem_id>/seed_<N>/<YYYYmmdd_HHMMSS>_local/
```

with `<policy>` from `--policy-name` (`maniflow`, `molmo2_maniflow` or `replay` by
default), `<out_subdir>` from the profile or `--out-subdir`, and `<problem_id>` from
`--problem-id`. Besides the [`evaluate.py` outputs](evaluate.md#outputs)
(`eval_results.json`, `eval_episodes.json`, the LeRobot dataset, videos), each worker
directory holds `launch_params.json` (the resolved launch parameters, including the
commit), `launch_command.sh` (the command line), `std_out_err.log` (the pipeline log
followed by that worker's output) and `skill_success.json` (per-skill success rates from
[`scripts/skill_success_from_eval_run.py`](https://github.com/allenai/ToyBlocks/blob/main/scripts/skill_success_from_eval_run.py)).

At the end, [`scripts/merge_eval_runs.py`](https://github.com/allenai/ToyBlocks/blob/main/scripts/merge_eval_runs.py)
merges the workers into one run directory, `runs/<task>-v0/<policy>/<out_subdir>/<problem_id>/<run_id>/`,
with every worker's episodes in one `eval_episodes.json`, the merged success LeRobot
dataset (moved out of the workers; the failure datasets stay in them) and its own
`skill_success.json`.

With `--wandb`, [`scripts/wandb_consolidate.py`](https://github.com/allenai/ToyBlocks/blob/main/scripts/wandb_consolidate.py)
merges every worker into one W&B run named `<policy>__<task>-v0__<out_subdir>` (needs
`WANDB_API_KEY`). It carries `summary/run_stats_table` (one row of headline numbers:
success rates, episode lengths against the expert's, timeout rate, throughput),
`eval/aggregates_table` (every metric's mean, std, min and max),
`videos/episodes_with_expert_table` (one row per episode, with the expert video next to
the rollout), and, under `--save-diagnostic-plots`, the `debug/policy_inputs_table`,
`debug/ll_policy_inputs_table` and `debug/hl_policy_inputs_table` debugging tables.

## Examples

```bash
# Smoke test of Molmo2 high level + ManiFlow low level (the default policy)
python scripts/launch_eval.py --smoke-test \
    --model-path data/checkpoints/my_maniflow_run/checkpoints/steps_400000_model.safetensors \
    --hl-model-path data/checkpoints/my_molmo2_run \
    --dataset-path data/datasets/my_dataset

# ManiFlow with the high-level oracle, on 4 eval GPUs, logged to W&B
python scripts/launch_eval.py --policy maniflow --num-eval-gpus 4 \
    --model-path data/checkpoints/my_maniflow_run/checkpoints/steps_400000_model.safetensors \
    --dataset-path data/datasets/my_dataset --wandb

# Molmo2 high level + motion-planned skills (low-level oracle), episodes 0-19 only
python scripts/launch_eval.py --ll-oracle \
    --model-path data/checkpoints/my_maniflow_run/checkpoints/steps_400000_model.safetensors \
    --hl-model-path data/checkpoints/my_molmo2_run \
    --dataset-path data/datasets/my_dataset --episode-indices "0-19"

# Start after every flip or rotate, with a per-episode timeout of 1.5x the expert's
python scripts/launch_eval.py --policy maniflow \
    --model-path data/checkpoints/my_maniflow_run/checkpoints/steps_400000_model.safetensors \
    --dataset-path data/datasets/my_dataset \
    --init-after-hl-action flip,rotate --expert-timeout-scale 1.5

# Replay the dataset's recorded actions (no policy server; one cube scale)
python scripts/launch_eval.py --replay \
    --dataset-path data/datasets/my_dataset --episode-indices "0"

# Print the pipeline invocation instead of running it
python scripts/launch_eval.py --dry-run --policy maniflow \
    --model-path data/checkpoints/my_maniflow_run/checkpoints/steps_400000_model.safetensors \
    --dataset-path data/datasets/my_dataset --output /tmp/eval_run.sh
```

## Flags

### Policy and run mode

| Flag | Default | Description |
|---|---|---|
| `--policy` | `molmo2_maniflow` | Policy to evaluate: `molmo2_maniflow` or `maniflow`. |
| `--replay` | off | Replay the dataset's recorded actions instead of evaluating a policy: no policy server, each worker runs `evaluate.py --replay`. Overrides `--policy`; `--num-envs` defaults to and must stay 1. Rejects `--model-path`, `--hl-model-path`, `--oracle-comparison`, `--replicate-noise` and `--init-after-hl-action`. See [Dataset Replay](replay.md). |
| `--replay-clip-stats` | none | With `--replay`: a `stats.json` whose `action.joint_target` q01/q99 bands clamp every replayed arm joint target. Adds `replay_clipped_frames` / `replay_clip_max_rad`. |
| `--smoke-test` | off | Use the smoke-test profile above. |
| `--dry-run` | off | Print the `env VAR=... bash run_eval_pipeline.sh` invocation without running it. |
| `--output` | none | With `--dry-run`: write the invocation to this path instead of stdout. |

### Dataset, task and queue

See [The episode queue](#the-episode-queue) for how these flags shape the queue.

| Flag | Default | Description |
|---|---|---|
| `--dataset-path` | required | LeRobot dataset the queue reads its episode setups from and the gym task is generated from. |
| `--task-name` | dataset basename | Override the gym task slug (a valid Python identifier). |
| `--episode-indices` | all | Episodes to queue, e.g. `0,3,5,10-19` or `@file.txt`. |
| `--allow-duplicate-episodes` | off | Allow repeated indices, e.g. `0,0,0,0,0` with `--num-envs 5` to run episode 0 five times in parallel. |
| `--init-after-hl-action` | none | Start each episode at the first frame after every instance of these high-level actions (comma or `\|` separated, e.g. `flip,rotate`; `flip` also matches `reorient`). Episodes without a match start at frame 0; episodes whose last match is their last frame are skipped. |
| `--queue-limit` | profile | Cap the queue at N episodes. |
| `--queue-log-level` | profile | Log level of the episode queue server. |
| `--usd-library` | `train_blocks_large` | Glyph asset library for bare block names in task generation; `train_blocks` for legacy small-block datasets. |

### Scale and episode budget

| Flag | Default | Description |
|---|---|---|
| `--num-envs` | profile | Maximum parallel environments per eval GPU (the pipeline right-sizes it to the queue). At most 128 for `molmo2_maniflow`. |
| `--num-eval-gpus` | profile (1) | Eval workers, one per GPU after the policy server's (GPU 0). Must be 1 for `molmo2_maniflow`. |
| `--episode-length-s` | profile | Episode timeout in sim seconds. |
| `--expert-timeout-scale` | `0` | Give each episode its own timeout, this multiple of its expert demonstration's length (e.g. `1.5`). The pipeline raises `--episode-length-s` to cover the longest expert in the queue. `0` keeps one shared timeout. |

### Episode end and scoring

| Flag | Default | Description |
|---|---|---|
| `--episode-end` | `goal` | What ends an episode before the timeout: `goal` (the goal predicate; oracle runs: plan completion), `horizon` (nothing), or `ll_done` (a play-mode LL's -1; `--policy maniflow` only). Replay always uses `horizon`. |
| `--collision` | `end` | A non-target block moving more than 2 cm or 15 deg: `end` fails and ends the episode, `penalize` fails it but lets it run on, `off` does not score collisions. |
| `--goal-ori-yaw-tol-deg` | `40.0` | Yaw tolerance of the goal's orientation atoms when judging success. |
| `--post-place-lift` | `0` | After a play-mode LL releases a block, lift the arm this many metres before the next LL query (`0.035` matches datagen). |

### ManiFlow model

| Flag | Default | Description |
|---|---|---|
| `--model-path` | none | ManiFlow `.safetensors` checkpoint (required for `maniflow` and `molmo2_maniflow`). |
| `--config-path` | `<model-path>/../config.yaml` | Model config (for a checkpoint inside `checkpoints/`, the run directory's `config.yaml`). |
| `--stats-path` | checkpoint's own | Normalization `stats.json`; by default the server uses the checkpoint's recorded training stats, else the `stats.json` beside its `config.yaml`. |
| `--train-config-path` | `maniflow-tb/examples/Franka/train_maniflow_multimodal.yaml` | Training config merged under the checkpoint's config; keep it at the pinned `maniflow-tb`. |
| `--action-mode` | auto-detected | `relative` or `absolute`. |
| `--policy-seed` | `0` | Seed of the policy server's action sampling. |
| `--replicate-noise` | off | Start every sample of a batched inference call from the same flow-matching noise, so identical observations give identical actions (`maniflow` only). |

### Molmo2 high-level model

| Flag | Default | Description |
|---|---|---|
| `--hl-model-path` | none | Molmo2 checkpoint (required for `molmo2_maniflow`). |
| `--hl-prompt` | per episode | Force a fixed language goal (e.g. `stack 2 blocks`) instead of each episode's prompt. |
| `--no-hl-prev-action` | off | Never put the previous action in the Molmo2 question (for HL checkpoints trained without it). |
| `--hl-max-new-tokens` | server default | Molmo2 decode budget per answer. |

### High-level conditioning

| Flag | Default | Description |
|---|---|---|
| `--use-oracle` | on | `maniflow` only: drive the task string and target heatmap from the client-side symbolic oracle (`--no-use-oracle` to disable). |
| `--oracle-comparison` | off | `molmo2_maniflow` only: also run a client-side oracle and show it next to the model in the HL overlay video. Needs `--save-hl-overlay-video`. |
| `--async-hl` | off | `molmo2_maniflow` with a play-mode LL: query Molmo2 only at episode start and when the LL ends a skill, instead of at every chunk boundary. |
| `--async-hl-call-scale` | no cap | With `--async-hl`: end an episode once Molmo2 has been called more than this multiple of its expert's HL calls. |
| `--ll-oracle` | off | `molmo2_maniflow`: run Molmo2's commands with the datagen motion-planned skills (cuRobo v2) instead of the served LL. Each command acts on the block nearest its pixel (or the table within 25 px), and Molmo2 is queried again per environment once it ends (implies asynchronous HL queries). |
| `--ll-oracle-hl-call-scale` | `3.0` | With `--ll-oracle`: the same HL call cap. |
| `--go-home` | off | With `--async-hl` or `--ll-oracle`: drive the arm home after a place, flip or rotate, before the next Molmo2 query. |

### HL latency

See [HL latency](#hl-latency) for how to choose K and M.

| Flag | Default | Description |
|---|---|---|
| `--hl-update-interval-ms` | `0` | HL invocation interval K in ms (`0` = every step). |
| `--hl-update-interval-jitter-ms` | `0` | Uniform jitter added to each interval. |
| `--estimated-hl-inference-time-ms` | `0` | Assumed HL inference time M in ms. |
| `--save-hl-latency-video` | off | Per-episode side-by-side of the fresh and the aged HL view (needs `--save-sensor-obs-video`). |

### Observations, transform and scene

See [Evaluating on rendered datasets](#evaluating-on-rendered-datasets) for how the camera,
render and block-identity flags work together.

| Flag | Default | Description |
|---|---|---|
| `--obs-transform` | per policy | Observation transform passed to `evaluate.py`. |
| `--action-horizon` | per policy | Actions applied per policy chunk. |
| `--robot-id` | dataset provenance | Robot config (`--env-cfg.robot-id`). |
| `--scene-preset` | dataset provenance | Scene preset (`--env-cfg.scene-preset-id`). |
| `--center-crop-ratio` | 0.95 for ManiFlow transforms | Centre-crop each resized 224x224 input to `int(224 * ratio)` and resize it back, matching a checkpoint trained with `random_crop_ratio`; `1.0` feeds the full frame. |
| `--enable-crop` | off | ManiFlow transforms only: build `target_front_crop_rgb` on the client. |
| `--use-calibrated-cameras` | on | Use the fixed sim2real camera intrinsics; `--no-use-calibrated-cameras` uses each episode's recorded intrinsics. |
| `--use-render-params` | off | On a rendered dataset, reproduce each episode's camera pose, HDRI, table material, lights, exposure and backdrop. Needs `--no-use-calibrated-cameras`; with `--num-envs > 1` add `--wave-resets`. |
| `--replay-block-identity` | on | On a glyph/colour-rendered dataset, paint each episode's recorded block letters and colours and prompt with the recorded goal. Success is graded on the source block names either way. |
| `--wave-resets` | off | Start episodes in waves, so each wave shares one episode's recorded scene lighting. Needs a rendered dataset and `--num-envs > 1`; not with `--replay` or calibrated cameras. |
| `--eval-table-z-offset` | none | Extra world-frame Z offset (m) for the table and blocks after the queue setup, e.g. `-0.02`. |
| `--replay-gripper-close-target` | none | Override the binary gripper close target (radians). |

### Recording

| Flag | Default | Description |
|---|---|---|
| `--save-lerobot` | on | Record every rollout as a LeRobot dataset, encoded by sharded writer processes as frames arrive. |
| `--lerobot-dataset-name` | run name | Base name of the merged dataset. |
| `--num-shards` | `8` | Parallel LeRobot writer processes, stitched into one success / failure pair at the end. |
| `--video-codec` | `libx264` | `libx264` or `libsvtav1` (about 4x the memory per open stream). |
| `--save-sensor-obs-video` | off | Per-episode MP4s from the RGB observations (buffered in RAM, unlike the LeRobot recording). |
| `--save-hl-overlay-video` | off | Record the HL overlay as a video stream in the LeRobot dataset (needs `--save-lerobot` and an HL). |
| `--save-step-metrics` | off | Per-step metric CSVs in each worker's output directory; for debugging. |

### Diagnostics

| Flag | Default | Description |
|---|---|---|
| `--save-diagnostic-plots` | off | Live-rollout diagnostics: policy-input verification panels, the HL staleness plot, and the server-side LL and HL input traces. Also renders every episode's offline control-diagnostic plots at the end of the pipeline. Implies `--save-first-batch-data` and `--save-lerobot`. |
| `--save-first-batch-data` | off | Dump the model-ready batch the server saw on step 0 to `first_batch_data/` (`maniflow` only). |
| `--deterministic-cuda` | off | Deterministic cuDNN and PhysX enhanced determinism on the server and the workers; slower, and still not bit-for-bit across hardware (see [Policy Evaluation](../evaluations.md)). |

### W&B and output naming

| Flag | Default | Description |
|---|---|---|
| `--wandb` | off | Log the run to W&B, merging every worker into one run. Also extracts each episode's expert video for the episodes table. |
| `--wandb-project` | `toyblocks-eval` | W&B project. |
| `--out-subdir` | profile | Output subdirectory under `runs/<task>-v0/<policy>/`. |
| `--policy-name` | from `--policy` | Policy label used in W&B names and output paths. Currently only the default works: the pipeline also reads this label to choose the policy server, so any other value stops it with `unknown POLICY_NAME`. |
| `--problem-id` | `problem_000000` | `<problem_id>` segment of the output path. |

### Deprecated

| Flag | Description |
|---|---|
| `--legacy-ee-pos` | Rejected with an explanation: `ee_pos` now always comes from the robot config's `ee_body_name`. |

---- FILE: docs_source_user_guide_workflows_evals_metrics.md ----

# Eval Metrics

ToyBlocks records evaluation metrics at three granularities: **per-step**, **per-episode**, and **across-episode**. All metrics flow through a common pipeline and are saved automatically at the end of every eval run.

## Architecture

```text
MetricsTracker          per-step tensors   RecordMetrics         toyblocks.eval.run_eval
(utils/metrics.py)  ──────────────────►  (wrappers/             (run by scripts/evaluate.py)
                       dict[str,            record_metrics.py)    │
                       Tensor[num_envs]]        │                 ├─► eval_results.json (per episode + aggregates)
                                                ├─► CSV per step  └─► eval_episodes.json (one record per episode)
                                                └─► episode summaries
```

### MetricsTracker

[`src/toyblocks/utils/metrics.py`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/utils/metrics.py)

Core per-step metric computation. Instantiated once in `BaseEnv.__init__` when any `track_*` config flag is enabled. Each call to `step()` reads the current simulation state (joint data, EE frame, contact sensor) and returns a flat `dict[str, Tensor[num_envs]]`. All values are scalar-per-environment tensors.

`BaseEnv` merges these tensors into `info["stats"]` via its `evaluate()` method, making them available to downstream wrappers.

### RecordMetrics

[`src/toyblocks/wrappers/record_metrics.py`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/wrappers/record_metrics.py)

A `gym.Wrapper` that sits between the environment and `RecordEpisode`. It does three things:

1. **Episode summaries** -- accumulates per-step stats and, when an episode ends, injects `{key}/mean`, `{key}/min`, `{key}/max`, and `{key}/final` into `info["final_info"]["episode"]`.
2. **Goal-progress summaries** -- the boolean goal stats (`goal_conj_<c>`, `goal_success`, `goal_blocks_settled`, `goal_gripper_open`; see "Goal-progress metrics" below) also get `{key}/initial` and `{key}/first_true_step`. They are also traced step by step and attached to the finished episode as change points (`info["final_info"]["goal_trace"]`, `[[step, value], ...]`, starting with `[1, initial]`). Both are timed with the env's episode clock (`episode_length_buf`), which eval stops during hold steps (PD-switch settles, chunk-boundary waits, wave parking), so they line up with `first_success_step` and `episode_len`.
3. **Per-step CSVs** -- when an `output_dir` is provided (`evaluate.py` passes one only with `--save_step_metrics`), buffers every step's stats and writes one CSV file per completed episode to `<output_dir>/step_metrics/`, named `env{idx}_episode_NNNN.csv` where `{idx}` is the sub-environment index and `NNNN` is a per-env episode counter. In queue-driven evals, the CSVs of "phantom" episodes (an env auto-reset after the queue drained) are dropped, as their videos and trajectories are.

### The eval loop

[`scripts/evaluate.py`](https://github.com/allenai/ToyBlocks/blob/main/scripts/evaluate.py) parses the arguments ([`src/toyblocks/eval/args.py`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/eval/args.py)) and runs the eval loop in [`toyblocks.eval.run_eval`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/eval/run_eval.py). When an episode finishes, the loop adds its own episode metrics (collisions, oracle and high-level counters, replay divergence, ...) to the summaries from `RecordMetrics`. At the end of the run it writes:

- **`eval_results.json`** (`_save_results` in `utils/dataset_recording_utils.py`) -- the raw value of each episode metric as a JSON list, plus mean, std, min, max, and count for every metric across episodes.
- **`eval_episodes.json`** (the episode table in `utils/wandb_logging.py`) -- one record per episode with its prompt, source-episode provenance, metrics, goal progress and video paths (fields listed under "eval_episodes.json" in [Output format](#output-format)). The same records make up the W&B episodes table.

A single `evaluate.py --wandb` run logs its own W&B run. Pipeline runs instead merge every worker's `eval_episodes.json` and `eval_results.json` into one W&B run through [`scripts/wandb_consolidate.py`](https://github.com/allenai/ToyBlocks/blob/main/scripts/wandb_consolidate.py), which logs an episodes table with the expert videos and a goal-progress plot per episode, an aggregates table and the headline metrics, and the offline diagnostic plots of one representative episode per worker.

## Available metrics

### Episode metrics

Always recorded when `record_metrics=True` (the default in `BaseEnvCfg`). These appear in `info["final_info"]["episode"]`.

| Key | Description |
|---|---|
| `return` | Cumulative reward over the episode |
| `episode_len` | Number of steps in the episode |
| `reward` | Mean reward per step (`return / episode_len`) |
| `success_once` | Whether the task succeeded at any point during the episode |
| `success_at_end` | Whether the task was in a success state at the final step |
| `first_success_step` | Episode step at which the task first succeeded (NaN if it never did) |
| `fail_once` | Whether a failure state was reached at any point |
| `fail_at_end` | Whether the task was in a failure state at the final step |

### Eval-loop metrics

Added per episode by `toyblocks.eval.run_eval`, only in the runs where they apply:

| Key | When | Description |
|---|---|---|
| `collision`, `collision_count` | `--collision end` (default) or `penalize` | Whether, and how many times, a non-target block moved more than 2 cm or 15 deg. A collision fails the episode: `success_once` and `success_at_end` are forced to false. |
| `success_once_ignore_collision`, `success_at_end_ignore_collision` | `--collision penalize` | The two successes before the collision penalty. `--collision off` scores no collisions at all. |
| `sub_goals`, `sub_goal_success` | Oracle and Molmo2 runs | Per sub-goal, in order: its name and whether it succeeded (`sub_goal_success_ignore_collision` too under `penalize`). The aggregate gets a rate per skill: `sub_goal_success_pick`, `_place`, `_flip`, `_rotate`. |
| `hl_done` | Learned-HL runs | Whether the HL model emitted its `done` token during the episode |
| `hl_calls` | Learned-HL runs | Number of HL model queries in the episode |
| `oracle_done` | Oracle-HL runs | Whether oracle plan completion ended the episode |
| `oracle_success_backstop` | Oracle-HL runs | Whether 10 consecutive successful steps ended the episode instead |
| `oracle_stuck` | Oracle-HL runs, or with a comparison oracle | Whether the oracle plan got stuck. It ends the episode for the oracle HL; a comparison oracle only flags it. |
| `ll_oracle_failures` | `--ll-oracle` runs | Skills the low-level oracle could not execute (no feasible parameters, a failed motion plan, an effect that did not hold); Molmo2 is asked again each time |
| `ll_skill_stops`, `ll_pause_steps` | Play-mode LL checkpoints | Number of times the LL predicted play mode -1 (stop), and number of steps it predicted 0 (pause) |
| `partial_progress` | Autogen PDDL tasks | `(final - initial) / (total - initial)` over the goal conjuncts, in `[-1, 1]`; NaN when the goal already held at the start |
| `replay_*` | `--replay` | Divergence from the recording; see [Dataset Replay](replay.md#replay_-metrics) |
| `render_replay_status`, `block_identity_status` | Render replay, `--replay_block_identity` | Whether the episode's recorded render parameters and block letters/colours were applied. In `eval_episodes.json` only. |

On learned-HL runs (`--policy molmo2_maniflow`) the HL model owns termination: its `done` token ends the episode, and an episode without a `done` runs out `episode_length_s` instead of stopping on goal-success. So `success_once && !hl_done` identifies episodes where the goal was reached but the HL model failed to call it. Under the default `--episode_end goal`, oracle-HL runs end on oracle plan completion or after success holds for 10 consecutive steps, and plain LL, random and zero-action paths end on instant goal-success. `--episode_end horizon` runs every episode to `episode_length_s`. `--episode_end ll_done` (play-mode LL checkpoints, no learned HL) ends an episode when the LL predicts play mode -1, or at `episode_length_s`; `success_at_end` then says whether the goal still holds and `ll_skill_stops` (1 vs 0) whether the LL stopped or timed out. Replay always uses `horizon`. Instead of the single `episode_length_s` timeout, `--expert_timeout_scale` (`--expert-timeout-scale` on the launcher) ends each queue episode after that multiple of its own expert demonstration's duration.

### Goal-progress metrics

Autogen PDDL tasks (generated by `tamp/blocks/template/codegen.py`) report goal progress as per-step boolean stats:

| Key | Description |
|---|---|
| `goal_conj_<c>` | Whether conjunct `<c>` of the episode's PDDL goal holds, e.g. `(on block_x block_w)` |
| `goal_success` | Whether the whole goal holds, including the settle gate below |
| `goal_blocks_settled`, `goal_gripper_open` | The settle gate's terms: the goal blocks have stopped moving and the gripper is open |

Each gets the usual `/mean`, `/min`, `/max`, `/final` summaries plus `/initial` and `/first_true_step` (see `RecordMetrics` above). In `eval_episodes.json`, each record also gets:

- `goal_progress`: one entry per goal conjunct, with its `predicate` text, its `initial`, `first_true_step`, `final`, `max` and `mean` values, and its change-point `trace`.
- `num_goal_conjuncts`, `num_goal_conjuncts_initial`, `num_goal_conjuncts_final`, `num_goal_conjuncts_ever`: the number of conjuncts in total, true at the start, true at the end, and true at some point.
- `goal_success_trace` (and `goal_blocks_settled_trace` / `goal_gripper_open_trace` when traced).

### Joint metrics

Enabled by `--track_joint_metrics` or `--track_metrics` (both on by default in `evaluate.py`).

| Key | Description |
|---|---|
| `joint_pos_norm` | L2 norm of the joint position vector |
| `joint_vel_norm` | L2 norm of the joint velocity vector |
| `joint_accel_norm` | L2 norm of the joint acceleration vector (finite-differenced from velocity) |
| `joint_effort_norm` | L2 norm of applied torques (when available) |
| `joint_pos/{name}` | Position of individual joint (one column per joint, e.g. `joint_pos/panda_joint1`) |
| `joint_vel/{name}` | Velocity of individual joint |
| `joint_accel/{name}` | Acceleration of individual joint |
| `joint_effort/{name}` | Applied torque on individual joint |

### End-effector metrics

Enabled by `--track_ee_metrics` or `--track_metrics` (both on by default in `evaluate.py`). Requires a `FrameTransformer` sensor for the EE (configured automatically for supported robots).

| Key | Description |
|---|---|
| `ee_pos_x`, `ee_pos_y`, `ee_pos_z` | World-frame EE position components |
| `ee_quat_w`, `ee_quat_x`, `ee_quat_y`, `ee_quat_z` | World-frame EE orientation as a quaternion (w, x, y, z) |
| `ee_vel_norm` | L2 norm of EE linear velocity (finite-differenced from position) |
| `ee_accel_norm` | L2 norm of EE linear acceleration |

### Collision metrics

Enabled by the env-config option `--env-cfg.track-collisions` (it is not an `evaluate.py` flag, and `launch_eval.py` does not expose it). Adds an Isaac Lab `ContactSensor` to every robot body, which increases VRAM usage. These contact forces are separate from the block-displacement `collision` metric above.

| Key | Description |
|---|---|
| `contact_force_norm` | Sum of per-body contact force norms across all robot bodies |
| `bodies_in_contact` | Number of robot bodies with contact force above the sensor threshold |
| `env_collision_count` | Cumulative count of body-in-contact events over the episode |
| `self_collision_count` | Cumulative count of self/filter-pair contacts (requires filter paths) |
| `contact_force/{body}/x,y,z` | Per-body 3D net contact force in world frame (e.g. `contact_force/panda_link3/x`) |
| `contact_pair/{body}/{filter}/x,y,z` | Per (body, filter-object) pair 3D force. Only available when `--env-cfg.collision-filter-prim-paths` is set. Filter name is the last path segment (e.g. `contact_pair/panda_link7/Block/z`). |

### Task-specific metrics

Individual tasks add their own metrics by overriding `evaluate()`. These appear under `stats/` in `eval_results.json`. For example, the **Lift** task adds:

| Key | Description |
|---|---|
| `object_to_goal_dist` | L2 distance from the object to the goal position |
| `object_to_tcp_dist` | L2 distance from the object to the end-effector |

The align, flip, isolate, push-stacked and rotate tasks add `object_to_tcp_dist` too.

## Output format

Every run writes both JSON files; `step_metrics/` is written only with `--save_step_metrics`:

```text
runs/<run_name>/
├── eval_results.json
├── eval_episodes.json
└── step_metrics/
    ├── env0_episode_0000.csv
    ├── env0_episode_0001.csv
    ├── env1_episode_0000.csv
    └── ...
```

### eval_results.json

```text
{
  "toyblocks_commit": "...",
  "toyblocks_branch": "...",
  "toyblocks_dirty": false,
  "submodule_commits": { ... },
  "args": { ... },
  "num_episodes": 10,
  "elapsed_seconds": 42.3,
  "per_episode": {
    "return": [1.2, 0.8, ...],
    "success_once": [1.0, 0.0, ...],
    "stats/ee_pos_x/mean": [0.61, 0.59, ...],
    ...
  },
  "per_episode_goal_conjuncts": [["(on block_x block_w)", ...], ...],
  "metrics": {
    "return": { "mean": 0.95, "std": 0.21, "min": 0.3, "max": 1.5, "count": 10 },
    "stats/joint_vel_norm/mean": { "mean": 0.12, "std": 0.03, ... },
    ...
  }
}
```

- `toyblocks_commit`, `toyblocks_branch`, `toyblocks_dirty` and `submodule_commits` record the checkout the run used (the dirty check ignores submodules).
- `per_episode` -- one list per metric key, where element *i* is the value for episode *i*.
- `per_episode_goal_conjuncts` -- for autogen PDDL tasks, the PDDL text of each `goal_conj_<c>` of episode *i* (`null` for episodes without goal labels).
- `metrics` -- across-episode aggregates (mean, std, min, max, count) for every metric key. The aggregation is NaN-safe, so NaN values (e.g. `first_success_step` of a failed episode) are left out.
- `success_efficiency` -- Molmo2 HL runs only: the mean, over successful episodes, of the HL commands the eval took divided by the commands the source demonstration took.

Episode-level stat keys are prefixed with `stats/` and suffixed with the aggregation (`/mean`, `/min`, `/max`, `/final`). For example, `stats/ee_pos_x/mean` is the mean of `ee_pos_x` over all steps in a single episode.

### eval_episodes.json

A JSON list with one record per scored episode, built by `EpisodeResultsTable` in `utils/wandb_logging.py`. It is written at the end of every run and rewritten once the LeRobot recorder has closed, when the output episode indices are known. Fields that do not apply to a run are `null` or absent.

```text
[
  {
    "sim_env_idx": 0,
    "episode_idx_for_sim_env": 0,
    "prompt": "put the red block on the blue block",
    "pddl_goal": "(and (on block_x block_w))",
    "source_dataset_path": "data/datasets/my_dataset",
    "source_dataset_episode_idx": 12,
    "expert_episode_length": 310,
    "init_frame_index": 0,
    "success_once": 1.0,
    "episode_len": 287,
    "collision": 0.0,
    "goal_progress": [{"index": 0, "predicate": "(on block_x block_w)", "initial": 0.0, "first_true_step": 241, ...}],
    "num_goal_conjuncts": 1,
    "partial_progress": 1.0,
    "step_dt_s": 0.04,
    "video_path": ".../sensor_obs_videos/env0_episode_0000.mp4",
    "output_lerobot_dataset_dir": ".../my_eval_success",
    "output_lerobot_episode_index": 0,
    ...
  },
  ...
]
```

| Group | Fields | Description |
|---|---|---|
| Identity | `sim_env_idx`, `episode_idx_for_sim_env` | The sub-env index and its per-env episode counter: the same pair that names the videos and step-metric CSVs. |
| | `output_lerobot_dataset_dir`, `output_lerobot_episode_index` | With `--save_lerobot`: the recorded dataset (success or failure split) and the episode's index in it. |
| Task | `prompt`, `pddl_goal` | The language prompt the policy received and the episode's PDDL goal. |
| Source episode | `source_dataset_path`, `source_dataset_episode_idx`, `source_dataset_episode_id` | Queue evals: the dataset episode the eval was initialized from. |
| | `expert_episode_length`, `expert_episode_seconds` | Length of that expert demonstration, in frames and seconds. |
| | `init_frame_index`, `init_after_hl_action` | The source frame the eval started from: 0 unless the queue was told to start after a given high-level action. |
| | `expert_videos`, `expert_video_path`, `expert_video_start_s` | Per-camera clip metadata of the expert demonstration, and the path and start time of the front-preferred camera's clip. |
| Metrics | the episode and eval-loop metrics | Every key of the result table (success, length, collision, sub-goal, oracle, HL and play-mode counters, status fields; see "Episode metrics" and "Eval-loop metrics" in [Available metrics](#available-metrics)), plus every `replay_*` scalar. |
| Goal progress | `goal_progress`, `num_goal_conjuncts*`, `partial_progress` | Autogen PDDL tasks: one entry per goal conjunct (`index`, `metric_key`, `predicate`, `initial`, `first_true_step`, `final`, `max`, `mean`, `trace`) and the counts derived from them; see "Goal-progress metrics" above. |
| | `goal_success_trace`, `goal_blocks_settled_trace`, `goal_gripper_open_trace` | Change points `[[step, value], ...]` over the episode clock. |
| | `goal_objects`, `step_dt_s` | The goal's blocks, in the order of the per-block settle-gate stats, and the control period (to convert steps to seconds). |
| Videos | `video_path` | The sensor-observation MP4 (`--save_sensor_obs_video`). |
| | `source_episode_video_path` | The extracted expert video (`--save_expert_video`, or `--wandb`). |
| | `hl_overlay_prev_action_video_path`, `hl_latency_video_path` | The HL overlay and HL latency videos, when written. |
| Other | `episode_seconds` | W&B runs only: `episode_len` divided by the video frame rate. |
| | `policy_input_*` | With `--save_diagnostic_plots`: paths of the policy-input verification panels. |

The per-camera expert first frames shown in the W&B table are left out of the JSON.

### Per-step CSVs

Each CSV has one row per simulation step and one column per metric. The first column is `step` (0-indexed). All values are raw floats from that step.

```text
step,joint_pos_norm,joint_vel_norm,...,ee_pos_x,ee_pos_y,...,contact_force_norm,...
0,3.118,1.039,...,1.612,-1.001,...,0.0,...
1,3.143,1.310,...,1.607,-1.005,...,0.0,...
```

When running with `num_envs > 1`, each sub-environment gets its own set of CSVs named `env{idx}_episode_NNNN.csv`, where `{idx}` is the env index and `NNNN` is a per-env episode counter that increments each time that env finishes an episode. If the evaluation ends mid-episode, partial files are saved with a `_partial` suffix.

## CLI flags

| Flag | Default | Description |
|---|---|---|
| `--track_metrics` | on | Enable both joint and EE metrics (equivalent to `--track_joint_metrics --track_ee_metrics`) |
| `--track_joint_metrics` | on | Track per-step joint position, velocity, acceleration, and effort |
| `--track_ee_metrics` | on | Track per-step end-effector position, orientation, velocity, and acceleration |
| `--save_step_metrics` | off | Write the per-step CSVs. Off by default: they cost a host copy of every stat on every step, and the episode summaries do not depend on them |
| `--collision` | `end` | Block-displacement collision scoring: `end`, `penalize` or `off` (see "Eval-loop metrics" above) |

The contact-force metrics are configured through env-config fields (`BaseEnvCfg` in `src/toyblocks/tasks/base_env_cfg.py`), set with `--env-cfg.<field>`:

| Env-config option | Default | Description |
|---|---|---|
| `--env-cfg.track-collisions` | off | Track per-step collision forces and counts. Adds a `ContactSensor` to the scene (increases VRAM) |
| `--env-cfg.collision-filter-prim-paths` | none | Prim path expressions for collision filter targets (e.g. `'{ENV_REGEX_NS}/Block'`). Only used with `track-collisions` |
| `--env-cfg.collision-filter-body-names` | none | Robot body names to create per-body filter sensors for (e.g. `panda_link7 panda_link8`). Required together with `collision-filter-prim-paths` to get `contact_pair/` metrics. Each listed body gets a lightweight single-body contact sensor |

`--track_metrics` is OR-ed with the two finer flags, so to turn joint and EE tracking off pass all three negations: `--no-track_metrics --no-track_joint_metrics --no-track_ee_metrics`.

Example with zero actions (no policy server needed, useful for sanity-checking metrics collection):

```bash
uv run python scripts/evaluate.py \
    --task ToyBlocks-Lift-v0 \
    --env-cfg.track-collisions \
    --env-cfg.collision-filter-prim-paths '{ENV_REGEX_NS}/Block' \
    --env-cfg.collision-filter-body-names panda_link7 panda_link8 \
    --save_step_metrics \
    --num_envs 4 --num_eval_steps 200
```

The same options apply to a run against a policy server; see the
[`evaluate.py` Reference](evaluate.md#running-against-a-policy-server-by-hand).

## How to extend

### Add a task-specific metric

Override `evaluate()` in your task environment. Call `super().evaluate()` first so that `MetricsTracker` stats are included, then add your own entries to the `stats` sub-dict.

```python
def evaluate(self) -> dict:
    result = super().evaluate()
    stats = result.setdefault("stats", {})
    stats["my_distance"] = torch.linalg.norm(
        self.object.data.root_pos_w - self.target_pos, dim=-1
    )
    return result
```

The value must be a `[num_envs]` tensor. It will automatically appear in the per-step CSVs and episode summaries.

### Add a new MetricsTracker category

1. Add a boolean flag to `BaseEnvCfg` (in `src/toyblocks/tasks/base_env_cfg.py`):

```python
track_my_sensor: bool = False
```

2. Add a corresponding `--track_my_sensor` field to the `Args` dataclass in `src/toyblocks/eval/args.py` and wire it into the env config in `_make_env` (`src/toyblocks/utils/dataset_recording_utils.py`), next to `track_joint_metrics`.

3. In `MetricsTracker.__init__`, initialize any buffers gated on the new flag.

4. Add a `_compute_my_sensor_metrics()` method that returns `dict[str, Tensor[num_envs]]`.

5. Call it from `MetricsTracker.step()`:

```python
if self._track_my_sensor:
    stats.update(self._compute_my_sensor_metrics())
```

6. If the sensor needs setup during scene creation, add the initialization logic to `BaseEnv._setup_scene()` (similar to how `ContactSensor` is added when `track_collisions` is `True`).

---- FILE: docs_source_user_guide_workflows_evals_replay.md ----

# Replaying Actions from a Dataset

Replay plays a LeRobot dataset's recorded actions back through the **same
queue-driven eval loop a policy uses** (`toyblocks.eval.run_eval._run_eval`).
There is no separate replay runner any more: `--replay` is just another action
source next to a policy server, random or zero actions.

What replay measures is the *open-loop ceiling* of the sim: replaying the
expert's own actions from the recorded initial state reports both the usual
eval metrics (`success_once`, `episode_len`, ...) and per-episode divergence
from the recording (`replay_*` metrics).

## Quickstart

```bash
# One eval GPU, episodes 0-39 of a merged LeRobot root (all of one cube scale)
python scripts/launch_eval.py --replay \
    --dataset-path data/datasets/my_flip_dataset \
    --episode-indices "0-39" \
    --save-diagnostic-plots --deterministic-cuda
```

`--num-envs` stays at 1 and the LeRobot recording is on by default. To replay on several
GPUs, add `--num-eval-gpus N`; the launcher currently also needs `--policy maniflow`
alongside it, because its one-GPU check for the default `molmo2_maniflow` policy runs
under `--replay` too.

`--replay` selects `POLICY_NAME=replay` in
[`scripts/eval/run_eval_pipeline.sh`](https://github.com/allenai/ToyBlocks/blob/main/scripts/eval/run_eval_pipeline.sh):
the policy server is skipped, the autogen task is generated from the dataset,
the episode queue is started, and each eval worker runs

```bash
python scripts/evaluate.py --task <slug>-v0 --replay \
    --queue_url http://localhost:8001/next --dataset_path <root> \
    --control_mode arm_joint_gripper_binary --obs_mode rgb+state --num_envs 1 --headless
```

Output lands under `runs/<task>-v0/replay/<out_subdir>/...` like any other eval (see
[`launch_eval.py` outputs](launch_eval.md#outputs))
(`eval_episodes.json`, `eval_results.json`, videos, the optional LeRobot
recording), so the offline diagnostics
([`scripts/plot_diagnostics_from_eval_run.py`](https://github.com/allenai/ToyBlocks/blob/main/scripts/plot_diagnostics_from_eval_run.py))
work unchanged.

Add `--dry-run` to print the pipeline invocation instead of running it.

## How it works

| Piece | Where | Role |
|---|---|---|
| Initial state | `apply_setup` (`utils/episode_queue.py`) via the queue setup | Robot joints, gripper, objects, table height, friction, `pddl_goal`, cube-scale slot. Under `--replay` the recorded frame-0 arm joint **velocity** is restored too (`setup["robot_joint_velocities"]`). |
| Actions | `ReplayPolicy` (`eval/replay.py`) | Emits a 9-dim action per step: 7 recorded joint targets, binary gripper command, and the recorded `action.pd_mode` as the 9th channel. |
| Gains | `PDModeController` (`eval/pd_mode_controller.py`) | The pd_mode channel drives the same controller a policy's prediction would. Whenever a ground-truth `--dataset_path` is given, a mode switch settles for the TAMP tick counts `DATASET_SWITCH_SETTLE_TICKS = (5, 10)` (compliant/stiff) with the arm frozen and the finger target active. The settle runs as per-env hold steps (`DeferredSettle`) that the policy, the recording and the episode clock never see. Initial writes at reset never settle. |
| Skipped ticks | `ReplayPolicy.pop_gap_holds` (`eval/replay.py`) | Where the recording skipped control ticks (detected by `_detect_unrecorded_ticks` from the recorded joint velocities and timestamps), the previous row's action is held for that many ticks before the next row runs, so the sim stays in step with the recording. Uses the same hold steps as the settle. |
| Termination | `ReplayPolicy.done_indices()` → `base_env.request_episode_end` | The episode ends on the step that applies the last recorded action; `episode_end` is forced to `horizon` and `episode_length_s` is raised to cover the longest recording. |
| Divergence | `ReplayPolicy.record_divergence()` / `episode_metrics()` | Joint error vs the recorded row, per-object position / quaternion error, pre/post PD-switch phases. Scalars only, folded into the episode metrics under `replay_*`. |

## `replay_*` metrics

Per episode (in `eval_episodes.json`; aggregated in `eval_results.json` and the
wandb episodes table):

- `replay_num_frames`, `replay_profile_switch_frame` (NaN when no switch),
  `replay_unrecorded_ticks` (control ticks the recording skipped; see "Skipped ticks"
  above)
- `replay_joint_pos_error_{mean,max,final}`,
  `replay_{pre,post}_switch_joint_pos_error_{mean,max,final}`
- `replay_object_<name>_{pos,quat}_error_{mean,max,final}`,
  `replay_{pre,post}_switch_object_<name>_{pos,quat}_error_{mean,max,final}`
- With `--replay_clip_stats` only: `replay_clipped_frames`, `replay_clip_max_rad`
  (see [Clipping replayed targets](#clipping-replayed-targets)).

Any metric without data is `NaN`; the aggregation is NaN-safe.

## Clipping replayed targets

`--replay_clip_stats <stats.json>` (`--replay-clip-stats` on `launch_eval.py`)
clamps every replayed arm joint target to the `action.joint_target` q01/q99
bands of that `stats.json`, for example a ManiFlow run's. It answers whether a
policy whose labels were clipped to those bands could still succeed, and adds
the per-episode metrics `replay_clipped_frames` and `replay_clip_max_rad`. It
only applies to `--replay` and raises otherwise.

## Requirements and failure modes

- **`--num_envs 1`.** `ReplayPolicy` advances every env's recording on each
  step, so it cannot hold one env through a PD-switch settle while the others
  move on. Replay therefore runs one env per worker (use `--num-eval-gpus` for
  parallelism). If the autogen task bakes several cube-scale slots,
  `reconcile_num_envs_with_task` raises `num_envs` and `evaluate()` errors
  out — restrict `--episode-indices` to episodes of a single cube scale, or
  use a task whose package bakes one slot.
- **`--control_mode arm_joint_gripper_binary`** — datagen records absolute
  joint targets, and the deferred settle holds the arm with absolute joint
  targets, so any run with `--dataset_path` (replay or policy eval) raises
  under another control mode. The pipeline sets this; pass it yourself when
  calling `evaluate.py` directly.
- **The dataset must record `action.pd_mode`** and the gain columns
  (`observation.state.current_stiffness` / `current_damping` /
  `current_effort_limit`). Missing gains fail at startup
  (`load_pd_gains_from_dataset`); a missing or all-NaN `action.pd_mode` fails
  when the episode is loaded (`ReplayPolicy.on_reset`).
- `replay_gripper_close_target` defaults to `0.72` (TAMP datagen's Robotiq close
  target); override with `--env-cfg.replay-gripper-close-target`.
- `apply_setup` is strict: a setup without a table pose / height delta, or
  referencing an object the scene does not spawn, raises instead of warning.

## Behavior notes

- Gain *values* are the dataset-wide stiff/compliant vectors from
  `load_pd_gains_from_dataset` (first parquet chunk, one representative vector
  per mode), not the exact per-frame recorded ones; joint velocity limits are
  not written. Identical for datasets recorded under two fixed profiles. When
  the dataset has no frames of one mode, that mode falls back to the ToyBlocks
  defaults.
- The 5/10-tick settle is a fixed convention (settle steps are not recorded in
  the source dataset). It applies to policy evals with a `--dataset_path` as
  well, so a pd_mode switch in a policy eval also settles.
- The LeRobot recorder (the same one datagen uses) pairs each row's observation
  with the action applied next, so a replay recording has the same row layout
  as the dataset it replays.

## Historical note

The former standalone path (`--replay_lerobot_dataset`, `--replay_dataset_path`,
`--max_replay_episodes`, `replay_results.json`, `replay_plots/`, comparison
videos) has been removed.
[`scripts/extract_lerobot_episode.py`](https://github.com/allenai/ToyBlocks/blob/main/scripts/extract_lerobot_episode.py)
and the side-by-side video helpers in `utils/tamp_dataset.py` remain for offline
inspection but are no longer used by eval.

---- FILE: docs_source_user_guide_workflows_evaluations.md ----

# Policy Evaluation

The evaluation system measures how well a trained policy performs in closed loop in
simulation, on scenes and tasks automatically generated by the datagen system. 

The evaluation system runs on your machine, from a workstation with a single GPU to a
multi-GPU machine that evaluates hundreds of episodes at a time spread over several GPUs.
It uses a queue to distribute episodes over GPU-parallel simulation environments in
IsaacSim/IsaacLab. It works with any policy that can be served over a WebSocket, such as
a hierarchical VLA.

Each evaluation episode can start from a randomly-generated unseen scene and task definition
or from the scene and task definition of an episode already recorded in a 
dataset (with the same robot pose, block poses, block sizes, table height and goal).
The policy has to reach the task's goal from that initial state. Because the eval scene can be 
rebuilt and initialized from a dataset episode, success metrics are indicative of policy performance
rather than of differences between the training and eval setups.

## What you can do with it

- Benchmark ManiFlow (low-level) policies, alone or under a Molmo2 (high-level) policy,
  on the episodes of a dataset.
- Run ablations that replace the high-level or the low-level policy with an oracle, to 
  help isolate where errors might be coming from.
- Replay the expert actions recorded in a dataset in an open-loop fashion, as a sanity 
  check of the simulation settings, the dataset, and the evaluation system overall.
- Plug in a new model by implementing a small policy-server interface.
- Capture the episodes on which a policy failed and send them back to data generation, which
  plans new expert demonstrations and recovery behaviors from those states
  ([TAMPER](https://github.com/allenai/ToyBlocks/blob/main/docs/tamper.md)).

## Design goals for our evaluation system

- **Scalability and GPU parallelization.** An eval runs many episodes at once at two
  levels. On one GPU, many parallel environments (up to 50 per GPU by default) live in
  one Isaac scene, and the policy server answers rollout requests from all of them with
  one GPU-batched inference call. Across GPUs, several eval workers (`--num-eval-gpus`)
  pull episodes from a single episode queue, so adding GPUs adds throughput without
  changing which episodes are evaluated. (The Molmo2 + ManiFlow server accepts a single
  eval worker, so it scales through environments only.)
- **Reproducible statistically rather than bit-by-bit.** Every episode starts from a 
  randomly-generated unseen scene and task or from the scene and task in a recorded 
  dataset episode, handed out by an episode queue. Seeds are fixed. A
  rerun therefore gives the same success rates within some noise. Individual
  trajectories, however, are *not* guaranteed to match bit-for-bit between runs. Sharing 
  one physics scene across environments is what makes this evaluation system fast, 
  but it is also the main reason results are not bit-for-bit reproducible (see reasons below).
- **One pipeline from one GPU to many.** The same evaluation pipeline runs a smoke test
  on a one-GPU workstation and a full evaluation over several GPUs; only the profile
  flags change.
- **Faithful to data generation.** When the eval scene (robot, scene preset, table height,
  block sizes, cameras) is taken from an existing episode in a dataset, provenance is recorded, 
  and a scene verification step compares the eval scene against the recording before
  any numbers are reported.
- **Model-agnostic.** Any policy that implements the `BasePolicy` interface can be
  served over WebSocket. Observation transforms convert the simulator's observations
  into the format each model expects, so the eval client is the same for every model.
- **Decomposable.** Policies that are split into a high-level part (which decides
  what to do next, e.g. "pick the red block") and a low-level part (which moves the
  arm) can have either part replaced by an oracle. This isolates whether a failure
  comes from the high-level decision or from its execution.
- **Easy definition of metrics.** A new metric is one tensor with one value per
  environment, added in the task's `evaluate()`. Per-episode summaries, aggregates
  across episodes, per-step CSVs and Weights & Biases (W&B) tables are produced
  automatically, with no additional logging code. See
  [Metrics](evals/metrics.md)
  for the built-in metrics and how to add your own.
- **Automatic definition of partial progress metrics** Each scene and task definition
  contains a PDDL logical goal that is defined over a set of logical predicates over the
  objects in the scene. We leverage this to measure how many predicates of the logical goal
  specification have been achieved at a particular point in an episode. Counting how many of
  these goal predicates are successful allows us to automatically have a partial progress metric
  estimated for every episode, without the need to write custom code. Moreover, the partial progress
  metrics are measured the same way for all tasks.
- **Diagnosable.** Runs can produce videos, per-episode metrics, detailed diagnostic figures, 
  W&B tables, checks of the exact inputs the policy received, and LeRobot recordings of the rollouts.
  This makes it easier to detect bugs during the development process.

:::{note}
**Why results are not bit-for-bit reproducible.** Two runs of the same eval give the
same success rates within noise, but not necessarily identical trajectories:

- **All parallel environments share one PhysX scene.** Isaac Sim 5.1 (through Isaac
  Lab 2.3.2) steps every environment in a single GPU physics solve. One environment's
  result can depend on which other environments are in the batch and what they are
  doing, which changes with the number of environments, the queue order, episodes
  ending at different times, and idle environments whose queue has run out.
- **The GPU physics solver is not deterministic.** Contact-rich PhysX simulation is
  not reproducible across GPUs, drivers or Isaac versions. `--deterministic-cuda`
  turns on PhysX enhanced determinism, a single solver partition and deterministic
  cuDNN. That narrows the gap on one machine at a speed cost, but it does not guarantee
  identical trajectories across hardware.
- **There is no per-environment physics step.** Any extra physics step (for example a
  settle after a controller gain switch) advances every environment, and PhysX keeps
  contact history when objects are teleported at reset, so earlier episodes in a run
  can affect later ones.
- **Some render state and the reseed are shared.** Lighting, and camera intrinsics
  under tiled rendering, are shared by all environments in the scene, and the
  per-episode reseed applies to the whole process, so the policy's sampling noise
  depends on scheduling.

In practice: compare runs by aggregate metrics over many episodes, use replay or a
single environment to debug one trajectory, and do not expect runs with a different
number of environments or GPUs to give identical per-episode outcomes.
:::


## Before you run the eval pipeline: creating an environment and task

`evaluate.py` runs an Isaac Lab gym task (`--task <id>`). Before a policy can be evaluated on
a scenario, a task for it has to exist and be registered, and it has to define three things:

- the scene: the robot, the table and the blocks;
- how each episode starts;
- an `evaluate()` method that returns a per-step `success` flag and any metric stats.

Evaluation scores episodes on that `success` signal and those stats, not on an RL reward.

**Blocks tasks are generated, not written by hand.** Both generators below render the domain
template in `src/toyblocks/tamp/blocks/template/` into a package
`src/toyblocks/tasks/autogen/<slug>/` (gitignored) that registers the gym id `<slug>-v0`.
Code generation also writes the success criterion and the metrics into the task's
`evaluate()`:

- `success` means the PDDL goal holds: every conjunct is true, the goal blocks have settled
  and the gripper is open;
- one `goal_conj_<c>` stat per conjunct.

So there is no reward or metric code to write: "Partial progress from the PDDL goal" below
explains how these stats become a partial progress score.

**From a dataset:**
[`scripts/generate_task_from_dataset.py`](https://github.com/allenai/ToyBlocks/blob/main/scripts/generate_task_from_dataset.py).
This is the task `launch_eval.py` evaluates, and the pipeline generates it for you from
`--dataset-path` before starting the workers. The slug is the dataset directory name with
`-` replaced by `_`, unless you pass `--task-name`. From the LeRobot dataset it reads:

- the block names, from the `observation.state.object_pose.<name>` columns;
- every distinct `pddl_goal`. A dataset with several goals gives one task that selects
  each environment's goal per episode.
- the recorded block sizes (`cube_scale`);
- the recorded `scene_id` and `robot_id`. A dataset that records no scene or robot is
  rejected.

It only generates code: each episode's starting state comes from the
[episode queue](evals/launch_eval.md#the-episode-queue), so no reset states are sampled. To
run it by hand, for example to debug code generation:

```bash
python scripts/generate_task_from_dataset.py --dataset-path data/datasets/my_dataset \
    --domain-path src/toyblocks/tamp/blocks --output-dir src/toyblocks/tasks/autogen --headless
```

**From a PDDL problem:**
[`scripts/generate_task_from_pddl.py`](https://github.com/allenai/ToyBlocks/blob/main/scripts/generate_task_from_pddl.py),
the [environment generation](datagen/env_generation.md) stage of data generation. Besides the
package it samples starting scenes from the problem's `:init` into `reset_states.pkl`, which
the task starts from when no queue is attached. Use it to evaluate on a problem that has no
dataset, by running `evaluate.py --task <slug>-v0` directly. `launch_eval.py` does not use it (this will 
be fixed by December 2026).

**Hand-written tasks** in `src/toyblocks/tasks/` (for example `ToyBlocks-Lift-v0`) define
their own `evaluate()`; [Metrics](evals/metrics.md) shows how to add task-specific metrics.

**Regenerate packages after updating the code.** Each package records the codegen version
that built it (`codegen_version` in `profiles.json`), and evaluation refuses a package built
by a different version. Otherwise a stale package's goal checks and success gate would
silently change success rates.

## How to run the eval pipeline

There are two entry points:

- `scripts/launch_eval.py` is the recommended one. It runs the whole queue-driven evaluation
  pipeline on your machine.
- `scripts/evaluate.py` is the eval worker the evaluation pipeline runs. You can also run this script
  directly, for example to debug one process against a policy server you started by
  hand.

The evaluation pipeline itself lives in
[`scripts/eval/run_eval_pipeline.sh`](https://github.com/allenai/ToyBlocks/blob/main/scripts/eval/run_eval_pipeline.sh)
and `launch_eval.py --dry-run` prints the exact invocation of it. Here's what processes
are launched when running `scripts/launch_eval.py`:

```text
launch_eval.py --policy {molmo2_maniflow,maniflow}  (or --replay)
  └─ run_eval_pipeline.sh
       ├─ GPU 0     policy server: serve_maniflow_policy --hl {model,oracle}  (none under --replay)
       ├─ codegen   builds the gym task from the dataset (generate_task_from_dataset.py)
       ├─ CPU       serve_episode_queue.py hands out one recorded setup per episode
       ├─ GPU 1..N  evaluate.py --queue_url ...  (one worker per GPU, many envs each)
       ├─ CPU       wandb_consolidate.py merges all workers into one W&B run (--wandb)
       └─ CPU       merge_eval_runs.py + skill_success_from_eval_run.py merge the workers'
                    results into one run directory under runs/
```

On a machine with fewer GPUs than that layout, the workers share the GPUs round-robin, so
a one-GPU workstation runs the server and one worker on GPU 0.

Detailed references:

- [`launch_eval.py` Reference](evals/launch_eval.md): every `launch_eval.py` flag, the
  default and smoke-test profiles, the per-policy defaults, the episode queue, dataset
  requirements and the output layout.
- [`evaluate.py` Reference](evals/evaluate.md):
  `evaluate.py` flag reference.
- [Metrics](evals/metrics.md):
  built-in metrics, output formats, and how to add metrics.

## Quick start with `launch_eval.py`

The eval pipeline initializes episodes from the recorded episodes of the LeRobot dataset
given by `--dataset-path` (required): the queue reads one setup per episode from it, and
the gym task is generated from it. `--smoke-test` switches to a small validation profile
(10 episodes, 1 eval GPU, 2 environments, 3-second episodes); drop it for a full run over
the whole dataset. Policy evals need the `maniflow-tb` and `molmo2` submodules (see
[Installation and setup](installation_and_setup_instructions.md)).

```bash
# Learned Molmo2 high-level policy + ManiFlow low-level policy (the default policy)
python scripts/launch_eval.py --smoke-test \
    --model-path data/checkpoints/my_maniflow_run/checkpoints/steps_400000_model.safetensors \
    --hl-model-path data/checkpoints/my_molmo2_run \
    --dataset-path data/datasets/my_dataset

# ManiFlow low-level policy, with the high-level oracle (the default for maniflow)
python scripts/launch_eval.py --smoke-test --policy maniflow \
    --model-path data/checkpoints/my_maniflow_run/checkpoints/steps_400000_model.safetensors \
    --dataset-path data/datasets/my_dataset

# Replay the dataset's recorded actions (no policy, no checkpoint)
python scripts/launch_eval.py --replay \
    --dataset-path data/datasets/my_dataset --episode-indices "0"
```

Useful additions: `--episode-indices "0,3,10-19"` to pick episodes, `--num-eval-gpus N`
to spread a `maniflow` eval over N eval GPUs, `--wandb` to log the run to W&B, and
`--dry-run` to print the pipeline command instead of running it.
Full episode rollouts and videos are recorded as a LeRobot dataset by default
(`--no-save-lerobot` to skip it). See the [`launch_eval.py` Reference](evals/launch_eval.md)
for every flag and its defaults.



## High-level conditioning modes

ManiFlow low-level policies are conditioned on a high-level command (a task string
and a target point in the front camera image). Where that command comes from is
chosen at launch:

- **High-level oracle** (`--policy maniflow`, `--use-oracle` on by default): a symbolic
  planner running next to the simulation produces the commands from the episode's
  PDDL problem. This measures the low-level policy on its own.
- **Learned high-level policy** (`--policy molmo2_maniflow`): a Molmo2 model served
  alongside ManiFlow produces the commands from camera images. By default it is
  queried at every action-chunk boundary; with a play-mode low-level checkpoint,
  `--async-hl` queries it only at the start of an episode and whenever the low-level
  policy ends a skill.
- **Low-level oracle** (`--policy molmo2_maniflow --ll-oracle`): the Molmo2 commands are
  executed by the motion-planned skills used in data generation (cuRobo v2) instead of
  by ManiFlow. This measures the high-level policy on its own.

The recorded expert actions can also be replayed open-loop with `--replay`, which needs
no policy at all; see [Dataset Replay](evals/replay.md).

## Running `evaluate.py` directly

`evaluate.py` is the eval worker the pipeline runs, and you can also run it by hand:
against a policy server you started yourself (the easiest way to debug either side with
breakpoints), with random or zero actions, or to replay a dataset.
[`evaluate.py` Reference](evals/evaluate.md) covers its action sources, a two-terminal
server + worker recipe, the observation transforms, every flag and its outputs.

## Episode scoring and outputs

An episode ends when the goal is reached, at the timeout, or when a play-mode low-level
policy stops (`--episode_end`); `--expert-timeout-scale` ties the timeout to the length of
each episode's expert demonstration. A block that was not supposed to move (by more than
2 cm or 15 degrees) counts as a collision and fails the episode (`--collision`).

Each eval worker writes `eval_results.json` (per-episode values and aggregates) and
`eval_episodes.json` (one record per episode) to its output directory under `runs/`,
plus a LeRobot dataset of the rollouts (`--save-lerobot`, on by default in pipeline runs)
and per-step CSVs with `--save_step_metrics`. At the end the pipeline merges the workers
into one run directory with per-skill success rates (`skill_success.json`), and with
`--wandb` into one W&B run; see [`launch_eval.py` outputs](evals/launch_eval.md#outputs).

See [Metrics](evals/metrics.md) for every metric, the output formats and how to add a
task-specific metric, and the [`evaluate.py` Reference](evals/evaluate.md) for the
scoring flags and for capturing failed episodes for TAMPER.

### Easily measuring partial progress from the PDDL goal

Success alone says nothing about how far a failed episode got. Because every episode comes
with a PDDL goal, the eval system measures partial progress for every task automatically, with no
task-specific code, and measures it the same way for all tasks.

**Where the goal comes from.** Each episode carries its PDDL goal (the queue setup's
`pddl_goal`), for example:

```text
(and (on_table block_a workspace_table) (on block_b block_a) (on block_c block_b))
```

When the gym task is generated,
[`codegen.py`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/tamp/blocks/template/codegen.py)
compiles each conjunct of each goal into a batched check on the live simulation state
(`_goal_conj_<k>`, which calls `batched_goal_conjunct` in
[`pddl_goal_tensor_conversions.py`](https://github.com/allenai/ToyBlocks/blob/main/src/toyblocks/tamp/blocks/pddl_goal_tensor_conversions.py)).
At reset, `set_episode_goal` selects each environment's own goal, and fails rather than
grade an episode against a goal the task was not compiled for. The supported predicates
are `on`, `on_table`, `on_left`, `on_right`, `on_front`, `on_back`, `next_to`, `ori_of`,
`clear` and `pick_obstructs`; `ori_of` accepts a yaw error up to `--goal-ori-yaw-tol-deg`
(40 degrees by default).

**Every step**, the task reports `goal_conj_<c>`, whether conjunct `c` holds (for example
`(on block_b block_a)`), and `goal_success`: all conjuncts hold and the settle gate passes
(the goal blocks are at rest and the gripper is open). The settle gate only affects
`goal_success`, not the conjunct counts.

**Each episode** counts the conjuncts in the goal (GT), those true at the start (IT), those
true at the end (CT), and those true at some point, and reports
`partial_progress = (CT - IT) / (GT - IT)`, which lies in `[-1, 1]`.

In the goal above, `block_a` starts on the table, so IT = 1 and GT = 3. Finishing the stack
gives 1.0, placing only `block_b` gives 0.5, and ending with none of the three conjuncts
holding gives -0.5. When the goal already holds at the start (GT = IT), `partial_progress`
is NaN and left out of the mean.

**Where it appears:**

- per episode in `eval_episodes.json`: `partial_progress`, the `num_goal_conjuncts*`
  counts, and a `goal_progress` entry per conjunct with its PDDL text, its `initial`,
  `first_true_step` and `final` values and its change-point `trace`;
- as the `partial_progress` aggregate in `eval_results.json`;
- as `mean_partial_progress` in the W&B aggregates table, with a goal-progress plot per
  episode in the episodes table's `goal_progress` column.

See [Metrics](evals/metrics.md) for every goal-progress key.

## Setting up a new policy server

Any model can be evaluated with this pipeline by wrapping it in a small policy-server
interface. See [Setting up a new policy server](imitation_learning/new_policy_server.md).

```{toctree}
:hidden:

evals/replay
evals/metrics
evals/launch_eval
evals/evaluate
```
---- FILE: docs_source_user_guide_workflows_imitation_learning.md ----

# Training ManiFlow Policies on Automatically Generated Data

ManiFlow policies are trained with the `maniflow-tb` submodule
([allenai/maniflow-tb](https://github.com/allenai/maniflow-tb), Python package `hvla`) and
its local launcher, `scripts/train_maniflow.py`. The script turns its flags into a single
training command,

```text
accelerate launch --config_file hvla/config/deepseeds/deepspeed_zero2.yaml ... hvla/training/train_hvla.py \
    --config_yaml ./examples/Franka/train_maniflow_multimodal.yaml --framework.name ManiFlowMultiModal ...
```

and runs it locally: `accelerate launch` on all visible GPUs by default, or
`torchrun` across several nodes. It trains on a merged LeRobot dataset, the output of the
[data generation pipeline](data_generation.md). Every flag is listed in the
`train_maniflow.py` [Reference](imitation_learning/train_maniflow.md).

## Setup

These docs describe maniflow-tb commit `c04eab7`, the commit the
`maniflow-tb` submodule is pinned to. The `maniflow` extra installs it in editable mode, together
with `molmo2` (see [Installation and Setup](installation_and_setup_instructions.md)):

```bash
git submodule update --init maniflow-tb molmo2
uv pip install -e ".[dev,isaac,torch-cu128,maniflow]"
```

The dataloader decodes the RGB videos with TorchCodec, which needs the FFmpeg shared libraries
(FFmpeg 4 to 7) on the machine. `python -c "import torchcodec"` should succeed before you train.
maniflow-tb's own `maniflow-tb/INSTALL.md` describes a standalone conda environment instead,
including FFmpeg and the optional `muon-optimizer` package for `--optimizer muon`.

Training downloads pretrained weights from the Hugging Face Hub on first use (the timm RGB
backbone and `t5-small`); set `HF_HOME` to choose the cache location. Metrics go to W&B when
credentials are available (`WANDB_API_KEY` or a `wandb login`); otherwise W&B runs offline and
its logs stay in the run directory.

## Training on a generated dataset

```bash
python maniflow-tb/scripts/train_maniflow.py  --data_root_dir data/datasets/merged/train/my_dataset 
```

Relative `--data_root_dir` and `--run_root_dir` paths are resolved against the directory you run
the script from; the training command itself runs inside `maniflow-tb/`.

- `--data_root_dir`: the merged LeRobot dataset (by default the pipeline writes it to  
`<output-root>/datasets/merged/train/<experiment-id>`). Pass several directories to co-train  
on them; `--dataset_ratio` sets their sampling ratio.  

Everything else keeps its default, which gives:

- absolute 9-D joint actions (7 joints, gripper, Play mode), predicting chunks of 50 actions  
and executing 25;
- a 9-D state (joint positions, gripper, Play mode); The play mode is used my Maniflow to indicate that it has completed the task and request the next instruction.
- front and gripper RGB through a fine-tuned CLIP ViT-B/16. Depth is supported but off by default.
- the target heatmap as cross-attention tokens through the shared RGB encoder (dropped
with probability 0.1, sigma 0.8 patches);
- T5-small language conditioning on the action string only (`action_only`);
- one node with all visible GPUs, AdamW with DeepSpeed ZeRO-2, a batch of 128 per GPU,
200k steps, a checkpoint every 10k steps and a 5% validation split.

The script prints the run ID, the run directory and the full command before it starts;
`--dry_run` prints them and exits. The run ID is built from the dataset name and the flags,
plus a timestamp.
`--user_prefix` puts a prefix in front of it, and `--run_id` replaces it.

## Choosing GPUs and nodes

`--num_gpus_per_node` defaults to the number of visible GPUs, so `CUDA_VISIBLE_DEVICES` picks
them. A short debug run on one GPU:

```bash
CUDA_VISIBLE_DEVICES=0 WANDB_MODE=offline python maniflow-tb/scripts/train_maniflow.py \
    --run_root_dir /tmp/maniflow_debug --duration 100 --save_interval 100 \
    --logging_frequency 10 --dbs 4 --num_workers 0 --max_episodes 500 \
    --data_root_dir data/datasets/merged/train/my_dataset
```

For several nodes, run the script on every node with the same flags, plus
`--num_nodes N --node_rank R --master_addr <address of node 0> --run_id <name>`. It then
launches `torchrun` instead of `accelerate launch`; every node must use the same `--run_id`
(or `--resume`) so that all of them write to the same run directory, which therefore has to be
on a filesystem the nodes share.

## The last batch of an epoch

The train dataloader keeps the last, partial batch of every epoch, and ManiFlow splits every batch
into a flow part (`int(0.75 * B)` samples) and a consistency part (`int(0.25 * B)` samples). A last
batch of 1 to 3 samples leaves the consistency part empty, and training stops at that step with

```text
IndexError: list index out of range
```

raised from the T5 tokenizer (`encode_text_input_T5`), because it is handed an empty list of
instructions. The `train: <episodes> episodes, <N> samples` line that `[FrankaDataset]` prints
before training gives `N`; the last batch holds `N mod --dbs` samples (per GPU). Pick a `--dbs` for
which that is 0 or at least 4. For example, 242 samples crash at `--dbs 16` (last batch: 2) and
train at `--dbs 32` (last batch: 18). The debug run above, at `--dbs 4`, crashes whenever `N` is
not a multiple of 4.

`N` is a property of the dataset, not of the training flags, and it is not fixed for a given
datagen command. The pipeline seeds task generation (`--task-gen-seed`, default `6303`), reset
state sampling (a fixed `0` with `--vecgen-problems-per-env 1`, `--seed` plus the group offset
otherwise) and execution (`--seed`, default `42`), so the problems and start states repeat.
The executed trajectories are not guaranteed to: vecgen steps GPU physics and builds motion plans
on worker threads, and a skill that is retried from the live state (a flip that misses keeps its
failed attempt in the episode) changes the episode length. Rerunning the same command can
therefore change `N`, and a `--dbs` that worked before can stop working. Check the log line after
each regeneration.

## Resuming and fine-tuning

- `--resume <run_id>` continues a run in `--run_root_dir` from its latest complete checkpoint,
and fails if there is none. The architecture (actions, state, cameras, conditioning, depth)
comes from the run's saved `config.yaml`, so the flags that define it are not emitted; only
the training-loop flags still apply. `--data_root_dir` is not needed. The run must resume on
the same number of GPUs it was saved with, since the optimizer state is sharded per GPU.
- `--pretrained_checkpoint <file>` starts a new run from a checkpoint's weights. The
optimizer, scheduler, EMA and W&B state start fresh.

## Outputs

Each run writes to `<run_root_dir>/<run_id>/` (`--run_root_dir` defaults to `./runs`):

| Path | Contents |
|---|---|
| `config.yaml` | The full training config, which the policy server reads. |
| `stats.json` | Normalization statistics of the (merged) training data. |
| `checkpoints/steps_<N>_model.safetensors` | Weights every `--save_interval` steps. |
| `checkpoints/steps_<N>_training_state.pt`, `checkpoints/state_<N>/`, `checkpoints/steps_<N>.done` | Scheduler and EMA state, the per-GPU optimizer state (newest only) and the completion marker `--resume` looks for. |
| `final_model/` | `model.safetensors`, `config.yaml` and `config.json` at the end of training. |
| `summary.jsonl` | One line per saved checkpoint. |
| `wandb/`, `wandb_run_id.txt` | W&B logs (also the offline ones) and the W&B run ID. |

Metrics go to the W&B project `maniflow-tb` (`--wandb_project`, or `$WANDB_PROJECT`), in your
default entity unless `--wandb_entity` or `$WANDB_ENTITY` names another.

## Evaluating the checkpoint

Pass a checkpoint to [`launch_eval.py`](evals/launch_eval.md). It finds `config.yaml` in
the run directory, and the policy server reads the training data's normalization stats
from it:

```bash
python scripts/launch_eval.py --policy maniflow \
    --model-path runs/<run_id>/checkpoints/steps_200000_model.safetensors \
    --dataset-path /path/to/lerobot_dataset
```

The policy server imports `hvla` from the `maniflow-tb` submodule, and the eval pipeline refuses
to start if that checkout is not the commit ToyBlocks pins (`git submodule update --init maniflow-tb` fixes it). A checkpoint trained with this code is on Hugging Face,
[allenai/maniflow-tb](https://huggingface.co/allenai/maniflow-tb), with the same layout
(`hf download allenai/maniflow-tb --local-dir <dir>`). See [Policy Evaluation](evaluations.md)
for the rest of the eval workflow, and
[Setting up a new policy server](imitation_learning/new_policy_server.md) to evaluate a
policy that is not ManiFlow.

```{toctree}
:hidden:

imitation_learning/train_maniflow
imitation_learning/new_policy_server
```

---- FILE: docs_source_user_guide_workflows_imitation_learning_new_policy_server.md ----

# Setting up a new policy server

ToyBlocks provides a base class and a WebSocket server so any model can be evaluated
with the same pipeline. The model implementation lives in its own repository;
ToyBlocks only provides the interface.

**1. Subclass `BasePolicy`** in your model's package:

```python
from toyblocks.serving import BasePolicy

class MyPolicy(BasePolicy):
    def __init__(self):
        self.model = load_my_model()

    def infer(self, obs: dict) -> dict:
        action = self.model.predict(obs)
        return {"actions": action}  # np.ndarray, shape (action_dim,) or (T, action_dim)
```

The `infer` method receives a dict of numpy arrays and must return a dict with at
least an `"actions"` key. Any extra ndarray keys returned alongside it are made
available to the eval loop on `PolicyClientAdapter.last_aux` (this is how
`action_pd_mode` is passed through).

**2. Serve it** using `toyblocks.serving.PolicyServer`:

```python
from toyblocks.serving import PolicyServer
server = PolicyServer(MyPolicy(), host="0.0.0.0", port=8000)
server.serve_forever()
```

There is no generic launcher script; wrap these lines in your own entry point.
`src/toyblocks/serving/serve_maniflow_policy.py` (run as
`python -m toyblocks.serving.serve_maniflow_policy`) is a complete example: a `tyro` CLI that
loads the ManiFlow checkpoint into a `BasePolicy` and serves it with `PolicyServer`.

Point [`evaluate.py`](../evals/evaluate.md) at the server with `--policy_host` and
`--policy_port`. `launch_eval.py` starts only the ManiFlow server (`--policy maniflow` or
`molmo2_maniflow`), so run your own server alongside `evaluate.py` instead.

**3. (Optional) Add an observation transform** if your model expects a different
observation format than the ToyBlocks env produces. Subclass `BaseObsTransform` in
`src/toyblocks/serving/obs_transforms/` and register it in `_lazy_registry`, then use
`--obs_transform <name>` at eval time. Transforms can also override
`action_postprocess` to rewrite the policy response before the action chunk broker.

---- FILE: docs_source_user_guide_workflows_imitation_learning_train_maniflow.md ----

# `train_maniflow.py` Reference

Every flag of maniflow-tb's `scripts/train_maniflow.py` at commit `c04eab7`, the commit the
`maniflow-tb` submodule is pinned to (`python maniflow-tb/scripts/train_maniflow.py --help`
prints the same list). For the workflow (setup, an example run, outputs, evaluation) see
[Pre-training Policies on Automatically Generated Data](../imitation_learning.md).

The flags are spelled with underscores. Each one either sets a field of
`examples/Franka/train_maniflow_multimodal.yaml` on the `train_hvla.py` command line or
configures the launcher. With `--resume`, the architecture flags (marked "fresh runs
only") are not emitted: the run's saved `config.yaml` defines them.

## Launcher and logging

| Flag | Default | Description |
|---|---|---|
| `--dry_run` | off | Print the run ID, run directory and training command, then exit without training. |
| `--user_prefix` | none | Prefix of the run ID (`<prefix>-<run name>`). |
| `--run_id` | derived | Run name; replaces the ID built from the flags (see [Run name](#run-name)). Must be shorter than 123 characters. |
| `--num_gpus_per_node` | all visible GPUs | GPUs per node (`CUDA_VISIBLE_DEVICES` aware). |
| `--num_nodes` | `1` | Nodes. More than one launches with `torch.distributed.run` (`torchrun`) instead of `accelerate launch`; run the script once per node with the same flags and its own `--node_rank`. |
| `--node_rank` | `$NODE_RANK` or `0` | Rank of this node (multi-node only). |
| `--master_addr` | `$MASTER_ADDR` or `127.0.0.1` | Address of node 0 (multi-node only). |
| `--master_port` | `$MASTER_PORT` or `29500` | Rendezvous port on node 0 (multi-node only). |
| `--wandb_project` | `$WANDB_PROJECT` or `maniflow-tb` | W&B project. |
| `--wandb_entity` | `$WANDB_ENTITY` or your default entity | W&B entity. |
| `--wandb_mode` | see description | `online`, `offline` or `disabled`. Default: `$WANDB_MODE`, else `online` when `WANDB_API_KEY` is set or `~/.netrc` holds W&B credentials, else `offline`. |

The training command runs inside `maniflow-tb/`. `--data_root_dir` and `--run_root_dir` are
resolved against the directory you launch from, so relative paths work from anywhere.

## Data

All fresh runs only, except `--num_workers`.

| Flag | Default | Description |
|---|---|---|
| `--data_root_dir` | none | One or more LeRobot datasets; several are co-trained, merged at load time. Required for a new run; a `--resume` run reads it from its saved config. |
| `--data_mix` | `apr13_test` | Dataset mixture name (`datasets.vla_data.data_mix`). |
| `--val_ratio` | `0.05` | Fraction of episodes held out for validation. |
| `--max_episodes` | all | Use only N episodes, then split them into validation and training. A comma-separated list (e.g. `10000,5000,2000`) caps each `--data_root_dir` separately. |
| `--dataset_ratio` | none | Sampling ratio across datasets, e.g. `1,1` or `10,5,2`; larger datasets are subsampled to match. |
| `--num_workers` | `12` | Dataloader workers per process. |
| `--filter_config` | none | Episode filter preset name or YAML path; presets are in `maniflow-tb/hvla/config/episode_filtering/` (`spatial_filter`). A relative YAML path is resolved from `maniflow-tb/`. |
| `--filter_override` | none | Dotlist overrides of the filter config, e.g. `spatial_region=inside bounds='[0.4,0.7,-0.1,0.1]'`. |
| `--filter_joint_jumps` | off | Drop episodes in which any joint moves more than RAD radians between consecutive frames (teleport resets). The bare flag uses 0.5. Applies to training and validation. |
| `--filter_small_rotates` | off | Drop episodes with a rotate cycle that turns the block less than DEG degrees about z (failed rotate attempts). The bare flag uses 10. Applies to training and validation. |
| `--goal_action_filter` | none | Allow-list of `goal.action` values a training sample may start on, e.g. `'pick,place'`. With several datasets, `'pick,place;stack,done;lift'` gives one `;`-separated group per dataset, and an empty group leaves that dataset unfiltered. Not to be combined with `--phase_sample_weights`. |
| `--phase_sample_weights` | none | Sampling weights per `action.low_level_action` phase: a preset string or a dictionary. |
| `--skip_actions` | none | Comma-separated low-level actions to skip. |
| `--drop_redundant_table_moves` | off | Drop redundant back-to-back table-to-table retries, keeping the last attempt. |
| `--max_frames_per_episode` | all | Truncate each episode to its first N frames. |
| `--skip_first_n_steps_per_episode` | none | Skip the first N frames of every episode. |

## Training loop and optimizer

| Flag | Default | Description |
|---|---|---|
| `--duration` | `200000` | Training steps (`trainer.max_train_steps`). |
| `--dbs` | `128` | Batch size per GPU. |
| `--grad_accum` | `1` | Gradient accumulation steps. |
| `--optimizer` | `adamw` | `adamw` (DeepSpeed ZeRO-2) or `muon` (distributed Muon + AdamW on plain DDP, bf16). `muon` needs the `muon-optimizer` package (see `maniflow-tb/INSTALL.md`). |
| `--muon_lr` | `0.02` | Muon learning rate; lower it (e.g. 0.01 or 0.005) if training diverges. |
| `--save_interval` | `10000` | Save a checkpoint every N steps. |
| `--logging_frequency` | `100` | Log metrics every N steps. |
| `--run_root_dir` | `runs` | Parent directory of the run directory (`<run_root_dir>/<run_id>`). |
| `--resume` | none | Run ID to resume from `<run_root_dir>/<run_id>/`, using its `config.yaml` and latest complete checkpoint. Fails if the run has no loadable checkpoint. |
| `--pretrained_checkpoint` | none | Checkpoint whose weights initialize a new run at step 0; optimizer, scheduler, EMA and W&B state are not restored. |

## Action and state

All fresh runs only.

| Flag | Default | Description |
|---|---|---|
| `--action_mode` | `abs` | Action space: `abs` or `relative` (9-D joints), `ee` (8-D end effector), `ee_target_7d` or `rel_ee_target_7d` (9-D). |
| `--action_keys` | none | Custom action columns, e.g. `action.cube_position.block_r action.cube_distance.block_r`. The action size is read from the first dataset's `meta/info.json`. |
| `--action_norm_band` | `q01_q99` | Arm-action normalization band: `q01_q99` (the `stats.json` quantiles, clipping the outer 1% of labels) or `valid_min_max` (min/max over the `action.is_valid` rows, no clipping). |
| `--state_estimation` | off | Predict `cube_position.block_red1` and `cube_distance.block_red1` (4-D) with a horizon of 1, saving every 2000 steps. |
| `--state_dim` | `9` | Proprioceptive state size: joint positions (7), gripper and PD mode. |
| `--include_jvel_ee_pos` | off | Add joint velocities (7) and the end-effector XYZ (3), giving a 19-D state. |
| `--zero_state` | off | Zero the state vector, keeping its size. |
| `--ft` | off | Add the 6-D wrench to the state. |
| `--horizon` | `50` | Predicted action chunk length. |
| `--n_action_steps` | `25` | Actions executed per chunk. |
| `--num_inference_steps` | `12` | ODE solver steps at inference. |

## Cameras and RGB

All fresh runs only.

| Flag | Default | Description |
|---|---|---|
| `--camera_config` | front and gripper RGB | Camera preset (table below). |
| `--no_gripper` | off | Legacy: same as `--camera_config front_rgb` (`front_rgb_depth` with `--depth`). |
| `--rgb_224` | off | Read pre-resized RGB videos from `<camera>_224` instead of the native 640x360 ones. Missing 224 videos fail the run. |
| `--rgb_backbone` | `vit_base_patch16_clip_224.openai` | timm RGB backbone, e.g. `vit_base_patch16_siglip_224.webli`, `vit_base_patch16_siglip_224.v2_webli` (SigLIP2) or `vit_so400m_patch14_siglip_224.webli`. The normalization mean and std are read from the checkpoint. |
| `--siglip` | off | Shorthand for `--rgb_backbone vit_base_patch16_siglip_224.v2_webli`. |
| `--freeze_rgb_backbone` | off | Freeze the RGB backbone instead of fine-tuning it. |
| `--use_previous_front_frame` | off | Add the previous front frame as a third RGB view. |
| `--previous_front_frame_lookback_weights` | none | Weighted lookback ranges of that frame, e.g. `0-1_1`. |
| `--target_crop` | `-1` | Target-centred square front crop: `-1` off, `0` = all of it above the target, `50` centred, `33` = 67/33 top/bottom, `25` = 75/25. Not with `--use_previous_front_frame`. |

`--camera_config` presets:

| Preset | RGB | Depth |
|---|---|---|
| `front_rgb` | front | none |
| `front_gripper_rgb` | front, gripper | none |
| `front_rgb_depth` | front | front |
| `front_gripper_rgb_front_depth` | front, gripper | front |
| `front_gripper_rgb_depth` | front, gripper | front, gripper |
| `front_gripper_rgb_gripper_depth` | front, gripper | gripper |
| `front_gripper_depth_only` | none | front, gripper |
| `gripper_rgb_depth` | gripper | gripper |
| `gripper_rgb` | gripper | none |

A preset without RGB turns target conditioning off.

## Depth

All fresh runs only. Any depth input also turns on `--per_cam_norm`.

| Flag | Default | Description |
|---|---|---|
| `--depth` | off | Use depth (raw depth, back-projected to a pointmap on the GPU). Without `--camera_config`, both cameras' depth. |
| `--depth_encoder` | `shared_rgb` | Depth encoder: `dense`, `sparse`, `shared_rgb` (the RGB backbone) or `defm`. |
| `--sparse_depth` | off | Sparse PointNet encoder. Only read when `--depth_encoder` is empty, which its choices do not allow, so it has no effect; use `--depth_encoder sparse`. |
| `--ptmap_backbone` | `convnextv2_tiny.fcmae_ft_in22k_in1k` | Pointmap encoder backbone (e.g. `vit_small_patch14_dinov2`). Ignored with `--depth_encoder shared_rgb`, which uses `--rgb_backbone`. |
| `--depth_rg8` | none | Decode depth from RG8-packed videos in `<camera>_<variant>`: `rg8` / `rg8_224` (depth = R + 256 G) or `rg8_55` / `rg8_55_224` (10-bit 5+5 pack, clipped to 1023 mm). Only for datasets re-encoded with `scripts/depth_conversion/reencode_to_rg8_batch.py`. |
| `--depth_g12` | none | Read depth from gray HEVC videos `<depth_key>_<variant>`: `g12_224` (lossless gray12le), `g10_224` (lossless gray10le, clipped to 1023 mm) or `g10_224_crf035` (x265 CRF 0.35). Not with `--depth_rg8`. |
| `--add_depth_noise` | off | RGB-guided depth noise augmentation. |
| `--depth_noise_ideal_mix` | `0.6` | Blend of clean and corrupted depth (1.0 = clean). |
| `--per_cam_norm` | off | Per-camera pointmap normalization bounds instead of global ones. |

## Target conditioning

All fresh runs only.

| Flag | Default | Description |
|---|---|---|
| `--token` | on | Target heatmap as cross-attention context tokens. |
| `--timestep_concat` | off | Heatmap fused into the AdaLN time conditioning. |
| `--target_embedding` | off | Gaussian bias on the RGB tokens, without a heatmap encoder. |
| `--target_pe` | off | Learned per-patch encoding on the RGB tokens, without a heatmap encoder. |
| `--no_target` | off | No target conditioning. |
| `--heatmap_encoder_type` | `shared_rgb` | Heatmap encoder for `--token`: `shared_rgb` (the CLIP ViT), `convnextv2` (a separate pretrained one), `lightweight`, or `cnn` (from scratch on the same 14x14 grid). |
| `--target_mask_prob` | `0.1` | Probability of dropping the target conditioning during training. |
| `--target_sigma` | `0.8` | Gaussian sigma of the heatmap, in patches. |

The five mode flags are mutually exclusive, but at this commit `--token` is on by default and
checked first, so `--timestep_concat`, `--target_embedding` and `--target_pe` have no
effect: the mode is `token` unless `--no_target` is given.

## Language conditioning

All fresh runs only.

| Flag | Default | Description |
|---|---|---|
| `--language_conditioned` | on | Language conditioning (already on; turn it off with `--no_language`). |
| `--no_language` | off | Disable language conditioning. |
| `--language_model` | `t5-small` | T5 encoder: `t5-small`, `t5-base` or `t5-large`. |
| `--language_mode` | `action_only` | `action_only` drops the coordinates from the language string; `action_goal` keeps them. |
| `--lang_injection_mode` | `token` | `token` (cross-attention) or `timestep_concat` (fused into AdaLN). |

## Action-chunk labelling

All fresh runs only.

| Flag | Default | Description |
|---|---|---|
| `--pause_on_attempt` | off | When a pick, place, flip or rotate switch falls inside a chunk, repeat that frame's action for the rest of the chunk and set done = 1 from the switch. Not with `--use_previous_front_frame`. |
| `--freeze_on_goal_change` | off | When the lookback crosses a goal change, relabel the chunk as "hold position". Needs `--use_previous_front_frame`. |

## Diagnostics

| Flag | Default | Description |
|---|---|---|
| `--save_first_batch` | off | Save the preprocessed first batch to `<run_dir>/first_batch_data/`. |
| `--save_arch_diagram` | off | Save an ASCII architecture diagram to `<run_dir>/architecture.txt`. |
| `--profile_steps` | `0` | cProfile the first N steps on rank 0, dumped to `<run_dir>/profiles/`. |
| `--faulthandler` | off | Set `PYTHONFAULTHANDLER=1`, so a native crash dumps a Python traceback per thread. |

## Checks the script enforces

The script stops with an error for:

- a new run without `--data_root_dir`;
- `--num_nodes` above 1 without `--run_id` or `--resume`;
- `--depth_rg8` together with `--depth_g12`;
- `--freeze_on_goal_change` without `--use_previous_front_frame`;
- `--pause_on_attempt` together with `--use_previous_front_frame`;
- no visible GPU and no `--num_gpus_per_node` (not checked with `--dry_run`);
- `--optimizer muon` without the `muon` package installed (not checked with `--dry_run`);
- `--resume` of a run without `<run_root_dir>/<run_id>/config.yaml` (not checked with `--dry_run`).

## Run name

A fresh run's ID is `<datasets>_<horizon>_<n_action_steps>_<action_mode>` plus a suffix for
each non-default choice, then a `-<MM-DD-HH-MM-SS>` timestamp:

- the target mode, heatmap encoder, mask and sigma (`_token_shared_rgb_mask0.1_sigma0.8`);
- the language model and mode (`_lang_t5-small_action_only`);
- the camera preset (for example `_FGd`) and depth encoder;
- the backbone, state, filtering, ratio, optimizer and labelling flags.

`--rgb_224`, `--max_episodes` and `--target_crop` add the prefixes `rgb224_`, `Ep<N>_` and
`tcrop<N>_`, and `--user_prefix` goes in front of everything. IDs longer than 122 characters
are truncated before the timestamp, so that `--resume` accepts them. `--run_id` replaces the
whole ID, timestamp included.

---- FILE: docs_source_user_guide_workflows_installation_and_setup_instructions.md ----

# ToyBlocks Installation and Setup Instructions

These instructions use `uv` and set up everything needed for evaluation, data generation and training.

## Prerequisites

- Linux with an NVIDIA GPU and a driver that supports CUDA 12.8 (driver 570 or newer).
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/) on your `PATH` (`curl -LsSf https://astral.sh/uv/install.sh | sh`).
- Git access to GitHub over HTTPS. ToyBlocks and all of its submodules (`curobo`, `maniflow-tb`, `molmo2` and `agentic_robotics`) are public.
- `tmux` (`sudo apt install tmux`): long-running jobs (pipeline runs, merges, renders) are run in detached `tmux` sessions so they survive a dropped connection.

## Setup

```bash
git clone https://github.com/allenai/ToyBlocks.git
cd ToyBlocks

# Create a virtual environment for Python 3.11 (required for Isaac Sim 5.1) and activate it
uv venv --python 3.11
source .venv/bin/activate

# Fetch the submodules (curobo, plus maniflow-tb and molmo2 for the policies and agentic_robotics
# for LLM agents)
git submodule update --init --recursive
# Without ManiFlow, only curobo is needed:
# git submodule update --init curobo

# Install like any Python package (uv sync is not recommended)
uv pip install -e ".[dev,isaac,torch-cu128]"

# Or, to also install the policies (the maniflow extra: maniflow-tb and molmo2, editable)
uv pip install -e ".[dev,isaac,torch-cu128,maniflow]"
```

Isaac Sim asks you to accept the NVIDIA Omniverse EULA the first time it starts. Headless and scripted runs have no prompt to answer and abort with `EOF when reading a line`, so accept it up front:

```bash
export OMNI_KIT_ACCEPT_EULA=YES
```

## Datagen (cuRobo) setup

Data generation (vecgen) needs cuRobo v2, which comes from the `curobo` submodule. Install the `vecgen` optional group, or `tamp`, which adds the rerun and flask debug viewers on top. The submodule must be initialized first (`git submodule update --init curobo`); the `--recursive` command above already does this. There is no TAMP submodule any more: the FF symbolic planner is vendored in `src/toyblocks/vecgen/symbolic/ff_planner/`.

```bash
uv pip install -e ".[dev,isaac,torch-cu128,vecgen]"

# Or datagen + ManiFlow
uv pip install -e ".[dev,isaac,torch-cu128,vecgen,maniflow]"
```

`uv` builds `curobo` from the submodule itself (it is registered in `pyproject.toml` as an editable source), so no separate `uv pip install -e curobo` step is needed.

No local CUDA toolkit is needed: cuRobo v2 compiles its kernels at runtime with NVRTC, using the `nvidia-*-cu12` pip packages installed with torch. The `cuda-12.8` toolkit install and the `setup_cuda` shell function that cuRobo v1 needed are no longer required.

:::{note}
**Docker:** `docker/vecgen.dockerfile` still installs `curobo` as a separate step after the main install instead of passing the `vecgen` group, because a one-step install failed inside `docker build`. `docker/eval.dockerfile` installs every extra, `vecgen` included, in one step.
:::

## Agentic robotics setup

The `agentic_robotics` submodule runs LLM agents that drive the robot through the skills as MCP
tools. It needs the `vecgen` extra for its scripted skills, plus the `agentic` extra:

```bash
git submodule update --init agentic_robotics
uv pip install -e ".[dev,isaac,torch-cu128,vecgen,agentic]"
```

Episodes call the model through OpenRouter, so you need your own OpenRouter API key. See
[Agentic Robotics](agentic_robotics.md) for the key, the web UI and adding tasks.

## Download the assets

The assets are downloaded from a public R2 bucket (about 280 MB, no credentials needed) into a cache at `~/.toyblocks`, and symlinked into the `assets` folder at the root of the repository. The cache is shared by every checkout on the machine, so the disk usage lands in your home directory and deleting `assets/` frees nothing. Run it with the virtual environment active, since the command is installed into `.venv/bin`:

```bash
get-toyblocks-assets --asset-manifest asset_manifest.json
```

This also installs the CC0 Poly Haven HDRI pool (1.8 GB, `assets/environments/polyhaven`) that rendering uses for backdrops. The second pool the default render flags use, the Laval Indoor HDR Dataset (`indoor-2018`), is licensed for research use and has to be requested from Université Laval. See [HDRI backdrops](https://github.com/allenai/ToyBlocks/blob/main/docs/source/user_guide/workflows/datagen/local.md#hdri-backdrops) in `docs/source/user_guide/workflows/datagen/local.md` for how to install it.

## Verify the installation

Run the installation checks from the repository root, with the virtual environment active:

```bash
pytest tests/install                    # seconds: packages, versions, submodules, assets
export OMNI_KIT_ACCEPT_EULA=YES
pytest tests/install --install-gpu      # several minutes: also Isaac Sim, cuRobo and vecgen
```

The first command checks each extra you installed and skips the others. For every installed extra, it checks that the packages are installed in the versions `pyproject.toml` allows and that what its workflows import imports. It also checks that the submodules the extra needs are checked out at the pinned commits and are the ones Python imports. Finally, it checks that the assets are downloaded. A failure names what is wrong and the command that fixes it.

`--install-gpu` also checks that PyTorch sees the GPU and that Isaac Sim starts headless with the right Warp. With the `vecgen` extra, it runs the vecgen check below, with and without videos. With the `agentic` extra, it imports the agentic skill servers.

To run the vecgen check by hand: with the `vecgen` group installed, generate one environment package from a checked-in problem and record a few episodes. This exercises Isaac Sim, cuRobo and LeRobot recording, and should end with a `RESULT episodes=4 success=...` line:

```bash
export OMNI_KIT_ACCEPT_EULA=YES
problem=src/toyblocks/tamp/blocks/problems/flip.pddl
python scripts/generate_task_from_pddl.py --domain_path src/toyblocks/tamp/blocks \
    --pddl ${problem} --num_reset_states 8 --num_envs 4 --seed 0 --output_dir outputs --headless
python scripts/vecgen/run.py --env-path outputs/flip --pddl ${problem} \
    --domain src/toyblocks/tamp/blocks/domain.pddl --num-envs 4 --episodes 4 \
    --record datasets/flip/flip --mark-complete --headless
```

That run records state and actions only. To also record camera videos (RGB and depth from the front and gripper cameras, 640x360), add `--record-videos --enable_cameras`: `--record-videos` adds the cameras to the scene, and `--enable_cameras` lets Isaac Sim render them. Each simulation step takes about 1.5 times as long:

```bash
python scripts/vecgen/run.py --env-path outputs/flip --pddl ${problem} \
    --domain src/toyblocks/tamp/blocks/domain.pddl --num-envs 4 --episodes 4 \
    --record datasets/flip/flip_videos --record-videos --enable_cameras --mark-complete --headless
```

The videos land in `datasets/flip/flip_videos/blocks_success/videos/` (and `blocks_failure/videos/` for failed episodes), one folder per camera stream.

A full pipeline run ([Running the pipeline locally](datagen/local.md)) also leaves two things worth checking: a plot of a sample episode, `episode_0.png`, next to the merged dataset, and the full run configuration, `run_datagen_pipeline_config_<timestamp>.json`, in the run's base directory.

## Build the docs

These docs are built with Sphinx and MyST from `docs/source`:

```bash
uv pip install -e ".[docs]"
sphinx-build docs/source docs/build/html
```

Then open `docs/build/html/index.html`.

## Docker images

Both images build from a fresh clone of a git ref (so push your branch first) and are tagged with its short SHA:

```bash
# eval image: Isaac + cuRobo + maniflow-tb + molmo2 (policy servers and evaluate.py)
docker/build_eval_image.sh main /tmp/eval_img        # -> toyblocks-eval:<sha>

# slim datagen image: vecgen + cuRobo v2, no policies, no CUDA toolkit
docker/build_vecgen_image.sh main /tmp/vecgen_img    # -> toyblocks-vecgen:<sha>
```

:::{note}
**Hardware:** the images need an x86_64 Linux host with an NVIDIA GPU (see [Prerequisites](#prerequisites)); they do not build on arm64 such as Apple Silicon, since the pinned CUDA torch has no arm64 wheels. Running them needs the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html). Tested on an NVIDIA RTX 5090 (32 GB).
:::

## Code Organization

All source code is in `src/toyblocks/`:

- `src/toyblocks/tasks`: all hand-created tasks, as well as templates for PDDL-based task generation
- `src/toyblocks/vecgen`: the datagen engine (FF planning, batched skills, cuRobo planner pool, LeRobot recording)
- `src/toyblocks/robots`: all robot assets and configurations, including controllers
- `src/toyblocks/serving`: policy serving infrastructure (`BasePolicy`, `PolicyServer`, WebSocket client, obs transforms)
- `src/toyblocks/eval`: evaluation of learned models (with or without oracles) and replay
- `src/toyblocks/wrappers`: gym `Wrapper` subclasses (recording, stats, obs flattening)
- `src/toyblocks/cli`: command line utilities
- `src/toyblocks/data_annotation`: dataset annotation utilities
- `src/toyblocks/utils`: utilities for ToyBlocks
- `src/toyblocks/utils/rigid_objects`: utilities for working with rigid objects (e.g. creating them more easily)

The ManiFlow and Molmo2 policy code is in the `maniflow-tb/` (package `hvla`) and `molmo2/` (package `olmo`) submodules.

## Next steps

- [Automatic Data Generation](data_generation.md): generate demonstration datasets.
- [Pre-training ManiFlow Policies](imitation_learning.md): train a policy on them.
- [Policy Evaluation](evaluations.md): evaluate it.
- [Agentic Robotics](agentic_robotics.md): let an LLM agent drive the robot through the skills.

---- FILE: docs_tamper.md ----

# TAMPER — TAMP Expert Relabeling

A DAgger-style loop with a TAMP expert. An evaluation run surfaces the states a
policy actually gets wrong; the expert then plans demonstrations *from those
states* instead of from freshly sampled ones, so the next round of training data
covers the distribution the policy visits rather than the one datagen happens to
sample.

The expert is the vecgen engine (`scripts/vecgen/run.py`, the same one datagen
runs): FF over the blocks domain from the captured scene, cuRobo v2 motion plans,
scripted skills with verified effects. No step needs the TAMP submodule.

Related docs:

- Evaluation: [evaluations.md](source/user_guide/workflows/evaluations.md) and [`evaluate.py` reference](source/user_guide/workflows/evals/evaluate.md)
- Dataset recording: [docs/lerobot_recording.md](lerobot_recording.md)
- Datagen pipeline: the **Datagen Pipeline** section in `CLAUDE.md`

## How it works

Capture happens inside `BaseEnv._before_auto_reset`, the only point where a
finished episode's terminal state is still in the sim. By the time
`infos["final_info"]` reaches the eval loop, the env has auto-reset and the sim
holds the *next* episode. `_success_once` and the queue setup are both still
live there too, so the outcome and the episode's goal are recoverable.

Each captured directory is a multi-problem **vecgen env package**:

- a clone of the eval's env package, with its gym id retargeted to the directory;
- the captured states as its `reset_states.pkl`;
- a `problems.json` index with one entry per state: its goal problem, its episode
  blocks, and reset-state range `[i, i + 1]`. The env's other spawned blocks stay
  parked.

`scripts/vecgen/run.py` then runs on it directly. `--init-from-scene` plans each
episode with FF from the scene read off the captured state (`on` / `on_table` /
`clear` / `ori_of`, as a vecgen re-plan does) toward the recorded goal, instead of
from the problem's `:init`. `--reset-state-ids` runs the selected states once each.

```
eval (policy fails)  ──►  TAMPER dir  ──►  vecgen (plan + execute + record)  ──►  dataset
        ▲                                                                            │
        └─────────────────────────  retrain, evaluate again  ◄───────────────────────┘
```

Where a state's goal comes from:

| Eval setup | Problem written |
|---|---|
| Queue setup with `pddl_problem_file` (file exists) | that file |
| Queue setup with `pddl_goal` (dataset queues, `launch_eval.py`) | rebuilt: `:objects` = the episode's blocks under their domain subtypes, `:goal` = `pddl_goal`, `:init` = the recorded `high_level_state` (vecgen ignores it under `--init-from-scene`) |
| No queue | none; pass `run_tamper_pipeline.py --pddl-problem-file` |

## Prerequisites

You need an eval env package and an episode queue: what `launch_eval.py` builds
from a LeRobot dataset. To build them by hand:

```bash
DS=/path/to/lerobot_dataset            # any datagen output (vecgen or merged)

# eval env package from the dataset -> src/toyblocks/tasks/autogen/tamper_src (gym id tamper_src-v0)
python scripts/generate_task_from_dataset.py --dataset-path $DS --task-name tamper_src --headless

# episode queue (one setup per dataset episode)
python scripts/serve_episode_queue.py --dataset-path $DS --port 8011 &
```

## Step 1 — Evaluate with capture enabled

```bash
python scripts/evaluate.py \
    --task tamper_src-v0 \
    --random_actions \
    --queue_url http://localhost:8011/next \
    --obs_mode rgb --enable_cameras \
    --num_envs 4 --num_eval_steps 600 \
    --env-cfg.episode-length-s 4.0 \
    --tamper_output_dir outputs/tamper/round1 \
    --output_dir runs/tamper_eval_round1 \
    --headless
```

`--random_actions` is the cheapest way to exercise the loop. For a real policy,
point it at a policy server with `--policy_host` / `--policy_port`, or pass `--tamper_output_dir` through
your usual eval. Capture is off unless `--tamper_output_dir` is set, so existing
eval runs are unaffected.

> **Episodes must end.** Autogen env packages ship `episode_length_s = 99999`. An
> episode that never succeeds never terminates, never auto-resets, and is
> therefore never captured. Pass `--env-cfg.episode-length-s`, or use the queue's
> expert-timeout scaling, to give the policy a fair attempt with a finite end.

### Capture flags

| Flag | Default | Description |
|---|---|---|
| `--tamper_output_dir` | `None` | Root for captured states. Unset disables capture entirely. |
| `--tamper_capture_successes` | `False` | Also snapshot successful episodes (tagged `success`), so you can filter at planning time instead. |
| `--tamper_max_states` | `None` | Cap the number of snapshots. Bounds the output of a long run against a policy that fails often. |
| `--tamper_source_env_path` | auto | Env package to clone. Auto-detected from `cfg.reset_states_path`; set it only when detection fails. |

On completion the run prints:

```
[TAMPER]: captured 16 state(s) across 1 problem(s) -> outputs/tamper/round1
```

## Step 2 — Inspect what was captured

```
outputs/tamper/round1/
    tamper_summary.json
    <problem_slug>/                       # PDDL stem, or unknown_problem (dataset queues)
        reset_states.pkl                  # captured states + scene profile ids
        problems.json, problems/*.pddl    # vecgen index: one entry per state
        tamper_failures.json              # instance_id -> episode, outcome, goal
        __init__.py, env.py, env_cfg.py,  # cloned env package (gym id retargeted)
        profiles.json, non_sim_state_randomizations.json
```

States are grouped by source PDDL problem file; a dataset queue records none, so
everything lands in `unknown_problem`, and each state's own goal sits in
`problems.json`. `tamper_failures.json` is the join key back to the eval run:

```json
{
  "pddl_problem_file": null,
  "num_instances": 16,
  "num_scene_profiles": 1,
  "reason_counts": {"timeout": 16},
  "failures": [
    {"instance_id": 0, "env_idx": 0, "reason": "timeout", "episode_len": 100,
     "episode_id": "ep_000015", "pddl_goal": "(and (on_table block_pink workspace_table) ...)",
     "scene_profile_id": 0, "source_problem": "vg_notamp_out",
     "episode_blocks": ["block_yellow", "block_o", "..."],
     "vecgen_problem": "tamper_00000"}
  ]
}
```

Outcomes are tagged `failure` (the env terminated) or `timeout` (it ran out of
episode length, or the end was requested while unsuccessful). `vecgen_problem` is
the state's `problems.json` entry. It is `null` when no problem could be recovered,
and the pipeline skips those states.

### What gets normalized, and why

A terminal state is captured mid-motion. Before writing, the collector zeroes
joint and root velocities and aligns `joint_position_target` with
`joint_position`. Without this, the PD controller would yank the arm toward a
stale target the moment vecgen wrote the state, so the scene executed would not
be the scene planned against.

Object **poses** are left exactly as captured; those are the TAMPER signal.

## Steps 3–5 in one command

`scripts/datagen/run_tamper_pipeline.py` runs vecgen, annotation and merge over a
TAMPER directory. Eval is deliberately *not* part of it: it needs a policy and a
live sim, so it stays step 1.

```bash
python scripts/datagen/run_tamper_pipeline.py \
    --tamper-dir outputs/tamper/round1 --exec-num-envs 32

# Only hard failures, record cameras so annotation runs, no merge
python scripts/datagen/run_tamper_pipeline.py \
    --tamper-dir outputs/tamper/round1 \
    --reasons failure --record-videos --skip-merge
```

The pipeline reads `tamper_summary.json` and each `tamper_failures.json`, selects
instances, and runs `scripts/vecgen/run.py` once per problem dir. Episodes go to
`<data-dir>/problem_<slug>/` (`blocks_success` / `blocks_failure`), in the layout
`merge_datasets.py` collects.

| Flag | Default | Description |
|---|---|---|
| `--tamper-dir` | required | Directory from `--tamper_output_dir` |
| `--reasons` | all | Filter instances by outcome (`failure` / `timeout` / `success`) |
| `--max-instances` | `None` | Cap instances per problem dir |
| `--pddl-problem-file` | recorded | Plan every state toward this one problem; required when eval ran without `--queue_url` |
| `--skip-execution` / `--skip-annotate` / `--skip-merge` | off | Step toggles |
| `--exec-num-envs` | `32` | vecgen envs. Capped at the selected states and rounded up to a multiple of the scene-profile count. |
| `--record-videos` | off | Record the scene cameras. Annotation needs them; without, render the episodes, then annotate. |
| `--vecgen-args` | `""` | Extra `run.py` flags, as one quoted string, e.g. `'--max-attempts 2 --pool-slots 16'` |
| `--data-dir` / `--merge-output-dir` | under `--tamper-dir` | Output overrides |

The pipeline continues past a failed problem dir and exits non-zero with a summary
of which steps failed.

## Running the steps individually

### Step 3 — vecgen: plan, execute, record

The goal is unchanged; the failure state is the starting configuration. That is
the recovery demonstration.

```bash
python scripts/vecgen/run.py \
    --env-path outputs/tamper/round1/unknown_problem \
    --domain src/toyblocks/tamp/blocks/domain.pddl \
    --init-from-scene --reset-state-ids 0 1 2 3 --episodes 4 \
    --num-envs 4 --seed 0 \
    --record outputs/tamper/round1/datasets/problem_unknown_problem --mark-complete \
    --headless            # + --record-videos --enable_cameras for camera streams
```

`--reset-state-ids` index `reset_states.pkl`: instance *i* is the *i*-th entry in
that dir's `failures` list. Expect some states to fail. A failure state can be
genuinely unrecoverable for the scripted expert: a block shoved out of reach or
tilted on another, or the arm left pressed into the scene, which cuRobo reports as
`INVALID_START_STATE_WORLD_COLLISION`. Treat the success rate as signal about how
far off-distribution the policy has wandered.

### Step 4 — Annotate

Pixel goals project into the front camera, so the annotator needs recorded
cameras: `--record-videos`, or rendered episodes.

```bash
python src/toyblocks/data_annotation/annotate_target_xy.py \
    outputs/tamper/round1/datasets/problem_unknown_problem -j 8
```

### Step 5 — Merge

```bash
python scripts/datagen/merge_datasets.py \
    --input_dirs outputs/tamper/round1/datasets \
    --output_dir datasets/merged/train/tamper_round1 \
    --cameras all --num_workers 8
```

The recovery demos merge with your baseline data. The point of the loop is to
train on the union, not on the recoveries alone.

## Step 6 — Retrain and repeat

Retrain on baseline plus round-1 recoveries, evaluate again with
`--tamper_output_dir outputs/tamper/round2`, and iterate. Each round should show
the failure count dropping and the remaining failures moving to harder states.

## Worked example

Run end to end on one RTX 5090 (Nov 2026). The source was a
16-episode vecgen stack-3 dataset with 10 blocks per scene.

| Step | Command | Result |
|---|---|---|
| Eval package | `generate_task_from_dataset.py --task-name tamper_src` | 1 scene profile |
| Eval | `evaluate.py --random_actions --queue_url … --tamper_output_dir …` (4 envs, 4 s episodes) | 16 episodes, **16 states captured** (all `timeout`), 16 goals rebuilt from `pddl_goal` |
| Pipeline | `run_tamper_pipeline.py --exec-num-envs 8` | vecgen **12–13/16 SUCCESS** (two runs) in about 72 s. Every failure is `INVALID_START_STATE_WORLD_COLLISION`: the random policy left the arm in contact. |
| Merge | (part of the pipeline) | 12 episodes, 12,554 frames |
| With cameras | `… --reasons timeout --max-instances 4 --record-videos --exec-num-envs 4` | 4/4 SUCCESS, annotated, merged (5,092 frames) |

The recordings are recoveries: vecgen planned from what the random policy left
behind, re-planning from the live scene when a pick's effect check failed.

## Troubleshooting

**Nothing was captured.** Almost always `episode_length_s = 99999`: failing
episodes never end. Pass `--env-cfg.episode-length-s`. Also confirm the policy is
actually failing: successes are skipped unless `--tamper_capture_successes` is set.

**`no problems.json … and no --pddl-problem-file given`.** Eval ran without a
queue (no goal recorded), or the directory was captured before the vecgen port.
Pass the problem with `--pddl-problem-file`.

**`IndexError` in `flatten_state_dict` at env creation.** Autogen envs return an
empty `goal` observation group, which `--obs_mode state` cannot flatten. Use
`--obs_mode rgb --enable_cameras`.

**`the deferred PD-switch settle (enabled by --dataset_path) … needs control_mode
'arm_joint_gripper_binary'`.** `--dataset_path` with `--random_actions` (relative
control). Drop `--dataset_path` for random-action smoke tests.

**vecgen cannot load the directory.** The source env package was not found, so
nothing was cloned. The collector warns about this at capture time; pass
`--tamper_source_env_path`. `task_id` in `tamper_summary.json` is `null` when the
source package had no `__init__.py` to clone.

**`profiles.json … codegen version None`.** The env package predates the current
codegen. Regenerate it; it cannot be evaluated or replayed as-is.

**Merged dataset is empty or holds failures.** `merge_datasets.py` collects only
`problem_*/blocks_success`. Record under `<data-dir>/problem_<slug>` (the pipeline
does).

---- FILE: src_toyblocks_domain_randomization_YAML_REFERENCE.md ----

# Randomization yaml reference

The yaml is the single description of *what* gets randomized. It is the only place
randomization is configured, and the file is recorded in the output's `render_params.json` as the
dataset's visual provenance.

In this repository it is consumed by:

| Consumer | How it is named |
|---|---|
| `scripts/render/render.py` | `--flags` |
| `scripts/render/render_from_params.py` | reads the recorded flags back |
| `scripts/datagen/run_datagen_pipeline.py`, `scripts/datagen/run_playdata_pipeline.py` | `--render-pass FLAGS.yaml[:N]`, repeatable, one pass per look; there is no default |
| the library itself | `DRSession`, for in-process consumers |

The presets live in `src/toyblocks/domain_randomization/flags/`:

| preset | use |
|---|---|
| `render_flags_plain.yaml` | one fixed look, nothing sampled: the plain baseline |
| `render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml` | `allrand_texcache` plus the train glyph split (symmetry-preserving) and per-env block colours |
| `render_flags_allrand_texcache.yaml` | the production all-random lighting / materials / camera render, without glyph or colour swaps |
| `render_flags_camtest.yaml` | fixed camera overrides for quick local tests of the camera rig; randomizes nothing |
| `render_flags_open_hybrid_camera_rand_only.yaml` | camera randomization only |

The `allrand` presets sample backdrops from `polyhaven` and the 44 GB `indoor-2018` pool, installed
under `assets/environments/` (or `RENDER_HDRI_DIR`). Where to get each pool and what happens when
one is missing: [HDRI backdrops](../../../docs/source/user_guide/workflows/datagen/local.md#hdri-backdrops).

For what the renderer does with this file, see
[the rendering guide](../../../docs/source/user_guide/workflows/datagen/render.md);
for reproducibility guarantees, see
[DETERMINISM.md](../../../docs/render/DETERMINISM.md).

**Beware `render_flags_camtest.yaml`:** it is the one shipped preset with no random section at
all, so an `-N 4` run with it produces four pixel-identical copies while every size-based check
still reports 4x. Use it to test the camera rig, never to validate that randomization works.

### Validation

`validate_flags()` returns `(errors, warnings)`. An unknown key is normally a **warning, not an
error**, so a typo silently does nothing — check the startup log. The exceptions are
`randomize_task_letters` and `randomize_block_colors`, where an unknown or malformed key is a hard
**error** (`randomize_task_letters: unknown key(s) ...; only 'glyphs'`).

`config.py::TOP_LEVEL` is the allowlist, but it is **not** a complete list of what the code reads.
Three keys are read by the interpreter/build layer yet missing from it, so every file using them
warns on load even though they work:

| Key | Status |
|---|---|
| `couple_gi_to_env_sphere` | read, documented below, warns |
| `randomized_colored_lighting` | read at build time, warns |
| `dr_schema` | used by `canonicalize_flags`, ships in both `allrand` presets, warns |

`skybox.intensity_dist` is in the same position: it is read, but is absent from the skybox
allowlist, so a file that uses it warns.

## Value forms

Almost every numeric field accepts:

| form | meaning |
|---|---|
| `5` | fixed |
| `[min, max]` | sampled uniformly |
| `<field>_dist: log` | sample that range log-uniformly. Spelled `intensity_dist` **inside** the `skybox:` block, and `skybox_intensity_dist` at scenario level. |
| `auto` | derived from another quantity (only `fill_intensity`) |
| a probability in (0, 1) | a per-wave Bernoulli draw (only `skybox.visible_background`) |
| `intensity_auto_ratio` | on a local light: a scalar or `[min, max]` ratio resolved at wave time against the effective dome intensity |

## When each thing is drawn — this matters

| scope | concerns | keyed by |
|---|---|---|
| **per episode** | `materials`, `env_sphere`, `local_lights`, camera offsets (`randomize`) | `md5(seed \| concern \| episode_index)` under `hash` seeding — order-independent |
| **per episode, own RNG** | block glyphs (`randomize_task_letters`), cuboid colours (`randomize_block_colors`) | their own fixed per-episode RNGs — **not** affected by `--dr_seeding` at all |
| **per wave** (one batch of envs) | `scenarios`, dome/`skybox` intensity + rotation, `exposure`, `lighting_intensity` (`[min,max]` form), `scene_lights.fill_intensity`, `scene_lights.sun`, `skybox.visible_background` as a probability | a sequential RNG — **depends on how many waves have been drawn** |

Per-wave draws are *not* hash-keyed. Offline that is handled by `--fragment_invariant` (on by
default), which replays the full episode prefix so wave N really is wave N. In training it simply
means the scenario sequence depends on reset count.

## Top-level keys

### `carb_settings`
Raw carb settings applied at launch, e.g. the RT2 render mode:
```yaml
carb_settings:
  "/persistent/rtx/modes/rt2/enabled": true
  "/rtx/rendermode": RealTimePathTracing
```
⚠️ These become **launch kit_args**, and IsaacLab re-applies the `balanced.kit` preset *after*
launch (`simulation_context.py:742-745`), overriding ~15 keys — including the denoiser and
`dlss/execMode`. None of the shipped yamls collide, but if you set one of those keys here it is
silently discarded. Use `run_parity_ab --carb` (which writes `RenderCfg.carb_settings`) instead.

### `hide_objects`, `env_spacing`, `render_mode`, `lighting_intensity`
```yaml
hide_objects: ["backdrop"]   # prims removed before rendering
env_spacing: 500             # metres between envs; the YAML WINS over --env_spacing
```
`env_spacing` must exceed `2 × env_sphere.radius`, or a neighbour's backdrop sphere intrudes into
the side cameras.

`lighting_intensity` takes three forms, and they do **not** go through the same path:

| form | behaviour |
|---|---|
| `[min, max]` | sampled **per wave**, the intended form |
| a scalar | set **once at build time** on `/World/Light` |
| `"random"` | set once at build time from `uniform(200, 5000)` drawn from bare `np.random` — **not reproducible from any seed in this file** |

`validate_flags` only warns on a non-range value; it does not reject one.

### `skybox` — the dome light (global illumination)
```yaml
skybox:
  set: polyhaven/rooms          # or: sets / names / textures / textures_dir
  texture_format: latlong
  rotation_deg: [0, 360]
  intensity: [500, 1000]
  visible_background: false     # false = lights the scene but is not drawn
  seed: 0
  shuffle: true
  exhaust_before_repeat: true   # serve every unique texture before repeating
```
One dome for the whole wave — it is global, so it cannot differ per env.

### `env_sphere` — the visible backdrop
A large emissive sphere per env, so **each env can show a different background** in the same batch:
```yaml
env_sphere:
  sets: [{set: polyhaven/all}, {set: indoor-2018/all}]   # as in the allrand presets
                                                        # drops the second entry -- 1.8 GB not 46 GB
  exhaust_before_repeat: true
  shuffle: true
  seed: 7
  material: usdpreview
  emissive: true
  emissive_normalize: true          # scale each HDRI to a target median luminance
  emissive_intensity: [0.15, 0.28]  # the target when normalising
  emissive_clamp: [0.05, 100.0]
  cast_shadows: false
  backdrop_only: true               # visible to camera rays only, not to secondary rays
  radius: 200
  far_clip: 800                     # cameras' far clip is raised to see the sphere
  rotation_deg: 0
```
`emissive_normalize` is why dim HDRIs stay visible. Its queue is **stateful** — picks advance a
without-replacement queue.

### `scene_lights` — fill, local lights and the shared sun

`scene_lights` has three sub-keys: `fill_intensity` (with `fill_auto_ratio`), `local_lights`, and
`sun`.

`sun` is the single shared `DistantLight` for the whole scene, sampled **per wave**. For a
multi-env render this is the one to use: a per-env `local_lights` distant light is authored
per environment, which is not what a sun is. None of the four shipped presets uses it.

```yaml
scene_lights:
  fill_intensity: 0        # number | [min,max] | "auto"
  fill_auto_ratio: 0.35    # with "auto": fill = ratio × dome intensity
  sun:                     # ONE shared distant light for the whole scene, drawn per wave
    intensity: [300, 700]
    elevation: [28, 58]
    azimuth: [0, 360]
    angle: [0.1, 0.3]
  local_lights:
    link_per_env: true     # each env gets its own light, not one shared
    seed: 5
    count: 1
    lights:
      - type: distant                      # a sun
        intensity: [300, 700]
        color: {temperature: [4300, 6700]}
        angle: [0.1, 0.3]                  # angular size in deg — SMALLER = sharper shadows
        elevation: [28, 58]
        azimuth: [0, 360]
```

### `scenarios` — coordinated "looks", one per wave
The highest-leverage block. Each entry **overrides** the global levers for that wave:
```yaml
scenarios:
  seed: 123
  mix:
    - name: open_hybrid                 # soft and bright, no hard shadow
      prob: 0.4                         # relative weight; need not sum to 1
      skybox_intensity: [500, 1100]
      skybox_intensity_dist: log
      iso: [90, 145]
      fill_intensity: auto
      local_lights: false               # suppress local_lights this wave (see note below)
    - name: sun_shadow                  # darker, hard shadows
      prob: 0.6
      skybox_intensity: [150, 400]
      iso: [70, 110]
      fill_intensity: 0                 # no fill => high contrast
      sun: true
```
`prob`, `probability` and `weight` are synonyms (first wins). Contrast comes from **low GI + no
fill**, not from ISO.

**The key you type is not the key the interpreter sees.** Under `dr_schema: 3`,
`canonicalize_flags` renames `mix[].local_lights` to `sun` (and the top-level `global_distant` to
`sun`) before interpretation. So you author `local_lights: false`, and the key named `sun` is what
gates local lights internally. Older files still spell it `sun:` directly; both work, but
`local_lights` is what the shipped `allrand` presets use.

### `exposure` — camera response
```yaml
exposure:
  auto: false      # disable auto-exposure so scenario ISO actually takes effect
  iso: [70, 145]   # also fstop, shutter, iso_dist
  seed: 7
```
Scenarios that set `iso` force this path on automatically.

### `materials` — per-object surface randomization
```yaml
materials:
  table: {object: workspace_table, seed: 11}
```
A materials entry takes five keys, not two:

| key | default | meaning |
|---|---|---|
| `object` | the entry's own label | the scene prim to apply to |
| `library` | `toyblocks.TABLE_MATERIALS_FILEPATH` (override with the `RENDER_TABLE_MATERIALS` env var) | the materials JSON to draw from |
| `seed` | `0` | per-entry seed |
| `randomize` | — | a dict of ± jitter ranges, restricted to the eight jitter keys |
| `overrides` | — | per-material-**name** jitter overrides, mirroring `randomize.cameras.<cam>` |

`table` is a label; `object` is the scene prim. Materials come from the object's
`materials.json` library — texture, `albedo_add`, `albedo_brightness`, `texture_scale`,
`texture_rotate`, `texture_translate`, roughness, metallic. Each env has its own shader prim, so
every env in a batch can differ.

⚠️ A key a draw omits keeps the **previous episode's** value (materials bleed). `render.py
--material_baseline_revert` reverts to the asset's baseline first; it is opt-in because it changes
existing output.

### `randomize` — camera jitter
```yaml
randomize:
  position_offset_cm: [3, 3, 3]     # per-axis magnitude
  pitch_deg: 5
  yaw_deg: 5
  roll_deg: 2
  vertical_fov_deg: 3
  seed: 0
  cameras:                          # per-camera overrides
    gripper_camera: {position_offset_cm: [0.5, 0.5, 0.5], pitch_deg: 1}
```
⚠️ Offsets are drawn in **sorted camera order**, so adding a camera whose name sorts earlier
shifts every later camera's draw.

### `randomize_task_letters` — swap the glyph on every block
```yaml
randomize_task_letters: true      # default false; every block draws from all 36
```
The vocabulary is **36 glyphs: `A`–`Z`, `1`–`9` and `10`**. There is no `0` tile. `10` is the one
glyph whose token is two characters, so `[1-10]` spans ten glyphs and `block_10` is a valid
object name (the task generators never author one; blocks can only be swapped TO it).

The value takes four forms:
```yaml
randomize_task_letters: true                     # unconstrained: all 36, no repeats in an episode
randomize_task_letters: [C, D, E, 1, 3]          # a LIST (or a string): every block draws from it
randomize_task_letters:
  glyphs: [A-F, 1-5]                             # the same, spelled as a mapping with `glyphs`
randomize_task_letters:
  glyphs:                                        # a MAPPING under `glyphs`: per authored character
    A: [A-Z]
    7: [1-9]
```

**Two draws, not one.** `true` keeps the historical draw: one rng per episode picks all of that
episode's blocks *without replacement* from the 36, so no two blocks share a glyph. Every other form
is *constrained*: each block draws **independently** from the set its authored character allows,
so two blocks may land on the same glyph — routine once a set is small. They stay distinct PDDL
objects because copy indices are renumbered on rewrite: three blocks drawing `X` become `block_x`,
`block_x_2`, `block_x_3`, the convention `glyph_blocks.block_name` uses. `glyphs: "*"` therefore
allows the same 36 as `true` but draws differently.

A mapping is per authored character and acts as an **allowlist**:
```yaml
randomize_task_letters:
  glyphs:
    A: [A-Z]                      # A-blocks become letters
    7: [1-9]                      # 7-blocks become digits
                                  # every other character KEEPS ITS GLYPH

randomize_task_letters:
  glyphs:
    "*": [A-Z]                    # catch-all for characters not named
    I: [I]                        # pinned (confusable with 1)
    7: [1-9]                      # escapes the letters-only default
```
A rule keys on the **authored character**, so `A: [X-Z]` covers `block_a`, `block_a_2` and
`block_a_3` alike, each drawing on its own. Writing `F: [F]` and omitting `F` mean the same thing.

Entry grammar is three shapes — a character `A`, an inclusive range `A-F`, or `"*"` — and a list
unions them. Rejected at load with a specific message: `[0]` and `[0-5]` (no 0 tile), `[A-9]`
(mixes kinds), `[Z-A]` and `[10-1]` (backwards), and anything resolving to nothing.

⚠️ `*` is YAML's alias marker, so quote it in **both** positions: `glyphs: "*"` and `"*": [A-Z]`.

#### Train and test glyph splits

`render_flags_allrand_texcache_glyphs_trainsplit_symmetric.yaml` restricts the swap to the task
generator's TRAIN split (the 20 letters A-Z minus A, B, I, O, R, T, and the digits 1, 3, 5) and maps
every glyph only to a glyph of its own symmetry class, so goals that accept several orientations stay
correct; it also randomizes block colours over the train palette. The classes are the ones
`scripts/task_gen/stack_three.py` builds goals from:

| class | glyphs |
|---|---|
| upside-down and lower-case symmetric | `S X Z` |
| upside-down symmetric only | `H N` |
| lower-case symmetric only | `C P U V W` |
| neither ("plain") | `D E F G J K L M Q Y 1 3 5` |

and the colour palette is red, green, blue and white. Characters outside the train split keep their
glyph.

The symmetric split exists because a glyph's symmetry class decides which orientations read as
"the same character", so swapping across classes silently changes what an orientation goal means.

The preset is `render_flags_allrand_texcache.yaml` plus those keys, so it differs from an
unswapped render only in the block faces and the text. A list preset is constrained, so two
blocks can show the same glyph.

#### What gets rewritten and recorded

Per env, each block's glyph is moved on the shared decal atlas, and both `pddl_goal` and the
LeRobot `task` string are rewritten so the instruction still describes what the camera sees. One
"stack A on I on 2" dataset becomes many relabelled variants without re-planning or re-simulating
anything — the trajectory, the poses and the physics are untouched.

How it works: every block in `train_blocks_large` is the SAME USD with the decal mesh's `st`
shifted to a different 3×2 quadrant of one 16×16 atlas, and the decals material is `OmniPBR`,
which exposes `inputs:texture_translate`. So the glyph is one shader input per env — no USD
swapping, no extra materials. Applied in the same prender window as camera DR, so the RTX
warm-up sees the final letters.

| carrier | what happens |
|---|---|
| `pddl_goal` | rewritten, e.g. `(on block_a block_i)` → `(on block_x block_7)` |
| `task` (→ `meta/tasks.parquet`, `task_index`) | rewritten the same way |
| `observation.state.object_pose.block_*` | **unchanged** — parquet schema is per file, not per episode |
| `glyph_map` column | forward `{original_block: glyph}` per episode (the shape shipped datasets carry) |
| `block_variable_map` column | inverse, keyed by the GOAL token: `{"block_8": {"from": "block_a", "kind": "glyph", ...}}` — covers glyph blocks and colour cuboids; use it to find a goal token's pose column |
| `render_params.json` | `episodes[].block_randomization`, same keying, with the pose column |

Notes:
- Keyed on the episode's own `episode_index` (salted per concern), not the env slot or wave, so a
  shard renders the same glyphs as a full run.
- **Sharding must be problem-aligned.** Each process rebuilds the `meta/tasks.parquet` of every
  problem it touches; two processes holding parts of one problem would each write it, and the last
  writer wins. `render.py` refuses a slice that splits a problem (`randomize_task_letters needs
  PROBLEM-ALIGNED sharding`). The pipeline renders whole problems, so its slices are always
  problem-aligned.
- Widening the pool from 35 to 36 (when `10` became assignable) changed the unconstrained draw for
  a given seed; datasets rendered before it do not render with identical letters. Each episode
  is still self-consistent, because its recorded map drives both the pixels and the text.
- Only `type: usd` blocks with an authored glyph are swapped. If a block's decal shader is not
  found the run logs a **text/pixel mismatch** naming the blocks, because the strings are rewritten
  regardless and the dataset would otherwise claim a glyph it never drew.

Verify a run with `scripts/datagen/verify_glyph_swap.py` (labels each block with the glyph the
dataset claims) and `scripts/datagen/compare_glyph_runs.py` (asserts OFF is a no-op and that
only text changed).

### `randomize_block_colors` — recolour the procedural cuboids
```yaml
randomize_block_colors: true          # default false; the six dataset colours below
randomize_block_colors:
  colors:                             # or an explicit palette; HSV floats in 0-1
    - {name: red,    hsv: [0.0,                1.0, 1.0]}
    - {name: green,  hsv: [0.3333333333333333, 1.0, 1.0]}
    - {name: blue,   hsv: [0.6666666666666666, 1.0, 1.0]}
    - {name: yellow, hsv: [0.1666666666666667, 1.0, 1.0]}
    - {name: purple, hsv: [0.75,               1.0, 1.0]}
    - {name: orange, hsv: [0.0833333333333333, 1.0, 1.0]}
```
The colour sibling of `randomize_task_letters`. It owns the blocks whose env spec is
`type: cuboid` (spawned by `create_cuboid`); glyphs own `type: usd` blocks with an authored glyph.
The partition is by spec type, never by name (`block_b` is a letter block, `block_blue` a cuboid),
and a hard assert stops a run if both ever claim one block, so the two keys combine safely.

- The default palette is the six colours the generated env packages author, so a recoloured "red"
  is byte-identical to an authored red. HSV converts to linear RGB with no gamma, the units
  `UsdPreviewSurface.diffuseColor` takes. The mapping takes only `colors`; each entry needs exactly
  `name` and `hsv`, and one name cannot carry two colours.
- Drawn **with replacement**, independently per cuboid and per episode (keyed on `episode_index`),
  so two cuboids may share a colour ("the red block" can be ambiguous in a scene).
- `pddl_goal` and `task` are rewritten so the colour word matches the pixels, with tokens numbered
  in the dataset's style (`block_red1`, `block_red2`). A rewritten token can collide with another
  block's authored name — `block_orange` recoloured red becomes `block_red1` while the block
  authored `block_red1` turned blue — so look objects up through `block_variable_map` (keyed by the
  goal token), not by matching names to pose columns.
- Recorded per episode in the `cuboid_color_map` column and in `render_params.json`
  `episodes[].block_randomization` (`from`, `pose_column`, `color`, `hsv`, `rgb`).

### `couple_gi_to_env_sphere`
When only `env_sphere` defines a texture pool, take the wave's dome GI from the batch's **first**
env-sphere pick. If `skybox` also defines a pool the two stay independent and this is ignored.

## Debugging

- `[dr] WARNING skybox bucket resolved 0 textures` → your HDRI root is wrong; the backdrop will be
  black. Fix it with `render.py --assets_paths <root> [<root> ...]` (ordered extra roots, the
  repo default searched last) or the `RENDER_HDRI_DIR` environment variable. Each root may be an
  assets-root or an environments-root; the resolver auto-detects which.
- An unknown key is only a warning in most blocks — if a section seems to do nothing, check its
  spelling. Inside `randomize_task_letters` and `randomize_block_colors` it is an error instead,
  so those fail loudly.
- Every applied value is recorded per episode in the output's `meta/render_params.json`. The
  `episodes[]` entries carry `materials`, `skybox`, `env_sphere`, `exposure`, `scenario`,
  `camera_offsets`, and also `sun`, `local_lights`, `fill_intensity`, `lighting_intensity`,
  `split` and `block_randomization`. That file, from the run that produced your reference frames,
  is the ground truth for any comparison.
- To compare two shards, use the digests the file carries rather than diffing the YAML:
  `flags_sha256` identifies the literal file as written on disk, and `flags_resolved_sha256`
  identifies the **resolved** settings. Group shards by the resolved digest — two shards with the
  same one were rendered under identical settings even if the YAML was reformatted or moved, and
  they differ if a code-side default changed under the same file.
- `dr_seeding` is recorded top-level. Pass the recorded mode back when reproducing or patching a
  dataset; never mix two modes within one dataset.

---- DOCSTRING: src/toyblocks/vecgen/skills/flip.py ----
Reorient (scripted flip) skill, reusing the TAMP executor's flip geometry.

``ReOrientTrajectory`` (ported from the TAMP executor) holds the whole scripted flip
(edge/contact/pull waypoints, tip-offset measurement, IK anchor search with yaw and
seed candidates, drag resampling, retry escalation). Those helpers only need a robot
object with IK/FK and a simulator with scene access, so this skill feeds them thin
adapters over :class:`VecSim` / :class:`Geometry` and turns the returned joint-target
list into one segment per env. The IK calls are per env (not batched); flips are a
small fraction of an episode's ticks, so this is the reuse-first path.

Sequence, as in the old pipeline: plan to the pre-reorient start pose (0.2111 m above
the block, gripper yawed by the block's residual yaw), fully close the gripper, run the
scripted press-and-pull, retract, settle, then check ``ori_of``.

---- DOCSTRING: src/toyblocks/vecgen/skills/rotate.py ----
Rotate (scripted grasp-and-twist) skill, reusing the RotateTrajectory helpers (ported from TAMP).

Sequence (per sub-step; a rotate splits into an align correction plus the 90 deg step
when the block's spawn yaw pushes the total past 95 deg): descend onto the block, close
and attach, lift / twist joint 7 / lower, release, retreat (plus an inter-stage
clearance lift). The start pose and its IK check follow PreRLPoseGenerator.
