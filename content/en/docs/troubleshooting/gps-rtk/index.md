---
title: Troubleshooting GPS-RTK
linkTitle: GPS-RTK
tags: [gps, gps-rtk, simplertk2b, zed-f9p, ntrip]
resources:
    - src: "**.png"
---

We assume that you at least followed [documentation of GPS setup]({{< relref "/docs/step-by-step/2-robot-modification/prepare-the-parts/prepare-the-gps" >}}). If mower is already assembled - open the top cover.

Get your Windows PC and connect to GPS module directly with microUSB cable (as if you were uploading the configuration). 

Make sure that `Protocol of received messages` in bottom status bar right shows `UBX`, not `NMEA`. If not - upload configuration again. Then disconnect/connect power of GPS and make sure it stayed `UBX`.

Connect the antenna to the board and go outside to check if general GPS is working. If the mower is already assembled and an antenna is plugged in - just take it outside with the mower.
Even indoors next to the windows with antenna connected, you should see satellites and other info start appearing in u-center. In few minutes `GPS Fix` led will start blinking on GPS board.

Deviation map (`View -> Deviation Map, F12`) should stay in a ~1m, that what you expect from average GPS. If you got some existing garbage there already, clean it via `File -> Database clean`.

Now let's connect NTRIP. We assume that you either found a suitable [NTRIP node somewhere nearby](https://discord.com/channels/958476543846412329/980099128879108137/980100319700742145) (<30km) or running your own [base station]({{< relref "/docs/Knowledge-Base/rtk-base-setup" >}}).

Go to `Receiver -> NTRIP Client...` and configure your NTRIP settings. This will be the same settings that you will use in the ROS configuration file later.
{{< imgproc ntrip-client Resize 500x />}}

NTRIP client should display green connection in the status bar. Deviation map (`View -> Deviation Map, F12`) should stay dead center. `No RTK` led will start blinking or go away completely.
{{< imgproc gps-fix-and-deviation Resize 800x />}}


## Test GPS on Mainboard

We have checked that GPS works alone, let's see if it would together with the mainboard. Plug the GPS into the mainboard. Everything should light up and start flashing.  
Wait until the LED lights up GREEN or GREEN/RED.

{{% alert title="🔋 Powering the mainboard" color="info" %}}
If you don't have dock station assembled and want to save the power in the main mower battery, you can power it from the Pico Dev board MicroUSB port, right below the GPS board. Use a 1A+ power bank, because computer USB port's 500mA might be not enough.
{{% /alert %}}

{{< tabpane text=true >}}
{{% tab header="**OpenMowerOS version**:" disabled=true /%}}
{{% tab header="0.1.0" %}}
Then SSH into your OpenMower.  
In the home directory (`~/`) there is a scripts called `start_ros_bash.sh`.  
Run the `start_ros_bash.sh` script by executing `~/start_ros_bash.sh` which should take you to a bash inside the container.
{{% /tab %}}
{{< /tabpane >}}

There you can run `rostopic list` to list all topics and `rostopic echo --clear -w 5  /ll/position/gps` to look at the GPS data.  
You will get some lines of data:

```yaml
header:
  seq:    44
  stamp:
    secs: 1708328554
    nsecs: 51810942
  frame_id: "gps"
sensor_stamp: 114172000
received_stamp: 1711341013
source:     1
flags:     3
orientation_valid:     0
motion_vector_valid:     1
position_accuracy: 0.024
orientation_accuracy: 3.141
pose:
  pose:
    position:
      x: 1.975
      y: 4.819
      z: 114.9
    orientation:
      x: 0.000
      y: 0.000
      z: 0.201
      w: 0.979
  covariance: [88.21, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 88.21, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 88.21, 0.000, 0.000, 0.000, 0.000, 0.000, 10000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 10000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 9.869]
motion_vector:
  x: 0.045
  y: -0.05
  z: -0.01
vehicle_heading: 1.570
motion_heading: 0.405
---
```

The important lines here are:

- `flags:     3`  
    you want a `3` here since that means your rtk state is "fixed"  
    `3` is "fix", `5` is "float" and `0` is "single" (classic non-rtk GNSS gps only)

<br>

- `position_accuracy: 0.024`  
  this value is in meters so the example has a accuracy of ~2,5cm and that is great.  
  It can be the case that this value is ok but the rtk state is not yet "fixed"
