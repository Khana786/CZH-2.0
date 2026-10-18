import os
import sys
import socket
import ssl
import hashlib
import subprocess
import urllib.request

RED = "\033[91m"
GRN = "\033[92m"
YEL = "\033[93m"
BLU = "\033[94m"
MAG = "\033[95m"
CYN = "\033[96m"
WHT = "\033[97m"
RST = "\033[0m"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def dns_lookup():
    host = input("\nEnter domain for DNS lookup (e.g., example.com): ").strip()
    if not host: return
    try:
        print(f"\n{CYN}[+] Resolving: {host}{RST}")
        ip = socket.gethostbyname(host)
        print(f"{GRN}[OK]{RST} IPv4 Address: {ip}")
    except Exception as e:
        print(f"{RED}[FAIL]{RST} Could not resolve: {e}")

def tls_info():
    host = input("\nEnter domain for TLS check (e.g., example.com): ").strip()
    if not host: return
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                print(f"\n{CYN}[+] TLS Info for: {host}{RST}")
                print(f"{GRN}[OK]{RST} Protocol: {ssock.version()}")
                print(f"{GRN}[OK]{RST} Issuer: {dict(x[0] for x in cert['issuer'])['commonName']}")
                print(f"{GRN}[OK]{RST} Expires: {cert['notAfter']}")
    except Exception as e:
        print(f"{RED}[FAIL]{RST} Connection error: {e}")

def security_headers():
    url = input("\nEnter URL for headers (e.g., https://example.com): ").strip()
    if not url: return
    if not url.startswith("http"): url = "https://" + url
    try:
        req = urllib.request.Request(url, method="HEAD", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(f"\n{CYN}[+] Headers for: {url}{RST}")
            for h in ["Server", "X-Frame-Options", "Strict-Transport-Security", "Content-Security-Policy"]:
                val = resp.headers.get(h, "Missing")
                print(f"{GRN}[OK]{RST} {h}: {val}")
    except Exception as e:
        print(f"{RED}[FAIL]{RST} {e}")

def file_hash():
    path = input("\nEnter file path for SHA-256 (e.g., ~/test.txt): ").strip()
    path = os.path.expanduser(path)
    if not os.path.isfile(path):
        print(f"{RED}[FAIL]{RST} File not found.")
        return
    try:
        sha = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""): sha.update(chunk)
        print(f"\n{CYN}[+] SHA-256 Hash for: {path}{RST}")
        print(f"{GRN}[OK]{RST} {sha.hexdigest()}")
    except Exception as e:
        print(f"{RED}[FAIL]{RST} {e}")

def system_info():
    print(f"\n{CYN}[+] System Environment Info{RST}")
    print(f"{GRN}[OK]{RST} Platform: {sys.platform}")
    print(f"{GRN}[OK]{RST} Python: {sys.version.split()[0]}")
    print(f"{GRN}[OK]{RST} Home: {os.path.expanduser('~')}")

def network_health():
    print(f"\n{CYN}[+] Network Health Inspector{RST}")
    try:
        ip = socket.gethostbyname(socket.gethostname())
        print(f"{GRN}[OK]{RST} Local IP: {ip}")
    except:
        print(f"{YEL}[!]{RST} Local IP hidden")
    try:
        socket.gethostbyname("example.com")
        print(f"{GRN}[OK]{RST} DNS Reachability: ONLINE")
    except:
        print(f"{RED}[FAIL]{RST} DNS Reachability: OFFLINE")

def whois_lookup():
    dom = input("\nEnter domain for WHOIS: ").strip()
    if not dom: return
    print(f"\n{CYN}[+] WHOIS Lookup: {dom}{RST}")
    try:
        res = subprocess.run(["whois", dom], capture_output=True, text=True, timeout=10)
        print(res.stdout[:1000] + "\n... (truncated)")
    except FileNotFoundError:
        print(f"{RED}[FAIL]{RST} 'whois' not installed. Run: pkg install whois")
    except Exception as e:
        print(f"{RED}[FAIL]{RST} {e}")

def ping_host():
    host = input("\nEnter host to ping: ").strip()
    if not host: return
    print(f"\n{CYN}[+] Pinging: {host}{RST}")
    try:
        res = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True, timeout=15)
        if res.returncode == 0:
            print(res.stdout)
        else:
            print(f"{RED}[FAIL]{RST} Host unreachable.")
    except Exception as e:
        print(f"{RED}[FAIL]{RST} {e}")

def main():
    while True:
        clear()
        print(f"""{RED}╔═══════════════════════════════════════════╗
║{GRN}  ██████╗███████╗██╗  ██╗{RED}                  ║
║{GRN} ██╔════╝╚══███╔╝██║  ██║{RED}                  ║
║{GRN} ██║       ███╔╝  ███████║{RED}                  ║
║{GRN} ██║      ███╔╝   ██╔══██║{RED}                  ║
║{GRN} ╚██████╗███████╗ ██║  ██║{RED}                  ║
║{GRN}  ╚═════╝╚══════╝ ╚═╝  ╚═╝{RED}                  ║
║{CYN}             C Z H   T O O L S               {RED}║
╠═══════════════════════════════════════════╣
║{WHT} [+] STATUS: ARMED // CZH SECURE           {RED}║
╠═══════════════════════════════════════════╣
║{YEL} [01]{WHT} DNS LOOKUP      {RED}║{YEL} [05]{WHT} SYS ENVIRONMENT {RED}║
║{YEL} [02]{WHT} CERT INTEL      {RED}║{YEL} [06]{WHT} NET HEALTH      {RED}║
║{YEL} [03]{WHT} SEC HEADERS     {RED}║{YEL} [07]{WHT} WHOIS LOOKUP    {RED}║
║{YEL} [04]{WHT} SHA-256 HASH    {RED}║{YEL} [08]{WHT} PING HOST       {RED}║
╠═══════════════════════════════════════════╣
║{RED} [00] ABORT SESSION & EXIT                  {RED}║
╚═══════════════════════════════════════════╝{RST}""")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == "1": dns_lookup()
        elif choice == "2": tls_info()
        elif choice == "3": security_headers()
        elif choice == "4": file_hash()
        elif choice == "5": system_info()
        elif choice == "6": network_health()
        elif choice == "7": whois_lookup()
        elif choice == "8": ping_host()
        elif choice == "0" or choice == "00":
            print(f"\n{GRN}CZH Toolkit closed.{RST}")
            break
        else:
            print(f"\n{YEL}Invalid option.{RST}")
        
        input(f"\n{CYN}Press Enter to return to menu...{RST}")

if __name__ == "__main__":
    main()
