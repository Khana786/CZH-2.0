#!/usr/bin/env python3
import os
import sys
import time
import json
import urllib.request
import urllib.parse

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def unshorten_url(url):
    try:
        # Add http if missing
        if not url.startswith('http'):
            url = 'http://' + url
            
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.geturl() # Returns the final redirected URL
    except Exception as e:
        return f"Error: {e}"

def check_safety(url):
    # Using a free URL safety API (URLhaus or similar heuristic based check)
    # Note: Without API keys, we use a basic domain check for known malicious TLDS or structures.
    # For this simulator, we will do a basic heuristic check.
    
    suspicious_keywords = ["login", "free-gift", "hack", "verify", "update-bank", "account-suspended"]
    suspicious_tlds = [".xyz", ".tk", ".ml", ".ga", ".cf", ".gq"]
    
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc
    
    for kw in suspicious_keywords:
        if kw in url.lower():
            return "SUSPICIOUS", f"URL contains suspicious keyword: '{kw}'"
            
    for tld in suspicious_tlds:
        if domain.endswith(tld):
            return "SUSPICIOUS", f"Domain uses a free/suspicious TLD: '{tld}'"
            
    if not parsed.scheme == "https":
        return "WARNING", "Website is not using HTTPS encryption."
        
    return "SAFE", "No obvious malicious patterns detected."

def scan_url():
    clear()
    print(f"{C}")
    print("      ██╗   ██╗██████╗ ██╗         ███████╗ ██████╗ █████╗ ███╗   ██╗")
    print("      ██║   ██║██╔══██╗██║         ██╔════╝██╔════╝██╔══██╗████╗  ██║")
    print("      ██║   ██║██████╔╝██║         ███████╗██║     ███████║██╔██╗ ██║")
    print("      ██║   ██║██╔══██╗██║         ╚════██║██║     ██╔══██║██║╚██╗██║")
    print("      ╚██████╔╝██║  ██║███████╗    ███████║╚██████╗██║  ██║██║ ╚████║")
    print("       ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝")
    print(f"{NC}")
    print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{BG_R}{W}  ☠  C Z H   U R L   S C A N N E R   &   U N M A S K E R  ☠        {NC}")
    print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}\n")

    target_url = input(f"{Y}  [?] Enter URL to scan (e.g., bit.ly/xyz): {NC}").strip()
    if not target_url: return

    print(f"\n{C}  [*] Analyzing URL structure...{NC}")
    time.sleep(0.8)
    
    print(f"{C}  [*] Unmasking redirects (Please wait)...{NC}")
    time.sleep(1)
    real_url = unshorten_url(target_url)
    
    if "Error:" in real_url:
         print(f"\n{R}  [✗] Could not resolve URL: {real_url}{NC}")
         input(f"\n{C}  Press Enter to return...{NC}")
         return

    print(f"{W}  ▶ Real Destination: {C}{real_url}{NC}")
    
    print(f"{C}  [*] Running safety heuristics...{NC}")
    time.sleep(1)
    status, reason = check_safety(real_url)
    
    print(f"\n{G}  ┌───[ S C A N   R E P O R T ]────────────────────────────────────┐{NC}")
    print(f"  {W}▶ Final URL : {C}{real_url}{NC}")
    
    if status == "SAFE":
        print(f"  {W}▶ Status    : {G}[ SAFE ]{NC}")
        print(f"  {W}▶ Reason    : {G}{reason}{NC}")
    elif status == "WARNING":
        print(f"  {W}▶ Status    : {Y}[ WARNING ]{NC}")
        print(f"  {W}▶ Reason    : {Y}{reason}{NC}")
    else:
        print(f"  {W}▶ Status    : {R}[ SUSPICIOUS ]{NC}")
        print(f"  {W}▶ Reason    : {R}{reason}{NC}")
        print(f"  {W}▶ Advice    : {R}DO NOT click this link!{NC}")
        
    print(f"{G}  └──────────────────────────────────────────────────────────────┘{NC}\n")
    input(f"{C}  Press Enter to return...{NC}")

def main():
    while True:
        clear()
        print(f"{C}")
        print("      ██╗   ██╗██████╗ ██╗         ███████╗ ██████╗ █████╗ ███╗   ██╗")
        print("      ██║   ██║██╔══██╗██║         ██╔════╝██╔════╝██╔══██╗████╗  ██║")
        print("      ██║   ██║██████╔╝██║         ███████╗██║     ███████║██╔██╗ ██║")
        print("      ██║   ██║██╔══██╗██║         ╚════██║██║     ██╔══██║██║╚██╗██║")
        print("      ╚██████╔╝██║  ██║███████╗    ███████║╚██████╗██║  ██║██║ ╚████║")
        print("       ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝")
        print(f"{NC}")
        print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print(f"  ☠  C Z H   U R L   S C A N N E R  ☠                              ")
        print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}\n")
        
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} SCAN & UNMASK URL                      {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")
        
        choice = input(f"{R}  CZH-URLSCAN ➜ {NC}").strip()
        
        if choice == "1":
            scan_url()
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH URL Scanner closed. Stay Safe.{NC}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
