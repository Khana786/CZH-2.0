#!/usr/bin/env python3
"""Read-only CZH admin overview; no privileged actions are performed."""

from pathlib import Path
import os

root = Path(os.environ.get("CZH_PLATFORM_ROOT", Path.home() / "CZH/Platform-v2"))

print("=== CZH ADMIN CENTER ===")
print("Mode: READ-ONLY")
print(f"Platform root: {root}")
print(f"Root exists: {root.is_dir()}")
print("No settings changed.")
