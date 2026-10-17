#!/usr/bin/env python3
"""CZH // CYBER ACADEMY — Premium Terminal Interface."""

import json
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = Path(os.environ.get("CZH_PRIVATE_ROOT", str(ROOT / "PrivateData")))
PROGRESS_FILE = DATA_DIR / "course-progress.json"

# CZH NEON COLOR SYSTEM
R = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
WHITE = "\033[97m"
GRAY = "\033[90m"

WIDTH = 58

LESSONS = [
    ("TERMUX & LINUX", "Learn what the shell does. Practice: pwd, ls, whoami."),
    ("FILES & PERMISSIONS", "Understand paths, ls -l, chmod and safe file handling."),
    ("NETWORKING CORE", "Learn IP addresses, DNS resolution, ports and network basics."),
    ("HTTPS & TLS", "Understand encryption, certificates and server authentication."),
    ("SHA-256 INTEGRITY", "Calculate a file hash and compare it with a trusted checksum."),
    ("PASSWORD DEFENSE", "Use unique passwords, password managers and multifactor authentication."),
    ("ANTI-PHISHING", "Recognize suspicious links, fake senders and credential theft attempts."),
    ("DEVICE SECURITY", "Update Android, review app permissions and install trusted software."),
    ("SECURITY HEADERS", "Learn HSTS, CSP, X-Frame-Options and browser security policies."),
    ("BACKUPS & LOGS", "Protect encrypted backups and avoid exposing passwords or access tokens."),
]


def line(char="━", color=CYAN):
    print(color + char * WIDTH + R)


def center(text, color=WHITE):
    print(color + text.center(WIDTH) + R)


def banner():
    print()
    line("━", MAGENTA)
    center("  CCCC    ZZZZZ    H   H", CYAN + BOLD)
    center(" C        Z   Z    H   H", CYAN + BOLD)
    center(" C        Z  Z     H   H", CYAN + BOLD)
    center(" C        Z Z      HHHHH", CYAN + BOLD)
    center(" C        ZZ       H   H", CYAN + BOLD)
    center("  CCCC    ZZZZZ    H   H", CYAN + BOLD)

    center("CZH  //  CIPHER ZERO HACKERS", MAGENTA + BOLD)
    center("CYBER ACADEMY  //  VERSION 2.0", GREEN)
    line("━", MAGENTA)
    center("[ CZH LEARN ]  ◆  [ SECURE ]  ◆  [ DEFEND ]", YELLOW)
    center("CZH OFFLINE TRAINING SYSTEM", GRAY)
    line("─", CYAN)


def load_progress():
    if not PROGRESS_FILE.exists():
        return set()

    try:
        data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        completed = data.get("completed", [])
        if not isinstance(completed, list):
            raise ValueError("Invalid progress format")
        return {str(x) for x in completed if str(x).isdigit()}
    except (OSError, json.JSONDecodeError, AttributeError, ValueError):
        print(f"\n{RED}[!] Progress file unreadable. Existing data preserved.{R}")
        return None


def save_progress(completed):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    try:
        DATA_DIR.chmod(0o700)
    except OSError:
        pass

    temp = PROGRESS_FILE.with_suffix(".json.tmp")
    temp.write_text(
        json.dumps({"completed": sorted(completed)}, indent=2) + "\n",
        encoding="utf-8",
    )

    try:
        temp.chmod(0o600)
    except OSError:
        pass

    temp.replace(PROGRESS_FILE)

    try:
        PROGRESS_FILE.chmod(0o600)
    except OSError:
        pass


def progress_bar(done, total, width=30):
    filled = int(width * done / total) if total else 0
    bar = GREEN + "█" * filled + GRAY + "░" * (width - filled) + R
    return f"{bar}  {CYAN}{done}/{total}{R}"


def dashboard(completed):
    os.system("clear" if os.name == "posix" else "cls")
    banner()

    valid = completed.intersection(str(i) for i in range(1, len(LESSONS) + 1))
    done = len(valid)

    print(f"\n  {MAGENTA}{BOLD}◈ CZH CYBER OPERATIONS CENTER{R}")
    print(f"  {GRAY}COURSE PROGRESS{R}")
    print(f"  {progress_bar(done, len(LESSONS))}\n")

    for i, (title, _) in enumerate(LESSONS, 1):
        if str(i) in completed:
            status = f"{GREEN}✔ COMPLETE{R}"
            number = f"{GREEN}[{i:02}]{R}"
        else:
            status = f"{CYAN}◈ READY{R}"
            number = f"{CYAN}[{i:02}]{R}"

        print(f"  {number} {WHITE}{title:<24}{R} {status}")

    line("─", MAGENTA)
    print(f"  {YELLOW}[C]{R} Reset progress     {YELLOW}[0]{R} Exit Academy")
    line("━", CYAN)


def open_lesson(number, completed):
    title, description = LESSONS[number - 1]

    os.system("clear" if os.name == "posix" else "cls")
    line("━", MAGENTA)
    center("CZH // OPERATIONS MODULE", CYAN + BOLD)
    center(f"MODULE {number:02}  ::  {title}", MAGENTA + BOLD)
    line("─", CYAN)

    print(f"\n  {YELLOW}MISSION BRIEF{R}")
    print(f"  {WHITE}{description}{R}")

    extra = {
        1: "Try pwd to see your current directory. Use ls to list files.",
        2: "Practice only inside a test folder. Avoid changing system file permissions.",
        3: "DNS maps domain names to addresses. A port identifies a service endpoint.",
        4: "Never bypass certificate warnings for sites you do not trust.",
        5: "A hash helps detect changes; it does not encrypt or hide file contents.",
        6: "Never share passwords or one-time verification codes.",
        7: "Open suspicious links only in a safe analysis environment; do not enter credentials.",
        8: "Review permissions carefully and keep your operating system updated.",
        9: "A missing header alone does not establish that a website is vulnerable.",
        10: "Test restoring backups and keep private keys and tokens out of logs.",
    }

    print(f"\n  {CYAN}FIELD NOTES{R}")
    print(f"  {GRAY}{extra[number]}{R}")
    print()
    line("─", MAGENTA)

    if str(number) in completed:
        print(f"  {GREEN}✔ This module is already marked complete.{R}")
        input(f"\n  {CYAN}Press Enter to return to Academy...{R}")
        return

    answer = input(
        f"  {YELLOW}Mark module complete? [y/N]: {R}"
    ).strip().lower()

    if answer == "y":
        completed.add(str(number))
        save_progress(completed)
        print(f"\n  {GREEN}{BOLD}✔ PROGRESS SAVED LOCALLY{R}")
        print(f"  {GRAY}Your progress remains on this device.{R}")
    else:
        print(f"\n  {GRAY}Module not marked complete.{R}")

    input(f"\n  {CYAN}Press Enter to return to Academy...{R}")


def main():
    if os.environ.get("NO_COLOR"):
        for name in ("R", "BOLD", "DIM", "CYAN", "MAGENTA", "GREEN",
                     "YELLOW", "RED", "BLUE", "WHITE", "GRAY"):
            globals()[name] = ""

    completed = load_progress()
    if completed is None:
        return

    while True:
        dashboard(completed)

        try:
            choice = input(f"\n  {MAGENTA}CZH@OPERATIONS{R} {CYAN}➜ {R}").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print(f"\n\n  {GREEN}Session terminated safely.{R}")
            return

        if choice == "0":
            print(f"\n  {CYAN}CZH OPERATIONS{R} {GRAY}// Session closed.{R}\n")
            return

        if choice == "c":
            confirm = input(f"  {RED}Type RESET to clear progress: {R}").strip()
            if confirm == "RESET":
                completed.clear()
                save_progress(completed)
                print(f"  {GREEN}Progress reset.{R}")
            continue

        if choice.isdigit() and 1 <= int(choice) <= len(LESSONS):
            open_lesson(int(choice), completed)
        else:
            print(f"  {RED}Unknown command. Select a module from the menu.{R}")
            input(f"  {GRAY}Press Enter to continue...{R}")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print(f"\n{CYAN}CZH Academy closed safely.{R}")
