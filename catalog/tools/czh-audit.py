#!/usr/bin/env python3
import os
import sys
import time
import shutil
from pathlib import Path

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; BG_G='\033[42m'; NC='\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def check_root():
    try:
        return os.geteuid() == 0
    except:
        return False

def check_private_data_perms():
    priv_dir = Path.home() / "CZH/PrivateData"
    if not priv_dir.exists():
        return False, "Not Found"
    perms = oct(priv_dir.stat().st_mode)[-3:]
    if perms in ['700', '750']:
        return True, perms
    return False, perms

def run_audit():
    score = 100
    issues = []
    passed = []

    if check_root():
        score -= 20
        issues.append("Device is running as ROOT. Risk of system-wide compromise.")
    else:
        passed.append("Running as non-root user.")

    perm_ok, perms = check_private_data_perms()
    if perm_ok:
        passed.append(f"PrivateData permissions are secure ({perms}).")
    else:
        score -= 25
        issues.append(f"PrivateData permissions are weak ({perms}). Should be 700.")

    essential_tools = ["openssl", "nmap", "python"]
    missing_tools = []
    for tool in essential_tools:
        if not shutil.which(tool):
            missing_tools.append(tool)
            score -= 10
            issues.append(f"Missing security tool: {tool}")
    
    if not missing_tools:
        passed.append("All essential security tools are installed.")

    if not shutil.which("termux-notification"):
        score -= 5
        issues.append("termux-api missing. Notifications won't work.")
    else:
        passed.append("Termux API is installed for notifications.")

    if score < 0: score = 0

    bar_length = 20
    filled = int((score / 100) * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    
    color = G
    if score < 50: color = R
    elif score < 80: color = Y

    clear()
    print(f"{C}")
    print("      █████╗ ██╗   ██╗██████╗ ██╗████████╗")
    print("     ██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝")
    print("     ███████║██║   ██║██║  ██║██║   ██║   ")
    print("     ██╔══██║██║   ██║██║  ██║██║   ██║   ")
    print("     ██║  ██║╚██████╔╝██████╔╝██║   ██║   ")
    print("     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝   ")
    print(f"{NC}")
    
    print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
    print(f"{BG_R}{W}  ║  ☠  C Z H   S Y S T E M   H A R D E N I N G   A U D I T  ☠       ║{NC}")
    print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")

    print(f"{W}  [+] SCANNING ENVIRONMENT...{NC}")
    time.sleep(1.5)
    
    print(f"\n{color}  ┌───[ S E C U R I T Y   S C O R E ]──────────────────────────────┐{NC}")
    print(f"  {W}▶ Score: {color}{score}/100{NC}")
    print(f"  {W}▶ Rating: {color}[{bar}]{NC}")
    print(f"{color}  └──────────────────────────────────────────────────────────────┘{NC}\n")

    if issues:
        print(f"{R}  ┌───[ ⚠ V U L N E R A B I L I T I E S   F O U N D ]──────────────┐{NC}")
        for i in issues:
            print(f"  {R}[X]{NC} {W}{i}{NC}")
        print(f"{R}  └──────────────────────────────────────────────────────────────┘{NC}\n")
    
    if passed:
        print(f"{G}  ┌───[ ✓ P A S S E D   C H E C K S ]─────────────────────────────┐{NC}")
        for p in passed:
            print(f"  {G}[✔]{NC} {W}{p}{NC}")
        print(f"{G}  └──────────────────────────────────────────────────────────────┘{NC}\n")

    print(f"{Y}  [*] Audit Complete.{NC}")
    input(f"{C}  Press Enter to return...{NC}")

def main():
    while True:
        clear()
        print(f"{C}")
        print("      █████╗ ██╗   ██╗██████╗ ██╗████████╗")
        print("     ██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝")
        print("     ███████║██║   ██║██║  ██║██║   ██║   ")
        print("     ██╔══██║██║   ██║██║  ██║██║   ██║   ")
        print("     ██║  ██║╚██████╔╝██████╔╝██║   ██║   ")
        print("     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝   ")
        print(f"{NC}")
        print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
        print(f"  ║  ☠  C Z H   S Y S T E M   H A R D E N I N G  ☠                   ║")
        print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")
        
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} RUN SECURITY AUDIT                     {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")
        
        choice = input(f"{R}  CZH-AUDIT ➜ {NC}").strip()
        
        if choice == "1":
            run_audit()
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH Audit closed. Stay Secure.{NC}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
