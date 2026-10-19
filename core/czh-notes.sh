#!/data/data/com.termux/files/usr/bin/bash

NOTES_FILE="$HOME/CZH/PrivateData/secure_notes.db"
touch "$NOTES_FILE"
chmod 600 "$NOTES_FILE"

R='\033[91m'
G='\033[92m'
Y='\033[93m'
C='\033[96m'
W='\033[97m'
D='\033[90m'
BG_R='\033[41m'
NC='\033[0m'

while true; do
    clear
    echo -e "${C}"
    echo -e "      ███╗   ██╗ ██████╗ ████████╗███████╗███████╗"
    echo -e "      ████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝██╔════╝"
    echo -e "      ██╔██╗ ██║██║   ██║   ██║   █████╗  ███████╗"
    echo -e "      ██║╚██╗██║██║   ██║   ██║   ██╔══╝  ╚════██║"
    echo -e "      ██║ ╚████║╚██████╔╝   ██║   ███████╗███████║"
    echo -e "      ╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝"
    echo -e "${NC}"
    
    echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BG_R}${W}  ║  ☠  C Z H   S E C U R E   N O T E S   V A U L T  ☠              ║${NC}"
    echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
    
    echo -e "${Y}  [!] Only Admin can view existing notes. Members can only add.${NC}\n"
    
    echo -e "${C}  ┌────────────────────────────────────────────┐${NC}"
    echo -e "  ${C}│${NC} ${Y}[1]${W} ADD NEW SECURE NOTE                    ${C}│${NC}"
    echo -e "  ${C}│${NC} ${Y}[2]${W} VIEW ALL NOTES (Admin Key Required)    ${C}│${NC}"
    echo -e "  ${C}│${NC} ${R}[3]${W} CLEAR ALL NOTES (Admin Only)           ${C}│${NC}"
    echo -e "  ${C}├────────────────────────────────────────────┤${NC}"
    echo -e "  ${C}│${NC} ${R}[0]${W} ABORT & EXIT                           ${C}│${NC}"
    echo -e "${C}  └────────────────────────────────────────────┘${NC}\n"
    
    read -r -p "$(echo -e "${R}  CZH-NOTES ➜ ${NC}")" choice
    
    case "$choice" in
        1)
            echo ""
            read -r -p "$(echo -e "${Y}  Enter Author Alias: ${NC}")" author
            echo -e "${Y}  Enter Note (Type END on a new line to finish):${NC}"
            note=""
            while read -r line; do
                [[ "${line^^}" == "END" ]] && break
                note="$note$line "
            done
            
            if [ -n "$note" ]; then
                DATE=$(date '+%Y-%m-%d %H:%M:%S')
                echo "[$DATE] [$author] $note" >> "$NOTES_FILE"
                echo -e "\n${G}  [✓] Note saved securely.${NC}"
            else
                echo -e "\n${R}  [✗] Note was empty.${NC}"
            fi
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        2)
            echo ""
            read -r -s -p "$(echo -e "${R}  Enter Admin Key: ${NC}")" admin_key
            echo ""
            
            if [ "$admin_key" == "CZH-DARKWEB-QEP5ES" ]; then
                echo -e "\n${C}  --- SECURE NOTES ---${NC}"
                if [ -s "$NOTES_FILE" ]; then
                    cat "$NOTES_FILE"
                else
                    echo -e "  ${Y}No notes available yet.${NC}"
                fi
            else
                echo -e "\n${R}  [✗] ACCESS DENIED. Invalid Admin Key.${NC}"
            fi
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        3)
            echo ""
            read -r -s -p "$(echo -e "${R}  Enter Admin Key to clear: ${NC}")" admin_key
            echo ""
            
            if [ "$admin_key" == "CZH-DARKWEB-QEP5ES" ]; then
                > "$NOTES_FILE"
                echo -e "\n${R}  [✓] All secure notes wiped permanently.${NC}"
            else
                echo -e "\n${R}  [✗] ACCESS DENIED. Invalid Admin Key.${NC}"
            fi
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        0)
            echo -e "${R}\n  [!] CLOSING SECURE NOTES VAULT.${NC}"
            exit 0
            ;;
        *)
            echo -e "${R}  [✗] Invalid option.${NC}"
            sleep 1
            ;;
    esac
done
