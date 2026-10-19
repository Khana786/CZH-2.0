#!/data/data/com.termux/files/usr/bin/bash

clear
R='\033[91m'
G='\033[92m'
Y='\033[93m'
C='\033[96m'
W='\033[97m'
D='\033[90m'
BG_R='\033[41m'
BG_G='\033[42m'
NC='\033[0m'

# 5-Second Boot Sequence
for i in {5..1}; do
    clear
    echo -e "${R}  ╔══════════════════════════════════════════════╗${NC}"
    echo -e "${R}  ║ ${W} ☠  C Z H   S Y S T E M   D O C T O R ${R}║${NC}"
    echo -e "${R}  ╚══════════════════════════════════════════════╝${NC}\n"
    echo -e "${C}  [ RUNNING DIAGNOSTIC PROTOCOLS... ]${NC}"
    echo -e "${D}  Scanning for vulnerabilities and anomalies...${NC}\n"
    echo -e "${Y}  [+] Injection in ${W}$i${Y}...${NC}"
    sleep 1
done
clear

# Compact & Fixed ASCII Art
echo -e "${C}"
echo -e "      ██████╗███████╗██╗  ██╗"
echo -e "     ██╔════╝╚══███╔╝██║  ██║"
echo -e "     ██║       ███╔╝ ███████║"
echo -e "     ██║      ███╔╝  ██╔══██║"
echo -e "     ╚██████╗███████╗██║  ██║"
echo -e "      ╚═════╝╚══════╝╚═╝  ╚═╝"
echo -e "${W}         D O C T O R${NC}"
echo ""

echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BG_G}${W}  [+] DIAGNOSTIC REPORT: READ-ONLY MODE ACTIVE                  ${NC}"
echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${C}  ┌───[ 1. CONFIGURATION ]────────────────────────────────────┐${NC}"
if [ -f "$HOME/CZH/Platform-v2/config/platform.conf" ]; then
    echo -e "  ${G}[ OK ] Platform configuration file is intact.${NC}"
else
    echo -e "  ${R}[FAIL] Platform configuration file missing!${NC}"
fi
echo -e "${C}  └────────────────────────────────────────────────────────────┘${NC}\n"

echo -e "${C}  ┌───[ 2. ESSENTIAL MODULES ]────────────────────────────────┐${NC}"
MODULES=("core" "install" "members" "ai" "catalog/tools" "catalog/labs" "catalog/projects")
for mod in "${MODULES[@]}"; do
    if [ -d "$HOME/CZH/Platform-v2/$mod" ]; then
        echo -e "  ${G}[ OK ] Module: \033[97m$mod${NC}"
    else
        echo -e "  ${R}[FAIL] Module missing: \033[97m$mod${NC}"
    fi
done
echo -e "${C}  └────────────────────────────────────────────────────────────┘${NC}\n"

echo -e "${C}  ┌───[ 3. WEAPON SYSTEMS ]───────────────────────────────────┐${NC}"
CMDS=("bash" "python" "git" "curl" "nmap" "proot-distro")
for cmd in "${CMDS[@]}"; do
    if command -v "$cmd" >/dev/null 2>&1; then
        echo -e "  ${G}[ OK ] Command ready: \033[97m$cmd${NC}"
    else
        echo -e "  ${Y}[WARN] Command missing: \033[97m$cmd${NC}"
    fi
done
echo -e "${C}  └────────────────────────────────────────────────────────────┘${NC}\n"

echo -e "${C}  ┌───[ 4. ERROR LOGS ]───────────────────────────────────────┐${NC}"
LOG_FILE="$HOME/CZH/PrivateData/reports/activity.log"
if [ -f "$LOG_FILE" ]; then
    ERRORS=$(grep -c "ERROR" "$LOG_FILE")
    if [ "$ERRORS" -gt 0 ]; then
        echo -e "  ${Y}[WARN] Detected ${W}$ERRORS${Y} historical errors in activity log.${NC}"
    else
        echo -e "  ${G}[ OK ] No errors detected in activity log.${NC}"
    fi
else
    echo -e "  ${D}[INFO] No activity log found yet.${NC}"
fi
echo -e "${C}  └────────────────────────────────────────────────────────────┘${NC}\n"

echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BG_R}${W}  ⚠  SCAN COMPLETE. NO AUTOMATIC REPAIRS MADE.  ⚠               ${NC}"
echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

read -r -p "  Press Enter to return..."
