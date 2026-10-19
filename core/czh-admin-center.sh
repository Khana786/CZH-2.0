#!/data/data/com.termux/files/usr/bin/bash

clear
R='\033[91m'
G='\033[92m'
Y='\033[93m'
B='\033[94m'
C='\033[96m'
W='\033[97m'
D='\033[90m'
BG_B='\033[44m'
BG_G='\033[42m'
BG_R='\033[41m'
NC='\033[0m'

# --- 5 SECOND HIFI ENTRY ANIMATION ---
for i in {1..5}; do
    clear
    echo -e "${B}"
    echo -e "      █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗"
    echo -e "     ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║"
    echo -e "     ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║"
    echo -e "     ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║"
    echo -e "     ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║"
    echo -e "     ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝"
    echo -e "${W}"
    echo -e "       [ VERIFYING AUTHORIZATION - CEO / FOUNDER ]"
    echo -e "${B}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BG_B}${W}  ⚠  S Y S T E M   B O O T I N G   I N   P R O G R E S S  ⚠  ${NC}"
    echo -e "${B}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "${Y}  [+] Checking Biometrics..."
    echo -e "${Y}  [+] Establishing Secure Connection..."
    echo -e "${Y}  [+] Bypassing Standard Security (Admin Override)...${NC}"
    echo ""
    echo -e "${R}  [!] ACCESS GRANTED IN ${W}$((6-i))${R}...${NC}"
    sleep 1
done
# -------------------------------------

# --- ADMIN LOCK VERIFICATION ---
clear
echo -e "${B}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BG_R}${W}  ☠  S Y S T E M   L O C K E D   -   A D M I N   O N L Y  ☠  ${NC}"
echo -e "${B}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${Y}  ⚠ UNAUTHORIZED ACCESS IS A CRIMINAL OFFENSE.${NC}"
echo ""
read -r -s -p "$(echo -e "${R}  ▶ ENTER ADMIN AUTHORIZATION KEY: ${NC}")" input_key
echo ""

if [ "$input_key" != "CZH-DARKWEB-QEP5ES" ]; then
    echo -e "\n${BG_R}${W}  [✗] ACCESS DENIED. SELF-DESTRUCT INITIATED...  ${NC}"
    sleep 2
    exit 1
fi
echo -e "${G}  [✓] ACCESS GRANTED. WELCOME BACK, FOUNDER.${NC}"
sleep 1
# ------------------------------

ADMIN_DIR="$HOME/CZH/PrivateData/Admin"
mkdir -p "$ADMIN_DIR"
LOG_MAIN="$HOME/CZH/PrivateData/reports/activity.log"
LOG_DARK="$HOME/CZH/PrivateData/darklab_activity.log"
LOG_MEMBER="$HOME/CZH/PrivateData/Members/member_activity.log"
ROADMAP_FILE="$ADMIN_DIR/roadmap.txt"
touch "$ROADMAP_FILE"

while true; do
    clear
    echo -e "${B}"
    echo -e "      █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗"
    echo -e "     ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║"
    echo -e "     ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║"
    echo -e "     ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║"
    echo -e "     ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║"
    echo -e "     ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝"
    echo -e "${G}"
    echo -e "       C Z H   A D M I N   C O M M A N D"
    echo -e "${NC}"

    echo -e "${B}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BG_B}${W}  👑 C Z H   F O U N D E R   C O N T R O L   P A N E L  👑  ${NC}"
    echo -e "${B}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    echo -e "${BG_G}${W}  [+] SYSTEM STATUS: ALL MODULES ONLINE // AARHIV HACKERS       ${NC}"
    echo ""
    
    echo -e "${C}  ┌─────────────────────────────┬─────────────────────────────┐${NC}"
    echo -e "${C}  │${NC} ${G}[1]${W} Main Activity Logs   ${C}│${NC} ${G}[6]${W} Manage Members        ${C}│${NC}"
    echo -e "${C}  │${NC} ${G}[2]${W} Dark Lab Logs        ${C}│${NC} ${G}[7]${W} Bug Reports           ${C}│${NC}"
    echo -e "${C}  │${NC} ${G}[3]${W} Member Reg. Logs     ${C}│${NC} ${G}[8]${W} System Diagnostics    ${C}│${NC}"
    echo -e "${C}  │${NC} ${G}[4]${W} Clear All Logs       ${C}│${NC} ${Y}[9]${W} CZH Roadmap & Updates${C}│${NC}"
    echo -e "${C}  │${NC} ${G}[5]${W} SYSTEM UPDATE        ${C}│${NC} ${Y}[B]${W} BOUNTY STATS        ${C}│${NC}"
    echo -e "${C}  ├─────────────────────────────┴─────────────────────────────┤${NC}"
    echo -e "${C}  │${NC} ${R}[L]${W} LOCK ADMIN PANEL (SECURITY)                            ${C}│${NC}"
    echo -e "${C}  └──────────────────────────────────────────────────────────┘${NC}"
    echo ""
    echo -e "${D}  [ LIVE SYSTEM MONITORING ACTIVE ]${NC}"
    echo ""
    read -r -p "$(echo -e "${B}  ADMIN ➜ ${NC}")" choice

    case "$choice" in
        1) clear; echo -e "${W}  === MAIN ACTIVITY LOGS ===${NC}"; cat "$LOG_MAIN" 2>/dev/null | tail -n 15; read -r -p "  Press Enter..." ;;
        2) clear; echo -e "${W}  === DARK LAB LOGS ===${NC}"; cat "$LOG_DARK" 2>/dev/null | tail -n 15; read -r -p "  Press Enter..." ;;
        3) clear; echo -e "${W}  === MEMBER LOGS ===${NC}"; cat "$LOG_MEMBER" 2>/dev/null | tail -n 15; read -r -p "  Press Enter..." ;;
        4) clear; echo -e "${R}  === CLEAR LOGS ===${NC}"; read -r -p "  Confirm clear all logs? (y/N): " c; if [[ "$c" == "y" ]]; then > "$LOG_MAIN"; > "$LOG_DARK"; > "$LOG_MEMBER"; echo -e "${G}  [✓] Cleared."; fi; read -r -p "  Press Enter..." ;;
        5) clear; echo -e "${Y}  === SYSTEM UPDATE ===${NC}"; echo -e "  Fetching latest from GitHub..."; cd "$HOME/CZH-2.0-PUBLIC-RELEASE" && git pull origin main; read -r -p "  Press Enter..." ;;
        6) clear; echo -e "${W}  === MEMBERS ===${NC}"; echo -e "  Total: $(wc -l < "$HOME/CZH/PrivateData/Members/members.db" 2>/dev/null || echo 0)"; cat "$HOME/CZH/PrivateData/Members/members.db" 2>/dev/null | awk -F: '{print "  - " $1 " (" $3 ")"}'; read -r -p "  Press Enter..." ;;
        7) clear; echo -e "${W}  === BUG REPORTS ===${NC}"; cat "$HOME/CZH/PrivateData/BugBounty/reports.txt" 2>/dev/null | tail -n 20; read -r -p "  Press Enter..." ;;
        8) clear; echo -e "${W}  === DIAGNOSTICS ===${NC}"; df -h "$HOME" | tail -n 1; echo -e "  Members: $(wc -l < "$HOME/CZH/PrivateData/Members/members.db" 2>/dev/null || echo 0)"; read -r -p "  Press Enter..." ;;
        9) clear; echo -e "${Y}  === CZH ROADMAP & NEW FEATURES ===${NC}"; cat "$ROADMAP_FILE"; echo ""; read -r -p "  Add new feature to roadmap (or 'exit'): " new_feat; if [[ "$new_feat" != "exit" && -n "$new_feat" ]]; then echo "[ ] $new_feat" >> "$ROADMAP_FILE"; echo -e "${G}  [✓] Added!"; fi; read -r -p "  Press Enter..." ;;
        B|b)
            clear
            echo -e "${B}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
            echo -e "${BG_B}${W}  👑  B U G   B O U N T Y   S T A T S  👑  ${NC}"
            echo -e "${B}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
            
            REPORTS_DB="$HOME/CZH/PrivateData/BugBounty/reports.db"
            if [ -f "$REPORTS_DB" ] && [ -s "$REPORTS_DB" ]; then
                TOTAL=$(wc -l < "$REPORTS_DB" | tr -d ' ')
                PENDING=$(awk -F'|' '$6=="PENDING"{c++} END{print c+0}' "$REPORTS_DB")
                ACCEPTED=$(awk -F'|' '$6=="ACCEPTED"{c++} END{print c+0}' "$REPORTS_DB")
                REJECTED=$(awk -F'|' '$6=="REJECTED"{c++} END{print c+0}' "$REPORTS_DB")
                
                echo -e "${W}  Total Reports : ${G}$TOTAL${NC}"
                echo -e "${W}  Pending       : ${Y}$PENDING${NC}"
                echo -e "${W}  Accepted      : ${G}$ACCEPTED${NC}"
                echo -e "${W}  Rejected      : ${R}$REJECTED${NC}\n"
                
                echo -e "${C}  [ Recent Accepted Reports ]${NC}"
                awk -F'|' '$6=="ACCEPTED" {printf "  - ID: %s | Alias: %s | Severity: %s\n", $1, $2, $5}' "$REPORTS_DB" | tail -n 5
            else
                echo -e "${Y}  No Bug Reports found yet.${NC}"
            fi
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        L|l) echo -e "${R}\n  [✗] ADMIN PANEL LOCKED. Exiting...${NC}"; sleep 1; exit 0 ;;
        0) echo -e "${B}\n  [!] DISCONNECTING. STAY ETHICAL.${NC}"; exit 0 ;;
        *) echo -e "${R}\n  [✗] INVALID OPTION.${NC}"; sleep 1 ;;
    esac
done
