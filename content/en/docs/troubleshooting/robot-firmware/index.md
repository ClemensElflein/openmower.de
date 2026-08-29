---
title: "Troubleshooting: Invalid Robot Firmware"
linkTitle: "Robot Firmware"
description: >-
  Fix the 'Robot firmware ... invalid for this hardware' error by setting the
  correct board type in mower_params.yaml.
tags: [troubleshooting, firmware, board, mower_params]
---

The firmware logs the following error repeatedly and the status LED blinks red:

```text
Robot firmware '<name>' invalid for this hardware...
```

This means the `board:` value in your `mower_params.yaml` does not match the
mainboard that is actually installed. The firmware rejects the name and keeps
waiting for a valid one.

## Fix

{{< tabpane text=true >}}
{{% tab header="Supported mower" text=true %}}

Open the ROS configuration (this opens `mower_params.yaml`):

```bash
openmower configure ros
```
<br>

Set the `board:` value under `ll:` field to the board type that matches your hardware:

```yaml
ll:
  board: "YardForce"
```
<br>

After saving, OpenMower restarts automatically and should boot with a green
status LED.

{{% /tab %}}
{{% tab header="Universal / Custom (MOWER=CUSTOM)" text=true %}}

Edit `~/params/custom_params.yaml`:

```bash
nano ~/params/custom_params.yaml
```
<br>

Set the `board:` value under `ll:`, for a Universal board, use `Universal-5S`,
`Universal-7S`, or `Universal-8S` depending on your battery:

```yaml
ll:
  board: "Universal-7S"
```
<br>

Editing `custom_params.yaml` does not restart the stack automatically, so apply
the change via:

```bash
openmower restart
```
<br>

See [Universal Board Configuration]({{< relref "/docs/Knowledge-Base/configuration/universal-board-configuration" >}})
for the full custom-build reference.

{{% /tab %}}
{{< /tabpane >}}

## Valid board types

| Board type     | Hardware                                             |
| -------------- | ---------------------------------------------------- |
| `YardForce`    | Regular YardForce board                              |
| `YardForce-V4` | YardForce board with YFR4-xESC (old Rev.4 mow motor) |
| `Universal-5S` | Universal board with 5S battery                      |
| `Universal-7S` | Universal board with 7S battery                      |
| `Universal-8S` | Universal board with 8S battery                      |
| `Worx`         | Universal board with Worx functionality              |
| `Lyfco-E1600`  | Universal board with Lyfco-E1600 functionality       |
| `Husq310MKII`  | Husqvarna 310 MKII board                             |

The value must match exactly (including capitalization).

The default template with all valid values lives in the OpenMowerOS repository:
[mower_params.yaml](https://github.com/ClemensElflein/OpenMowerOS/blob/main/stage-openmower/40-openmower/files/home/openmower/params/mower_params.yaml).
