---
title: "Getting Started"
linkTitle: "Getting Started"
weight: 10
description: >
  How to get started with the Open Mower project.
---

## Important Info
{{% alert title="Read Before Starting" color="warning" %}}
- **This project is still in an early stage**: You will need time to get the robot running! You will encounter bugs! You might break stuff! You might spend the money and don't get it to work! No guarantees for anything!
- **DO NOT** use the stock charger with the OpenMower mainboard!
- **Lithium Batteries can be dangerous:** You will be building your own charger. Make sure you are comfortable doing that and understand the dangers of working with Lithium batteries.
- **Read** the whole documentation and **get a high level overview**: Understand every step involved in the build before actually doing anything.
- **You are responsible for your own actions**: Be sure that you know what you are doing!
- **This documentation is work in progress**: There might be errors and missing steps. If you have questions **ask on Discord**.
{{% /alert %}}

## Prerequisites

Read this paragraph thoroughly in order to understand _which_ components you will need for the Open Mower project and _why_ you will need them. This prevents you from buying expensive stuff and later noticing that you will need even more expensive stuff in order to finish the project.


### Required Knowledge
- **Linux**: You should be comfortable using a Linux PC and you should know how to install a Raspberry Pi. Although there is the Open Mower app available, you will need to change some settings and probably do some debugging to get it working.
- **Electronics**: You should be comfortable handling PCBs and have some soldering skills. You should be capable of understanding each step you are about to perform.

### Required Parts
The Open Mower project consists of multiple parts:
- **The Robot**: The robot is a modified lawn-mowing robot. The robot is built by using the case and motors of an off-the-shelf lawn mowing robot and replacing the electronics with custom electronics. You will either need to buy the custom electronics or get the parts and solder it yourself.
- **RTK GPS**: The robot needs to know where _exactly_ it is inside your property in order to mow with high precision. This is achieved by a technology called RTK GPS. This type of GPS uses two receivers: one on the robot and one fixed base station. The base station sends error correction data to the robot via some radio link. This way, the robot is able to position with centimeter accuracy. This can be done using WiFi or some other long range radio. _Hint: There are also cloud services available for RTK error corrections. Some are free and some are paid_
- **Docking Station**: The robot needs to recharge in a docking station. Unfortunately the battery charging electronics is not part of the original docking station. That's why we will replace the electronics inside the original docking station as well. **Do not use the stock docking station with the modified robot**

If you are ready and want to get shopping, check out the [Shopping List](/docs/knowledge-base/shopping-list)

## Build Steps

![Open Mower Build Overview](flow_chart.jpg)

It's important to build the components in the correct order:
- The first step is to modify the robot by follwing the [Robot Assembly](/docs/robot-assembly) steps. Don't let the mower powered on for too long, because **you cannot charge it using the unmodified docking station**.
- With the modified robot it's time to modify the docking station by following the [Docking Station Assembly](/docs/docking-station-assembly) section. **Now you are able to charge the battery with the new docking station.**
- The next step is to setup the software. Since this might take some time and therefore drain the battery, it's important that you do this step after finishing the docking station assembly. This step connects the robot to your WiFi, downloads the OpenMower software and you will do some general configuration.
- Finally with the software running, you can use the Open Mower App to record your mowing areas and navigation areas and finally mow.


If you have the parts and are ready to assemble the robot, read the [Robot Assembly](/docs/robot-assembly) docs.