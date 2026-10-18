# CZH 2.0 — Cipher Zero Hackers

**Community:** AARHIV HACKERS  
**Organization:** CIPHER ZERO HACKERS  
**Version:** 2.0.0-dev  
**Status:** Development — Not a stable release

## About

CZH is a Termux-oriented project focused on ethical cybersecurity
learning, local utilities, and responsible security awareness.

The project is under active development. Features, installation
procedures, and security controls require verification before a
stable release can be announced.

## Project Goals

- Provide useful, public-safe cybersecurity learning utilities.
- Encourage responsible and authorized security testing.
- Keep private member information and credentials out of public releases.
- Document setup, testing, and security limitations.
- Evaluate backend services only when genuinely needed and with consent.

## Development Features

The public development tree includes:

- CZH command hub.
- Local diagnostic utilities.
- File SHA-256 integrity checking.
- DNS lookup utilities.
- HTTPS/TLS certificate checks.
- HTTP security-header checks.
- Documentation for tools, labs, and projects.
- Offline Cyber Academy with 10 structured modules and local progress tracking.

Availability and behavior must be verified against the actual source code.
Do not assume every feature has passed testing.

## Cyber Academy

CZH includes an offline, terminal-based Cyber Academy with 10 core modules:
- Termux & Linux
- Files & Permissions
- Networking Core
- HTTPS & TLS
- SHA-256 Integrity
- Password Defense
- Anti-Phishing
- Device Security
- Security Headers
- Backups & Logs

Each module includes a mission brief, key concepts, practice steps, safety notes, and a quick knowledge check (quiz). Learning progress is stored locally on the device and is never uploaded.

Access the Academy from the CZH Mission Control menu by selecting `[06] Cyber Academy`.

## Requirements

- Android device with Termux.
- A compatible Python environment for Python-based utilities.
- Network access for features that query external services.

Exact dependency and compatibility requirements are still being documented.

## Installation

**A verified clean-install procedure is not yet available.**

Do not run unreviewed scripts from this development repository on a
production device. Back up important data before testing.

See `INSTALLATION.md` for the current development guidance.

## Security and Privacy

- Use security utilities only on systems you own or have permission to test.
- Do not commit passwords, access tokens, private member records,
  local configuration, backups, or AI model files.
- Review scripts before executing them.
- Report suspected security or privacy issues privately to the maintainer.
- No claim of a completed security audit is being made.

## Backend Status

A central backend is not configured in this development release.
Do not assume that registration, synchronization, or remote services
are available.

## Roadmap

- [ ] Review public-safe modules.
- [ ] Document dependencies and supported environments.
- [ ] Add repeatable tests.
- [ ] Verify clean installation on a fresh Termux environment.
- [ ] Complete security and privacy review.
- [ ] Configure a backend only if needed and with appropriate consent.
- [ ] Select a license.
- [ ] Publish a stable release after verification.

## License

No license has been selected yet. Until a license is added, do not
assume that this repository grants permission to redistribute or reuse
its code.

## Project Status

CZH 2.0 is a development project, not a verified stable release.
Features and instructions may change as testing progresses.
