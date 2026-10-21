#!/usr/bin/env python3
import os
import sys
import time
import random
import string

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

FIRST_NAMES = ["Alex", "Sam", "John", "David", "Michael", "Chris", "Max", "Leo", "Victor", "Zero"]
LAST_NAMES = ["Smith", "Doe", "Shadow", "Cipher", "Ghost", "Root", "Void", "Rogue", "Byte"]
DOMAINS = ["example.com", "test.com", "fakeemail.net", "mailinator.com"]

def generate_email():
    fname = random.choice(FIRST_NAMES).lower()
    lname = random.choice(LAST_NAMES).lower()
    num = random.randint(10, 99)
    domain = random.choice(DOMAINS)
    return f"{fname}.{lname}{num}@{domain}"

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def generate_credit_card():
    # Generates a fake but mathematically valid-looking CC number (Luhn Algorithm bypassed for simulation)
    prefixes = ["4", "5"] # Visa, Mastercard
    prefix = random.choice(prefixes)
    digits = [random.randint(0, 9) for _ in range(14)]
    cc = prefix + "".join(map(str, digits))
    return f"{cc[:4]} {cc[4:8]} {cc[8:12]} {cc[12:]}"

def generate_fake_data():
    clear()
    print(f"{C}")
    print("      ███████╗ █████╗ ██╗  ██╗███████╗")
    print("      ██╔════╝██╔══██╗██║ ██╔╝██╔════╝")
    print("      █████╗  ███████║█████╔╝ █████╗  ")
    print("      ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ")
    print("      ██║     ██║  ██║██║  ██╗███████╗")
    print("      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
    print(f"{NC}")
    print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{BG_R}{W}  ☠  C Z H   F A K E   D A T A   G E N E R A T O R  ☠              {NC}")
    print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}\n")

    print(f"{Y}  [*] Generating Fake Identity Data...{NC}")
    time.sleep(0.5)

    print(f"{G}  ┌───[ G E N E R A T E D   D A T A ]──────────────────────────────┐{NC}")
    print(f"  {W}▶ Fake Email     : {C}{generate_email()}{NC}")
    print(f"  {W}▶ Fake Password  : {Y}{generate_password()}{NC}")
    print(f"  {W}▶ Fake CC Number : {G}{generate_credit_card()}{NC}")
    print(f"{G}  ├──────────────────────────────────────────────────────────────┤{NC}")
    print(f"  {D}[!] WARNING: These are mathematically generated fake data for{NC}")
    print(f"  {D}    software testing purposes only. Do not use for fraud.{NC}")
    print(f"{G}  └──────────────────────────────────────────────────────────────┘{NC}\n")
    
    input(f"{C}  Press Enter to generate new data...{NC}")

def main():
    while True:
        clear()
        print(f"{C}")
        print("      ███████╗ █████╗ ██╗  ██╗███████╗")
        print("      ██╔════╝██╔══██╗██║ ██╔╝██╔════╝")
        print("      █████╗  ███████║█████╔╝ █████╗  ")
        print("      ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ")
        print("      ██║     ██║  ██║██║  ██╗███████╗")
        print("      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
        print(f"{NC}")
        print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print(f"  ☠  C Z H   F A K E   D A T A   G E N E R A T O R  ☠              ")
        print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}\n")
        
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} GENERATE FAKE DATA                    {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")
        
        choice = input(f"{R}  CZH-FAKEDATA ➜ {NC}").strip()
        
        if choice == "1":
            generate_fake_data()
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH Fake Data Generator closed.{NC}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
