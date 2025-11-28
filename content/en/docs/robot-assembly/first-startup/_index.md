---
title: "First Startup"
linkTitle: "First Startup"
weight: 30
description: Start the robot
---

Congratulations that you have made it this far. Now comes the fun part — starting it all up!


{{% alert title="Warning" color="warning" %}}
If you see / smell anything unexpected, turn the switch off **immediately!**

This includes but is not limited to:
- Smoke / Fire
- Smell of hot electronics
- Blown Fuses
  {{% /alert %}}


It's time to power the robot up by hitting the switch at the back of the robot.

Once turned on, the RGB LED on your mainboard should go through some colors starting with RED and ending with RED - ORANGE blinking.

This shows that the mower is in emergency mode and that ROS is not connected to the mainboard.

**This is expected because our Raspberry Pi has no OpenMower software yet, just the basic operating system**.


{{% alert title="Warning" color="warning" %}}
Don't run the mower for too long, you **cannot recharge it with the unmodified docking station!**
{{% /alert %}}

If everything seems healthy, **turn off the mower** and proceed to the next section: [TODO]().
Otherwise, refer to [Troubleshooting]({{% relref "/docs/troubleshooting/" %}}).
