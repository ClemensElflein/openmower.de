---
title: "GPS / Coordinate System"
linkTitle: "GPS / Coordinate System"
weight: 300
description: >
  Information about the RTK modes and the coordinate system used by OpenMower.
---

## How RTK GPS replaces the perimeter wire

RTK (Real-Time Kinematic) positioning combines satellite measurements at the mower with correction data from a fixed reference station or an NTRIP service. With a good RTK fix, OpenMower can use centimetre-level positioning to follow the mowing areas you record in the app.

The map defines lawn boundaries, fixed obstacles, and connecting paths. You still need to [record those areas]({{% relref "/docs/knowledge-base/operation/record-areas" %}}) and test them in your garden.

### Reception and correction data

The mower needs reliable satellite reception and a continuing supply of correction data. Nearby buildings and trees can interfere with reception; an ordinary GPS position without an RTK fix is not enough for precise mowing. Review the [GPS troubleshooting guide]({{% relref "/docs/troubleshooting/gps-rtk" %}}) when evaluating your garden.

You can [set up a local base station]({{% relref "/docs/knowledge-base/gps/rtk-base-setup" %}}) or use a suitable correction service. Include the required receiver, antenna, connectivity, and any service fees in your [parts budget]({{% relref "/docs/knowledge-base/getting-started/shopping-list" %}}).

## Positioning / Coordinate System

Positioning in the Open Mower project is done in a local 2D coordinate system. This means that the robot's current position can be described by the coordinates (X / Y) of the VRP and the current orientation.

The origin of the coordinate system can either be chosen freely by the user or can be set to the base station. If an external correction service is used, the origin has to be specified manually.

Open Mower uses a right-handed ENU coordinate system.
