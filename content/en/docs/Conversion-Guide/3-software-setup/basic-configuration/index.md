---
title: "Step 3.2: Basic Configuration (Environment, Firmware Installation, xESC configuration)"
linkTitle: "Basic Configuration"
weight: 20
description: >
  Configure the environment, install firmware to the xCore board and configure your xESC motor controllers.
---

{{% toc %}}

## Overview:
### Types of settings
There are two parts to the robot configuration:
- **Environment Variables:** tell the system which mower model and hardware version you are using as well as which version of the ROS to use. **We will need to configure these first.**
- **ROS Parameters:** Configure the ROS runtime behavior. This includes GPS settings, mowing behavior, MQTT configuration for smart-home, etc.

### The `openmower` command line tool
We have created the `openmower` command line tool which helps you with all tasks related to running, configuring and debugging the OpenMower software stack.

The `openmower` tool is preinstalled on the OpenMowerOS and has the following features (and more):
- Edit ROS and Environment configuration files
- Install / Update Firmware on the xCore board
- Start / Stop the ROS software
- Show ROS logs
- Enter a ROS shell for debugging

### Accessing the terminal
You will need access to the terminal for all of the following steps.
You can either use SSH or the browser-based terminal.

SSH can be reached using the following credentials:
```
username: openmower
hostname: openmower
password: openmower
```

The browser based terminal does not need any credentials and can be reached at: [http://openmower:7681](http://openmower:7681)

## Step 3.2.0: Basic Checks

### Update the `openmower` tool to the latest version
To make sure you have the latest version of the `openmower` tool, you need to update it to the latest version.
The tool has an integrated update mechanism, so to update, you need to run:
```bash
sudo openmower update-self
```

Here is the expected output:
<div class="container pb-3">
<div class="row justify-content-md-center">
<div id="step-3-2-0-player" class=""></div>
</div>
<div class="row justify-content-md-center">
<div>Example output for a successful update.</div>
</div>
</div>
<script>
    AsciinemaPlayer.create(
        'cast/openmower-update-self.cast',
        document.getElementById('step-3-2-0-player'),
        { cols: 110, rows: 24, autoplay: false, loop: true }
    );
</script>


### Check, if filesystem expanded correctly
{{% alert title="Warning" color="warning" %}}
OpenMowerOS currently has an issue where sometimes the file system doesn't expand correctly.
You can see, if you have the problem by running `df -h /` and checking, if the `Use %` column is almost 100%.

![full-file-system.png](images/full-file-system.png)

{{% /alert %}}


**If your filesystem is almost full**, do the following steps to properly expand the filesystem:
- **Run** `sudo raspi-config`
- **Select** Advanced Options -> Expand Filesystem
- **Finish and Reboot**
- **Run** `df -h /` again, you should see the `Use %` column is now down to a low percentage (depending on your SD card size)

### Rename your host (optional)
If you are running multiple openmowers, it's a good idea to rename your host to distinguish between them.

This can easily be done in `raspi-config`:
- **Run** `sudo raspi-config`
- **Select** System Options -> Hostname
- **Enter** a new hostname and press <kbd>Enter</kbd>`
- **Finish and Reboot**


## Step 3.2.1: Setup Environment Variables
Now we can start the configuration by setting the environment variables.

- **Start the configuration** by running `openmower configure env`
- **Select** your favorite editor (e.g. `nano`)
- **Edit the environment variables**, the comments tell you what to do
- **Save the file** (<kbd>Ctrl</kbd> + <kbd>O</kbd>, <kbd>Enter</kbd> to save followed by <kbd>Ctrl</kbd> + <kbd>X</kbd>, <kbd>Enter</kbd> to exit nano)

Here is a screncast showing the whole process:
<div class="container pb-3 pt-3">
<div class="row justify-content-md-center">
<div id="step-3-2-1-player" class=""></div>
</div>
<div class="row justify-content-md-center">
<div>In the example a YardForce Classic 500 with v2 Hardware was used.</div>
</div>
</div>
<script>
    AsciinemaPlayer.create(
        'cast/openmower-configure-env.cast',
        document.getElementById('step-3-2-1-player'),
        { cols: 110, rows: 24, autoplay: false, loop: true }
    );
</script>



After this is done, the system will know which ROS version to use and which mower model is used.




## Step 3.3.1: Install Firmware
Now that the system knows which hardware you are using, we are ready to install the firmware to the xCore board.
{{< include-markdown file="/docs/Knowledge-Base/firmware-update/index.md" >}}



## Step 3.3.2: Configure xESC Motor Controllers
{{< include-markdown file="/docs/Knowledge-Base/configure-xesc/index.md" >}}


## Continue with Step 3.4: [Configure ROS Parameters]({{< relref "/docs/Conversion-Guide/3-software-setup/setup-ros" >}})
