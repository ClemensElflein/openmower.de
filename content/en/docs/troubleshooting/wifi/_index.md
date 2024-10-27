---
title: Troubleshoot Wi-Fi
linkTitle: Wi-Fi
description: >
    Issues with Wi-Fi like disconnects.
tags: [Wi-Fi, wireless, usb]
resources:
    - src: "**.png"
---


# Wi-Fi Disconnects and unstable Wi-Fi with external dongle

The Raspberry Pi tries to powersave on the Wi-Fi, which causes high latency or even packet loss on the Wi-Fi connections.

Please check which chipset your Wi-Fi dongle uses.
You can solve this by editing the modprobe as following:


## Realtek RTL8192cu

```bash
sudo nano /etc/modprobe.d/8192cu.conf
# Change the following lines
rtw_power_mgnt=0
rtw_enusbss=0
```

## Realtek RTL8821CU

```bash
sudo nano /etc/modprobe.d/8821cu.conf
# Change the following lines
rtw_drv_log_level=1
rtw_led_ctrl=1
rtw_vht_enable=1
rtw_power_mgnt=0
rtw_enusbss=0
```
