# CZH 2.0 — Installation Guide

**Status:** Development documentation; clean installation is not yet verified.

## Before You Begin

1. Back up important Termux files and data.
2. Use a test environment if possible.
3. Review the repository source before running any script.
4. Never share passwords, access tokens, or private configuration files.

## Current Status

A verified, one-command installation procedure is not available yet.
The development repository must not be treated as a stable installer.

## Prepare Termux

Install or update Termux using a trusted distribution source.

After opening Termux, update its package lists:

    pkg update

Do not install additional dependencies until they have been confirmed
against the actual requirements of the selected CZH modules.

## Obtain the Source

The public development repository is:

https://github.com/Khana786/CZH-2.0

You can inspect or download the source from GitHub. Review the files
before executing any scripts.

## Verification

Before testing an installation:

- Identify the required dependencies.
- Review commands and scripts for unexpected file or network changes.
- Confirm that private data and credentials are not included.
- Test in a clean environment and document the results.
- Record any errors and supported Android/Termux versions.

## Troubleshooting

No verified clean-install troubleshooting procedure is available yet.
Do not delete existing CZH data or configuration to resolve an error
without first making a backup.

## Important Notice

CZH 2.0 is under development. This guide does not claim that installation
has been tested or that all modules work on every Android device.
