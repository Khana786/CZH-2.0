import os
import sys
import socket
import ssl
import hashlib
import subprocess
import urllib.request
import time

# Colors
R='\033[91m'
G='\033[92m'
Y='\033[93m'
C='\033[96m'
W='\033[97m'
D='\033[90m'
BG_R='\033[41m'
BG_G='\033[42m'
NC='\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def dns_lookup():
    host = input(f"\n{Y}  [?] Enter domain for DNS lookup (e.g., example.com): {NC}").strip()
    if not host: return
    try:
        print(f"\n{C}  [+] Resolving: {host}{NC}")
        ip = socket.gethostbyname(host)
        print(f"{G}  [✔] IPv4 Address: {ip}{NC}")
    except Exception as e:
        print(f"{R}  [✗] Could not resolve: {e}{NC}")

def tls_info():
    host = input(f"\n{Y}  [?] Enter domain for TLS check (e.g., example.com): {NC}").strip()
    if not host: return
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                print(f"\n{C}  [+] TLS Info for: {host}{NC}")
                print(f"{G}  [✔] Protocol: {ssock.version()}{NC}")
                print(f"{G}  [✔] Issuer: {dict(x[0] for x in cert['issuer'])['commonName']}{NC}")
                print(f"{G}  [✔] Expires: {cert['notAfter']}{NC}")
    except Exception as e:
        print(f"{R}  [✗] Connection error: {e}{NC}")

def security_headers():
    url = input(f"\n{Y}  [?] Enter URL for headers (e.g., https://example.com): {NC}").strip()
    if not url: return
    if not url.startswith("http"): url = "https://" + url
    try:
        req = urllib.request.Request(url, method="HEAD", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(f"\n{C}  [+] Headers for: {url}{NC}")
            for h in ["Server", "X-Frame-Options", "Strict-Transport-Security", "Content-Security-Policy"]:
                val = resp.headers.get(h, "Missing")
                print(f"{G}  [✔] {h}: {val}{NC}")
    except Exception as e:
        print(f"{R}  [✗] {e}{NC}")

def file_hash():
    path = input(f"\n{Y}  [?] Enter file path for SHA-256 (e.g., ~/test.txt): {NC}").strip()
    path = os.path.expanduser(path)
    if not os.path.isfile(path):
        print(f"{R}  [✗] File not found.{NC}")
        return
    try:
        sha = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""): sha.update(chunk)
        print(f"\n{C}  [+] SHA-256 Hash for: {path}{NC}")
        print(f"{G}  [✔] {sha.hexdigest()}{NC}")
    except Exception as e:
        print(f"{R}  [✗] {e}{NC}")

def system_info():
    print(f"\n{C}  [+] System Environment Info{NC}")
    print(f"{G}  [✔] Platform: {sys.platform}{NC}")
    print(f"{G}  [✔] Python: {sys.version.split()[0]}{NC}")
    print(f"{G}  [✔] Home: {os.path.expanduser('~')}{NC}")

def network_health():
    print(f"\n{C}  [+] Network Health Inspector{NC}")
    try:
        ip = socket.gethostbyname(socket.gethostname())
        print(f"{G}  [✔] Local IP: {ip}{NC}")
    except:
        print(f"{Y}  [!] Local IP hidden{NC}")
    try:
        socket.gethostbyname("example.com")
        print(f"{G}  [✔] DNS Reachability: ONLINE{NC}")
    except:
        print(f"{R}  [✗] DNS Reachability: OFFLINE{NC}")

def whois_lookup():
    dom = input(f"\n{Y}  [?] Enter domain for WHOIS: {NC}").strip()
    if not dom: return
    print(f"\n{C}  [+] WHOIS Lookup: {dom}{NC}")
    try:
        res = subprocess.run(["whois", dom], capture_output=True, text=True, timeout=10)
        print(res.stdout[:1000] + "\n... (truncated)")
    except FileNotFoundError:
        print(f"{R}  [✗] 'whois' not installed. Run: pkg install whois{NC}")
    except Exception as e:
        print(f"{R}  [✗] {e}{NC}")

def ping_host():
    host = input(f"\n{Y}  [?] Enter host to ping: {NC}").strip()
    if not host: return
    print(f"\n{C}  [+] Pinging: {host}{NC}")
    try:
        res = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True, timeout=15)
        if res.returncode == 0:
            print(res.stdout)
        else:
            print(f"{R}  [✗] Host unreachable.{NC}")
    except Exception as e:
        print(f"{R}  [✗] {e}{NC}")

def main():
    while True:
        clear()
        
        # Perfect CZH Logo
        print(f"{R}")
        print("      ██████╗███████╗██╗  ██╗")
        print("     ██╔════╝╚══███╔╝██║  ██║")
        print("     ██║       ███╔╝ ███████║")
        print("     ██║      ███╔╝  ██╔══██║")
        print("     ╚██████╗███████╗██║  ██║")
        print("      ╚═════╝╚══════╝╚═╝  ╚═╝")
        print(f"{W}         T O O L S{NC}\n")
        
        # Danger Borders
        print(f"{R}  ╔════════════════════════════════════════════╗{NC}")
        print(f"{BG_R}{W}  ║  ☠  S T A T U S :   A R M E D  ☠          ║{NC}")
        print(f"{R}  ╚════════════════════════════════════════════╝{NC}\n")
        
        # Single Column Menu
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[01]{W} DNS Lookup                             {C}│{NC}")
        print(f"  {C}│{NC} {Y}[02]{W} Certificate Information                {C}│{NC}")
        print(f"  {C}│{NC} {Y}[03]{W} Security Headers                       {C}│{NC}")
        print(f"  {C}│{NC} {Y}[04]{W} File SHA-256 Hash                      {C}│{NC}")
        print(f"  {C}│{NC} {Y}[05]{W} System Environment                     {C}│{NC}")
        print(f"  {C}│{NC} {Y}[06]{W} Network Health                         {C}│{NC}")
        print(f"  {C}│{NC} {Y}[07]{W} WHOIS Lookup                           {C}│{NC}")
        print(f"  {C}│{NC} {Y}[08]{W} Ping Host                              {C}│{NC}")
        print(f"{C}  ├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[00]{W} ABORT SESSION & EXIT                   {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")
        
        # Warning Footer
        print(f"{R}  ╔════════════════════════════════════════════╗{NC}")
        print(f"{BG_G}{W}  ║  [+] MONITORING ACTIVE // CZH SECURE       ║{NC}")
        print(f"{R}  ╚════════════════════════════════════════════╝{NC}\n")

        choice = input(f"{R}  CZH-TOOLS ➜ {NC}").strip()
        
        if choice == "1": dns_lookup()
        elif choice == "2": tls_info()
        elif choice == "3": security_headers()
        elif choice == "4": file_hash()
        elif choice == "5": system_info()
        elif choice == "6": network_health()
        elif choice == "7": whois_lookup()
        elif choice == "8": ping_host()
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✔] CZH Toolkit closed. Stay Ethical.{NC}")
            break
        else:
            print(f"\n{R}  [✗] Invalid option.{NC}")
            time.sleep(1)
            continue
        
        input(f"\n{C}  Press Enter to return to menu...{NC}")

if __name__ == "__main__":
    main()
