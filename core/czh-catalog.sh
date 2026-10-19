#!/data/data/com.termux/files/usr/bin/bash
clear
R='\033[91m'; G='\033[92m'; Y='\033[93m'; C='\033[96m'; W='\033[97m'; NC='\033[0m'
DIR="$1"
TITLE="$2"

echo -e "${R}  ╔══════════════════════════════════════════════╗${NC}"
echo -e "${R}  ║ ${C}☠  $TITLE${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════╝${NC}\n"

if [ -d "$DIR" ]; then
    if [ -f "$DIR/README.md" ]; then
        echo -e "${Y}  [+] DOCUMENTATION:${NC}"
        head -n 15 "$DIR/README.md"
        echo ""
    fi
    echo -e "${Y}  [+] AVAILABLE FILES:${NC}"
    find "$DIR" -maxdepth 1 -type f ! -name "README.md" -printf "  ${G}▶ %f${NC}\n"
else
    echo -e "${R}  [✗] ERROR: Directory not found.${NC}"
fi
echo ""
read -r -p "  Press Enter to return..."
