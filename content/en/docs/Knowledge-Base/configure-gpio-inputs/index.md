---
title: "Configuring GPIO Inputs"
linkTitle: "Configure GPIO Inputs"
weight: 130
description: >-
  Learn how to configure GPIO inputs for emergency stops, wheel lift sensors,
  and other hardware buttons using the OpenMower input service.
---

## Overview

OpenMower supports configuring GPIO pins as digital inputs that can trigger emergency stops or other events. Common use cases include:

- **Wheel lift sensors** — detect when the mower is lifted
- **Stop buttons** — physical emergency stop buttons on top of the mower

## Step 1: Create the inputs configuration file

Create `/home/openmower/params/inputs.yaml` with your GPIO input definitions:

```yaml
gpio:
  - name: Front left wheel lift
    line: GPIO10
    active: low
    emergency:
      reason: lift
      delay: 2500

  - name: Front right wheel lift
    line: GPIO11
    active: low
    emergency:
      reason: lift
      delay: 2500

  - name: Top stop button 1
    line: GPIO12
    active: low
    emergency:
      reason: stop
      delay: 10

  - name: Top stop button 2
    line: GPIO13
    active: low
    emergency:
      reason: stop
      delay: 10
```

### Configuration fields

| Field | Description |
|---|---|
| `name` | Human-readable label for the input |
| `line` | GPIO pin name (e.g. `GPIO10`) |
| `active` | Logic level that triggers the event — `low` or `high` |
| `emergency.reason` | Emergency type — `lift` for wheel lift, `stop` for stop button |
| `emergency.delay` | Debounce/delay in milliseconds before the emergency is triggered |

## GPIO Pin Mapping

The example config above uses GPIO10–GPIO13. Here is how those map to physical connectors on each board.

### OpenMower Universal Board

Orientation: looking at the board with the ethernet ports facing you.

| Position | GPIO |
|---|---|
| Top left | GPIO13 |
| Top right | GPIO12 |
| Bottom right | GPIO11 |
| Bottom left | GPIO10 |

### OpenMower Yardforce Board

Orientation: looking at the board with the ethernet ports at the bottom left, pins sorted top to bottom.

| Position | GPIO |
|---|---|
| 1st (topmost) | GPIO10 |
| 2nd | GPIO11 |
| 3rd | GPIO12 |
| 4th | GPIO13 |

## Step 2: Enable the input service

Add the following to your `mower_params.yaml` (or `custom_params.yaml` for Universal board builds):

```yaml
ll:
  services:
    input:
      config_file: /data/params/inputs.yaml
```

To open the file for editing:

```bash
openmower configure ros
```

{{% alert title="Path mapping on OSv2" color="info" %}}
On OSv2, `/home/openmower/params` is mapped to `/data/params` inside the container. If you are on a different setup, adjust the `config_file` path accordingly.
{{% /alert %}}

## Step 3: Restart OpenMower

After saving both files, restart the service to apply the changes:

```bash
openmower restart
```

Your GPIO inputs are now active and will trigger the configured emergency events when the specified logic level is detected.
