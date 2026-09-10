---
title: "WiFi Setup via Bluetooth or USB (Improv)"
linkTitle: "WiFi Setup (Improv)"
weight: 115
description: >
  Configure your mower's WiFi connection straight from your phone or computer over Bluetooth or USB — no hotspot hunting required.
---

{{% alert title="Requires OpenMowerOS v3+" color="info" %}}
This guide is for **OpenMowerOS v3 and later**, which provision WiFi using the open [Improv Wi-Fi](https://www.improv-wifi.com/) standard, over Bluetooth or USB.

Running an older OS version? Use the [hotspot-based WiFi setup]({{< relref "/docs/step-by-step/3-software-setup/connect-wifi" >}}) guide instead.
{{% /alert %}}

## How it works
OpenMowerOS v3 speaks the [Improv Wi-Fi](https://www.improv-wifi.com/) protocol, either advertised over Bluetooth Low Energy or over a USB serial connection. Your browser talks to the mower directly to send it your WiFi credentials, so there's no need to connect to a temporary hotspot first. Pick whichever of the two options below is easier for you.

## Step 1: Get ready
- Power on the mower (e.g. place it in the docking station) and keep it nearby.
- For Bluetooth: turn on Bluetooth on your phone or computer.
- For USB: grab a Micro USB cable and connect your computer to the Micro USB port on the core board.

## Step 2: Start provisioning

### Option A: Bluetooth
{{% alert title="Browser support" color="warning" %}}
Requires **Web Bluetooth**: **Google Chrome** or **Microsoft Edge**. Works out of the box on Windows, macOS, ChromeOS and Android.

**Linux desktop:** Chrome/Edge ship Bluetooth support turned off by default — see the note below the button if you hit this.

**Not supported at all:** Safari and any browser on iOS/iPadOS (Apple does not permit Web Bluetooth there), and Firefox. On an iPhone or iPad, borrow a Chrome/Edge-capable Android device or computer instead — OSv3 has no hotspot fallback.
{{% /alert %}}

Click the button below, then pick your mower from the Bluetooth device picker (it's named something like `OpenMower-XXXX`).

<div class="d-flex flex-column align-items-center my-4">
<improv-wifi-launch-button class="improv-launch">
  <button slot="activate" class="btn btn-primary btn-lg">Set up WiFi via Bluetooth</button>
  <div slot="unsupported" class="alert alert-warning mb-0 text-center" role="alert" id="improv-unsupported-msg">
    <span id="improv-unsupported-generic">Your browser doesn't support Web Bluetooth. This normally works out of the box on Windows, macOS, ChromeOS and Android — please use Chrome or Edge.</span>
    <span id="improv-unsupported-linux" style="display:none">
      Chrome/Edge on Linux ships Bluetooth support turned off by default. Enable it: paste <code>chrome://flags/#enable-web-bluetooth</code> into the address bar, set it to <strong>Enabled</strong>, then relaunch the browser. Prefer not to? Use the <a href="#option-b-usb-serial">USB option</a> below instead — no flag needed.
    </span>
  </div>
  <div slot="not-allowed" class="alert alert-danger mb-0 text-center" role="alert">
    Bluetooth provisioning needs HTTPS. You're seeing this by mistake — please <a href="https://openmower.de">reload over https://</a>.
  </div>
</improv-wifi-launch-button>
</div>

### Option B: USB (Serial)
{{% alert title="Browser support" color="warning" %}}
Requires **Web Serial**: **Google Chrome**, **Microsoft Edge**, or **Firefox 151+**, desktop only (Windows, macOS, Linux, ChromeOS) — no flags to enable, works out of the box.

**Not supported at all:** Safari, and any browser on iOS/iPadOS or Android.
{{% /alert %}}

Plug the Micro USB cable into your computer, click the button below, then pick the mower's port from the browser's port picker.

<div class="d-flex flex-column align-items-center my-4">
<improv-wifi-serial-launch-button class="improv-launch">
  <button slot="activate" class="btn btn-primary btn-lg">Set up WiFi via USB</button>
  <div slot="unsupported" class="alert alert-warning mb-0 text-center" role="alert">
    Your browser doesn't support Web Serial. Please use Chrome or Edge on a desktop computer.
  </div>
  <div slot="not-allowed" class="alert alert-danger mb-0 text-center" role="alert">
    USB provisioning needs HTTPS. You're seeing this by mistake — please <a href="https://openmower.de">reload over https://</a>.
  </div>
</improv-wifi-serial-launch-button>
</div>

### Option C: Manual via Terminal
For advanced users, or as a last resort if neither Bluetooth nor USB provisioning works: connect directly to the mower and configure WiFi by hand.

**Connect — pick one:**
- **Ethernet**: plug a cable directly between your computer and the mower's Ethernet port. The mower serves itself `172.16.78.1` on a `172.16.78.0/24` network and hands your computer an address via DHCP. Then: `ssh root@172.16.78.1` (password `openmower`).
- **USB Serial**: plug a Micro USB cable into the core board. A serial device shows up on your computer (e.g. `/dev/ttyACM0` on Linux/macOS, a `COM` port on Windows) — open it with a serial terminal (`screen`, `minicom`, PuTTY, etc., any baud rate works) and log in as `root` (password `openmower`). If two serial ports show up, use the first one — the second is reserved for the USB provisioning method above.

**Configure WiFi:**
```bash
mkdir -p /data/wifi
cat > /data/wifi/wpa_supplicant-wlan0.conf <<'EOF'
ctrl_interface=/var/run/wpa_supplicant
update_config=0

network={
	ssid="YourSSID"
	psk="YourPassword"
}
EOF
chmod 600 /data/wifi/wpa_supplicant-wlan0.conf
systemctl restart wpa_supplicant@wlan0.service
```
For an open network with no password, replace the `psk="..."` line with `key_mgmt=NONE`.

**Verify it worked:**
```bash
systemctl status wpa_supplicant@wlan0.service
ip -4 addr show wlan0
```

**To reset and provision a different network later:**
```bash
rm /data/wifi/wpa_supplicant-wlan0.conf
reboot
```

<style>
improv-wifi-launch-button.improv-launch,
improv-wifi-serial-launch-button.improv-launch {
  display: block;
  --improv-primary-color: #1B9D52;
  --improv-on-primary-color: #fff;
}
improv-wifi-launch-button.improv-launch [slot="unsupported"],
improv-wifi-launch-button.improv-launch [slot="not-allowed"],
improv-wifi-serial-launch-button.improv-launch [slot="unsupported"],
improv-wifi-serial-launch-button.improv-launch [slot="not-allowed"] {
  max-width: 480px;
  margin-left: auto;
  margin-right: auto;
}
</style>
<script>
(function () {
  var isLinux = (navigator.userAgentData && navigator.userAgentData.platform === "Linux")
    || (!navigator.userAgentData && /Linux/.test(navigator.platform) && !/Android/.test(navigator.userAgent));
  if (!isLinux) return;
  var generic = document.getElementById("improv-unsupported-generic");
  var linux = document.getElementById("improv-unsupported-linux");
  if (generic) generic.style.display = "none";
  if (linux) linux.style.display = "";
})();
</script>
{{< script-src src="js/improv-wifi/launch-button.js" >}}
{{< script-src src="js/improv-wifi/serial-launch-button.js" >}}

## Step 3: Enter your WiFi credentials
A dialog opens on this page once the mower is connected. Select your home WiFi network, enter the password and confirm. The mower will connect and the dialog will confirm success.

## Step 4: Check the connection
- From another device on your network: `ping openmower.local`
- SSH: `ssh root@openmower.local` (password `openmower`)
- Browser terminal: [http://openmower.local:7681/](http://openmower.local:7681/)

## Troubleshooting
- **No device found in the Bluetooth picker**: make sure the mower is powered on, within a few meters, and that Bluetooth is enabled on your device.
- **No port found in the USB picker**: make sure the Micro USB cable is properly connected to the core board and your computer, and that it's a data cable (not charge-only).
- **"Your browser doesn't support Web Bluetooth" on Linux**: this is Chrome/Edge shipping the feature off by default, not a real limitation — enable it via `chrome://flags/#enable-web-bluetooth` and relaunch, or use the USB option instead.
- **"Your browser doesn't support Web Bluetooth/Serial" elsewhere**: switch to Chrome or Edge (Bluetooth or USB), or Firefox 151+ (USB only). iOS/iPadOS isn't supported by any browser there — it's an Apple platform restriction, not something we can work around.
- **Connection fails / times out**: move closer to the mower (Bluetooth) or check the cable (USB) and try again. If it keeps failing, double-check the WiFi password and that you selected a 2.4GHz network if your mower doesn't support 5GHz.
- **Already provisioned and want to change networks**: run through this guide again — entering new credentials overwrites the old ones.
- **Neither browser method works**: fall back to [Option C](#option-c-manual-via-terminal) and configure WiFi directly over SSH or a serial console.
