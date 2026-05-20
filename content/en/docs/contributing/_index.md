---
title: "Contributing"
linkTitle: "Contributing"
weight: 990
description: >
  How to contribute to OpenMower — code, firmware, documentation, and community.
---

OpenMower is a community project and contributions of all kinds are welcome — bug reports, code, documentation improvements, or simply helping others on Discord.

Not sure where to start? Read the [System Architecture]({{< relref "/docs/knowledge-base/architecture" >}}) overview to understand how the components fit together before diving into a specific repo.

## Contributing to these Docs

Improving the documentation is one of the easiest ways to contribute — no local tooling required for small fixes.

**For small changes** (typos, wording, adding a note): every page has an **Edit this page** button at the bottom. Click it, edit the file directly on GitHub, and open a pull request. Done.

**For larger changes** (new articles, restructuring): run the site locally with Docker — no dependencies to install beyond Docker itself.

1. [Fork the repository](https://github.com/ClemensElflein/openmower.de/fork) on GitHub.
2. Clone your fork:
   ```bash
   git clone https://github.com/<your-username>/openmower.de.git
   cd openmower.de
   ```
3. Start the local dev server:
   ```bash
   docker compose up
   ```
4. Open [http://localhost:8080](http://localhost:8080) in your browser. The site rebuilds automatically as you save files. If you see `502 Bad Gateway`, wait a moment — it's still starting up.
5. When you're happy with your changes, stop the server with <kbd>Ctrl</kbd>+<kbd>C</kbd>, commit, push, and open a pull request against the main repository.

The docs are written in Markdown using the [Hugo Docsy](https://www.docsy.dev/) theme.

## Code Contributions

{{% alert title="Before starting large changes" color="warning" %}}
Open an issue first to discuss your approach before investing time in an implementation. Someone may already be working on the same thing, and there are often existing architectural decisions that affect how something should be built. A quick discussion can save you a lot of wasted effort — and makes it much more likely your PR gets merged.

You can also head to the **#software** channel on [Discord](https://discord.gg/jE7QNaSxW7) to talk through your idea before writing any code.
{{% /alert %}}

OpenMower is split across several repositories — one per concern. This keeps each repo focused and lets hardware, firmware, and software evolve independently without changes in one area breaking unrelated parts.

### Software

| Repository | What it covers |
|---|---|
| [open_mower_ros](https://github.com/ClemensElflein/open_mower_ros) | ROS software — navigation and planning |
| [openmower-app](https://github.com/xtech/openmower-app) | The OpenMower mobile and web app |
| [OpenMowerOS](https://github.com/ClemensElflein/OpenMowerOS) | The operating system image |

### Firmware

| Repository | What it covers |
|---|---|
| [fw-openmower-v2](https://github.com/xtech/fw-openmower-v2) | Mainboard firmware — motor control, sensor drivers, hardware abstraction |
| [xesc_firmware](https://github.com/ClemensElflein/xesc_firmware) | xESC motor controller firmware |

### Hardware

| Repository | What it covers |
|---|---|
| [hw-openmower-universal](https://github.com/xtech/hw-openmower-universal) | Universal Mainboard |
| [hw-openmower-yardforce](https://github.com/xtech/hw-openmower-yardforce) | Yardforce Mainboard |
| [hw-openmower-sabo](https://github.com/xtech/hw-openmower-sabo) | Sabo / John Deere Mainboard |

## Reporting Issues

- **Software bugs** — open an issue in the relevant GitHub repository.
- **Documentation errors** — open an issue or PR in [openmower.de](https://github.com/ClemensElflein/openmower.de).
- **Questions and general discussion** — use [Discord](https://discord.gg/jE7QNaSxW7).

## Supporting the Project

OpenMower is developed and maintained in free time. If you'd like to support the project financially, you can do so via [Patreon](https://patreon.com/ClemensElflein).

---

## Code of Conduct

OpenMower is an open and welcoming project. Everyone participating — in GitHub issues, pull requests, Discord, or anywhere else in the community — is expected to follow these guidelines.

### Be respectful

Treat everyone with respect. Disagreement is fine; personal attacks, harassment, and discriminatory language are not. This applies regardless of experience level, background, or the type of contribution someone makes.

### Be constructive

When giving feedback, focus on the work, not the person. Explain *why* something should change, not just *that* it should. Everyone was a beginner once.

### Be patient

OpenMower is a volunteer-driven project. Maintainers and contributors have limited time. If a response takes a while, that is normal — a polite follow-up after a few days is fine.

### Stay on topic

Keep discussions relevant to OpenMower and the matter at hand. Off-topic conversations belong in the appropriate Discord channels.

### Assume good faith

Most people are trying to help. If something reads as rude or confusing, consider that it may simply be a language or communication style difference before escalating.

### Enforcement

Behaviour that violates these guidelines may result in a warning or, for repeated or severe violations, removal from the community spaces. Decisions are made by the project maintainers.
