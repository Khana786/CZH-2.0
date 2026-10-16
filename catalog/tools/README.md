# CZH Ethical Security Toolkit

**CIPHER ZERO HACKERS — LEARN • SECURE • DEFEND**

Version: 2.0.0-dev

## Available tool module

| Tool | Purpose | Status |
|---|---|---|
| `czh-tools.py` | Ethical utility menu for DNS lookup, HTTPS/TLS certificate checks, security headers, SHA-256 file hashing, and local environment information | Existing module; launch and verify before use |
| `czh-integrity` | Calculate SHA-256, save a local file baseline, and detect changes against that baseline | Implemented and locally tested |

## Safe use

- Inspect only files, systems, and domains you own or have explicit permission to assess.
- DNS and HTTPS checks are informational; they do not guarantee a system is secure.
- File baselines are stored locally. Protect the device and private data.
- A changed hash indicates that file contents differ from the saved baseline; it does not by itself prove malicious activity.
- No hidden monitoring or automatic upload of local data is intended.

## Development status

This catalog documents known modules; it is not proof that every feature is production-ready. Verify each module before relying on it.
