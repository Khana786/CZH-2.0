#!/usr/bin/env python3
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.home() / "CZH"
PRIVATE = ROOT / "PrivateData"
BASELINES = PRIVATE / "integrity-baselines.json"


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_baselines():
    try:
        data = json.loads(BASELINES.read_text(encoding="utf-8"))
        if isinstance(data, dict) and data.get("version") == 1:
            if isinstance(data.get("files"), dict):
                return data
        print("[ERROR] Baseline file has an invalid structure.")
    except FileNotFoundError:
        return {"version": 1, "files": {}}
    except (OSError, json.JSONDecodeError) as exc:
        print("[ERROR] Cannot read baseline file:", exc)
    return None


def save_baselines(data):
    PRIVATE.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE, 0o700)
    temp = BASELINES.with_suffix(".json.tmp")
    temp.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    os.chmod(temp, 0o600)
    temp.replace(BASELINES)
    os.chmod(BASELINES, 0o600)


def get_file():
    raw = input("Path to a file you own or may inspect: ").strip()
    if not raw:
        print("[ERROR] No path entered.")
        return None
    path = Path(os.path.expanduser(raw))
    try:
        path = path.resolve(strict=True)
        if not path.is_file():
            print("[ERROR] Path is not a regular file.")
            return None
        return path
    except (OSError, RuntimeError) as exc:
        print("[ERROR] Cannot access file:", exc)
        return None


def calculate():
    path = get_file()
    if path is None:
        return
    try:
        print("File:", path)
        print("SHA-256:", sha256_file(path))
    except OSError as exc:
        print("[ERROR] File read failed:", exc)


def save_baseline():
    path = get_file()
    if path is None:
        return
    try:
        digest = sha256_file(path)
        data = load_baselines()
        if data is None:
            return
        data["files"][str(path)] = {
            "sha256": digest,
            "saved_at": datetime.now(timezone.utc).isoformat()
        }
        save_baselines(data)
        print("[OK] Baseline saved privately.")
        print("File:", path)
        print("SHA-256:", digest)
        print("Storage:", BASELINES)
    except OSError as exc:
        print("[ERROR] Could not save baseline:", exc)


def verify_baseline():
    path = get_file()
    if path is None:
        return
    data = load_baselines()
    if data is None:
        return
    record = data["files"].get(str(path))
    if not record:
        print("[INFO] No baseline saved for this exact file path.")
        print("Choose option 2 first.")
        return
    try:
        current = sha256_file(path)
        print("File:", path)
        print("Saved SHA-256:", record["sha256"])
        print("Current SHA-256:", current)
        if current == record["sha256"]:
            print("[PASS] UNCHANGED — hash matches baseline.")
        else:
            print("[WARNING] CHANGED — hash differs from baseline.")
    except (OSError, KeyError, TypeError) as exc:
        print("[ERROR] Verification failed:", exc)


def main():
    while True:
        print("""
========================================
       CZH FILE INTEGRITY CHECKER
        CIPHER ZERO HACKERS
        LEARN • SECURE • DEFEND
========================================
1. Calculate SHA-256
2. Save local baseline
3. Verify against saved baseline
0. Exit
""")
        choice = input("Select option: ").strip()
        if choice == "1":
            calculate()
        elif choice == "2":
            save_baseline()
        elif choice == "3":
            verify_baseline()
        elif choice == "0":
            print("CZH Integrity Checker closed.")
            return
        else:
            print("Invalid option.")
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nCZH Integrity Checker closed.")
        sys.exit(0)
