#!/usr/bin/env python3
import os
import sys
import json
import time
import socket
import urllib.request

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def radar_animation():
    frames = [
        "     [ .      ]     ",
        "     [  .     ]     ",
        "     [   .    ]     ",
        "     [    .   ]     ",
        "     [     .  ]     ",
        "     [      . ]     ",
        "     [       .]     ",
    ]
    for _ in range(2):
        for frame in frames:
            sys.stdout.write(f"\r{Y}  [*] SCANNING TARGET {frame}{NC}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * 50 + "\r")

def track_target():
    clear()
    print(f"{C}")
    print("      ██████╗  █████╗ ██████╗  █████╗ ██████╗ ")
    print("      ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗")
    print("      ██████╔╝███████║██║  ██║███████║██████╔╝")
    print("      ██╔══██╗██╔══██║██║  ██║██╔══██║██╔══██╗")
    print("      ██║  ██║██║  ██║██████╔╝██║  ██║██║  ██║")
    print("      ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝")
    print(f"{NC}")
    print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
    print(f"{BG_R}{W}  ║  ☠  G E O - L O C A T I O N   &   O S I N T   R A D A R  ☠        ║{NC}")
    print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")

    target = input(f"{Y}  [?] Enter IP Address or Domain (e.g., 8.8.8.8 or google.com): {NC}").strip()
    if not target:
        return

    ip = target
    if not target.replace('.', '').isdigit():
        print(f"\n{C}  [*] Resolving Domain to IP...{NC}")
        try:
            ip = socket.gethostbyname(target)
            print(f"{G}  [✓] Resolved: {target} -> {ip}{NC}")
        except Exception as e:
            print(f"{R}  [✗] Could not resolve domain: {e}{NC}")
            input(f"\n{C}  Press Enter to return...{NC}")
            return

    print("")
    radar_animation()
    
    print(f"{C}  [*] Querying Global Intelligence Database...{NC}")
    try:
        url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())

        if data.get("status") == "success":
            lat = data.get('lat', 0)
            lon = data.get('lon', 0)
            maps_link = f"https://www.google.com/maps?q={lat},{lon}"
            
            print(f"\n{G}  ┌───[ T A R G E T   A C Q U I R E D ]──────────────────────────┐{NC}")
            print(f"  {W}▶ IP Address  : {C}{data.get('query')}{NC}")
            print(f"  {W}▶ Country     : {G}{data.get('country')} ({data.get('countryCode')}){NC}")
            print(f"  {W}▶ Region      : {W}{data.get('regionName')}{NC}")
            print(f"  {W}▶ City        : {W}{data.get('city')} {data.get('zip')}{NC}")
            print(f"  {W}▶ Timezone    : {Y}{data.get('timezone')}{NC}")
            print(f"  {W}▶ ISP         : {C}{data.get('isp')}{NC}")
            print(f"  {W}▶ Org         : {D}{data.get('org')}{NC}")
            print(f"  {W}▶ Coordinates : {Y}{lat}, {lon}{NC}")
            print(f"{G}  ├──────────────────────────────────────────────────────────────┤{NC}")
            print(f"  {W}▶ Live Map    : {C}{maps_link}{NC}")
            print(f"{G}  └──────────────────────────────────────────────────────────────┘{NC}")
            
            os.system(f"termux-open-url '{maps_link}' 2>/dev/null")
            print(f"\n{Y}  [*] Opening location in Browser...{NC}")
            
        else:
            print(f"\n{R}  [✗] Target not found or API error: {data.get('message', 'Unknown')}{NC}")
            
    except Exception as e:
        print(f"\n{R}  [✗] Error: {e}{NC}")

    print("")
    input(f"{C}  Press Enter to return...{NC}")

def main():
    while True:
        clear()
        print(f"{C}")
        print("      ██████╗  █████╗ ██████╗  █████╗ ██████╗ ")
        print("      ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗")
        print("      ██████╔╝███████║██║  ██║███████║██████╔╝")
        print("      ██╔══██╗██╔══██║██║  ██║██╔══██║██╔══██╗")
        print("      ██║  ██║██║  ██║██████╔╝██║  ██║██║  ██║")
        print("      ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝")
        print(f"{NC}")
        print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
        print(f"  ║  ☠  C Z H   R A D A R   //   G E O - L O C A T I O N  ☠          ║")
        print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")
        
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} TRACK IP / DOMAIN (Radar)             {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")
        
        choice = input(f"{R}  CZH-RADAR ➜ {NC}").strip()
        
        if choice == "1":
            track_target()
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH Radar closed. Stay Anonymous.{NC}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
