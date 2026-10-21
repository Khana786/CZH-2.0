#!/data/data/com.termux/files/usr/bin/bash

clear
R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

echo -e "${C}"
echo -e "      ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗"
echo -e "      ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝"
echo -e "      ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  "
echo -e "      ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  "
echo -e "      ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗"
echo -e "       ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝"
echo -e "${NC}"
echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BG_R}${W}  ║  ☠  C Z H   A U T O - U P D A T E R  ☠                           ║${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"

echo -e "${Y}  [*] Checking for updates from GitHub...${NC}"
sleep 1

RELEASE_DIR="$HOME/CZH-2.0-PUBLIC-RELEASE"

if [ ! -d "$RELEASE_DIR" ]; then
    echo -e "${R}  [✗] Error: Release directory not found.${NC}"
    echo -e "${Y}  [!] Please re-clone the repository from GitHub.${NC}"
    exit 1
fi

cd "$RELEASE_DIR" || exit 1

# Check if there are new updates
git fetch origin main >/dev/null 2>&1
BEHIND=$(git rev-list --count HEAD..origin/main)

if [ "$BEHIND" -eq 0 ]; then
    echo -e "\n${G}  [✓] Your CZH is already up-to-date! (Version 2.0.0)${NC}"
    exit 0
fi

echo -e "\n${C}  [*] Found $BEHIND new update(s). Applying now...${NC}"

# Backup user's current config just in case
cp -r "$RELEASE_DIR/config" "$HOME/CZH/Backups/config_backup_$(date +%s)" 2>/dev/null

# Pull the update
git pull origin main >/dev/null 2>&1

if [ $? -eq 0 ]; then
    echo -e "\n${G}  ┌───[ U P D A T E   C O M P L E T E ]──────────────────────────┐${NC}"
    echo -e "  ${W}▶ Status : ${G}SUCCESS${NC}"
    echo -e "  ${W}▶ Version: ${G}Latest (GitHub Main)${NC}"
    echo -e "${G}  └──────────────────────────────────────────────────────────────┘${NC}\n"
    
    # Copy updated tools to local execution paths
    cp "$RELEASE_DIR/czh-arsenal.sh" "$HOME/CZH/Platform-v2/" 2>/dev/null
    cp -r "$RELEASE_DIR/catalog/tools/"* "$HOME/CZH/Platform-v2/catalog/tools/" 2>/dev/null
    cp -r "$RELEASE_DIR/core/"* "$HOME/CZH/Platform-v2/core/" 2>/dev/null
    chmod +x "$HOME/CZH/Platform-v2/czh-arsenal.sh" 2>/dev/null
    chmod +x "$HOME/CZH/Platform-v2/core/"*.sh 2>/dev/null
    
    echo -e "${Y}  [✓] Local Termux Environment Updated.${NC}"
    echo -e "${D}  [!] Note: Your private data in PrivateData/ was NOT touched.${NC}"
else
    echo -e "\n${R}  [✗] Update failed. Check your internet connection or Git conflicts.${NC}"
fi

echo ""
input=$(read -p "  Press Enter to exit...")
