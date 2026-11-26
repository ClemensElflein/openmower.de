---
title: "Troubleshooting: Invalid Robot Firmware"
linkTitle: "Robot Firmware"
description: >-
  Fix the 'Robot firmware ... invalid for this hardware' error by setting the
  correct board variant (ll/board) in mower_params.yaml.
tags: [troubleshooting, firmware, board, mower_params]
aliases: ["/ll/board/"]
---

The firmware logs the following error repeatedly and the status LED blinks red:

```text
Robot firmware '<name>' invalid for this hardware...
```

This means the `board:` value in your `mower_params.yaml` does not match the
board variant that is actually installed. The firmware rejects the name and
keeps waiting for a valid one.

## Fix

{{< tabpane text=true >}}
{{% tab header="Supported mower" text=true %}}

Open the ROS configuration (this opens `mower_params.yaml`):

```bash
openmower configure ros
```
<br>

Set the `board:` value under `ll:` to the variant that matches your hardware:

```yaml
ll:
  board: "Worx"
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

## Detected automatically - no setting needed

These board variants are recognised at boot from the hardware itself, `board:` is
ignored for them:

| Board Variant  | Detected by                                                             |
| -------------- | ----------------------------------------------------------------------- |
| `Sabo`         | EEPROM on the carrier board                                             |
| `xBot`         | EEPROM on the carrier board                                             |
| `YardForce`    | EEPROM as well as mower ESC on UARTD2 answers without the YFR4 protocol |
| `YardForce-V4` | EEPROM as well as mower ESC on UARTD2 answers with the YFR4 protocol    |


## Boards that need the value

For these boards the firmware waits until a matching name arrives, and that is
where the `Robot firmware ... invalid for this hardware` error comes from:

| Board Variant  | Hardware                                       |
| -------------- | ---------------------------------------------- |
| `Universal-5S` | Universal board with 5S battery                |
| `Universal-7S` | Universal board with 7S battery                |
| `Universal-8S` | Universal board with 8S battery                |
| `Worx`         | Universal board with Worx functionality        |
| `Lyfco-E1600`  | Universal board with Lyfco-E1600 functionality |
| `Husq310MKII`  | Husqvarna 310 MKII board                       |

The value must match exactly (including capitalization).

The value is the board variant, not strictly the board: `Universal-5S`/`7S`/`8S`
are the same Universal board with a different battery, `Worx`, `Lyfco-E1600` and
`Husq310MKII` are the same board with a different case and UI.

The default template with all valid values lives in the OpenMowerOS repository:
[mower_params.yaml](https://github.com/ClemensElflein/OpenMowerOS/blob/main/stage-openmower/40-openmower/files/home/openmower/params/mower_params.yaml).
