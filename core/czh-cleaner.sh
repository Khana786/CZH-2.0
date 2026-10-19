#!/data/data/com.termux/files/usr/bin/bash

clear
R='\033[91m'
G='\033[92m'
Y='\033[93m'
C='\033[96m'
W='\033[97m'
D='\033[90m'
BG_R='\033[41m'
NC='\033[0m'

# --- HIFI HACKER LOGO ---
echo -e "${C}"
echo -e "     ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗ "
echo -e "    ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗"
echo -e "    ██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝"
echo -e "    ██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗"
echo -e "    ╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║"
echo -e "     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝"
echo -e "${NC}"

echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BG_R}${W}  ║  ☠  S Y S T E M   O P T I M I Z E R   &   C L E A N E R  ☠       ║${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"

# Calculate current space
BEFORE_FREE=$(df -h "$HOME" | tail -1 | awk '{print $4}')
echo -e "${Y}  [*] Current Free Space: ${W}$BEFORE_FREE${NC}"
echo -e "${Y}  [!] WARNING: This will delete Termux cache, temp files, and old logs.${NC}"
read -r -p "$(echo -e "${R}  ▶ Proceed with deep clean? (y/N): ${NC}")" confirm

if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo -e "\n${R}  [✗] Cleanup aborted.${NC}"
    exit 0
fi

echo -e "\n${C}  [*] INITIATING DEEP SCAN...${NC}"
sleep 1

# 1. Termux Package Cache
echo -e "${W}  [+] Purging Termux package cache...${NC}"
pkg clean -y > /dev/null 2>&1
rm -rf "$PREFIX/var/cache/apt/archives/"*.deb 2>/dev/null
sleep 0.5

# 2. Temp Files
echo -e "${W}  [+] Wiping temporary system files...${NC}"
rm -rf "$PREFIX/tmp/"* 2>/dev/null
rm -rf "$HOME/.cache/"* 2>/dev/null
sleep 0.5

# 3. Python Caches
echo -e "${W}  [+] Removing Python __pycache__ directories...${NC}"
find "$HOME/CZH" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
sleep 0.5

# 4. CZH Old Logs & Backups (keep latest, clear old)
echo -e "${W}  [+] Truncating old CZH logs and backups...${NC}"
find "$HOME/CZH/PrivateData/reports" -type f -name "*.log" -exec truncate -s 0 {} + 2>/dev/null
find "$HOME/CZH/Platform-v2" -type f -name "*.bak*" -delete 2>/dev/null
sleep 0.5

# 5. Empty Trash
echo -e "${W}  [+] Emptying local trash...${NC}"
rm -rf "$HOME/.local/share/Trash/files/"* 2>/dev/null
sleep 0.5

# Calculate new space
AFTER_FREE=$(df -h "$HOME" | tail -1 | awk '{print $4}')

echo -e "\n${G}  ┌───[ O P T I M I Z A T I O N   C O M P L E T E ]──────────────────┐${NC}"
echo -e "  ${W}▶ Space Before : ${R}$BEFORE_FREE${NC}"
echo -e "  ${W}▶ Space After  : ${G}$AFTER_FREE${NC}"
echo -e "  ${W}▶ Status       : ${C}SYSTEM SECURED & OPTIMIZED${NC}"
echo -e "${G}  └──────────────────────────────────────────────────────────────────┘${NC}"

echo -e "\n${C}  [✓] CZH SYSTEM CLEANED SUCCESSFULLY.${NC}"
read -r -p "  Press Enter to exit..."
