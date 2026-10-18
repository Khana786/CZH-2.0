# CZH Ethical Security Projects

**CIPHER ZERO HACKERS — LEARN • SECURE • DEFEND**

Version: 2.0.0-dev  
Status: Project catalog; implementations may be pending.

## Projects

| ID | Project | Purpose | Status |
|---|---|---|---|
| CZH-P01 | Network Health Inspector | Inspect basic network connectivity and local interface information | Implemented in `czh-tools` (option 6) |
| CZH-P02 | DNS & Domain Inspector | Perform DNS lookups and explain the results | Implemented in `czh-tools` (option 1) |
| CZH-P03 | HTTPS/TLS Inspector | Check certificate validity and HTTPS security headers | Implemented in `czh-tools` (options 2 and 3) |
| CZH-P04 | File Integrity Checker | Calculate SHA-256 hashes to help detect file changes | Implemented: `czh-integrity` and `czh-tools` (option 4) |
| CZH-P05 | Security Learning Lab | Guided beginner exercises using owned or explicitly authorized targets | Implemented: `[06] Cyber Academy` and practical labs |
| CZH-P06 | Local Platform Doctor | Check CZH configuration and report problems without changing files | Implemented and locally tested: `czh-doctor` |

## Safety rules

- Test only devices, systems, and domains you own or have explicit permission to assess.
- No stealth, credential theft, unauthorized access, or destructive testing.
- Explain what each check does before running it.
- Prefer read-only checks; back up files before changes.
- Do not transmit member data or local activity logs without informed consent and a configured backend.

## Development policy

This file is a catalog, not proof that every listed project is implemented.
Each project must be implemented and tested separately before its status is changed.
