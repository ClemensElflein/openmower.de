---
title: IC2 is INA180A3IDBVR which has inadequate voltage range
linkTitle: INA180A3IDBVR burns
---

Due to sourcing error, IC2 that was installed (INA180A3IDBVR) had a lower voltage rating (<24V) that mower needs (<30V).

{{< imgproc datasheet Resize "400x q99" />}}

Symptoms:

* mower stops charging
* mower status topic reports 10A charging current, makes no sense with 2A fuses
* IC2 burns out

{{< imgproc burnt_tomm Resize "300x q99" />}}{{< imgproc burnt_vermut Resize "300x q99" />}}

# Solutions:

First, for many people, it's just working. So if your mower worked for a couple of weeks, it might survive.

### Option 1

Replace IC2 with TSC101CILT (DigiKey 497-6947-1-ND).

    pretty simple with a normal soldering iron. 
    for desoldering I usually do a blob of solder to heat the whole part then remove it.
    then clean the pads using some desoldering wick
    then add solder to one pad, position the part with one leg into the pad
    then solder other legs

### Option 2

Disable the check in firmware. This is only one of the safety features, and it's ok to just disable it in firmware.
To do that, update your firmware, hard-coding charge current to 1A.

Replace

```c
        status_message.charging_current =
                (float) analogRead(PIN_ANALOG_CHARGE_CURRENT) * (3.3f / 4096.0f) / (CURRENT_SENSE_GAIN * R_SHUNT);
```

with

```c
        status_message.charging_current = 1.0
```

For mainstream kit versions, we prepared download-ready versions. Just update your mower_version in `/boot/mower_config`

| Existing mover_version | Update to  |
|------------------------|------------|
| 0_13_X                 | 0_13_X_IC2 |
| 0_12_X                 | 0_12_X_IC2 |
| 0_11_X_WT901           | 0_11_X_IC2 |
| 0_10_X_WT901           | 0_10_X_IC2 |
| 0_9_X_WT901            | 0_9_X__IC2 |
