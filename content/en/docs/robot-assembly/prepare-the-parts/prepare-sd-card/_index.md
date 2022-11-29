---
title: "Prepare the SD Card"
linkTitle: "Prepare the SD Card"
weight: 20
description: >
  In this step we will install the SD card and configure the basic settings for our mower.
---

We have created a Docker image that contains the Open Mower software. Additionally, we have created a Raspberry Pi image that is modified specifically for Open Mower use. In this step we flash the image and do some basic setup for your mower.

## Prerequisites
In order to follow this guide, you will need:
- **An SD card with at least 16 GB**
- **A PC with the Raspberry Pi Imager Software installed:**<br/>
  :link:&nbsp;[https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/)
- **The latest OpenMowerOS Image:**<br/>
  :link:&nbsp;[https://github.com/ClemensElflein/OpenMowerOS/releases](https://github.com/ClemensElflein/OpenMowerOS/releases)<br/>
  You can download it in the `Assets` section. You don't need to unzip the image.
- **An SD card reader**

## Step 1: Flash the Image to your SD Card
- Start the Raspberry Pi Imager Software. Select `CHOOSE OS > Use Custom`. Then open the image file you downloaded earlier.
- Select `CHOOSE STORAGE` and select your SD card from the Window. **Make sure that you are really selecting the correct SD card, all data on the selected device will be erased!**
- Select `WRITE` and wait for the process to finish

## Step 2: Configure Open Mower
For the robot to work correctly, you need to set some configuration options. In order to make this as simple as possible, the configuration files are located in the `boot` partition of your newly flashed SD card. You can access the files in Windows or Linux without any additional steps (it's mounted as mass-storage device). If the partition does not show up in your file explorer, unplug and replug the SD card.

#### /boot/openmower/openmower_version.txt
This file selects the Open Mower version to use. You can choose the following:
- **testing:** This one changes very often. Only use it if you want to take part in the development or are asked to use it by a developer.
- **alpha:** For people who like to test stuff. This one will be updated fairly often as well and without notice. Only use it, if you want to be among the first people to get new features, but prepare to have issues.
- **beta (recommended):** This one is the _most stable_ one of the three. I try to keep this as stable as possible.

An example:
```bash
OM_VERSION="beta"

export OM_VERSION
```

#### /boot/openmower/mower_config.txt
This file has important settings for the Open Mower software.
The configurations in the file might change with the Open Mower release, that's why the documentation can be found in the file. Here is an example file, but please use and modify the one that came with your OpenMowerOS.

{{< spoiler text="Click to see annotated config code" id="mower_config_example">}}
```bash
################################
## Hardware Specific Settings ##
################################

# The type of mower you're using, used to get some hardware parameters automatically
# Currently supported:
# YardForce500
# CUSTOM (put your configs in ~/mower_params/)
export OM_MOWER="YardForce500"

# Your Hardware Version (more a firmware version, really). Check the OpenMower docs (https://www.openmower.de/docs) for the firmware versions.
# Supported values as of today:
# 0_10_X_WT901: Use this if you have an WT901 and have a 0.10.x mainboard.
# 0_10_X_MPU9250: Use this if you have an MPU9250 and have a 0.10.x mainboard (be aware that there are many fake chips on the market. So probably not your hardware version).
# 0_9_X_WT901_INSTEAD_OF_SOUND: Use this if you have soldered the WT901 in the sound module's slot and have a 0.9.x mainboard.
# 0_9_X_MPU9250: Use this if you have an MPU9250 and have a 0.9.x mainboard (be aware that there are many fake chips on the market. So probably not your hardware version).
export OM_HARDWARE_VERSION=""

# Select your ESC type
# Supported values as of today:
# xesc_mini: for the STM32 version (VESC)
# xesc_2040: for the RP2040 version (very experimental!)
export OM_MOWER_ESC_TYPE="xesc_mini"

# Select your gamepad
# Currently supported: ps3, xbox360
export OM_MOWER_GAMEPAD="xbox360"

# Set to true to record your session.
# Output will be stored in your $HOME
# export OM_ENABLE_RECORDING_ALL=False

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

# If OM_USE_RELATIVE_POSITION is set to False, uncomment and set to coordinates near you, around to docking station
# This will be your map origin!
# export OM_DATUM_LAT=99.CHANGEME
# export OM_DATUM_LONG=11.CHANGEME

# NTRIP Settings
# Set to False if using external radio plugged into the Ardusimple board.
export OM_USE_NTRIP=True
export OM_NTRIP_HOSTNAME=192.168.178.55
export OM_NTRIP_PORT=2101
export OM_NTRIP_USER=gps
export OM_NTRIP_PASSWORD=gps
export OM_NTRIP_ENDPOINT=BASE1

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
```
{{< /spoiler >}}

## Step 3: Done :tada:
You can now remove the SD card from your PC, it is ready to be used with the Open Mower software.
