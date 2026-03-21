---
title: "New Website Design & OpenMower Brand System"
date: 2026-03-21
author: "Clemens Elflein"
description: "The documentation site has been redesigned from the ground up, and we've published the first official OpenMower brand system."
---

The docs at openmower.de just got a complete visual overhaul — and alongside it, we're publishing the first official **OpenMower brand system**.

### **What Changed on the Site**

The site now runs a fully custom theme built directly on OpenMower design tokens: self-hosted DM Sans and DM Mono fonts, a cohesive green-on-dark colour palette, and a homepage that leads with what the project actually is — a GPL-licensed, ROS and RTOS-based platform that replaces the closed, manufacturer-controlled firmware of robotic mowers. No lock-in. No black boxes.

### **The OpenMower Brand System**

We now have a proper, versioned design system — [`design-openmower-branding`](https://github.com/ClemensElflein/OpenMower) — that gives the project a consistent visual identity across any platform:

- **Colour palette** — Primary green `#1B9D52`, dark graphite surfaces, amber code accents
- **Typography** — DM Sans Variable + DM Mono across all weights
- **Component library** — Buttons, cards, alerts, tables, inputs — all token-driven and documented
- **Logo assets** — Full wordmark SVG and square icon mark, ready for headers, favicons, and marketing
- **Machine-readable tokens** — `tokens.json` as the single source of truth, with an AI-optimised token file and a Theme Factory JSON for Claude Code

The theme ships as a **Material UI v6 theme** you can drop into any React/MUI project. The design tokens are format-agnostic — Tailwind and CSS custom properties mappings are included too.

**Live demo →** [https://xtech.github.io/design-openmower-branding/](https://xtech.github.io/design-openmower-branding/)

Brand assets are CC BY-NC-SA 4.0. Theme code is MIT.
