---
title: "OpenMower ROS v1.0.1 Edge Releases"
date: 2024-07-24
author: "Clemens Elflein"
description: "Three edge (pre-release) builds between v1.0.0 and v1.0.2: docking improvements, NTRIP fix, YardForce Rev4 support, and more."
---

Three edge pre-releases shipped between v1.0.0 and v1.0.2. Here's a summary of what landed in each.

### v1.0.1-edge.2 — 2024-07-24

- **Docking retry on roll-off** — The mower now retries docking if it rolls off the charger instead of giving up. Thanks [@jeremysalwen](https://github.com/jeremysalwen).
- **NTRIP IP ban fix** — Fixed an issue where the NTRIP client could get your IP banned from public casters. Thanks [@EtheriVR](https://github.com/EtheriVR).
- **Configurable docking retry count** — `docking_retry_count` can now be changed via environment variable. Thanks [@gytisgreitai](https://github.com/gytisgreitai).
- **Publish current mowing area** — The active mowing area is now published to both ROS and MQTT. Thanks [@11phc](https://github.com/11phc).
- **YardForce Rev4 adapter board support** — Added support for the Rev4 adapter board variant.
- **Bug fixes** — Map not rebuilt unnecessarily on nav point clear; fake `mower/status` stamp set correctly in simulation; mowing motor no longer starts and stops repeatedly on GPS fix loss.

### v1.0.1-edge.1 — 2024-07-02

- **Docking improvements** — Optional delay after voltage detection during docking; logging of the reason for each docking event.
- **Reset emergency from app** — The OpenMower app can now reset the emergency state remotely.
- **Configuration as JSON Schema** — The mower configuration is now described as a JSON Schema, enabling better tooling and validation.
- **Dockerised dev environment** — A fully containerised development environment has been added.

### v1.0.1-edge.0 — 2024-05-31

- **Docking reliability** — Short voltage drops during mowing due to current spikes are now tolerated without triggering a docking event.
- **NMEA GPS sign fix** — Fixed incorrect sign in the motion vector when using NMEA GPS devices.
- **Slic3r segfault fix** — Fixed a segmentation fault in the coverage planner.
- **Perimeter fix** — Fixed perimeter joining when islands are present in the map.
