---
title: Raspberry Pi 4
linkTitle: Raspberry Pi
description: >
    You don't get `RED/GREEN` or `GREEN`, webapp is not opening, cannot move mower via controller. We go step by step.
tags: [docker, rpi, raspberry, docker, ssh]
---

Follow the [SD Card preparation step]({{< relref "/docs/robot-assembly/prepare-the-parts/prepare-sd-card" >}}) and insert that card into Raspberry Pi 4, then, without plugging anywhere, power it from USB-C port.

Then follow the [Wifi Configuration]({{< relref "/docs/software-setup/configuring-wifi" >}}).

Board will connect to your Wi-Fi and will start downloading ~2Gb docker image which will definitely take some time.
While waiting, I recommend figuring out IP of the mower from router DHCP leases and opening SSH connection.


{{% alert title="🔑 Default SSH credentials" color="info" %}}
Username: `openmower`, password: `openmower`.
{{% /alert %}}


Running `sudo systemctl status --no-pager -l -n 99999 openmower` should display something reassuring.
{{< spoiler text="Click to see sample cold start startup log" id="openmower_status_log" >}}
```
● openmower.service - OpenMower service
     Loaded: loaded (/etc/systemd/system/openmower.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2022-12-11 17:38:46 GMT; 1min 56s ago
   Main PID: 1539 (start_open_mowe)
      Tasks: 9 (limit: 4164)
        CPU: 295ms
     CGroup: /system.slice/open-mower.service
             ├─1539 /bin/bash /root/start_open_mower.sh
             └─1540 docker pull ghcr.io/clemenselflein/open_mower_ros:releases-testing

Dec 11 17:39:58 openmower bash[1540]: 69ea1fadf775: Verifying Checksum
Dec 11 17:39:58 openmower bash[1540]: 69ea1fadf775: Download complete
Dec 11 17:40:00 openmower bash[1540]: 15e1b3c068e4: Verifying Checksum
Dec 11 17:40:00 openmower bash[1540]: 15e1b3c068e4: Download complete
Dec 11 17:40:01 openmower bash[1540]: 4f4fb700ef54: Verifying Checksum
Dec 11 17:40:01 openmower bash[1540]: 4f4fb700ef54: Download complete
Dec 11 17:40:38 openmower bash[1540]: ebf4cb1b6e8d: Verifying Checksum
Dec 11 17:40:38 openmower bash[1540]: ebf4cb1b6e8d: Download complete
Dec 11 17:40:48 openmower bash[1540]: 0acc91bc6454: Pull complete
Dec 11 17:40:48 openmower bash[1540]: c2b7ae792e5c: Pull complete
Dec 11 17:40:48 openmower bash[1540]: ffd8732fa33d: Pull complete
Dec 11 17:40:49 openmower bash[1540]: f77cf07a1833: Pull complete
Dec 11 17:40:49 openmower bash[1540]: c2e28204415f: Pull complete
Dec 11 17:40:50 openmower bash[1540]: d20c270f7c57: Pull complete
Dec 11 17:40:50 openmower bash[1540]: 88fa587d1506: Pull complete
Dec 11 17:40:50 openmower bash[1540]: cdca27d2d0cc: Pull complete
Dec 11 17:48:13 openmower bash[1540]: 67f58a6eff2a: Verifying Checksum
Dec 11 17:48:13 openmower bash[1540]: 67f58a6eff2a: Download complete
....
Dec 11 17:51:30 openmower bash[1540]: Digest: sha256:dafdce282bf6963a07dc391c2cc06119ac5a5ca5a9ecaac8b97204f81922635c
Dec 11 17:51:33 openmower bash[1540]: Status: Downloaded newer image for ghcr.io/clemenselflein/open_mower_ros:releases-testing
Dec 11 17:51:33 openmower bash[1540]: ghcr.io/clemenselflein/open_mower_ros:releases-testing
Dec 11 17:52:18 openmower bash[3156]: [48B blob data]
Dec 11 17:52:18 openmower bash[3156]: [62B blob data]
Dec 11 17:52:19 openmower bash[3156]: ... logging to /root/.ros/log/8ed2c83c-797c-11ed-a3ba-e45f0178e709/roslaunch-openmower-85.log
Dec 11 17:52:19 openmower bash[3156]: Checking log directory for disk usage. This may take a while.
Dec 11 17:52:19 openmower bash[3156]: Press Ctrl-C to interrupt
Dec 11 17:52:19 openmower bash[3156]: Done checking log file disk usage. Usage is <1GB.
Dec 11 17:52:19 openmower bash[3156]:
Dec 11 17:52:20 openmower bash[3156]: started roslaunch server http://openmower:39419/
Dec 11 17:52:20 openmower bash[3156]:
Dec 11 17:52:20 openmower bash[3156]: SUMMARY
....
bunch of PARAMETERS/NODES and view exception due to missing literally all the hardware
```
{{< /spoiler >}}

If you are lazy, just wait 5-10 minutes and check that http://\<openmower IP\>:8080/ is accessible. If it's not, you need to SSH and check the logs with `sudo journalctl -fu openmower`. Usually problem would be bad config file.

If you got to the webapp - you are good. Plug the Raspberry Pi back to mainboard.
