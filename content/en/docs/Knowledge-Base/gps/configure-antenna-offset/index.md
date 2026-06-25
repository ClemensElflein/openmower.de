---
title: "Configuring the GPS Antenna Offset"
linkTitle: "Configure Antenna Offset"
weight: 410
description: >-
  Configure the physical offset between your GPS antenna and the mower's
  wheel axis center so OpenMower can accurately compute its position.
---

## Overview

OpenMower tracks position using the GPS antenna. If the antenna is not mounted exactly at the center of the wheel axis, the mower's computed position will be off by that physical offset. Configuring the antenna offset corrects for this.

## Coordinate System

The offset is expressed in the mower's local coordinate frame:

- **Origin**: center of the wheel axis (midpoint between the two drive wheels)
- **X axis**: points forward
- **Y axis**: points left
- **Z axis**: points up (right-handed coordinate system)

| Direction | Sign |
|---|---|
| Forward | X positive |
| Backward | X negative |
| Left | Y positive |
| Right | Y negative |

**Examples:**

- Antenna 10 cm forward, 5 cm to the right → `antenna_offset_x: 0.1`, `antenna_offset_y: -0.05`
- Antenna 5 cm to the left → `antenna_offset_x: 0.0`, `antenna_offset_y: 0.05`

## Configuration

Open the ROS parameter config file:

```bash
openmower configure ros
```

Add the following section at the end of the file, adjusting the values to match your physical antenna position:

```yaml
xbot_positioning:
  antenna_offset_x: 0.05
  antenna_offset_y: -0.15
```

Values are in **meters**.

Save the file. ROS will restart automatically and apply the new offset.
