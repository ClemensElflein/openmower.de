---
title: "Prepare the SD Card"
linkTitle: SD Card
weight: 20
description: >
  In this step we will install the SD card and configure the basic settings for our mower.
---

We have created a Container image that contains the Open Mower software. Additionally, we have created a Raspberry Pi image that is modified specifically for Open Mower use. In this step, we flash the image and do some basic setup for your mower.


## Prerequisites

In order to follow this guide, you will need:
- **An SD card with at least 16 GB**
- **A PC with the Raspberry Pi Imager Software installed:**<br/>
  🔗&nbsp;[https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/)
- **The latest OpenMowerOS Image:**<br/>
  🔗&nbsp;[https://github.com/ClemensElflein/OpenMowerOS/releases](https://github.com/ClemensElflein/OpenMowerOS/releases)<br/>
  You can download it in the `Assets` section. You don't need to unpack the image.
- **An SD card reader**


## Step 1: Flash the Image to your SD Card

- Start the Raspberry Pi Imager Software. Select `CHOOSE OS -> Use Custom`. Then open the image file you downloaded earlier.
- Select `CHOOSE STORAGE` and select your SD card from the Window. **Make sure that you are really selecting the correct SD card, all data on the selected device will be erased!**
- Select `WRITE` and wait for the process to finish


## Step 2: Configure Open Mower

For the robot to work correctly, you need to set some configuration options. In order to make this as simple as possible, the configuration files are located in the `boot` partition of your newly flashed SD card. You can access the files on Windows or Linux without any additional steps (it's mounted as a mass-storage device). If the partition does not show up in your file explorer, unplug and replug the SD card.


#### /openmower/openmower_version.txt (on Linux: /boot/openmower/openmower_version.txt)

This file selects the Open Mower version to use. You can choose the following:
{{< tabpane text=true >}}
{{% tab header="**OpenMowerOS version**:" disabled=true /%}}
{{% tab header="0.1.0" %}}
**edge:** This one changes very often. Only use it if you want to take part in the development or are asked to use it by a developer.

**alpha:** For people who like to test stuff. This one will be updated fairly often as well and without notice. Only use it if you want to be among the first people to get new features, but prepare to have issues.

**beta (recommended):** This one is the _most stable_ one of the three. I try to keep this as stable as possible.
{{% /tab %}}
{{< /tabpane >}}


#### /openmower/mower_config.txt (on Linux: /boot/openmower/mower_config.txt)

This file has important settings for the Open Mower software.
The configurations in the file might change with the Open Mower release, that's why the documentation can be found in the file. Here is an example file, but please use and modify the one that came with your OpenMowerOS.

{{< spoiler text="Click to see annotated config code" id="mower_config_example">}}
```bash
################################
##     Important Settings     ##
################################

# Most of the time you must modify those settings, so they are moved to the beginning of document from their respective sections
# Refer to documentation for more info: https://openmower.de/docs/robot-assembly/prepare-the-parts/prepare-sd-card/#step-2-configure-open-mower

# Your Hardware Version (more a firmware version, really). Check the OpenMower docs (https://openmower.de/docs/versions/) for the firmware versions.
# Supported values as of today:
# 0_13_X: Use this if you have 0.13.x mainboard with LSM6DSOTR (default).
# 0_12_X_LSM6DSO: Use this if you have an LSM6DSOTR and have a 0.12.x mainboard.
# 0_11_X_WT901: Use this if you have an WT901 and have a 0.11.x mainboard.
# 0_10_X_WT901: Use this if you have an WT901 and have a 0.10.x mainboard.
# 0_10_X_MPU9250: Use this if you have an MPU9250 and have a 0.10.x mainboard (be aware that there are many fake chips on the market. So probably not your hardware version).
# 0_9_X_WT901_INSTEAD_OF_SOUND: Use this if you have soldered the WT901 in the sound module's slot and have a 0.9.x mainboard.
# 0_9_X_MPU9250: Use this if you have an MPU9250 and have a 0.9.x mainboard (be aware that there are many fake chips on the market. So probably not your hardware version).
export OM_HARDWARE_VERSION="0_13_X"

# Uncomment and set to coordinates near your future docking station, this will be your map origin.
# There might be a case that you don't need those if you using OM_USE_RELATIVE_POSITION=True
export OM_DATUM_LAT=48.CHANGEME
export OM_DATUM_LONG=11.CHANGEME

# NTRIP Settings
# Set to False if using external radio plugged into the Ardusimple board.
export OM_USE_NTRIP=True
export OM_NTRIP_HOSTNAME=192.168.178.55
export OM_NTRIP_PORT=2101
export OM_NTRIP_USER=gps
export OM_NTRIP_PASSWORD=gps
export OM_NTRIP_ENDPOINT=BASE1

################################
## Hardware Specific Settings ##
################################

# The type of mower you're using, used to get some hardware parameters automatically
# Currently supported:
# YardForce500
# YardForceSA650
# CUSTOM (put your configs in ~/mower_params/)
export OM_MOWER="YardForce500"

# Select your ESC type
# Supported values as of today:
# xesc_mini: for the STM32 version (VESC)
# xesc_2040: for the RP2040 version (very experimental!)
export OM_MOWER_ESC_TYPE="xesc_mini"

# Select your gamepad
# Currently supported: ps3, steam_stick, steam_touch, xbox360
export OM_MOWER_GAMEPAD="xbox360"

# Set to true to record your session.
# Output will be stored in your $HOME
# export OM_ENABLE_RECORDING_ALL=False

# Full Sound Support - But read on carefully:
# Up to (and inclusive) OM hardware version 0.13.x, DFPlayer's power supply is set by default to 3.3V.
# This is done by solder jumper "JP1" whose board track is by default at 3.3V.
# If you manually opened the 3.3V track and solder a bridge to 5V, then you can indicate it here to get full sound support.
# DO NOT enable "OM_DFP_IS_5V=True" if you haven't changed it in real. You might risk your "Raspberry Pico"!
# And even if the Pico isn't expensive, it's a torture to replace it.
# Full details are available here: https://github.com/ClemensElflein/OpenMower/blob/main/Firmware/LowLevel/README-Sound%2C%20DFPIS5V.md
# export OM_DFP_IS_5V=False
#
# Language as ISO-639-1 code string (currently only used by sound).
# Supported languages: en|de
# export OM_LANGUAGE="en"
#
# Sound volume (%)
# Supported values:
# 0-100 = Set sound volume on OM start, ignoring a previously set volume level (i.e. changed by CoverUI)
#    -1 = Don't change a previously set volume level (i.e. changed by CoverUI)
# export OM_VOLUME=-1

################################
##        GPS Settings        ##
################################
# Relative Positioning vs LatLng coordinates
# If OM_USE_RELATIVE_POSITION=False, we're using an arbitrary point as map origin. This point is called the DATUM point and
# needs to be set using OM_DATUM_LAT and OM_DATUM_LONG below.
# If OM_USE_RELATIVE_POSITION=True, we're using the ublox NAVRELPOSNED messages as position.
# This makes your base station the map origin
# For it recommended to set OM_USE_RELATIVE_POSITION to False. This way you can move your base station without re-recording your maps and it's also more compatible overall.
export OM_USE_RELATIVE_POSITION=False

# GPS protocol. Use UBX for u-blox chipsets and NMEA for everything else
export OM_GPS_PROTOCOL=UBX

# If you want to use F9R's sensor fusion, set this to true (you will also need to set DATUM_LAT and DATUM_LONG.
# Consider this option unstable, since I don't have the F9R anymore, so I'm not able to test this.
# IF YOU DONT KNOW WHAT THIS IS, SET IT TO FALSE
export OM_USE_F9R_SENSOR_FUSION=False


################################
##    Mower Logic Settings    ##
################################
# The distance to drive forward AFTER reaching the second docking point
export OM_DOCKING_DISTANCE=1.0

# The distance to drive for undocking. This needs to be large enough for the robot to have GPS reception
export OM_UNDOCK_DISTANCE=2.0

# How many outlines should the mover drive. It's not recommended to set this below 4.
export OM_OUTLINE_COUNT=4

# Mowing angle offset -180 deg - +180 deg, 0 = east, -90 = north. If mowing angle offset is not absolute it gets added to the auto detected angle which is set by the first 2 m of recorded outline.
export OM_MOWING_ANGLE_OFFSET=0
export OM_MOWING_ANGLE_OFFSET_IS_ABSOLUTE=False

# The width of mowing paths.
# Choose it smaller than your actual mowing tool in order to have some overlap.
# 0.13 works well for the Classic 500.
export OM_TOOL_WIDTH=0.13

# Voltages for battery to be considered full or empty
export OM_BATTERY_EMPTY_VOLTAGE=23.0
export OM_BATTERY_FULL_VOLTAGE=28.0

# Mower motor temperatures to stop and start mowing
export OM_MOWING_MOTOR_TEMP_HIGH=80.0
export OM_MOWING_MOTOR_TEMP_LOW=40.0

export OM_GPS_WAIT_TIME_SEC=10.0
export OM_GPS_TIMEOUT_SEC=5.0

# Mowing Behavior Settings
# True to enable mowing motor
export OM_ENABLE_MOWER=true

# True to start mowing automatically. If this is false, you need to start manually by pressing the start button
export OM_AUTOMATIC_START=false

export OM_OUTLINE_OFFSET=0.05

# source the default values for the hardware platform.
# you only need this line on non-docker installs. in the docker, it will be done automatically.
# source $(rospack find open_mower)/params/hardware_specific/$OM_MOWER/default_environment.sh
```
{{< /spoiler >}}


## Step 3: Done 🎉

You can now remove the SD card from your PC, it is ready to be used with the Open Mower software.
