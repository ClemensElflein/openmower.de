---
title: Configuring xESC
linkTitle: Configuring xESC
description: >
  Configuring xESC in the mower 
---

<!-- ![WiFi Connect]({{< relref "/docs/Knowledge-Base/configure-xesc" >}}/images/connect_wifi_screen_1.png) -->

The xESC motor controllers can be configured to work with many BLDC and DC motors.
The firmware for the controllers is based on the open source VESC project and therefore, the controllers can be configured using the VESC Configuration Tool.

### Prerequisites
- **Windows or Linux computer** to run the VESC Configuration Tool
- **VESC Tool (https://vesc-project.com/vesc_tool)** You can download the tool for free by adding the "free" version in your cart and proceeding to checkout.
- Firmware needs to be successfully installed in the xCore board. This is needed because the xCore bridges the connection between your computer and the xESC.
- **Optional (but makes your life easier):**<br/>Configuration files for the mower you are using.<br/>Look in the [OpenMower repository](https://github.com/ClemensElflein/OpenMower/tree/main/configs/xESC) for the files suited for your mower. <br/>You will need three files:
  - App configuration XML (sets the baud rate, etc.)
  - Mower Motor configuration XML (motor parameters for the mower motor)
  - Drive Motor configuration XML (motor parameters for the wheel motors)

### Configuration Process
By default, the xESC controllers are not directly reachable within your local network, but the `openmower` tool 
allows you to expose the xESC controllers to your local network, so that you can configure them using the VESC Configuration Tool.

On a high level, configuration goes like this:
- Run `openmower stop` to stop ROS from interfering with the controllers during configuration
- Upload configuration to your xESC controllers (repeat for each of the three xESC controllers):
  - `openmower expose-esc [left|right|mower]` to expose the xESC controller (left, mower or right).<br/>The controller is then reachable in your local network on `openmower:65102` until you hit <kbd>Ctrl</kbd> + <kbd>C</kbd>.
  - Connect the VESC tool and upload the configuration files.
  - Hit <kbd>Ctrl</kbd> + <kbd>C</kbd> in your openmower terminal.

### Detailed Configuration
Open the VESC Configuration Tool and connect to the xESC controllers by clicking:
- `Connection -> TCP`
- Insert the IP address of your mower or `openmower` into the field.
- Set the port to `65102`
- `Connect`



With the VESC Configuration Tool connected, you can now upload the configuration to your xESC controllers:
- `File -> Load Motor Configuration XML`
- Select the motor configuration XML file for your mower (different for mowing motor and the drive motors)
- `Write Motor configuration`
- `File -> Load App Configuration XML`
- Select the app configuration XML file for your mower (the same for all three motors)
- `Write App configuration`

Repeat these steps for each of the three xESC controllers.


### Configuring the xESC

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
1. Download XML configuration files from [repo](https://github.com/ClemensElflein/OpenMower/tree/main/configs/xESC)
1. File>Load Motor Configuration XML
1. Select file named motor for the xESC you connected to
1. On the right toolbar click "Write Motor configuration" (the M with a arrow pointing down)

Loading XML app configuration:
1. Download XML configuration files from [repo](https://github.com/ClemensElflein/OpenMower/tree/main/configs/xESC)
1. File>Load App Configuration XML
1. Select file named app for the xESC you connected to
1. On the right toolbar click "Write App configuration" (the A with a arrow pointing down)


Finally hit <kbd>Ctrl</kbd> + <kbd>C</kbd> in the openmower terminal and start the openmower service again. `sudo systemctl start openmower`
