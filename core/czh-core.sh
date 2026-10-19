#!/data/data/com.termux/files/usr/bin/bash

PLATFORM="${CZH_PLATFORM_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
CONFIG="$PLATFORM/config/platform.conf"

R='\033[91m'
G='\033[92m'
Y='\033[93m'
C='\033[96m'
W='\033[97m'
D='\033[90m'
BG_R='\033[41m'
BG_G='\033[42m'
BG_B='\033[44m'
NC='\033[0m'

clear

# Perfectly Straight CZH CORE ASCII Art
echo -e "${C}"
echo -e "      ██████╗███████╗██╗  ██╗"
echo -e "     ██╔════╝╚══███╔╝██║  ██║"
echo -e "     ██║       ███╔╝ ███████║"
echo -e "     ██║      ███╔╝  ██╔══██║"
echo -e "     ╚██████╗███████╗██║  ██║"
echo -e "      ╚═════╝╚══════╝╚═╝  ╚═╝"
echo -e "${W}      ██████╗ ██████╗ ██████╗ ███████╗"
echo -e "     ██╔════╝██╔═══██╗██╔══██╗██╔════╝"
echo -e "     ██║     ██║   ██║██████╔╝█████╗  "
echo -e "     ██║     ██║   ██║██╔══██╗██╔══╝  "
echo -e "     ╚██████╗╚██████╔╝██║  ██║███████╗"
echo -e "      ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝"
echo -e "${NC}"

# Danger Borders
echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BG_R}${W}  ║  ☠  S Y S T E M   F O U N D A T I O N   S T A T U S  ☠          ║${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"

# Identity Section
echo -e "${C}  ┌───[ C O R E   I D E N T I T Y ]──────────────────────────────────┐${NC}"
echo -e "  ${W}▶ Platform Name : ${G}CZH LAB${NC}"
echo -e "  ${W}▶ Build Version : ${G}2.0.0-dev${NC}"
echo -e "  ${W}▶ Root Directory: ${D}$PLATFORM${NC}"
echo -e "  ${W}▶ Security Mode : ${Y}WHITE HAT / ETHICAL${NC}"
echo -e "${C}  └──────────────────────────────────────────────────────────────────┘${NC}\n"

# Configuration Section
echo -e "${C}  ┌───[ C O N F I G U R A T I O N ]──────────────────────────────────┐${NC}"
if [ -f "$CONFIG" ]; then
    echo -e "  ${G}[ ✔ ] platform.conf is present and readable.${NC}"
else
    echo -e "  ${R}[ ✗ ] CRITICAL: platform.conf is MISSING!${NC}"
fi
echo -e "${C}  └──────────────────────────────────────────────────────────────────┘${NC}\n"

# Modules Section
echo -e "${C}  ┌───[ M O D U L E   F O U N D A T I O N S ]────────────────────────┐${NC}"
MODULES=("core" "install" "members" "ai" "catalog/tools" "catalog/labs" "catalog/projects" "czh-darklab" "czh-bugfinder")
for mod in "${MODULES[@]}"; do
    if [ -d "$PLATFORM/$mod" ]; then
        printf "  ${G}[ ✔ ] Directory: %-25s ${G}ONLINE${NC}\n" "$mod"
    else
        printf "  ${R}[ ✗ ] Directory: %-25s ${R}OFFLINE${NC}\n" "$mod"
    fi
done
echo -e "${C}  └──────────────────────────────────────────────────────────────────┘${NC}\n"

# Warning Footer
echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BG_R}${W}  ║  ⚠  WARNING: UNAUTHORIZED MODIFICATIONS ARE LOGGED & BLOCKED  ⚠  ║${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}"
echo ""

if [[ "${1:-}" != "--no-pause" ]]; then
    read -r -p "  Press Enter to return..."
fi
