#!/data/data/com.termux/files/usr/bin/bash
clear
R='\033[91m'; G='\033[92m'; Y='\033[93m'; C='\033[96m'; W='\033[97m'; NC='\033[0m'
echo -e "${R}  ╔══════════════════════════════════════════════╗${NC}"
echo -e "${R}  ║ ${C}☠  S Y S T E M   D I A G N O S T I C S${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════╝${NC}\n"

echo -e "${Y}  [+] STORAGE HEALTH:${NC}"
df -h "$HOME" | tail -n 1 | awk '{print "  Used: "$3" / Total: "$2" ("$5")"}'
echo ""
echo -e "${Y}  [+] MEMORY STATUS:${NC}"
free -h | grep "Mem:" | awk '{print "  Used: "$3" / Total: "$2}'
echo ""
echo -e "${Y}  [+] CORE MODULES:${NC}"
for dir in core catalog install members ai; do
    [ -d "$HOME/CZH/Platform-v2/$dir" ] && echo -e "  ${G}✔ $dir${NC}" || echo -e "  ${R}✗ $dir (MISSING)${NC}"
done
echo ""
read -r -p "  Press Enter to return..."
