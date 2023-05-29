---
title: IC2 is INA180A3IDBVR which has inadequate voltage range
linkTitle: INA180A3IDBVR breaks
---

Due to sourcing error, IC2 that was installed on the boards (INA180A3IDBVR) has a lower voltage rating than the original part. The voltage rating is 26V, but the mower needs 30V for the fully charged battery. That's why some IC2 break after some time.

{{< imgproc datasheet Resize "400x q99" />}}

Symptoms:

* mower stops charging
* mower status topic reports 10A charging current, makes no sense with 2A fuses
* IC2 breaks (black residue on the PCB)

{{< imgproc burnt_tomm Resize "300x q99" />}}
{{< imgproc burnt_vermut Resize "300x q99" />}}

## Determining if you are affected
INA180A3IDBVR has marking `1A9D`. If you see that - you are affected. Good chip TSC101CILT is marked `0106`.

{{< figure src=INA180A3IDBVR caption="Wrong INA180A3IDBVR" >}}
{{< figure src=TSC101CILT caption="Good TSC101CILT" >}}


## Solutions

First, for many people, it's just working. So if your mower worked for a couple of weeks, it might survive. In that case you don't have to take any action. If your robot does not charge anymore, there are two options: Fixing the hardware or ignoring the error in software.

I recommend replacing the IC to fix this issue.

### Option 1

Replace IC2 with TSC101CILT (DigiKey `497-6947-1-ND`, Mouser `511-TSC101CILT`, TME `TSC101CILT` or other major distributor).

The process is pretty simple to do with a normal soldering iron.
Disconnect all modules and power from the mainboard before starting the replacement.

For replacement, follow these steps:
1. For desoldering the IC, use a blob of solder to cover all pins of the IC. Heat it up and remove the part. 
2. Then clean the pads using desoldering wick.
3. Add solder to one pad, position the part with one leg into the pad and let cool.
4. Solder remaining legs, the part will not move anymore.

### Option 2: Disable the safety check in firmware.
The current sense IC prevents the charger from applying excessive current to the battery. This is one of three safety checks in the charging circuit:
1. Fuse in the charging path
2. IC2 to measure the current and shut down charging, if excessive current occurs
3. Battery management system inside the battery to protect the battery.

If you feel that you don't need the safety check and don't want to switch the IC, you can disable the check in the firmware. We advise to do the hardware replacement instead. As always: Do this at your own risk.

To do that, update your firmware, hard-coding charge current to -1A:
Replace

```c
        status_message.charging_current =
                (float) analogRead(PIN_ANALOG_CHARGE_CURRENT) * (3.3f / 4096.0f) / (CURRENT_SENSE_GAIN * R_SHUNT);
```

with

```c
        status_message.charging_current = -1.0
```

For mainstream kit versions, we prepared this already. Just update your mower_version in `/boot/mower_config.txt` to use the firmware without charging current control.

| Existing Version | Change to  |
|------------------------|------------|
| 0_13_X                 | 0_13_X_IGNORE_CHARGING_CURRENT |
| 0_12_X                 | 0_12_X_IGNORE_CHARGING_CURRENT |
| 0_11_X_WT901           | 0_11_X_IGNORE_CHARGING_CURRENT |
| 0_10_X_WT901           | 0_10_X_IGNORE_CHARGING_CURRENT |
| 0_9_X_WT901            | 0_9_X_IGNORE_CHARGING_CURRENT |
