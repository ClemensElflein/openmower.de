---
title: "NX Types"
linkTitle: "NX Types"
weight: 30
description: >
  Modification Guide for YardForce NX Type Mowers with Carrierboard version ≥ 1.2.0
---


{{% alert title="Carrierboard ≥ 1.2.0 only!" color="warning" %}}
This guide is exclusively for **Carrierboard version ≥ 1.2.0**!<br>
![v1.2.0 Carrierboard identification](../carrierboard_version_v1.2.0.jpg)<br>
{{% /alert %}}

{{% alert title="Coming Soon" color="info" %}}
This guide is currently being written. Check back soon or ask on [Discord](https://discord.gg/jE7QNaSxW7) for the latest information.
{{% /alert %}}

## Configuring GPIO Inputs

The YardForce NX types use GPIO-based sensors for wheel lift detection, stop buttons, and collision detection.
These must be configured before the robot is operational.

There is currently no dedicated hardware-specific `inputs.yaml` for NX types yet.
As a starting point, use the [SA/SC types definition](https://github.com/ClemensElflein/open_mower_ros/blob/main/src/open_mower/params/hardware_specific/YardForceSA_OEM/inputs.yaml) as a template and adjust it to your wiring.

Refer to [Configuring GPIO Inputs]({{< relref "/docs/Knowledge-Base/configuration/configure-gpio-inputs" >}}) for detailed instructions
– including the Hall-MUX selection required for Carrierboard ≥ 1.2.0.
