---
title: "Getting Started"
linkTitle: "Getting Started"
weight: 10
description: >
  How to get started with the Open Mower project.
---


## Prerequisites

Read this paragraph thoroughly in order to understand _which_ components you will need for the Open Mower project and _why_ you will need them. This prevents you from buying expensive stuff and later noticing that you will need even more expensive stuff in order to finish the project.


### Required Knowledge
- **Linux**: You should be comfortable using a Linux PC and you should know how to install a Raspberry Pi. This is important, because at the moment the Open Mower doesn't have a graphical user interface. It is started in an ssh terminal!
- **Very Basic Electronics**: You should be comfortable handling PCBs and have some basic soldering skills. If you have worked with an Arduino before, you should be fine.

### Required Parts
The Open Mower project consists of multiple parts:
- **The Robot**: The robot is a modified lawn-mowing robot. The robot is built by using the case and motors of an off-the-shelf lawn mowing robot and replacing the electronics with custom electronics. You will either need to buy the custom electronics or get the parts and solder it yourself.
- **RTK GPS**: The robot needs to know where _exactly_ it is inside your property in order to mow with high precision. This is achieved by a technology called RTK GPS. This type of GPS uses two receivers: one on the robot and one fixed base station. The base station sends error correction data to the robot via some radio link. This way, the robot is able to position with centimeter accuracy. This can be done using WiFi or some other long range radio. _Hint: There are also cloud services available for RTK error corrections. Some are free and some are paid_
- **Docking Station**: The robot needs to recharge in a docking station. Unfortunately the battery charging electronics is not part of the original docking station. That's why we will replace the electronics inside the original docking station as well.

If you are ready and want to get shopping, check out the [Shopping List](/docs/getting-started/shopping-list)


## Next Steps

If you have the parts and are ready to assemble the robot, read the [Robot Assembly](/docs/robot-assembly) docs.