---
title: Hardware Versions / Known Issues
linkTitle: Hardware Versions
weight: 200
description: >
  Version History, Release Notes and Known Errors
resources:
  - src: "**.jpg"

---
{{< toc >}}

## 0.13.0 - Red
{{< imgproc 0_13_b Fill "400x400 q99" />}}
{{< imgproc 0_13_a Fill "400x400 q99" />}}

#### Notable changes:
 * Custom CoverUI added to the kit
 * Dropped support for dfPlayer sound module 

#### Known issues:
 * The first batch of 0.13 boards was mistakenly labeled "latest". No action needed.
 * [Outdated Firmware]({{< relref "/docs/versions/errata/outdated-firmware" >}}). Affect kits shipped pre-May'23.
 * [IC2 chip is wrong]({{< relref "/docs/versions/errata/ic2-is-wrong" >}}). Affect kits shipped pre-May'23.
 * [rain sensor cable is female, but needs to be male]({{< relref "/docs/versions/errata/wrong-rain-sensor-cable" >}}). Affect kits shipped pre-May'23.


## 0.12.0 - Black
{{< imgproc 0_12_x Resize "400x q99" />}}

#### Notable changes:
 * IMU: LSM6DSO instead of WT901

#### Known issues:
 * SPI tracks from Pico were misplaced, already fixed in firmware. No action needed.
 * [Outdated Firmware]({{< relref "/docs/versions/errata/outdated-firmware" >}})
 * [IC2 chip is wrong]({{< relref "/docs/versions/errata/ic2-is-wrong" >}})
 * [rain sensor cable is female, but needs to be male]({{< relref "wrong-rain-sensor-cable" >}})

## 0.11.0 - Purple
{{< imgproc 0_11_x Resize "400x q99" />}}

#### Notable changes:
 * Connected WT901 via I2C freeing pins for dfPlayer
 * Upgraded dock station PCB with extra holes and terminals (red)

#### Known issues:
* [IC2 chip is wrong]({{< relref "/docs/versions/errata/ic2-is-wrong" >}})

## 0.10.0 - Green
{{< imgproc 0_10_x Resize "400x q99" />}}

#### Notable changes:
 * Added dock station PCB (green)

#### Known issues:
* [IC2 chip is wrong]({{< relref "/docs/versions/errata/ic2-is-wrong" >}})

## 0.9.3 - Also Green
{{< imgproc 0_9_3 Resize "400x q99" />}}
{{< imgproc 0_9_3_gps Resize "400x q99" />}}

First build. Experimental xESC2040 instead of xESC-mini (STM32).
