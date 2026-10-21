#!/usr/bin/env python3
import os
import sys
import time
import base64
import random
import string
from pathlib import Path

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

SANDBOX_DIR = Path.home() / "CZH_RANSOMWARE_SANDBOX"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def setup_sandbox():
    if not SANDBOX_DIR.exists():
        SANDBOX_DIR.mkdir(parents=True)
        for i in range(1, 6):
            (SANDBOX_DIR / f"victim_file_{i}.txt").write_text(f"This is a very important personal document number {i}.\nDo not lose this data!")
        (SANDBOX_DIR / "passwords.txt").write_text("admin:password123\nuser:qwerty")

def get_files():
    return list(SANDBOX_DIR.glob("*"))

def encrypt_simulation():
    files = get_files()
    encrypted_count = 0
    for file in files:
        if file.suffix != ".czh_locked":
            try:
                data = file.read_bytes()
                # Simulate encryption (Base64 is safe and reversible)
                enc_data = base64.b64encode(data)
                file.write_bytes(enc_data)
                file.rename(file.with_suffix(file.suffix + ".czh_locked"))
                encrypted_count += 1
            except: pass
    return encrypted_count

def decrypt_simulation():
    files = list(SANDBOX_DIR.glob("*.czh_locked"))
    decrypted_count = 0
    for file in files:
        try:
            data = file.read_bytes()
            dec_data = base64.b64decode(data)
            file.write_bytes(dec_data)
            new_name = str(file).replace(".czh_locked", "")
            file.rename(new_name)
            decrypted_count += 1
        except: pass
    return decrypted_count

def ransomware_ui():
    clear()
    print(f"{R}")
    print("      ██████╗  █████╗ ███╗   ██╗███████╗ ██████╗ ███╗   ███╗")
    print("      ██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔═══██╗████╗ ████║")
    print("      ██████╔╝███████║██╔██╗ ██║███████╗██║   ██║██╔████╔██║")
    print("      ██╔══██╗██╔══██║██║╚██╗██║╚════██║██║   ██║██║╚██╔╝██║")
    print("      ██║  ██║██║  ██║██║ ╚████║███████║╚██████╔╝██║ ╚═╝ ██║")
    print("      ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝")
    print(f"{NC}")
    print(f"{BG_R}{W}  ☠  Y O U R   F I L E S   H A V E   B E E N   L O C K E D  ☠  {NC}\n")
    print(f"{W}  All your documents, photos, and databases are encrypted.{NC}")
    print(f"{W}  To decrypt your files, you must pay 0.5 Bitcoin to the address below:{NC}\n")
    print(f"  {Y}BTC Address: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa{NC}\n")
    print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{Y}  [!] THIS IS A SIMULATION. NO REAL FILES WERE HARMED.{NC}")
    print(f"{C}  [*] Type 'PAY' to simulate paying the ransom and unlock files.{NC}")
    print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}\n")

def main():
    setup_sandbox()
    
    while True:
        clear()
        print(f"{C}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print(f"{G}       ☠  C Z H  //  R A N S O M W A R E  S I M U L A T O R  ☠{NC}")
        print(f"{C}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}\n")
        
        files = get_files()
        locked = len([f for f in files if f.suffix == ".czh_locked"])
        
        print(f"{W}  [+] Sandbox Location: {D}{SANDBOX_DIR}{NC}")
        print(f"{W}  [+] Total Files     : {C}{len(files)}{NC}")
        print(f"{W}  [+] Locked Files    : {R if locked > 0 else G}{locked}{NC}\n")

        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} LAUNCH RANSOMWARE ATTACK             {C}│{NC}")
        print(f"  {C}│{NC} {Y}[2]{W} VIEW FILES IN SANDBOX                 {C}│{NC}")
        print(f"  {C}│{NC} {G}[3]{W} DECRYPT FILES (Restore Data)         {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")

        choice = input(f"{R}  CZH-RANSOM ➜ {NC}").strip()

        if choice == "1":
            if locked > 0:
                print(f"\n{R}  [✗] Files are already encrypted! Decrypt them first.{NC}")
                input(f"{C}  Press Enter...{NC}")
                continue
                
            print(f"\n{R}  [*] Deploying Payload...{NC}")
            time.sleep(1)
            count = encrypt_simulation()
            print(f"{R}  [*] Encrypting {count} files...{NC}")
            time.sleep(2)
            
            ransomware_ui()
            cmd = input(f"{R}  > {NC}").strip().upper()
            if cmd == "PAY":
                print(f"\n{G}  [*] Payment verified. Sending decryption key...{NC}")
                time.sleep(2)
                d_count = decrypt_simulation()
                print(f"{G}  [✓] {d_count} files have been restored successfully!{NC}")
            else:
                print(f"\n{R}  [✗] Incorrect input. Files remain locked.{NC}")
            input(f"\n{C}  Press Enter to return...{NC}")

        elif choice == "2":
            print(f"\n{C}  [*] Files in Sandbox:{NC}")
            for f in get_files():
                print(f"  {W}▶ {f.name}{NC}")
            input(f"\n{C}  Press Enter to return...{NC}")

        elif choice == "3":
            if locked == 0:
                print(f"\n{G}  [✓] No locked files found. Everything is safe.{NC}")
            else:
                print(f"\n{G}  [*] Bypassing ransomware and decrypting...{NC}")
                time.sleep(1)
                d_count = decrypt_simulation()
                print(f"{G}  [✓] {d_count} files decrypted successfully.{NC}")
            input(f"\n{C}  Press Enter to return...{NC}")

        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH Ransomware Simulator closed.{NC}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
