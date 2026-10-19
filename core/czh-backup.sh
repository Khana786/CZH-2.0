#!/data/data/com.termux/files/usr/bin/bash

clear
R='\033[91m'
G='\033[92m'
Y='\033[93m'
C='\033[96m'
W='\033[97m'
D='\033[90m'
BG_B='\033[44m'
BG_G='\033[42m'
NC='\033[0m'

BACKUP_DIR="$HOME/CZH/Backups"
mkdir -p "$BACKUP_DIR"

# Check if zip is installed
if ! command -v zip >/dev/null 2>&1; then
    echo -e "${Y}  [*] Installing zip utility...${NC}"
    pkg install zip -y > /dev/null 2>&1
fi

TIMESTAMP=$(date '+%Y%m%d-%H%M%S')
BACKUP_FILE="$BACKUP_DIR/CZH_FULL_BACKUP_$TIMESTAMP.zip"

clear
echo -e "${C}"
echo -e "      ██████╗ █████╗  ██████╗██╗  ██╗██╗   ██╗██████╗ "
echo -e "      ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║   ██║██╔══██╗"
echo -e "      ██████╔╝███████║██║     █████╔╝ ██║   ██║██████╔╝"
echo -e "      ██╔══██╗██╔══██║██║     ██╔═██╗ ██║   ██║██╔═══╝ "
echo -e "      ██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║     "
echo -e "      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     "
echo -e "${NC}"

echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BG_R}${W}  ║  ☠  C Z H   S E C U R E   B A C K U P   S Y S T E M  ☠         ║${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"

echo -e "${Y}  [!] Preparing to backup the entire CZH System...${NC}"
echo -e "${C}  [*] Compressing Core Files, Members, Bug Reports, and Keys...${NC}"

# Change to home directory to keep paths relative
cd "$HOME" || exit 1

# Create the zip file (excluding backups, .git, and caches)
zip -r "$BACKUP_FILE" \
    "CZH/Platform-v2" \
    "CZH/PrivateData" \
    "CZH-Termux-Branding-" \
    -x "*/Backups/*" "*.git/*" "*__pycache__*" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo -e "\n${G}  [✓] BACKUP CREATED SUCCESSFULLY!${NC}"
    echo -e "${W}  Location: ${C}$BACKUP_FILE${NC}"
    
    # Calculate size
    SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
    echo -e "${W}  Size    : ${G}$SIZE${NC}\n"
    
    echo -e "${Y}  [!] IMPORTANT INSTRUCTIONS:${NC}"
    echo -e "  1. Copy this ZIP file to your Pendrive / Google Drive."
    echo -e "  2. To restore in the future, just unzip it in Termux."
    echo -e "  3. This file contains your Master Keys and Private Data."
    echo -e "  4. DO NOT SHARE THIS FILE WITH ANYONE.\n"
else
    echo -e "\n${R}  [✗] BACKUP FAILED. Check storage space.${NC}\n"
fi

echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BG_G}${W}  ║  [+] SESSION SECURED BY CZH CYBER TEAM                         ║${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}"
echo ""
read -r -p "  Press Enter to exit..."
