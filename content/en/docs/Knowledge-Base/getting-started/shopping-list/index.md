---
title: "Shopping List"
linkTitle: "Shopping List"
weight: 20
description: "Plan the parts and costs for an OpenMower conversion: mower, electronics, compute module, GPS receiver, antennas, and RTK base station options."
---

_If you make a purchase through the links marked with an Asterisk (*), I may earn a small commission at no extra cost to you. Thank you for supporting this project!_

{{% alert title="Warning" color="warning" %}}
Read this first: [Important Info]({{% relref "/docs/getting-started#important-warnings" %}})
{{% /alert %}}


## Plan the total build cost

The getting-started guide's approximately €700 figure is an earlier planning estimate for the conversion, excluding the mower and RTK base station. It is not a current supplier quote. Hardware revision, receiver choice, shipping, and taxes can change the total; price the parts below for your exact mower before buying.

Include these items in your budget:

- A compatible mower and any necessary battery, motor, or chassis repairs.
- The OpenMower hardware kit and compute module; confirm what the kit includes to avoid buying parts twice.
- A rover GPS receiver, antenna, cables, mounts, and storage where needed.
- Either a local base station with receiver, antenna, power, and mounting, or access to a suitable correction service. Check service coverage and fees.
- Tools, connectors, weatherproofing, delivery charges, and taxes.

Check the [compatibility list]({{% relref "/docs/knowledge-base/getting-started/compatible-mowers" %}}) and read the [build guide]({{% relref "/docs/step-by-step" %}}) before ordering.

## Parts for the Robot and the Charging Station

| Name                                    | Description                                                                                                                       | Quantity Required | Source Link                                                                                                                                                                                     | Notes                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mower<br>(YardForce Classic 500(B))     | The mower to modify.                                                                                                              | 1                 | [Amazon*](https://amzn.to/3NWgIxk)                                                                                                                                                              | Check the [Compatible Mowers]({{% relref "/docs/knowledge-base/getting-started/compatible-mowers" %}})                                                                                                                                                                                                                                                                                                  |
| Open Mower Hardware Kit                 | The electronics we will mount inside the robot. Consists of the mainboard (includes LiPo charger), xCore board, and 3x ESC.     | 1                 | Contact @Apehaenger on Discord, he has Hardware available (see [Announcement]({{% relref "/updates" %}})) | Alternatively you can source and solder most of these parts yourself. Check the repositories in the Links section for PCB designs and BOMs.                                                                                                                                                                                                                                             |
| Ardusimple RTK2B GPS + Antenna          | Positioning system for the robot                                                                                                  | 1                 | [ArduSimple](https://www.ardusimple.com/product/simplertk2b-basic-starter-kit-ip65/)                                                                                                            | Some users use UM9XX chips (available from [WitMotion](https://witmotion-sensor.com/products/rtk-gps-gnss-modules-centimeter-level-um982-um980-um960) and [AliExpress](https://aliexpress.com/item/1005007177629130.html)) as alternative. Compared to ArduSimple, they're a bit cheaper and support triple-band frequencies. |
| Raspberry Pi Compute Module 4 with WiFi | The brain of the robot.<br><br>RAM: 2GB+ for running the software<br>4GB+ for development<br><br> 16GB+ storage (eMMC or µSD Card)| 1                 | [RPi Locator](https://rpilocator.com/?cat=CM4&instock)                                                                                                                                          | Must plug into the xCore board — CM4 and CM5 are supported. Other CM-compatible boards may work but the pre-made OS image won't.                                                                                                                                                                                                                                                                                 |
| µSD Card                                | Only for RPi CM4 Lite. The absolute minimum capacity you should buy is 16GB. But better buy a 32GB one                            | 1                 | [Amazon*](https://amzn.to/3EeWBXj) or your local hardware store                                                                                                                                 |                                                                                                                                                                                                                                                                |
| **Optional:**                           | **Optional:**                                                                                                                     |                   |                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                         |
| USB Wi-Fi Dongle                        | For better Wi-Fi reception                                                                                                        | 0                 |                                                                                                                                                                                                 | Check for Linux Support                                                                                                                                                                                                                                                                                                                                                                 |
| Left-Angle USB adapter                  | If you want to keep Wi-Fi dongle inside the mower. RPi USB is really close to the mower side wall                                 | 0                 | [Amazon*](https://amzn.to/3ukNAIj) or your local hardware store                                                                                                                                 | The kit contains the wire to connect external USB port. That may be enough if Wi-Fi dongle is waterproof.                                                                                                                                                                                                                                                                               |


## Parts for the GPS Base Station

{{% alert title="Info" color="info" %}}
You only need a GPS base station if you don't have access to an external NTRIP service. There are multiple free services available, so check before buying this.
{{% /alert %}}

| Name                                        | Description                                                               | Quantity Required | Source Link                                                                          | Notes     |
| ------------------------------------------- | ------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------ | --------- |
| Raspberry Pi<br>+ SD Card<br>+ Power Supply | You can basically use any Raspberry Pi for this. No special requirements. | 1                 | [e.g. Raspberry Pi 4](https://amzn.to/4a904YP)                                       |           |
| Ardusimple RTK2B GPS + Antenna              | Positioning system for the base station                                   | 1                 | [ArduSimple](https://www.ardusimple.com/product/simplertk2b-basic-starter-kit-ip65/) | See above |

For the setup check the [GPS Base Setup Guide]({{% relref "/docs/knowledge-base/gps/rtk-base-setup" %}})
