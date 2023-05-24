---
title: Version history
linkTitle: Versions
weight: 200
description: >
  Version history, release notes and known errors
resources:
  - src: "**.jpg"

---

# 0.13.0 - Red
The first batch was mistakenly labeled "latest."
{{< imgproc 0_13_a Resize "400x q99" />}}

#### Notable changes:
 * Custom CoverUI added to the kit
 * Dropped support for dfPlayer sound module 

#### Known issues:
 * [outdated firmware]({{< relref "/docs/Knowledge-Base/issues/outdated-firmware" >}})
 * [IC2 chip is wrong]({{< relref "/docs/Knowledge-Base/issues/ic2-is-wrong" >}})
 * [rain sensor cable is female, but needs to be male]({{< relref "/docs/Knowledge-Base/issues/wrong-rain-sensor-cable" >}}) (fixed in batch #6)


# 0.12.0 - Black
{{< imgproc 0_12_x Resize "400x q99" />}}

#### Notable changes:
 * IMU: LSM6DSO instead of WT901

#### Known issues:
 * SPI tracks from Pico were misplaced, fixed in firmware.
* [outdated firmware]({{< relref "outdated-firmware" >}})
* [IC2 chip is wrong]({{< relref "outdated-firmware" >}})
* [rain sensor cable is female, but needs to be male]({{< relref "wrong-rain-sensor-cable" >}})

# 0.11.0 - Purple
{{< imgproc 0_11_x Resize "400x q99" />}}

#### Notable changes:
 * Connected WT901 via I2C freeing pins for dfPlayer
 * Upgraded dock station PCB with extra holes and terminals (red)

# 0.10.0 - Green
{{< imgproc 0_10_x Resize "400x q99" />}}

#### Notable changes:
 * Added dock station PCB (green)

# 0.9.3 - Also Green
First build. Experimental xESC2040 instead of xESC-mini (STM32). 
