#!/usr/bin/env python3
import os
import sys
import time
import random

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

def typewriter(text, delay=0.02, color=W):
    for char in text:
        sys.stdout.write(f"{color}{char}{NC}")
        sys.stdout.flush()
        time.sleep(delay)
    print("")

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def run_hijack():
    clear()
    for _ in range(5):
        print(f"{G}" + "".join(random.choice("01") for _ in range(50)) + f"{NC}")
        time.sleep(0.1)
    
    clear()
    print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
    print(f"{BG_R}{W}  ║  ☠  E X T E R N A L   B R E A C H   D E T E C T E D  ☠          ║{NC}")
    print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")

    time.sleep(0.5)
    typewriter("  [+] Bypassing Android Security Protocols...", 0.03, Y)
    time.sleep(0.5)
    typewriter("  [+] Accessing Front Camera... [RECORDING]", 0.03, Y)
    time.sleep(0.5)
    typewriter("  [+] Extracting WhatsApp Chats and Gallery...", 0.03, Y)
    time.sleep(0.5)
    typewriter("  [+] Connecting to Dark Web Server: 192.168.1.666", 0.03, Y)
    time.sleep(0.5)
    
    print(f"\n{R}  [!!!] DOWNLOADING YOUR DATA [!!!]{NC}")
    for i in range(0, 101, 10):
        bar = "█" * (i // 10) + "░" * (10 - (i // 10))
        sys.stdout.write(f"\r  {R}[{bar}] {i}%{NC}")
        sys.stdout.flush()
        time.sleep(0.2)
    
    time.sleep(1)
    clear()
    
    print(f"{R}")
    print("      ██████╗  █████╗ ███╗   ██╗ ██████╗ ███████╗██████╗ ")
    print("      ██╔══██╗██╔══██╗████╗  ██║██╔════╝ ██╔════╝██╔══██╗")
    print("      ██║  ██║███████║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝")
    print("      ██║  ██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗")
    print("      ██████╔╝██║  ██║██║ ╚████║╚██████╔╝███████╗██║  ██║")
    print("      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝")
    print(f"{NC}")
    
    print(f"\n{W}  Wait wait wait... 😂{NC}")
    time.sleep(1)
    print(f"{Y}  Bhai, dar mat. Yeh sirf ek prank tha! CZH Cyber Team ki taraf se. 🫡{NC}")
    print(f"{C}  Tumhari koi file delete nahi hui, camera access nahi hua. Sab safe hai.{NC}\n")
    
    input(f"{G}  Press Enter to exit the prank...{NC}")

if __name__ == "__main__":
    try:
        run_hijack()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Prank cancelled.{NC}")
