---
title: "Universal Board Configuration"
linkTitle: "Universal Board Configuration"
weight: 230
description: >-
  How to configure the Universal Board for custom mower builds: parameter reference,
  template file, and wheel tick calibration.
---

This guide is for **custom mower builds** using the OpenMower Universal Board. Unlike supported mowers, custom builds require you to measure and set several hardware-specific parameters before the mower will operate correctly.

All custom parameters go into `~/params/custom_params.yaml` on the mower.

{{% alert title="Do not use openmower configure ros" color="warning" %}}
`openmower configure ros` opens `mower_params.yaml` by default — this is the **wrong file** for custom builds. Always edit `custom_params.yaml` directly:

```bash
nano ~/params/custom_params.yaml
```

All other `openmower` commands (e.g. `openmower configure env`) work as expected.
{{% /alert %}}

## Configuration Template

Download the template and place it at `~/params/custom_params.yaml` on your mower as a starting point:

**[Download custom_params.yaml](custom_params.yaml)**

The sections below explain every parameter marked `# TODO`.

---

### Differential Drive

```yaml
ll:
  services:
    diff_drive:
      wheel_distance_m: 0.325
      ticks_per_m: 1600.0
```

| Parameter | What to set |
|---|---|
| `wheel_distance_m` | Distance in meters between the center of the left and right drive wheels. Measure with a tape measure. |
| `ticks_per_m` | Encoder ticks per meter of travel. Must be measured — see [Calibrating Wheel Ticks](#calibrating-wheel-ticks) below. |

---

### IMU Orientation

```yaml
    imu:
      axis_config: "+X-Y-Z"
```

| Parameter | What to set |
|---|---|
| `axis_config` | Orientation of the mainboard relative to the mower chassis. `+X-Y-Z` is correct for a flat, horizontal mounting with the board's X axis pointing forward. Change this if your mainboard is mounted at an angle or rotated. |

---

### Battery Voltages

```yaml
    power:
      battery_full_voltage: 20.0
      battery_empty_voltage: 18.5
      battery_critical_voltage: 16.5
      battery_critical_high_voltage: 21.0
      charge_critical_high_voltage: 30.0
      charge_critical_high_current: 1.5
```

Look up the voltage spec for your battery pack and set accordingly.

| Parameter | What to set |
|---|---|
| `battery_full_voltage` | Voltage of a fully charged pack (from spec). |
| `battery_empty_voltage` | Voltage at which the mower returns to dock. |
| `battery_critical_voltage` | Emergency low-voltage cutoff. Set below empty but above damaging discharge. |
| `battery_critical_high_voltage` | Overvoltage protection threshold. Set slightly above full charge voltage. |
| `charge_critical_high_voltage` | Maximum acceptable charger output voltage. |
| `charge_critical_high_current` | Maximum acceptable charge current in amps. |

---

### GPS Antenna Offset

```yaml
xbot_positioning:
  antenna_offset_x: 0.3
  antenna_offset_y: 0.0
```

The positioning system needs to know where the GPS antenna is relative to the mower's **center of rotation** (the midpoint between the two drive wheels).

| Parameter | What to set |
|---|---|
| `antenna_offset_x` | Forward/back offset in meters. Positive = antenna is in front of the rotation center. Measure from wheel midpoint to antenna. |
| `antenna_offset_y` | Left/right offset in meters. Positive = antenna is to the left. Usually 0 if the antenna is centered. |

---

### GPS Datum

```yaml
    gps:
      datum_lat: 53.457452
      datum_long: 10.014737
```

These are not marked `TODO` in the template but **must be changed**. Set them to coordinates near your docking station — this becomes the origin of your mower's map. Use a GPS or map tool to get the coordinates.

---

### NTRIP Credentials

```yaml
ntrip_client:
  host: "www.your-ntrip-caster.de"
  port: 2101
  username: "ntripuser"
  password: "ntrippass"
  mountpoint: "ntripmount"
```

Fill in the credentials from your RTK correction provider.

---

### Emergency Sensors

Before enabling the mower motor, configure and verify all emergency sensors (lift detection, tilt detection, stop buttons). This is done via the GPIO input configuration — see [Configuring GPIO Inputs]({{< relref "/docs/Knowledge-Base/configuration/configure-gpio-inputs" >}}) for the full setup guide.

### Enable Mower Motor

```yaml
mower_logic:
  enable_mower: false
```

Set to `true` only after all emergency sensors are wired, configured, and verified to work correctly. Running without functioning emergency sensors is unsafe.

---

## Calibrating Wheel Ticks

This procedure measures the `ticks_per_m` value for your specific mower's wheel encoders.

### Prerequisites

- OpenMower is running
- SSH or web terminal access
- A flat surface with ~10 m of clear, straight space
- Something to mark the start and end position (tape, chalk, etc.)

### Step 1: Enter recording mode

Open the OpenMower app and activate **area recording mode**. This ensures the drive motors and wheel encoders are active and publishing odometry data.

### Step 2: Record start tacho values

Open the ROS shell:

```bash
openmower shell
```

Subscribe to the left ESC status topic and note the `tacho` field:

```bash
rostopic echo /ll/diff_drive/left_esc_status
```

Write down the value, then press <kbd>Ctrl</kbd>+<kbd>C</kbd>. Repeat for the right wheel:

```bash
rostopic echo /ll/diff_drive/right_esc_status
```

### Step 3: Drive a 10 m straight line

Mark the mower's current position, then drive it in a straight line for exactly **10 meters**. Drive slowly and steadily — the straighter the line, the more accurate the result.

### Step 4: Record end tacho values

Subscribe to each topic again and note the new `tacho` values:

```bash
rostopic echo /ll/diff_drive/left_esc_status
```

```bash
rostopic echo /ll/diff_drive/right_esc_status
```

### Step 5: Calculate ticks_per_m

Compute the difference for each wheel. If negative, flip the sign:

```
left_diff  = |tacho_end_left  - tacho_start_left|
right_diff = |tacho_end_right - tacho_start_right|
```

The two values should be approximately equal. Average them and divide by 10:

```
ticks_per_m = (left_diff + right_diff) / (2 * 10)
```

### Step 6: Apply the value

Edit `custom_params.yaml` directly:

```bash
nano ~/params/custom_params.yaml
```

Set the value you calculated:

```yaml
ll:
  services:
    diff_drive:
      ticks_per_m: <your_value>
```

Save the file and restart OpenMower to apply.

{{% alert title="Tip" color="info" %}}
Run the measurement two or three times and average the results for better accuracy. Small variations in how straight you drive will affect individual readings.
{{% /alert %}}
