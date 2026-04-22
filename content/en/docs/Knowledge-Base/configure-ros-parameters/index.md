---
title: "Managing ROS Parameters"
linkTitle: "Configure ROS Parameters"
weight: 120
description: >-
     Learn how to view and override ROS parameters in OpenMower using the shell
     and configuration files for flexible system tuning.
---

## Viewing and Configuring ROS Parameters

OpenMower is built on ROS, which means much of its behavior is controlled through parameters. Understanding how to inspect and modify these parameters gives you fine-grained control over your mower’s operation.

### Listing All Parameters

To see all currently active ROS parameters, open the OpenMower shell:

```bash
openmower shell
```

Then run:

```bash
rosparam list
```

This will display a full list of parameters currently loaded in the system. It’s a useful first step when debugging or trying to understand how your mower is configured.

### Overwriting Parameters

All parameters can be customized using the `mower_params.yaml` configuration file. This file acts as the central place to override default values.

The easiest way to edit it is with:

```bash
openmower configure ros

```

### Example

In this example we will be overwriting the speed parameter.

#### 1. Fetch the Parameter's current value
After discovering a parameter you want to edit using `rosparam list`, you can get the value using `rosparam get <parameter>`:

```bash
🚜 openmower@openmower-v2:~$ rosparam get /move_base_flex/FTCPlanner/speed_fast
0.4
```

In this case, our speed is currently at 0.4 m/sec for mowing

#### 2. Change the value for your config
On the host system call `openmower configure ros` and translate the parameter name to YAML.
This is done by replacing each `/` into indentations (2x space).

For our example it looks like this:
```yaml
move_base_flex:
  FTCPlanner:
    speed_fast: 0.5
```

#### 3. Save the file and check the updated value
After saving the file, ROS is automatically restarted and you can check, if the value is now updated:
```bash
🚜 openmower@openmower-v2:~$ rosparam get /move_base_flex/FTCPlanner/speed_fast
0.5
```

:tada: Done!

### If you have issues
If some parameter isn't overriding correctly, make sure you are on the latest version of OpenMower. If it still doesn't work ask on Discord.

