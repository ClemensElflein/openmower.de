---
title: "OpenMower ROS v1.0.2"
date: 2025-06-17
author: "Clemens Elflein"
description: "GPS via TCP, rain detection, angled undocking, RPM and sensor thresholds, background sound, v2 hardware preparation, and many fixes."
---

[v1.0.2](https://github.com/ClemensElflein/open_mower_ros/releases/tag/v1.0.2) is a large feature release with contributions from across the community.

### Highlights

**GPS via TCP** — The GPS driver can now connect to a GPS source over TCP, making it easier to use network-attached GPS receivers and relay setups. Thanks [@rovo89](https://github.com/rovo89).

**Rain detection** — The mower now implements rain logic: when rain is detected it stops mowing and waits for the configurable `OM_RAIN_DELAY_MINUTES` before resuming. Thanks [@olliewalsh](https://github.com/olliewalsh).

**Angled undocking** — The mower can now undock at an angle, improving reliability on docking stations where a straight-back exit causes issues. Thanks [@AndreKR](https://github.com/AndreKR).

**RPM monitoring and sensor thresholds** — Motor RPM and configurable sensor thresholds have been added, along with improved sensor reporting. Thanks [@Apehaenger](https://github.com/Apehaenger).

**Background sound** — An option to play background sounds has been added. Thanks [@Apehaenger](https://github.com/Apehaenger).

**Manual mower control during area recording** — It's now possible to drive the mower manually while in area recording mode. Thanks [@olliewalsh](https://github.com/olliewalsh).

**Toggle automatic point collection during recording** — Point collection can now be toggled on and off during a recording session. Thanks [@rovo89](https://github.com/rovo89).

**Configurable docking retry count above 10** — The docking retry limit is no longer capped at 10. Thanks [@jeremysalwen](https://github.com/jeremysalwen).

**OM_NO_COMMS environment variable** — A new env var disables the communications node entirely, useful for running without the lower-level hardware connected. Thanks [@jeremysalwen](https://github.com/jeremysalwen).

**Sparse path planning** — The slic3r coverage planner has been updated to support sparse paths, enabling less dense mowing patterns. Thanks [@ClemensElflein](https://github.com/ClemensElflein).

**IMU axis mapping for v2 hardware** — Correct IMU axis orientation for the v2 mainboard has been added. Thanks [@Apehaenger](https://github.com/Apehaenger).

### v2 Hardware Preparation

This release includes early groundwork for the v2 hardware interface, reworked mower communications, an enlarged config packet format, and an `InputService` interface (the initial version was reverted pending further work, but the infrastructure is in place).

### Notable Bug Fixes

- Fixed GPS header detection for UBX protocol.
- Fixed planner crash on certain edge-case map geometries.
- Fixed mowing motor repeatedly starting and stopping when GPS fix is lost.
- Fixed segmentation fault in slic3r.
- Fixed perimeter joining when islands exist.
- Updated NTRIP client to prevent IP bans from RTK2GO.
- Improved undocking smoothness.

### Internals

- Parameter system comprehensively reworked.
- UART mapping handling updated for newer kernel versions.
- FTC planner stop-distance lookahead disabled once `speed_fast_threshold` is exceeded.
- `spdlog` redirected to the ROS logging system.
- Native arm64 CI runner support.
- License switched to **GPLv3**.

**Full changelog:** [v1.0.1-edge.2 → v1.0.2](https://github.com/ClemensElflein/open_mower_ros/compare/v1.0.1-edge.2...v1.0.2)
