#!/data/data/com.termux/files/usr/bin/bash

DIR="$1"
TITLE="$2"

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

echo -e "${C}"
echo -e "      ██████╗███████╗██╗  ██╗    ██╗     █████╗ ██████╗ "
echo -e "     ██╔════╝╚══███╔╝██║  ██║    ██║    ██╔══██╗██╔══██╗"
echo -e "     ██║       ███╔╝ ███████║    ██║    ███████║██████╔╝"
echo -e "     ██║      ███╔╝  ██╔══██║    ██║    ██╔══██║██╔══██╗"
echo -e "     ╚██████╗███████╗██║  ██║    ███████╗██║  ██║██████╔╝"
echo -e "      ╚═════╝╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═════╝ "
echo -e "${NC}"

echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BG_R}${W}  ☠  C Z H   $TITLE  ☠  ${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"

if [ -d "$DIR" ]; then
    echo -e "${C}  ┌───[ D O C U M E N T A T I O N ]──────────────────────────────────┐${NC}"
    if [ -f "$DIR/README.md" ]; then
        head -n 12 "$DIR/README.md" | sed 's/^/  \033[97m/; s/$/\033[0m/'
        echo -e "  ${D}... (Open README.md for full details)${NC}"
    else
        echo -e "  ${Y}[!] No documentation found.${NC}"
    fi
    echo -e "${C}  └──────────────────────────────────────────────────────────────────┘${NC}\n"

    echo -e "${C}  ┌───[ A V A I L A B L E   F I L E S ]──────────────────────────────┐${NC}"
    
    FILE_COUNT=0
    for file in "$DIR"/*; do
        if [ -f "$file" ] && [[ "$file" != *"README.md"* ]] && [[ "$file" != *".bak"* ]]; then
            FILENAME=$(basename "$file")
            echo -e "  ${G}[✔] ${W}$FILENAME${NC}"
            ((FILE_COUNT++))
        fi
    done
    
    if [ "$FILE_COUNT" -eq 0 ]; then
        echo -e "  ${Y}[!] No files found in this catalog.${NC}"
    fi
    echo -e "${C}  └──────────────────────────────────────────────────────────────────┘${NC}\n"
else
    echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BG_R}${W}  [✗] ERROR: Catalog directory not found.${NC}"
    echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
fi

echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BG_B}${W}  [+] SYSTEM MONITORING ACTIVE // CZH SECURE                      ${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}"
echo ""

read -r -p "  Press Enter to return..."
