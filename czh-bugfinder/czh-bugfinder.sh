#!/data/data/com.termux/files/usr/bin/bash

clear
R='\033[91m'
G='\033[92m'
Y='\033[93m'
C='\033[96m'
W='\033[97m'
D='\033[90m'
BG_R='\033[41m'
BG_B='\033[44m'
NC='\033[0m'

BOUNTY_DIR="$HOME/CZH/PrivateData/BugBounty"
mkdir -p "$BOUNTY_DIR"
touch "$BOUNTY_DIR/reports.txt"
chmod 600 "$BOUNTY_DIR/reports.txt"

log_action() {
    printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$1" >> "$BOUNTY_DIR/bounty_activity.log"
}

IS_ADMIN="false"
while true; do
    clear
    echo -e "${R}"
    echo -e "     ██████╗███████╗██╗  ██╗    ██████╗ ██╗   ██╗ ██████╗ "
    echo -e "    ██╔════╝╚══███╔╝██║  ██║    ██╔══██╗██║   ██║██╔════╝ "
    echo -e "    ██║       ███╔╝ ███████║    ██████╔╝██║   ██║██║  ███╗"
    echo -e "    ██║      ███╔╝  ██╔══██║    ██╔══██╗██║   ██║██║   ██║"
    echo -e "    ╚██████╗███████╗██║  ██║    ██████╔╝╚██████╔╝╚██████╔╝"
    echo -e "     ╚═════╝╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝  ╚═════╝ "
    echo -e "${C}"
    echo -e "           ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ "
    echo -e "           ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗"
    echo -e "           █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝"
    echo -e "           ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗"
    echo -e "           ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║"
    echo -e "           ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝"
    echo -e "${NC}"

    echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BG_R}${W}  ☠  C Z H   B U G F I N D E R   -   H U N T E R   L A B  ☠  ${NC}"
    echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    echo -e "${BG_B}${W}  [!] SYSTEM STATUS: ACTIVE // AUTHORIZED HUNTING ONLY          ${NC}"
    echo -e "${Y}"
    echo -e "  ⚠ TARGET SCOPE: Authorized systems & localhost only."
    echo -e "  ⚠ UNAUTHORIZED HUNTING IS ILLEGAL AND PROHIBITED."
    echo -e "  ⚠ ALL REPORTS ARE MONITORED AND LOGGED.${NC}"
    echo ""
    
    echo -e "${C}  ┌──────────────────────────────────────────────────────────┐${NC}"
    echo -e "${C}  │${NC} ${Y}[1]${W} VIEW AUTHORIZED TARGETS & RULES                     ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[2]${W} SUBMIT A NEW BUG REPORT (FOUND A FLAW?)            ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[3]${W} VIEW MY SUBMITTED REPORTS                           ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[4]${W} READ BUG BOUNTY RESOURCES                           ${C}│${NC}"
    if [ "$IS_ADMIN" == "true" ]; then
        echo -e "${C}  │${NC} ${MAG}[5]${W} ADMIN REVIEW PANEL (Owner Only)                     ${C}│${NC}"
    fi
    echo -e "${C}  ├──────────────────────────────────────────────────────────┤${NC}"
    echo -e "${C}  │${NC} ${R}[0]${W} ABORT & EXIT BUG FINDER                             ${C}│${NC}"
    echo -e "${C}  └──────────────────────────────────────────────────────────┘${NC}"
    echo ""
    echo -e "${D}  [ SESSION MONITORED BY AARHIV HACKERS ]${NC}"
    echo ""
    read -r -p "$(echo -e "${R}  BUG HUNTER ➜ ${NC}")" choice

    case "$choice" in
        1)
            clear
            echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
            echo -e "${BG_R}${W}  ☠  A U T H O R I Z E D   T A R G E T S   &   R U L E S  ☠  ${NC}"
            echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
            echo ""
            echo -e "${W}  You are ONLY allowed to test on the following:${NC}"
            echo -e "${G}  ✔ Your own domains / servers / VPS${NC}"
            echo -e "${G}  ✔ Localhost (127.0.0.1)${NC}"
            echo -e "${G}  ✔ Deliberately vulnerable practice sites (HackTheBox, TryHackMe, PortSwigger)${NC}"
            echo ""
            echo -e "${R}  ✗ NEVER test on public websites or companies without written permission.${NC}"
            echo -e "${R}  ✗ NEVER use these reports for malicious intent.${NC}"
            echo ""
            log_action "Viewed Authorized Targets"
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        2)
            clear
            echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
            echo -e "${BG_R}${W}  ☠  S U B M I T   A   N E W   B U G   R E P O R T  ☠  ${NC}"
            echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
            echo ""
            read -r -p "$(echo -e "${Y}  Target URL/IP: ${NC}")" target
            read -r -p "$(echo -e "${Y}  Vulnerability Type (XSS, SQLi, etc.): ${NC}")" v_type
            read -r -p "$(echo -e "${Y}  Severity (Low/Medium/High/Critical): ${NC}")" severity
            echo -e "${Y}  Description (Type END on a new line to finish):${NC}"
            desc=""
            while read -r line; do
                [[ "$line" == "END" ]] && break
                desc="$desc$line\n"
            done
            
            DATE=$(date '+%Y-%m-%d %H:%M:%S')
            echo -e "[$DATE] Target: $target | Type: $v_type | Severity: $severity\nDescription: $desc\n---" >> "$BOUNTY_DIR/reports.txt"
            log_action "Submitted a bug report for $target ($severity)"
            echo -e "\n${G}  [✓] REPORT SUBMITTED SUCCESSFULLY. Admin will review it.${NC}"
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        3)
            clear
            echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
            echo -e "${BG_R}${W}  ☠  Y O U R   S U B M I T T E D   R E P O R T S  ☠  ${NC}"
            echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
            echo ""
            if [ -s "$BOUNTY_DIR/reports.txt" ]; then
                cat "$BOUNTY_DIR/reports.txt"
            else
                echo -e "${Y}  No reports submitted yet.${NC}"
            fi
            log_action "Viewed own bug reports"
            echo ""
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        4)
            clear
            echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
            echo -e "${BG_R}${W}  ☠  B U G   B O U N T Y   R E S O U R C E S  ☠  ${NC}"
            echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
            echo ""
            echo -e "${W}  1. OWASP Top 10:${NC}"
            echo -e "     https://owasp.org/www-project-top-ten/"
            echo -e "${W}  2. HackerOne 101:${NC}"
            echo -e "     https://www.hackerone.com/"
            echo -e "${W}  3. PortSwigger Web Security Academy:${NC}"
            echo -e "     https://portswigger.net/web-security"
            echo -e "${W}  4. Bugcrowd University:${NC}"
            echo -e "     https://www.bugcrowd.com/hackers/bugcrowd-university/"
            echo ""
            echo -e "${R}  ⚠ Always read the program's scope before testing.${NC}"
            log_action "Viewed Bug Bounty Resources"
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        5)
            if [ "$IS_ADMIN" == "true" ]; then
                clear
                echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
                echo -e "${MAG}${W}  ☠  A D M I N   R E V I E W   P A N E L  ☠  ${NC}"
                echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
                echo ""
                if [ -s "$BOUNTY_DIR/reports.txt" ]; then
                    cat "$BOUNTY_DIR/reports.txt"
                else
                    echo -e "${Y}  No reports to review.${NC}"
                fi
                echo ""
                read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            else
                echo -e "${R}\n  [✗] ACCESS DENIED. ADMIN ONLY.${NC}"
                read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            fi
            ;;
        secret_admin_login)
            read -r -s -p "$(echo -e "${R}  Enter Admin Key: ${NC}")" admin_key
            echo ""
            if [ "$admin_key" == "CZH-DARKWEB-QEP5ES" ]; then
                IS_ADMIN="true"
                echo -e "${G}  [✓] Admin Access Granted.${NC}"
            else
                echo -e "${R}  [✗] Invalid Key.${NC}"
            fi
            sleep 1
            ;;
        0)
            echo -e "${R}\n  [!] DISCONNECTING FROM BUG HUNTER MODE. STAY ETHICAL.${NC}"
            log_action "Exited Bug Finder"
            exit 0
            ;;
        *)
            echo -e "${R}\n  [✗] INVALID OPTION.${NC}"
            sleep 1
            ;;
    esac
done
