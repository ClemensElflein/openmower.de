---
title: Troubleshooting GPS-RTK
linkTitle: GPS-RTK
tags: [gps, gps-rtk, simplertk2b, zed-f9p, ntrip]
resources:
    - src: "**.png"
---

We assume that you at least followed [documentation of GPS setup]({{< relref "/docs/robot-assembly/prepare-the-parts/prepare-the-gps" >}}). If mower is already assembled - open the top cover.

Get your Windows PC and connect to GPS module directly with microUSB cable (as if you were uploading the configuration). 

Make sure that `Protocol of received messages` in bottom status bar right shows `UBX`, not `NMEA`. If not - upload configuration again. Then disconnect/connect power of GPS and make sure it stayed `UBX`.

Connect the antenna to the board and go outside to check if general GPS is working. If the mower is already assembled and an antenna is plugged in - just take it outside with the mower.
Even indoors next to the windows with antenna connected, you should see satellites and other info start appearing in u-center. In few minutes `GPS Fix` led will start blinking on GPS board.

Deviation map (`View->Deviation Map, F12`) should stay in a ~1m, that what you expect from average GPS. If you got some existing garbage there already, clean it via `File->Database clean`.

Now let's connect NTRIP. We assume that you either found a suitable [NTRIP node somewhere nearby](https://discord.com/channels/958476543846412329/980099128879108137/980100319700742145) (<30km) or running your own [base station]({{< relref "/docs/rtk-base-setup" >}}).

Go to `Receiver->NTRIP Client...` and configure your NTRIP settings. This will be the same settings that you will use in [configuration file later]({{< relref "/docs/robot-assembly/prepare-the-parts/prepare-sd-card#openmowermower_configtxt-on-linux-bootopenmowermower_configtxt">}}).
{{< imgproc ntrip-client Resize 500x />}}

NTRIP client should display green connection in the status bar. Deviation map (`View->Deviation Map, F12`) should stay dead center. `No RTK` led will start blinking or go away completely.
{{< imgproc gps-fix-and-deviation Resize 800x />}}


## Test GPS on Mainboard

We have checked that GPS works alone, let's see if it would together with mainboard. Plug GPS into mainboard. Everything should light up and start flashing. Wait until you are GREEN or RED/GREEN.

{{% alert title="🔋 Powering the mainboard" color="info" %}}
If you don't have dock station assembled and want to save the power in the main mower battery, you can power it from the Pico Dev board MicroUSB port, right below the GPS board. Use a 1A+ power bank, because computer USB port's 500mA might be not enough.
{{% /alert %}}

Then SSH into OpenMower console. In the home directory there's do `./start_ros_bash.sh` which should take you to a bash inside the docker, then you can do `rostopic list` to list all topics and `rostopic echo -c -w 5  /xbot_driver_gps/xb_pose` to look at the GPS data. There's a position and some accuracy number in meters.

```yaml
header:
  seq:   318
  frame_id: "gps"
orientation_valid: 0
motion_vector_valid: 1
position_accuracy: 0.021  # this is good
orientation_accuracy: 3.141
```
