#!/usr/bin/env python3
import os
import sys
import time
import random

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; BG_G='\033[42m'; NC='\033[0m'

COUNTRIES = [
    "RUSSIA (Moscow)", "USA (New York)", "CHINA (Beijing)", 
    "BRAZIL (Sao Paulo)", "INDIA (Mumbai)", "GERMANY (Berlin)", 
    "UK (London)", "JAPAN (Tokyo)", "NORTH KOREA (Pyongyang)"
]
ATTACK_TYPES = ["DDoS Attack", "SQL Injection", "Brute Force", "Malware", "Phishing", "Zero-Day Exploit"]
STATUS = ["BLOCKED", "DROPPED", "MONITORED", "QUARANTINED"]

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def draw_map():
    print(f"{D}  ======================================================================")
    print(f"  {C}          ▄▄▄▄▄▄▄▄▄▄▄▄▄  {D}        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  {D}      ▄▄▄▄▄▄▄")
    print(f"  {C}       ▄██████████████████▄{D}     ▄███████████████████████▄{D}   ▄█████████▄")
    print(f"  {C}      ██████████████████████{D}   ██████████████████████████{D} ███████████████")
    print(f"  {C}      ██████████████████████{D}  ████████████████████████████{D}████████████████")
    print(f"  {C}      ▀██████████████████▀{D}    ▀█████████████████████████▀{D} ▀██████████████")
    print(f"  {D}  ======================================================================{NC}")

def run_map():
    clear()
    print(f"{C}")
    print("      ██████╗██╗   ██╗██████╗ ███████╗██████╗ ")
    print("     ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗")
    print("     ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝")
    print("     ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗")
    print("     ╚██████╗   ██║   ██████╔╝███████╗██║  ██║")
    print("      ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝")
    print(f"{NC}")
    print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{BG_R}{W}  ☠  G L O B A L   T H R E A T   M A P   -   L I V E  ☠          {NC}")
    print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}\n")

    draw_map()
    print(f"\n{G}  [+] FIREWALL: ACTIVE // IPS: BLOCKING ATTACKS // LOGS: LIVE{NC}\n")

    try:
        for _ in range(15): # Show 15 random attacks
            country = random.choice(COUNTRIES)
            attack = random.choice(ATTACK_TYPES)
            status = random.choice(STATUS)
            
            src_ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
            dst_ip = f"192.168.1.{random.randint(2,254)}"
            
            # Colorize based on status
            if status == "BLOCKED":
                color = R
            elif status == "QUARANTINED":
                color = Y
            else:
                color = C
                
            time.sleep(random.uniform(0.2, 0.6))
            print(f"  {W}[{time.strftime('%H:%M:%S')}] {C}Incoming from {country}{NC}")
            print(f"           {D}└─ IP: {src_ip} -> {dst_ip}{NC}")
            print(f"           {D}└─ Type: {W}{attack}{NC}")
            print(f"           {D}└─ Action: {color}{status}{NC}\n")

        print(f"{G}  ┌──────────────────────────────────────────────────────────────┐{NC}")
        print(f"  {W}▶ Status: {G}ALL ATTACKS DEFLECTED. SYSTEM SECURE.{NC}")
        print(f"{G}  └──────────────────────────────────────────────────────────────┘{NC}\n")

    except KeyboardInterrupt:
        pass
    input(f"{C}  Press Enter to stop monitoring...{NC}")

def main():
    while True:
        clear()
        print(f"{C}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print(f"{G}       ☠  C Z H  //  C Y B E R  A T T A C K  M A P  ☠{NC}")
        print(f"{C}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}\n")
        
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} START LIVE THREAT MONITOR              {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")

        choice = input(f"{R}  CZH-MAP ➜ {NC}").strip()
        if choice == "1":
            run_map()
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH Cyber Map closed.{NC}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
