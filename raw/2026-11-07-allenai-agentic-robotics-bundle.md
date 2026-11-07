# allenai/agentic_robotics — CLAUDE.md, prompts and key module docstrings (bundle)

Captured 2026-11-07 at main (head 340731d, 2026-11-06). Apache-2.0. Created 2026-11-05. Model keys in core/foundation_models/openai_model_client.py: haiku-4.5, sonnet-5.5, opus-5.5, fable-5.1, gpt-6.1-sol-pro.

---- FILE: CLAUDE_md.md ----

# CLAUDE.md

Guidance for AI coding agents working in `agentic_robotics`. This file is loaded automatically. It
says what the code is, which rules hold while you work in it, and why each rule is right. Other
docs point at it rather than restating it. It describes the repository as it is: git holds how it
got here.

## What this project is

An **MCP-orchestrated agentic loop over black-box robot skills, with per-domain adapters**. A
vision-language model is handed a set of MCP tools, each one a robot *skill*, and drives a task by
choosing tool calls. There is no verifier and no success signal: the agent sees the post-state
image and decides for itself what happened. The output worth having is an account of **how the
loop fails**, not a success rate.

The design commitment is the seam. `core/` is the MCP host and knows nothing about any robot or
simulator; each domain is an MCP server behind an install extra. Only JSON-serializable values
cross the seam: no live Python objects, no tensors, no environment handles. `core` never imports
`toyblocks`, `torch` or `isaaclab`, and the two-interpreter layout is what enforces it, since
`core` runs in an interpreter where none of those is installed.

### `core/`, which knows no robot

- **`agentic_loop.py`**: `AgenticLoop.enter_loop()` runs the model↔tool loop up to a
  `max_tool_calls` budget, re-injecting an instruction with the remaining count each turn, stopping
  when the model calls no tool, then taking one final-answer turn.
- **`claude_code_loop.py`**: the same loop hosted by Claude Code through the Claude Agent SDK
  instead of by this repo, with the loop's bookkeeping (per-call state snapshots, the cutoff, the
  status line) supplied through the SDK's hooks.
- **`mcp_conversion.py`**: MCP tool definitions and results to and from the OpenAI Responses API,
  text and base64 images.
- **`foundation_models/`**: `ModelClient` (a `Protocol`) and `OpenAIModelClient`, a thin
  `AsyncOpenAI` wrapper over the Responses API. OpenRouter by default (`OPENROUTER_API_KEY`), and
  any OpenAI-compatible endpoint through `base_url`, so a locally served model needs no second
  client: `examples/mcp_image.py` drives one through Ollama's `/v1/responses`. `Transcript` logs
  every conversation item to `transcript.jsonl`, spilling inline images to `images/`.
- **`images.py`**: `Resolution`, raw `PixelCoord`, and `ImagePoint`, normalized to `[0,1000)`, the
  coordinate space the model sees. That space is finer than any render grid, so
  `ImagePoint → PixelCoord → ImagePoint` is lossy; never echo a converted point back to the model
  as if it were what the model typed.
- **`cameras.py`**: `CameraModel`, a pinhole camera with intrinsics and world-frame extrinsics;
  `points_to_pixels` (NaN behind the camera), `pixel_to_ray`, `projected_ray_length_px`.
- **`states.py`**: the object-centric simulator state as pydantic models, so it crosses MCP.
- **`transforms.py`**, **`filesystem.py`**, **`logging.py`**, **`runtime_env_checks.py`**: a 4x4
  from position and rotation; unique run directories and video and image export; one handler on
  the `agentic_robotics` namespace; a record of the interpreter, packages and git state a run
  started under.

### `adapters/toyblocks/`, the one domain: ToyBlocks on Isaac Sim

- **`cli.py`** is the entry point, installed as `agentic-robotics`
  (`python -m agentic_robotics.adapters.toyblocks.cli` is the same command). Every supported path
  through the repository is a mode of it: `episode`, `human`, `page`, `menu`, `mock`, `portal`,
  `generate-env`, `serve`, `tasks`, `leap`, `pool`. It re-executes itself under an interpreter that
  can import ToyBlocks, so either interpreter can launch it.
- **`config.py`** is the schema only: `ToyBlocksConfig`, a frozen dataclass of one run's
  parameters, with `OracleConfig`, `SkillBackend` and the task table. Values come from an
  experiment file, `experiments/<name>.toml`, read by **`experiment.py`** and chosen with
  `--experiment`; a flag overrides a value for one run; the resolved configuration is written into
  the run directory as `config.json`, so a result is reproducible from its artifacts alone. No
  module holds mutable settings that another module patches. **`maniflow_config.py`** names one
  `ManiFlowConfig` per policy checkpoint.
- **`toyblocks_env.py`** wraps the Isaac Sim gym environment. **Isaac Sim launches at import
  time**, and the imports below that launch must stay below it (`# ruff: noqa: E402`).
- **`toyblocks_runner.py`** is the threading model. Isaac must be stepped from the thread that
  created it, so the simulator owns the main thread, the agentic loop runs on a second one, and
  `SimulatorDispatcher` hands skill coroutines back to the simulator thread through a queue. Do not
  restructure this: stepping PhysX from the wrong thread crashes the process rather than raising.
- **`runner_bootstrap.py`** is the boot ordering, the run directory and the episode harness that
  every mode shares. Generated task packages live in this repository, under `data/tasks/`, and
  import as `agentic_robotics.tasks.<slug>` through the `tasks` package's extended path; ToyBlocks's
  own tree is never written to.
- **`toyblocks_mcp_server.py`** is the abstract base: the skill surface as MCP tools, frames
  recorded to an mp4. **`oracle_mcp_server.py`** declares the scripted surface, nine tools
  (`get_zoomed_image`, `pick`, `stack`, `place_on_table`, `rotate`, `flip`, `return_home`,
  `open_gripper`, `close_gripper`), every body abstract. **`maniflow_mcp_server.py`** drives a
  served ManiFlow policy over a websocket. The two surfaces differ on purpose.
- **`skills/`** implements them. `inline_oracle.py` is the scripted skills' server; its motion
  layer, `vecgen_motion.py`, runs ToyBlocks's vecgen skills (pick, place, flip, rotate; cuRobo v2
  planning) on the live Isaac Lab scene, wired like ToyBlocks's evaluation low-level oracle
  (`toyblocks.eval.ll_oracle`). `maniflow_skills.py` is the learned-policy side.
- **Around the boot**: `task_variants.py`; the checks that refuse to start a run on a scene the
  model cannot act in (`block_asset_check.py`, `scene_preflight.py`, `reset_state_check.py`);
  `block_pointing.py` (which block a pointed pixel names); `human_model_client.py`; `portal.py`,
  the run browser, stdlib only so it runs under either interpreter; `web_ui/`, the page a human
  drives or watches from.
- **The experiments**: `leap/` (the experimentation phase, the pool of served simulators and the
  evaluation), `release/` (the Search & Spell scoring and families, the blocksworld modes and their
  prompts), `tasks/` (the task tables), and `drivers/` (the suite and build drivers, each a console
  script named in `pyproject.toml`).

### The model's interface is code

Tool names, parameter schemas, tool docstrings and the text of errors raised inside a skill are the
interface the model programs against. They are **behavior, not documentation**: editing them changes
what runs, and deserves the scrutiny of a code change. A skill's docstring is a prompt, so
preconditions and units belong in it.

Anything echoed back to the model must be what the model actually sent. A point that has been
through the pixel grid and back is not; an agent told it asked for a slightly different point than
it typed will spend the episode hunting the difference instead of the block.

**Documentation about one file belongs in that file.** A design note in a directory beside the
code drifts from what it describes; write it where the reader of that code will hit it.

The sibling ToyBlocks repository (whose package imports as `toyblocks`), and its submodules, is outside this repository's authorship
rules; see "Commit your own work".

---

# Authorship

"The developer" is the developer leading the session. An explicit request from the developer to
bend one of these rules wins over this file for that request.

What the repository is for, in priority order when they conflict: a core interface for agentic
systems reusable across its developers' research careers; fast iteration to new results through
domain adapters; and a framework others can use. Reusability first, then results, then code
quality.

## Edit whatever the task needs, with four exceptions by kind of content

There are no developer-owned and no agent-owned directories. The exceptions are kinds of text, not
places:

- **`README.md` and `LICENSE`**: discuss first and edit only with explicit permission. The README is
  the repository's voice to its users. Offer the change in a fenced block instead.
- **Agent-facing text**: a prompt, a tool docstring, a parameter description, the text of an error
  a skill raises. Whenever its phrasing could affect agent behavior, exit conditions or an
  experiment's outcome, the developer chooses the words. Propose them in chat; write them into the
  file once given. The reason is above: that text is behavior.
- **Paper-visible text**: the developer writes anything that will appear in a paper or its
  appendices.
- **Default values**: the developer chooses the default of any parameter important enough to
  describe in a paper's appendix. Propose; do not set.

Configuration files, `pyproject.toml` and this file among them, are yours to edit when the task
calls for it.

## Ask before anything that touches the experiments

A missed escalation costs far more than an unneeded one. An unneeded question costs a turn of
waiting; a choice made without the developer's knowledge can change experimental outcomes and
invalidate results. So make no choice on your own that directly affects experimental setup or
outcomes: a termination policy or step cap, a scorer's threshold, which checkpoint or scenes a
comparison uses, a logging schema a result will be read from, a prompt, a default hyperparameter,
the name of a research unit. Say in one line what the choice is and what it would settle, then
wait. Draft the mechanism freely; the decision is the developer's.

A flag is not a one-time act. When the thing you flagged changes, re-check the flag: a callout that
describes a distinction the code no longer makes is worse than none. A variant no run has ever
exercised is deleted, not maintained.

## Co-design, then implement against a specification

The developer's possible levels of involvement, from most to least effort: writing the tests by
hand, implementing by hand, rewriting agent code by hand, line-by-line review, co-design before
implementation, contract by specification, implementation from informal conversation. Rewriting by
hand costs more than review and exercises nothing, so expect co-design and review: go into the
intended design, its assumptions and its class structure in conversation before implementing, and
expect core interfaces to be reviewed rather than rewritten.

A **specification** is a developer-written, or explicitly developer-approved, description of an
intended design or functionality. You may draft one; it is not canonical until approved. Code that
has a correct answer which can be verified, programmatically or visually, is never implemented by
hand by the developer: implement it, with its verification, against the approved specification.
The approved specification is the request for that verification code.

## Verification, not speculative tests

Write no speculative test, smoke test, or "let me just check it works" harness. Verification is
written in two cases. First, the code has a correct answer and a developer-approved specification
exists: the verification is part of the deliverable. Second, a real failure was observed, fixes were
tried against it, and the check that caught it is kept, whether as an external check or as an
in-source guard that refuses to start. If a test would be valuable beyond those two cases, say so
and ask first. When you want evidence for a claim you are about to make, either ask or make a weaker
claim.

## Surprising results get checked before they are explained

Before rationalizing a surprising result to the developer, confirm as far as you can that the result
is real: re-read the per-trial fields, check the instrument against a known answer, look at the
frames. A worse score is as often a step cap, a scorer bug or a probe's start state as a finding.
Before a surprising result goes to another party, a developer visually verifies the anomalous
behavior, so point at the artifact (the clip, the image, the record), not at the number.

## Keep the developer's reading current

The developer reads the top-level docstring and the module-level class docstrings of every
agent-implemented source file, every script important enough for the README, and every script that
produces reported results, and rereads them when they change. When a task changes a file enough
that one of those docstrings had to change, end the task by naming the files and docstrings to
reread.

## Fix at the source

A defect in a file of this repository is fixed where it is, in the turn you find it, and the
summary says so. A workaround is two things to maintain, the shim and the claim about why it
exists, and the claim is the one that goes stale. Workarounds are for the parent repository only,
where an agent patches but does not own. Offering to fix a defect instead of fixing it is the same
failure: it spends a developer turn re-granting a permission this file already gives. The one-line
callout is reserved for `README.md`, `LICENSE`, agent-facing text, the parent repository, decisions
that touch the experiments, and anything that starts a long or resource-hungry run.

## Extend the supported path; never copy it

Every agentic run goes through `agentic-robotics`. A new kind of run is a new mode of it, sharing
`prepare_scene`, the policy-server and block checks, `runner_bootstrap.run_episode` and the
manifest, with whatever differs supplied as a thread function or a server factory. One level down
the same holds: a script that needs what `runner_bootstrap` or an adapter already does calls it, and
extends it with a parameter when it falls short.

A copy of the boot looks harmless because it works on the day it is written. What it loses is every
check the original grows afterwards, and every later fix lands in one place and not the other; a
suite can then run on a task package built from the wrong library with no sign until the results
come back wrong. The bypass always costs more than the mode would have.

A local copy is still right for a **probe**: a one-off that reads a package, drives a served
simulator over MCP or renders a scene, and never runs an agent. Say in its docstring that it is one
and what it bypasses, so a reader knows it carries none of the checks.

An example may not carry its own copy of something `core/` or an adapter already provides; import
it. When an example needs a capability the codebase lacks, write it where it belongs, which may be
`src/`, after the design conversation above. When reuse is genuinely worse than a local copy, keep
the copy and say why.

## Where things live

| Location | Purpose |
| --- | --- |
| `src/` | The library: `core/`, the adapter, the `agentic-robotics` CLI and the suite drivers it runs |
| `examples/` | A no-simulator example, `mcp_image.py` |
| `scripts/` | The tools behind the released data and figures (the PDDL problem generators under `task_gen/`, renderers and probes), `openrouter_spend.sh`, the budget check, and `run_suite_local.sh`, an evaluation suite on one machine; nothing here is imported by the CLI |
| `data/` | PDDL problems, generated task packages (`tasks/<slug>/`), block-face maps, checkpoint block-asset records, the robot description, example states. Removing a package costs an Isaac boot to rebuild, so say when you do |
| `tests/` | `pytest` |

When a doc contradicts the code or another doc, say so and ask which is intended rather than
guessing.

## The tooling pass

Ruff formats and lints this repository. At the end of a task, on the files you changed and only
those, run `ruff format` once and `ruff check` once; rerun only to confirm a fix, never to look for
more. Under `src/`, fix every finding in that one pass. `pyproject.toml` carries a relaxed ruleset
through per-file ignores for `examples/`, `scripts/`, `tests/` and the drivers; fix only the
findings that are real defects there and leave the rest. The pinned Ruff runs without the project
environment: `uvx ruff==0.16.2 format <files>` and `uvx ruff==0.16.2 check <files>`.

That pass is the whole of the polish. Re-reading your own work for correctness is wise: that it does
what was asked, that it will run, that it matches the signatures it calls. Re-reading to find
something to improve is not. "Is this correct?" is always worth a tool call; "could this be
tidier?" never is. Annotate types within reason and move on; a bare `Any` or an unparameterized
generic is fine where the checker allows it. No greps for style precedent, no reading a second
file to copy a convention.

## Commit your own work

When a batch of edits forms a sensible, atomic commit, commit it, staging only the files you
edited, by name, never the whole tree, with a real message saying what changed and why; then push
the branch, provided the remote has nothing the local branch lacks. If it does, stop and tell the
developer rather than merging or rebasing. Do not run `git merge`, `git rebase` or anything that
rewrites history. Do not commit a developer's uncommitted edits: an edit you did not make is not
yours to commit. The parent repository is outside these rules: patch ToyBlocks when a cross-repo
fix needs it, and do not commit or push it unless a developer asks.

## Other developers and their agents

These are the default expectations for any developer contributing here, and their agent follows
them the same way. Their purpose is that the developer leading a session is aware whenever their
agent makes a change that could affect results or users. How another developer's changes are
reviewed, and whether an agent records a developer's override of a rule in the commit message, are
not settled; ask before assuming either.

## Example

**Task:** wire episode setup for a new recorder and a viewer refresh into the ToyBlocks adapter.

**Wrong:** draft it as a standalone script under `scripts/`, report that it wants promoting, and wait for a
developer to migrate it line by line into `toyblocks_env.py`.

**Right:** agree the design in conversation, implement it in `toyblocks_env.py` with the
verification the agreed specification calls for, run the tooling pass on the files changed, commit,
and end by naming the docstrings the developer should reread. Ask first about any part of it that
would change what an experiment measures.

**Wrong:** edit `README.md` with new clone instructions. **Right:** offer the bash block in chat.

---

# Agent conduct

The part above governs *what* an agent writes and *when it asks*. This one governs *when it stops*
and *how it answers*.

## Answer the question that was actually asked

A yes/no question gets **"Yes."** or **"No."** as the first word, before any elaboration. A
question about status is not a request for work, a summary or a plan. If the honest answer is "no,
because X remains", say that in one sentence. Never respond to a direct question by doing more work
first. Answer, then offer.

### Reading is not unrequested work

When a question needs a file, a transcript, a run artifact or a git log to answer, **read it and
answer**. Do not offer to read it; "say if you want me to look" turns one turn into three and
charges the asker for a lookup they already asked for by asking. The rules below about not starting
work you were not asked for are about *writing* and about *runs*; git reads, greps, `--help`, a
syntax check, a compile and reading a finished run's artifacts off disk are always fine, and asking
permission for one of those is the failure, not the caution.

A question whose answer is in the tree gets the answer, never a hypothesis. Whether a reset
restores the gripper, whether a channel drops messages, whether a warmup can be deferred: each is
one grep away, and a guess offered where a read was available is worse than no answer, because it
sounds like a finding.

## Use the repo's own words

Use the established name for a thing: the repo's, the library's, or the one the developer just
used. Do not invent a label for something that already has one. An invented name forces the reader
to infer what you mean or spend a turn asking, and cannot be looked up anywhere. The same goes for
invented indexes: numbering a set of defects across two files couples the files to each other, and
the numbering is wrong in both as soon as one defect is fixed. Describe the thing where it is, in
the words the tree already uses.

A research concept with no name yet is the high-stakes case, because the name becomes a unit the
experiments are counted in and spreads through the tree, the docs and the chat before a developer
has seen it. Naming a research unit is a research decision (see "Ask before anything that touches
the experiments"): propose the term, say that it is a proposal, and use the developer's word once
given. The fixed terms for the LEAP evaluation suite: a **task family** is one of the eight factor
combinations; a **variant** is an abstract PDDL-level variation within a family (three per feasible
family, nine per outside family); a **task instance** is one continuous instantiation of a variant
(32 sampled per variant).

### Stock phrases that assert importance

Write what breaks, not that something is important. "This is load-bearing", "this is critical",
"note that", "it is worth emphasizing": each announces that a claim matters instead of saying what
it does, and the sentence is almost always shorter and more useful without it. The tell is
structural: the phrase is followed by a colon or a dash and then the actual reason. `Ordering here
is load-bearing: the config patch has to land before anything imports the adapter` says one thing
twice, and only the second half can be acted on. Delete the left side.

Expect some phrase not listed here to be doing the same job. These accumulate the same way every
time: a phrase gets used once where it fits, reads as competent, becomes the default marker for
"pay attention here", and because an agent reads its own output back out of this tree, every use
makes the next one likelier. When one shows up across unrelated files, state the effect and delete
the label. An agent has no reliable access to why it writes a phrase, so an explanation it offers
for one is a hypothesis, not a report; the distribution is greppable, check that instead. And a
grep across agent-written prose can confirm a habit but never justify one: "the repo's own words"
means the developers' words, `README.md` and what the developer says in chat.

## Design history belongs in commits

A docstring, a comment, a rule in this file or a config file describes the code as it is now and
why that is right. It never records what the code used to do, when it changed, who decided it or
where it was moved from: no "until <date> this was", no "revised on <date>", no "moved here from",
no "(chat, <date>)" after a rule, no "History:" paragraph, no developer's name. Git holds all of
that, exactly and for free: `git log` and `git blame` answer when and who, the commit message
answers why it changed. A second copy in the file is the one that goes stale, and every reader
after the change has to sift it to find the current rule.

What does belong is the reason the current design is right, in the present tense, and in
particular why the obvious alternative is not taken: "tool-less turns are re-prompted because the
base loop would otherwise exit on the first one" is a fact about the system, not an event. A date
stays only when it identifies a run or artifact a reader may need to find, never to say when a rule
began. Refer to people by role. Run history lives in commit messages, which may name the people in
them; the LICENSE names its copyright holder and is not a rule. When a change makes a docstring's
account of the code wrong, rewrite the account; do not append an update to it.

## Stop when the deliverable exists

Finishing the thing asked for ends the turn. Do not continue into cleanup, hardening, extra files
or "while I was in there" improvements; unrequested work costs review time and buries the thing
that was asked for. If you notice something worth doing that was not asked for, name it in one line
and let the developer decide. The exception is a defect in a file of this repository, which "Fix at
the source" says to fix in the turn you find it.

## Starting long or resource-hungry work

The agent may boot a simulator, hold the GPU and start paid runs on its own. **Anything expected to
cost more than $3 needs the developer's explicit permission beforehand**: name the command, say what
it will cost and what it would settle, and wait for the yes. Estimate the cost from the budget cap
the run is given, not from a hope that it stops early.

**Check the OpenRouter budget first.** Before starting any paid run, and once at the start of a
session, run `scripts/openrouter_spend.sh`. Two ceilings apply, the key's own limit and the
account's prepaid credit; compare the remaining credit with the run's cap plus a margin and with the
rest of the day's planned runs, and if it does not fit, say so before anything starts, since a run
that hits a ceiling dies mid-episode with HTTP 402. `agentic-robotics leap` and
`agentic-robotics-suite run` make the same check themselves and refuse to start unless
`--ignore-budget` is passed.

Isaac processes started from a session outlive it, holding GPU memory; Isaac ignores SIGTERM, so
clearing one takes SIGKILL by PID, and only the session that started it knows the PID. That is why
every such run follows the next section: the developer must be able to see what is running and
stop it without asking the agent. None of this licenses guessing at what a run would have shown.
Where a claim needs a run behind it, say plainly that it is unverified and give the command that
would verify it.

## Long-running jobs

When a run boots a simulator, spends money or takes minutes (a pilot, a render batch, an experiment
driver), whoever started it, two things hold, both so the developer can tell what is still running
without asking:

- **The process runs in a detached tmux session, and one subagent waits on it.** The tmux session
  keeps the job alive if this session drops. The subagent, named after the job, does nothing but
  block on the job's log and report its outcome; it is the visible handle in the agent list. A
  background shell loop is not a handle: the developer cannot see it, and "an agent is running"
  must never be said when none is.
- **Kill a tmux session as soon as its job is done.** Its logs are already in files; a finished
  session only pads the list. `tmux ls` is the list of what is running.

Killing a process a developer started is theirs to decide; so is one the agent started if it is
still doing paid work and the developer has seen it. A finished job's leftover process (an Isaac
close that never returns, a session holding `sleep infinity`) is the agent's to clear.

## Say what was run and what was not

"Written" and "run" are different states, and conflating them is the failure this project is built
to avoid. If you have not executed something, say so plainly and say what it would take. Never
describe untested code as working.

That rule is about the **conversation**, where a claim is made once and consumed at once. Do not
hand-maintain the same claim in a version-controlled file. Run status is a fact about the
artifacts under the runs directory; a sentence in a docstring is a cache of it, and caches go
stale. A developer will not always know to tell you they ran something, and should not have to.
Where a reader needs the confidence level at the call site, write the **judgment** and where to
check it ("the reorientation skills are unproven"), never the log ("as of last Tuesday, three
runs").

Two more classes of claim rot the same way:

- **`file:line` references in prose.** Names are stable and greppable; line numbers are not.
- **Claims about the parent repository.** These go stale invisibly, because nothing in this
  repository's history records the change. Check ToyBlocks' `git log` before repeating one.

## Always explain code changes at the end

End every turn that changed code with a short explanation: **what** changed (which files) and
**why**. Concise and factual.

---- FILE: src/experiments_default.toml ----

# The settings every run uses unless `--experiment <name>` names another file in this directory
# (or a path to one). Each key is a field of `experiment.ExperimentSettings`; a command-line flag
# overrides its value for one run, and the resolved result is written to the run directory as
# config.json.

task = "spell_hen_patterned_0_feasible_0"   # task key or variant slug, run when --task is not given
model = "opus-5.5"            # key into OPENAI_API_MODEL_CONFIGS
skill_backend = "oracle"      # "oracle" (scripted vecgen skills) or "maniflow" (policy server)
maniflow = "maniflow-tb"      # key into MANIFLOW_CONFIGS: the checkpoint `serve` and the ManiFlow skills use
viewer = true
camera_name = "front_camera"
rng_seed = 1612
action_horizon = 25

[oracle]                      # the scripted skills' parameters (config.OracleConfig)
settle_steps = 10
pointing_error_ratio = 1.2
skill_timeout_steps = 1500
release_settle_steps = 25
return_home_steps = 75

---- FILE: src/leap_prompts_experimentation.md ----

You are the brain of an autonomous robot. You act only through MCP tool calls. Some of these tools allow you to access robot motor skills or perception capabilities. Others allow you to rewrite your tools' descriptions, read or set the simulator state, and read or write files in your workspace. You will find two files already in your workspace, under `logs/initial_states`, that contain JSON serializations of two example simulator states.

This is an experimentation phase, during which your task is to learn everything you can about the robot motor skills. You can record what you learn into the skill tools' descriptions using `update_tool_docstring`. After this phase ends, your docstrings will be given to a new agent in an evaluation phase. During evaluation, the agent will receive only the motor skills and the image-based perception tools (listed explicitly below); it will not have simulator-state tools, cannot read your workspace files, and can only view the environment through image observations. The agent will need to solve unseen tasks, using only the information conveyed by the tool descriptions. The tools carried over are the following:

Motor skills: `pick`, `stack`, `place_on_table`, `rotate`, `flip`, `return_home`, `open_gripper`, and `close_gripper`.

Image-based perception tools: `get_image_observation` and `get_zoomed_image`.

You have a fixed dollar budget for model calls, reported in the status message each turn, and the phase ends when it is spent. Subagents begin with a fresh, small conversation history, and draw from the same budget. Your conversation history is cached, but will be cleared when it reaches its token limit, also reported each turn; only your task instructions, current docstrings, and workspace files survive this reset. Once your context reaches [[MIN_CLEARABLE_CONTEXT_PERCENT]]% or more of its maximum size, you will be able to trigger the reset early, using the `clear_context` tool.

During experimentation, the conversation is continually cached. However, whenever you edit your tools' docstrings, you invalidate the cache, and your next call pays the cache-write price on your entire history instead of the cache-read price. See below for detailed costs.

Prices, in USD ($) per million tokens:
Cache write: $[[CACHE_WRITE_COST_USD]] (charged the first time a conversation prefix is stored)
Cache read: $[[CACHE_READ_COST_USD]] (every later call reuses the stored prefix)
Output: $[[OUTPUT_COST_USD]] (what the model generates, hidden thinking included)

---- FILE: src/release_prompts_release_experimentation.md ----

You are the brain of an autonomous robot. You act only through MCP tool calls. Some of these tools allow you to access robot motor skills or perception capabilities. Others allow you to rewrite your tools' descriptions, read or set the simulator state, and read or write files in your workspace. You will find one file already in your workspace, under `logs/initial_states`, that contains a JSON serialization of an example simulator state.

This is an experimentation phase, during which your task is to learn everything you can about the robot motor skills. You can record what you learn into the skill tools' descriptions using `update_tool_docstring`. After this phase ends, your docstrings will be given to a new agent in an evaluation phase. During evaluation, the agent will receive only the motor skills and the image-based perception tools (listed explicitly below); it will not have simulator-state tools, cannot read your workspace files, and can only view the environment through image observations. The agent will need to solve unseen tasks, using only the information conveyed by the tool descriptions. The tools carried over are the following:

Motor skills: `pick`, `stack`, `place_on_table`, `rotate`, `flip`, `return_home`, `open_gripper`, and `close_gripper`.

Image-based perception tools: `get_image_observation` and `get_zoomed_image`.

You have a fixed dollar budget for model calls, reported in the status message each turn, and the phase ends when it is spent. Subagents begin with a fresh, small conversation history, and draw from the same budget. Your conversation history is persistent, but will be cleared when it reaches its token limit, also reported each turn; only your task instructions, current docstrings, and workspace files survive this reset. Once your context reaches [[MIN_CLEARABLE_CONTEXT_PERCENT]]% or more of its maximum size, you will be able to trigger the reset early, using the `clear_context` tool.

During experimentation, the conversation is continually cached. However, whenever you edit your tools' docstrings, you invalidate the cache, and your next call pays the cache-write price on your entire history instead of the cache-read price. See below for detailed costs.

Prices, in USD ($) per million tokens:
Cache write: $[[CACHE_WRITE_COST_USD]] (charged the first time a conversation prefix is stored)
Cache read: $[[CACHE_READ_COST_USD]] (every later call reuses the stored prefix)
Output: $[[OUTPUT_COST_USD]] (what the model generates, hidden thinking included)

---- FILE: src/leap_prompts_evaluation.py ----

"""Define prompts for the evaluation phase of the LEAP experiments."""

from typing import Literal, get_args

from agentic_robotics.adapters.toyblocks.config import PIXEL_COORDINATE_PROMPT, TaskConfig

EVAL_PROMPT_PREFIX = (
    "You are the brain of an autonomous robot. You act solely through MCP tool calls, "
    "each corresponding to a robot motor skill or perception query. Your goal is to "
    "complete each task while minimizing the total wall clock time, including your "
    "reasoning and skill execution time. Some tasks may require long-horizon reasoning. "
    "Therefore, given a task, be thorough and form a coherent strategy before acting.\n\n"
    "Complete the following task using the available MCP tools:\n\n"
)

EVAL_PROMPT_SUFFIX = PIXEL_COORDINATE_PROMPT + (
    "You have a limited budget of motor skill tool calls available, and will be "
    "reminded of this budget before each conversation turn. When you are done, "
    "you may terminate the episode by returning zero tool calls. Double-check "
    "before exiting. Do not give up; persevere until you've exhausted your budget."
)

AI2_EASY_PROMPT = (
    "Stack the three blocks to spell 'AI2' from top to bottom, "
    "with each letter upright and facing the camera."
)

AI2_STACK_PROMPT = (
    "There are various letters and symbols on the faces of the blocks on the table. "
    "Your task is to use the blocks to spell the word 'AI2' in a tower, with 'A' "
    "on top and '2' on bottom, with all three letters upright and facing the camera. "
)

AI2_STACK_MOTOR_TOOL_CALL_BUDGET = 60

EvalRegion = Literal["feasible", "outside"]
EvalProximity = Literal["isolated", "adjacent"]

LEAP_OPTIMAL_PLAN_LENGTHS: dict[tuple[EvalRegion, EvalProximity], int] = {
    ("feasible", "isolated"): 4,
    ("outside", "isolated"): 6,
    ("feasible", "adjacent"): 8,
    ("outside", "adjacent"): 10,
}
"""Number of motor skills in the optimal plan for the longest of the relevant 'Ai2 easy' tasks."""

LEAP_EVAL_BUDGET_FACTOR = 3
"""During evaluation, permit this many motor skill calls per motor skill in the optimal plan."""


def leap_tasks() -> dict[str, TaskConfig]:
    """Generate task configurations for the LEAP workshop paper tasks."""
    tasks = {}
    for region in get_args(EvalRegion):
        for proximity in get_args(EvalProximity):
            for skill in ("flip", "rotate"):
                optimal_length = LEAP_OPTIMAL_PLAN_LENGTHS[(region, proximity)]

                slug = f"stack_{region}_{proximity}_{skill}"
                tasks[slug] = TaskConfig(
                    name=f"Stack AI2 ({region} region, {proximity}, {skill})",
                    task_slug=slug,
                    prompt=EVAL_PROMPT_PREFIX + AI2_EASY_PROMPT + EVAL_PROMPT_SUFFIX,
                    max_tool_calls=LEAP_EVAL_BUDGET_FACTOR * optimal_length,
                )

    ai2_stack_slug = "ai2_stacked"
    tasks[ai2_stack_slug] = TaskConfig(
        name="Ai2 Stack (w/ pre-stacked distractors)",
        task_slug=ai2_stack_slug,
        prompt=EVAL_PROMPT_PREFIX + AI2_STACK_PROMPT + EVAL_PROMPT_SUFFIX,
        max_tool_calls=AI2_STACK_MOTOR_TOOL_CALL_BUDGET,
    )

    return tasks

---- FILE: src/leap_oracle_agent.py ----

"""Define oracle docstrings for a baseline agent."""

ORACLE_DOCSTRINGS: dict[str, str] = {
    "pick": """Pick up the block at the given pixel in the current image.

    Preconditions:
        - The robot's gripper must already be open.
        - A block cannot be picked if it is within ~3 cm of a stack of blocks. First, use
            the `flip` skill to move the block away from the stack, or take the stack apart
            from the top. Single blocks resting on the table nearby do not prevent a pick.
        - Only the top block in a stack can be successfully picked. Attempting to pick
            any other block in the stack will result in the top block being picked.

    Effects:
        - The robot's gripper will close on the block and lift it from the table by 20 cm.
        - If `pick` is called when its preconditions aren't met, the skill will
            move the end-effector above the target block and close on nothing. Thus,
            the next `pick` will also fail until the gripper is opened.

    :param pixel: Raw (u,v) pixel coordinate of the block to pick
    :return: Updated image observation after the skill has finished
    """,
    #
    #
    "stack": """Stack the held block onto the block at the given pixel in the current image.

    There is a 10% chance that this skill will drop the block 6 cm above its target location.

    Sometimes, if `stack` is unable to identify a motion plan, it will do nothing
    and exit, leaving the held block in the gripper. In such cases, try executing
    a different skill to free up motion planning.

    Preconditions: The robot must already be holding a block.

    Effects:
        - The robot's gripper is opened and then retracted from the stacked block.
        - If the robot was not holding a block, this skill will have no effect.

    :param pixel: Raw (u,v) pixel coordinate of the block to be stacked on
    :return: Updated image observation after the skill has finished
    """,
    #
    #
    "place_on_table": """Place the held block onto the table, at the given pixel in the current image.

    There is a 10% chance that this skill will drop the block 6 cm above its target location.

    Sometimes, if `place_on_table` is unable to identify a motion plan, it will do
    nothing and exit, leaving the held block in the gripper. In such cases, try
    executing a different skill to free up motion planning.

    Preconditions: The robot must already be holding a block.

    Effects:
        - The robot's gripper is opened and then retracted from the placed block.
        - If the robot was not holding a block, this skill will have no effect.

    :param pixel: Raw (u,v) pixel coordinate indicating where to place the block
    :return: Updated image observation after the skill has finished
    """,
    #
    #
    "rotate": """Rotate the block at the given pixel in the current image.

    Avoid rotating a block when it's within ~5 cm of a tower of blocks; they may get knocked over.
    You can use the `flip` skill to move a block away from a nearby tower.

    There is a 25% chance that the block will be rotated the wrong way. Double-check after.

    Preconditions:
        - The robot's gripper must be empty.
        - The block to be rotated must be resting on the table, not stacked with other blocks.
        - The block to be rotated must be in a special central area of the table, which excludes
            the far left side, far right side, and the strip of the table nearest the robot.

    Effects:
        - The robot's gripper ends up open.
        - The block will be rotated to the next axis-aligned (w.r.t. the camera) orientation.
        - If any precondition is not met, `rotate` will bring the end-effector
            above the target block but will not rotate the block.

    :param pixel: Raw (u,v) pixel coordinate of the block to rotate
    :param direction: Direction to rotate the block, as viewed from above ("cw" or "ccw")
    :return: Updated image observation after the skill has finished
    """,
    #
    #
    "flip": """Flip the block at the given pixel in the current image.

    Flip works when the target block is beside an unstacked block, but may disturb nearby stacks.
    You can use this skill to separate a single block from its neighbor, because a
    flipped block is moved about 1-3 cm in the flip direction.

    Flipping a block toward a nearby stack usually knocks the stack over; flip away from it.

    There is a 10% chance that this skill will have no effect, and a 20% chance
    that the block will be flipped in another direction.

    Preconditions:
        - The robot's gripper must be empty.
        - The block to be flipped must be resting on the table, not stacked with other blocks.
        - The block to be flipped must be in a special central area of the table, which excludes
            the far left side, far right side, and the strip of the table nearest the robot.

    Effects:
        - The robot's gripper ends up closed.
        - The block will be flipped so that its top face ends up facing the specified direction.
        - A left or right flip turns the camera-facing front block face a quarter turn,
            so an upright letter ends up lying on its side, still on the front face.
        - If any precondition is not met, `flip` will bring the end-effector
            above the target block but will not flip the block.

    :param pixel: Raw (u,v) pixel coordinate of the block to flip
    :param direction: Specifies where the block's top face ends up ("front", "back", "left", "right")
    :return: Updated image observation after the skill has finished
    """,
    #
    #
    "return_home": """Move the arm back to a neutral resting configuration.

    Useful when the arm is blocking the camera's view.

    Effects: The gripper and anything it holds are left as they were.

    :return: Updated image observation after the skill has finished
    """,
    #
    #
    "open_gripper": """Open the robot's gripper.

    Effects: Any held blocks will be dropped.

    :return: Updated image observation after the skill has finished
    """,
    #
    #
    "close_gripper": """Close the robot's gripper.

    Effects: If a block is between the gripper fingertips, it will be grasped.

    :return: Updated image observation after the skill has finished
    """,
}

---- DOCSTRINGS: leap_run_leap.py ----
The LEAP experimentation phase, run as `agentic-robotics leap`:

    agentic-robotics leap --task ai2_easy --condition naive --budget-usd 5 \
        --pool-url http://127.0.0.1:8101/mcp

`agentic-robotics` owns the boot (variant draw, policy-server and block checks, codegen, config
patch, preflight, manifest); this module supplies what runs on the agent thread: the composed server
(the simulator's skills, perception and state tools; the file, docstring, context and subagent or
experiment tools locally) and `LeapAgenticLoop` under a dollar cap. The prompt comes from
`--prompt-file`, which defaults to the developer's `experimentation.md` under the ABC package's
`prompts/` directory (`prompt_file_for`). Artifacts land in the run directory: `transcript.jsonl`
and `images/`, `workspace/notes/`, `workspace/logs/docstrings/`, `phase_summary.json`, and
`video.mp4`.

`--resume RUN_DIR` continues a finished phase in a fresh context: the earlier run's workspace is
copied in, its final docstring snapshot is applied before the initial snapshot, the ledger starts
at what it spent, and the agent's first system message says so. The developer's plan is to launch at
$5, resume to $10, then to $50; each stop overshoots by about one turn.

Before the first model call, the tool set the agent will see is checked against the baseline's
declaration (`NaiveAgent` or `HarnessAgent` from the ABCs): names, descriptions and input schemas,
or the run refuses to start. Both baselines declare a subagent tool, so both need at least one
`agentic-robotics pool` simulator, pinned to the same variant slug, passed as `--pool-url`.

The boot is `cli.py`'s alone, so this phase gets every check an episode gets; a copy of the boot
without the block check let two pilots run on the wrong glyph library (2026-09-29).
-- prompt_file_for : The developer's experimentation prompt, one file for both baselines: what differs
between Naive and Harness is the tool set, and the Harness-specific sentence lives in
`run_experiment`'s docstring.
-- run_experimentation_phase : Connect an agent to the composed server and run the phase; writes `phase_summary.json`.
-- seed_example_states : Copy the example initial states into the workspace's read-only `logs/initial_states/`.

The hand-holding setting (`--example-tasks`) passes its own directory and `example_tasks`.

:param workspace: This run's workspace
:param source: Directory whose `*.json` files are copied
:param target_name: Subdirectory of `logs/` they are copied into
:return: The workspace-relative paths copied, in name order; empty when there are none
-- final_snapshot : The description set of the highest-numbered snapshot under `docstrings_dir`.

:raises FileNotFoundError: If there is no snapshot
-- resume_from : Carry a finished phase's workspace, final descriptions and spend into this run.

:param run_dir: The earlier run's directory (holding `phase_summary.json` and `workspace/`)
:param workspace: This run's workspace, which receives a copy of the earlier one
:param ledger: This run's ledger, charged with what the earlier run spent
:return: The earlier run's final description set and its cost
-- leap_agentic_thread : Run the phase on this thread, which is not the simulator's; release it when done.

---- DOCSTRINGS: leap_evaluate.py ----
The LEAP evaluation phase, run as `agentic-robotics episode --baseline <name>`:

    agentic-robotics episode --task <variant slug> --baseline control
    agentic-robotics episode --task <variant slug> --baseline naive \
        --docstrings <leap run>/workspace/logs/docstrings/0007.json

`agentic-robotics` owns the boot; this module supplies the agent thread. It is `toyblocks_runner`'s
episode (the repo's `AgenticLoop` against the task prompt and the task's tool-call cutoff) with a
`ComposedServer` between the agent and the skill server, which is what lets the served
descriptions be replaced and the served set be checked. With `--instance k` the scene is reset
to the package's reset state k on the simulator's thread before the first model call (and the
visibility preflight re-run on it), so every baseline and model sees the same task instances
(instances 0 and 1 of every variant). When the loop ends the final scene is
scored with the package's goal classifier, and `evaluation_summary.json` records success and
each conjunct, tool calls by category (motor, perception, other), model calls, dollars and
wall-clock seconds: the E2 metrics. Before the first model call the tools the
agent will see must be exactly `EvaluationAgent`'s (the motor skills and the perception tools),
carrying the baseline's description set: Control, the declared docstrings; Naive and Harness, the
final docstring snapshot of that run's experimentation phase; Oracle, the developer's
`ORACLE_DOCSTRINGS` for the motor skills with the declared perception docstrings. The initial
snapshot written under the run's `docstrings/` is the record of what passed.

The model host is the repo's loop over OpenRouter unless `--model-host claude-code` is passed, in
which case the composed server is served over HTTP and the episode runs inside the Claude Code CLI
through the Claude Agent SDK (`core.claude_code_loop`); `make_claude_code_evaluation_loop_class`
is that host's counterpart of `make_evaluation_loop_class`, with the same counters, cutoff rule,
per-call snapshot and batched-image rule, and the summary carries the same fields plus
`cost_source: "sdk_estimate"`, since the SDK's dollar figure is a client-side estimate.
-- oracle_description_set : The developer's handwritten docstrings for the motor skills of `backend`, plus the declared
perception docstrings: `oracle_agent.ORACLE_DOCSTRINGS` for the scripted skills,
`maniflow_skills.maniflow_oracle_agent.DOCSTRINGS` for the ManiFlow skills.

:raises SystemExit: If a motor skill is missing from the set or still reads "TODO"
-- load_description_set : The description set the baseline is evaluated with, or None for the declared docstrings.

:param backend: `config.skill_backend`, which picks the handwritten set for the oracle baseline

:raises SystemExit: If a learned baseline has no snapshot, or the Oracle set is asked for
-- on_simulator_thread : Run `work()` on the simulator's thread through the server's dispatcher and await it.
-- reset_to_instance : Reset env 0 to reset state `instance`, settle, and re-run the visibility preflight.
-- classify_scene : The package's goal classifier on the scene as it is: success and every conjunct.
-- open_gripper_for_scoring : Open the gripper the way the serving skill module does.

The ManiFlow server ramps the gripper command through `ToyBlocksEnv.step`; the scripted
server opens it through its motion layer, which settles and forgets the held
block. Calling only the
ManiFlow path would make a scripted-skills episode that ends with the gripper closed raise
during scoring and be recorded with no success value.
-- score_scene : Score the final scene the way the task means it: settled, with the robot letting go.

The autogen classifier gates success on every goal block being at rest and `finger_joint`
reading open (`scene_settled_and_gripper_open`), a guard against success firing mid-skill
during data generation. `stack` and `place_on_table` leave the gripper partly closed after
releasing (finger 0.49-0.64 on 2026-10-04's pick-start probe), so a scene whose every
conjunct holds would score as a failure (as in the Control suite,
`stack_feasible_isolated_flip_01` instance 0). Here the scene is synced to rest, the gripper
is opened if it reads closed (arm held still, the same command `open_gripper` sends), synced
again, and classified;
anything still held drops, which is the scene's honest end state. The raw classification is
kept beside it, and the final `SimState` is written to `final_state.json` for re-scoring.
`success` is the classifier corrected for letter case (`leap.spelling`: AI2, Ai2, aI2 or ai2
all count), or for a Search & Spell instance the specification's rule
(`leap.spelling.search_spell_report`, whose report is kept under `search_spell`; the
classifier's own reading, the designated blocks stacked in order, stays `success_strict`),
and for the velocity gate (`SETTLE_DISPLACEMENT_M`: a scene whose conjuncts all hold, gripper
open, and whose blocks do not move across the settle syncs is a success,
`settle_gate_overridden`); `success_strict` keeps the
uncorrected classifier's reading only so that suites scored before the corrections can be
compared.
-- motor_tool_names : The motor skill tool names, from the ABC.
-- budgeted_tool_names : The motor skill tool names that count toward the cutoff.
-- search_spell_episode_caps : (motor cutoff, ceiling on all calls, letter blocks) for a Search & Spell instance, from its
family and `config`'s per-letter-block rate and factor; None for any other task.
-- final_assistant_message : The text of the last assistant message in a transcript, or None.
-- make_evaluation_loop_class : `AgenticLoop` with a cutoff on motor skill calls (heavy imports deferred to call time).

:param total_ceiling: The ceiling on calls of any kind; the ABC package's
    `MAX_EPISODE_TOOL_CALLS` when None
:param after_motor_call: Awaited with (motor calls made, the call's tool name) after every
    motor skill call, for per-skill state recording
:param batch_images: Whether a motor skill's result keeps its image when the agent issued
    another motor skill right after it in the same turn (`BATCHED_IMAGE_NOTE` replaces it)

The evaluation cutoff is `LEAP_EVAL_BUDGET_FACTOR` calls per motor skill in the optimal plan,
counting only motor skill calls, so looking is free and the cutoff is not what ends an
episode that was going to finish. `MAX_EPISODE_TOOL_CALLS` from the ABC package bounds calls
of any kind, a safety ceiling against perception loops. The counting and the two messages go
through the base loop's hooks; see `EvaluationLoop`.
-- make_claude_code_evaluation_loop_class : `ClaudeCodeLoop` with the motor-call cutoff of `make_evaluation_loop_class`, enforced
through the SDK's hooks (heavy imports deferred to call time).

:param motor_cutoff: Motor skill calls after which the next model step is the final answer
:param total_ceiling: The ceiling on calls of any kind; the ABC package's
    `MAX_EPISODE_TOOL_CALLS` when None
:param after_motor_call: Awaited with (motor calls made, the call's tool name) after every
    motor skill call, for per-skill state recording
:param batch_images: Whether a motor skill's result keeps its image when the agent issued
    another motor skill right after it in the same step (`BATCHED_IMAGE_NOTE` replaces it)

The rule is the base loop's, at the same boundary: the budget is checked when a model step
starts, so a step that overruns it runs every call it issued, and the first call of a step
that starts over budget is denied with `evaluation_final_update`, the message the base loop
gives on its final turn. The model answers that denial with its final message, which ends
the run; any further call is denied the same way, and `max_turns` is the ceiling on that.
-- claude_code_model_id : The Messages-API model id behind an OpenRouter id (`anthropic/claude-opus-5.5` to
`claude-opus-5-5`), the only kind Claude Code can host.

OpenRouter writes the version with a dot and Anthropic with a dash; the CLI rejects the
dotted form as an unknown model.

:raises SystemExit: For a model OpenRouter routes to another vendor
-- claude_agent_sdk_version : The installed `claude-agent-sdk` version, which pins the bundled CLI.
-- claude_code_summary : The summary fields a Claude Code episode fills in place of the model client's usage.

`cost_usd` is the SDK's `total_cost_usd`, an estimate from its bundled price table rather
than a provider's bill, so `cost_source` says so; `model_seconds` is the SDK's API time.
-- tool_call_counts : Tool calls in the transcript, by category and by name.
-- run_evaluation_episode : One evaluation episode behind the composed server, checked against `EvaluationAgent`.

:param allow_declaration_mismatch: Log how the served tools differ from the declaration and
    run anyway, instead of refusing; for a skill surface the declarations do not yet cover
:param model_host: `openrouter` (the repo's loop) or `claude-code` (the Claude Agent SDK)
:param claude_code: For the `claude-code` host, `effort` and `max_turns` (both may be None)
-- evaluation_agentic_thread : Run the episode on this thread, which is not the simulator's; release it when done.
-- EvaluationLoop : The base loop with the motor-call cutoff, set through the base loop's hooks:
`max_tool_calls` is the motor cutoff (`tool_call_cost` charges only the budgeted motor
skills), the safety ceiling on calls of any kind is `should_continue`, and the two
messages are `status_text` and `get_final_update`. `motor_calls_made` counts the budgeted
skills; `skill_calls_made` every motor skill, `return_home` included, and indexes the
per-call state snapshots.
-- ClaudeCodeEvaluationLoop : The Claude Code loop with the motor-call cutoff: `deny_reason` is the cutoff and the
ceiling, `after_tool_call` the counting and the snapshot, `edit_tool_output` the
batched-image rule, `status_text` the status line. Counts as `EvaluationLoop`'s.

---- DOCSTRINGS: leap_harness.py ----
The Harness baseline's experiment tools: plan_experiment and run_experiment.

The tools are `ScientificAgent.plan_experiment` and `run_experiment` from the ABCs, which fix
their names, docstrings and the `ExperimentPlan` schema: a hypothesis, success criteria, and the
trials (each a subagent `Episode` with a label). The Harness agent keeps the file, docstring,
state and perception tools and context clearing; its motor skills are registered with their
docstrings but refuse every call (the composed server does that, with the refusal text from
`NoOpMotorSkillsAgent`), and it has no `spawn_subagents`. What replaces it is the same machinery,
the subagent spawner and the pool, behind a structure the agent has to fill in before anything
runs:

- **plan_experiment** validates the plan (every trial's tools from the permitted set, exactly one
  readable starting scene per trial, distinct labels) and writes it as
  `logs/experiments/<id>/plan.json`. It runs nothing.
- **run_experiment** runs a planned experiment's trials once, as the Naive agent's
  `spawn_subagents` would, with each trial's prompt wrapped in a preamble that names the
  hypothesis and the criteria and asks the trial to report against them. Results go to
  `logs/experiments/<id>/results.json` and each trial's rendered log beside it, all readable
  with `read_file`, which is why there is no separate log-review tool.

What this encodes is a research decision, not mechanism: the harness forces the
hypothesis-criteria-trials shape and records it, and a trial is still an agent. The paper's own
documents win where they specify the tools differently.
-- trial_episode : The episode a trial runs as: its prompt behind the experiment's preamble.
-- ExperimentHarness : Plans and runs experiments for one parent agent.
-- register_harness_tools : Register the two experiment tools on `server` as `ScientificAgent` declares them.

:return: The tools' names, for allowlists
-- __init__ : Initialize the harness.

:param spawner: The subagent spawner the experiments' trials run through
:param workspace: The parent's workspace; experiments live under its logs
-- plan : Validate and record a plan; nothing runs.

:raises ToolError: If a trial's tools or starting scene are invalid, or labels repeat
-- run : Run a planned experiment's trials once and record the results.

:return: One row per trial: its label and its `EpisodeResult` fields
:raises ToolError: If the experiment is unknown or has already run

---- DOCSTRINGS: leap_leap_agents.py ----
Define abstract base classes for all method and baseline agents used in the LEAP paper.
-- EvaluationAgent : An agent defining the toolset (but not docstrings) provided to all approaches during the
evaluation phase.

Note that each agent should use the appropriate docstrings for the motor skills:
    - Control: Original docstrings
    - Oracle: Human-designed 'ground-truth' docstrings
    - Naive: Docstrings (presumably) adapted during experimentation
    - Harness: Docstrings (presumably) adapted during experimentation
-- ControlAgent : A control agent, with original-docstring motor skills and perception tools.
-- NaiveAgent : A naive, experiment-capable agent able to update its docstrings, spawn subagents, etc.
-- NoOpMotorSkillsAgent : An agent with the standard motor skills interface, but whose motor skills cannot execute.
-- HarnessAgent : An experiment-capable agent with tools forcing it to follow the scientific method.
-- get_refusal_text : Construct the refusal message given to the agent when it tries to call a motor skill.

---- DOCSTRINGS: leap_subagents.py ----
Subagent episodes: one blocking batch tool that runs each episode on a pool simulator under
the parent's budget and returns what each one reported.

The tool is `RecursiveAgent.spawn_subagents` from the ABCs, which fixes its name, docstring and
the `Episode` schema: a prompt, a tool allowlist (the skills, the perception and state tools and
the file tools; never docstring updates, context clearing or spawning), a tool-call ceiling of at
most `MAX_EPISODE_TOOL_CALLS`, and a starting scene, either a `SimState` or a workspace path to a
file holding one as JSON. Every episode runs on the parent's model. An
episode ends when it stops calling tools, when it reaches its ceiling, or when the shared ledger
passes its cap, in which case it returns a budget-exceeded result with no final message.
Subagents inherit the parent's current tool descriptions and share its workspace; the parent gets
back an `EpisodeResult` per episode. The parent's prompt is the first user message; the system
instructions are the developer's preamble under the ABC package's `prompts/` directory.

Simulators come from `SimulatorPool`: pre-warmed `pool_server.py` processes serving one scene
each over streamable HTTP. An episode checks one out for its duration, so more episodes than
simulators queue. An episode's transcript lands under `workspace/logs/subagents/`, with `log.md`
rendered once from it by `render_log` and its images beside it, all readable by the parent with
`read_file`.

An unpriced model call inside an episode raises `UnpricedModelCallError` out of the episode and
out of the tool, which the MCP layer reports to the parent as a tool error rather than a crash.
The parent's own next model call goes through the same endpoint, so the ledger raises there and
ends the phase within one turn.
-- SimulatorPool : Pre-warmed simulators, each serving one scene's tools at a URL, checked out one at a time.
-- SubagentLoop : The base loop with a per-turn call count, the shared ledger, and a budget stop.

Hooks only: the loop itself, the turn and the tool-call recording are the base's. A
tool-less turn ends the episode, as the base does.
-- _text_of : The text in a message's content, which is a string or a list of blocks.
-- final_message_of : The text of the last assistant message, or empty when there is none.
-- render_log : Render an episode's `transcript.jsonl` as Markdown: prompts, agent text, calls and results.

Images are named by file under `image_dir`, which the spawner passes as the workspace-relative
path of the episode's `images/` directory so the parent can hand it straight to `read_file`.
Reasoning items are left out: the API returns them summarised at best, and the model's own
text carries the account.
-- SubagentSpawner : Runs batches of episodes on the pool; one instance per parent agent.
-- register_spawn_tool : Register spawn_subagents on `server` as `RecursiveAgent` declares it.

:return: The tool's name, for allowlists
-- check : Connect to every simulator and list its tools; all must serve the same set.

:return: The tool names every simulator serves
:raises RuntimeError: If a simulator is unreachable or serves a different set
-- acquire : Check a simulator out until the block ends; waits when all are in use.
-- _record_usage : Add any new usage snapshots to the ledger and this episode's own total.
-- status_text : The subagent's per-turn status line, from `messages.py`.
-- should_continue : Stop, and say so, once the shared ledger is over its cap.
-- take_turn : The base turn, then the call's cost goes to the ledger and this episode's total.
-- run_tool_calls : The base run, counted.
-- take_final_turn : No final answer once the ledger is over its cap; otherwise the base's.
-- get_final_update : The final-answer request, from `messages.py` rather than the core loop.
-- __init__ : Initialize the spawner.

:param pool: Simulators the episodes run on; `check` must have run
:param parent: The parent's composed server, whose current descriptions episodes inherit
:param workspace: The parent's workspace, shared with every episode
:param ledger: The dollar ledger every episode spends against
:param model_config: The parent's model, which every episode runs on
:param preamble: System instructions given to every episode
-- model_name : The model every episode runs on, as the results report it.
-- permitted_tools : What an episode may be given: everything the pool serves, plus the file tools.
-- validate : Refuse an episode naming a tool outside the permitted set or a missing state file.

:raises ToolError: Saying which episode and listing every permitted tool by name
-- _initial_state : The episode's starting scene, read from the workspace when given as a path.
-- run_batch : Run every episode, each on a pool simulator, and wait for all of them.

:param episodes: The episodes to run concurrently
:param batch_dir: Where their logs go; the next numbered batch directory when omitted
    (the harness passes its experiment's directory)

---- DOCSTRINGS: release_search_spell_families.py ----
The Search & Spell task families as data: the specification's constants, the block face maps,
and the per-task `families.json` that `drivers/search_spell_env.py` writes and that
`search_spell_scoring` and ``agentic-robotics-spell-build` (drivers/search_spell_build.py)` read.

The developer's task specification is the source of every number here. Units, in its words: a
**task family** fixes the target word, the
block inventory (which concrete blocks, how many of them letter blocks), which blocks begin
stacked, and every block's abstract orientation; a **task instance** is one continuous sampling
of a family (poses, block sizes, table height, friction) by Stage-1 codegen under the training
data's settings. Each instance is its own PDDL file and so its own autogen package
(`task_variants` maps one PDDL to one package), which is what lets every instance carry its own
scene profile in env slot 0, the only slot an episode runs in.

Layout, under `data/problems/<task key>/`:

    spell_<word>_<collection>/                     one task key per word and block collection
        spell_<word>_<collection>_<k>_<feasibility>_<j>.pddl
                                                   inventory k (6+k letter blocks), `feasible` or
                                                   `infeasible`, instance j
        families.json                              every family of the task, keyed by family slug

Every family hides its target letters at the start (the specification's visibility rule: a face
is visible on the front of a block, or on top of a block with nothing on it). An infeasible
family is its feasible counterpart with one target letter absent: the block or blocks carrying
that letter are replaced, in the same slots of the same stack layout, by blocks carrying no
letter of the word, so the word cannot be spelled and everything else matches. Within one word
and inventory, the patterned and unpatterned families share their letter-block count, their
color cubes and their stack layout over numbered block slots (targets fill the first slots).

Block names are PDDL object names: `block_<letter>` for the patterned collection
(`train_blocks_large`), `block_NNNNN` for the unpatterned one (`eval_blocks_36_0`), and the
training data's six color cubes. The face maps under `data/block_faces/` come from
`scripts/decode_block_faces.py`.
-- LetterFace : A letter on one body face of a block, and which body axis its top points along.
-- BlockFaces : Every glyph on a block, from `data/block_faces/<library>.json`.
-- load_block_faces : The face map of a glyph library, by block name.
-- Family : One task family, as `families.json` records it.
-- TaskFamilies : The `families.json` of one task key.
-- letter_blocks_for : Letter blocks in inventory k of a word: `LETTER_BLOCKS_RANGE[0] + k`, so 6, 7 and 8 for
k = 0, 1, 2 under the suite's range; `max_letter_blocks` raises the limit for task keys
outside the suite (the example families run to ten, a scene with no color cube).
-- parse_slug : The parts of a family or instance slug, or None for a slug of some other task.
-- family_of_instance : The family an instance slug belongs to, or None when the slug is not a Search & Spell
instance or its task has no `families.json`.
-- task_keys : Every Search & Spell task key the specification defines.
-- letters : The faces carrying a letter A-Z or a-z, in face order.
-- target_faces : The faces of block `name` carrying a letter of the word, in either case.

---- DOCSTRINGS: release_search_spell_scoring.py ----
Success for a Search & Spell task instance, read from the final scene's block poses.

The developer's specification: an episode succeeds if the final state holds a
stack of 3 blocks whose front faces spell the letters of the target word, uppercase or
lowercase, from top to bottom, with those faces oriented so the letters are upright from the
front camera; a block is accepted within 45 degrees of yaw of the nominal orientation. Read here
as:

- *stack*: a block is on another when it rests on it, whatever the offset: one block height
  above it (two cubes resting flat are separated by the mean of their edges, so the height step
  is the edge for the blocks in play) with overlapping footprints, which for cubes means a
  horizontal offset smaller than that height step. The simulator has settled every scored state,
  so a tower that stands is stable; no center tolerance is applied. A stack of 3 is a tower of
  exactly three blocks, its bottom on no other block and nothing on its top; the report also
  says whether three consecutive blocks of a taller tower would have spelled the word
  (`success_any_three`), should the developer read the rule that way instead.
- *front face spells the letter*: the block has a face carrying the letter in either case (its
  family's `letter_faces`, from the block face maps), and the block is within `TILT_TOL_DEG` of
  tilt and `YAW_TOL_DEG` of yaw of the nominal orientation that turns that face to the camera
  with the glyph's top up (`block_orientations.nominal_orientation`), the yaw measured from
  world x or from the line to the camera (`block_orientations.orientation_ok`). Nothing else is
  required: distractors, cubes and the gripper may be anywhere.

The report beside the verdict (`letters_in_place`, `letters_readable`, `tower_heights`, the
readable letters per block) is what lets a near miss be read from an episode summary without
the image. `feasible` and `absent_letter` carry the family's feasibility: on an infeasible
instance no stack can spell the word, so `success` is always False there and the outcome of
interest is the agent's own claim, which the runner records.
``agentic-robotics-spell-check` (drivers/spelling_check.py)` is the known-answer check.
-- _is_on : `top` rests on `bottom`: one block height above it with overlapping footprints. The
height step of two cubes resting flat is the mean of their edges, so the footprints overlap
exactly when each horizontal offset is smaller than the height step.
-- supports : The blocks `top` rests on: of the blocks it overlaps from above, the nearest beneath it,
and any other at the same height step, which it bridges. A block two levels down also
overlaps from above, which is why only the nearest level counts.
-- towers : Every maximal chain of blocks resting on one another among `names`, each listed top to
bottom. A block bridging two blocks rests on both, so it heads a chain through each; the
chains then share blocks, and there can be more chains than blocks on the table.
-- glyph_ups : Every body axis that may point upward for `glyph` to read as itself: its own up, plus the
opposite one for the half-turn-symmetric glyphs.
-- readable_letters : The letters on `name` that read from the front camera in `pose`: the face toward the
camera with the glyph's top up, or upside down for a half-turn-symmetric glyph.
-- search_spell_report : Score a final `SimState` dict against a Search & Spell family; see the module docstring.

:return: `success`, plus what the scene held: `towers` (top to bottom), `tower_heights`,
    `readable` (letters readable per block), and for the best tower `letters_in_place` and
    `letters_readable` by position (first letter first)
-- family_for_slug : The family of a task instance slug, read once per process; None for any other task.
-- search_spell_report_for : `search_spell_report` for a task slug, or None when it is not a Search & Spell instance.
-- nearest_orientation : The abstract orientation (one of the 24) closest to a block's quaternion, and the angle to it
in degrees.
-- exposed_target_letters : The target-letter faces visible in `state` under the specification's rule, as
`<glyph>@<block>`: a face is visible on the front of a block (its world axis `FRONT_AXIS` under
the block's nearest abstract orientation) or on top of a block with nothing on it. The rule
is the one the generator hides the letters under, applied to a continuous state through the
nearest of the 24 orientations; it says nothing about whether the camera could read the
glyph.
-- declared_outcome : What the agent's final message declares: the value of the one substring of `declarations`
it contains, "both" if it contains more than one, None if none.

---- DOCSTRINGS: oracle_mcp_server.py ----
Define an abstract interface for an MCP server providing oracle skills as MCP tools.
-- OracleMCPServer : The interface for an MCP server providing MCP tools to call TAMP and RL oracle skills.
-- _register_skills : Register oracle-specific skills as MCP tools provided by the server.
-- get_zoomed_image : Retrieve a magnified view of a cropped area of the current image observation.

A zoom factor of 4 produces a zoomed image covering a quarter of the original
image's height and width, magnified to be four times its original size. Thus,
the zoomed image has the same resolution as the original image observation.

:param pixel: Raw pixel coordinate defining the center of the cropped region
:param zoom: Zoom factor for the magnified view (must be between 1.0 and 20.0)
:return: Zoomed crop of the current image observation
-- pick : Pick up the block at the given pixel in the current image.

:param pixel: Raw pixel coordinate in the current image observation
:return: Updated image observation after the skill has finished
-- stack : Stack the held block onto the block at the given pixel in the current image.

Precondition: The robot's gripper must be holding a block.

:param pixel: Raw pixel coordinate in the current image observation
:return: Updated image observation after the skill has finished
-- place_on_table : Place the held block on the table, at the given pixel in the current image.

Precondition: The robot's gripper must be holding a block.

:param pixel: Raw pixel coordinate in the current image observation
:return: Updated image observation after the skill has finished
-- rotate : Rotate the block at the given pixel in the current image.

Preconditions:
    - The robot's gripper must be empty.
    - The block to be rotated must be laying directly on the table's surface.

:param pixel: Raw pixel coordinate in the current image observation
:param direction: Direction to rotate the block, as viewed from above ("cw" or "ccw")
:return: Updated image observation after the skill has finished
-- flip : Flip the block at the given pixel in the current image.

Preconditions:
    - The robot's gripper must be empty.
    - The block to be flipped must be laying directly on the table's surface.

:param pixel: Raw pixel coordinate in the current image observation
:param direction: Specifies where the top face of the block ends up after the flip
:return: Updated image observation after the skill has finished
-- return_home : Open the gripper, then move the arm back to a neutral resting configuration.

Use this when another skill reports that the arm cannot plan from its current
configuration. All motion-planning-based skills will continue to fail until
the arm is moved. To get the arm unstuck, this skill drives the joints directly.

:return: Updated image observation after the skill has finished
-- open_gripper : Open the robot gripper, releasing anything it holds.

:return: Updated image observation after the skill has finished
-- close_gripper : Close the robot gripper, grasping anything between its fingers.

:return: Updated image observation after the skill has finished
