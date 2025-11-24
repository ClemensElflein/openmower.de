---
title: "Overview"
linkTitle: "Overview"
weight: 1
description: General information about the Open Mower project.
carousel:
  - image: open_mower_app_1.jpg
  - image: open_mower_app_2.jpg
  - image: homeassistant_dashboard.png
  - image: smarthome_tracker.png
---

### Introduction and Vision

**OpenMower** is a pioneering project aimed at revolutionizing robotic lawn mowing through open-source collaboration. What started as a modest garage project has grown into a mature, community-driven initiative with robust hardware, advanced features, and a dedicated user base.

If you want to see a quick overview, you can check out this video:

<a href="https://www.youtube.com/watch?v=BSF04i3zNGw" target="_blank"><img src="https://user-images.githubusercontent.com/2864655/161540069-f4263fa7-a47b-49d2-a7bc-d1cdc3a47704.jpg" /></a>


### Key Features and Achievements

**Autonomous Lawn Mowing:** The device efficiently mows the lawn automatically, ensuring a neat and even cut.

**Good Safety:** Equipped with emergency stop features for enhanced safety.

**No Perimeter Wire Needed:** Supports flexible operation across multiple mowing areas without the need for perimeter wires.

**Open Source:** Committed to sharing knowledge and enabling others to build their own OpenMower.

**User-Friendly App:** The web app interface allows easy setup, control and management of the mower, from desktop or mobile phone.

**Smart Home Integration:** Seamlessly integrates with HomeAssistant, allowing for advanced automations and detailed monitoring.  
Users can view real-time data such as battery status, motor temperatures, and power sensors directly from their smart home dashboard.  
Additionally, the integration supports automations like pausing operations during rain and resuming once conditions improve, ensuring efficient and safe operation.

{{< carousel height="500" unit="px" items="4" duration="3000" >}}


### Supported Mowers

Open Mower replaces the electronics inside the robot mower with custom ones, so that we can gain full control of the robot's sensors and actuators.
Therefore, adding support for a new mower model means providing the electronics for that mower model.

Currently, there exist multiple Mainboard Versions, so the following mower models are supported:
- YardForce Classic 500, YardForce Classic 500B, YardForce SA650ECO and YardForce SA900ECO models, though the later two requires some extra work.
- SABO MOWit 500F (Series-I & II), John Deere Tango E5 (Series-I & II)
- Many others with the new v2 Universal Board (Ask on Discord, the Docs are not ready at the moment)

Also check the [Compatible Mowers Page]({{% relref "/docs/knowledge-base/compatible-mowers" %}}) for more infos.

### Community and Development

The OpenMower project thrives on the contributions of a vibrant community of hobbyists and professionals. Active discussions and collaborative efforts on platforms like Discord are continuously working on supporting a variety of other mower models, including the Worx Landroid, Fuxtec Redback, Bosch Indego, Lidl Parkside, and Viking MI 632. While these models are not yet officially supported out of the box, the collaborative efforts and shared knowledge in the community make it worthwhile to try adapting other models or join the discussion.


### Getting Started and Resources

Interested in joining the OpenMower project? Explore the following resources to get started:
- [Getting Started]({{% relref "/docs/getting-started/" %}}): Quick start guide to building your own OpenMower.
- [Links]({{% relref "/docs/links" %}}): Additional information, repositories, and the shop.
- [Compatible Mowers Page]({{% relref "/docs/knowledge-base/compatible-mowers" %}}): Comprehensive list of supported mower models.


### Project Goals and Future Plans

The OpenMower project continues to evolve with ambitious goals for the future. Planned features include obstacle detection, enhanced scheduling, and expanded compatibility with new mower models. Join us on this journey to redefine robotic lawn mowing.
