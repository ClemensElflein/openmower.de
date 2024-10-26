---
title: "Shopping List"
linkTitle: "Shopping List"
date: 2022-11-17
description: >
  A shopping list for your Open Mower build.	
---

{{% alert title="Warning" color="warning" %}}
Read this first: [Important Info](/docs/getting-started/#important-info)
{{% /alert %}}


## Parts for the Robot and the Charging Station

| Name                               | Description                                                                                                                   | Quantity Required | Source Link                                                                          | Notes                                                                                                                                      |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Mower<br />(YardForce Classic 500 or 500B) | The mower to modify.                                                                                                          | 1                 | [Amazon](https://amzn.to/3NWgIxk)                                                    |                                                                                                                                            |
| Open Mower Hardware Kit            | The electronics we will mount inside the robot and the charging station. Also includes goodies to make stuff easier to mount. | 1                 | [Vermut's shop](https://shop.devops.care/10-openmower)                               | Alternatively you can source and solder most of these parts yourself. Check the repositories in the Links section for PCB designs and BOMs. |
| Ardusimple RTK2B GPS + Antenna     | Positioning system for the robot                                                                                              | 1                 | [ArduSimple](https://www.ardusimple.com/product/simplertk2b-basic-starter-kit-ip65/) |                                                                                                                                            |
| Raspberry Pi 4                     | The brain of the robot.<br /><br />Use 2GB + model for running the software<br /><br />Use 8GB model for development          | 1                 | [RPi Locator](https://rpilocator.com/?cat=PI4&instock)                               | Yes, it has to be the Raspberry Pi 4, because we need all the UARTs.                                                                       |
| SD Card (16 GB+)                   |                                                                                                                               | 1                 | [Amazon](https://amzn.to/3EeWBXj) or your local hardware store                       |                                                                                                                                            |
| USB Wi-Fi Dongle (Optional)         | For better Wi-Fi reception                                                                                                     | 0                 |                                                                                      | Check for Linux Support                                                                                                                    |
| Left-Angle USB adapter (Optional)  | If you want to keep Wi-Fi dongle inside the mower. RPi USB is really close to the mower side wall                              | 0                 | [Amazon](https://amzn.to/3ukNAIj) or your local hardware store                       | The kit contains the wire to connect external USB port. That may be enough if Wi-Fi dongle is waterproof.                             |


## Parts for the GPS Base Station

{{% alert title="Info" color="info" %}}
You only need a GPS base station if you don't have access to an external NTRIP service. There are multiple free services available, so check before buying this.
{{% /alert %}}

| Name                                            | Description                                                               | Quantity Required | Source Link                                                            | Notes |
|-------------------------------------------------|---------------------------------------------------------------------------|-------------------|------------------------------------------------------------------------|-------|
| Raspberry Pi<br />+ SD Card<br />+ Power Supply | You can basically use any Raspberry Pi for this. No special requirements. | 1                 | [RPi Locator](https://rpilocator.com/?cat=PI4&instock)                                |       |
| Ardusimple RTK2B GPS + Antenna                  | Positioning system for the base station                                   | 1                 | [ArduSimple](https://www.ardusimple.com/product/simplertk2b-basic-starter-kit-ip65/) |       |
