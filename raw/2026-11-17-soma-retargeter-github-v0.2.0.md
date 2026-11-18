# Capture: https://github.com/NVIDIA/soma-retargeter/tree/v0.2.0
Captured 2026-11-17 by git clone at tag v0.2.0 (commit 1733b820f3cdf6f74bbc81a10bda3201b38c7bcf, 2026-09-15). Bundle of repository files, verbatim, each under a ==== FILE header: README.md, CHANGELOG.md, documentation/code-overview.md, documentation/robot-configuration-reference.md, documentation/ik-weight-optimizer.md, documentation/foot-contact.md. A later tag, v0.2.1 (2026-10-01), changes only a Robot Configurator DOF-range bug.

==== FILE README.md

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Version](https://img.shields.io/github/v/tag/NVIDIA/soma-retargeter?sort=date&label=version)](https://github.com/NVIDIA/soma-retargeter/tags)

# SOMA Retargeter

![SOMA Retargeter banner](documentation/images/banner_allrobots.gif)

SOMA Retargeter converts human motion in a SOMA-skeleton BVH file into joint animation for a humanoid robot. The result is a CSV file that can be inspected, compared, or passed to downstream robot-control and simulation tools.

Start with the bundled motion and robot, confirm that the software works on your computer, and then move on to your own files and tuning.

> **Important:** SOMA Retargeter is in active beta, so APIs and features may change without notice. Generated motion is kinematic; validate its safety, feasibility, and controller compatibility in simulation before hardware use.

## What the retargeter does

The human source and target robot have different proportions and joints. SOMA  
Retargeter does the following:

1. reads a SOMA-base skeleton BVH animation;
2. retargets human scale joints to the robot's proportions;
3. solves inverse kinematics for each frame;
4. stabilizes contacts and clamps configured joint limits;
5. writes the robot root pose and actuated joint values to CSV.

![Retargeting pipeline from BVH to robot CSV](documentation/images/retargeting-pipeline.png)


The repository includes:

- 10 example BVH motions and matching CSV results for all five bundled robots;
- an interactive viewer for loading, retargeting, inspecting, and saving one motion;
- a headless mode for converting folders of motions;
- configuration and model assets for `unitree_g1`, `unitree_h2`, `booster_t1`, `agibot_x2ultra`, and `agibot-a3t3`;
- tools for configuring another robot and tuning and optimizing inverse-kinematics weights.
- 15 BVH motions for inverse-kinematics weights optimization

## Motion data and credit
The bundled BVH motion examples and optimizer inputs are provided with permission from [Bones](https://bones.studio/) and are drawn from the [BONES-SEED dataset](https://bones.studio/datasets/seed). We thank the Bones team for supporting this release. See BONES-SEED for the broader motion collection and licensing options.


## Documentation structure

Documentation from setup through batch processing:

![Documentation workflow from setup through batch processing](documentation/images/workflow-overview.png)

1. **[Installation](documentation/installation.md)** — install prerequisites, create the environment, download assets, and verify the setup.
2. **[First retarget](documentation/first-retarget.md)** — convert one bundled BVH in the interactive viewer and save a CSV.
3. **[Robot configurator](documentation/robot-configurator.md)** — begin the guided process of adding a robot. The later tutorial uses Unitree H1 as the new-robot example;
4. **[Robot configuration reference](documentation/robot-configuration-reference.md)** — understand manifests, model descriptions, retargeting objectives, scaling, and post-processing settings.
5. **[Contact detection & foot-plant correction configuration](documentation/foot-contact.md)** — detailed description of contact detection and foot planting settings.
6. **[Interactive retargeting](documentation/interactive-retargeting.md)** — learn viewer controls and work with SOMA BVH files.
7. **[IK weight optimizer](documentation/ik-weight-optimizer.md)** — optimize for better objective weights.
8. **[Compare and tune](documentation/compare-and-tune.md)** — evaluate results and refine a robot configuration.
9. **[Batch retargeting](documentation/batch-retargeting.md)** — convert a directory tree without opening a viewer.
10. **[Code overview](documentation/code-overview.md)** — review the main application entry points and `soma_retargeter` package modules.
11. **[Troubleshooting](documentation/troubleshooting.md)** — diagnose installation, viewer, input, GPU, and output problems.

## Inputs and outputs

### Input: SOMA BVH

A `.bvh` file contains a skeleton hierarchy and one pose per animation frame. The retargeter currently expects the source hierarchy and naming used by the SOMA base skeleton. An arbitrary BVH exported from another character or motion capture package may load incorrectly or fail because its skeleton is different.

For the first run, use `assets/motions/bvh/Neutral_walk_forward_002__A057.bvh`. Keeping the input known removes one source of incertainty while you test the installation.

### Output: robot CSV

The `.csv` output stores the root pose and actuated robot joint values over time. Joint columns correspond to the selected robot model. Two target robots can have different columns, even when they were generated from the same BVH.

The bundled CSV files under `assets/motions/csv/` are organized by robot and provide reference results for all five bundled robots. Select the folder matching your target robot. Your result should have the same general motion, but exact values can change when configuration or dependency versions change.

## Bundled robot targets

Use these exact target names when using bundled robots:

- `unitree_g1` — the default target and the best choice for the first tutorial;
- `unitree_h2`;
- `booster_t1`;
- `agibot_x2ultra`;
- `agibot-a3t3`.

The interactive viewer lists discovered targets in its robot selector. Headless conversion reads the target from the `retarget_target` field in the converter configuration.

## Command convention in this guide

Run commands from the repository root. The documentation uses `uv` because it creates and manages the project environment without requiring you to activate it manually:

```bash
uv run python app/bvh_to_csv_converter.py --config assets/default_bvh_to_csv_converter_config.json --viewer gl
```

Paths with forward slashes work in PowerShell and in Linux shells. If a path you provide contains spaces, enclose it in quotes.

## Related Work

SOMA Retargeter is a support tool within the SOMA ecosystem for humanoid motion data:

* [SOMA Body Model](https://github.com/NVlabs/SOMA-X) - Parametric human body model with standardized skeleton, mesh, and shape parameters
* [GEM-X](https://github.com/NVlabs/GEM-X) - Human motion estimation from video
* [Kimodo](https://github.com/nv-tlabs/kimodo) - Kinematic motion diffusion model for text and constraint-driven 3D human and robot motion generation
* [ProtoMotions](https://github.com/NVlabs/ProtoMotions) - GPU-accelerated simulation and learning framework for training physically simulated digital humans and humanoid robots
* [SONIC](https://nvlabs.github.io/GEAR-SONIC/) - Whole-body control for humanoid robots, training locomotion and interaction policies

## Acknowledgments

This project draws inspiration and builds upon excellent open-source work, including:
* [GMR](https://github.com/YanjieZe/GMR) - General Motion Retargeting
* [PyRoki](https://pyroki-toolkit.github.io/) - A Modular Toolkit for Robot Kinematic Optimization

## License

NVIDIA-authored source code is licensed under [Apache-2.0](LICENSE).

The bundled motion data under `assets/motions/bvh/`, `assets/motions/optimizer/`, and `assets/motions/csv/` is licensed separately under the [NVIDIA Sample Data Evaluation License](assets/motions/LICENSE.txt). It is not covered by Apache-2.0.

The repository directly includes third-party robot-description and mesh assets:

- Unitree G1 and Unitree H2 assets are licensed under BSD-3-Clause. See [`licenses/unitree-LICENSE.txt`](licenses/unitree-LICENSE.txt).
- Booster Robotics T1 assets are licensed under BSD-3-Clause. See [`licenses/booster-LICENSE.txt`](licenses/booster-LICENSE.txt).
- AGIBot X2 and AGIBot A3 assets are licensed under Mulan PSL v2. See [`licenses/agibot-LICENSE.txt`](licenses/agibot-LICENSE.txt) and the pinned upstream [X2 source](https://github.com/AgibotTech/agibot_x2_urdf/tree/77f43eb0904dae4c48ccd9154fee824f8ffd4d38/X2_URDF-v1.4.0) and [A3 source](https://github.com/AgibotTech/A3-A3U-robot-model/tree/589f508ff357447c610a3f3004419035ddc8f153/a3_t3d0).

The applicable robot-asset license texts and path scopes are also included in the top-level [LICENSE](LICENSE). License copies for Python dependencies are available in [`licenses/`](licenses/). Python dependencies are installed from package registries rather than copied into this repository.

Some manifest-driven workflows can ask NVIDIA Newton to retrieve a separately hosted robot asset at runtime. Those assets remain subject to their upstream terms and are not bundled by SOMA Retargeter unless they are present in this repository.

## Where to go next

Go to **[Installation](documentation/installation.md)** to prepare Python, Git LFS, the GPU driver, and the project environment. If you already completed installation, run the verification command there before continuing to **[First retarget](documentation/first-retarget.md)**.

---

[Next: Installation →](documentation/installation.md)

==== FILE CHANGELOG.md

# Changelog

## [0.2.0] - 2026-09-15

### Added

- Manifest-driven robot package discovery, including custom package paths through `extra_robot_paths`.
- Bundled packages for Unitree G1 and H2, Booster T1, AgiBot A3/T3, and AgiBot X2 Ultra, with their license files.
- Robot-package selection in the viewer.
- Robot Configurator for registering URDF or MJCF robots, mapping links, mirroring mappings, and editing joint offsets.
- Example retargeted motions for every bundled robot.
- Experimental contact detection and foot-plant correction.
- Experimental IK Weight Optimizer for generating candidate weights from tracking and smoothness metrics.

### Changed

- Migrated robot assets and configurations to manifest-based packages; custom v0.1 configurations require updating.
- Improved bundled mapping, scaling, and post-processing configurations for better pose matching.
- Upgraded Newton to 1.3.0 and set the minimum required Warp version to 1.14.0.

### Fixed

- Corrected smooth joint-limit filtering for active DOF masks and configurable lower and upper offsets.
- Improved validation and error reporting for malformed BVH files and incomplete custom robot configurations.

## [0.1.0] - 2026-03-16

Initial public release.

==== FILE documentation/code-overview.md

# Code Overview

This page summarizes the main application entry points and the importable `soma_retargeter` package.

## `app/`

| File | Description |
|------|-------------|
| `bvh_to_csv_converter.py` | Main Retargeting application. Runs the interactive OpenGL viewer for live retargeting preview and handles headless batch BVH-to-CSV conversion. |
| `tools/robot_config_generator.py` | Robot Configurator tool. Loads a URDF or MJCF, copies robot assets into `assets/robotics/`, creates the robot manifest, defines SOMA-to-robot link mappings, and writes the scaler and retargeter config files. |
| `tools/ik_weight_optimizer.py` | IK Weight Optimizer tool. Runs repeated retargeting passes over a BVH corpus, scores tracking and smoothness metrics, and writes an optimized `ik_match_table` config. |

## `soma_retargeter/`

### `pipelines/`

The core retargeting pipeline. `SomaRetargetingPipeline` in `soma_retargeting_pipeline.py` orchestrates the full run:

1. Scales human effector targets to robot proportions (`HumanToRobotScaler`).
2. Prepends initialization and stabilization frames.
3. Runs a **base IK pass** (Newton Levenberg–Marquardt) with position, rotation, joint-limit, and smooth-filter objectives.
4. Optionally runs a **post-process pass** — two-bone limb stabilization and foot-plant correction blending.
5. Clamps all joint coordinates to limits before output.

| File | Role |
|------|------|
| `soma_retargeting_pipeline.py` | Top-level pipeline: config loading, pass construction, frame loop, output. |
| `ik_solver.py` | `IKSolver` / `BaseIKSolver` — own the Newton IK solver, joint_q buffer, and objective factories. |
| `ik_pass.py` | `BasePass` / `PostProcessPass` — per-frame execution with CUDA-graph capture. |
| `ik_objectives.py` | `IKSmoothJointFilter` — custom smooth joint-limit objective. |
| `limb_stabilizer.py` | Two-bone IK for feet and hands during the post-process pass. |
| `joint_limit_clamper.py` | Hard clamp of joint coordinates to model limits after the solve. |
| `plant_subsegment_detector.py` | Detects foot-plant sub-segments from contact results. |
| `plant_correction_blender.py` | Blends foot-plant corrections into effector targets. |
| `utils.py` | Config loading, source-type helpers, robot builder construction. |

### `animation/`

Core data structures and algorithms operating on source-skeleton data.

| File | Role |
|------|------|
| `skeleton.py` | `Skeleton` and `SkeletonInstance` — joint hierarchy, local/global transforms. |
| `animation_buffer.py` | `AnimationBuffer` — frame-indexed local transforms with sample-rate metadata. |
| `contact_detection.py` | Velocity/jerk-based foot contact detection (`detect_contacts_velocity_jerk`). |
| `contact_phase.py` | Foot landmark models (authored and heuristic) used by plant detection. |
| `ik.py` | Skeleton-space IK helpers. |
| `mesh.py` | Skinned mesh data structures. |

### `robotics/`

Robot-side data and registry.

| File | Role |
|------|------|
| `robot_registry.py` | Registers robot manifests and resolves robot asset roots by name. |
| `human_to_robot_scaler.py` | Computes scaled effector targets from source-skeleton poses. |
| `csv_animation_buffer.py` | `CSVAnimationBuffer` — wraps raw joint-coordinate arrays for CSV output. |

### `io/`

File I/O for animation and configuration formats.

| File | Role |
|------|------|
| `bvh.py` | BVH parser — returns `(Skeleton, AnimationBuffer)`. |
| `csv.py` | CSV writer for retargeted joint-coordinate sequences. |
| `usd.py` | USD skeletal mesh loader. |
| `utils.py` | Shared path and format helpers. |

### `renderers/`

OpenGL visualization used by the interactive applications.

| File | Role |
|------|------|
| `skeleton_renderer.py` | Draws joint hierarchies as lines and spheres. |
| `mesh_renderer.py` | Draws skinned robot and human meshes. |
| `coordinate_renderer.py` | Draws remapped coordinate axis overlays. |
| `base_renderer.py` | Shared VAO/shader setup. |

### `utils/`

Math and integration helpers.

| File | Role |
|------|------|
| `newton_utils.py` | Joint coordinate masks, initialization frame construction, Newton/Warp helpers. |
| `space_conversion_utils.py` | `SpaceConverter` — converts source-space root transforms to Newton world space. |
| `pose_utils.py` | Batched global pose computation. |
| `math_utils.py` | Quaternion, vector, and interpolation utilities. |
| `maya_utils.py` | Maya coordinate-space helpers. |
| `time_utils.py` | Timing utilities. |

### `assets/`

Bundled runtime assets: SOMA source skeleton BVH, robot description manifests, scaler and retargeter configs, and USD skeletons.

---

## Example

Retarget one bundled SOMA BVH to `unitree_h2`, save the result as CSV, then open the viewer to play it back.

```python
from pathlib import Path

import newton
import newton.examples
import warp as wp

from app.bvh_to_csv_converter import Viewer
from soma_retargeter.io import bvh as bvh_io
from soma_retargeter.io import csv as csv_io
from soma_retargeter.pipelines.soma_retargeting_pipeline import SomaRetargetingPipeline
from soma_retargeter.utils.newton_utils import get_filtered_joint_names
from soma_retargeter.utils.space_conversion_utils import (
    SpaceConverter,
    get_facing_direction_type_from_str,
)

bvh_path = Path("assets/motions/bvh/Neutral_walk_forward_002__A057.bvh")
csv_path = Path("output/examples/unitree_h2_walk.csv")
csv_path.parent.mkdir(parents=True, exist_ok=True)

# Load the SOMA-skeleton BVH animation.
skeleton, animation = bvh_io.load_bvh(str(bvh_path))

# Match the default converter orientation (Mujoco convention).
space_converter = SpaceConverter(get_facing_direction_type_from_str("Mujoco"))
source_offset = space_converter.transform(wp.transform_identity())

# Build and run the retargeting pipeline.
pipeline = SomaRetargetingPipeline(
    skeleton=skeleton,
    source_type="soma",
    robot_type="unitree_h2",
)
pipeline.add_input_motions([animation], [source_offset], scale_animation=True)
csv_buffers = pipeline.execute()

# CSV columns are the robot's revolute joints in model order.
joint_names = get_filtered_joint_names(pipeline.robot_builder, [newton.JointType.REVOLUTE])
csv_io.save_csv(str(csv_path), joint_names, csv_buffers[0])
print(f"Saved retargeted H2 motion to {csv_path}")

# Open the viewer and play back the CSV on the robot.
parser = newton.examples.create_parser()
parser.set_defaults(viewer="gl")
viewer, _ = newton.examples.init(parser)

viewer_app = Viewer(viewer, {
    "retarget_source_facing_direction": "Mujoco",
    "retarget_target": "unitree_h2",
})
viewer_app._reset_viewer_model()
viewer_app.load_csv_file(str(csv_path))
viewer_app.run()
```

---

[Documentation home](../README.md)

==== FILE documentation/robot-configuration-reference.md

# Robot configuration reference

A robot target is a description file plus a connected set of configuration JSON files. The manifest gives the target a registry name. The retargeter uses the scaler and post-processing files. Those files must all agree on source-joint names, robot body-link names, and robot coordinate layout.

Use [Add a robot with the configurator](robot-configurator.md) for a guided H1 example. 

Use this reference page when reviewing generated files, creating an override, or diagnosing configurations.

## Robot descriptions prerequisites

### supported formats

Robot configuration files can register robots from .urdf and mjcf .xml descriptions. If a robot is defined by a .xacro file, it needs to be converted to .urdf or mjcf .xml files prior to being registered in the Robot Configurator. S

Supported formats for robot meshes are STL or DAE

### Units

No units conversions are done when registering robots. The SOMA Retargeter assumes that all unites provided from the robot description are:
	- Lengths and positions: meters
	- Angles: radians
	- Mass: kilograms

### Robot transformations

Robot definitions are assumed to be oriented as:

- +Z up
- +X forward
- +Y left

No offset is applied to the robots in the SOMA Retargeter. Robots are assumed to be at origin and feet on the ground. 

### Memory management

High-DOF hands are not supported yet. Avoid registering robot descriptions that include  articulated fingers or dense hand mechanisms. The current retargeting workflow is designed for humanoid body motion, not high-DOF dexterous hands. Finger links can add many extra joints and may cause memory or solver issues. If a manufacturer description includes hands, prefer a simplified version that stops at the wrist or palm, or remove links beyond the hand before registering the robot.

## Bundled and user robot targets

SOMA Retargeter has two distinct robot-asset locations:

- `soma_retargeter/assets/robotics/` contains targets bundled with the Python package. The registry scans this location automatically.
- `assets/robotics/` is the repository-level location used by the Robot Configurator for user-created targets. The converter discovers the user robots as an `extra_robot_paths` in its configuration file .

Do not edit a bundled robot target merely to test a change. Prefer to copy the complete robot target directory to a user search root included in the `extra_robot_paths`. Keep or deliberately change its manifest name. An extra robot target with the same registry `name` overrides the bundled target for that process.

A conventional user robot target looks like:

```text
assets/robotics/
└── <vendor>/
    └── <robot-directory>/
        ├── manifest.json
        ├── desc/
        │   ├── <robot>.urdf
        │   └── meshes/
        └── configs/
            ├── <source>_to_<robot>_scaler_config.json
            ├── <source>_to_<robot>_retargeter_config.json
            └── <robot>_post_processing_config.json
```

The vendor and directory levels organize files; discovery is recursive and does not derive the target name from those folder names. `manifest.json` is authoritative for the registered robot name.

## Discovery and `extra_robot_paths`

The registry recursively scans each search root for files named `manifest.json`. It scans bundled assets first, then additional roots. A later target with the same name replaces the earlier registry entry.

The converter registers extra roots from its JSON config file (assets\default_bvh_to_csv_converter_config.json) : 

```json
{
    "extra_robot_paths": ["assets/robotics"]
}
```

`extra_robot_paths` may be a JSON array or a single string. Values are converted to absolute paths from the process's current working directory, so run documented commands from the repository root or use an explicit path. A missing root is skipped; it does not create the directory.

The interactive converter reads these paths at startup. Its **Reload** button rescans for registered roots. The Robot Configurator is different: it always scans the bundled root and repository-level `assets/robotics/`, and it writes new targets to `assets/robotics/`.

In Python, applications can register another root before creating a pipeline:

```python
from soma_retargeter.robotics.robot_registry import register_robots_path

register_robots_path("assets/robotics")
```

Use a new name to keep two robot target variants selectable. Reuse a bundled name only when you intend the extra target to override it.

## `manifest.json`

The simplest manifest declares one target:

```json
{
    "name": "unitree_h2",
    "desc": {
        "urdf_path": "desc/H2.urdf"
    },
    "retarget_configs": {
        "soma": "configs/soma_to_h2_retargeter_config.json"
    }
}
```

All local paths in a manifest are relative to the directory containing that manifest.

### Manifest fields

- `name` — required registry key used by `retarget_target`, the UI target selector, and `robot_type` in the scaler.
- `desc` — required object describing how Newton loads the robot.
- `desc.urdf_path` — path to a URDF. Use either this or `xml_path`.
- `desc.xml_path` — path to an MJCF XML. Use either this or `urdf_path`.
- `desc.urdf_offset` — optional precomputed Z lift for a URDF. Without it, the loader builds the URDF once, measures the lowest collision geometry, and rebuilds it at ground level.
- `desc.newton_asset` — optional Newton asset identifier. When present, description paths are resolved below Newton's downloaded asset directory rather than the manifest directory.
- `retarget_configs` — source-name-to-retargeter-path map. The current public source key is `soma`.

If neither `urdf_path` nor `xml_path` is present, model loading fails. If `retarget_configs.soma` is absent, the model can still appear as registered, but SOMA retargeting fails because no source-to-target configuration can be resolved.

A manifest may group targets:

```json
{
    "targets": [
        {
            "name": "robot_variant_a",
            "desc": {"xml_path": "desc/robot.xml"},
            "retarget_configs": {
                "soma": "configs/soma_to_variant_a_retargeter_config.json"
            }
        },
        {
            "name": "robot_variant_b",
            "desc": {"urdf_path": "desc/robot.urdf"},
            "retarget_configs": {
                "soma": "configs/soma_to_variant_b_retargeter_config.json"
            }
        }
    ]
}
```

Each entry becomes a separate registry target and shares the manifest directory as its path base.

## Description and meshes

The description defines the robot's:

- body-link and joint names;
- parent-child topology;
- joint types, axes, and limits;
- inertial, visual, and collision geometry;
- default joint pose.

Configuration files refer to **body-link names**, not URDF joint names. For example, `left_ankle_link` is a body, while `left_ankle_joint` is the revolute joint connecting it.

Keep a portable description:

```text
desc/
├── robot.urdf
└── meshes/
    ├── pelvis.STL
    └── ...
```

Use description-relative mesh references such as `meshes/pelvis.STL`. Avoid absolute paths and machine-specific package locations in a distributable target.

Convert Xacro files to URDF or MJCF prior to register.  Xacro registration requires the external `xacro` executable and expands the source to a URDF before copying meshes. `xacro` is not installed as a core project dependency.

When the configurator registers a URDF or MJCF, it:

1. copies the selected description into `desc/`;
2. finds `filename="..."` mesh references;
3. copies referenced STL, DAE and OBJ files into `desc/meshes/`;
4. rewrites successful references to `meshes/<filename>`.

For `package://<package>/...` references, the importer removes the package prefix and resolves the remaining path relative to the selected description's directory. Stage the description and mesh tree accordingly, as shown in the [H1 tutorial](robot-configurator.md). Treat every `Mesh not found` warning as a failed portability check.

## The scaler config

The scaler converts source-skeleton transforms into robot-aligned IK effector transforms. The retargeter points to it through `human_robot_scaler_config`.

Example shape:

```json
{
    "human_type": "soma",
    "human_root": "Hips",
    "robot_type": "unitree_h2",
    "robot_root": "pelvis",
    "human_scale_ratio": 1.0,
    "reference_joint_q": [],
    "human_joint_offsets": {
        "Hips": [
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ]
    }
}
```

The numeric values above illustrate structure only; they are not an H2 calibration.

General note on human joint offsets:

- If a joint doesn't have a link mapping, do not include it in `human_joint_offsets`.
### Scaler fields

- `human_type` — source label written by the configurator; currently `soma`.
- `human_root` — source-root label written by the configurator; normally `Hips`.
- `robot_type` — required target registry name. It must identify the same target selected by the manifest and converter.
- `robot_root` — mapped root body recorded by the configurator, normally the body selected for `Hips`.
- `human_scale_ratio` — required scalar applied to source translations. In normal converter use, the motion is proportionally scaled about the source root; root height is scaled as well.
- `reference_joint_q` — optional complete Newton joint-coordinate vector used to initialize the base IK solve. For a floating-base robot it begins with root translation `[x, y, z]` and quaternion `[x, y, z, w]`, followed by articulated coordinates in model order.
- `human_joint_offsets` — required map from SOMA joint name to `[translation, quaternion]`. Quaternions use `[x, y, z, w]` and are normalized when loaded.

The configurator's auto scale uses the current SOMA Hips height and the mapped robot-root height. It computes offsets from the current zero pose, current scale, and each mapped link. Therefore `human_scale_ratio`, `reference_joint_q`, and `human_joint_offsets` form one calibration set; changing one without recomputing or validating the others can make the target inconsistent.

Only source joints present in `human_joint_offsets` become scaler effectors. Their nearest mapped source ancestors form the scaled effector hierarchy. This is why leaving unsupported anatomy unmapped is valid, but accidentally omitting a required foot or root mapping affects later IK and post-processing.

## The retargeter config

The retargeter config is the central runtime configuration. It selects the scaler, defines IK correspondences and weights, controls initialization and solver behavior, and optionally selects post-processing.

Representative structure:

```json
{
    "num_initialization_frames": 10,
    "num_stabilization_frames": 5,
    "human_robot_scaler_config": "configs/soma_to_h2_scaler_config.json",
    "ik_iterations": 24,
    "joint_limit_weight": 10.0,
    "smooth_joint_filter_weight": 5.5,
    "enable_post_processing": true,
    "enable_contact_processing": true,
    "post_processing": {
        "robot_config": "configs/h2_post_processing_config.json"
    },
    "ik_match_table": {
        "Hips": {
            "t_body": "pelvis",
            "r_body": "pelvis",
            "t_weight": 30.0,
            "r_weight": 2.0
        }
    }
}
```

These are configurator defaults that demonstrate field placement, not optimized H2 values.

### Initialization and solver fields

- `num_initialization_frames` — number of source-zero-pose transition frames prepended before solving. Half transition the root; the remainder blend joint rotations.
- `num_stabilization_frames` — additional first-pose hold frames after initialization. Both groups are removed from exported output.
- `human_robot_scaler_config` — required path to the scaler, relative to the manifest directory.
- `ik_iterations` — base IK iterations per frame; values below 1 are clamped to 1.
- `joint_limit_weight` — global joint-limit objective weight; negative values are clamped to zero.
- `smooth_joint_filter_weight` — global weight for the smooth joint-limit avoidance objective; negative values are clamped to zero.

More iterations can improve convergence but increase processing cost. Higher objective weights do not guarantee better motion; evaluate tracking and joint-limit behavior together.

### `ik_match_table`

Each key is a mapped SOMA joint. Its object contains:

- `t_body` — robot body whose position follows the scaled source effector;
- `r_body` — robot body whose rotation follows it;
- `t_weight` — position objective weight;
- `r_weight` — rotation objective weight.

The configurator assigns the same selected link to `t_body` and `r_body`, but hand-edited configs may use different bodies. Every source name must exist in the SOMA skeleton and in the scaler's mapped effectors. Every target body must exactly match a body-link name in the loaded description. A typo fails during pipeline construction rather than being silently ignored.

Mappings and weights solve different problems:

- correct the link mapping, scale, zero pose, and offsets first;
- tune `t_weight` and `r_weight` only after the structural calibration works.

The [IK weight optimizer](ik-weight-optimizer.md) changes these two weights. It does not change the scaler or body-link choices.

General notes on `ik_match_table`:

- Always choose the root link of the robot for the hips joint. 
- If a joint doesn't have a link mapping, do not include it in the `ik_match_table`.

### Smooth joint-limit filter

`smooth_joint_filter_objective_body_masks` is optional:

```json
{
    "smooth_joint_filter_objective_body_masks": {
        "left_shoulder_pitch_link": [1.0, 1.0, 1.0]
    }
}
```

Each entry is `[mask, lower_offset, upper_offset]`:

| Value | Meaning | Units |
|---|---|---|
| `mask` | Scales the residual; `0` disables it. | Unitless |
| `lower_offset` | Moves the ramp start inward from the lower DOF limit. | Radians |
| `upper_offset` | Moves the ramp start inward from the upper DOF limit. | Radians |

The filter uses a smooth residual curve to discourage a joint from approaching either limit. For joint coordinate `q` and limits `L` and `U`:

```text
center      = (L + U) / 2
distance    = max((L + lower_offset) - q, 0, q - (U - upper_offset))
ramp        = smooth_exponential_ramp(distance)
residual    = (q - center) * ramp * smooth_joint_filter_weight * mask
```

The residual is zero between the two ramp starts. On either side, the ramp has an inverted Gaussian-like shape: it stays near zero at first, then rises smoothly and steeply toward `1`. `mask` and `smooth_joint_filter_weight` scale its strength without changing its shape.

`lower_offset` controls how far before the lower DOF limit the penalty begins, and `upper_offset` does the same for the upper DOF limit. Larger offsets start penalizing the DOF earlier. As the DOF approaches its limit, the objective gradually makes the pose more costly. When the kinematic chain has enough freedom, the IK solver can then distribute more of the motion across less-penalized joints while still trying to match the effector targets.

The arrows measure each offset from its DOF limit to its ramp start, while the shaded band marks the zero-residual region between the starts. The animation changes each offset, then moves the lower DOF limit from `-1` to `-2` to show that the offsets follow their corresponding limits.

![Effect of changing joint-limit offsets and DOF limits](images/smooth-joint-limit-moving-limits.gif)

Newton stores revolute DOF coordinates and limits in radians. Each offset is therefore a distance in radians measured inward from its corresponding limit. Unlisted bodies and entries with `mask = 0` are disabled. Start with `lower_offset` and `upper_offset` at `1 rad`, adjust where each ramp begins, then tune `mask` gradually. The **Smooth Filter** tab edits these values; body names must match the robot model.

### Post-Processing switches

- `enable_post_processing` — enables the limb-stabilizer pass. If true, `post_processing.robot_config` must resolve to a file containing `limb_stabilizer`.
- `enable_contact_processing` — enables contact detection and plant correction within post-processing. (see important note below)
- `post_processing.robot_config` — robot post-processing path relative to the manifest directory.

**Important note : Experimental feature**

Contact-guided foot stabilization is an **experimental** post-processing feature for motion retargeting. It reduces visible foot drift and abrupt motion when a source foot is detected as planted.

**To enable:** 

The feature runs only when both runtime settings are `true`:

```json
{
  "enable_post_processing": true,
  "enable_contact_processing": true
}
```

H2 configuration already sets both values to `true`.

**To disable:**

To reproduce the non-stabilized baseline, set both flags to `false`:

```json
{
  "enable_post_processing": false,
  "enable_contact_processing": false
}
```

Turning off only `enable_contact_processing` disables plant detection and correction but leaves the general limb stabilizer active.

**Limitations**

This is not a collision or scene-interaction feature. It does not guarantee that a foot will avoid penetration or floating, and it is not intended to solve stairs, uneven terrain, props, or handrails.

**Advanced tuning**

The source-contact thresholds and H2 post-processing settings are shared advanced defaults. Do not change them for a single motion. If you find a repeatable issue, compare the same input with the feature on and off, then report the source BVH, target configuration, output CSV/USD, and affected frame range to the retargeting team.

To learn more about configuring foot contacts, check the [Contact detection & foot-plant correction configuration](foot-contact.md) page.

## The post-processing config

The robot post-processing file supplies robot-specific foot correction and limb stabilization. 

Generated structure:

```json
{
    "contact_correction": {
        "transition_frames": 4,
        "propagation_ratio": 0.4,
        "rotation_propagation_ratio": 0.15,
        "enable_flatten_foot_plant": true,
        "sole_normal_local": [0.0, 0.0, 1.0]
    },
    "limb_stabilizer": {
        "ik_iterations": 20,
        "joint_limit_weight": 10.0,
        "effectors": {
            "pelvis": [30.0, 8.0],
            "left_hip_roll_link": [1.5, 0.15],
            "left_knee_link": [1.0, 1.0],
            "left_ankle_link": [10.0, 2.0]
        },
        "ik_root": 0,
        "root_correction_ratio": 1.0,
        "root_smooth_alpha": 0.8,
        "ik_limbs": {
            "LeftFoot": {
                "effectors": [1, 2, 3],
                "hint_reference": 2,
                "hint_offset": [0.25, 0.0, 0.0]
            }
        }
    }
}
```

Again, this shows dependencies, not validated H2 tuning.

### Contact-correction fields

- `transition_frames` — becomes the plant-correction blend transition length.
- `propagation_ratio` — positional correction propagated around a planted interval.
- `rotation_propagation_ratio` — rotational correction propagated around a planted interval.
- `enable_flatten_foot_plant` — allows planted-foot orientation flattening.
- `sole_normal_local` — sole-up direction, expressed in the **local frame of the foot**  (`LeftFoot`/`RightFoot` in the retargeter's `ik_match_table`). Used when flattening a planted foot.

### Limb-stabilizer fields

- `ik_iterations` — iterations for the stabilizer solve.
- `joint_limit_weight` — stabilizer joint-limit objective weight.
- `effectors` — ordered map from robot body to `[translation_weight, rotation_weight]`.
- `ik_root` — zero-based index into the ordered `effectors` map, normally the pelvis/root entry.
- `root_correction_ratio` — amount of computed vertical root correction.
- `root_smooth_alpha` — root-correction smoothing coefficient, clamped to `[0, 1]`.
- `ik_limbs` — source limb targets and their robot effector chains.
- `ik_limbs.<name>.effectors` — three indices into the ordered `effectors` map for the limb chain.
- `hint_reference` — index into `effectors` used to orient the two-bone IK hint *(the knee)*.
- `hint_offset` — local offset from that hint body *(in front of the knee)*.

The indices depend on JSON object insertion order. If you add, remove, or reorder `effectors`, update `ik_root`, every `effectors` index list, and every `hint_reference`. The configurator calculates these indices dynamically from its current Hips, leg, shin, and foot mappings; manual edits must preserve the same consistency.

For contact-aware feet, scaler offsets for `LeftFoot` and `RightFoot`, retargeter mappings for those source joints, and corresponding post-processing limb definitions must all exist and agree.

## Dependency chain

Runtime resolution follows this order:

```text
converter config
 ├─ extra_robot_paths ─► registry search roots
 ├─ retarget_source ───► manifest retarget_configs key
 └─ retarget_target ───► manifest name
                            ├ desc ─► URDF/MJCF ─► meshes
                            └ retargeter config
                                ├── human_robot_scaler_config ─► scaler
                                ├── ik_match_table ─► source joints + robot bodies
                                └── post_processing.robot_config ─► post-processing
```

All robot-local config references are resolved from the target's manifest directory, even when one config points to another.

## Validation checklist

Review a target in this order:

1. **Discovery:** the intended search root is listed, the manifest is found, and the target name appears once.
2. **Manifest:** one valid description path exists and `retarget_configs.soma` resolves.
3. **Description:** all mesh references are portable, geometry loads, joint limits are credible, and body-link names are stable.
4. **Scaler:** `robot_type` matches the manifest name; scale is measured; `reference_joint_q` has the exact coordinate count; offsets cover every intended source effector.
5. **Retargeter:** its scaler and post-processing paths exist; source names and target body names are exact; weights are finite and intentionally chosen.
6. **Post-processing:** effectors exist in the robot; all indices refer to the intended ordered entries; foot limbs agree with the scaler and retargeter.
7. **Converter:** `retarget_target` uses the manifest name and representative motions run in both interactive and headless modes.

## Common failures

- **Unknown target:** the extra search root was not registered, `name` differs from `retarget_target`, or the process needs a reload.
- **No retargeter config for source:** `retarget_configs` lacks the `soma` key or its path is wrong.
- **Description must specify** `urdf_path` **or** `xml_path`**:** `desc` is present but has no supported description key.
- **A body name is not in the model:** a retargeter, smooth mask, or post-processing entry uses a joint name instead of a body link, contains a typo, or belongs to another robot variant.
- **Reference joint shape mismatch:** `reference_joint_q` came from a different description or omitted the floating-root coordinates.
- **Post-processing is enabled but missing:** set a valid `post_processing.robot_config` with `limb_stabilizer`, or explicitly disable post-processing for diagnosis.
- **Foot correction affects the wrong bodies:** recheck ordered effector indices, foot mappings, and scaler offsets.
- **Bundled changes seem to have no effect:** an extra target with the same registry name is overriding it.
- **User override seems to have no effect:** another later extra search root defines the same target name.

## Tips to solve common issues

### Tune IK weights in config file

Many motion-quality issues can be reduced by tuning the IK weights directly in the `*_retargeter_config.json` file. Default weights may work well for one robot but produce unstable or exaggerated motion on another. Change one group of values at a time and review several representative animations before keeping the result. Best values are often a compromise between values validated on different animations. 

Each `ik_match_table` entry can contain translation and rotation weights:

- `t_weight` controls how strongly the solver matches the source position.
- `r_weight` controls how strongly it matches the source orientation.

Higher values give that objective more influence relative to the other IK objectives. Excessively high values can make the solve stiff or transfer problems elsewhere.

Common adjustments include:

- **Excessive torso rotation**: If the robot torso rotates more strongly than the source chest, increase `Chest.r_weight`. This makes the torso orientation follow the human chest more closely. Increase it in steps of `1.0` or `2.0`. `Chest.t_weight` can also help when the chest position drifts, but it does not directly correct orientation.
- **Incorrect arm angles or popping**: An arm can flip or take an undesirable direction while reaching its end effector. Increase `LeftArm.r_weight` and `RightArm.r_weight` to preserve more of the source upper-arm orientation. Use small increments such as `0.1` or `0.5`, then review several animations. Values that are too high can restrict the solve and make the overall result worse.
- **Pelvis popping**: Fast pelvis motion, jumps, and strong hips movement during walking can cause the pelvis to pop when its objective is too weak relative to the other effectors. Increase `Hips.t_weight` in steps of approximately `10.0` and `Hips.r_weight` in steps of approximately `2.0`. This gives the pelvis position and orientation more influence during the solve.

These adjustments only help when the robot diverges from the source objective. They do not remove motion that already exists in the human animation.

### Unmapped joints

Source joints such as `Head`, `LeftToeBase`, and `RightToeBase` may not correspond to dedicated robot links. Approximately placing these landmarks relative to the robot can still improve the solve.

A toe-base landmark provides a directional reference beyond the foot, which can improve foot and ankle orientation. A head landmark can similarly provide a reference above the torso and help orient the upper body. These landmarks do not create new robot links; they only provide additional spatial references for the mapped IK hierarchy.

Place them approximately where the corresponding anatomical feature would be on the robot. Exact placement is less important than maintaining a sensible direction and distance from the nearest mapped body.

### Redistribute shoulder motion near joint limits

If a shoulder coordinate approaches its limit and absorbs too much of the required rotation, increase the first value, `mask`, in that link's `smooth_joint_filter_objective_body_masks` entry. This makes the solver favor other coordinates while the configured ramp is active.

If avoidance begins too late, increase `lower_offset` or `upper_offset` on the affected side. These values are distances in radians measured inward from the corresponding limit.

Increase `mask` gradually, typically in steps of `0.1`, and review the result across multiple animations. Values that are too high can reduce reach or move the problem to another joint. Changes have no effect while the coordinate remains entirely inside the zero-contribution region.

## Where to go next

Use [Interactive retargeting](interactive-retargeting.md) to validate one motion visually. Once the topology and scaler are correct, use [IK weight optimizer](ik-weight-optimizer.md) and [Compare and tune](compare-and-tune.md) to evaluate weight changes without overwriting the baseline.

[← Previous: Add a robot with the configurator](robot-configurator.md) · [Documentation home](../README.md) · [Next: Interactive retargeting →](interactive-retargeting.md)
==== FILE documentation/ik-weight-optimizer.md

# IK weight optimizer

**Important note: Experimental feature**

The IK weight optimizer is an experimental calibration tool. It writes a new retargeter configuration with candidate IK weights based on kinematic tracking and smoothness metrics; compare the result visually with the baseline before adoption.

The IK weight optimizer tunes how strongly a robot retargeter tries to match each source effector. Use it after the standard retargeter works but consistently favors the wrong body parts—for example, good hands but poor feet, or good root tracking but weak limb tracking.

The optimizer is a corpus-level calibration tool, not a single-motion converter. It repeatedly retargets a set of BVH motions, measures solved robot poses against the scaler targets, proposes new IK weights, and accepts only updates that satisfy its objective and clip policy.

## The three inputs

A useful optimization run depends on three groups of repository content:

1. **Motions:** `assets/motions/optimizer/` is the representative BVH corpus. It should contain varied motions that exercise locomotion, turns, reaches, impacts, and full-body movement. Or, if you need to train a robot for specific motions, you can optimize for another set of representative motions.
2. **Robot assets:** the selected target’s discovered manifest, model description, scaler config, and base retargeter config. For the H1 tutorial these are under `assets/robotics/unitree/unitree_h1/`.
3. **Optimizer:** `app/tools/ik_weight_optimizer.py` and its JSON run config at `app/tools/assets/ik_optimizer/ik_weight_optimizer_config.json`.

The bundled optimizer config has:

```json
"input_folder": ""
```

The optimizer validates this field as a non-empty string, so the default config **cannot run unchanged**. The 15 motions under `assets/motions/optimizer/` are a useful first corpus for general H1 movement; replace or extend them later with motions representative of the robot's intended use.

## What changes and what stays fixed

The optimizer changes only:

- `t_weight` values in the target retargeter’s `ik_match_table`.
- `r_weight` values in the same table.

The final values are the base weights multiplied by learned per-effector scales and rounded to three decimal places. By default, matching `Left*` and `Right*` effectors are constrained to remain symmetric.

The optimizer does **not** change:

- The robot model or kinematic structure.
- The human-to-robot scaler config or its correspondence offsets.
- Joint limits.
- The source BVH files.
- The base retargeter file in the bundled robot assets.
- Post-processing settings in the deployable output.

`retargeter_overrides` can temporarily disable processing stages while candidates are evaluated. Those evaluation-only overrides are not written into the final deployable retargeter config. For best results in the optimisation process, it is recommended to set the overrides to false.

## Create a run config

Do not edit the tracked default for an experiment. Create `local-configs/` with
your file manager or editor if needed, then create
`local-configs/ik_weight_optimizer_config.json`:

```json
{
    "target_type": "unitree_h1",
    "input_folder": "../assets/motions/optimizer",
    "output_folder": "../output/ik-optimizer",
    "extra_robot_paths": ["../assets/robotics"],
    "outer_iterations": 50,
    "ik_weight_update": {
        "learning_rate": 0.075,
        "max_scale": 4.0,
        "protect_root_position": true,
        "protect_root_rotation": false,
        "root_rotation_min_scale": 0.7,
        "hard_clip_emphasis": 1.0
    },
    "clip_guard": {
        "mode": "auto",
        "penalty_balance": 1.0,
        "penalty_tail_weight": 0.5,
        "max_clip_frame_loss_p95_regression": 0.15,
        "max_aligned_frame_loss_p95_regression": 0.30,
        "catastrophic_accel_spike_regression": 1.5
    },
    "objective": {
        "smoothness_balance": 0.08
    },
    "plot": {
        "enabled": true,
        "live": false
    },
    "effector_priorities": {
        "position_weights": {
            "Hips": 5.0,
            "Chest": 1.2,
            "LeftFoot": 3.0,
            "RightFoot": 3.0
        },
        "rotation_weights": {
            "Hips": 1.2,
            "Chest": 1.0
        }
    },
    "retargeter_overrides": {
        "enable_post_processing": false,
        "enable_contact_processing": false,
        "enable_post_smoothing": false
    }
}
```

Optimizer paths are resolved relative to the optimizer config’s directory. In this example:

- `../assets/motions/optimizer` resolves to the bundled corpus.
- `../output/ik-optimizer` keeps generated artifacts separate from source assets.
- `../assets/robotics` lets the optimizer discover the H1 target created by the Robot Configurator.

For a smoke test, set `outer_iterations` to `2`. Restore the planned iteration count for a real calibration run.

## Run optimization

There are 2 ways to run the optimization process. One with no graphic reports and one with graphic reports. In both cases, a set of report output files are generated as diagnostic files. 

If you only want to optimize IK weights and write the JSON/CSV diagnostics only, run the following:  

```bash
uv run python app/tools/ik_weight_optimizer.py --config local-configs/ik_weight_optimizer_config.json
```

For a strictly no-graph run, set the run config's plot block to:

```json
"plot": {
    "enabled": false,
    "live": false
}
```

With plotting disabled, the optimizer still writes the optimized retargeter config, `optimizer_metrics.json`, and the motion improvement ranking. It skips the dashboard PNG and the flattened iteration-metrics CSV.

Expected startup messages report:

- The number of BVH motions found recursively.
- Skeleton loading.
- Whether target symmetry is enabled.
- The initial tracking, smoothness, frame-loss, position, rotation, and reachability metrics.

Each iteration then reports `ACCEPT`, `REJECT - PROBE`, or `HOLD`:

- **ACCEPT** means a candidate improved the objective and passed the active clip policy.
- **REJECT - PROBE** means the line search will try a smaller update.
- **HOLD** means every probe was rejected and the current accepted weights were retained.

An early `CONVERGED` message is normal when repeated probes cannot improve the accepted state. In `auto` clip-guard mode, the optimizer can first transition from strict `gate` behavior to softer `penalty` behavior.

### Generate the dashboard graph

Graphs are useful once the basic command runs successfully. The dashboard makes it much easier to see whether the optimizer is improving steadily, getting stuck, or trading one kind of accuracy for another.

![Example IK optimizer dashboard](images/ik-optimizer-dashboard-example.png)

The dashboard shows:

- optimization loss, tracking loss, and smoothness penalty;
- IK weight update size per accepted iteration;
- position error in meters;
- rotation error in radians;
- motion smoothness and acceleration signals;
- mean, p95, and worst-frame tracking loss.

To generate the dashboard during a run, keep plotting enabled in the config:

```json
"plot": {
    "enabled": true,
    "live": false
}
```

Then run with Matplotlib available only for this command:

```bash
uv run --with matplotlib python app/tools/ik_weight_optimizer.py --config local-configs/ik_weight_optimizer_config.json
```

`--with matplotlib` does not modify the project dependency files. It only makes Matplotlib available to this `uv run` invocation. The optimizer writes `optimizer_dashboard.png` beside the optimizer metrics when plotting succeeds.

Keep `"live": false` for most runs. Set `"live": true` only when you want the dashboard image refreshed during optimization; that adds repeated plot rendering and file-writing overhead.

## Expected output files

For `target_type: "unitree_h1"` and the config above, outputs are written under:

```text
output/ik-optimizer/optimized_unitree_h1/
```

The directory contains:

- `optimized_soma_to_unitree_h1_retargeter_config.json` — deployable retargeter config with optimized IK weights.
- `optimizer_metrics.json` — complete run metadata, accepted history, per-motion metrics, final scales, and artifact paths.
- `optimizer_improvement_ranking.csv` — each corpus motion ranked by baseline-to-final tracking-loss change.
- `optimizer_iteration_metrics.csv` — flat per-iteration metrics, when plotting is enabled.
- `optimizer_dashboard.png` — six-panel dashboard, when plotting is enabled and Matplotlib is available.
- `optimizer_probe_diagnostics.csv` — optional probe-level accept/reject details, only when `"save_probe_diagnostics": true`.

The optimizer does not produce retargeted motion CSV files. Use the optimized config in a custom robot override, then run the converter as described in [Compare and tune](compare-and-tune.md).

Alternatively, you can copy the `optimized_soma_to_unitree_h1_retargeter_config.json` optimized config file into the robot's `configs` folder and update the `manifest.json` file of the robot to point to the `optimized_soma_to_unitree_h1_retargeter_config.json` retargeter file. Reloading robots in the converter will use the updated manifest and retarget with the optimized config file. 

## Read the results

Start with these checks:

1. In `optimizer_dashboard.png`, confirm tracking loss trends downward rather than improving once and then flattening through repeated holds.
2. Check position and rotation error separately; a lower combined objective can still trade one against the other.
3. Check smoothness and worst-frame signals for spikes.
4. Open `optimizer_improvement_ranking.csv`. Review both the best improvements and every row marked `regressed`.
5. Inspect the optimized config’s `ik_match_table`; confirm weights remain plausible and symmetric where expected.
6. Validate representative motions visually before adopting the config.

Lower loss is evidence, not proof that the motion is better for control or deployment.

## Render a dashboard later

If the run completed without Matplotlib, the JSON and CSV diagnostics still remain. Render from the full-precision JSON:

```bash
uv run --with matplotlib python app/tools/ik_weight_optimizer.py --plot output/ik-optimizer/optimized_unitree_h1/optimizer_metrics.json
```

Or choose the output PNG explicitly:

```bash
uv run --with matplotlib python app/tools/ik_weight_optimizer.py --plot output/ik-optimizer/optimized_unitree_h1/optimizer_metrics.json output/ik-optimizer/optimized_unitree_h1/review-dashboard.png
```



## IK Optimizer Best Practices

The motions in `assets/motions/optimizer/` are a good place to start because they exercise a range of full-body behaviors. They are not guaranteed to be the best corpus for every robot. Each robot has a different body shape, DOF layout, joint range, end-effector placement, and intended task. A motion set that is useful for one humanoid can be too easy, too difficult, or simply not representative for another.

Good optimizer inputs should be close to what the robot is expected to do. For a robot that needs stable walking and turning, choose motions with gait changes, direction changes, and foot plants. For a robot that needs manipulation, include motions with reaches, arm coordination, and torso motion. Avoid optimizing around motions the robot cannot realistically perform, because the optimizer may learn weights that chase impossible targets and make ordinary motions worse.

After you understand the basic optimizer workflow, use motion selection as a second-stage refinement step. If the bundled corpus does not improve results for your robot, test the motions one at a time before running another large optimization:

1. Create a temporary input folder with one BVH from `assets/motions/optimizer/`.
2. Run a short optimization for that single motion.
3. Review `optimizer_dashboard.png` and `optimizer_improvement_ranking.csv`.
4. Visually compare the baseline and optimized retargeting in the converter.
5. Repeat with the next motion and keep notes about which motions improve, stay neutral, or regress.

This exercise helps you build a better robot-specific corpus. Keep motions that produce meaningful improvements, remove motions that consistently regress or force unnatural poses, and then run one combined optimization on the curated set. The goal is not to find one perfect motion. The goal is to collect a small set of representative motions that pull the weights in a useful direction for the robot's real use case.

You can use the same approach with your own SOMA-compatible BVH motions. Prepare or source motions that match the robot's intended tasks, test them individually, then combine the strongest examples into a single optimization run. If you need a broader library of SOMA-ready motions, the [BONES-SEED dataset](https://huggingface.co/datasets/bones-studio/seed) provides a large collection of annotated humanoid motions in SOMA formats. The dataset page may require accepting its access terms before downloading files. The [SEED interactive viewer](https://seed-viewer.bones.studio/) is useful when you want to browse motions visually before choosing candidates.

Treat IK optimization as an iterative calibration process. Run an experiment, inspect the metrics, watch the robot, adjust the corpus, and rerun with a clean output folder. Lower loss is useful evidence, but the final decision should always include visual validation on meaningful motions for the robot.

## Recover from a failed run

- Keep the failed output directory until you have read the last console error.
- Fix the personal run config or corpus; do not patch the bundled robot config to make the run continue.
- Use a new `output_folder` for materially different experiments so results are not confused.
- If GPU memory is exhausted, lower `motion_batch_size` and `fk_frame_batch_size` in the run config.
- If one malformed motion stops loading, move it out of the corpus, record why, and rerun the complete corpus. The optimizer does not skip failed clips.
- If every iteration holds, inspect guard messages and probe diagnostics before relaxing thresholds. A hold can be correctly preventing regression.



## Where to go next

Keep the generated optimizer directory unchanged as evidence, then use [Compare and tune](compare-and-tune.md) to install the candidate in a non-destructive robot override and compare it with the baseline on identical motions.

[← Previous: Interactive retargeting](interactive-retargeting.md) · [Documentation home](../README.md) · [Next: Compare and tune →](compare-and-tune.md)

==== FILE documentation/foot-contact.md

# Contact detection & foot-plant correction configuration

All configs under `soma_retargeter/assets/`.

There are two sides to the config:
 - Human (source) side : configures the contact detection and foot-plant acceptance gates
 - Robot side : configures the foot-plant correction


## Human side

`assets/<source>/contact_processing/*_contact_config.json` 

For SOMA : `soma_retargeter/assets/soma/contact_processing/soma_contact_config.json` 

One file per source, used by all robots. Resolved by source type, so a change here affects every robot.

**Contact detection** — finds coarse contact segments from foot speed and jerk.

| Param | Default | |
|---|---|---|
| `joint_names` | `LeftFoot, LeftToeBase, RightFoot, RightToeBase` | contact joints |
| `foot_channel_map` | `{0:0, 2:1}` | index into `joint_names` → foot index (LeftFoot=0→left, RightFoot=2→right) |
| `velocity_contact` | 0.1 m/s | speed below this → contact starts |
| `jerk_contact` | -0.05 m/s³ | jerk below this opens the contact window |
| `velocity_uncontact` | 0.2 m/s | speed above this for 2 frames → contact ends |
| `velocity_probably_lift_off` | 0.05 m/s | speed above this marks the candidate lift-off frame contact is rolled back to |
| `post_contact_jerk_window` | 5 frames | how long a jerk trigger stays open |
| `transition_frames` | 4 frames | ramp added on each side of a contact region |
| `edge_propagation_frames` | 8 frames | max extension of a contact at clip start/end |

**Plant acceptance gates** — `plant_subsegment.*`, promotes a contact segment to a
correctable flat plant. All are code defaults; only present keys override.

| Param | Default | |
|---|---|---|
| `max_flatness_deg` | 25° | max sole-normal tilt from world up |
| `plant_speed_threshold` | 0.15 m/s | max foot speed; also normalizes the speed score |
| `max_height_spread` | 0.05 m | max heel-to-toe height difference |
| `max_position_delta` | 0.01 m | max per-frame foot-centre movement |
| `min_plant_frames` | 3 frames | shorter runs are dropped |
| `max_gap_frames` | 2 frames | bridges noise gaps inside a plant run |
| `min_acceptance_confidence` | 0.5 | reject the run below this confidence |
| `ground_height_tolerance` | 0.03 m | foot centre within this of z=0 counts as on the ground |
| `ground_confidence_boost` | 1.15 | confidence multiplier when on the ground |
| `elevated_confidence_scale` | 1.0 | confidence multiplier when off the ground |

Confidence is the mean per-frame `flatness_score × speed_score` over the run, then scaled by
whichever of the two multipliers applies, capped at 1.0.

**Landmarks**

| Param | Default | |
|---|---|---|
| `foot_landmarks` | — | per-side foot geometry in the **source skeleton's** joint frames, see *Foot landmarks* below |


## Robot side

`assets/robotics/<vendor>/<robot>/configs/`

**1. Enable — `*_retargeter_config.json`**
- `enable_post_processing`
- `enable_contact_processing`
- `post_processing.robot_config` → path to the post-processing config below

**2. Tune — `*_post_processing_config.json`, key `contact_correction`**

| Param | Default | |
|---|---|---|
| `transition_frames` | 4 frames | blend length |
| `propagation_ratio` | 0.4 | fraction (0–1) of adjacent swing taking position correction |
| `rotation_propagation_ratio` | 0.15 | fraction (0–1) of adjacent swing taking rotation correction |
| `enable_flatten_foot_plant` | true | **not an on/off switch** — `true` flattens the sole to horizontal and may shift heading (yaw); `false` still flattens, but preserves the original heading |
| `sole_normal_local` | *(unset)* | sole-up direction in the **robot foot effector link's** frame; defaults to `+Z` |

Flattening only fires when plant tilt exceeds 5° and subsegment confidence is >= 0.5.


## Configuring foot plant correction for a new robot

Contact detection runs entirely on the human skeleton, so the robot supplies no foot
geometry — no heel, no toe, no tip.

1. Set the two enable flags and `post_processing.robot_config` in `*_retargeter_config.json`.
2. Tweak the `contact_correction` parameters in `*_post_processing_config.json` as needed.
3. Set `sole_normal_local` only if the foot effector link's local `+Z` is not sole-up at the
   zero pose.


## Source foot landmarks

The `foot_landmarks` block of `*_contact_config.json`, under `rigs.<source>.left` / `.right`.
Four joint names plus three vectors per side:

```jsonc
{
  // Names in the source skeleton, define the frame for the vectors below
  "foot_joint": "LeftFoot",         // ankle joint. Frame for heel_local_in_foot
  "toe_joint": "LeftToeBase",       // toe base joint. Frame for toe_pivot_local_in_toe
  "toe_end_joint": "LeftToeEnd",    // optional, may be null. Only used by the heuristic
                                    // fallback to find the foot's forward axis; ignored
                                    // when the vectors below are authored
  "sole_normal_space": "foot",      // "foot" or "toe" — local frame for the sole_normal_local
                                    // Default "foot"

  // Relative to the joint named in the key, in metres
  "heel_local_in_foot":     [x, y, z],  // heel contact point, offset from foot_joint's origin
  "toe_pivot_local_in_toe": [x, y, z],  // toe/ball contact point, offset from toe_joint's origin
  "sole_normal_local":      [x, y, z]   // unit DIRECTION, points UP out of the sole
}
```

However, registering a **new source type** is a code change, not a config change: `SourceType` is an
enum, and the contact-config path, zero-pose asset and model mesh are each resolved by a
switch on it. The skeleton key must also be added to the heuristic-config table.
