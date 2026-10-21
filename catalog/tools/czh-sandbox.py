#!/usr/bin/env python3
import os
import sys
import time
import random
import hashlib
from pathlib import Path

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; BG_G='\033[42m'; NC='\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def matrix_animation(duration, text):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    end_time = time.time() + duration
    while time.time() < end_time:
        line = "".join(random.choice(chars) for _ in range(45))
        sys.stdout.write(f"\r{C}  [*] {text} {D}{line}{NC}")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\r" + " " * 75 + "\r")

def progress_bar(seconds, prefix):
    for i in range(21):
        percent = i * 5
        bar = "█" * i + "░" * (20 - i)
        sys.stdout.write(f"\r{Y}  [+] {prefix} [{G}{bar}{Y}] {percent}%{NC}")
        sys.stdout.flush()
        time.sleep(seconds / 20)
    print("")

def analyze_file(file_path):
    clear()
    print(f"{C}")
    print("      ██████╗███████╗██╗  ██╗")
    print("     ██╔════╝╚══███╔╝██║  ██║")
    print("     ██║       ███╔╝ ███████║")
    print("     ██║      ███╔╝  ██╔══██║")
    print("     ╚██████╗███████╗██║  ██║")
    print("      ╚═════╝╚══════╝╚═╝  ╚═╝")
    print(f"{W}        M A L W A R E   S A N D B O X{NC}")
    print(f"{NC}")
    
    print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{BG_R}{W}  ☠  C Z H   M A L W A R E   S A N D B O X  ☠  {NC}")
    print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}\n")

    try:
        path = Path(os.path.expanduser(file_path))
        if not path.is_file():
            print(f"{R}  [✗] File not found. Please check the path.{NC}")
            input(f"\n{C}  Press Enter to return...{NC}")
            return

        # Get real hash for visual realism
        sha = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""): sha.update(chunk)
        file_hash = sha.hexdigest()
        file_size = path.stat().st_size

        print(f"{W}  [+] Target File : {C}{path.name}{NC}")
        print(f"{W}  [+] File Size   : {C}{file_size} bytes{NC}")
        print(f"{W}  [+] SHA-256     : {D}{file_hash}{NC}\n")

        print(f"{C}  [*] INITIALIZING SECURE SANDBOX ENVIRONMENT...{NC}")
        time.sleep(1)
        
        matrix_animation(1.5, "Unpacking payload...")
        progress_bar(1.5, "Extracting Strings")
        
        matrix_animation(1.5, "Analyzing Heuristics...")
        progress_bar(1.5, "Checking Virus Signatures")

        # Randomize Result (Mostly safe, sometimes suspicious)
        is_threat = random.choices([True, False], weights=[20, 80])[0]
        
        print(f"\n{G}  ┌───[ A N A L Y S I S   R E P O R T ]───────────────────────────┐{NC}")
        if is_threat:
            threat_name = random.choice(["Trojan.Win32.Fake", "Worm.Android.Fake", "Ransomware.Test", "Spyware.Simulated"])
            print(f"  {W}▶ Threat Level : {R}HIGH RISK{NC}")
            print(f"  {W}▶ Detection    : {R}{threat_name}{NC}")
            print(f"  {W}▶ Action       : {Y}Quarantine Recommended{NC}")
            print(f"{G}  ├──────────────────────────────────────────────────────────────┤{NC}")
            print(f"  {D}[!] Note: This is a simulated report for educational purposes.{NC}")
        else:
            print(f"  {W}▶ Threat Level : {G}CLEAN / SAFE{NC}")
            print(f"  {W}▶ Detection    : {G}No malicious signatures found.{NC}")
            print(f"  {W}▶ Action       : {G}File is safe to use.{NC}")
            print(f"{G}  ├──────────────────────────────────────────────────────────────┤{NC}")
            print(f"  {D}[!] Note: This is a simulated report for educational purposes.{NC}")
        
        print(f"{G}  └──────────────────────────────────────────────────────────────┘{NC}\n")

    except Exception as e:
        print(f"\n{R}  [✗] Error reading file: {e}{NC}")

    input(f"{C}  Press Enter to return...{NC}")

def main():
    while True:
        clear()
        print(f"{C}")
        print("      ██████╗███████╗██╗  ██╗")
        print("     ██╔════╝╚══███╔╝██║  ██║")
        print("     ██║       ███╔╝ ███████║")
        print("     ██║      ███╔╝  ██╔══██║")
        print("     ╚██████╗███████╗██║  ██║")
        print("      ╚═════╝╚══════╝╚═╝  ╚═╝")
        print(f"{W}        M A L W A R E   S A N D B O X{NC}")
        print(f"{NC}")
        
        print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
        print(f"  ║  ☠  C Z H   M A L W A R E   S A N D B O X  ☠                    ║")
        print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")

        print(f"{Y}  ⚠ NOTE: SIMULATOR ONLY. Safe for your files.{NC}\n")

        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} SCAN A FILE                            {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")

        choice = input(f"{R}  CZH-SANDBOX ➜ {NC}").strip()

        if choice == "1":
            f_path = input(f"\n{Y}  [?] Enter file path to scan (e.g., ~/test.txt): {NC}").strip()
            if f_path:
                analyze_file(f_path)
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH Sandbox closed. Stay Safe.{NC}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
