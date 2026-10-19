#!/usr/bin/env python3
import os
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

RSS_FEEDS = [
    "https://feeds.feedburner.com/TheHackersNews",
    "https://www.bleepingcomputer.com/feed/"
]

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def fetch_news():
    clear()
    print(f"{C}  [*] Establishing Secure Connection to Threat Intel Servers...{NC}")
    time.sleep(1)
    
    articles = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for feed_url in RSS_FEEDS:
        try:
            req = urllib.request.Request(feed_url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                xml_data = response.read()
                root = ET.fromstring(xml_data)
                
                # Parse RSS items
                for item in root.findall('.//item'):
                    title = item.find('title').text if item.find('title') is not None else "No Title"
                    link = item.find('link').text if item.find('link') is not None else ""
                    pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ""
                    
                    articles.append({
                        "title": title,
                        "link": link,
                        "date": pub_date[:16] if pub_date else "Recent"
                    })
        except Exception as e:
            pass # Ignore failed feeds and try the next one
            
    return articles[:10] # Return top 10 latest articles

def display_feed():
    articles = fetch_news()
    clear()
    
    print(f"{R}")
    print("      ████████╗██╗  ██╗██████╗ ███████╗ █████╗ ████████╗")
    print("      ╚══██╔══╝██║  ██║██╔══██╗██╔════╝██╔══██╗╚══██╔══╝")
    print("         ██║   ███████║██████╔╝█████╗  ███████║   ██║   ")
    print("         ██║   ██╔══██║██╔══██╗██╔══╝  ██╔══██║   ██║   ")
    print("         ██║   ██║  ██║██║  ██║███████╗██║  ██║   ██║   ")
    print("         ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ")
    print(f"{NC}")
    print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
    print(f"{BG_R}{W}  ║  ☠  L I V E   C Y B E R   T H R E A T   I N T E L L I G E N C E  ║{NC}")
    print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")
    
    if not articles:
        print(f"{R}  [✗] Failed to fetch news. Check your internet connection.{NC}")
        return
    
    print(f"{Y}  [+] Latest Global Cyber Security News (Updated Live):{NC}\n")
    
    for i, art in enumerate(articles, 1):
        title = art['title']
        if len(title) > 60: title = title[:57] + "..."
        
        print(f"  {C}[{i:02d}]{NC} {W}{title}{NC}")
        print(f"       {D}▶ {art['date']}{NC}\n")
        
    print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
    print(f"  {C}│{NC} {Y}[1-10]{W} Open Article in Browser             {C}│{NC}")
    print(f"  {C}│{NC} {R}[0]{W} Refresh Feed                           {C}│{NC}")
    print(f"{C}  └────────────────────────────────────────────┘{NC}\n")
    
    choice = input(f"{R}  CZH-THREAT ➜ {NC}").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(articles):
        idx = int(choice) - 1
        link = articles[idx]['link']
        print(f"\n{G}  [*] Opening: {link}{NC}")
        os.system(f"termux-open-url '{link}' 2>/dev/null")
        time.sleep(2)
        display_feed() # Loop back
    elif choice == "0":
        display_feed()
    else:
        return

def main():
    while True:
        clear()
        print(f"{C}")
        print("      ████████╗██╗  ██╗██████╗ ███████╗ █████╗ ████████╗")
        print("      ╚══██╔══╝██║  ██║██╔══██╗██╔════╝██╔══██╗╚══██╔══╝")
        print("         ██║   ███████║██████╔╝█████╗  ███████║   ██║   ")
        print("         ██║   ██╔══██║██╔══██╗██╔══╝  ██╔══██║   ██║   ")
        print("         ██║   ██║  ██║██║  ██║███████╗██║  ██║   ██║   ")
        print("         ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ")
        print(f"{NC}")
        print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
        print(f"  ║  ☠  C Z H   T H R E A T   F E E D   //   G L O B A L  ☠          ║")
        print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")
        
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} FETCH LATEST CYBER NEWS                {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")
        
        choice = input(f"{R}  CZH-THREAT ➜ {NC}").strip()
        
        if choice == "1":
            display_feed()
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH Threat Feed closed. Stay Updated.{NC}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
