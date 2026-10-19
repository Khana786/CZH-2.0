#!/usr/bin/env python3
import socket
import threading
import sys
import os
import time

R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'
PORT = 9999

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear()
    print(f"{C}")
    print("      ██████╗  █████╗ ██████╗ ██╗  ██╗    ███╗   ██╗███████╗████████╗")
    print("      ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ████╗  ██║██╔════╝╚══██╔══╝")
    print("      ██║  ██║███████║██████╔╝█████╔╝     ██╔██╗ ██║█████╗     ██║   ")
    print("      ██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║╚██╗██║██╔══╝     ██║   ")
    print("      ██████╔╝██║  ██║██║  ██║██║  ██╗    ██║ ╚████║███████╗   ██║   ")
    print("      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝   ")
    print(f"{NC}")
    print(f"{R}  ╔══════════════════════════════════════════════════════════════════╗{NC}")
    print(f"{BG_R}{W}  ║  ☠  C Z H   D A R K   N E T   //   S E C U R E   L I N K  ☠      ║{NC}")
    print(f"{R}  ╚══════════════════════════════════════════════════════════════════╝{NC}\n")

# --- SERVER LOGIC ---
def start_server():
    banner()
    print(f"{Y}  [*] Booting up CZH Dark Net Node on port {PORT}...{NC}")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', PORT))
    server.listen()
    
    print(f"{G}  [✓] NODE ONLINE. Waiting for agents to connect...{NC}")
    print(f"{D}  [!] Tell your team to run 'czh-darknet' and enter your Local IP.{NC}\n")
    
    clients = []
    aliases = {}

    def broadcast(msg, sender_sock):
        for client in clients:
            if client != sender_sock:
                try: client.send(msg.encode('utf-8'))
                except: client.close()

    # Server Input Loop (Host typing)
    def server_input():
        while True:
            try:
                msg = input(f"{Y}[HOST] {W}")
                if msg.lower() == 'exit':
                    os._exit(0)
                if msg:
                    print(f"\033[A\r{C}[HOST]{W} {msg}{NC}") # Move up and overwrite prompt
                    broadcast(f"[HOST] {msg}", None)
            except:
                break

    def handle_client(client_sock):
        try:
            alias = client_sock.recv(1024).decode('utf-8')
            aliases[client_sock] = alias
            print(f"\n{G}  [+] Agent '{alias}' connected to the Dark Net.{NC}")
            print(f"{Y}[HOST] {W}", end="", flush=True)
            
            broadcast(f"[SYSTEM] {alias} entered the chat.", client_sock)
            clients.append(client_sock)
            
            while True:
                msg = client_sock.recv(1024).decode('utf-8')
                if not msg: break
                print(f"\033[A\r{C}[{alias}]{W} {msg}{NC}")
                print(f"{Y}[HOST] {W}", end="", flush=True)
                broadcast(f"[{alias}] {msg}", client_sock)
        except:
            pass
        finally:
            if client_sock in clients: clients.remove(client_sock)
            if client_sock in aliases:
                print(f"\n{R}  [-] Agent '{aliases[client_sock]}' disconnected.{NC}")
                print(f"{Y}[HOST] {W}", end="", flush=True)
                broadcast(f"[SYSTEM] {aliases[client_sock]} left the chat.", client_sock)
                del aliases[client_sock]
            client_sock.close()

    threading.Thread(target=server_input, daemon=True).start()
    print(f"{Y}[HOST] {W}", end="", flush=True)

    try:
        while True:
            client_sock, addr = server.accept()
            threading.Thread(target=handle_client, args=(client_sock,), daemon=True).start()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Server shutting down...{NC}")
        server.close()

# --- CLIENT LOGIC ---
def start_client():
    banner()
    print(f"{Y}  [!] Note: You must be on the same WiFi as the Host.{NC}")
    ip = input(f"  [?] Enter Host IP Address (e.g., 192.168.1.5): {NC}").strip()
    alias = input(f"  [?] Enter your Agent Alias: {NC}").strip()
    
    if not ip or not alias: return

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"\n{C}  [*] Establishing secure connection to {ip}:{PORT}...{NC}")
    try:
        sock.connect((ip, PORT))
    except Exception as e:
        print(f"{R}  [✗] Connection Failed: {e}{NC}")
        input(f"\n{C}  Press Enter to return...{NC}")
        return
        
    sock.send(alias.encode('utf-8'))
    clear()
    print(f"{G}  [✓] CONNECTED. Welcome to the CZH Dark Net, {alias}.{NC}")
    print(f"{D}  [ Type 'exit' to disconnect ]{NC}\n")

    def receive():
        while True:
            try:
                msg = sock.recv(1024).decode('utf-8')
                if not msg: break
                print(f"\r  {C}{msg}{NC}")
                print(f"{Y}  {alias}: {W}", end="", flush=True)
            except:
                break
        print(f"\n{R}  [!] Connection to Dark Net lost.{NC}")

    threading.Thread(target=receive, daemon=True).start()
    
    while True:
        try:
            msg = input(f"{Y}  {alias}: {W}")
            if msg.lower() == 'exit': break
            if msg: sock.send(msg.encode('utf-8'))
        except KeyboardInterrupt:
            break
    sock.close()

def main():
    while True:
        banner()
        print(f"{C}  ┌────────────────────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[1]{W} HOST NODE (Create Chat)               {C}│{NC}")
        print(f"  {C}│{NC} {Y}[2]{W} CONNECT TO NODE (Join Chat)            {C}│{NC}")
        print(f"  {C}├────────────────────────────────────────────┤{NC}")
        print(f"  {C}│{NC} {R}[0]{W} ABORT & EXIT                           {C}│{NC}")
        print(f"{C}  └────────────────────────────────────────────┘{NC}\n")
        
        choice = input(f"{R}  CZH-DARKNET ➜ {NC}").strip()
        if choice == "1": start_server()
        elif choice == "2": start_client()
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✓] CZH Dark Net closed. Stay Hidden.{NC}")
            break
        else:
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}  [!] Session aborted.{NC}")
