---
title: Configuring xESC
linkTitle: Configuring xESC
weight: 110
description: >
  Configuring xESC in the mower 
---

If you bought the kit the xESC are preconfigured with [VESC firmware](https://github.com/vedderb/bldc) 5.x"

| device  	    | xESC        	|
|---------	    |-------------	|
| /dev/ttyAMA2 	| drive motor 	|
| /dev/ttyAMA3 	| mow motor   	|
| /dev/ttyAMA4 	| drive motor 	|

the config of the mow motor differs from the config of the drive motors, the configs of the two drive motors are equal

Configurations for each xESC can be found at &nbsp;https://github.com/ClemensElflein/OpenMower/tree/main/configs/xESC


## Configuring the xESC

Prereqs:
* VESC Tool (https://vesc-project.com/vesc_tool)

Connecting to the xESC:
1. `sudo systemctl stop openmower`
1. `socat tcp-listen:65102,reuseaddr,fork file:/dev/ttyAMAx,raw` <- replace `x` with devicenumber
1. start VESC Tool
1. Go to `Connection -> TCP` and insert openmower IP, leave port at 65102
1. Connect

{{% alert %}}
To change xESC just <kbd>Ctrl</kbd> + <kbd>C</kbd> in the openmower terminal replacing `ttyAMAx` with a new device number and reconnect in VESC Tool.
{{% /alert %}}

Loading XML motor configuration:
1. Download XML configuration files from repo
1. File>Load Motor Configuration XML
1. Select file named motor for the xESC you connected to
1. On the right toolbar click "Write Motor configuration" (the M with a arrow pointing down)

Loading XML app configuration:
1. Download XML configuration files from repo
1. File>Load App Configuration XML
1. Select file named app for the xESC you connected to
1. On the right toolbar click "Write App configuration" (the A with a arrow pointing down)


Finally hit <kbd>Ctrl</kbd> + <kbd>C</kbd> in the openmower terminal and start the openmower service again. `sudo systemctl start openmower`
