---
source_url: https://bitrobot-foundation.github.io/humanoids-in-the-wild-500-hours/
collected: 2026-09-11
published: 2026-06
author: BitRobot, Unitree, Hugging Face
companion_urls:
  - https://huggingface.co/datasets/BitRobot/HIW-500 (raw ROS bag / MCAP; card below)
  - https://huggingface.co/datasets/BitRobot/HIW-500-LeRobot (LeRobot v3.0; meta/info.json summarized below)
  - https://huggingface.co/datasets/BitRobot/2026-humanoid-ikea-assembly-challenge (hardware references)
license: CC BY 4.0
note: Page counters are JS-animated (render as "0+" when stripped); the per-task table and subtask treemap below are read from the page's embedded chart data. data-count attributes on the page: 500 (hours), 23 (K episodes), 10 (TB), 10 (tasks), 12 (homes).
---

# HIW-500 project page (tag-stripped)

HIW-500: Humanoids In-the-Wild Dataset
HIW-500: Humanoids In-the-Wild Dataset
Overview
Dataset
Citation
        Your browser does not support the video tag.
HIW-500 
Humanoids In-the-Wild Dataset
            An in-the-wild dataset
            for whole-body humanoid robot learning.
II
Contributors
Overview
Built for learning from real homes, not lab-only scenes.
            HIW-500: Humanoids In-the-Wild Dataset focuses on task execution in natural environments where layout,
            object state, lighting, clutter, and human operating style vary from episode to episode.
            The dataset is collected in real homes in Southeast Asia through 
human whole-body teleoperation
 of 
Unitree G1
,
            providing demonstrations for mobile manipulation, bimanual interaction, and long-horizon household skills.
0+
Hours
0+
Episodes
0
Data
0+
Tasks
0
Homes
Hardware
Acquisition setup
            The hardware stack uses grippers for household manipulation, with a head camera
            and wrist-mounted cameras for visual observations.
01
Gripper manipulation
End-effector grippers are used for household grasping, placing, and object interaction.
02
Head camera
Head-mounted camera provides a wider scene view for task context and navigation.
03
Hand stereo IR cameras
Wrist-mounted stereo IR cameras capture close-range observations around the robot hands.
Dataset
What data is collected?
            Each episode records human whole-body teleoperation of Unitree G1 in real homes,
            combining camera streams, robot states, action traces, and language annotations.
Head camera
RGB
Stereo
480P
30 FPS
Wrist camera
RGB
IR
Stereo
480P
30 FPS
State and actions
29-DoF Joints
End-Effector
IMU
Odometry
Metadata
Language annotation
Episode info
Camera intrinsics & extrinsics
Live demo
              Open the Rerun preview in a new tab
Dataset Statistics
Task Coverage
Building children table
Hang hanger
Clean up the room
Setting the table
Restocking fridge
Kitchen organization
Hang keys on a hook
Move pillow to sofa
Sweep floor
Picking trash
Clothes washing
Task Episodes
Average Duration
Subtask Labels
161
Total subtask labels
148k+
Subtask annotation
Top 40
Shown in treemap
                  Every robot subtask is annotated with a fine-grained action label. Hover tiles for details.
Roadmap
Open Source timeline
June 2026
Release V1: 500+ hours of data
V2
Release more tasks and environments
LeRobot Integration
            We host the dataset on Hugging Face in two formats: raw ROS bag / MCAP recordings and
            a version in LeRobot format for robot learning workflows.
              View raw dataset
              View dataset in LeRobot format
Citation
@misc{hiw500_2026,
  title={HIW-500: Humanoids In-the-Wild Dataset for Robot Learning},
  author={BitRobot and Unitree and Hugging Face},
  year={2026},
  howpublished={\url{https://bitrobot-foundation.github.io/humanoids-in-the-wild-500-hours/}}
}
License
            The public HIW-500 dataset is released under the 
CC BY 4.0
 license.
Commercial Licensing for Additional Humanoid Data
            Access our growing in-the-wild humanoid dataset or request custom data collection
Request Data Access
© 2026 HIW-500: Humanoids In-the-Wild Dataset
contact@bitrobot.ai

## Per-task statistics (embedded chart data)

| Task | Episodes | Hours | Avg s |
|---|---:|---:|---:|
| Building children table | 760 | 110.0 | 520.9 |
| Hang hanger | 1481 | 68.8 | 167.2 |
| Clean up the room | 1454 | 62.9 | 155.8 |
| Setting the table | 5526 | 46.6 | 30.4 |
| Restocking fridge | 1879 | 42.6 | 81.6 |
| Kitchen organization | 1586 | 42.2 | 95.8 |
| Hang keys on a hook | 2381 | 30.3 | 45.8 |
| Move pillow to sofa | 1995 | 24.8 | 44.7 |
| Sweep floor | 1877 | 20.6 | 39.5 |
| Picking trash | 1805 | 19.3 | 38.5 |
| Clothes washing | 2423 | 17.2 | 25.6 |

## Subtask treemap, top 25 labels by annotation count

- move to table: 51257
- move to bed: 24374
- dump trash: 19650
- move to trash can: 16143
- pick trash: 14412
- move to sink: 12865
- move to fridge: 12078
- move to countertop: 11536
- pick bowl: 9094
- pick plate: 8703
- pick fork: 7766
- pick spoon: 7697
- move to clothing rack: 7155
- move to chair: 6232
- place clothes to washer: 6097
- pick keychain: 5743
- sweep trash: 5650
- move to hook: 5481
- rotate leg to tighten: 5435
- hang keychain to hook: 5427
- open fridge: 5350
- close fridge: 5350
- pick chopsticks: 5346
- pick clothes from laundry basket: 5298
- place chopsticks to sink: 5024

---

# Hugging Face dataset card — BitRobot/HIW-500

---
pretty_name: 'HIW-500: Humanoids In-the-Wild Dataset'
language:
- en
tags:
- robotics
- humanoid
license: cc-by-4.0
---

# HIW-500: Humanoids In-the-Wild Dataset

https://bitrobot-foundation.github.io/humanoids-in-the-wild-500-hours/

HIW-500: Humanoids In-the-Wild Dataset is a large-scale dataset for whole-body humanoid robot learning in natural home environments. It captures human teleoperation demonstrations on Unitree G1 across real homes in Southeast Asia, where layouts, object states, lighting, clutter, and operator styles vary from episode to episode.

The dataset is designed for research on mobile manipulation, bimanual interaction, long-horizon household skills, imitation learning, and general-purpose robot learning from in-the-wild demonstrations.

## Dataset Overview

- 500+ hours of humanoid robot demonstrations
- 23K+ episodes
- Around 10 TB of data
- 10+ household tasks
- 12 real homes
- 161 subtask labels
- 148K+ subtask annotations

## Data Modalities

Each episode records human whole-body teleoperation of Unitree G1 in real homes. The dataset combines synchronized visual observations, robot states, actions, and metadata.

### Camera Streams

- Head camera: RGB stereo, 480p, 30 FPS
- Wrist camera: RGB, stereo IR, 480p, 30 FPS

### Robot State and Actions

- 29-DoF joint states
- End-effector state
- IMU
- Odometry
- Action traces from human whole-body teleoperation

### Metadata

- Language annotations
- Episode information
- Camera intrinsics and extrinsics

## Dataset Statistics

![Task duration](assets/readme/task_duration_share.png)

![Task episodes](assets/readme/task_episodes.png)

![Average duration](assets/readme/average_duration.png)

## Dataset Access

The dataset is hosted on Hugging Face in two formats:

- Raw ROS bag / MCAP recordings: https://huggingface.co/datasets/BitRobot/HIW-500
- LeRobot format: https://huggingface.co/datasets/BitRobot/HIW-500-LeRobot

_For raw data from the Building Children Table task, see our challenge dataset: https://huggingface.co/datasets/BitRobot/2026-humanoid-ikea-assembly-challenge_

## License

The public HIW-500 dataset is released under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/). If you're interested in additional datasets similar to HIW-500, be it for commercial or academic purposes, pls [contact us](mailto:contact@bitrobot.ai?subject=Dataset%20Inquiry).

## Citation

If you use this dataset, please cite:

```bibtex
@misc{hiw500_2026,
  title={HIW-500: Humanoids In-the-Wild Dataset for Robot Learning},
  author={BitRobot and Unitree and Hugging Face},
  year={2026},
  howpublished={\url{https://bitrobot-foundation.github.io/humanoids-in-the-wild-500-hours/}}
}
```

---

# LeRobot version — meta/info.json (summary)

codebase_version v3.0, robot_type unitree_g1, fps 30, total_episodes 23743, total_frames 40839947, total_tasks 11

{
 "observation.images.head": [
  "video",
  [
   480,
   1280,
   3
  ],
  [
   "height",
   "width",
   "channels"
  ]
 ],
 "observation.images.left_wrist": [
  "video",
  [
   480,
   640,
   3
  ],
  [
   "height",
   "width",
   "channels"
  ]
 ],
 "observation.images.right_wrist": [
  "video",
  [
   480,
   640,
   3
  ],
  [
   "height",
   "width",
   "channels"
  ]
 ],
 "observation.state": [
  "float32",
  [
   29
  ],
  [
   "kLeftHipPitch.q",
   "kLeftHipRoll.q",
   "kLeftHipYaw.q",
   "kLeftKnee.q",
   "kLeftAnklePitch.q",
   "kLeftAnkleRoll.q",
   "kRightHipPitch.q",
   "kRightHipRoll.q",
   "kRightHipYaw.q",
   "kRightKnee.q",
   "kRightAnklePitch.q",
   "kRightAnkleRoll.q",
   "kWaistYaw.q",
   "kWaistRoll.q",
   "kWaistPitch.q",
   "kLeftShoulderPitch.q",
   "kLeftShoulderRoll.q",
   "kLeftShoulderYaw.q",
   "kLeftElbow.q",
   "kLeftWristRoll.q",
   "kLeftWristPitch.q",
   "kLeftWristyaw.q",
   "kRightShoulderPitch.q",
   "kRightShoulderRoll.q",
   "kRightShoulderYaw.q",
   "kRightElbow.q",
   "kRightWristRoll.q",
   "kRightWristPitch.q",
   "kRightWristYaw.q"
  ]
 ],
 "observation.state.wbc": [
  "float32",
  [
   23
  ],
  [
   "pivot_vx",
   "pivot_vy",
   "pivot_vyaw",
   "pivot_roll",
   "pivot_pitch",
   "pivot_yaw",
   "pivot_height",
   "left_ee_x",
   "left_ee_y",
   "left_ee_z",
   "left_ee_roll",
   "left_ee_pitch",
   "left_ee_yaw",
   "right_ee_x",
   "right_ee_y",
   "right_ee_z",
   "right_ee_roll",
   "right_ee_pitch",
   "right_ee_yaw",
   "left_trigger",
   "left_squeeze",
   "right_trigger",
   "right_squeeze"
  ]
 ],
 "action": [
  "float32",
  [
   23
  ],
  [
   "pivot_vx",
   "pivot_vy",
   "pivot_vyaw",
   "pivot_roll",
   "pivot_pitch",
   "pivot_yaw",
   "pivot_height",
   "left_ee_x",
   "left_ee_y",
   "left_ee_z",
   "left_ee_roll",
   "left_ee_pitch",
   "left_ee_yaw",
   "right_ee_x",
   "right_ee_y",
   "right_ee_z",
   "right_ee_roll",
   "right_ee_pitch",
   "right_ee_yaw",
   "left_trigger",
   "left_squeeze",
   "right_trigger",
   "right_squeeze"
  ]
 ],
 "timestamp": [
  "float32",
  [
   1
  ],
  null
 ],
 "frame_index": [
  "int64",
  [
   1
  ],
  null
 ],
 "episode_index": [
  "int64",
  [
   1
  ],
  null
 ],
 "index": [
  "int64",
  [
   1
  ],
  null
 ],
 "task_index": [
  "int64",
  [
   1
  ],
  null
 ],
 "language_persistent": [
  "language",
  [
   1
  ],
  null
 ],
 "language_events": [
  "language",
  [
   1
  ],
  null
 ]
}

---

# Hugging Face dataset card — BitRobot/2026-humanoid-ikea-assembly-challenge (hardware references)

---
license: cc-by-4.0
task_categories:
- robotics
language:
- en
tags:
- humanoid
- robotics
pretty_name: 2026 Humanoid IKEA Assembly Challenge
size_categories:
- n<1K
viewer: false
---

# 2026-humanoid-ikea-assembly-challenge
https://humanoid-ikea-assembly-challenge.github.io/

## Hardware References
- [Unitree Dex1-1](https://www.unitree.com/Dex1-1)
- [Head Stereo Camera (HBVCAM-4M2214HD-2 V11)](https://github.com/unitreerobotics/xr_teleoperate/blob/main/Device.md#522-stereo-camera-30-fps)
- [Wrist Stereo Camera (RealSense-D405)](https://github.com/unitreerobotics/xr_teleoperate/blob/main/Device.md#523-g1-wrist-realsense-d405)

## Data Format
This repository contains the raw dataset in ROS bag / MCAP format.
The data can be viewed using tools such as Foxglove Studio and Rerun.

Available data streams include:
- Head stereo camera streams (RGB)
- Wrist stereo camera streams (RGB and IR)
- Joint states and actions
- End-effector
- IMU
- Annotations

For the LeRobot-format version of the dataset, please refer to [G1_WBT_Dex1_Building-Children-Table](https://huggingface.co/datasets/BitRobot/G1_WBT_Dex1_Building-Children-Table) .
