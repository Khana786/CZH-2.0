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
BG_G='\033[42m'
NC='\033[0m'

BOUNTY_DIR="$HOME/CZH/PrivateData/BugBounty"
MEMBER_DB="$HOME/CZH/PrivateData/Members/members.db"
REPORTS_DB="$BOUNTY_DIR/reports.db"
mkdir -p "$BOUNTY_DIR"
touch "$REPORTS_DB"
touch "$MEMBER_DB"

IS_ADMIN="false"

log_action() {
    printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$1" >> "$BOUNTY_DIR/bounty_activity.log"
}

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

    echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BG_R}${W}  ║  ☠  C Z H   B U G F I N D E R   -   H U N T E R   L A B  ☠      ║${NC}"
    echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
    
    echo -e "${BG_B}${W}  [!] SYSTEM STATUS: ACTIVE // AUTHORIZED HUNTING ONLY            ${NC}\n"
    echo -e "${Y}  ⚠ TARGET SCOPE: Authorized systems & localhost only."
    echo -e "  ⚠ UNAUTHORIZED HUNTING IS ILLEGAL AND PROHIBITED."
    echo -e "  ⚠ ALL REPORTS ARE MONITORED AND LOGGED.${NC}\n"
    
    echo -e "${C}  ┌──────────────────────────────────────────────────────────┐${NC}"
    echo -e "${C}  │${NC} ${Y}[1]${W} VIEW AUTHORIZED TARGETS & RULES                     ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[2]${W} SUBMIT A NEW BUG REPORT (FOUND A FLAW?)            ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[3]${W} VIEW MY SUBMITTED REPORTS                           ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[4]${W} READ BUG BOUNTY RESOURCES                           ${C}│${NC}"
    if [ "$IS_ADMIN" == "true" ]; then
        echo -e "${C}  │${NC} ${R}[5]${W} ADMIN REVIEW PANEL (Accept/Reject)                  ${C}│${NC}"
    fi
    echo -e "${C}  ├──────────────────────────────────────────────────────────┤${NC}"
    echo -e "${C}  │${NC} ${R}[0]${W} ABORT & EXIT BUG FINDER                             ${C}│${NC}"
    echo -e "${C}  └──────────────────────────────────────────────────────────┘${NC}\n"
    
    echo -e "${D}  [ SESSION MONITORED BY CZH CYBER TEAM ]${NC}\n"
    
    read -r -p "$(echo -e "${R}  BUG HUNTER ➜ ${NC}")" choice

    case "$choice" in
        1)
            clear
            echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${BG_R}${W}  ║  ☠  A U T H O R I Z E D   T A R G E T S   &   R U L E S  ☠      ║${NC}"
            echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
            echo -e "${W}  You are ONLY allowed to test on the following:${NC}"
            echo -e "${G}  ✔ Your own domains / servers / VPS${NC}"
            echo -e "${G}  ✔ Localhost (127.0.0.1)${NC}"
            echo -e "${G}  ✔ Deliberately vulnerable practice sites (HackTheBox, TryHackMe, PortSwigger)${NC}\n"
            echo -e "${R}  ✗ NEVER test on public websites or companies without written permission.${NC}"
            echo -e "${R}  ✗ NEVER use these reports for malicious intent.${NC}\n"
            log_action "Viewed Authorized Targets"
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        2)
            clear
            echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${BG_R}${W}  ║  ☠  S U B M I T   A   N E W   B U G   R E P O R T  ☠            ║${NC}"
            echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
            
            read -r -p "$(echo -e "${Y}  Your Hacker Alias (must match member): ${NC}")" alias
            if ! grep -q "^$alias:" "$MEMBER_DB"; then
                echo -e "\n${R}  [✗] Alias not found in Member Database. Register first!${NC}"
                read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
                continue
            fi
            
            read -r -p "$(echo -e "${Y}  Target URL/IP: ${NC}")" target
            read -r -p "$(echo -e "${Y}  Vulnerability Type (e.g., XSS, SQLi): ${NC}")" v_type
            echo -e "${Y}  Severity:${NC}"
            echo "  1) Low (5 points)"
            echo "  2) Medium (15 points)"
            echo "  3) High (30 points)"
            echo "  4) Critical (50 points)"
            read -r -p "  Select Severity [1-4]: " sev_choice
            
            case "$sev_choice" in
                1) severity="Low" ;;
                2) severity="Medium" ;;
                3) severity="High" ;;
                4) severity="Critical" ;;
                *) severity="Low" ;;
            esac
            
            echo -e "${Y}  Description (Type END on a new line to finish):${NC}"
            desc=""
            while read -r line; do
                [[ "${line^^}" == "END" ]] && break
                desc="$desc$line "
            done
            
            ID="B-$(date +%s | tail -c 5)"
            echo "$ID|$alias|$target|$v_type|$severity|PENDING|$desc" >> "$REPORTS_DB"
            log_action "New bug report submitted by $alias ($severity)"
            
            echo -e "\n${G}  [✓] REPORT SUBMITTED! ID: $ID. Admin will review it.${NC}"
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        3)
            clear
            echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${BG_R}${W}  ║  ☠  Y O U R   S U B M I T T E D   R E P O R T S  ☠              ║${NC}"
            echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
            read -r -p "$(echo -e "${Y}  Enter your Hacker Alias: ${NC}")" search_alias
            echo ""
            if grep -q "|$search_alias|" "$REPORTS_DB"; then
                echo -e "${C}  ID    | TARGET          | TYPE      | SEVERITY | STATUS${NC}"
                echo -e "${D}  ---------------------------------------------------------${NC}"
                awk -F'|' -v al="$search_alias" '$2==al {printf "  %-5s | %-15s | %-9s | %-8s | %s\n", $1, $3, $4, $5, $6}' "$REPORTS_DB"
            else
                echo -e "${Y}  No reports found for this alias.${NC}"
            fi
            log_action "Checked own bug reports"
            echo ""
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        4)
            clear
            echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${BG_R}{W}  ║  ☠  B U G   B O U N T Y   R E S O U R C E S  ☠                  ║${NC}"
            echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
            echo -e "${W}  1. OWASP Top 10: ${D}https://owasp.org/www-project-top-ten/${NC}"
            echo -e "${W}  2. HackerOne 101: ${D}https://www.hackerone.com/${NC}"
            echo -e "${W}  3. PortSwigger Academy: ${D}https://portswigger.net/web-security${NC}"
            echo -e "${W}  4. Bugcrowd University: ${D}https://www.bugcrowd.com/hackers/bugcrowd-university/${NC}\n"
            log_action "Viewed Bug Bounty Resources"
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        5)
            if [ "$IS_ADMIN" == "true" ]; then
                clear
                echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
                echo -e "${BG_R}${W}  ║  ☠  A D M I N   R E V I E W   P A N E L  ☠                      ║${NC}"
                echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
                
                PENDING=$(grep "|PENDING|" "$REPORTS_DB" || true)
                if [ -z "$PENDING" ]; then
                    echo -e "${G}  [✓] No pending reports to review.${NC}"
                else
                    echo -e "${C}  PENDING REPORTS:${NC}"
                    echo "$PENDING" | awk -F'|' '{printf "  [%s] Alias: %s | Sev: %s | Type: %s\n", $1, $2, $5, $4}'
                    echo ""
                    read -r -p "$(echo -e "${Y}  Enter Report ID to review (or press Enter to cancel): ${NC}")" rid
                    
                    if [ -n "$rid" ]; then
                        REPORT=$(grep "^$rid|" "$REPORTS_DB")
                        if [ -n "$REPORT" ]; then
                            ALIAS=$(echo "$REPORT" | cut -d'|' -f2)
                            SEV=$(echo "$REPORT" | cut -d'|' -f5)
                            
                            echo -e "\n${C}  Target  : ${W}$(echo "$REPORT" | cut -d'|' -f3)${NC}"
                            echo -e "${C}  Type    : ${W}$(echo "$REPORT" | cut -d'|' -f4)${NC}"
                            echo -e "${C}  Desc    : ${W}$(echo "$REPORT" | cut -d'|' -f7)${NC}\n"
                            
                            read -r -p "$(echo -e "${Y}  [A]ccept or [R]eject? ${NC}")" action
                            if [[ "$action" == "a" || "$action" == "A" ]]; then
                                # Update Report
                                awk -F'|' -v OFS='|' -v r="$rid" '{if($1==r) $6="ACCEPTED"; print}' "$REPORTS_DB" > "${REPORTS_DB}.tmp" && mv "${REPORTS_DB}.tmp" "$REPORTS_DB"
                                
                                # Award Points
                                case "$SEV" in
                                    Low) PTS=5 ;;
                                    Medium) PTS=15 ;;
                                    High) PTS=30 ;;
                                    Critical) PTS=50 ;;
                                    *) PTS=0 ;;
                                esac
                                awk -F: -v OFS=: -v al="$ALIAS" -v p="$PTS" '{if($1==al) $5=$5+p; print}' "$MEMBER_DB" > "${MEMBER_DB}.tmp" && mv "${MEMBER_DB}.tmp" "$MEMBER_DB"
                                echo -e "\n${G}  [✓] Report ACCEPTED. $PTS points awarded to $ALIAS.${NC}"
                                log_action "ADMIN: Accepted report $rid. Awarded $PTS pts to $ALIAS."
                            elif [[ "$action" == "r" || "$action" == "R" ]]; then
                                awk -F'|' -v OFS='|' -v r="$rid" '{if($1==r) $6="REJECTED"; print}' "$REPORTS_DB" > "${REPORTS_DB}.tmp" && mv "${REPORTS_DB}.tmp" "$REPORTS_DB"
                                echo -e "\n${R}  [✗] Report REJECTED.${NC}"
                                log_action "ADMIN: Rejected report $rid."
                            else
                                echo -e "\n${Y}  [!] Invalid action.${NC}"
                            fi
                        else
                            echo -e "\n${R}  [✗] Invalid Report ID.${NC}"
                        fi
                    fi
                fi
                read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            else
                echo -e "${R}\n  [✗] ACCESS DENIED. ADMIN ONLY.${NC}"
                sleep 1
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
