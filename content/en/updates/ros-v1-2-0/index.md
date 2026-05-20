---
title: "OpenMower ROS v1.2.0"
date: 2026-05-13
author: "Clemens Elflein"
description: "Area-level setting overrides, extended battery reporting, improved emergency handling for v2 hardware, obstacle ordering fix, and simulator improvements."
---

[v1.2.0](https://github.com/ClemensElflein/open_mower_ros/releases/tag/v1.2.0) brings per-area configuration overrides, a batch of v2 hardware improvements, and a handful of reliability fixes.

### Area Overrides for Various Settings

The move from `map.bag` to `map.json` in v1.1.0 opened the door to flexible, backwards-compatible map extensions. The first major use of that flexibility lands here: individual mowing areas can now carry their own values for `outline_count`, `outline_overlap_count`, `outline_offset`, and `angle`.

The first three override the global defaults for that area only. `angle` replaces the automatic orientation detection (which is based on the first two meters of the outline) with a fixed heading — useful for areas where auto-detection consistently picks the wrong direction.

For now, these attributes must be added manually by editing `map.json` in a text editor. Support in the [OpenMower app](https://github.com/xtech/openmower-app) is planned. Thanks [@jrv](https://github.com/jrv) and [@rovo89](https://github.com/rovo89).

### v2 Hardware Improvements

Several improvements have landed specifically for v2 hardware:

- **Input service & emergency handling** — A new input service replaces the previous approach, with more granular emergency state tracking and handling. Thanks [@rovo89](https://github.com/rovo89).
- **High-level service** — A new high-level service consolidates control logic for v2 boards. Thanks [@Apehaenger](https://github.com/Apehaenger).
- **Extended battery reporting** — Battery state is now reported in more detail, giving better visibility into charge level and health. Thanks [@Apehaenger](https://github.com/Apehaenger), with additional contributions by [@ClemensElflein](https://github.com/ClemensElflein).

### User Parameters Always Win

The params include order has been corrected so that user-provided parameters are loaded last and always override built-in defaults. Previously, certain default values could silently take precedence. ([@ClemensElflein](https://github.com/ClemensElflein))

### Obstacle Area Ordering Fix

Obstacle areas are now respected regardless of the order they appear in the map. Previously, a quirk in how areas were processed could cause obstacles defined later in the map to be ignored during coverage planning. Thanks [@olliewalsh](https://github.com/olliewalsh).

### Reliability & Developer Experience

- **Deadlock protection in xbot_monitoring** — The monitoring subsystem is now guarded against deadlocks that could cause it to hang silently. Thanks [@rovo89](https://github.com/rovo89).
- **Unbuffered logging** — Log output is now written immediately rather than buffered, so messages appear in real time when tailing logs. Thanks [@Apehaenger](https://github.com/Apehaenger).
- **Simulator fixes** — Several issues in the simulator have been resolved. Thanks [@olliewalsh](https://github.com/olliewalsh) and [@rovo89](https://github.com/rovo89).

**Full changelog:** [v1.1.1 → v1.2.0](https://github.com/ClemensElflein/open_mower_ros/compare/v1.1.1...v1.2.0)
