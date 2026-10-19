#!/usr/bin/env python3

import getpass
import hashlib
import hmac
import json
import os
import secrets
import sys
from pathlib import Path

ROOT = Path.home() / "CZH"
PLATFORM = ROOT / "Platform-v2"
PRIVATE = ROOT / "PrivateData"
AUTH_FILE = PRIVATE / "admin-auth.json"
MEMBERS_FILE = PRIVATE / "member-registry.json"
ACTIVITY_FILE = PRIVATE / "reports" / "activity.log"
ITERATIONS = 600_000


def save_auth(password):
    PRIVATE.mkdir(parents=True, exist_ok=True)
    os.chmod(PRIVATE, 0o700)

    salt = secrets.token_bytes(32)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, ITERATIONS
    )

    data = {
        "version": 1,
        "algorithm": "pbkdf2_sha256",
        "iterations": ITERATIONS,
        "salt": salt.hex(),
        "password_hash": digest.hex(),
    }

    temp = AUTH_FILE.with_suffix(".json.tmp")
    temp.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    os.chmod(temp, 0o600)
    temp.replace(AUTH_FILE)
    os.chmod(AUTH_FILE, 0o600)


def verify_password(password):
    try:
        data = json.loads(AUTH_FILE.read_text(encoding="utf-8"))
        if data.get("algorithm") != "pbkdf2_sha256":
            return False
        if int(data.get("iterations", 0)) != ITERATIONS:
            return False

        salt = bytes.fromhex(data["salt"])
        expected = bytes.fromhex(data["password_hash"])
        actual = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt, ITERATIONS
        )
        return hmac.compare_digest(actual, expected)
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError):
        return False


def setup_admin():
    if AUTH_FILE.exists():
        return True

    print("\n=== FIRST-TIME CZH ADMIN SETUP ===")
    print("Password kam bhi share mat karna.")
    print("Minimum 12 characters required.")

    first = getpass.getpass("Create admin password: ")
    if len(first) < 12:
        print("[ERROR] Password must be at least 12 characters.")
        return False

    second = getpass.getpass("Confirm admin password: ")
    if not hmac.compare_digest(first, second):
        print("[ERROR] Passwords do not match.")
        return False

    try:
        save_auth(first)
    except OSError as exc:
        print("[ERROR] Could not securely save admin configuration:", exc)
        return False

    print("[OK] Admin password hash saved privately.")
    return True


def login():
    if not setup_admin():
        return False

    print("\n=== CZH ADMIN AUTHENTICATION ===")
    for attempt in range(3):
        password = getpass.getpass("Admin password: ")
        if verify_password(password):
            print("[OK] Authentication successful.")
            return True
        print("[ERROR] Incorrect password.")

    print("[LOCKED] Too many failed attempts. Restart the command to try again.")
    return False


def member_count():
    try:
        data = json.loads(MEMBERS_FILE.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return str(len(data))
        return "Invalid registry structure"
    except FileNotFoundError:
        return "0 (registry not created)"
    except (OSError, json.JSONDecodeError):
        return "Registry unavailable or invalid"


def show_status():
    config = PLATFORM / "config" / "platform.conf"
    print("\n--- CZH PLATFORM OVERVIEW ---")
    print("Platform:", "CZH")
    print("Configuration:", "FOUND" if config.is_file() else "MISSING")
    print("Member registry count:", member_count())
    print("Admin authentication:", "CONFIGURED")
    print("Backend: Not connected by this local module")
    print("Local device only; no data is uploaded.")


def show_activity():
    print("\n--- RECENT LOCAL ACTIVITY ---")
    try:
        lines = ACTIVITY_FILE.read_text(encoding="utf-8").splitlines()
        if not lines:
            print("No activity entries yet.")
            return
        for line in lines[-15:]:
            print(line[:300])
    except FileNotFoundError:
        print("No local activity log found.")
    except OSError as exc:
        print("Cannot read activity log:", exc)


def main():
    if not login():
        return 1

    while True:
        print("\n================================")
        print("       CZH ADMIN CENTER")
        print("  CIPHER ZERO HACKERS")
        print("================================")
        print("1. Platform overview")
        print("2. Recent local activity")
        print("3. Exit Admin Center")

        choice = input("Select: ").strip()

        if choice == "1":
            show_status()
        elif choice == "2":
            show_activity()
        elif choice == "3":
            print("Admin session closed.")
            return 0
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print("\nAdmin session closed.")
        sys.exit(0)
