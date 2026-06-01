---
title: "Unicore GPS Modules"
linkTitle: "Unicore GPS"
weight: 210
description: "Set up Unicore GPS RTK modules (UM960, UM980, UM982) as alternatives to ArduSimple simpleRTK2B — cheaper, triple-band, and compatible with OpenMower."
---

Several users have chosen alternative GPS RTK modules with chips by **Unicore**:

- UM960
- UM980
- UM982

These chips are sold in different variants. Some come with a USB-C socket (so they can be connected directly to a PC for configuration via UPrecise). Some have a different antenna socket, which requires an *SMA F* to *MMCX M90* cable.

Compared to the *ArduSimple simpleRTK2B*, they are a bit cheaper and support triple-band frequencies.

## Configuration via UART (mainboard)

Use this method to wire the module directly to the mainboard UART header and configure it via the OpenMower CLI.

### Prerequisites

- Modified mower with replaced mainboard
- RPi with `openmower` stack running

### Step 1 — Solder headers on the UM9XX

![UM9XX module with header pins]({{< relref "/docs/Knowledge-Base/unicore-gps" >}}/images/wm9xx.png)

You only need the 4 middle pins from the 6 available: **GND**, **VCC**, **TX**, **RX**.

The remaining 2 pins are not needed:
- **EN** — can be used to temporarily shut down the module
- **PPS** — pulse-per-second signal, useful only if you need precise timing

### Step 2 — Wire UM9XX to the mainboard

An [adapter board](https://github.com/xtech/hw-openmower-utils/tree/main/hw-openmower-utils-v1-arduino-uno-um9x) is available as an alternative to manual wiring.

| MainBoard | UM9XX |
|---|---|
| TXD | TXD |
| RXD | RXD |
| 5V_IN | VCC |
| GND | GND |

![UM9XX wiring pinout sample]({{< relref "/docs/Knowledge-Base/unicore-gps" >}}/images/um9xx-wiring-pinout.jpg)
![Mainboard wiring sample]({{< relref "/docs/Knowledge-Base/unicore-gps" >}}/images/mainboard-wiring.jpg)

### Step 3 — Configure UM9XX over UART

Install miniterm (part of `python3-serial`):

```bash
sudo apt-get install python3-serial
```

Stop the openmower stack so it does not occupy the GPS connection:

```bash
openmower stop
```

In a separate terminal, expose the GPS over TCP at the default baud rate (115200):

```bash
openmower expose-gps 115200
```

Connect to the GPS:

```bash
python -m serial.tools.miniterm socket://localhost:2000 -e
```

{{< alert color="info" >}}
Press <kbd>Enter</kbd> after each command to send it to the receiver.
{{< /alert >}}

> **Note:** The following commands assume you wired to the bottom lane (COM1). If you used a different lane, replace `COM1` with `COM2`.

Factory-reset the module and note the response:

```
FRESET
```

Expected output:
```
$command,FRESET,response: OK*4D
system is rebooting
..........
$devicename,COM1*67
```

Set the baud rate to 460800:

```
CONFIG COM1 460800
```

Exit miniterm with **Ctrl+]**, then restart `expose-gps` at the new baud rate and reconnect:

```bash
openmower expose-gps 460800
```

```bash
python -m serial.tools.miniterm socket://localhost:2000 -e
```

> **Note:** If commands get no response, the baud rate or COM port is wrong. Restart `expose-gps` at 115200, run `FRESET`, and try again.

Configure NMEA output. Each `GP*` command produces extra output — make sure `SAVECONFIG` completes successfully at the end:

```
MODE ROVER UAV
GPGSV COM1 2
GPRMC COM1 1
GPGSA COM1 1
GPVTG COM1 1
GPGGA COM1 0.5
SAVECONFIG
```

Expected output after `SAVECONFIG`:

```
$GNGGA,192705.50,,,,,0,00,9999.0,,,,,,*45
$command,SAVECONFIG,response: OK*55
$GNGGA,192706.00,,,,,0,00,9999.0,,,,,,*43
$GPGSA,,1,,,,,,,,,,,,,,,,*73
$GNRMC,192706.00,V,,,,,,,030625,0.0,E,N,V*7B
```

Exit miniterm with **Ctrl+]**.

### Step 4 — Configure OpenMower

Run `openmower configure ros` and set the GPS protocol to `NMEA` and the baud rate to `460800`.

With your RTK base configured, take the mower outside and verify you get a GPS fix.

## Troubleshooting — receiver resets

If the receiver cannot get a fix, a reboot may help. UPrecise provides three reset buttons. Unlike `FRESET`, these **do not wipe the configuration**:

| Button | Command | Effect |
|---|---|---|
| Hot Start | `RESET` | Quick restart |
| Warm Start | `RESET EPHEM` | Clears ephemeris data |
| Cold Start | `RESET EPHEM ALMANAC IONUTC POSITION` | Full data reset |

See section 8.3 ("Reset") in the [Unicore command reference](https://core-electronics.com.au/attachments/localcontent/Unicore_Reference_Commands_Manual_For_N4_High_Precision_Products_V2_EN_R1_1_189543505cb.pdf) for details.
