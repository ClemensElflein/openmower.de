---
title: "OpenMower ROS v1.1.1"
date: 2026-03-16
author: "Clemens Elflein"
description: "Patch release: inactive area skipping, real-time logging order fix, MQTT parameter publishing, and meta RPC filtering."
---

[v1.1.1](https://github.com/ClemensElflein/open_mower_ros/releases/tag/v1.1.1) is a focused patch on top of v1.1.0.

### What's New

**Skip inactive mowing areas** — The mower now correctly skips areas that have been marked as inactive, so you don't need to delete and re-record areas you only want to temporarily disable. Thanks [@rovo89](https://github.com/rovo89).

**Publish parameters to MQTT** — Mower configuration parameters are now published to MQTT, making it easier to observe and integrate the current configuration from external tools and home automation systems. Thanks [@rovo89](https://github.com/rovo89).

**Ignore meta RPC method requests** — JSON-RPC meta requests are now filtered out correctly instead of being treated as unknown commands. Thanks [@rovo89](https://github.com/rovo89).

**Real-time logging order fix** — A fix to the real-time logging subsystem ensures log messages are emitted in the correct chronological order. Thanks [@Apehaenger](https://github.com/Apehaenger).

**Full changelog:** [v1.1.0 → v1.1.1](https://github.com/ClemensElflein/open_mower_ros/compare/v1.1.0...v1.1.1)
