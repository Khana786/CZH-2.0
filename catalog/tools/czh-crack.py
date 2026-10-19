#!/usr/bin/env python3
import os
import sys
import time
import hashlib
import random
import string

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

RAINBOW_FILE = os.path.expanduser("~/CZH/PrivateData/czh_rainbow.csv")

WORDLIST = [
    "admin", "password", "123456", "12345678", "qwerty", "hacker", "root", 
    "czh", "khan", "cyber", "letmein", "welcome", "abc123", "iloveyou",
    "admin123", "password123", "secret", "system", "shadow", "master"
]

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def matrix_animation(duration=2, text="LOOKING UP"):
    end_time = time.time() + duration
    chars = string.ascii_letters + string.digits
    while time.time() < end_time:
        line = "".join(random.choice(chars) for _ in range(30))
        sys.stdout.write(f"\r{C}  [*] {text}: {D}{line}{NC}")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\r" + " " * 60 + "\r")

# --- RAINBOW TABLE FUNCTIONS ---
def generate_rainbow():
    clear()
    print(f"{C}  [*] Generating Rainbow Table for MD5 & SHA-256...{NC}")
    os.makedirs(os.path.dirname(RAINBOW_FILE), exist_ok=True)
    
    with open(RAINBOW_FILE, "w") as f:
        f.write("password,md5,sha256\n")
        for word in WORDLIST:
            md5_h = hashlib.md5(word.encode()).hexdigest()
            sha256_h = hashlib.sha256(word.encode()).hexdigest()
            f.write(f"{word},{md5_h},{sha256_h}\n")
            sys.stdout.write(f"\r{Y}  [+] Precomputing: {W}{word:<15}{NC}")
            sys.stdout.flush()
            time.sleep(0.1)
            
    print(f"\n\n{G}  [✓] Rainbow Table Generated successfully!{NC}")
    print(f"{W}  Location: {C}{RAINBOW_FILE}{NC}")
    input(f"\n{C}  Press Enter to return...{NC}")

def lookup_rainbow(target_hash):
    clear()
    if not os.path.exists(RAINBOW_FILE):
        print(f"{R}  [✗] Rainbow Table not found! Please generate it first.{NC}")
        input(f"\n{C}  Press Enter to return...{NC}")
        return

    print(f"{C}  [*] Initializing Rainbow Table Lookup...{NC}")
    time.sleep(0.5)
    matrix_animation(1.5, "SEARCHING TABLE")
    
    found = False
    with open(RAINBOW_FILE, "r") as f:
        lines = f.readlines()[1:] # Skip header
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 3:
                word, md5_h, sha256_h = parts
                if target_hash.lower() == md5_h or target_hash.lower() == sha256_h:
                    print(f"{G}  ┌───[ R A I N B O W   H I T ]───────────────────────────────────┐{NC}")
                    print(f"  {W}▶ Password Found : {G}{word}{NC}")
                    print(f"  {W}▶ Status         : {G}INSTANT MATCH (0.01s){NC}")
                    print(f"{G}  └──────────────────────────────────────────────────────────────┘{NC}")
                    found = True
                    break
    
    if not found:
        print(f"{R}  ┌───[ N O   M A T C H ]─────────────────────────────────────────┐{NC}")
        print(f"  {W}▶ Status : {R}Hash not found in Rainbow Table.{NC}")
        print(f"  {W}▶ Tip    : {C}Generate table again or add custom hashes.{NC}")
        print(f"{R}  └──────────────────────────────────────────────────────────────┘{NC}")

def main():
    while True:
        clear()
        print(f"{C}")
        print("      ██████╗██████╗  █████╗  ██████╗██╗  ██╗")
        print("     ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝")
        print("     ██║     ██████╔╝███████║██║     █████╔╝ ")
        print("     ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ")
        print("     ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗")
        print("      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")
        print(f"{NC}")
        print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
        print(f"  ║  ☠  C Z H   P A S S W O R D   C R A C K E R  ☠                  ║")
        print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")
        
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} DICTIONARY ATTACK (Active)            {C}│{NC}")
        print(f"  {C}│{NC} {Y}[2]{W} RAINBOW TABLE LOOKUP (Instant)        {C}│{NC}")
        print(f"  {C}│{NC} {G}[3]{W} GENERATE RAINBOW TABLE                 {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")

        choice = input(f"{R}  CZH-CRACK ➜ {NC}").strip()
        
        if choice == "1":
            # Dictionary Attack (Old logic simplified)
            h = input(f"\n{Y}  [?] Enter Hash to Crack: {NC}").strip()
            if h:
                matrix_animation(2, "BRUTE-FORCING")
                found = False
                for w in WORDLIST:
                    if hashlib.md5(w.encode()).hexdigest() == h or hashlib.sha256(w.encode()).hexdigest() == h:
                        print(f"{G}  [✓] CRACKED! Password: {w}{NC}")
                        found = True
                        break
                if not found: print(f"{R}  [✗] Not found in dictionary.{NC}")
            input(f"\n{C}  Press Enter...{NC}")
            
        elif choice == "2":
            h = input(f"\n{Y}  [?] Enter Hash to Lookup in Rainbow Table: {NC}").strip()
            if h:
                lookup_rainbow(h)
            input(f"\n{C}  Press Enter...{NC}")
            
        elif choice == "3":
            generate_rainbow()
            
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH Cracker closed. Stay Ethical.{NC}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
