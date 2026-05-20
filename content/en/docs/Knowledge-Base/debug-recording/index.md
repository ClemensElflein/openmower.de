---
title: "Creating a Debug Recording"
linkTitle: "Debug Recording"
weight: 150
description: >-
  How to record a rosbag for debugging positioning and other issues,
  and how to retrieve it from the mower for sharing.
---

When investigating issues — especially positioning problems — a rosbag recording gives developers a full snapshot of sensor data to analyse. This guide walks you through recording one and retrieving it from your mower.

{{% alert title="Privacy notice" color="warning" %}}
A rosbag records raw sensor data, which includes the **GPS position of your mower**. By sharing the file you disclose the physical location of your garden. Only share it with people you trust.
{{% /alert %}}

## Prerequisites

- OpenMower is running and the mower has a GPS fix (green GPS icon in the app)
- You can access the mower via SSH or the web terminal

## Step 1: Start the recording

Connect to your mower via SSH or the web terminal, then enter the ROS shell:

```bash
openmower shell
```

Once inside, navigate to the recordings directory and start recording all topics:

```bash
cd /data/recordings
rosbag record -a
```

This records **all** active ROS topics. Leave the terminal open — the recording runs until you stop it with <kbd>Ctrl</kbd>+<kbd>C</kbd>.

## Step 2: Enter area recording mode

Open the OpenMower app and activate **area recording mode** — the same mode you use when recording mowing areas. This ensures all relevant topics (GPS, IMU, wheel odometry) are actively publishing at full rate.

{{% alert title="GPS fix required" color="warning" %}}
Make sure the GPS icon in the app is **green** before driving. Recording without a fix produces data that cannot be used for analysis.
{{% /alert %}}

## Step 3: Drive the test patterns

Drive the mower through the following patterns. Each one exercises a different aspect of positioning:

| Pattern | Purpose |
|---|---|
| Straight lines | Linear odometry and GPS consistency |
| Figure-8 | Combined turning and straight-line tracking |
| Rotate on the spot (clockwise) | Yaw estimation, IMU vs. GPS heading |
| Rotate on the spot (counter-clockwise) | Same, opposite direction |

A minute or two of each pattern is sufficient. You don't need a large area — a small open patch of lawn works fine.

## Step 4: Stop the recording

Once done, go back to the terminal and press <kbd>Ctrl</kbd>+<kbd>C</kbd>, then type `exit` to leave the ROS shell.

The `.bag` file is now in `~/recordings/` on the mower. List the directory to find your filename:

```bash
ls -lh ~/recordings/
```

The filename includes a timestamp, e.g. `2024-06-01-12-34-56.bag`.

## Step 5: Retrieve the file

Copy the `.bag` file from `~/recordings/` on the mower to your computer.

{{< tabpane text=true >}}

{{% tab header="Linux / macOS" %}}
Use `scp` from your local terminal:

```bash
scp openmower@<mower-ip>:recordings/<filename>.bag .
```

Replace `<mower-ip>` with your mower's IP address and `<filename>` with the actual filename. The file downloads to your current directory.
{{% /tab %}}

{{% tab header="Windows" %}}
**Windows 10 (build 1809 or later) and Windows 11** include an OpenSSH client. Open **Command Prompt** or **PowerShell** and run:

```bat
scp openmower@<mower-ip>:recordings/<filename>.bag .
```

On **older Windows versions**, use a graphical SFTP client instead:

- **[WinSCP](https://winscp.net)** — free, open source
- **[Cyberduck](https://cyberduck.io)** — free, cross-platform

Connect with protocol **SFTP**, host `<mower-ip>`, user `openmower`, and navigate to `/home/openmower/recordings/` to download the file.
{{% /tab %}}

{{< /tabpane >}}

{{% alert title="Tip" color="info" %}}
`.bag` files compress very well. Zipping before sharing can reduce the file size significantly:
{{% /alert %}}

Once you have the file, share it with whoever is helping you debug — via Discord, a file sharing service, or any other method that works in context.

## Step 6: Clean up

Once debugging is done, delete the recordings from the mower to free up disk space:

```bash
# delete a specific file
rm ~/recordings/<filename>.bag

# delete all recordings
rm ~/recordings/*.bag
```
