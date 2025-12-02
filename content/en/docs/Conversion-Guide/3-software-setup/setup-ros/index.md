---
title: "Step 3.3: Configure ROS"
linkTitle: "Configure ROS"
weight: 30
description: >
  Configure the ROS system, so that it knows on which mower model it is running.
---


## Step 3.3.1: Configure ROS Parameters
The ROS parameters can be configured using similar to the environment above.
Simply run the `openmower configure ros` command and set the parameters as needed.

For a first setup, you can leave the default values for most parameters.

**You need to set the following parameters:**
- **gps/baud_rate**: The baud rate of the GPS module. If you are using the Ardusimple GPS with the provided configuration file, leave it at 921600.
- **gps/protocol**: The GPS protocol used. If you are using the Ardusimple GPS with the provided configuration file, leave it at "UBX".
- **gps/datum_lat, gps/datum_long**: Use coordinates close to where you will setup your docking station. **Tip:** Open [Google Maps](https://maps.google.com/) and right-click on any location to get the coordinates. It should be within a few meters of the dock, no need to be ultra precise here.
- __ntrip_client/\*__: Set the NTRIP parameters for your GPS base station.


<div class="container pb-3 pt-3">
<div class="row justify-content-md-center">
<div id="step-3-2-3-player" class=""></div>
</div>
<div class="row justify-content-md-center">
<div>Example ROS configuration.</div>
</div>
</div>
<script>
    AsciinemaPlayer.create(
        'cast/openmower-configure-ros.cast',
        document.getElementById('step-3-2-3-player'),
        { cols: 130, rows: 30, autoplay: false, loop: true }
    );
</script>