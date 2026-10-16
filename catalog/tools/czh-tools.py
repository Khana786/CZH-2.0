#!/usr/bin/env python3
import hashlib
import os
import platform
import socket
import ssl
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

def get_host():
    raw = input("Domain ya hostname: ").strip()
    if "://" in raw:
        raw = urllib.parse.urlsplit(raw).hostname or ""
    raw = raw.split("/")[0].split(":")[0].strip()
    if not raw or any(c.isspace() for c in raw):
        print("Invalid hostname.")
        return None
    return raw

def dns_lookup():
    host = get_host()
    if not host:
        return
    try:
        results = sorted({item[4][0] for item in socket.getaddrinfo(host, None)})
        print("\nDNS results:")
        for ip in results:
            print(" ", ip)
    except (socket.gaierror, OSError) as exc:
        print("DNS error:", exc)

def tls_info():
    host = get_host()
    if not host:
        return
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=8) as sock:
            with context.wrap_socket(sock, server_hostname=host) as tls:
                cert = tls.getpeercert()
                print("TLS version:", tls.version())
                print("Cipher:", tls.cipher()[0] if tls.cipher() else "Unknown")
                print("Certificate subject:", cert.get("subject", "Unknown"))
                print("Certificate issuer:", cert.get("issuer", "Unknown"))
                expiry = cert.get("notAfter")
                print("Certificate expires:", expiry or "Unknown")
                if expiry:
                    exp = datetime.strptime(
                        expiry, "%b %d %H:%M:%S %Y %Z"
                    ).replace(tzinfo=timezone.utc)
                    days = (exp - datetime.now(timezone.utc)).days
                    print("Days until expiry:", days)
    except (OSError, ssl.SSLError, ValueError) as exc:
        print("TLS check failed:", exc)

def security_headers():
    raw = input("Full HTTPS URL (only check sites you are allowed to test): ").strip()
    parsed = urllib.parse.urlsplit(raw)
    if parsed.scheme != "https" or not parsed.hostname:
        print("Please provide a valid HTTPS URL.")
        return
    request = urllib.request.Request(
        raw, method="GET", headers={"User-Agent": "CZH-Ethical-Lab/1.0"}
    )
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            print("HTTP status:", response.status)
            print("Final URL:", response.geturl())
            headers = response.headers
            wanted = [
                "Strict-Transport-Security",
                "Content-Security-Policy",
                "X-Content-Type-Options",
                "X-Frame-Options",
                "Referrer-Policy",
                "Permissions-Policy",
            ]
            print("\nSecurity header review:")
            for name in wanted:
                print(f"{name}: {headers.get(name, 'NOT PRESENT')}")
            print("\nNote: missing headers alone do not prove a vulnerability.")
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
        print("HTTP check failed:", exc)

def file_hash():
    raw = input("File path: ").strip()
    path = Path(os.path.expanduser(raw))
    if not path.is_file():
        print("File not found.")
        return
    digest = hashlib.sha256()
    try:
        with path.open("rb") as file:
            for chunk in iter(lambda: file.read(1024 * 1024), b""):
                digest.update(chunk)
        print("File:", path)
        print("SHA-256:", digest.hexdigest())
    except OSError as exc:
        print("File read error:", exc)

def system_info():
    print("Platform:", platform.platform())
    print("Python:", platform.python_version())
    print("Machine:", platform.machine())
    print("Termux PREFIX:", os.environ.get("PREFIX", "Not detected"))
    print("Home directory:", Path.home())
    print("This option does not collect or upload device information.")

def main():
    while True:
        print("""
========================================
      CZH ETHICAL CYBER TOOLKIT
       LEARN • SECURE • DEFEND
========================================
1. DNS lookup
2. HTTPS certificate information
3. HTTPS security headers
4. File SHA-256 hash
5. Local environment information
0. Exit
""")
        choice = input("Select option: ").strip()
        if choice == "1":
            dns_lookup()
        elif choice == "2":
            tls_info()
        elif choice == "3":
            security_headers()
        elif choice == "4":
            file_hash()
        elif choice == "5":
            system_info()
        elif choice == "0":
            print("CZH Toolkit closed.")
            break
        else:
            print("Invalid option.")
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
