#!/usr/bin/env python3

import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.home() / "CZH"
DATA_DIR = ROOT / "PrivateData"
DATA_FILE = DATA_DIR / "member-registry.json"


def load_members():
    if not DATA_FILE.exists():
        return []

    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        raise RuntimeError(
            "Registry read nahi ho saki. Data ko manually inspect karo; "
            "automatic overwrite nahi kiya gaya."
        )


def save_members(members):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    os.chmod(DATA_DIR, 0o700)

    temporary = DATA_FILE.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(members, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.chmod(temporary, 0o600)
    temporary.replace(DATA_FILE)
    os.chmod(DATA_FILE, 0o600)


def register():
    print("\n=== CZH 2.0 MEMBER JOINING ===")
    print("AARHIV HACKERS | CIPHER ZERO HACKERS")
    print("Registration local device par save hogi.")
    print("Password, OTP, phone number ya private key mat do.\n")

    nickname = input("Member nickname: ").strip()
    if not nickname or len(nickname) > 40:
        print("Nickname required hai (maximum 40 characters).")
        return

    interests = input("Learning interests (comma-separated): ").strip()
    if len(interests) > 250:
        print("Interests bahut lambe hain.")
        return

    print("\nCZH Member Rules:")
    print("1. Sirf authorized systems par security testing.")
    print("2. Kisi ka password, account ya private data target nahi karna.")
    print("3. Team members ki privacy aur consent ka respect karna.")

    consent = input("\nKya aap rules aur local registration se sehmat hain? (yes/no): ")
    if consent.strip().lower() not in ("yes", "y"):
        print("Registration cancel. Koi member record save nahi hua.")
        return

    members = load_members()
    if any(m.get("nickname", "").casefold() == nickname.casefold()
           for m in members):
        print("Ye nickname local registry mein pehle se maujood hai.")
        return

    member = {
        "nickname": nickname,
        "interests": interests,
        "status": "registered-local",
        "rules_accepted": True,
        "registered_at": datetime.now(timezone.utc).isoformat(),
    }

    members.append(member)
    save_members(members)

    print("\nRegistration successful!")
    print("Nickname:", nickname)
    print("Status: REGISTERED LOCALLY")
    print("Registry:", DATA_FILE)
    print("Note: Is registration se online account ya central membership nahi banti.")


def show_directory():
    members = load_members()

    print("\n=== CZH LOCAL MEMBER DIRECTORY ===")
    print("Privacy: interests aur doosri personal details hide hain.")

    if not members:
        print("Abhi koi local member registered nahi hai.")
        return

    for number, member in enumerate(members, start=1):
        if not isinstance(member, dict):
            print(f"{number}. [Invalid record structure]")
            continue

        nickname = str(member.get("nickname", "Unknown"))
        status = str(member.get("status", "unknown"))
        registered = str(member.get("registered_at", "Unknown"))
        date = registered[:10] if len(registered) >= 10 else registered

        print(f"\n{number}. {nickname}")
        print(f"   Status: {status}")
        print(f"   Registered: {date or 'Unknown'}")

    print("\nNote: Ye directory sirf isi device ki registry dikhati hai.")


def main():
    while True:
        print("\n--- CZH MEMBER CENTER ---")
        print("1. Join CZH")
        print("2. Show local member count")
        print("3. Member Directory")
        print("4. Exit")

        choice = input("Select: ").strip()

        if choice == "1":
            try:
                register()
            except (OSError, RuntimeError) as exc:
                print("Safe stop:", exc)
        elif choice == "2":
            try:
                print("Local registered members:", len(load_members()))
            except (OSError, RuntimeError) as exc:
                print("Safe stop:", exc)
        elif choice == "3":
            try:
                show_directory()
            except (OSError, RuntimeError) as exc:
                print("Safe stop:", exc)
        elif choice == "4":
            print("CZH Member Center closed.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
