---
title: "SABO / John Deere"
linkTitle: "SABO / John Deere"
weight: 20
description: >
  Modification Guide for SABO MOWiT 500F / John Deere Tango E5
---

## Prerequisites

### Things you will need:
- **SABO MOWiT 500F or John Deere Tango E5**
- **Open Mower V2 Carrier Board for SABO** with all modules installed (xCore, CM4, GPS, 3x ESCs)

{{< image-gallery gallery_dir="images/prerequisites" >}}

### Tools you will need:
- **M10 ratchet** for the cover
- **5mm Allen key** for the blade
- **Torx T30** for the mainboard mount/holder
- **Torx T20** for the mainboard

## Step 2.4.1: Open the mower and remove the OEM mainboard 🔓

1. Place the mower on its back and remove the six 10 mm screws from the housing.
2. Remove the blade with the 5mm Allen key (right‑hand thread). Use gloves and secure the blade while loosening.
3. Hold the housing together with both hands and place the mower back on its wheels.
4. Slightly open the cover on the handle (rear) side by a few centimeters.
5. Using a flashlight, disconnect the display ribbon cable(s):
   - Series‑I: two ribbon cables going to the CoverUI. Each plug has small side locks; press to release, then unplug from the mainboard.
   - Series‑II: one ribbon cable; pull it straight out from the mainboard (no release locks).
6. You can now open the cover further. A single cable from the cover’s charging contacts goes toward the mainboard. Before the mainboard there is a 2‑pin Molex plug; press to unlock and disconnect it. Put the cover aside for later modification and reassembly.
7. Disconnect all remaining cables from the OEM mainboard. Many plugs have a latch; press to release before pulling.
8. The OEM mainboard is mounted on a black plastic mainboard holder. On its back side are two larger Torx T30 screws. Remove them to lift out the mainboard together with the holder.
9. Remove the OEM mainboard from the holder by unscrewing the Torx T20 screws.

{{< image-gallery gallery_dir="images/disassemble-mower" >}}

## Step 2.4.2: Mount prepared parts

Assemble the previously [prepared parts]({{% relref "/docs/step-by-step/2-robot-modification/prepare-the-parts" %}}):

1. Mount your prepared UM9x GPS module to the carrier board and attach the IPEX/SMA cable (usually included with the UM9x) as shown:<br>
  ![UM9x IPEX/SMA cable](images/UM9x-IPEX-SMA-Cable.jpg)
2. Mount your xCore + CM4 (+ optional heatsink) combo to the carrier board (if not already mounted)

## Step 2.4.3 (optional): Install Wi‑Fi adhesive antenna 📶

The Wi‑Fi adhesive antenna can be placed as shown:

{{< image-gallery gallery_dir="images/wifi-adhesive-antenna" >}}


## Step 2.4.4: Assemble carrier board with mainboard 🔩

1. Now that all modules are prepared and mounted, fasten the carrier board to the mainboard holder.<br>
   **If you have fewer screws than holes, prioritize holes close to the larger connectors!**
2. Mount the carrier board + mainboard-holder back into the mower and fasten it with the two T30 screws.
3. Carefully connect all plugs. Some plugs fit into multiple counterparts, verify the labels or use this plug overview:<br>
  
   |                    Series-I Plugs                     |                    Series-II Plugs                     |
   | :---------------------------------------------------: | :----------------------------------------------------: |
   | ![Series-I Plugs](images/om-sabo-cb-s1-v02-plugs.jpg) | ![Series-II Plugs](images/om-sabo-cb-s2-v02-plugs.jpg) |

   Note: some plugs are rotated — do not force any connector!


## Step 2.4.5: Install GPS antenna (e.g. HA/HX‑901) on the cover 🛰️

An alternative non-destructive internal holder was [designed by STS](https://discord.com/channels/958476543846412329/1355300774523174922/1426287736356077808). Check the Discord discussion for more details and STL files if available.

1. Drill a 6.5–7 mm hole in the cover approximately at the position as shown in the images.
1. Install the (included) 30-40cm SMA extension cable. Ensure the SMA bulkhead protrudes far enough so the HA/HX‑901 can fully engage and make good contact; if in doubt, omit one washer/spacer on the inside to gain thread length.<br>
  Seal it from the top with silicone or a similar sealant. Don’t use too much sealant, so the HA/HX‑901 can still be screwed on later.
1. Also seal the inside thoroughly to prevent any water ingress. On the inside use sealant rule: *More is better*
1. Allow sufficient time for the sealant to cure before proceeding.

{{< image-gallery gallery_dir="images/gps-antenna" >}}


## Step 2.4.6: Close the housing ✅

1. Place the cover back onto the mower. Let the front engage slightly, but keep the rear open enough to:
   1. Connect the GPS antenna cable to the carrier board
   1. Reconnect the docking‑contact cable
   1. Finally, reconnect the CoverUI ribbon cable(s)
1. Close the cover completely so it fits and latches evenly all around
1. Hold the housing together with both hands and turn the mower back onto its back
1. Reinstall and fasten the six 10 mm hex‑head screws
1. **Do not install the blade yet**
1. Put the mower back on its wheels
1. Finally, screw the HA/HX‑901 antenna onto the cover

## Step 2.4.7: First Startup

It's time to power the robot up by hitting the switch at the back of the robot.

{{% alert title="Warning" color="warning" %}}
If you see / smell anything unexpected, turn the switch off **immediately!**

This includes but is not limited to:
- Smoke / Fire
- Smell of hot electronics
- Blown Fuses
  {{% /alert %}}


Once turned on, it will take approximately 10 seconds before the LEDs and LCD start to show signs of life.
**Keep the robot turned on for at least five minutes to make sure the CM4 boots up properly. It performs setup during the first boot.**

{{% alert title="Info" color="info" %}}
It's a good idea to place the mower into the docking station, so that the battery doesn't drain and can charge.
{{% /alert %}}

If everything seems healthy, proceed to the [Software Setup]({{< relref "/docs/step-by-step/3-software-setup" >}}).

Otherwise, **stop here and ask for help on the Discord server**.
