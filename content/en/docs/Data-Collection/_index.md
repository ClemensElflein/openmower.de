---
title: "Data Collection"
linkTitle: "Data Collection"
weight: 995
description: >
  What data your mower sends, and when.
---

## What this page covers
This page explains what data your mower (running OpenMowerOS) sends over the network, and why. For how the openmower.de website itself handles cookies and analytics, see our [Privacy Policy]({{< param name="privacy_policy" >}}) instead.

## OS update checks
OpenMowerOS automatically checks for available updates once per day. It does not auto update: if a new version is available, you'll see a prompt the next time you run the `openmower` command, and in the future also inside the app.

Each check sends a request to our update server containing:

- **Your IP address**, inherent to any network request. Used only to serve the response, not logged or stored beyond normal request handling.
- **A unique device ID**, a random identifier generated on your device. It cannot be resolved to you or to your mower's owner. We don't collect names, emails, or any other identifying information alongside it.
- **The OS version currently installed**, so the server can tell whether a newer version is available.

That's it. No location data, no usage statistics, no telemetry about how you use your mower.

### Disabling this check
Create an empty file at `/data/openmower/no-update-check` on the device (e.g. `touch /data/openmower/no-update-check` over SSH) and the daily check stops running. Delete the file to turn it back on.

## Why we collect this
- **IP address**: technically required to respond to the request, like with any server on the internet.
- **Unique device ID**: lets us see roughly how many active installations exist and on which versions, without identifying individual users. This is also how we judge whether a new OS version is mature enough to mark as the latest stable release: seeing a version running successfully on many distinct devices for a while gives us confidence it's safe to recommend broadly, rather than promoting it the day it ships.
- **OS version**: needed to determine whether, and what, update to offer.

## Questions
If you have questions about this, reach out via our [Community]({{< relref "/community" >}}) channels.
