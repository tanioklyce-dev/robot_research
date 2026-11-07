# XPolicyLab/XPolicyLab — capture bundle (2026-11-07)

Captured from https://github.com/XPolicyLab/XPolicyLab at main head 6baccd5 (2026-11-03). Files verbatim below, each under a heading with its repo path.

## GitHub API metadata
```
{"created_at":"2026-02-08T05:59:41Z","description":"[IROS 26 ScaleInfra Workshop Best Tool Paper] Involving over 50 Advanced Manipulation Policies","forks_count":200,"homepage":"https://xpolicylab.github.io","license":"Apache-2.0","open_issues_count":46,"pushed_at":"2026-11-03T17:47:36Z","stargazers_count":541}
commits on main: ~376 (pagination count)
top contributors:
TianxingChen 164
yuechen0614 33
FlowsMple 18
Haodong-Yan 14
zhanghaoyu913-cmyk 12
zhangxiwen1810 10
WenweiLin2004 8
Wanghao00pro 7
JinhuiYE 7
anesthesia3690 6
recent commits:
6baccd5 2026-11-03T17:47:13Z Merge branch 'main' of github.com:XPolicyLab/XPolicyLab
7f0c904 2026-11-03T17:46:05Z Rename physicalRSI to PhysicalRSI and list the 77 integrated policies.
c7479d6 2026-11-03T15:14:24Z Merge pull request #227 from Timsty1/codex/delete-useless-sha256-information
1dc073f 2026-11-03T15:01:10Z Delete Useless SHA256 Information
196ddec 2026-11-03T13:08:42Z Merge branch 'main' of github.com:XPolicyLab/XPolicyLab
utils/process_data.py RGB history:
2026-08-04 Unify image handling on RGB from data conversion through evaluation
2026-08-07 State decoded images are RGB as a conclusion, not something to re-derive
2026-09-09 Mark standard RGB JPEGs so decode_image_bit handles both byte formats
policy/ directories:
A1 ACT AHA_WAM Abot_M0 Awomo05 Being_H05 CloudRobo_WM DP Dexbotic_DM0 Dexora_1B Discrete_Forcing DreamZero EWAM EgoVLA EventVLA Evo_1 FastWAM G05 GO1 GO_3_Nano_preview GPT_6_Astra_Direct_EEF GR00T_N17 GalaxeaVLA GigaWorldPolicy HWM_CogWAM H_RDT Hy_Embodied_05_VLA InternVLA_A1 InternVLA_A1_5 InternW0_delta KinRT LDA_1B Liber_0_lite Liber_0_preview LingBot_VA LingBot_VLA ME_Brain_1 ME_Dex_1_0 MM_ABC MWA_Phoenix MachEmbodied-U0 Meituan_Robotics_0 Mem_0 MoPA MolmoAct2 OpenDM OpenVLA_OFT OpenWAM PICA_WAM PatchWAM PhysicalRSI Pi_0 Pi_05 Pi_0_Fast PrismWAM Q0_Preview RDT_1B RISE Rex_M1_preview Simate_beta SimpleMemVLA SmolVLA Spark_0 Spatial_Forcing Spirit_v15 StarVLA TinyVLA UniWAM VPP2 ViGAR WallX WorldLA WorldScape_Policy_2 X_VLA X_WAM Xiaomi_Robotics_0 Xiaomi_Robotics_1 demo_policy 
```

## AGENTS.md
````
# XPolicyLab Agent Guide

XPolicyLab wraps each robot policy as a self-contained adapter under `policy/<POLICY>/`. The policy
server imports it as `XPolicyLab.policy.<POLICY>.model`, so this checkout is always used as a
package inside a parent workspace — never as the top-level project.

- Submission standard: [CONTRIBUTING.md](CONTRIBUTING.md). Reference adapter: `policy/demo_policy/`.
  Data formats: [README](README.md#-standard-data-formats).
- Two skills carry the end-to-end workflows — `xpolicylab-model-integration` (build an adapter) and
  `xpolicylab-adapter-check` (audit one before a PR). They live in `.agents/skills/`, which
  `.cursor/skills` and `.claude/skills` symlink to, so Cursor, Claude Code and Codex all load them.
- Root docs stay bilingual: when you edit `README.md`, update `README_zh.md` in the same change (and
  the reverse). Keep structure, anchors, code blocks, and tables aligned; translate prose only.
  English remains the source of truth on conflict.

The rules below apply to every change in this repo. Their rationale is in CONTRIBUTING.md.

## Images are RGB from end to end

`decode_image_bit` and `decode_obs_images` return RGB, and the policy server hands `update_obs` /
`update_obs_batch` RGB. Treat this as settled, and note that it holds for a reason no caller can
reproduce: stored image bits come in **two byte formats**, and `decode_image_bit` reads a marker
inside each buffer to tell them apart and swap only where a swap is owed.

- **legacy** — a JPEG written by handing an RGB array straight to `cv2.imencode`, which reads it as
  BGR. The bytes are channel-reversed against the JPEG standard, and `cv2.imdecode` reverses them
  back. Everything collected before the marker existed is this.
- **standard** — a conforming RGB JPEG written by `encode_image_bit`, stamped with a JPEG `COM`
  segment holding `XPL-RGB1`. `cv2.imdecode` returns BGR for it, so it needs exactly one swap.

A `COLOR_BGR2RGB` added to "fix" a decode is therefore still always a bug, and now for a sharper
reason than before: the decoded pixels are indistinguishable to the eye — only the marker in the
encoded buffer tells the formats apart — so a caller-side swap is right on at most one of them and
silently wrong on the other. Channel
conversion is allowed **only inside `utils/process_data.py`**, which owns the distinction.

No channel conversion belongs in conversion, training, or eval code. Two exceptions only:

- Medium adapters: `COLOR_RGB2BGR` immediately before `cv2.VideoWriter.write(...)`, and
  `COLOR_BGR2RGB` immediately after `cv2.VideoCapture.read()`.
- A deliberate RGB→BGR conversion for a checkpoint trained on BGR data, opt-in through a documented
  `deploy.yml` key that defaults to RGB (see `input_color_order` in `policy/Dexora_1B`).

## Decoding goes through the shared helpers

`model.py` never decodes. The server decodes every observation it forwards, including for custom
RPCs, so `obs["vision"][<camera>]["color"]` is already an array; adapters only reshape, cast, resize.

Offline code — conversion scripts and training dataloaders — decodes **only** with
`decode_image_bit` from `XPolicyLab.utils.process_data`, and encodes **only** with its inverse
`encode_image_bit`. That is the single supported pair: image bits come in the two byte formats above
and carry further inconsistency in their container layouts from earlier data versions, and only
these functions handle every case. Never hand-roll `cv2.imdecode` / `np.frombuffer` / PIL decoding —
a hand-rolled decoder is right on one byte format and reverses the channels on the other, whichever
way it is written, and the rest trip over the older layouts.

Mechanically, `cv2.imdecode` must not appear outside `utils/process_data.py`, and image bits that
get **stored or published** — trajectory files, converted datasets — must come from
`encode_image_bit`, never from a bare `cv2.imencode`, which omits the marker and so writes a buffer
that can only be read as legacy — channel-reversed on decode if the frame was converted to BGR
before encoding, and even when fed RGB it mints more legacy data that every conforming viewer shows
reversed. The why is in README,
[Standard Data Formats](README.md#decode-only-through-decode_image_bit).

## Paths and dimensions come from the shared helpers

`env_cfg/` lives in the **parent workspace, outside this repo** — `XPolicyLab/env_cfg` does not
exist, so an adapter must never build that path itself.

- **Importable root** in `policy/<POLICY>/model.py` is the parent of the checkout:
  `Path(__file__).resolve().parent.parents[2]`, which is the same directory as
  `Path(__file__).resolve().parents[3]`. Counted from the policy directory, `parents[1]` is the
  checkout itself and `parents[3]` is unrelated; both are bugs.
- **Checkpoints** resolve through `XPolicyLab.utils.checkpoint_resolver` — `resolve_checkpoint_root`,
  or `build_run_dir_name` / `candidate_checkpoint_roots` when an adapter adds its own naming layer —
  never by re-deriving `checkpoints/<bench_name>-<ckpt_name>-<env_cfg_type>-<action_type>-<seed>/`.
- **Action dimensions** come from `get_robot_action_dim_info(env_cfg_type)` in
  `XPolicyLab.utils.process_data`, never hard-coded and never through a private re-implementation.

A new robot must be registered in **both** robot-info files, or training and evaluation disagree
about action dimensions:

| File | Read by | Keyed by |
| --- | --- | --- |
| `<parent>/env_cfg/robot/_robot_info.json` | `get_robot_action_dim_info()` and `get_action_dim()` in `XPolicyLab.utils.process_data` — runtime and offline conversion | robot name, from `config.robot` in `<parent>/env_cfg/<env_cfg_type>.yml` |
| `utils/robot/_robot_info.json` | `utils/get_action_dim.sh`, called by `train.sh` | `env_cfg_type` |

The two entry points named `get_action_dim` do **not** read the same file. Runtime and conversion
code imports the Python one; the training path — `train.sh`, or a Python training entry it invokes —
uses `utils/get_action_dim.sh`, which delivers the value as a shell variable, runs on stdlib `json`
alone, and works in a standalone checkout that has no outer `env_cfg/` tree.

## deploy.yml

`policy_name` must equal the directory name. Keep the full key set from
`policy/demo_policy/deploy.yml` — including `protocol: ws`, `host` and `port` — even where the
scripts have a default; per-run fields are overridden at launch.

````

## CLAUDE.md
````
@AGENTS.md

````

## CONTRIBUTING.md
````
# Contributing a Policy to XPolicyLab

This page is the submission standard for `policy/<POLICY>/` adapters: what a complete adapter contains, how to test it, and what a PR must include. For repo-wide concepts and workflows, see the [README](README.md) ([中文](README_zh.md)). Root `README.md` and `README_zh.md` must stay in sync — update both in the same change.

Two bundled Agent Skills automate most of this: `xpolicylab-model-integration` builds an adapter, `xpolicylab-adapter-check` audits one before a PR. They live in `.agents/skills/`, which `.cursor/skills` and `.claude/skills` symlink to, so Cursor, Claude Code and Codex all pick them up. [AGENTS.md](AGENTS.md) distills this page into the always-on rules every agent must follow; `CLAUDE.md` just imports it. See [Using a coding agent](#using-a-coding-agent).

## Getting started

The fastest route is to copy the reference adapter, keep the XPolicyLab boundary small, and debug before touching a simulator:

1. **Read [policy/demo_policy](policy/demo_policy/README.md)** — `model.py`, `deploy.py`, `deploy.yml`, and the `eval.sh` / `setup_eval_policy_server.sh` / `setup_eval_env_client.sh` trio.
2. **Scaffold** with `bash scripts/create_policy.sh <POLICY_NAME>`, then fill in its README.
3. **Implement `model.py` first**, keeping `bench_name`, `task_name`, `ckpt_name`, `env_cfg_type`, `action_type`, and `seed` consistent across data, training, and eval (README, [Common Workflow](README.md#-common-workflow)).
4. **Put deployment defaults in `deploy.yml`** and keep `deploy.py` aligned with `demo_policy/deploy.py` unless the environment loop truly differs.
5. **Run [Testing](#testing)**, then move to `EVAL_ENV_TYPE=sim` or a split-machine deployment (README, [Deployment Flow](README.md#-deployment-flow)).

Eval-only submissions are accepted when training code cannot be open-sourced yet: say so in the PR, notify the maintainers ([Contact](README.md#-contact)), and share a timeline. For leaderboard evaluation, attach a checkpoint download script (Hugging Face or ModelScope preferred).

## Adapter Standard

### Files

Scaffold with `bash scripts/create_policy.sh <POLICY>` (copies `policy/demo_policy/`), then keep:

```text
policy/<POLICY>/
├── README.md                    # required: install / data / train / eval guide
├── __init__.py                  # required: keeps XPolicyLab.policy.<POLICY> importable
├── install.sh                   # policy environment setup (see exceptions below)
├── eval.sh                      # required: same-machine evaluation
├── setup_eval_policy_server.sh  # required: policy-side server
├── setup_eval_env_client.sh     # required: environment-side client
├── deploy.yml                   # required: deployment config, protocol: ws
├── deploy.py                    # required: deployment loop
├── model.py                     # required: Model adapter class
├── process_data.sh              # data conversion (see exceptions below)
├── train.sh                     # training entry (see exceptions below)
└── INSTALLATION.md              # optional: extra setup notes
```

Three scripts have a narrow exception, and each one has to be **declared**; everything else in the tree is unconditional.

- `process_data.sh` / `train.sh` may be omitted only for an agreed **eval-only** submission: state it in the PR, notify the maintainers ([Contact](README.md#-contact)), and give a timeline for open-sourcing training.
- `install.sh` may be omitted only when the environment comes entirely from an upstream project's own recipe. Say so under `Installation` in the policy README and give the full manual steps there or in `INSTALLATION.md`, as `policy/Dexora_1B` and `policy/X_WAM` do.

### `model.py`

Define `class Model(ModelTemplate)` (`from XPolicyLab.model_template import ModelTemplate`):

| Method | Contract |
| --- | --- |
| `__init__(model_cfg)` | `model_cfg` is `deploy.yml` merged with per-run overrides (`ckpt_name`, `action_type`, `env_cfg_type`, `seed`, ...). Load checkpoints and processors here. |
| `update_obs(obs)` / `update_obs_batch(obs_list)` | Store observation dict(s) for the next action call. |
| `get_action()` | Return one action chunk: `list[dict]` of numpy arrays. |
| `get_action_batch(env_idx_list=None)` | Batched chunks aligned with active env indices. |
| `reset()` | Clear model state between episodes. |

Action dictionaries use the standard keys (`left_arm_joint_state`, `right_ee_joint_state`, `ee_pose`, ...) with dimensions taken from `get_robot_action_dim_info(env_cfg_type)` in `XPolicyLab.utils.process_data` — never hard-coded, and never through a private re-implementation of the lookup. `env_cfg/` lives in the parent workspace, outside this checkout, so an adapter that assembles that path itself gets it wrong. Observation and trajectory formats: README, [Standard Data Formats](README.md#-standard-data-formats).

A new robot must be registered in **both** robot-info files, or training and evaluation will disagree about action dimensions:

| File | Read by | Keyed by |
| --- | --- | --- |
| `<parent>/env_cfg/robot/_robot_info.json` | `get_robot_action_dim_info()` and `get_action_dim()` in `XPolicyLab.utils.process_data` — runtime and offline conversion | robot name, from `config.robot` in `<parent>/env_cfg/<env_cfg_type>.yml` |
| `utils/robot/_robot_info.json` | `utils/get_action_dim.sh`, called by `train.sh` | `env_cfg_type` |

Two entry points share the name `get_action_dim`, and they do **not** read the same file. Runtime and conversion code imports `get_action_dim` (or `get_robot_action_dim_info`) from `XPolicyLab.utils.process_data`. The training path — `train.sh`, or a Python training entry it invokes — uses `utils/get_action_dim.sh` instead: it delivers the value as a shell variable, runs on stdlib `json` alone (importing the Python module pulls in numpy, cv2, h5py and yaml), and works in a standalone checkout that has no outer `env_cfg/` tree.

Two more shared entry points, so adapters do not re-derive them: the importable root in `policy/<POLICY>/model.py` is the parent of this checkout, `Path(__file__).resolve().parent.parents[2]` (equivalently `Path(__file__).resolve().parents[3]`; counted from the policy directory, `parents[1]` or `parents[3]` is a bug), and checkpoint directories resolve through `XPolicyLab.utils.checkpoint_resolver` (`resolve_checkpoint_root`, or `build_run_dir_name` / `candidate_checkpoint_roots` when the adapter adds its own naming layer).

`model.py` never decodes images. The policy server decodes every observation it forwards, so `obs["vision"][<camera>]["color"]` is always a plain image array. This holds for `update_obs` / `update_obs_batch` and for any custom RPC a policy exposes that carries an observation, so an adapter with its own deploy loop still must not decode.

In offline code — conversion scripts and training dataloaders that read trajectory files — **only `decode_image_bit` from `XPolicyLab.utils.process_data` is supported**, and image bits that get written back out must come from its inverse, `encode_image_bit`. Never hand-roll `cv2.imdecode` / `np.frombuffer` / PIL decoding, and never write stored buffers with a bare `cv2.imencode`. The README states the rule in [Standard Data Formats](README.md#decode-only-through-decode_image_bit).

The reason is that stored image bits come in **two byte formats**, and only these two functions know the difference:

- **legacy** — a JPEG written by handing an RGB array straight to `cv2.imencode`, which reads its input as BGR. The stored bytes are channel-reversed with respect to the JPEG standard, so `cv2.imdecode` reverses them a second time and returns the original RGB, while PIL, ffmpeg or a browser show red and blue swapped. Everything collected before the marker existed is this format, and it is never migrated: JPEG cannot swap channels losslessly.
- **standard** — a conforming RGB JPEG written by `encode_image_bit`, carrying a JPEG `COM` segment with the payload `XPL-RGB1`. Every decoder skips an unknown `COM`, so the marker is free; PIL even surfaces it as `Image.open(...).info["comment"]`. `cv2.imdecode` returns BGR for these bytes, so decoding them owes exactly one swap.

`decode_image_bit` reads the marker and returns RGB for both, which is why callers never swap. Images are RGB end to end, and a `cv2.cvtColor(decode_image_bit(...), COLOR_BGR2RGB)` is always a bug: the decoded pixels are indistinguishable to the eye — only the marker in the encoded buffer tells the formats apart — so a caller-side swap is right on at most one of them and silently wrong on the other. That trap is easy to fall into — a PIL-based loader tested against fresh data looks perfect and then quietly corrupts older episodes.

No channel conversion belongs in conversion, training, or eval code; only `utils/process_data.py`, which owns the format distinction, may convert. Two exceptions: medium adapters — `COLOR_RGB2BGR` immediately before `cv2.VideoWriter.write(...)` and `COLOR_BGR2RGB` immediately after `cv2.VideoCapture.read()` — and a deliberate RGB→BGR conversion for a checkpoint trained on BGR data, which must be opt-in through a documented `deploy.yml` key that defaults to RGB (see `policy/Dexora_1B`'s `input_color_order`).

### `deploy.yml`

`policy_name` must equal the directory name — the server imports `XPolicyLab.policy.<policy_name>.model`, and the setup scripts derive the name from the directory. Keep `protocol: ws` (`legacy_tcp` is for unmigrated legacy adapters only). Per-run fields are overridden by the setup scripts; put stable defaults here. Reference (`policy/demo_policy/deploy.yml`):

```yaml
policy_name: demo_policy
protocol: ws
host: localhost
port: null
bench_name: null
task_name: null
ckpt_name: null
env_cfg_type: null
seed: null
action_type: null
gpu_id: null
eval_batch: false
```

All of these are required except `ckpt_name` and `gpu_id`, which the setup scripts supply per run. Keep a key even when a script already defaults it, and document model-specific extra keys in the policy README.

### Scripts

All adapters share the same entry-point conventions (argument meanings: README, [Common Workflow](README.md#-common-workflow)):

```bash
bash eval.sh <bench_name> <task_name> <ckpt_name> <env_cfg_type> <action_type> <seed> \
  <policy_gpu_id> <env_gpu_id> <policy_env_or_uv_path> <eval_env_conda_env>
```

`eval.sh` starts the policy server, waits for it, runs the environment client, and cleans up — keep it aligned with `policy/demo_policy/eval.sh`; document any extra arguments in the policy README. Checkpoints resolve to `checkpoints/<bench_name>-<ckpt_name>-<env_cfg_type>-<action_type>-<seed>/` unless the policy README documents another layout.

### Policy README

All policy READMEs share one template — [policy/demo_policy/README.md](policy/demo_policy/README.md) is the minimal reference, [policy/AHA_WAM/README.md](policy/AHA_WAM/README.md) shows a complex adapter (model assets, custom environment variables):

1. **Header**: `**Contributor:** ... | **Paper:** ... | **arXiv:** ... | **Original code:** ...`, then 1–3 sentences on the model and what the adapter supports; mention vendored upstream directories here.
2. **Pointer paragraph** (verbatim): shared conventions link to the root README, official results link to the [RoboDojo LeaderBoard](https://robodojo-benchmark.com/LeaderBoard).
3. **Sections in order**: `Installation`, `Data Processing`, `Training`, `Evaluation`, plus `Model Assets` / `Configuration` / `Notes` only when the adapter needs them. State explicitly when a stage is unsupported (eval-only, upstream-native data, ...).
4. **Policy-specific content only**: one command template plus one runnable example per stage, extra arguments, required environment variables, `deploy.yml` keys, checkpoint-layout deviations. Do not restate shared argument tables or the split-machine flow — link to the root README instead.
5. **Declare LeRobot data** when the policy trains on it. Under `Data Processing`, give the dataset version and say whether the keys match the official converters (README, [Official LeRobot conversion](README.md#official-lerobot-conversion)). If they do, name the converter or the prepared export you consume, and say whether `process_data.sh` is absent or only links and normalizes the dataset. If they do not, state the deviation and how to produce that layout — otherwise the next user feeds official output to a trainer that cannot read it.

## Testing

Run these in order before opening a PR.

**1. Static checks** (repo root):

```bash
git diff --check
bash -n policy/<POLICY>/*.sh
python -m py_compile policy/<POLICY>/model.py policy/<POLICY>/deploy.py
```

XPolicyLab data supports only `decode_image_bit` / `encode_image_bit` (README, [Standard Data Formats](README.md#decode-only-through-decode_image_bit)). The first grep must return nothing on adapter-owned conversion and training code; vendor files that never see XPolicyLab trajectories can be skipped, but a `cv2.imdecode` on those trajectories is a fail. The second grep catches image bits written without the format marker — a `cv2.imencode` whose output is stored or published is a fail, one whose output is decoded again in the same process is not. The third surfaces channel swaps that need judging (medium adapters and a documented `input_color_order` are the only allowed hits):

```bash
# only decode_image_bit is supported
grep -rnE 'cv2\.imdecode|np\.frombuffer|Image\.open' policy/<POLICY>/
# stored buffers must come from encode_image_bit — judge each hit
grep -rn 'cv2\.imencode' policy/<POLICY>/
# channel swaps — judge each hit
grep -rnE 'COLOR_BGR2RGB|COLOR_RGB2BGR|\.\.\., ::-1' policy/<POLICY>/
```

**2. Debug closed loop** — no simulator needed; verifies imports, server startup, observation serialization, action keys and dimensions, and batch logic:

```bash
cd policy/<POLICY>
export EVAL_ENV_TYPE=debug
bash eval.sh RoboDojo stack_bowls <ckpt_name> arx_x5 joint 0 0 0 <policy_env> base
```

The run must reach `[MAIN] eval finished` with no tracebacks. The debug client sends plain image arrays by default; re-run with `DEBUG_OBS_ENCODED=1` to make it send encoded camera colors instead — a JPEG buffer, raw bytes, and a plain array across the three cameras — which exercises the server-side decode path that real environment clients rely on. For a quick smoke test, `policy/demo_policy` accepts placeholder env names such as `base`.

**3. Simulator evaluation** — recommended for every PR and required before a leaderboard entry is published: run the same `eval.sh` with `EVAL_ENV_TYPE=sim` (or unset) inside a RoboDojo / RoboTwin workspace and record task success rates.

## Using a coding agent

`xpolicylab-model-integration` builds an adapter (a prompt like `Integrate <POLICY_NAME> into XPolicyLab` is enough). `xpolicylab-adapter-check` audits one against this page before a PR (`Check policy/<POLICY_NAME>`). For an agent that supports none of these, paste this checklist:

```text
Integrate <POLICY_NAME> into XPolicyLab.

Use policy/demo_policy as the reference.
1. Inspect the upstream model's inference API and dependencies.
2. Create or update policy/<POLICY_NAME>/README.md with install, checkpoint, train, and eval commands.
3. Implement install.sh and, if needed, process_data.sh and train.sh. Omitting any of the three requires a declared exception in the README.
4. Implement model.py with Model.__init__, update_obs, get_action, reset, and batch methods. model.py never decodes.
5. Offline conversion/training decodes XPolicyLab images only via decode_image_bit and writes them only via encode_image_bit. Stored bits come in two byte formats; only these functions tell them apart, and both give you RGB. Never swap channels yourself.
6. Keep deploy.py aligned with policy/demo_policy/deploy.py.
7. Put deployment defaults in deploy.yml, keeping the standard key set (protocol: ws, host, port, ...).
8. Run EVAL_ENV_TYPE=debug eval.sh and fix shape/action-key/server errors.
9. Summarize supported action_type, env_cfg_type, checkpoint layout, and remaining limitations.
```

## PR Standard

Title: `[policy] <POLICY>: <short summary>`, e.g. `[policy] FastWAM: add RoboDojo adapter`.

Every submission PR must include the adapter following the standard above, a working policy README, and test evidence. For **official leaderboard evaluation** ([RoboDojo](https://robodojo-benchmark.com/LeaderBoard), [RoboTwin](https://robotwin-platform.github.io/leaderboard)), the PR description must also carry a checkpoint download script — Hugging Face or ModelScope preferred — so we can reproduce your results; we evaluate and publish entries as soon as possible.

### PR description template

GitHub pre-fills this from [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md):

```markdown
## Policy
- Name / paper / upstream repo:
- Supported: bench_name=..., env_cfg_type=..., action_type=...
- Training support: full | eval-only (training release ETA: ...)

## Components
- [ ] install.sh (or upstream-native install, documented in the policy README)
- [ ] model.py (+ __init__.py)
- [ ] images: only decode_image_bit / encode_image_bit are supported (two byte formats → RGB), no channel swaps (see README)
- [ ] deploy.yml (standard key set incl. protocol: ws / host / port, policy_name matches the directory)
- [ ] deploy.py aligned with demo_policy (or divergence explained)
- [ ] eval.sh + setup_eval_policy_server.sh + setup_eval_env_client.sh
- [ ] process_data.sh / train.sh (or eval-only, declared above)
- [ ] policy README with install / data / train / eval commands

## Testing
- [ ] bash -n + py_compile pass
- [ ] decode/encode grep: only decode_image_bit and encode_image_bit on XPolicyLab data
- [ ] EVAL_ENV_TYPE=debug closed loop passes (paste the log tail)
- [ ] Simulator eval: task=..., success=... (if available)

## Checkpoint (required for leaderboard evaluation)
<download script, Hugging Face or ModelScope preferred>

## Limitations / notes
...
```

````

## .agents/skills/xpolicylab-model-integration/SKILL.md
````
---
name: xpolicylab-model-integration
description: Integrate a robot policy into XPolicyLab as a policy/<POLICY>/ adapter. Use when adding or updating a policy adapter, implementing model.py or deploy.yml, wiring install/process_data/train/eval scripts, or debugging debug-mode evaluation in the XPolicyLab repo.
---

# XPolicyLab Model Integration

Add each policy as a self-contained `policy/<POLICY>/` adapter; keep upstream model code unchanged where possible. `policy/demo_policy/` is the minimal reference — mirror it unless the model truly needs more.

## Before starting

Confirm with the user, or state the assumption explicitly in your first reply:

- Where the upstream model code and checkpoints live (repo URL, local path, or "not available yet").
- Which `env_cfg_type` (robot) and `action_type` (`joint` / `ee`) the model supports.
- Whether this is a full integration or eval-only (no `process_data.sh` / `train.sh`).
- Which conda/uv environment to use for the policy side.

## Workflow

1. Read `policy/demo_policy/` (`model.py`, `deploy.py`, `deploy.yml`, `eval.sh`, `README.md`), then the upstream model's inference API, dependencies, and checkpoint layout.
2. Scaffold: `bash scripts/create_policy.sh <POLICY>` (copies `demo_policy`).
3. Implement `model.py` first (contract below). The policy server imports `XPolicyLab.policy.<POLICY>.model`, so keep the directory importable (`__init__.py`). Put environment setup in `install.sh`; add `process_data.sh` / `train.sh` only if the model supports them. If the policy trains on LeRobot data, default to the official converters — `scripts/transform_lerobot_v21_format.py` / `scripts/transform_lerobot_v30_format.py`, or a prepared export produced by them — and let `process_data.sh` only link and normalize the dataset; write a custom converter only when the model needs a layout the official keys cannot express, and document that deviation.
4. Keep `deploy.py` aligned with `policy/demo_policy/deploy.py` unless the environment loop truly differs. Put runtime defaults in `deploy.yml`, keeping the whole key set from `policy/demo_policy/deploy.yml` — `policy_name` (equal to the directory name), `protocol: ws`, `host`, `port`, plus the per-run fields the setup scripts override. Keep a key even where the scripts already default it.
5. Debug without a simulator, from `policy/<POLICY>/`:

   ```bash
   export EVAL_ENV_TYPE=debug
   bash eval.sh RoboDojo stack_bowls <ckpt_name> arx_x5 joint 0 0 0 <policy_env> base
   ```

   `<policy_env>` (arg 9) follows the adapter's own convention — a conda env name, `uv`, or an environment path; `policy/Pi_05`, for example, requires `uv` (see its README). The trailing `base` is the eval-env conda env (arg 10).

   Fix import, server-startup, action-key, and shape errors until the loop completes. Run once more with `DEBUG_OBS_ENCODED=1` so the debug client sends encoded camera colors and the server-side decode path is exercised.
6. Static checks from the repo root: `bash -n policy/<POLICY>/*.sh` and `python -m py_compile policy/<POLICY>/model.py policy/<POLICY>/deploy.py`.
7. Write `policy/<POLICY>/README.md`: install, data, train, and eval commands, supported `action_type` / `env_cfg_type`, checkpoint layout, known limitations. An adapter that trains on LeRobot data must also declare, under `Data Processing`, the dataset version and whether its keys match the official converters (README, [Official LeRobot conversion](../../../README.md#official-lerobot-conversion)) — naming the converter or prepared export when they do, and the deviation when they do not.

## Model contract (`model.py`)

Define `class Model(ModelTemplate)`, importing `ModelTemplate` from `XPolicyLab.model_template`:

| Method | Contract |
| --- | --- |
| `__init__(model_cfg)` | `model_cfg` is `deploy.yml` merged with CLI overrides (`ckpt_name`, `action_type`, `env_cfg_type`, `seed`, `gpu_id`, ...). Load checkpoints and processors here. |
| `update_obs(obs)` / `update_obs_batch(obs_list)` | Store observation dict(s) for the next action call. |
| `get_action()` | Return one action chunk: `list[dict]` of numpy arrays. |
| `get_action_batch(env_idx_list=None)` | Batched chunks aligned with active env indices; fall back to the config batch size when `None`. |
| `reset()` | Clear model state between episodes. |

Action dict keys: dual-arm uses `left_arm_joint_state` / `right_arm_joint_state` plus `left_ee_joint_state` / `right_ee_joint_state`; single-arm drops the `left_` / `right_` prefix; `action_type=ee` replaces `*_arm_joint_state` with `*_ee_pose` as `[x, y, z, qw, qx, qy, qz]`.

Take dimensions from `get_robot_action_dim_info(env_cfg_type)` in `XPolicyLab.utils.process_data`, and register every new robot in **both** robot-info files — `AGENTS.md` at the repo root has the table and explains why the two `get_action_dim` entry points read different files. A private loader is acceptable only when it must run without importing XPolicyLab, and then it needs a configurable root plus a fallback, as `policy/AHA_WAM` does with `env_cfg_root`.

## Conventions

`AGENTS.md` at the repo root states the image, path, and dimension rules that apply to every change; it is always loaded, so follow it rather than re-deriving anything. The three that adapters get wrong most often: `model.py` never decodes (the server already did); offline code decodes **only** via `decode_image_bit` and writes stored bits **only** via `encode_image_bit`, because image bits come in two byte formats plus older container layouts and only that pair covers them all (see README [Standard Data Formats](../../../README.md#decode-only-through-decode_image_bit)); and everything is RGB end to end — a `COLOR_BGR2RGB` added after a decode is always a bug, since the decoded pixels are indistinguishable to the eye — only the buffer's marker tells the formats apart — and a caller-side swap is right on at most one of them. The only exceptions are medium adapters around `cv2.VideoWriter` / `cv2.VideoCapture` and a documented `deploy.yml` opt-in like `policy/Dexora_1B`'s `input_color_order`.

Adapter-specific conventions on top of those:

- `eval.sh` positional args, same for all adapters: `bench_name task_name ckpt_name env_cfg_type action_type seed policy_gpu_id env_gpu_id policy_env_or_uv_path eval_env_conda_env`.
- **The importable root is `Path(__file__).resolve().parent.parents[2]`** (equivalently `Path(__file__).resolve().parents[3]`) — the parent of the XPolicyLab checkout, since the server imports `XPolicyLab.policy.<POLICY>.model`. Counted from the policy directory, `parents[3]` is especially damaging: it silently shadows modules when inserted at `sys.path[0]`.
- **Resolve checkpoints with `XPolicyLab.utils.checkpoint_resolver`**: `resolve_checkpoint_root(model_cfg, checkpoints_dir)` covers the shared precedence (explicit `deploy.yml` path key, `ckpt_name` as a path, the concatenated run-dir name, then `checkpoints/<ckpt_name>`). Adapters with an extra naming layer build on `build_run_dir_name` / `candidate_checkpoint_roots` instead of starting over. Checkpoints land in `checkpoints/<bench_name>-<ckpt_name>-<env_cfg_type>-<action_type>-<seed>/`.
- Observations carry the language prompt under `instruction` (string; fall back to `instructions`). Poses are `[x, y, z, qw, qx, qy, qz]`.
- Trajectory HDF5 files store a singular `instruction` string and camera extrinsics as `extrinsic_matrix`; runtime observations use `extrinsics_matrix`.
- Full observation/trajectory format trees live in the repo README under "Standard Data Formats".

## Debug-mode troubleshooting

| Symptom | Usual cause |
| --- | --- |
| `ModuleNotFoundError` for the policy | Missing `policy/<POLICY>/__init__.py`, or `install.sh` did not install into the env passed as `<policy_env>`. |
| Client retries connect, then gives up | The server crashed during model loading — read the policy-server log, not the client log; model tracebacks are only printed server-side. |
| Action rejected for wrong keys/dims | Action dict keys must match `action_type` and the arm count; take dims from `get_robot_action_dim_info(env_cfg_type)`. |
| `FileNotFoundError` on `env_cfg/<type>.yml` or `_robot_info.json` | The adapter built the `env_cfg` path itself and pointed it inside the repo, or the robot is registered in only one of the two robot-info files. |
| Works plain, fails with `DEBUG_OBS_ENCODED=1` | `model.py` is decoding images itself, or assumes writable arrays — decoded arrays are read-only views, so copy first. |
| Call times out | Inference is slower than `request_timeout_s` (default 120 s); raise it in `deploy.yml`. |

## Reporting back

Finish with: what was created or changed, the exact eval command you ran and its result, supported `action_type` / `env_cfg_type`, expected checkpoint layout, and anything still unverified (e.g. training untested, no real checkpoint available). Never claim the debug loop passed if you could not run it.

````

## .agents/skills/xpolicylab-adapter-check/SKILL.md
````
---
name: xpolicylab-adapter-check
description: Audit a policy/<POLICY>/ adapter for XPolicyLab standard compliance and PR readiness — file completeness, deploy.yml, Model contract, decode_image_bit-only decoding, script conventions, static checks, debug-mode eval, README and checkpoint requirements. Use when asked to check, validate, review, or pre-flight a policy adapter or a policy submission PR in the XPolicyLab repo.
---

# XPolicyLab Adapter Check

Audit `policy/<POLICY>/` against the submission standard and report pass/fail per item with concrete fixes. The full standard lives in `CONTRIBUTING.md` at the repo root — read it before auditing; the list below is the executable summary. `policy/demo_policy/` is the reference implementation.

This is a **read-only audit**: report the fixes, do not apply them unless the user asks. If the user did not name a policy, list the adapters that changed on the current branch and ask which to audit.

## Checks

Run commands from the repo root unless noted.

1. **Files** — required: `README.md`, `__init__.py`, `eval.sh`, `setup_eval_policy_server.sh`, `setup_eval_env_client.sh`, `deploy.yml`, `deploy.py`, `model.py`. Three more are required but have a declared exception: `process_data.sh` / `train.sh` may be absent for a declared eval-only submission, and `install.sh` may be absent when the environment comes entirely from an upstream recipe and the policy README's `Installation` section carries the manual steps (`policy/Dexora_1B`, `policy/X_WAM`). An undeclared absence is a fail.
2. **deploy.yml** — `policy_name` equals the directory name (the server imports `XPolicyLab.policy.<policy_name>.model`). Ten keys are required and present in every adapter today: `policy_name`, `protocol` (`ws`), `host`, `port`, `bench_name`, `task_name`, `env_cfg_type`, `seed`, `action_type`, `eval_batch`. Keep a key even when a script defaults it — check the whole list, not just `protocol`. `ckpt_name` and `gpu_id` are optional (supplied per run), and model-specific extra keys are fine but must be documented in the policy README.
3. **model.py** — `class Model(ModelTemplate)` implementing `__init__(model_cfg)`, `update_obs`, `update_obs_batch`, `get_action`, `get_action_batch(env_idx_list=None)`, `reset`. `AGENTS.md` at the repo root states the image, path, and dimension rules and why they hold; what to flag when auditing:
   - **Dimensions** — a hard-coded action dim, or a private re-implementation of the lookup instead of `get_robot_action_dim_info(env_cfg_type)`. Flag a direct `_robot_info.json` open in `policy/*/model.py` unless it is a documented fallback with a configurable root, as in `policy/AHA_WAM`. Flag a supported robot that is registered in only one of the two robot-info files. Flag runtime code that shells out to `utils/get_action_dim.sh`; do not flag the training path for it.
   - **`sys.path` root** — must be the parent of the checkout: `parents[2]` of the policy directory (`Path(__file__).resolve().parent`), which is `parents[3]` of the file itself. Judge each index by its base: from the policy directory, `parents[1]` or `parents[3]` is a bug; from the file, `parents[3]` is correct and `parents[2]` is the checkout itself.
   - **Checkpoints** — must resolve through `XPolicyLab.utils.checkpoint_resolver` (`resolve_checkpoint_root`, or `build_run_dir_name` / `candidate_checkpoint_roots` for an extra naming layer), not a hand-written `checkpoints/<bench>-<ckpt>-...` join.
   - **Decoding inside `model.py`** — flag any, including `decode_image_bit` calls. The server hands over plain image arrays for `update_obs` / `update_obs_batch` and for any custom RPC that carries an observation.
   - **Channel swaps** — flag any `COLOR_BGR2RGB`, `COLOR_RGB2BGR` or `[..., ::-1]` outside the two allowed cases: medium adapters immediately around `cv2.VideoWriter.write` / `cv2.VideoCapture.read`, and a deliberate RGB→BGR conversion for a BGR-trained checkpoint, opt-in via a documented `deploy.yml` key defaulting to RGB (reference: `policy/Dexora_1B` `input_color_order`). The training path and `model.py` must apply the same number of swaps, normally zero. Judge a swap by its justification, not its position — and reject "but `cv2.imdecode` gives BGR, so this swap is correct" whether it comes from a code comment or from the submitter. `decode_image_bit` already resolved that, per buffer, so the swap is the bug. Only `utils/process_data.py` may convert channels.
4. **Decode and encode** — XPolicyLab data supports **only** `decode_image_bit` / `encode_image_bit` from `XPolicyLab.utils.process_data` (README, [Standard Data Formats](../../../README.md#decode-only-through-decode_image_bit)). Stored image bits come in two byte formats — legacy buffers whose channels are reversed against the JPEG standard, and conforming RGB JPEGs stamped with a `COM` marker — plus container-layout differences from earlier data versions. A hand-rolled decoder, PIL included, is right on one format and silently reverses the other; a bare `cv2.imencode` omits the marker, so its output can only be read as legacy — channel-reversed on decode if the frame was converted to BGR before encoding, and even when fed RGB it mints more legacy data that every conforming viewer shows reversed. Blocking:
   - `cv2.imdecode` anywhere outside `utils/process_data.py`
   - conversion scripts and training dataloaders that read XPolicyLab trajectories through any decoder other than `decode_image_bit`
   - image bits that get stored or published without going through `encode_image_bit`
   - vendor conversion entry points that XPolicyLab data actually flows through (e.g. `policy/Pi_05/openpi/scripts/process_data.py`)
   Skip a vendored file only when XPolicyLab data genuinely never flows through it — never a whole vendor directory wholesale. A `cv2.imencode` whose output is decoded again inside the same process (a compression simulator, a test client) is fine; one whose output is written to disk or sent to another system is not.
5. **Scripts** — `eval.sh` consumes the 10 standard args (`bench_name task_name ckpt_name env_cfg_type action_type seed policy_gpu_id env_gpu_id policy_env_or_uv_path eval_env_conda_env`) and stays aligned with `policy/demo_policy/eval.sh`; extra args must be documented in the policy README.
6. **Static checks**:

   ```bash
   bash -n policy/<POLICY>/*.sh
   python -m py_compile policy/<POLICY>/model.py policy/<POLICY>/deploy.py
   ```

   Then the mechanical greps, from the repo root. The missing-key loop and the decode grep must return nothing on adapter-owned code; the rest surface hits that need judging:

   ```bash
   # required deploy.yml keys that are missing
   for k in policy_name protocol host port bench_name task_name env_cfg_type seed action_type eval_batch; do
     grep -q "^${k}:" policy/<POLICY>/deploy.yml || echo "missing: ${k}"
   done
   # sys.path root candidates — judge each index against its base (see check 3)
   grep -rnE 'parents\[[123]\]' policy/<POLICY>/*.py
   # private env_cfg / robot-dim lookup
   grep -rnE '_robot_info\.json|env_cfg' policy/<POLICY>/model.py
   # only decode_image_bit is supported — fail any adapter-owned hit
   grep -rnE 'cv2\.imdecode|np\.frombuffer|Image\.open' policy/<POLICY>/
   # stored bits must come from encode_image_bit — judge each hit
   grep -rn 'cv2\.imencode' policy/<POLICY>/
   # channel swaps — judge each hit
   grep -rnE 'COLOR_BGR2RGB|COLOR_RGB2BGR|\.\.\., ::-1' policy/<POLICY>/
   ```

   `parents[...]`, channel-swap, `cv2.imencode` and `env_cfg` hits can be legitimate — `Path(__file__).resolve().parents[3]` as the parent of the checkout, `env_cfg_type` as a config key, a `VideoWriter` / `VideoCapture` adapter, a documented `input_color_order`, an encode whose output is decoded again in the same process — so judge each one; the point is that no hit goes unexamined. Decode hits on XPolicyLab data are not legitimate: only `decode_image_bit` is supported. Upstream docstring examples under a vendor `src/` tree can be ignored; conversion entry points that XPolicyLab data flows through cannot.

7. **Debug closed loop** — only when an environment with the policy dependencies is available:

   ```bash
   cd policy/<POLICY>
   EVAL_ENV_TYPE=debug bash eval.sh RoboDojo stack_bowls <ckpt_name> arx_x5 joint 0 0 0 <policy_env> base
   ```

   `<policy_env>` (arg 9) follows the adapter's own convention — a conda env name, `uv`, or an environment path; `policy/Pi_05`, for example, requires `uv` (see its README). The trailing `base` is the eval-env conda env (arg 10).

   Must reach `[MAIN] eval finished` with no tracebacks. Re-run with `DEBUG_OBS_ENCODED=1` so the debug client sends encoded camera colors and the server-side decode path is exercised. If it cannot be run, report the item as "not run" — never as passed.
8. **Policy README** — install / data / train / eval commands present and consistent with the actual scripts; supported `action_type` / `env_cfg_type`; checkpoint layout; known limitations. An adapter that trains on LeRobot data must also declare, under `Data Processing`, the dataset version and whether its keys match the official converters (README, [Official LeRobot conversion](../../../README.md#official-lerobot-conversion)) — naming the converter or prepared export when they do, and the deviation when they do not.
9. **PR readiness** (when auditing a submission PR) — description follows `.github/PULL_REQUEST_TEMPLATE.md`; checkpoint download script included (Hugging Face or ModelScope preferred) if targeting a leaderboard; eval-only status declared with a training-release timeline.

## Report format

- One line per check: ✅ pass / ❌ fail / ⚠️ not run, with a short reason.
- For each ❌: name the file and the exact change, pointing to `policy/demo_policy` where useful.
- End with a verdict: **ready for PR** or **needs fixes** (list blocking items first).
- Then offer to apply the fixes.

Keep the report short — checks that pass need one line, not an explanation. Never mark an item ✅ based on reading code alone when the check is a command you did not run.

````

## model_template.py
````
class ModelTemplate:
    """
    Base template for a policy/model class.
    策略/模型类的基础模板。

    This template defines the minimal interface required for:
    该模板定义了一个模型在以下场景中常用的最小接口：
    1. loading or building a model
       加载或构建模型
    2. updating observations from the environment
       接收并更新环境观测
    3. generating actions
       生成动作
    4. resetting internal states between episodes
       在每个 episode 之间重置内部状态

    Notes / 说明:
    - You should override the methods in your own subclass or implementation.
      你应该在自己的子类或具体实现中重写这些方法。
    - `self.model` can be a neural network, a planner, or any policy object.
      `self.model` 可以是神经网络、规划器，或者任意策略对象。
    """

    RED = "\033[31m"
    RESET = "\033[0m"

    def __init__(self):
        """
        Initialize the template model.
        初始化模板模型。

        Attributes / 属性:
            self.model:
                The actual model/policy object.
                实际的模型/策略对象。
        """
        self.model = None

    def _error_msg(self, msg: str) -> str:
        return f"{self.RED}[ERROR] {msg}{self.RESET}"

    def update_obs(self, obs):
        """
        Update the current observation used by the model.
        更新当前模型使用的观测。

        The policy server decodes camera colors before calling this, so
        obs["vision"][<camera>]["color"] is always an image array.
        策略服务端已完成图像解码，此处拿到的 color 一定是图像数组。
        """
        raise NotImplementedError(
            self._error_msg("update_obs() must be implemented by the user.")
        )

    def update_obs_batch(self, obs_list):
        """
        Update the current observation used by the model.
        更新当前模型使用的观测。

        Same decoding guarantee as update_obs().
        与 update_obs() 一样，图像已由服务端解码。
        """
        raise NotImplementedError(
            self._error_msg("update_obs_batch() must be implemented by the user.")
        )

    def get_action(self):
        """
        Predict or generate an action from the current observation/state.
        根据当前观测或内部状态预测/生成动作。
        """
        raise NotImplementedError(
            self._error_msg("get_action() must be implemented by the user.")
        )

    def get_action_batch(self, env_idx_list=None):
        """
        Predict or generate an action from the current observation/state.
        根据当前观测或内部状态预测/生成动作。
        """
        raise NotImplementedError(
            self._error_msg("get_action_batch() must be implemented by the user.")
        )

    def reset(self):
        """
        Reset the internal state of the model at the start of a new episode.
        在新 episode 开始时重置模型内部状态。
        """
        pass

    def prepare_case(self, case_meta=None):
        """
        Optional hook called before an action case starts.
        在 action case 开始前调用的 hook。
        """
        pass

    def on_trial_end(self, result=None):
        """
        Optional hook called after a trial finishes.
        在单次 trial 结束后调用的 hook。
        """
        pass

````

## setup_policy_server.py
````
import asyncio
import os
import threading
import ast
import time
import yaml
import importlib
import argparse
import traceback
from client_server.tcp.model_server import ModelServer


def _default_protocol() -> str:
    """Default to the websocket policy protocol."""
    return "ws"

def eval_function_decorator(policy_model_name, Func_and_Class_name):
    """Load a specified function (e.g., get_model) from a policy module"""
    module = importlib.import_module(policy_model_name)
    return getattr(module, Func_and_Class_name)

def main(deploy_cfg):
    """Main entry: load model, start server, run indefinitely"""
    # Extract basic arguments
    policy_name = deploy_cfg.get("policy_name")
    port = deploy_cfg.get("port")
    host = deploy_cfg.get("host", "0.0.0.0")
    protocol = deploy_cfg.get("protocol", "ws")

    # Instantiate model
    model_class_func = eval_function_decorator(f"XPolicyLab.policy.{policy_name}.model", "Model")
    model = model_class_func(deploy_cfg)

    if protocol == "ws":
        try:
            from client_server.ws.model_server import PolicyServer, PolicyServerConfig
        except ModuleNotFoundError as exc:
            if exc.name == "client_server":
                # client_server.ws ships in this repo; make it importable even when
                # XPolicyLab is not pip-installed in the current environment.
                import sys
                repo_root = os.path.dirname(os.path.abspath(__file__))
                if repo_root not in sys.path:
                    sys.path.insert(0, repo_root)
                try:
                    from client_server.ws.model_server import PolicyServer, PolicyServerConfig
                except ModuleNotFoundError as dep_exc:
                    raise RuntimeError(
                        "ws policy server requires XPolicyLab websocket dependencies "
                        f"(missing module: {dep_exc.name}). Install in the policy env with: "
                        "pip install -e . from the XPolicyLab root."
                    ) from dep_exc
            else:
                raise RuntimeError(
                    "ws policy server requires XPolicyLab websocket dependencies "
                    f"(missing module: {exc.name}). Install in the policy env with: "
                    "pip install -e . from the XPolicyLab root."
                ) from exc

        server = PolicyServer(
            model,
            PolicyServerConfig(
                host=host,
                port=int(port),
                ws_ping_interval_s=deploy_cfg.get("ws_ping_interval_s", 20.0),
                ws_ping_timeout_s=deploy_cfg.get("ws_ping_timeout_s", 20.0),
            ),
        )
        try:
            asyncio.run(server.serve_forever())
        except KeyboardInterrupt:
            print("\nShutting down websocket policy server...")
        return
    if protocol != "legacy_tcp":
        raise ValueError(f"unsupported policy server protocol: {protocol}")

    # Wrap server.start so exceptions inside thread are fully printed
    def run_server():
        try:
            server.start()
        except Exception:
            print("\033[31m[ERROR] Exception occurred inside server thread:\033[0m")
            traceback.print_exc()
            raise

    # Start server in background thread
    server = ModelServer(model, host=host, port=port)
    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()

    # Keep main thread alive until KeyboardInterrupt
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Shutting down server...")
        server.stop()
        thread.join()

def parse_args_and_config():
    """Parse CLI args and YAML config, merge overrides"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_path", "--config-path", dest="config_path", type=str, required=True, help="Path to config YAML")
    parser.add_argument("--protocol", choices=("legacy_tcp", "ws"), help="Policy server protocol")
    parser.add_argument("--host", help="Policy server bind host")
    parser.add_argument("--port", type=int, help="Policy server bind port")
    parser.add_argument("--relay-url", dest="relay_url", help="Relay URL for future relay mode")
    parser.add_argument("--overrides", nargs=argparse.REMAINDER, help="Override config values")
    args = parser.parse_args()

    # Load base config
    with open(args.config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    
    # Parse overrides: --key value pairs

    def _parse_val(s: str):
        # safer than eval; supports numbers/bool/None/list/dict when properly quoted
        try:
            return ast.literal_eval(s)
        except Exception:
            return s
        
    if args.overrides:
        tokens = args.overrides

        # Case A: key=value key=value ...
        if all(("=" in t and not t.startswith("-")) for t in tokens):
            for t in tokens:
                k, v = t.split("=", 1)
                cfg[k] = _parse_val(v)
        else:
            # Case B: --key value --key value ...
            if len(tokens) % 2 != 0:
                raise ValueError(f"--overrides expects key value pairs, got: {tokens}")

            it = iter(tokens)
            for key in it:
                val = next(it)
                cfg[key.lstrip("-")] = _parse_val(val)

    if args.protocol is not None:
        cfg["protocol"] = args.protocol
    else:
        cfg.setdefault("protocol", _default_protocol())
    if args.host is not None:
        cfg["host"] = args.host
    if args.port is not None:
        cfg["port"] = args.port
    if args.relay_url is not None:
        cfg["relay_url"] = args.relay_url

    def _require_non_empty(key: str):
        if key not in cfg:
            raise ValueError(f"{key} must be specified in config or overrides")
        val = cfg[key]
        if val is None:
            raise ValueError(f"{key} must be non-empty")
        if isinstance(val, str) and not val.strip():
            raise ValueError(f"{key} must be non-empty")

    _require_non_empty("host")
    _require_non_empty("port")
    return cfg

if __name__ == "__main__":
    deploy_cfg = parse_args_and_config()
    main(deploy_cfg)

````

## pyproject.toml
````
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "xpolicylab"
version = "0.0.1"
requires-python = ">=3.10"
dependencies = [
    "numpy>=1.23",
    "pyyaml>=6",
    "opencv-python-headless>=4.8",
    "h5py>=3.8",
    "websockets>=14.0",
    "msgpack>=1.0.8",
    "msgpack-numpy>=0.4.8",
    "pydantic>=2.5",
]

[tool.setuptools]
py-modules = ["XPolicyLab"]

[tool.setuptools.packages.find]
where = ["."]
include = ["client_server*", "utils*"]
exclude = ["policy*", "build*", "scripts*", "__pycache__*", "tests*"]

````

## policy/demo_policy/deploy.yml
````
policy_name: demo_policy
protocol: ws
host: localhost
port: null
bench_name: null
task_name: null
ckpt_name: null
env_cfg_type: null
seed: null
action_type: null
gpu_id: null
eval_batch: false

````

## client_server/ws/protocol/codec.py
````
"""msgpack encode/decode for WebSocket binary frames."""

from __future__ import annotations

import sys
from typing import Any

import msgpack
import msgpack_numpy
import numpy as np
from pydantic import ValidationError

from client_server.ws.protocol.exceptions import ErrorCode, WsError
from client_server.ws.protocol.schemas import Frame


def _tensor_to_numpy(obj: Any) -> Any:
    """Convert a torch.Tensor to numpy, or return obj unchanged.

    torch is looked up in sys.modules rather than imported: only a process
    that already loaded torch can hold a tensor, so this keeps the env-side
    client from paying a multi-second torch import (and a CUDA context) just
    to serialize observations.
    """
    torch = sys.modules.get("torch")
    if torch is None or not isinstance(obj, torch.Tensor):
        return obj
    # Same convenience as the legacy TCP codec: models may return CUDA or
    # half-precision tensors straight from inference.
    tensor = obj.detach().cpu()
    if tensor.dtype == torch.bfloat16:
        # numpy has no bfloat16; widen instead of failing.
        tensor = tensor.float()
    return tensor.numpy()


def _encode_numpy(obj: Any) -> Any:
    obj = _tensor_to_numpy(obj)
    if isinstance(obj, np.ndarray):
        if obj.dtype.kind == "O":
            raise WsError(
                ErrorCode.INVALID_FRAME, "object dtype numpy arrays are not supported"
            )
        return msgpack_numpy.encode(obj)
    if isinstance(obj, np.generic):
        if obj.dtype.kind == "O":
            raise WsError(
                ErrorCode.INVALID_FRAME, "object dtype numpy scalars are not supported"
            )
    return msgpack_numpy.encode(obj)


def _normalize_map_keys(mapping: dict[Any, Any]) -> dict[Any, Any]:
    """Match the legacy JSON codec: int-keyed maps arrive with str keys.

    json.dumps turned ``{0: ...}`` into ``{"0": ...}`` on the wire, so every
    model written against the TCP protocol indexes env-idx-keyed maps by
    string. msgpack preserves int keys, which would silently change those
    lookups from obs["0"] to obs[0]; normalize back to strings instead.
    """
    if all(isinstance(key, str) for key in mapping):
        return mapping
    out: dict[Any, Any] = {}
    for key, value in mapping.items():
        if isinstance(key, int) and not isinstance(key, bool):
            key = str(key)
        if key in out:
            raise ValueError(
                f"duplicate map key after int->str normalization: {key!r}"
            )
        out[key] = value
    return out


def _decode_numpy(obj: dict[Any, Any]) -> Any:
    if obj.get(b"nd") is True and obj.get(b"kind") == b"O":
        raise ValueError("object dtype numpy arrays are not supported")
    decoded = msgpack_numpy.decode(obj)
    if isinstance(decoded, np.ndarray) and decoded.dtype.kind == "O":
        raise ValueError("object dtype numpy arrays are not supported")
    if isinstance(decoded, dict):
        decoded = _normalize_map_keys(decoded)
    return decoded


def encode_frame(frame: Frame | dict[str, Any]) -> bytes:
    if isinstance(frame, Frame):
        wire = frame.to_wire_dict()
    else:
        wire = dict(frame)
    try:
        return msgpack.packb(wire, default=_encode_numpy, use_bin_type=True)
    except WsError:
        raise
    except Exception as exc:
        raise WsError(ErrorCode.INVALID_FRAME, f"msgpack encode failed: {exc}") from exc


def decode_frame(data: bytes) -> dict[str, Any]:
    try:
        obj = msgpack.unpackb(
            data,
            raw=False,
            # Observations may key dicts by env index. Accept int keys here;
            # _decode_numpy then normalizes them to strings so models see the
            # same key type the legacy JSON codec delivered.
            strict_map_key=False,
            object_hook=_decode_numpy,
        )
    except Exception as exc:
        raise WsError(ErrorCode.INVALID_FRAME, f"msgpack decode failed: {exc}") from exc
    if not isinstance(obj, dict):
        raise WsError(ErrorCode.INVALID_FRAME, "frame must be a msgpack map")
    return obj


def decode_envelope(data: bytes) -> Frame:
    try:
        return Frame.from_wire_dict(decode_frame(data))
    except WsError:
        raise
    except (TypeError, ValueError, ValidationError) as exc:
        raise WsError(
            ErrorCode.INVALID_FRAME, f"invalid frame envelope: {exc}"
        ) from exc

````

## utils/robot/_robot_info.json
````
{
    "piper": {
        "arm_dim": [6, 6],
        "ee_dim": [1, 1]
    },
    "arx_x5": {
        "arm_dim": [6, 6],
        "ee_dim": [1, 1]
    },
    "piper_x": {
        "arm_dim": [6, 6],
        "ee_dim": [1, 1]
    },
    "tianji_marvin_wuji": {
        "arm_dim": [7, 7],
        "ee_dim": [20, 20]
    },
    "aloha_agilex": {
        "arm_dim": [6, 6],
        "ee_dim": [1, 1]
    },
    "franka": {
        "arm_dim": [7, 7],
        "ee_dim": [1, 1]
    }
}

````

## policy/GPT_6_Astra_Direct_EEF/README.md
````
# GPT_6_Astra_Direct_EEF

**Contributor:** RoboProbe / RoboDojo Team | **Paper:** An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond | **arXiv:** https://arxiv.org/abs/2609.24170 | **Original code:** https://github.com/RoboProbe/RoboProbe

Evaluation-only, RGB-only GPT-6 Astra agent. The model (`L4_INSPECT_PLANNER=astra`, model id `gpt-6-astra`) calls one `move_eef` tool that names world-frame grasp-point dimensions. RoboDojo's local Cartesian planner turns those poses into time-aligned joint paths. There is no VLA checkpoint and no training entry. Shared Inspect runtime lives in `inspect/`.

Shared conventions — argument meanings, checkpoint naming, split-machine deployment, `EVAL_ENV_TYPE` — are documented in the [XPolicyLab README](../../README.md). Official results: [RoboDojo LeaderBoard](https://robodojo-benchmark.com/LeaderBoard).

## Installation

The policy server loads no weights. It borrows a Python that can import XPolicyLab (`uv` resolves `policy_uv_env_path` in `deploy.yml`, default `../Pi_05/openpi`). The eval client is where the LLM runs, and that interpreter needs `openai==3.8.0` and `pillow==12.3.0`:

```bash
bash policy/GPT_6_Astra_Direct_EEF/install.sh \
  /path/to/RoboDojo-eval/.venv/bin/python
```

Set `ARK_API_KEY` before evaluating. `ARK_API_KEY_BACKUP` is optional.

## Data Processing

Unsupported. This is an eval-only adapter: `process_data.sh` is omitted, and it does not convert datasets.

## Training

Unsupported. `train.sh` is omitted. There is no checkpoint directory and no training release to schedule. Actions are produced at eval time by the provider API.

## Evaluation

Layout-range entry, same arguments as the original EEF adapter. There is no separate policy GPU: the simulator uses `env_gpu`, and the only inference is the API call. Default task is `arrange_largest_number`. Default planner hard timeout is 90 seconds.

```bash
export ARK_API_KEY=...
export ROBODOJO_ROOT=/path/to/RoboDojo-eval

bash policy/GPT_6_Astra_Direct_EEF/run_fixed_layout.sh \
  0 0 general_pickup uv
```

Positional arguments are `<layouts> <env_gpu> <task> <eval_env>`. `layouts` is one index (`16`), an inclusive range (`20-39`), or a mix (`1-3,5,12-14`).

Standard harness entry:

```bash
bash policy/GPT_6_Astra_Direct_EEF/eval.sh \
  RoboDojo general_pickup no-checkpoint arx_x5 joint 0 0 0 uv uv
```

`policy_env` (arg 9) is `uv` or a uv project directory that contains `.venv/bin/python`. `eval_env` (arg 10) is `uv` (the `ROBODOJO_ROOT/.venv`), a virtualenv directory, a Python binary, or a conda env that already has the pinned `openai` and `pillow` versions.

`action_type` must stay `joint`: EEF is the model-facing action, and RoboDojo receives the planner's joint path. `env_cfg_type` is `arx_x5`. `ckpt_name` is ignored; `no-checkpoint` is the conventional placeholder. Batch evaluation is not supported.

Offline wiring check (no simulator). The debug client has no Cartesian planner, so motions are not planned. The loop still builds the action spec from the RoboDojo URDF (`ROBODOJO_ROOT/Assets/Robots/x5/X5A.urdf`) and can stop without calling the provider when `L4_INSPECT_MAX_LLM_CALLS=0`:

```bash
export EVAL_ENV_TYPE=debug
export ROBODOJO_ROOT=/path/to/RoboDojo-eval
export ARK_API_KEY=...
bash policy/GPT_6_Astra_Direct_EEF/eval.sh \
  RoboDojo stack_bowls no-checkpoint arx_x5 joint 0 0 0 uv <eval_env>
```

Re-run with `DEBUG_OBS_ENCODED=1` to exercise encoded camera colors. The client decodes those with `decode_image_bit`.

## Configuration

Extra `deploy.yml` keys beyond the shared set:

| Key | Role |
| --- | --- |
| `policy_uv_env_path` | uv project used when `policy_env` is `uv` (default `../Pi_05/openpi`) |
| `result_dir` | default result directory name |
| `obs_transform_pipeline` | observation transform tag (`xspark-v1.0`) |

Planner overrides (environment):

| Variable | Default | Role |
| --- | --- | --- |
| `L4_INSPECT_PLANNER` | `astra` | `astra` → `gpt-6-astra`; `gpt55` → `gpt-5.5-2026-04-24` |
| `L4_INSPECT_MODEL` | planner default | override the model id |
| `L4_INSPECT_MAX_LLM_CALLS` | `100` | per-episode call budget |
| `L4_INSPECT_DEPTH` | `off` | must stay `off` or unset |

## Notes

- The model estimates Cartesian targets from RGB and proprioception. It does not receive metric depth.
- Data processing and training are unsupported.
- A real episode needs `ROBODOJO_ROOT`, a RoboDojo client with CuRobo, and `ARK_API_KEY`.

````
