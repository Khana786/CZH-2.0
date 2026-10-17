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

LESSON_CONTENT = {
    1: {"overview": ["The shell is a text interface to your operating system.", "Termux provides a Linux-like environment on Android.", "Every command you type is parsed by the shell before execution."], "concepts": ["pwd - print working directory", "ls - list directory contents", "cd - change directory", "whoami - show current user name", "man <cmd> - read the manual for a command"], "practice": ["Run: pwd", "Run: ls", "Run: whoami", "Run: mkdir czh_test && cd czh_test && pwd"], "safety": "Read-only commands are safe. Never run commands from untrusted sources."},
    2: {"overview": ["Every file and folder has a path in the filesystem.", "Permissions decide who can read, write, or execute a file."], "concepts": ["ls -l - show file permissions", "chmod 600 file - owner read/write only", "chmod 700 dir - owner full access only", "~ is home; . is current; .. is parent directory"], "practice": ["Run: ls -l", "Run: touch note.txt && ls -l note.txt", "Run: chmod 600 note.txt && ls -l note.txt"], "safety": "Avoid chmod 777. Never loosen system file permissions unnecessarily."},
    3: {"overview": ["Networks exchange packets between devices.", "Every device has an IP address; every service uses a port."], "concepts": ["IPv4 example: 192.168.1.1", "IPv6 example: ::1", "DNS translates names to IP addresses", "Common ports: 80 HTTP, 443 HTTPS, 22 SSH"], "practice": ["Run: czh-tools then choose DNS lookup", "Inspect a domain you own or have permission to test"], "safety": "Do not scan networks you do not own or lack permission for."},
    4: {"overview": ["HTTPS protects traffic using TLS encryption.", "Certificates prove the identity of the server."], "concepts": ["TLS - encrypted transport layer", "Certificate - signed proof of identity", "Issuer - Certificate Authority (CA)", "Expiration - certificate validity date"], "practice": ["Run: czh-tools then choose HTTPS certificate information", "Inspect issuer and expiration for a trusted site"], "safety": "Never bypass certificate warnings for untrusted sites."},
    5: {"overview": ["A hash is a fixed-size fingerprint of data.", "SHA-256 produces a 256-bit value from any input."], "concepts": ["Same input produces the same hash", "Different input produces a different hash (with high probability)", "A hash is one-way and is not encryption"], "practice": ["Run: czh-tools then choose File SHA-256 hash", "Compare result with a trusted published checksum"], "safety": "A matching hash only proves integrity if the reference checksum is trusted."},
    6: {"overview": ["Weak or reused passwords are a top cause of account compromise.", "Multifactor authentication (MFA) adds a second barrier."], "concepts": ["Use a unique password per account", "Store passwords in a password manager", "Enable MFA wherever possible", "Never share one-time codes"], "practice": ["List accounts where you reuse passwords", "Enable MFA on at least one account today"], "safety": "Never share passwords or one-time verification codes."},
    7: {"overview": ["Phishing tricks people into giving up credentials or data.", "Attackers mimic trusted senders and links."], "concepts": ["Check the sender domain carefully", "Hover over links before clicking", "Be suspicious of urgency and fear tactics", "Verify via a separate channel"], "practice": ["Open suspicious emails only in a safe analysis environment", "Do not enter credentials on unfamiliar pages"], "safety": "Never enter credentials on pages you did not navigate to yourself."},
    8: {"overview": ["Devices stay safer when kept updated and minimal.", "App permissions control what apps can access."], "concepts": ["Keep Android and apps updated", "Review permissions regularly", "Install only from trusted sources", "Uninstall apps you no longer use"], "practice": ["Open Android settings and review app permissions", "Uninstall at least one unused app"], "safety": "Review permissions carefully before granting access."},
    9: {"overview": ["HTTP security headers tell browsers how to protect users.", "They add defense against common web attacks."], "concepts": ["Strict-Transport-Security (HSTS) - force HTTPS", "Content-Security-Policy (CSP) - restrict sources", "X-Frame-Options - prevent clickjacking", "X-Content-Type-Options - stop MIME sniffing"], "practice": ["Run: czh-tools then choose HTTPS security headers", "Inspect headers for a site you own"], "safety": "A missing header alone does not prove vulnerability."},
    10: {"overview": ["Backups protect data against loss and ransomware.", "Logs help detect and investigate issues."], "concepts": ["Encrypt sensitive backups", "Test restoring backups", "Keep logs free of passwords and tokens", "Rotate and expire old logs"], "practice": ["Create a small encrypted archive of a test folder", "Restore it to a separate directory"], "safety": "Keep private keys and tokens out of logs and backups that leave the device."},
}

QUIZ = {
    1: {"q": "Which command prints the current working directory?", "choices": ["pwd", "cd", "ls"], "answer": "pwd", "why": "pwd prints the working directory."},
    2: {"q": "Which mode gives only the owner read+write?", "choices": ["777", "644", "600"], "answer": "600", "why": "600 = owner read+write, no access for others."},
    3: {"q": "Which protocol resolves domain names to IP addresses?", "choices": ["DNS", "HTTP", "FTP"], "answer": "DNS", "why": "DNS maps hostnames to IP addresses."},
    4: {"q": "TLS primarily provides:", "choices": ["Encryption + authentication", "Compression", "Routing"], "answer": "Encryption + authentication", "why": "TLS encrypts traffic and authenticates the server."},
    5: {"q": "A SHA-256 hash is best described as:", "choices": ["Reversible encryption", "Fixed-size fingerprint", "A password"], "answer": "Fixed-size fingerprint", "why": "Hashes are one-way fingerprints, not encryption."},
    6: {"q": "Which practice is best for account security?", "choices": ["Reuse one strong password", "Unique password per site + MFA", "Write on paper"], "answer": "Unique password per site + MFA", "why": "Unique passwords + MFA limit the impact of any single breach."},
    7: {"q": "Best first step for a suspicious email?", "choices": ["Click the link to check", "Reply for confirmation", "Verify sender via separate channel"], "answer": "Verify sender via separate channel", "why": "Never trust the suspicious channel itself."},
    8: {"q": "Which device habit reduces risk most?", "choices": ["Keep apps updated", "Install from any source", "Grant all permissions"], "answer": "Keep apps updated", "why": "Updates patch known vulnerabilities."},
    9: {"q": "Which header forces HTTPS?", "choices": ["HSTS", "CSP", "X-Frame-Options"], "answer": "HSTS", "why": "Strict-Transport-Security tells browsers to require HTTPS."},
    10: {"q": "A trustworthy backup must be:", "choices": ["Tested by restoring", "Never checked", "Unencrypted"], "answer": "Tested by restoring", "why": "An untested backup is not a reliable backup."},
}


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

    content = LESSON_CONTENT.get(number, {})
    if content:
        if "overview" in content:
            print(f"\n  {CYAN}OVERVIEW{R}")
            for item in content["overview"]:
                print(f"  {WHITE}- {item}{R}")
        if "concepts" in content:
            print(f"\n  {CYAN}KEY CONCEPTS{R}")
            for item in content["concepts"]:
                print(f"  {WHITE}- {item}{R}")
        if "practice" in content:
            print(f"\n  {CYAN}PRACTICE{R}")
            for item in content["practice"]:
                print(f"  {WHITE}  {item}{R}")
        if "safety" in content:
            print(f"\n  {YELLOW}SAFETY NOTE{R}")
            print(f"  {GRAY}{content['safety']}{R}")

    print()
    line("─", MAGENTA)

    quiz = QUIZ.get(number)
    if quiz and str(number) not in completed:
        print(f"  {CYAN}QUICK CHECK{R}")
        print(f"  {WHITE}{quiz['q']}{R}")
        for i, c in enumerate(quiz["choices"], 1):
            print(f"    {i}) {c}")
        try:
            pick = input(f"  {YELLOW}Your answer [1-{len(quiz['choices'])}]: {R}").strip()
            idx = int(pick) - 1
            if 0 <= idx < len(quiz["choices"]) and quiz["choices"][idx] == quiz["answer"]:
                print(f"  {GREEN}✔ Correct.{R}")
            else:
                print(f"  {YELLOW}✗ Not quite. Correct: {quiz['answer']}{R}")
            print(f"  {GRAY}{quiz['why']}{R}")
        except (ValueError, EOFError):
            print(f"  {GRAY}Quiz skipped.{R}")
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
