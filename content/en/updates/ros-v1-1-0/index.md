---
title: "OpenMower ROS v1.1.0"
date: 2025-12-07
author: "Clemens Elflein"
description: "Map format migrated to JSON, unmowed strip bug fixed, JSON-RPC over MQTT, SVG map visualiser, Switch Pro controller support, and much more."
---

[v1.1.0](https://github.com/ClemensElflein/open_mower_ros/releases/tag/v1.1.0) is a substantial release with a breaking map format change, a long-standing planner bug fix, and a wide range of new features.

### Map Format Changed to JSON

The map is now stored as `map.json` instead of `map.bag`. On first boot after upgrading, your existing `map.bag` will be **automatically converted** — no manual action required. From that point on only `map.json` is read and updated.

The MQTT map format has changed to match the internal representation. If the map doesn't appear correctly in the web interface after upgrading, do a hard reload (Ctrl+F5) or clear your browser cache.

### Unmowed Strip Fix

A long-reported issue where the mower left narrow strips of unmowed grass between path lines has been fixed. The root cause was an incorrect parameter in the coverage planner. If you had worked around this by reducing the configured tool width below the actual blade diameter, you can now revert that to the correct value.

### New Features

- **JSON-RPC 2.0 over MQTT** — The mower now exposes a JSON-RPC 2.0 interface over MQTT, enabling clean remote control and query from any MQTT client.
- **Capabilities published via MQTT** — The mower publishes what it supports at runtime, so integrations can discover features without hardcoding assumptions.
- **Map to SVG visualiser** — A new tool converts the mowing map to an SVG file for offline inspection and debugging.
- **Skip fill / outlines per area** — Individual areas can now be configured to skip the fill pass, the outline pass, or both.
- **Switch Pro and Shield controller support** — Two more gamepads are now supported for manual control.
- **Rain detection exposed to MQTT** — The `rain_detected` flag is now included in the `robot_state/json` MQTT topic.
- **ROS node auto-respawn** — All nodes now respawn automatically after 10 seconds if they crash, improving overall resilience.
- **Configurable wait times for docking and undocking** — The delays before and after docking manoeuvres are now configurable via environment variables.
- **Abort docking/undocking** — It's now possible to abort an in-progress docking or undocking manoeuvre.
- **Snapshot recording** — An option to record snapshots of recent ROS messages has been added for debugging purposes.
- **Updated web app**.

### Notable Bug Fixes

- Obstacles outside the mowing area are no longer considered during coverage planning.
- Simulator fixed for maps without a docking station.
- GPS protocol selection for v1 hardware now matches v2 behaviour.
- Various topic naming fixes.

### Internals & Infrastructure

- Environment variable handling has been comprehensively reworked.
- GPS driver moved to the `ll/services/gps` namespace.
- Docker build and CI workflows updated.
- `spdlog` output redirected into the ROS logging system.
- License switched to **GPLv3**.

**Full changelog:** [v1.0.2 → v1.1.0](https://github.com/ClemensElflein/open_mower_ros/compare/v1.0.2...v1.1.0)
