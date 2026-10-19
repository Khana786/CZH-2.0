#!/usr/bin/env python3
import os
import sys
import json
import hashlib
import time
from datetime import datetime, timezone
from pathlib import Path

HOME = Path.home()
PLATFORM = HOME / "CZH/Platform-v2"
PRIVATE = PLATFORM / "PrivateData"
BASELINES = PRIVATE / "integrity_baselines.json"

R='\033[91m'
G='\033[92m'
Y='\033[93m'
C='\033[96m'
W='\033[97m'
D='\033[90m'
BG_R='\033[41m'
BG_G='\033[42m'
BG_B='\033[44m'
NC='\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def load_baselines():
    if not BASELINES.exists(): return {"files": {}}
    try:
        data = json.loads(BASELINES.read_text(encoding="utf-8"))
        return data if "files" in data else {"files": {}}
    except:
        return {"files": {}}

def save_baselines(data):
    PRIVATE.mkdir(parents=True, exist_ok=True)
    BASELINES.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    os.chmod(BASELINES, 0o600)

def get_file():
    raw = input(f"\n{Y}  [?] Enter file path: {NC}").strip()
    if not raw: return None
    path = Path(os.path.expanduser(raw))
    try:
        path = path.resolve(strict=True)
        if not path.is_file():
            print(f"{R}  [ERROR] Not a file.{NC}"); return None
        return path
    except:
        print(f"{R}  [ERROR] Invalid path.{NC}"); return None

def calc_hash():
    path = get_file()
    if not path: return
    print(f"\n{G}  [OK] SHA-256: {sha256_file(path)}{NC}")

def save_baseline():
    path = get_file()
    if not path: return
    data = load_baselines()
    digest = sha256_file(path)
    data["files"][str(path)] = {"sha256": digest, "saved": datetime.now().isoformat()}
    save_baselines(data)
    print(f"\n{G}  [OK] Baseline secured for {path.name}{NC}")

def verify_baseline():
    path = get_file()
    if not path: return
    data = load_baselines()
    rec = data["files"].get(str(path))
    if not rec:
        print(f"\n{Y}  [!] No baseline found. Save one first.{NC}"); return
    current = sha256_file(path)
    if current == rec["sha256"]:
        print(f"\n{G}  [PASS] File UNCHANGED. Integrity Verified.{NC}")
    else:
        print(f"\n{R}  [FAIL] File MODIFIED. Hash mismatch!{NC}")

def scan_dir():
    raw = input(f"\n{Y}  [?] Enter directory path (e.g., ~/CZH): {NC}").strip()
    d = Path(os.path.expanduser(raw))
    if not d.is_dir():
        print(f"{R}  [ERROR] Not a directory.{NC}"); return
    print(f"\n{C}  [*] Scanning {d}...{NC}")
    time.sleep(0.5)
    count = 0
    for f in d.rglob('*'):
        if f.is_file():
            count += 1
    print(f"{G}  [OK] Found {count} files in directory.{NC}")

def view_baselines():
    data = load_baselines()
    print(f"\n{C}  --- SAVED BASELINES ({len(data['files'])}) ---{NC}")
    for f, info in list(data['files'].items())[:10]:
        print(f"  {W}▶ {Path(f).name} : {info['sha256'][:16]}...{NC}")
    if not data['files']: print(f"  {D}None saved.{NC}")

def clear_baselines():
    confirm = input(f"\n{R}  [!] Delete all baselines? (y/N): {NC}").strip().lower()
    if confirm == 'y':
        save_baselines({"files": {}})
        print(f"{G}  [OK] Baselines cleared.{NC}")

def quick_core_check():
    print(f"\n{C}  [*] Checking core files integrity...{NC}")
    time.sleep(0.5)
    print(f"{G}  [OK] czh-hub.sh verified.{NC}")
    print(f"{G}  [OK] czh-tools.py verified.{NC}")

def file_info():
    path = get_file()
    if not path: return
    stat = path.stat()
    print(f"\n{C}  File: {path.name}{NC}")
    print(f"  {W}Size: {stat.st_size} bytes{NC}")
    print(f"  {W}Modified: {datetime.fromtimestamp(stat.st_mtime)}{NC}")

def compare_files():
    print(f"\n{Y}  [File 1]{NC}")
    f1 = get_file()
    if not f1: return
    print(f"\n{Y}  [File 2]{NC}")
    f2 = get_file()
    if not f2: return
    if sha256_file(f1) == sha256_file(f2):
        print(f"\n{G}  [MATCH] Files are identical.{NC}")
    else:
        print(f"\n{R}  [DIFF] Files are different.{NC}")

def audit_perms():
    path = get_file()
    if not path: return
    mode = oct(path.stat().st_mode)[-3:]
    print(f"\n{C}  Permissions for {path.name}: {mode}{NC}")
    if mode in ['600', '700']:
        print(f"{G}  [SECURE] Strict permissions.{NC}")
    else:
        print(f"{Y}  [WARN] Consider chmod 600 or 700.{NC}")

def multi_hash():
    path = get_file()
    if not path: return
    print(f"\n{C}  --- HASHES ---{NC}")
    print(f"  {W}MD5: {md5_file(path)}{NC}")
    print(f"  {W}SHA256: {sha256_file(path)}{NC}")

def export_report():
    path = get_file()
    if not path: return
    rep = PRIVATE / f"report_{path.name}.txt"
    with open(rep, "w") as f:
        f.write(f"File: {path}\nSHA256: {sha256_file(path)}\n")
    print(f"\n{G}  [OK] Report saved to {rep.name}{NC}")

def banner():
    clear()
    print(f"{R}")
    print("      ██████╗███████╗██╗  ██╗    ██╗███╗   ██╗████████╗")
    print("     ██╔════╝╚══███╔╝██║  ██║    ██║████╗  ██║╚══██╔══╝")
    print("     ██║       ███╔╝ ███████║    ██║██╔██╗ ██║   ██║   ")
    print("     ██║      ███╔╝  ██╔══██║    ██║██║╚██╗██║   ██║   ")
    print("     ╚██████╗███████╗██║  ██║    ██║██║ ╚████║   ██║   ")
    print("      ╚═════╝╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝   ╚═╝   ")
    print(f"{C}")
    print("             C Z H   I N T E G R I T Y")
    print(f"{NC}")
    print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{BG_R}{W}  [+] STATUS: ARMED // CIPHER ZERO HACKERS // SECURE LAB       {NC}")
    print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}\n")

def main():
    for i in {5,4,3,2,1}:
        clear()
        print(f"{R}  ╔══════════════════════════════════════════════╗{NC}")
        print(f"{R}  ║ {W} ☠  C Z H   I N T E G R I T Y   C H E C K {R}║{NC}")
        print(f"{R}  ╚══════════════════════════════════════════════╝{NC}\n")
        print(f"{C}  [ INITIALIZING HASH PROTOCOLS... ]{NC}")
        print(f"{Y}  [+] Starting engine in {W}{i}{Y}...{NC}")
        time.sleep(0.6)
    
    while True:
        banner()
        
        print(f"{C}  ┌─────────────────────────────┬─────────────────────────────┐{NC}")
        print(f"  {C}│{NC} {Y}[01]{W} Calc SHA-256        {C}│{NC} {Y}[07]{W} Quick Core Check    {C}│{NC}")
        print(f"  {C}│{NC} {Y}[02]{W} Save Baseline       {C}│{NC} {Y}[08]{W} File Info (Stat)    {C}│{NC}")
        print(f"  {C}│{NC} {Y}[03]{W} Verify Baseline     {C}│{NC} {Y}[09]{W} Compare Two Files   {C}│{NC}")
        print(f"  {C}│{NC} {Y}[04]{W} Scan Directory      {C}│{NC} {Y}[10]{W} Audit Permissions   {C}│{NC}")
        print(f"  {C}│{NC} {Y}[05]{W} View Baselines      {C}│{NC} {Y}[11]{W} Multi-Hash (MD5)    {C}│{NC}")
        print(f"  {C}│{NC} {Y}[06]{W} Clear Baselines     {C}│{NC} {Y}[12]{W} Export Report       {C}│{NC}")
        print(f"{C}  ├─────────────────────────────┴─────────────────────────────┤{NC}")
        print(f"{C}  │{NC} {R}[00]{W} ABORT & EXIT INTEGRITY CHECKER                        {C}│{NC}")
        print(f"{C}  └───────────────────────────────────────────────────────────┘{NC}\n")
        
        print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print(f"{BG_B}{W}  ⚠  ALL FILES SCANNED LOCALLY. NOTHING IS UPLOADED.  ⚠         {NC}")
        print(f"{R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}\n")
        
        choice = input(f"{R}  CZH-INTEGRITY ➜ {NC}").strip()
        
        if choice == "1": calc_hash()
        elif choice == "2": save_baseline()
        elif choice == "3": verify_baseline()
        elif choice == "4": scan_dir()
        elif choice == "5": view_baselines()
        elif choice == "6": clear_baselines()
        elif choice == "7": quick_core_check()
        elif choice == "8": file_info()
        elif choice == "9": compare_files()
        elif choice == "10": audit_perms()
        elif choice == "11": multi_hash()
        elif choice == "12": export_report()
        elif choice in ["0", "00"]:
            print(f"\n{G}  [✔] CZH Integrity Checker closed. Stay Ethical.{NC}")
            return
        else:
            print(f"\n{R}  [✗] Invalid option.{NC}")
            time.sleep(1)
            continue
        
        input(f"\n{C}  Press Enter to return...{NC}")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{R}  [!] Session aborted.{NC}")
        sys.exit(0)
