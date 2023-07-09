---
title: Add OpenMower in Home Assitant with MQTT
linkTitle: Home Assistant
description: >
  Add OpenMower in Home Assitant with MQTT.
---

Author: Etienne@discord , DocGalaxyBlock@discord , JuergenLeber@discord

### Prerequisites
- **Home assistant**
- **[Mosquitto broker addons](https://github.com/home-assistant/addons/tree/master/mosquitto)**


### Step 0: Configure mqtt in Home Assistant
Go to to addons settings and add in "Logins"
 ```bash
 - username: openmoweruser
   password: openmowerpass
```
Of course choose your own password.

### Step 2: Install and setup MQTT bridqe on openmower
Create mqtt-bridge.conf for connect bridge to HA Mosquitto
```bash
sudo mkdir /boot/openmower/mqtt
sudo nano /boot/openmower/mqtt/mqtt-bridge.conf
```
Paste your config:
```bash
connection bridge-to-external-broker

try_private true
cleansession true
topic # out 0 "" openmower/
topic # in 0 "" openmower/

address 192.168.XXX.XXX # Ip of HA instance

remote_username openmoweruser
remote_password openmowerpass
```
You need change IP adress,user and password.

Create mosquitto.conf for connect bridge to openmower (ROS)
```bash
sudo mkdir /etc/mosquitto/
sudo nano /etc/mosquitto/mosquitto.conf
```
Paste (nothing to change here).
```bash
# A full description of the configuration file is at
# /usr/share/doc/mosquitto/examples/mosquitto.conf.example

pid_file /run/mosquitto/openmower-mqtt-bridge.pid

log_type notice
#log_dest /var/log/mosquitto/
#some random port
listener 18838


#the bridge to the openmower container
connection bridge-to-openmower

try_private true
cleansession true
topic # out 0
topic # in 0
address localhost

#include the config for the external bridge
include_dir /boot/openmower/mqtt
```

Create openmower-mqtt-bridge.service
```bash
sudo nano /etc/systemd/system/openmower-mqtt-bridge.service
```
Paste (nothing to change here).
```bash
[Unit]
Description=OpenMower MQTT Bridge
Documentation=man:mosquitto.conf(5) man:mosquitto(8)
After=network.target openmower.service openmower-debug.service
Wants=network.target
StartLimitBurst=0

[Service]
Type=notify
NotifyAccess=main
ExecStart=/usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=10s
ExecStartPre=/bin/mkdir -m 740 -p /var/log/mosquitto
ExecStartPre=/bin/chown mosquitto /var/log/mosquitto
ExecStartPre=/bin/mkdir -m 740 -p /run/mosquitto
ExecStartPre=/bin/chown mosquitto /run/mosquitto

[Install]
WantedBy=multi-user.target
```

Install and launch mqtt-bridge
```bash
systemctl disable podman-auto-update.timer podman-auto-update.service
sudo apt-get update
sudo apt-get install -y mosquitto #!don't update the mosquitto.conf!
systemctl mask mosquitto.service
systemctl enable openmower-mqtt-bridge.service
systemctl enable podman-auto-update.timer podman-auto-update.service
```
Test if service is started:
```bash
sudo systemctl status openmower-mqtt-bridge.service
```
Should return something like this:
```bash
● openmower-mqtt-bridge.service - OpenMower MQTT Bridge
     Loaded: loaded (/etc/systemd/system/openmower-mqtt-bridge.service; enabled; vendor preset: enabled)
     Active: active (running) since Sat 2023-07-08 10:14:55 BST; 1 day 5h ago
       Docs: man:mosquitto.conf(5)
             man:mosquitto(8)
    Process: 5977 ExecStartPre=/bin/mkdir -m 740 -p /var/log/mosquitto (code=exited, status=0/SUCCESS)
    Process: 5978 ExecStartPre=/bin/chown mosquitto /var/log/mosquitto (code=exited, status=0/SUCCESS)
    Process: 5979 ExecStartPre=/bin/mkdir -m 740 -p /run/mosquitto (code=exited, status=0/SUCCESS)
    Process: 5980 ExecStartPre=/bin/chown mosquitto /run/mosquitto (code=exited, status=0/SUCCESS)
   Main PID: 5981 (mosquitto)
      Tasks: 1 (limit: 4471)
        CPU: 7min 52.689s
     CGroup: /system.slice/openmower-mqtt-bridge.service
             └─5981 /usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf

Jul 08 22:43:28 openmower mosquitto[5981]: 1688852608: Connecting bridge (step 1) bridge-to-external-broker (192.168.xxx.xxx:1883)
```
Now openmower is connet to your HA MQTT addons.
You can check with [MQTT Explorer](http://mqtt-explorer.com/)


### Step 3: Configure Home Assistant configuration.yaml
add in configuration.yaml
```bash
 mqtt: !include mqtt.yaml
```

Then create a new file mqtt.yaml and paste:
```bash
############################# MQTT sensors ###########################
sensor:
  - state_topic: "openmower/robot_state/json"
    name: "OpenMower Gps"
    device_class: distance
    unique_id: "OM/sensors/om_gps_accuracy"
    value_template: "{{ value_json.pose.pos_accuracy }}"
    json_attributes_topic: "pos_accuracy"
    unit_of_measurement: "m"
  
  - state_topic: "openmower/sensors/om_mow_esc_temp/data"
    name: "OpenMower Mow ESC Temp"
    unique_id: "OM/sensors/om_mow_esc_temp"
    value_template: "{{ value  | round(2) }}"
    unit_of_measurement: "°C"
  
  - state_topic: "openmower/sensors/om_mow_motor_temp/data"
    name: "OpenMower Mow Motor Temp"
    unique_id: "OM/sensors/om_mow_esc_temp/data"
    value_template: "{{ value  | round(2) }}"
    unit_of_measurement: "°C"
  
  - state_topic: "openmower/sensors/om_left_esc_temp/data"
    name: "OpenMower Left ESC Temp"
    unique_id: "OM/sensors/om_left_esc_temp"
    value_template: "{{ value  | round(2) }}"
    unit_of_measurement: "°C"
  
  - state_topic: "openmower/sensors/om_right_esc_temp/data"
    name: "OpenMower Right ESC Temp"
    unique_id: "OM/sensors/om_right_esc_temp"
    value_template: "{{ value  | round(2) }}"
    unit_of_measurement: "°C"
  
  - state_topic: "openmower/sensors/om_charge_current/data"
    name: "OpenMower Charge Current"
    device_class: current
    unique_id: "OM/sensors/om_charge_current"
    value_template: "{{ value  | round(2) }}"
    unit_of_measurement: "A"
  
  - state_topic: "openmower/sensors/om_v_battery/data"
    name: "OpenMower V Battery"
    device_class: voltage
    unique_id: "OM/sensors/om_v_battery"
    value_template: "{{ value  | round(2) }}"
    unit_of_measurement: "V"
  
  - state_topic: "openmower/sensors/om_v_charge/data"
    name: "OpenMowerV Charge"
    device_class: voltage
    unique_id: "OM/sensors/om_v_charge"
    value_template: "{{ value  | round(2) }}"
    unit_of_measurement: "V"
  
  - state_topic: "openmower/robot_state/json"
    name: "OpenMower Battery %"
    device_class: battery
    value_template: "{{ value_json.battery_percentage |  round(2) | float * 100 }}"
    json_attributes_topic: "battery_percentage"
    unique_id: "OM/robot_state/battery_percentage"
    unit_of_measurement: "%"
  
  - state_topic: "openmower/robot_state/json"
    name: "OpenMower Current State"
    value_template: "{{ value_json.current_state }}"
    unique_id: "OM/robot_state/current_state"
    json_attributes_topic: "current_state"

binary_sensor:
  - state_topic: "openmower/robot_state/json"
    name: "OpenMower Emergency"
    device_class: safety
    unique_id: "OM/sensors/om_emergency"
    value_template: "{{ value_json.emergency }}"
    payload_on: "1"
    payload_off: "0"
    json_attributes_topic: "emergency"
    

  - state_topic: "openmower/robot_state/json"
    name: "OpenMower is Charging"
    device_class: battery_charging
    value_template: "{{ value_json.is_charging }}"
    payload_on: "1"
    payload_off: "0"
    unique_id: "OM/robot_state/is_charging"
    json_attributes_topic: "is charging"

button:
    - unique_id: "OM/actions/start_mowing"
      name: "OpenMower start mowing"
      command_topic: "openmower//action"
      payload_press: "mower_logic:idle/start_mowing"
      availability_mode: "all"
      availability:
      - topic: "openmower/actions/json"
        value_template: >
            {% for actions in value_json -%}
              {% if actions.action_id == "mower_logic:idle/start_mowing" -%}
                {{ actions.enabled }} 
              {%- endif %}
            {%- endfor %}
        payload_available: "1"
        payload_not_available: "0"
      qos: 0
      retain: false
    
    - unique_id: "OM/actions/abort_mowing"
      name: "OpenMower abort mowing"
      command_topic: "openmower//action"
      payload_press: "mower_logic:mowing/abort_mowing"
      availability_mode: "all"
      availability:
      - topic: "openmower/actions/json"
        value_template: >
            {% for actions in value_json -%}
              {% if actions.action_id == "mower_logic:mowing/abort_mowing" -%}
                {{ actions.enabled }} 
              {%- endif %}
            {%- endfor %}
        payload_available: "1"
        payload_not_available: "0"
      qos: 0
      retain: false
    - unique_id: "OM/actions/pause_mowing"
      name: "OpenMower pause mowing"
      command_topic: "openmower//action"
      payload_press: "mower_logic:mowing/pause"
      availability_mode: "all"
      availability:
      - topic: "openmower/actions/json"
        value_template: >
            {% for actions in value_json -%}
              {% if actions.action_id == "mower_logic:mowing/pause" -%}
                {{ actions.enabled }} 
              {%- endif %}
            {%- endfor %}
        payload_available: "1"
        payload_not_available: "0"
      qos: 0
      retain: false
    
    - unique_id: "OM/actions/continue_mowing"
      name: "OpenMower continue mowing"
      command_topic: "openmower//action"
      payload_press: "mower_logic:mowing/continue"
      availability_mode: "all"
      availability:
      - topic: "openmower/actions/json"
        value_template: >
            {% for actions in value_json -%}
              {% if actions.action_id == "mower_logic:mowing/continue" -%}
                {{ actions.enabled }} 
              {%- endif %}
            {%- endfor %}
        payload_available: "1"
        payload_not_available: "0"
      qos: 0
      retain: false

    - unique_id: "OM/actions/skip_area"
      name: "OpenMower skip area"
      command_topic: "openmower//action"
      payload_press: "mower_logic:mowing/skip_area"
      availability_mode: "all"
      availability:
      - topic: "openmower/actions/json"
        value_template: >
            {% for actions in value_json -%}
              {% if actions.action_id == "mower_logic:mowing/skip_area" -%}
                {{ actions.enabled }} 
              {%- endif %}
            {%- endfor %}
        payload_available: "1"
        payload_not_available: "0"
      qos: 0
      retain: false
```

### Step 4: Create your own dashboard in HA
After that you can create your dashbord! Enjoy!
