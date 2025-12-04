---
title: "Shopping List"
linkTitle: "Shopping List"
description: >
  A shopping list for your Open Mower build.	
---

_If you make a purchase through the links marked with an Asterisk (*), I may earn a small commission at no extra cost to you. Thank you for supporting this project!_

{{% alert title="Warning" color="warning" %}}
Read this first: [Important Info]({{% relref "/docs/getting-started/#important-info" %}})
{{% /alert %}}


## Parts for the Robot and the Charging Station

| Name                               | Description                                                                                                                   | Quantity Required | Source Link                                                                                                                                                                                     | Notes                                                                                                                                      |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Mower<br>(YardForce Classic 500(B)) | The mower to modify.                                                                                                         | 1                 | [Amazon*](https://amzn.to/3NWgIxk)                                                                                                                                                              | Check the [Compatible Mowers]({{% relref "/docs/knowledge-base/compatible-mowers" %}})                                                                     |
| Open Mower Hardware Kit            | The electronics we will mount inside the robot and the charging station. Also includes goodies to make stuff easier to mount. | 1                 | <b>Version 2 Hardware:</b><br/> (see [Announcement]({{% relref "/updates" %}}))<br/>Contact @Apehaenger on Discord, he has Hardware available<br/><br/><b>Version 1 Hardware:</b><br/>[Vermut's shop](https://shop.devops.care/10-openmower) | Alternatively you can source and solder most of these parts yourself. Check the repositories in the Links section for PCB designs and BOMs. |
| Ardusimple RTK2B GPS + Antenna     | Positioning system for the robot                                                                                              | 1                 | [ArduSimple](https://www.ardusimple.com/product/simplertk2b-basic-starter-kit-ip65/)                                                                                                            | Some users use [UM9XX chips](https://wiki.openmower.de/index.php?title=Unicore_GPS_modules) (available from [WitMotion](https://witmotion-sensor.com/products/rtk-gps-gnss-modules-centimeter-level-um982-um980-um960) and [AliExpress](https://aliexpress.com/item/1005007177629130.html)) as alternative. Compared to ArduSimple, they're a bit cheaper and support triple-band frequencies.|
| Raspberry Pi 4                     | The brain of the robot.<br><br>RAM: 2GB+ for running the software<br>4GB+ for development                                     | 1                 | [RPi Locator](https://rpilocator.com/?cat=PI4&instock)                                                                                                                                          | Yes, it has to be the Raspberry Pi 4, because we need all the UARTs.                                                                       |
| µSD Card                           | The absolute minimum capacity you should buy is 16GB. But better buy a 32GB one                                               | 1                 | [Amazon*](https://amzn.to/3EeWBXj) or your local hardware store                                                                                                                                 | A Gucci option would be a [RasPiKey](https://www.uugear.com/product/raspikey-plug-and-play-emmc-module-for-raspberry-pi/)                  |
| **Optional:**                      | **Optional:**                                                                                                                 |                   |                                                                                                                                                                                                 |                                                                                                                                            |
| USB Wi-Fi Dongle                   | For better Wi-Fi reception                                                                                                    | 0                 |                                                                                                                                                                                                 | Check for Linux Support                                                                                                                    |
| Left-Angle USB adapter             | If you want to keep Wi-Fi dongle inside the mower. RPi USB is really close to the mower side wall                             | 0                 | [Amazon*](https://amzn.to/3ukNAIj) or your local hardware store                                                                                                                                 | The kit contains the wire to connect external USB port. That may be enough if Wi-Fi dongle is waterproof.                                  |


## Parts for the GPS Base Station

{{% alert title="Info" color="info" %}}
You only need a GPS base station if you don't have access to an external NTRIP service. There are multiple free services available, so check before buying this.
{{% /alert %}}

| Name                                            | Description                                                               | Quantity Required | Source Link                                                                          | Notes |
|-------------------------------------------------|---------------------------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------|-------|
| Raspberry Pi<br>+ SD Card<br>+ Power Supply     | You can basically use any Raspberry Pi for this. No special requirements. | 1                 | [e.g. Raspberry Pi 4](https://amzn.to/4a904YP)                                       |       |
| Ardusimple RTK2B GPS + Antenna                  | Positioning system for the base station                                   | 1                 | [ArduSimple](https://www.ardusimple.com/product/simplertk2b-basic-starter-kit-ip65/) | See above |

For the setup check the [GPS Base Setup Guide]({{% relref "/docs/knowledge-base/rtk-base-setup" %}})
