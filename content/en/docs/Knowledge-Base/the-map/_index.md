---
title: "The Map"
linkTitle: "The Map"
weight: 4
description: >
  Information about the Open Mower map (Mowing Areas, Navigation Areas, Docking Point).
---

## The Map

The most important information for the Open Mower is its map. The map tells the robot in which areas the robot is allowed to drive **(= Navigation Area)**, which areas need to be mowed **(= Mowing Area)** and where the docking station is located. Using this information, the robot is able to do its work automatically.

Each area consists of **one outline** and **multiple obstalces**. The mower is allowed to drive inside the outline of all areas, except for the obstacles. This way you can exclude some parts of your lawn and prevent the mower from entering them.

The map is stored in the map.bag file that is located on the mower at /root/ros_home/.ros 

