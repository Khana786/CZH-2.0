#!/usr/bin/env python3
import os
import sys
import time
import random

# Colors
R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; NC='\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def trigger_panic():
    # 1. Kill background daemon (if running)
    os.system("pkill -f czh-daemon.sh 2>/dev/null")
    
    # 2. Clear terminal history
    os.system("history -c 2>/dev/null")
    os.system("rm -f ~/.bash_history 2>/dev/null")
    
    # 3. Show Fake System Update Screen
    clear()
    print(f"{W}")
    print("  ==================================================")
    print("            A N D R O I D   S Y S T E M            ")
    print("                 U P D A T E                       ")
    print("  ==================================================")
    print("")
    print("  Please do not turn off your device.")
    print("  Installing security patches...\n")
    
    for i in range(0, 101, 5):
        bar = "█" * (i // 5) + "░" * (20 - (i // 5))
        sys.stdout.write(f"\r  [{bar}] {i}%")
        sys.stdout.flush()
        time.sleep(0.15)
        
    print("\n\n  Update completed successfully.")
    print("  Restarting device in 3 seconds...")
    time.sleep(3)
    
    clear()
    # 4. Fake Innocent Prompt
    print(f"{W}Welcome to Termux!\n")
    while True:
        try:
            cmd = input(f"{G}~ $ {NC}")
            if cmd.lower() in ["exit", "quit"]:
                break
            print(f"bash: {cmd}: command not found")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    trigger_panic()
