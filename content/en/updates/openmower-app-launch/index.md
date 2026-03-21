---
title: "Introducing the OpenMower App"
date: 2026-03-16
author: "Clemens Elflein"
description: "A brand new app for OpenMower is available to try — starting with a map editor. Works on OpenMowerOS v2 alongside the freshly released ROS v1.1.1."
---

Community member [@rovo89](https://github.com/rovo89) has been quietly building something great: the **OpenMower App**, a completely new application for your OpenMower mower.

You can find it here: **[github.com/xtech/openmower-app](https://github.com/xtech/openmower-app)**

### What's in it right now

At this stage, the app ships with a **map editor** and some debug information. The map editor is the part we wanted to get into people's hands first — it's the most useful starting point and lets you manage your mowing areas directly from the browser.

If you're running **OpenMowerOS v2**, adding it is straightforward:

1. Open `http://<mower-ip>:5001/compose/openmower` in your browser.
2. Switch to edit mode and add the following to your `compose.yaml`, above the `# Dockge-specific extras` line:

```yaml
  app:
    image: ghcr.io/xtech/openmower-app:edge
    container_name: app
    ports:
      - 3000:3000
    restart: unless-stopped
```

3. Also add the new URL to the `x-dockge` section:

```yaml
x-dockge:
  urls:
    - http://${HOSTNAME}:8080
    - http://${HOSTNAME}:3000
```

4. Hit **Deploy**. The app will be available at `http://<mower-ip>:3000`.

Not on OSv2? You can still try it by running the container manually.

### ROS version

You should be running **ROS v1.1.1**, which was [released at the same time]({{< relref "ros-v1-1-1" >}}). The map editor also works with v1.1.0, but it won't respect the "active" flag on mowing areas — so upgrade if you can.

### Why "OpenMower App"?

After some deliberation, we settled on **OpenMower App** even though it is a conflict with the current OpenMower App naming. The reasoing is that as the new app matures, the older one will be phased out and confusion will stop.

More features are on the way — great work rovo89, this is just the beginning.
