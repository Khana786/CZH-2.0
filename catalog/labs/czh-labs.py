#!/usr/bin/env python3
"""CZH practical defensive cybersecurity learning labs."""

import hashlib
import os
import socket
import ssl
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


def hostname_input():
    value = input("Authorized hostname (without https://): ").strip()
    if (
        not value
        or "/" in value
        or "://" in value
        or any(c.isspace() for c in value)
    ):
        print("Enter a valid hostname, not a URL or path.")
        return None
    return value


def dns_lab():
    host = hostname_input()
    if not host:
        return
    try:
        results = sorted({
            item[4][0]
            for item in socket.getaddrinfo(host, None)
        })
        print(f"\nDNS results for {host}:")
        for address in results:
            print(f"  {address}")
    except (socket.gaierror, OSError) as exc:
        print(f"DNS lookup failed: {exc}")


def https_lab():
    host = hostname_input()
    if not host:
        return
    try:
        context = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=5) as raw:
            with context.wrap_socket(raw, server_hostname=host) as conn:
                cert = conn.getpeercert()
                print("\nHTTPS certificate information")
                print("TLS version:", conn.version())
                print("Certificate subject:", cert.get("subject", "Unavailable"))
                print("Certificate issuer:", cert.get("issuer", "Unavailable"))
                print("Valid from:", cert.get("notBefore", "Unavailable"))
                print("Valid until:", cert.get("notAfter", "Unavailable"))
    except (OSError, ssl.SSLError, ValueError) as exc:
        print(f"HTTPS check failed: {exc}")


def headers_lab():
    host = hostname_input()
    if not host:
        return

    url = "https://" + host
    request = Request(url, method="HEAD", headers={"User-Agent": "CZH-Defensive-Lab/1.0"})

    try:
        response = urlopen(request, timeout=8)
    except HTTPError as exc:
        response = exc
    except (URLError, OSError, ValueError) as exc:
        print(f"HTTPS request failed: {exc}")
        return

    with response:
        print("HTTP status:", response.status)
        headers = response.headers
        for name in (
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Referrer-Policy",
            "Permissions-Policy",
        ):
            print(f"{name}: {headers.get(name, 'Not present in this response')}")

    print("Note: a missing header alone does not prove a vulnerability.")


def hash_lab():
    raw_path = input("Path to a file you own or may inspect: ").strip()
    path = Path(os.path.expanduser(raw_path))

    try:
        if not path.is_file():
            print("That path is not a regular file.")
            return

        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(65536), b""):
                digest.update(chunk)

        print("SHA-256:", digest.hexdigest())
        print("Compare it with a trusted checksum if one is available.")
    except OSError as exc:
        print(f"Could not read file: {exc}")


def main():
    labs = {
        "1": ("DNS Basics", dns_lab),
        "2": ("HTTPS Certificate", https_lab),
        "3": ("HTTPS Security Headers", headers_lab),
        "4": ("File SHA-256", hash_lab),
    }

    while True:
        print("\n======================================")
        print("       CZH PRACTICAL CYBER LABS")
        print("======================================")
        for key, (label, _) in labs.items():
            print(f"{key}. {label}")
        print("0. Exit")

        try:
            choice = input("Select lab: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nLabs closed.")
            return

        if choice == "0":
            print("CZH Labs closed.")
            return

        selected = labs.get(choice)
        if selected:
            print(f"\n--- {selected[0]} ---")
            try:
                selected[1]()
            except (EOFError, KeyboardInterrupt):
                print("\nReturning to lab menu.")
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
