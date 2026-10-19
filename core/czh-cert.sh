#!/data/data/com.termux/files/usr/bin/bash

PROGRESS_FILE="$HOME/CZH/PrivateData/course-progress.json"
R='\033[91m'; G='\033[92m'; Y='\033[93m'; C='\033[96m'; W='\033[97m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

clear
echo -e "${R}"
echo -e "  ██████╗███████╗██████╗ ████████╗██╗███████╗██╗███████╗██████╗ "
echo -e " ██╔════╝██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝██║██╔════╝██╔══██╗"
echo -e " ██║     █████╗  ██████╔╝   ██║   ██║█████╗  ██║█████╗  ██║  ██║"
echo -e " ██║     ██╔══╝  ██╔══██╗   ██║   ██║██╔══╝  ██║██╔══╝  ██║  ██║"
echo -e " ╚██████╗███████╗██║  ██║   ██║   ██║██║     ██║███████╗██████╔╝"
echo -e "  ╚═════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚═════╝ "
echo -e "${NC}"

echo -e "${C}  [*] Bypassing Academy Security...${NC}"
sleep 1

if [ "$1" == "preview" ]; then
    COMPLETED=10
else
    COMPLETED=$(python3 -c "import json; print(len(json.load(open('$PROGRESS_FILE')).get('completed', [])))" 2>/dev/null || echo 0)
fi

if [ "$COMPLETED" -lt 10 ] && [ "$1" != "preview" ]; then
    echo -e "\n${BG_R}${W}  [✗] ACCESS DENIED. INSUFFICIENT CLEARANCE.  ${NC}"
    echo -e "${Y}  Modules: ${W}$COMPLETED/10${NC}"
    exit 1
fi

read -r -p "$(echo -e "${C}  [?] Enter Hacker Alias: ${NC}")" alias
if [ -z "$alias" ]; then alias="UNKNOWN"; fi

DATE=$(date '+%Y-%m-%d')
CERT_ID="CZH-$(head /dev/urandom | tr -dc A-Z0-9 | head -c 6)"

clear
echo -e "${R}  ╔══════════════════════════════════════════════════╗${NC}"
echo -e "${R}  ║ ${BG_R}${W} ☠ C Z H   E L I T E   C E R T I F I C A T E ☠ ${NC}${R} ║${NC}"
echo -e "${R}  ╠══════════════════════════════════════════════════╣${NC}"
echo -e "  ${R}║${NC} ${Y}STATUS: ${G}VERIFIED & DANGEROUS${NC}                        ${R}║${NC}"
echo -e "  ${R}║${NC} ${Y}DATE:   ${W}$DATE${NC}                                ${R}║${NC}"
echo -e "  ${R}║${NC} ${Y}ID:     ${C}$CERT_ID${NC}                            ${R}║${NC}"
echo -e "${R}  ╠══════════════════════════════════════════════════╣${NC}"
echo -e "  ${R}║${NC}                                                  ${R}║${NC}"
echo -e "  ${R}║${NC}      This certifies that the hacker known as     ${R}║${NC}"
echo -e "  ${R}║${NC}                                                  ${R}║${NC}"
echo -e "  ${R}║${NC}               ${W}>> $alias <<${NC}                     ${R}║${NC}"
echo -e "  ${R}║${NC}                                                  ${R}║${NC}"
echo -e "  ${R}║${NC}      has successfully infiltrated all 10         ${R}║${NC}"
echo -e "  ${R}║${NC}      modules of the CZH BLACKSITE and is         ${R}║${NC}"
echo -e "  ${R}║${NC}      hereby recognized as a                      ${R}║${NC}"
echo -e "  ${R}║${NC}                                                  ${R}║${NC}"
echo -e "  ${R}║${NC}      ${BG_R}${W} ☠ ELITE CZH HACKER ☠ ${NC}                     ${R}║${NC}"
echo -e "${R}  ╠══════════════════════════════════════════════════╣${NC}"
echo -e "  ${R}║${NC} ${W}Authorized Signatory:${NC}                            ${R}║${NC}"
echo -e "  ${R}║${NC} ${G}  _  __  _   _    _    _   _  ${NC}                      ${R}║${NC}"
echo -e "  ${R}║${NC} ${G} | |/ / | | | |  / \\  | \\ | | ${NC}                      ${R}║${NC}"
echo -e "  ${R}║${NC} ${G} | ' /  | |_| | / _ \\ |  \\| | ${NC}                      ${R}║${NC}"
echo -e "  ${R}║${NC} ${G} | . \\  |  _  |/ ___ \\| |\\  | ${NC}                      ${R}║${NC}"
echo -e "  ${R}║${NC} ${G} |_|\\_\\ |_| |_/_/   \\_\\_| \\_| ${NC}                      ${R}║${NC}"
echo -e "  ${R}║${NC} ${Y}[ KHAN ] ${C}CEO / FOUNDER // CZH${NC}                    ${R}║${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════════╝${NC}"
read -r -p "  Press Enter to exit..."
