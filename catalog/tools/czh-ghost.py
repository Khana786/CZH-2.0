#!/usr/bin/env python3
import os
import sys
import time
import random
import string

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

FIRST_NAMES = ["Alex", "Sam", "John", "David", "Michael", "Chris", "Max", "Leo", "Victor", "Zero"]
LAST_NAMES = ["Smith", "Hacker", "Doe", "Shadow", "Cipher", "Ghost", "Root", "Void", "Rogue", "Byte"]
DOMAINS = ["protonmail.com", "tutanota.com", "gmail.com", "yahoo.com", "outlook.com"]
CITIES = ["Mumbai", "Delhi", "New York", "London", "Tokyo", "Berlin", "Moscow", "Dubai", "Sydney"]
STREETS = ["Main St", "Cyber Ave", "Dark Web Blvd", "Node Rd", "Cipher Lane", "Binary St"]

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def generate_password(length=14):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def generate_identity():
    fname = random.choice(FIRST_NAMES)
    lname = random.choice(LAST_NAMES)
    username = f"{fname.lower()}_{lname.lower()}{random.randint(10,99)}"
    email = f"{username}@{random.choice(DOMAINS)}"
    
    # Fake Indian/US format phone
    phone = f"+91 {random.randint(70000,99999)}{random.randint(10000,99999)}"
    
    # Fake Address
    addr = f"{random.randint(1, 999)} {random.choice(STREETS)}, {random.choice(CITIES)}"
    
    # Fake IP (Private range just for realism)
    ip = f"192.168.{random.randint(1,255)}.{random.randint(1,255)}"
    
    pwd = generate_password()
    
    return {
        "Name": f"{fname} {lname}",
        "Username": username,
        "Email": email,
        "Phone": phone,
        "Address": addr,
        "Local IP": ip,
        "Password": pwd
    }

def display_identity():
    clear()
    print(f"{C}")
    print("      ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗")
    print("     ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝")
    print("     ██║  ███╗███████║██║   ██║███████╗   ██║   ")
    print("     ██║   ██║██╔══██║██║   ██║╚════██║   ██║   ")
    print("     ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ")
    print("      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ")
    print(f"{NC}")
    print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
    print(f"{BG_R}{W}  ║  ☠  C Z H   G H O S T   //   F A K E   I D E N T I T Y  ☠        ║{NC}")
    print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")

    print(f"{Y}  [*] Synthesizing Fake Identity...{NC}")
    time.sleep(0.5)
    
    ident = generate_identity()
    
    print(f"{G}  ┌───[ I D E N T I T Y   G E N E R A T E D ]──────────────────────┐{NC}")
    print(f"  {W}▶ Full Name   : {C}{ident['Name']}{NC}")
    print(f"  {W}▶ Username    : {C}{ident['Username']}{NC}")
    print(f"  {W}▶ Email       : {C}{ident['Email']}{NC}")
    print(f"  {W}▶ Phone       : {C}{ident['Phone']}{NC}")
    print(f"  {W}▶ Address     : {C}{ident['Address']}{NC}")
    print(f"  {W}▶ Local IP    : {C}{ident['Local IP']}{NC}")
    print(f"  {W}▶ Password    : {G}{ident['Password']}{NC}")
    print(f"{G}  └──────────────────────────────────────────────────────────────┘{NC}\n")
    
    print(f"{D}  [ WARNING: This is a simulated identity for testing/privacy only. ]{NC}")
    print(f"{D}  [ Do NOT use for illegal activities. ]{NC}\n")
    input(f"{C}  Press Enter to generate a new one...{NC}")

def main():
    while True:
        clear()
        print(f"{C}")
        print("      ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗")
        print("     ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝")
        print("     ██║  ███╗███████║██║   ██║███████╗   ██║   ")
        print("     ██║   ██║██╔══██║██║   ██║╚════██║   ██║   ")
        print("     ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ")
        print("      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ")
        print(f"{NC}")
        print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
        print(f"  ║  ☠  C Z H   G H O S T   //   U N D E R C O V E R  ☠              ║")
        print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")
        
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} GENERATE FAKE IDENTITY                 {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")
        
        choice = input(f"{R}  CZH-GHOST ➜ {NC}").strip()
        
        if choice == "1":
            display_identity()
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH Ghost Identity closed. Stay Hidden.{NC}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
