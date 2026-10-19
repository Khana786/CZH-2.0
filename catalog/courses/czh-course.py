import os
import json
import time
from pathlib import Path

HOME = Path.home()
PLATFORM = HOME / "CZH/Platform-v2"
PRIVATE = PLATFORM / "PrivateData"
PROGRESS_FILE = PRIVATE / "course-progress.json"

R='\033[91m'
G='\033[92m'
Y='\033[93m'
C='\033[96m'
W='\033[97m'
D='\033[90m'
BG_R='\033[41m'
NC='\033[0m'

LESSONS = [
    ("TERMUX & LINUX", "Learn what the shell does. Practice: pwd, ls, whoami."),
    ("FILES & PERMISSIONS", "Understand paths, ls -l, chmod and safe file handling."),
    ("NETWORKING CORE", "Learn IP addresses, DNS resolution, ports and network basics."),
    ("HTTPS & TLS", "Understand encryption, certificates and server authentication."),
    ("SHA-256 INTEGRITY", "Calculate a file hash and compare it with a trusted checksum."),
    ("PASSWORD DEFENSE", "Use unique passwords, password managers and multifactor authentication."),
    ("ANTI-PHISHING", "Recognize suspicious links, fake senders and credential theft attempts."),
    ("DEVICE SECURITY", "Update Android, review app permissions and install trusted software."),
    ("SECURITY HEADERS", "Learn HSTS, CSP, X-Frame-Options and browser security policies."),
    ("BACKUPS & LOGS", "Protect encrypted backups and avoid exposing passwords or access tokens."),
]

QUIZ = {
    1: {"q": "Which command prints the current working directory?", "choices": ["pwd", "cd", "ls"], "answer": "pwd", "why": "pwd prints the working directory."},
    2: {"q": "Which mode gives only the owner read+write?", "choices": ["777", "644", "600"], "answer": "600", "why": "600 = owner read+write."},
    3: {"q": "Which protocol resolves domain names to IP addresses?", "choices": ["DNS", "HTTP", "FTP"], "answer": "DNS", "why": "DNS maps hostnames to IPs."},
    4: {"q": "TLS primarily provides:", "choices": ["Encryption + auth", "Compression", "Routing"], "answer": "Encryption + auth", "why": "TLS encrypts and authenticates."},
    5: {"q": "A SHA-256 hash is best described as:", "choices": ["Reversible encryption", "Fixed-size fingerprint", "A password"], "answer": "Fixed-size fingerprint", "why": "Hashes are one-way fingerprints."},
    6: {"q": "Best for account security?", "choices": ["Reuse password", "Unique + MFA", "Write on paper"], "answer": "Unique + MFA", "why": "Unique passwords + MFA are best."},
    7: {"q": "First step for suspicious email?", "choices": ["Click link", "Reply", "Verify via separate channel"], "answer": "Verify via separate channel", "why": "Never trust the suspicious channel."},
    8: {"q": "Device habit to reduce risk?", "choices": ["Keep apps updated", "Any source install", "All permissions"], "answer": "Keep apps updated", "why": "Updates patch vulnerabilities."},
    9: {"q": "Which header forces HTTPS?", "choices": ["HSTS", "CSP", "X-Frame-Options"], "answer": "HSTS", "why": "HSTS requires HTTPS."},
    10: {"q": "A trustworthy backup must be:", "choices": ["Tested by restoring", "Never checked", "Unencrypted"], "answer": "Tested by restoring", "why": "Untested backups are unreliable."},
}

LESSON_CONTENT = {
    1: {"overview": ["The shell is a text interface to your OS.", "Termux provides a Linux-like environment."], "concepts": ["pwd - print working directory", "ls - list directory contents", "cd - change directory"], "practice": ["Run: pwd", "Run: ls", "Run: whoami"], "safety": "Read-only commands are safe."},
    2: {"overview": ["Every file has a path.", "Permissions decide access."], "concepts": ["ls -l - show permissions", "chmod 600 - owner rw only"], "practice": ["Run: ls -l", "Run: touch a.txt && ls -l a.txt"], "safety": "Avoid chmod 777."},
    3: {"overview": ["Networks exchange packets.", "IPs and Ports define connections."], "concepts": ["IPv4: 192.168.1.1", "DNS: Name to IP", "Ports: 80 HTTP, 443 HTTPS"], "practice": ["Run: czh-tools (DNS lookup)"], "safety": "Do not scan unauthorized networks."},
    4: {"overview": ["HTTPS uses TLS.", "Certificates prove identity."], "concepts": ["TLS - Encryption", "CA - Certificate Authority"], "practice": ["Run: czh-tools (Cert info)"], "safety": "Never bypass cert warnings."},
    5: {"overview": ["Hashes are fingerprints.", "SHA-256 is 256-bit."], "concepts": ["One-way function", "Integrity check"], "practice": ["Run: czh-tools (SHA-256)"], "safety": "A hash does not encrypt."},
    6: {"overview": ["Passwords are main defense.", "MFA adds a second layer."], "concepts": ["Unique passwords", "Password managers", "MFA"], "practice": ["Enable MFA on an account."], "safety": "Never share OTPs."},
    7: {"overview": ["Phishing steals credentials.", "Attackers mimic brands."], "concepts": ["Check sender domain", "Hover over links", "Verify separate channel"], "practice": ["Analyze a safe phishing email."], "safety": "Never enter creds on unknown pages."},
    8: {"overview": ["Devices need updates.", "Permissions restrict apps."], "concepts": ["Keep Android updated", "Review app permissions"], "practice": ["Review app permissions."], "safety": "Install from trusted stores."},
    9: {"overview": ["Headers protect browsers.", "They add defense."], "concepts": ["HSTS - Force HTTPS", "CSP - Restrict sources"], "practice": ["Run: czh-tools (Headers)"], "safety": "Missing headers != vulnerability."},
    10: {"overview": ["Backups protect data.", "Logs help investigate."], "concepts": ["Encrypt backups", "Test restores", "Clean logs"], "practice": ["Restore a test backup."], "safety": "Keep tokens out of logs."},
}

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def load_progress():
    if not PROGRESS_FILE.exists(): return set()
    try:
        data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        return set(str(x) for x in data.get("completed", []))
    except:
        return set()

def save_progress(completed):
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    PROGRESS_FILE.write_text(json.dumps({"completed": list(completed)}), encoding="utf-8")

def banner():
    clear()
    print(f"{R}  ╔══════════════════════════════════════════════╗")
    print(f"  ║ {R}██████╗███████╗██╗  ██╗ {R}                   ║")
    print(f"  ║ {R}██╔════╝╚══███╔╝██║  ██║ {R}                   ║")
    print(f"  ║ {R}██║       ███╔╝ ███████║ {R}                   ║")
    print(f"  ║ {R}██║      ███╔╝  ██╔══██║ {R}                   ║")
    print(f"  ║ {R}╚██████╗███████╗██║  ██║ {R}                   ║")
    print(f"  ║ {R} ╚═════╝╚══════╝╚═╝  ╚═╝ {R}                   ║")
    print(f"  ║ {C}      B L A C K S I T E {R}                   ║")
    print(f"  ╠══════════════════════════════════════════════╣")
    print(f"  ║ {BG_R}{W} ⚠ DANGER ZONE :: RESTRICTED ACCESS ⚠ {R}     ║{NC}")
    print(f"  ╚══════════════════════════════════════════════╝{NC}\n")

def open_lesson(num, completed):
    title, desc = LESSONS[num-1]
    clear()
    print(f"{R}  ╔══════════════════════════════════════════════╗")
    print(f"  ║ {BG_R}{W} MODULE {num:02d} :: {title:<28} {R}║{NC}")
    print(f"  ╚══════════════════════════════════════════════╝\n")
    
    print(f"{Y}  [+] MISSION BRIEF{NC}")
    print(f"  {W}{desc}{NC}\n")
    
    c = LESSON_CONTENT.get(num, {})
    if c:
        print(f"{C}  [+] OVERVIEW{NC}")
        for o in c["overview"]: print(f"  {W}- {o}{NC}")
        print(f"\n{C}  [+] KEY CONCEPTS{NC}")
        for k in c["concepts"]: print(f"  {W}- {k}{NC}")
        print(f"\n{C}  [+] PRACTICE{NC}")
        for p in c["practice"]: print(f"  {W}  {p}{NC}")
        print(f"\n{Y}  [!] SAFETY NOTE{NC}")
        print(f"  {D}{c['safety']}{NC}\n")
        
    if str(num) in completed:
        print(f"{G}  [✓] MODULE ALREADY COMPLETED.{NC}")
        input(f"\n{C}  Press Enter to return...{NC}")
        return

    q = QUIZ.get(num)
    if q:
        print(f"{C}  [+] QUICK CHECK{NC}")
        print(f"  {W}{q['q']}{NC}")
        for i, ch in enumerate(q["choices"], 1): print(f"    {i}) {ch}")
        try:
            ans = input(f"\n{Y}  Your answer [1-{len(q['choices'])}]: {NC}").strip()
            if 0 < int(ans) <= len(q["choices"]) and q["choices"][int(ans)-1] == q["answer"]:
                print(f"  {G}✔ Correct.{NC}")
            else:
                print(f"  {R}✗ Incorrect. Answer: {q['answer']}{NC}")
            print(f"  {D}{q['why']}{NC}\n")
        except:
            print(f"  {D}Quiz skipped.{NC}\n")
            
    ans = input(f"{Y}  Mark module complete? [y/N]: {NC}").strip().lower()
    if ans == 'y':
        completed.add(str(num))
        save_progress(completed)
        print(f"\n  {G}✔ PROGRESS SAVED LOCALLY.{NC}")
    input(f"\n{C}  Press Enter to return...{NC}")

def main():
    while True:
        banner()
        completed = load_progress()
        count = len(completed)
        percent = int((count / 10) * 100)
        bar = "█" * int(percent / 10) + "░" * (10 - int(percent / 10))
        
        print(f"{R}  ╔══════════════════════════════════════════════╗")
        print(f"  ║ {W}[+] PROGRESS: {G}[{bar}] {count}/10 {R}       ║{NC}")
        print(f"  ╠══════════════════════════════════════════════╣")
        
        for i in range(10):
            t, _ = LESSONS[i]
            status = f"{G}✔ DONE {NC}" if str(i+1) in completed else f"{Y}◈ READY{NC}"
            # Padding to align borders perfectly
            print(f"  {R}║{NC} {Y}[{i+1:02d}]{W} {t:<23} {status} {R}║{NC}")
            
        print(f"{R}  ╠══════════════════════════════════════════════╣")
        print(f"  ║ {R}[C]{W} RESET PROGRESS  {R}│{NC} {R}[0]{W} EXIT BLACKSITE {R}║{NC}")
        print(f"  ╚══════════════════════════════════════════════╝\n")
        
        # Danger warning footer to fill the screen
        print(f"{R}  ╔══════════════════════════════════════════════╗")
        print(f"  ║ {BG_R}{W} ⚠ WARNING: AUTHORIZED PERSONNEL ONLY ⚠ {R}    ║{NC}")
        print(f"  ║ {Y} ⚠ ALL ACTIVITIES ARE MONITORED AND LOGGED ⚠ {R}║{NC}")
        print(f"  ║ {C}   [ SESSION ENCRYPTED // STAY ETHICAL ]   {R}║{NC}")
        print(f"  ╚══════════════════════════════════════════════╝\n")
        
        choice = input(f"{R}  BLACKSITE ➜ {NC}").strip()
        
        if choice == "0":
            print(f"\n{R}  [!] DISCONNECTING FROM BLACKSITE. STAY ETHICAL.{NC}")
            break
        elif choice.lower() == "c":
            confirm = input(f"  {Y}Reset all progress? (y/N): {NC}").strip().lower()
            if confirm == 'y':
                if PROGRESS_FILE.exists(): PROGRESS_FILE.unlink()
                print(f"  {G}[✓] Progress reset.{NC}")
                time.sleep(1)
        elif choice.isdigit() and 1 <= int(choice) <= 10:
            open_lesson(int(choice), completed)
        else:
            print(f"  {R}[✗] Invalid option.{NC}")
            time.sleep(1)

if __name__ == "__main__":
    main()
