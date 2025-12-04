---
title: Configuring xESC
linkTitle: Configuring xESC
description: >
  Configuring xESC in the mower 
---

The xESC motor controllers can be configured to work with many BLDC and DC motors.
The firmware for the controllers is based on the open source VESC project and therefore, the controllers can be configured using the VESC Configuration Tool.

### Prerequisites
- **Windows or Linux computer** to run the VESC Configuration Tool
- **VESC Tool (https://vesc-project.com/vesc_tool)** You can download the tool for free by adding the "free" version in your cart and proceeding to checkout.
- **OpenMower Firmware** needs to be successfully installed in the xCore board. This is needed because the xCore bridges the connection between your computer and the xESC. If you haven't done it, follow the [Firmware Update]({{< relref "/docs/Knowledge-Base/firmware-update" >}}) guide.
- **Optional (but makes your life easier):**<br/>Configuration files for the mower you are using.<br/>Look in the [OpenMower repository](https://github.com/ClemensElflein/OpenMower/tree/main/configs/xESC) for the files suited for your mower. <br/>You will need three files:
    - App configuration XML (sets the baud rate, etc. Same for all three xESC controllers)
    - Mower Motor configuration XML (motor parameters for the mower motor)
    - Drive Motor configuration XML (motor parameters for the wheel motors)

### Configuration Process
#### Stop ROS from interfering with the controllers
`openmower stop` to stop ROS from interfering with the controllers during configuration.


#### Expose the ESC to the network
![Expose ESC to the network]({{< relref "/docs/Knowledge-Base/configure-xesc" >}}/images/openmower-expose-xesc.png)
Run `openmower expose-esc [left|right|mower]` to expose the xESC controller (choose `left`, `mower` or `right`).<br/>The controller is then reachable in your local network on `openmower:65102` until you hit <kbd>Ctrl</kbd> + <kbd>C</kbd>.


#### Connect to the xESC
![Connect VESC tool to ESC]({{< relref "/docs/Knowledge-Base/configure-xesc" >}}/images/ConnectToTheESC.png)
Open the VESC Configuration Tool and connect to the xESC controllers by clicking:
- `Connection -> TCP` **[1]**
- Insert the IP address of your mower or `openmower` into the Address field **[2]**.
- Set the port to `65102` **[3]**
- Click `Connect` **[4]**

{{% alert title="Information" color="info" %}}
If you encounter this warning message:


![Warning message]({{< relref "/docs/Knowledge-Base/configure-xesc" >}}/images/Firmware_Version_Warning_Message.png)

you can safely ignore it. The VESC tool is backward compatible with the firmware version used on the xESC controller.
{{% /alert %}}




#### Upload the configurations
{{< image-gallery gallery_dir="images/upload-configurations" >}}

With the VESC Configuration Tool connected, you can now upload the configuration to your xESC controllers:
- **[Image 1]**: Click `File -> Load Motor Configuration XML`
- **[Image 2]**: Select the motor configuration XML file for your motor (different for mowing motor and the drive motors)
- **[Image 3]**: Ignore the version message, if it appears
- **[Image 4]**: Click `Write Motor configuration`. The green banner will appear on success.
- **[Image 5]**: Click `File -> Load App Configuration XML`. Ignore the version message, if it appears
- **[Image 6]**: Click `Write App configuration`. The green banner will appear on success.
- **Hit <kbd>Ctrl</kbd> + <kbd>C</kbd>** in the openmower terminal to stop exposing the xESC controller.


**Repeat these steps for all three of the three xESC controllers.**

