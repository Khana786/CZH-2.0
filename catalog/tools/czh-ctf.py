#!/usr/bin/env python3
import os
import sys
import time
import json
from pathlib import Path

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

PROGRESS_FILE = os.path.expanduser("~/CZH/PrivateData/ctf_progress.json")

# Define the CTF Levels
LEVELS = {
    1: {
        "title": "LEVEL 1: BASE64 DECODING",
        "brief": "Decode the following Base64 string to find the hidden flag:\nQ1pIe0Jhc2U2NF9NYXN0ZXJ9",
        "flag": "CZH{Base64_Master}",
        "hint": "Use czh-cipher option 1 to decode."
    },
    2: {
        "title": "LEVEL 2: CAESAR CIPHER",
        "brief": "The flag was encrypted using a Caesar cipher with a shift of +3. Decode it:\nFck{FDHVDU_BLSKHU}",
        "flag": "CZH{Caesar_Cipher}",
        "hint": "Shift the letters backwards by 3."
    },
    3: {
        "title": "LEVEL 3: HEX TRICKERY",
        "brief": "Convert the following HEX code back to text:\n435a487b4865785f4d61737465727d",
        "flag": "CZH{Hex_Master}",
        "hint": "Use czh-cipher option 3 to decode."
    },
    4: {
        "title": "LEVEL 4: THE FINAL CODE",
        "brief": "Decode this Morse code to get the final flag:\n-.-. --.. .... {-.-. -.-. .-. -.-- .--. - --- --. .-. .- .--. .... . .-.}",
        "flag": "CZH{CryptoGrapher}",
        "hint": "Morse code dots and dashes."
    }
}

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r') as f:
                data = json.load(f)
                return data.get("completed_level", 0)
        except:
            return 0
    return 0

def save_progress(level):
    os.makedirs(os.path.dirname(PROGRESS_FILE), exist_ok=True)
    with open(PROGRESS_FILE, 'w') as f:
        json.dump({"completed_level": level}, f)

def play_ctf():
    while True:
        clear()
        current_level = load_progress()
        
        print(f"{C}")
        print("      ██████╗████████╗███████╗")
        print("     ██╔════╝╚══██╔══╝██╔════╝")
        print("     ██║        ██║   █████╗  ")
        print("     ██║        ██║   ██╔══╝  ")
        print("     ╚██████╗   ██║   ██║     ")
        print("      ╚═════╝   ╚═╝   ╚═╝     ")
        print(f"{NC}")
        print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
        print(f"{BG_R}{W}  ║  ☠  C Z H   M I N I - C T F   A R E N A  ☠                       ║{NC}")
        print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")

        if current_level >= 4:
            print(f"{G}  🎉 CONGRATULATIONS! You have completed all 4 levels of the CZH CTF!{NC}")
            print(f"{W}  You are now officially a CZH Flag Master.{NC}")
            print(f"\n{C}  Type 'reset' to play again, or 'exit' to return.{NC}")
            cmd = input(f"{R}  CZH-CTF ➜ {NC}").strip().lower()
            if cmd == 'reset':
                save_progress(0)
                continue
            elif cmd == 'exit':
                return
            else:
                continue

        next_level = current_level + 1
        level_data = LEVELS[next_level]
        
        print(f"{Y}  [+] CURRENT PROGRESS: Level {current_level}/4 Completed{NC}")
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {W}{level_data['title']:<42} {C}│{NC}")
        print(f"  {C}│{NC}                                            {C}│{NC}")
        print(f"  {C}│{NC} {D}HINT: {level_data['hint']:<35} {C}│{NC}")
        print(f"  {C}└────────────────────────────────────────────┘{NC}\n")
        
        print(f"{W}  {level_data['brief'].replace(chr(10), chr(10) + '  ')}{NC}\n")
        
        answer = input(f"{R}  [?] Enter the Flag (or 'exit'): {NC}").strip()
        
        if answer.lower() == 'exit':
            break
            
        if answer == level_data['flag']:
            print(f"\n{G}  [✓] CORRECT! Flag accepted.{NC}")
            save_progress(next_level)
            time.sleep(1.5)
        else:
            print(f"\n{R}  [✗] INCORRECT. Try again or use the hint.{NC}")
            input(f"{C}  Press Enter to retry...{NC}")

def main():
    while True:
        clear()
        print(f"{C}")
        print("      ██████╗████████╗███████╗")
        print("     ██╔════╝╚══██╔══╝██╔════╝")
        print("     ██║        ██║   █████╗  ")
        print("     ██║        ██║   ██╔══╝  ")
        print("     ╚██████╗   ██║   ██║     ")
        print("      ╚═════╝   ╚═╝   ╚═╝     ")
        print(f"{NC}")
        print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
        print(f"  ║  ☠  C Z H   C A P T U R E   T H E   F L A G  ☠                   ║")
        print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")
        
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} START / CONTINUE CTF                    {C}│{NC}")
        print(f"  {C}│{NC} {Y}[2]{W} RESET PROGRESS                        {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")
        
        choice = input(f"{R}  CZH-CTF ➜ {NC}").strip()
        
        if choice == "1":
            play_ctf()
        elif choice == "2":
            save_progress(0)
            print(f"\n{G}  [✓] CTF Progress Reset.{NC}")
            time.sleep(1)
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH CTF Arena closed. Stay Ethical.{NC}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
