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
Run `openmower expose-xesc [left|right|mower]` to expose the xESC controller (choose `left`, `mower` or `right`).<br/>The controller is then reachable in your local network on `openmower:65102` until you hit <kbd>Ctrl</kbd> + <kbd>C</kbd>.


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


#### Configure xESC

{{< tabpane text=true >}}
{{% tab header="**Choose your configuration path**:" disabled=true /%}}
{{% tab header="Preset configs (Yard Force)" text=true %}}


#### Upload the configurations

<div class="tab-gallery">{{< image-gallery gallery_dir="images/upload-configurations" >}}</div>

With the VESC Configuration Tool connected, you can now upload the configuration to your xESC controllers:
- **[Image 1]**: Click `File -> Load Motor Configuration XML`
- **[Image 2]**: Select the motor configuration XML file for your motor (different for mowing motor and the drive motors)
- **[Image 3]**: Ignore the version message, if it appears
- **[Image 4]**: Click `Write Motor configuration`. The green banner will appear on success.
- **[Image 5]**: Click `File -> Load App Configuration XML`. Ignore the version message, if it appears
- **[Image 6]**: Click `Write App configuration`. The green banner will appear on success.
- **Hit <kbd>Ctrl</kbd> + <kbd>C</kbd>** in the openmower terminal to stop exposing the xESC controller.


**Repeat these steps for all three of the three xESC controllers.**

{{% /tab %}}


{{% tab header="SABO/John Deere (tuning)" text=true %}}

#### Required preparations

1. Remove the mower blade.
2. Really, remove the blade! This is a huge mower with a strong motor and large blade! :skull:
3. Lift the mower's rear so wheels can spin freely (use a carton, block or stand).
4. Unmount the mower blade!
6. Use battery power for calibration (not dock power), and ensure the battery has sufficient charge.
7. Check if you disassembled the mower blade!


#### Drive motor calibration (left then right)

Perform calibration for left drive first, then repeat the procedure for the right drive.

1. **Enable realtime data:** Later on, we wanna validate our calibration with a known reference value, but also during calibration it's interesting to see the displayed values in the marked 2 window. That's why we enable real-time data first:<br>
   ![RT Data](images/sabo/vesc_3_realtime_data.jpg)
1. Start the **FOC Calibration Wizard**:<br>
   ![Start FOC Calibration](images/sabo/vesc_4_voc_1.jpg)<br>

1. Now we need to provide some specs of our motor. **These are the specs for the left and right drive motors**, for the mow motor, we need to use other specs:<br>
   <img src="images/sabo/vesc_4_voc_2.jpg" style="vertical-align: middle; width:31%"> 🡆 <img src="images/sabo/vesc_4_voc_3.jpg" style="vertical-align: middle; width:31%"> 🡆 <img src="images/sabo/vesc_4_voc_4.jpg" style="vertical-align: middle; width:31%"><br>

   <img src="images/sabo/vesc_4_voc_5.jpg" style="vertical-align: middle; width:31%"> 🡆 <img src="images/sabo/vesc_4_voc_6.jpg" style="vertical-align: middle; width:31%"> 🡆 <img src="images/sabo/vesc_4_voc_7.jpg" style="vertical-align: middle; width:31%"><br>

1. Once calibration has been done, **do not change the direction** (even though the left wheel turns forward during calibration, whereas the right one backwards):

   <img src="images/sabo/vesc_4_voc_8.jpg" style="vertical-align: middle; width:31%">
9. Now that the calibration succeed, lets test the result:
   ![Run Test](images/sabo/vesc_5_test.jpg)<br>

   Test with "**D 0,4**" (1) and press the "Duty cycle" play button (2). If it draw **<= 0.15A** (3) and sound healty, it is calibrated well.<br>
   Test with some higher duty settings. It will become more loud for sure, but should always spin smooth and sound healty. If not, press the STOP sign (4).

10. As a last important step, load the correct ESC-App config via: _File → Load App Configuration XML_, choose `SABO_Drive-App.xml` (see [SABO ESCs configs](https://github.com/xtech/hw-openmower-sabo/tree/main/Configs/xESC)) and finally press the `↧A` icon (Write app configuration) on the right side.

11. Optional misc settings which you might align to be within the motor/battery specs:<br>
   ![Drive Settings](images/sabo/vesc_6_settings1.jpg)

Done :satisfied:<br>
... **but not finished** :v: ... you need to do the whole procedure again, but with the right drive side.

So, <kbd>Ctrl</kbd>+<kbd>c</kbd> your `openmower expose-xesc left`, and do it again but with `openmower expose-xesc right`.


#### Mow Motor Calibration

For the mow motor ESC calibration, you do the same workflow, but with adapted values:

1. `openmower expose-xesc mower`
1. During FOC Calibration Wizard use the following values:
   - Tab "Motor" = Medium Inrunner ~750g
     - Advanced: Max Power Loss = 200, Motor Poles = 8
   - Tab "Battery"
     - Battery Capacity = 3.9Ah (same as before)
   - Tab "Setup"
     - Gear Ratio = Check Direct Drive
     - Motor Poles = 8
     - Motor Temp. Sensor = disabled

1. Test with "**D 0,08**" which should draw **<= 0.52A** (without assembled blade)
1. Check/Adjust blade rotation direction:<br>
   We need to ensure that the blade rotate CCW (when watching from downside onto the axis). Do this with a slow rotation speed like "D 0,08".

   If it rotates CW, change direction via: _Motor Settings → General → Tab General → Invert Motor Direction_. **Do not forget to do: "Write motor configuration" via `↧M`**

1. Load the correct ESC-App config via: _File → Load App Configuration XML_, choose `SABO_Mower-App.xml` (see [SABO ESCs configs](https://github.com/xtech/hw-openmower-sabo/tree/main/Configs/xESC)) and finally press the `↧A` icon (Write app configuration) on the right side.

1. Limit blade RPM:<br>
   It's important to limit the max. RPM to the one like OEM is running it! Otherwise you risk your motor bearings or more dangerous: Your blade might fly away :skull:
   ![Limit RPM](images/sabo/vesc_7_mow_settings2.jpg)

1. Optional misc settings which you might align to be within the motor/battery specs:<br>
   ![Drive Settings](images/sabo/vesc_7_mow_settings1.jpg)

{{% /tab %}}


{{% tab header="New model? Let’s dial it in" %}}

Choose your adventure. Your build, your rules.

{{% /tab %}}

{{< /tabpane >}}
