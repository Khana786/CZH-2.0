# CZH 2.0 — Cipher Zero Hackers

**Community:** AARHIV HACKERS  
**Project:** White Hat Cyber Lab  
**Version:** 2.0.0-dev  
**Principle:** Learn • Secure • Defend

CZH is an Android Termux-based cybersecurity learning project focused on
ethical diagnostics, file integrity, platform health and beginner-friendly
security education.

## Available Features

- Platform health and local system monitoring
- DNS lookup for hostnames
- HTTPS/TLS certificate information
- HTTPS security-header review
- SHA-256 file hashing and local integrity baselines
- Local member registration with consent
- Password-protected local admin center
- Learning labs and project/tool catalogs
- Local diagnostic and status reports

## Requirements

- Android device with Termux
- Bash
- Python 3
- Git and curl for the existing setup workflows

## Current Status

This project is under active development (`2.0.0-dev`).
Features have been manually tested in the developer's local environment.
A clean installation on another device, full automated test suite and
public deployment review have not yet been completed.

The central backend is not configured. Member registration is local to
the device; it does not create a central online account.

## Safety and Privacy

- Use diagnostic tools only on systems you own or are authorized to test.
- Missing HTTP security headers alone do not establish a vulnerability.
- Never commit passwords, private keys, API tokens, member registries,
  private reports, recovery archives or personal data.
- Do not treat local monitoring as remote or continuous surveillance.
- Review scripts before running them and back up important data first.

## Installation

Installation instructions are being prepared. Do not run unreviewed
scripts copied from this development project on a production device.

## Roadmap

- Review and document public-safe modules
- Add repeatable tests and clean-install instructions
- Complete security and privacy review
- Configure and test a backend only if needed and consented to
- Publish a stable release after verification

## License

No license has been selected yet. Until one is added, all rights remain
with the respective copyright holder; reuse and redistribution are not
automatically permitted.
