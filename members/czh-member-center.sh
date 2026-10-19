#!/data/data/com.termux/files/usr/bin/bash

clear
R='\033[91m'
G='\033[92m'
Y='\033[93m'
C='\033[96m'
W='\033[97m'
D='\033[90m'
MAG='\033[95m'
BG_R='\033[41m'
BG_B='\033[44m'
NC='\033[0m'

MEMBER_DIR="$HOME/CZH/PrivateData/Members"
mkdir -p "$MEMBER_DIR"
touch "$MEMBER_DIR/members.db"
chmod 600 "$MEMBER_DIR/members.db"

log_action() {
    printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$1" >> "$MEMBER_DIR/member_activity.log"
}

while true; do
    clear
    TOTAL_MEMBERS=$(wc -l < "$MEMBER_DIR/members.db" 2>/dev/null || echo 0 | tr -d ' ')
    
    echo -e "${R}"
    echo -e "     ██████╗███████╗██╗  ██╗    ██╗  ██╗██╗   ██╗██████╗ "
    echo -e "    ██╔════╝╚══███╔╝██║  ██║    ██║  ██║██║   ██║██╔══██╗"
    echo -e "    ██║       ███╔╝ ███████║    ███████║██║   ██║██████╔╝"
    echo -e "    ██║      ███╔╝  ██╔══██║    ██╔══██║██║   ██║██╔══██╗"
    echo -e "    ╚██████╗███████╗██║  ██║    ██║  ██║╚██████╔╝██████╔╝"
    echo -e "     ╚═════╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ "
    echo -e "${C}"
    echo -e "             T E A M   C E N T E R"
    echo -e "${NC}"

    echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BG_R}${W}  ☠  C Z H   M E M B E R   C E N T E R   -   H I F I  ☠  ${NC}"
    echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    echo -e "${BG_B}${W}  [+] NETWORK STATUS: ACTIVE // TOTAL MEMBERS: $TOTAL_MEMBERS          ${NC}"
    echo ""
    
    echo -e "${C}  ┌──────────────────────────────────────────────────────────┐${NC}"
    echo -e "${C}  │${NC} ${Y}[1]${W} JOIN CZH TEAM (Register New Member)                ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[2]${W} MEMBER DIRECTORY (View All Hackers)                ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[3]${W} MY PROFILE (View Your Stats)                        ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[4]${W} LEADERBOARD (Top Hackers)                           ${C}│${NC}"
    echo -e "${C}  │${NC} ${G}[5]${W} EDIT MY PROFILE (Update Info)                       ${C}│${NC}"
    echo -e "${C}  │${NC} ${R}[6]${W} DELETE MY ACCOUNT (Leave CZH)                       ${C}│${NC}"
    echo -e "${C}  ├──────────────────────────────────────────────────────────┤${NC}"
    echo -e "${C}  │${NC} ${MAG}[A]${W} ADMIN PANEL (Owner Only)                            ${C}│${NC}"
    echo -e "${C}  │${NC} ${R}[0]${W} ABORT & EXIT MEMBER CENTER                         ${C}│${NC}"
    echo -e "${C}  └──────────────────────────────────────────────────────────┘${NC}"
    echo ""
    
    # Top 3 Hackers Mini-Dashboard
    echo -e "${Y}  [+] TOP 3 HACKERS:${NC}"
    if [ -s "$MEMBER_DIR/members.db" ]; then
        sort -t: -k5 -nr "$MEMBER_DIR/members.db" | head -n 3 | awk -F: '{print "  \033[93m#"NR"\033[97m "$1" \033[90m("$5" pts)\033[0m"}'
    else
        echo -e "  ${D}No members registered yet.${NC}"
    fi
    echo ""
    echo -e "${D}  [ SESSION MONITORED BY AARHIV HACKERS ]${NC}"
    echo ""
    read -r -p "$(echo -e "${R}  MEMBER ➜ ${NC}")" choice

    case "$choice" in
        1)
            clear
            echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${BG_R}${W}  ║  ☠  R E G I S T E R   N E W   M E M B E R  ☠                    ║${NC}"
            echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
            read -r -p "$(echo -e "${Y}  Choose Hacker Alias: ${NC}")" alias
            read -r -p "$(echo -e "${Y}  Real Name (Optional): ${NC}")" real_name
            read -r -p "$(echo -e "${Y}  Role (e.g., Pentester, Learner): ${NC}")" role
            
            if grep -q "^$alias:" "$MEMBER_DIR/members.db"; then
                echo -e "\n${R}  [✗] Alias already exists! Choose another.${NC}"
            else
                DATE=$(date '+%Y-%m-%d')
                echo "$alias:$real_name:$role:$DATE:0" >> "$MEMBER_DIR/members.db"
                log_action "New member registered: $alias"
                echo -e "\n${G}  [✓] Welcome to CZH, $alias! Registration successful.${NC}"
            fi
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        2)
            clear
            echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${BG_R}${W}  ║  ☠  C Z H   M E M B E R   D I R E C T O R Y  ☠                  ║${NC}"
            echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
            if [ -s "$MEMBER_DIR/members.db" ]; then
                echo -e "${C}  ALIAS           | ROLE            | JOINED     | POINTS${NC}"
                echo -e "${D}  -------------------------------------------------------${NC}"
                awk -F: '{printf "  %-15s | %-15s | %-10s | %s\n", $1, $3, $4, $5}' "$MEMBER_DIR/members.db"
            else
                echo -e "${Y}  No members registered yet.${NC}"
            fi
            log_action "Viewed Member Directory"
            echo ""
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        3)
            clear
            echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${BG_R}${W}  ║  ☠  M Y   P R O F I L E  ☠                                      ║${NC}"
            echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
            read -r -p "$(echo -e "${Y}  Enter your Hacker Alias: ${NC}")" search_alias
            PROFILE=$(grep "^$search_alias:" "$MEMBER_DIR/members.db")
            if [ -n "$PROFILE" ]; then
                ALIAS=$(echo "$PROFILE" | cut -d: -f1)
                REAL=$(echo "$PROFILE" | cut -d: -f2)
                ROLE=$(echo "$PROFILE" | cut -d: -f3)
                JOINED=$(echo "$PROFILE" | cut -d: -f4)
                POINTS=$(echo "$PROFILE" | cut -d: -f5)
                echo -e "${C}  ┌──────────────────────────────────────────────────────────┐${NC}"
                echo -e "  ${W}Alias   : ${G}$ALIAS${NC}"
                echo -e "  ${W}Name    : ${G}$REAL${NC}"
                echo -e "  ${W}Role    : ${G}$ROLE${NC}"
                echo -e "  ${W}Joined  : ${G}$JOINED${NC}"
                echo -e "  ${W}Points  : ${Y}$POINTS${NC}"
                echo -e "${C}  └──────────────────────────────────────────────────────────┘${NC}"
            else
                echo -e "\n${R}  [✗] Profile not found.${NC}"
            fi
            echo ""
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        4)
            clear
            echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${BG_R}${W}  ║  ☠  C Z H   L E A D E R B O A R D  ☠                            ║${NC}"
            echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
            if [ -s "$MEMBER_DIR/members.db" ]; then
                echo -e "${C}  RANK | ALIAS           | POINTS${NC}"
                echo -e "${D}  ---------------------------------${NC}"
                sort -t: -k5 -nr "$MEMBER_DIR/members.db" | awk -F: '{printf "   #%-3d| %-15s | %s\n", NR, $1, $5}' | head -10
            else
                echo -e "${Y}  No members to rank yet.${NC}"
            fi
            log_action "Viewed Leaderboard"
            echo ""
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        5)
            clear
            echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${BG_R}${W}  ║  ☠  E D I T   M Y   P R O F I L E  ☠                            ║${NC}"
            echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
            read -r -p "$(echo -e "${Y}  Enter your Hacker Alias: ${NC}")" edit_alias
            if grep -q "^$edit_alias:" "$MEMBER_DIR/members.db"; then
                read -r -p "$(echo -e "${Y}  New Real Name: ${NC}")" new_name
                read -r -p "$(echo -e "${Y}  New Role: ${NC}")" new_role
                
                # Use awk to update specific fields securely
                awk -F: -v OFS=: -v al="$edit_alias" -v nn="$new_name" -v nr="$new_role" '{
                    if($1 == al) { $2 = nn; $3 = nr; }
                    print
                }' "$MEMBER_DIR/members.db" > "${MEMBER_DIR}/members.tmp" && mv "${MEMBER_DIR}/members.tmp" "$MEMBER_DIR/members.db"
                
                echo -e "\n${G}  [✓] Profile updated successfully.${NC}"
                log_action "Member $edit_alias updated their profile."
            else
                echo -e "\n${R}  [✗] Alias not found.${NC}"
            fi
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        6)
            clear
            echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${BG_R}${W}  ║  ☠  D E L E T E   A C C O U N T  ☠                              ║${NC}"
            echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
            echo -e "${R}  ⚠ WARNING: This will permanently delete your account and points.${NC}"
            read -r -p "$(echo -e "${Y}  Enter your Hacker Alias to confirm: ${NC}")" del_alias
            if grep -q "^$del_alias:" "$MEMBER_DIR/members.db"; then
                read -r -p "$(echo -e "${R}  Are you absolutely sure? (y/N): ${NC}")" confirm
                if [[ "$confirm" == "y" || "$confirm" == "Y" ]]; then
                    grep -v "^$del_alias:" "$MEMBER_DIR/members.db" > "${MEMBER_DIR}/members.tmp" && mv "${MEMBER_DIR}/members.tmp" "$MEMBER_DIR/members.db"
                    echo -e "\n${G}  [✓] Account deleted successfully. Goodbye.${NC}"
                    log_action "Member $del_alias deleted their account."
                else
                    echo -e "\n${Y}  [!] Action cancelled.${NC}"
                fi
            else
                echo -e "\n${R}  [✗] Alias not found.${NC}"
            fi
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        A|a)
            clear
            echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${BG_R}${W}  ║  ☠  A D M I N   P A N E L  ☠                                    ║${NC}"
            echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
            read -r -s -p "$(echo -e "${R}  Enter Admin Key: ${NC}")" admin_key
            echo ""
            if [ "$admin_key" == "CZH-DARKWEB-QEP5ES" ]; then
                echo -e "${G}  [✓] Admin Access Granted.${NC}"
                echo -e "${Y}  [1] Purge Entire Database${NC}"
                echo -e "${Y}  [0] Back${NC}"
                read -r -p "  Select ➜ " admin_choice
                if [ "$admin_choice" == "1" ]; then
                    read -r -p "  Are you sure you want to wipe all members? (y/N): " wipe
                    if [[ "$wipe" == "y" ]]; then
                        > "$MEMBER_DIR/members.db"
                        echo -e "${R}  [✗] All members purged permanently.${NC}"
                        log_action "ADMIN: Purged member database"
                    fi
                fi
            else
                echo -e "${R}  [✗] Invalid Key.${NC}"
            fi
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        0)
            echo -e "${R}\n  [!] DISCONNECTING FROM MEMBER CENTER. STAY ETHICAL.${NC}"
            log_action "Exited Member Center"
            exit 0
            ;;
        *)
            echo -e "${R}\n  [✗] INVALID OPTION.${NC}"
            sleep 1
            ;;
    esac
done
