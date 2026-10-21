#!/usr/bin/env python3
import os
import sys
import time
import hashlib
from pathlib import Path

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def generate_hashes(data, is_file=False):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    sha512 = hashlib.sha512()

    if is_file:
        try:
            with open(data, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    md5.update(chunk)
                    sha1.update(chunk)
                    sha256.update(chunk)
                    sha512.update(chunk)
        except Exception as e:
            return None
    else:
        md5.update(data.encode('utf-8'))
        sha1.update(data.encode('utf-8'))
        sha256.update(data.encode('utf-8'))
        sha512.update(data.encode('utf-8'))

    return {
        "MD5": md5.hexdigest(),
        "SHA-1": sha1.hexdigest(),
        "SHA-256": sha256.hexdigest(),
        "SHA-512": sha512.hexdigest()
    }

def display_results(title, hashes):
    print(f"\n{G}  ┌───[ H A S H   R E S U L T S ]──────────────────────────────────┐{NC}")
    print(f"  {W}▶ Target : {C}{title}{NC}")
    print(f"{G}  ├──────────────────────────────────────────────────────────────┤{NC}")
    for algo, h in hashes.items():
        print(f"  {Y}▶ {algo:<7}{NC} : {W}{h}{NC}")
    print(f"{G}  └──────────────────────────────────────────────────────────────┘{NC}\n")

def hash_menu():
    while True:
        clear()
        print(f"{C}")
        print("      ██╗  ██╗ █████╗ ███████╗██╗  ██╗")
        print("      ██║  ██║██╔══██╗██╔════╝██║  ██║")
        print("      ███████║███████║███████╗███████║")
        print("      ██╔══██║██╔══██║╚════██║██╔══██║")
        print("      ██║  ██║██║  ██║███████║██║  ██║")
        print("      ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
        print(f"{NC}")
        print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print(f"{BG_R}{W}  ☠  C Z H   H A S H   G E N E R A T O R  ☠                        {NC}")
        print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}\n")

        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} HASH A TEXT STRING                     {C}│{NC}")
        print(f"  {C}│{NC} {Y}[2]{W} HASH A FILE                            {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} BACK TO PREVIOUS MENU                  {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")

        choice = input(f"{R}  CZH-HASH ➜ {NC}").strip()

        if choice == "1":
            text = input(f"\n{Y}  [?] Enter text to hash: {NC}")
            if text:
                hashes = generate_hashes(text)
                display_results("TEXT INPUT", hashes)
                input(f"{C}  Press Enter to continue...{NC}")
        elif choice == "2":
            f_path = input(f"\n{Y}  [?] Enter file path (e.g., /sdcard/stego/imag.jpg): {NC}").strip()
            if f_path:
                path = Path(os.path.expanduser(f_path))
                if path.is_file():
                    print(f"{C}  [*] Calculating hashes... (Please wait){NC}")
                    time.sleep(0.5)
                    hashes = generate_hashes(str(path), is_file=True)
                    if hashes:
                        display_results(path.name, hashes)
                    else:
                        print(f"{R}  [✗] Error reading file.{NC}")
                else:
                    print(f"{R}  [✗] File not found! Check path.{NC}")
                input(f"{C}  Press Enter to continue...{NC}")
        elif choice in ["0", "00"]:
            break
        else:
            time.sleep(1)

def main():
    hash_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
