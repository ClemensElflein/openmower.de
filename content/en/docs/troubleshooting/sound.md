---
title: Troubleshoot Sound
linkTitle: Sound
tags: [dfplayer, sound]
---

### All sounds get played infinite

This is most likely because your OpenMower's mainboard miss R7 and/or R13. See [DFPlayer Module](../../robot-assembly/prepare-the-parts/prepare-sound/#dfplayer-module).

But also happen if you use an old or damaged SD-Card which take loooong for getting the file allocation table.


### Howto increase or decrease volume?

This depend on the type and version of your CoverUI:

| Volume | Custom CoverUI V1<br>Stock C500(A/B) | Custom CoverUI V2<br>&nbsp; | RM-ECOW-V1.0.0<br>(NX80i, ...) | RM-EC3-V1.1<br>(NX100i) | SA/SC-Pro<br>(240*160 Pixel) |
|------|:--------:|:----:|:----:|:---:|:---:|
| up   | <kbd>Mon</kbd> | <kbd>Sun</kbd> | <kbd>4H</kbd> | <kbd>1</kbd> | <kbd>↑</kbd> |
| down | <kbd>Tue</kbd> | <kbd>Mon</kbd> | <kbd>6H</kbd> | <kbd>2</kbd> | <kbd>↓</kbd> |


### I decreased my volume via volume-down button, but sound get still played at full volume

This is a known issue with DFPlayer-Clones in mainboard version 0.9.x up (and incl.) 0.13.x. [Read here how to fix](http://localhost:1313/docs/robot-assembly/prepare-the-parts/prepare-sound/#dfplayer-module).

### I do hear one or two more adverts as before, but no GPS-Pings, no "Bidaa bidaa" emergency, ...

First off: "Bidaa bidaa" emergency signalling or similar, is an optional 'background-sound' feature, which is disabled by default.
You need to enable it via `export OM_BACKGROUND_SOUNDS=True` in your mower_config.

If it still doesn't play after changing `export OM_BACKGROUND_SOUNDS=True` in your mower_config, this is most likely because your DFPlayer's SD-Card is still in the old format. See [Sound SD-Card](../../robot-assembly/prepare-the-parts/prepare-sound/#sound-sd-card),


### I do hear some new sounds, but they do not match to what happen

You mixed up DFPlayer's SD-Card by adding the new files on top of the old ones. You need to remove all old files before copying the new ones. See [Sound SD-Card](../../robot-assembly/prepare-the-parts/prepare-sound/#sound-sd-card).


### Sound worked for a couple of weeks, but then my Pico suddenly died

This happen because you enabled full sound support by signalling it via `OM_DFP_IS_5V=True` flag, but didn't switched it in real. See [Change DFPlayer’s V<sub>CC</sub> to 5V](../../robot-assembly/prepare-the-parts/prepare-sound/#change-dfplayers-vsubccsub-to-5v).

Don't worry. A new Pico is cheap (~ 4$). Happy desoldering :no_mouth:!