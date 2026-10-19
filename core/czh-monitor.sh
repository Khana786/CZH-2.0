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


# --- ADMIN LOCK VERIFICATION ---
clear
echo -e "${R}  ╔══════════════════════════════════════════════╗${NC}"
echo -e "${R}  ║ ${W} ☠  M O N I T O R I N G   R O O M  ☠        ${R}║${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════╝${NC}\n"
echo -e "${Y}  [!] AUTHORIZED PERSONNEL ONLY.${NC}\n"
read -r -s -p "$(echo -e "${R}  ▶ ENTER ADMIN KEY: ${NC}")" input_key
echo ""

if [ "$input_key" != "CZH-DARKWEB-QEP5ES" ]; then
    echo -e "\n${BG_R}${W}  [✗] ACCESS DENIED. SECURITY BREACH LOGGED.  ${NC}"
    sleep 2
    exit 1
fi
echo -e "${G}  [✓] ACCESS GRANTED. LOADING SURVEILLANCE...${NC}"
sleep 1
# ------------------------------

# 7-Second Boot Sequence
for i in {7..1}; do
    clear
    echo -e "${R}  ╔══════════════════════════════════════════════╗${NC}"
    echo -e "${R}  ║ ${W} ☠  C Z H   M O N I T O R I N G   R O O M ${R}║${NC}"
    echo -e "${R}  ╚══════════════════════════════════════════════╝${NC}\n"
    echo -e "${G}  [ SYSTEM INITIALIZING... ]${NC}"
    echo -e "${G}  [ CONNECTING TO SATELLITE... ]${NC}"
    echo -e "${D}  [ CCTV FEEDS LOADING... ]${NC}\n"
    echo -e "${Y}  [+] Establishing secure connection in ${W}$i${Y}...${NC}"
    sleep 1
done
clear

# Fixed CZH MONITOR ASCII Art
echo -e "${G}"
echo -e "   ██████╗███████╗██╗  ██╗    ███╗   ███╗ ██████╗ ███╗   ██╗"
echo -e "  ██╔════╝╚══███╔╝██║  ██║    ████╗ ████║██╔═══██╗████╗  ██║"
echo -e "  ██║       ███╔╝ ███████║    ██╔████╔██║██║   ██║██╔██╗ ██║"
echo -e "  ██║      ███╔╝  ██╔══██║    ██║╚██╔╝██║██║   ██║██║╚██╗██║"
echo -e "  ╚██████╗███████╗██║  ██║    ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║"
echo -e "   ╚═════╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝"
echo -e "${NC}"

echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BG_G}${W}  [+] LIVE TELEMETRY & SURVEILLANCE FEED ACTIVE                 ${NC}"
echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Time Section
echo -e "${C}  ┌───[ S Y S T E M   T I M E ]────────────────────────────────┐${NC}"
echo -e "  ${W}▶ $(date '+%Y-%m-%d %H:%M:%S %Z')${NC}"
echo -e "${C}  └────────────────────────────────────────────────────────────┘${NC}"
echo ""

# Storage Section
echo -e "${C}  ┌───[ S T O R A G E   T E L E M E T R Y ]───────────────────┐${NC}"
df -h "$HOME" | tail -n 1 | awk '{print "  \033[97m▶ Disk: \033[92m"$3" used \033[97m/ "$2" total ("$5")\033[0m"}'
echo -e "${C}  └────────────────────────────────────────────────────────────┘${NC}"
echo ""

# Memory Section
echo -e "${C}  ┌───[ M E M O R Y   C O R E ]───────────────────────────────┐${NC}"
free -h | grep "Mem:" | awk '{print "  \033[97m▶ RAM:  \033[92m"$3" used \033[97m/ "$2" total\033[0m"}'
echo -e "${C}  └────────────────────────────────────────────────────────────┘${NC}"
echo ""

# Module Health Section
echo -e "${C}  ┌───[ M O D U L E   H E A L T H ]───────────────────────────┐${NC}"
MODULES=("core" "config" "install" "members" "ai" "catalog/tools" "catalog/labs" "catalog/projects")
for mod in "${MODULES[@]}"; do
    if [ -d "$HOME/CZH/Platform-v2/$mod" ]; then
        echo -e "  ${G}[✔] SECURE: \033[97m$mod${NC}"
    else
        echo -e "  ${R}[✗] BREACH: \033[97m$mod (MISSING)${NC}"
    fi
done
echo -e "${C}  └────────────────────────────────────────────────────────────┘${NC}"
echo ""

# Weapon Systems Section
echo -e "${C}  ┌───[ W E A P O N   S Y S T E M S ]─────────────────────────┐${NC}"
CMDS=("bash" "python" "git" "curl" "nmap" "proot-distro" "msfconsole")
for cmd in "${CMDS[@]}"; do
    if command -v "$cmd" >/dev/null 2>&1; then
        echo -e "  ${G}[ARMED] \033[97m$cmd${NC}"
    else
        echo -e "  ${Y}[STANDBY] \033[97m$cmd (Not Installed)${NC}"
    fi
done
echo -e "${C}  └────────────────────────────────────────────────────────────┘${NC}"
echo ""

echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BG_R}${W}  ⚠  WARNING: ALL ACTIONS ARE LOGGED BY AARHIV HACKERS  ⚠       ${NC}"
echo -e "${R}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

read -r -p "  Press Enter to return..."
