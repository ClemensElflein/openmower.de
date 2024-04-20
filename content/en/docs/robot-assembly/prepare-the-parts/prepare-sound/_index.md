---
title: Sound (DFPlayer)
linkTitle: Sound
weight: 60
description: >
 Optional sound
tags: [dfplayer, sound, speaker, optional]
---

### DFPlayer Module

If your mainboard got delivered with an already equipped DFPlayer, you most likely got the original [DFRobot-DFPlayer](https://www.dfrobot.com/product-1121.html) with a 'DFRobot LISP3' chip.

If you need to attach one, and your're not located in the US, you might also use a DFPlayer-Clone with an 'MH2024K-24SS' or 'GD3200B' chip, as sold by Amazon, AliExpress or the like.

{{% alert title="☝️" color="info" %}}
You also need to take attention that your motherboard has the required R7 and R13 (1k) resistors assembled:<br>
<img title="Required 1kΩ R7 & R13" src="mainboard-013x-snd-r7-r13.png" width="200">
{{% /alert %}}

#### Change DFPlayer's V<sub>CC</sub> to 5V

All mainboard version &le; 0.13.x supply the DFPlayer with 3.3V by default.
But for full sound support, it's highly advised to change this to 5V, otherwise you might risk your Pico's PMIC 💣. More technical details here: [Sound-Readme](https://github.com/ClemensElflein/OpenMower/blob/main/Firmware/LowLevel/README-Sound%2C%20DFPIS5V.md)<br>
<img title="Required 1kΩ R7 & R13" src="mainboard-013x-snd-change5v.png" width="200">

Once changed, you're save to enable full sound support via `OM_DFP_IS_5V=True` [mower_config](../prepare-sd-card/#openmowermower_configtxt-on-linux-bootopenmowermower_configtxt) switch.


#### Sound SD-Card

{{% alert title="🧰" %}}
SDCard (128Mb) and DFPlayer Mini are included in the kit.
{{% /alert %}}

Take an SD card (different from the one you are using for RPi), format as FAT, copy [MP3 files](https://github.com/ClemensElflein/OpenMower/tree/main/Firmware/LowLevel/soundfiles) to the root folder. Insert SD card to DFPlayer. Insert DFPlayer into motherboard SD card facing right (towards RPi)

{{% alert title="☝️ Updated 5/2024 " color="info" %}}
The soundfile structure completely changed in May 2024.
If you already prepared your SD-Card before, it still works, but for full sound support you need to **replace** all files with the new structure.
{{% /alert %}}

#### Speaker mount

There're a couple of 3D-Printable speaker mounts available for different models. Worth to check [OpenMower @ Printables](https://www.printables.com/search/models?q=tag:openmower%20speaker)
