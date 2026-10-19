#!/data/data/com.termux/files/usr/bin/bash
clear
R='\033[91m'; G='\033[92m'; Y='\033[93m'; C='\033[96m'; W='\033[97m'; NC='\033[0m'
LOG_FILE="$HOME/CZH/PrivateData/reports/activity.log"

echo -e "${R}  ╔══════════════════════════════════════════════╗${NC}"
echo -e "${R}  ║ ${C}☠  A C T I V I T Y   &   E R R O R S${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════╝${NC}\n"

if [ -f "$LOG_FILE" ]; then
    echo -e "${Y}  [+] RECENT LOGS (Last 15):${NC}"
    tail -n 15 "$LOG_FILE" | while read -r line; do
        if [[ "$line" == *"ERROR"* ]]; then
            echo -e "  ${R}$line${NC}"
        else
            echo -e "  ${G}$line${NC}"
        fi
    done
else
    echo -e "${Y}  [!] No activity logs found yet.${NC}"
fi
echo ""
read -r -p "  Press Enter to return..."
