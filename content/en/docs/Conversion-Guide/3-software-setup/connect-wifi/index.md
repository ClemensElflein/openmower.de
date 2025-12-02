---
title: "Step 3.1: Connect WiFi"
linkTitle: "Connect WiFi"
weight: 10
description: >
  Connect the mower to WiFi.
---


## Step 3.0: Ensure the Robot has Power
Make sure that the Robot does not drain the battery, it probably will be empty until your setup is finished.
Usually this can be done by putting it into the docking station (except for the Universal board).


## Step 3.1: Search the Hotspot
<div class="container-fluid m-0 p-0">
<div class="row">
<div class="col">
With the mower turned on, use your mobile device and scan for WiFi networks.
OpenMowerOS will automatically create a hotspot with the name `OpenMower-<Some Number>`. Connect to this hotspot.

If your mobile device complains that the network does not have internet connectivity, tell it to use it anyway.
</div>
<div class="col-3">

![connect_wifi_screen_1.png](images/connect_wifi_screen_1.png)

</div>
</div>
</div>

## Step 3.2: Open a browser to the configuration page.
<div class="container-fluid m-0 p-0">
<div class="row">
<div class="col">
Some devices will detect that the hotspot does not provide internet connectivity and will send you to a configuration page.

If your device does not do this, open the browser on your phone and navigate to: [http://10.41.0.1/](http://10.41.0.1/).
</div>
<div class="col-3">

![connect_wifi_screen_1.png](images/connect_wifi_screen_1.png)

</div>
</div>
</div>

### Step 3.3: Enter your WiFi Credentials
Once on the configuration page, select your home Wi-Fi connection and enter your password. Then click connect.

The OpenMower WiFi should disappear and the robot will connect to your home network.


### Step 3.4: Check Connection
Let's do some sanity checks, if the mower has powered on successfully.
- Check the connection by using any other PC in your network and `ping openmower.local`. This should be working. Alternatively, you can check if the device is connected by logging into your router.
- Check, if you can reach the mower via SSH (`ssh openmower@openmower.local`, password `openmower`).
- Check, if you can reach the mower's terminal in a browser. Navigate to [http://openmower.local:7681/](http://openmower.local:7681/)

