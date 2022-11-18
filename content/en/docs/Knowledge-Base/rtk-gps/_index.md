---
title: "GPS / Coordinate System"
linkTitle: "GPS / Coordinate System"
weight: 4
description: >
  Information about the RTK modes and the coordinate system used by OpenMower.
---

## Positioning / Coordinate System

Positioning in the Open Mower project is done in a local 2D coordinate system. This means, that the robot's current position can be described by the coordinates (X / Y) of the VRP and the current orientation.

The origin of the coordinate system can either be chosen freely by the user or can be set to the base station. If an external correction service is used, the origin has to be specified manually.

Open Mower uses a right-handed ENU coordinate system.
