---
title: "Concepts"
linkTitle: "Concepts"
weight: 4
description: >
  This chapter introduces concepts used in the Open Mower project. 
---

## Positioning / Coordinate System

Positioning in the Open Mower project is done in a local 2D coordinate system. This means, that the robot's current position can be described by the coordinates (X / Y) of the VRP and the current orientation.

The origin of the coordinate system can either be chosen freely by the user or can be set to the base station. If an external correction service is used, the origin has to be specified manually.

Open Mower uses a right-handed ENU coordinate system.

## The Map

The most important information for the Open Mower is its map. The map tells the robot in which areas the robot is allowed to drive **(= Navigation Area)**, which areas need to be mowed **(= Mowing Area)** and where the docking station is located. Using this information, the robot is able to do its work automatically.

Each area consists of **one outline** and **multiple obstalces**. The mower is allowed to drive inside the outline of all areas, except for the obstacles. This way you can exclude some parts of your lawn and prevent the mower from entering them.