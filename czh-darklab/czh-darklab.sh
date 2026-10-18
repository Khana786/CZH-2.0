#!/data/data/com.termux/files/usr/bin/bash

KEY_FILE="$HOME/CZH/PrivateData/darkweb.key"
clear

R='\033[91m'
G='\033[92m'
Y='\033[93m'
C='\033[96m'
W='\033[97m'
D='\033[90m'
BG_R='\033[41m'
NC='\033[0m'

if [ ! -f "$KEY_FILE" ]; then
    echo -e "${R}[-] CRITICAL ERROR: MASTER KEY NOT FOUND.${NC}"
    exit 1
fi

# --- 5 SECOND INTENSE WARNING SEQUENCE ---
for i in {1..5}; do
    clear
    echo -e "${BG_R}${W}  ⚠  C R I T I C A L   W A R N I N G  ⚠  ${NC}"
    echo -e "${R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "${R}             ▄▄████████████████▄▄             ${NC}"
    echo -e "${R}          ▄████████████████████████▄          ${NC}"
    echo -e "${R}         ████████████████████████████         ${NC}"
    echo -e "${W}         █████  ${R}████████${W}    ${R}████████${W}  █████         ${NC}"
    echo -e "${W}         █████  ${R}████████${W}    ${R}████████${W}  █████         ${NC}"
    echo -e "${R}          ██████▄▄██████▄▄██████████          ${NC}"
    echo -e "${R}           ████████  ██  ██████████           ${NC}"
    echo -e "${R}            ▀▀████████████████▀▀             ${NC}"
    echo ""
    echo -e "${Y}      [!] UNAUTHORIZED ACCESS DETECTED        ${NC}"
    echo -e "${Y}      [!] SYSTEM IS MONITORING THIS DEVICE    ${NC}"
    echo -e "${Y}      [!] SECURITY PROTOCOLS ACTIVATED        ${NC}"
    echo ""
    echo -e "${R}          LOADING SECURE VAULT IN ${W}$((6-i))${R}...          ${NC}"
    echo -e "${R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    sleep 1
done
# ----------------------------------------

clear
# Big Danger Text
echo -e "${R}"
echo -e "  ██████╗  █████╗ ███╗   ██╗ ██████╗ ███████╗██████╗ "
echo -e "  ██╔══██╗██╔══██╗████╗  ██║██╔════╝ ██╔════╝██╔══██╗"
echo -e "  ██║  ██║███████║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝"
echo -e "  ██║  ██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗"
echo -e "  ██████╔╝██║  ██║██║ ╚████║╚██████╔╝███████╗██║  ██║"
echo -e "  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝"
echo -e "${NC}"

# Warnings Section
echo -e "${Y}"
echo -e "  ⚠ WARNING: YOU ARE ENTERING THE CZH DARK LAB."
echo -e "  ⚠ THIS SYSTEM IS HIGHLY RESTRICTED AND DANGEROUS."
echo -e "  ⚠ ALL ACTIVITIES ARE BEING MONITORED AND RECORDED."
echo -e "  ⚠ UNAUTHORIZED ACCESS IS A CRIMINAL OFFENSE."
echo -e "  ⚠ YOU ARE NOT SAFE. TURN BACK NOW IF NOT AUTHORIZED.${NC}"

echo -e "${R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# Hifi Popup Box
echo -e "${R}  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓${NC}"
echo -e "${BG_R}${W}  ┃       ☠  C Z H   D A R K   L A B   L O C K E D  ☠       ┃${NC}"
echo -e "${R}  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫${NC}"
echo -e "${R}  ┃${NC} ${Y}⚠ DANGER ZONE // UNAUTHORIZED ACCESS PROHIBITED           ${NC} ${R}┃${NC}"
echo -e "${R}  ┃${NC} ${C}⚡ SYSTEM COMPROMISED - FIREWALL ACTIVE                 ${NC} ${R}┃${NC}"
echo -e "${R}  ┃${NC} ${G}✔ AUTHORIZATION REQUIRED TO PROCEED                     ${NC} ${R}┃${NC}"
echo -e "${R}  ┃${NC} ${R}✗ YOU ARE IN A HIGH RISK ENVIRONMENT. STAY ALERT.         ${NC} ${R}┃${NC}"
echo -e "${R}  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${NC}"
echo ""

read -r -s -p "$(echo -e "${R}  ▶ ENTER DARK LAB AUTHORIZATION KEY: ${NC}")" input_key
echo ""

MASTER_KEY=$(cat "$KEY_FILE")

if [[ "$input_key" != "$MASTER_KEY" ]]; then
    echo ""
    echo -e "${BG_R}${W}  [✗] ACCESS DENIED. SELF-DESTRUCT INITIATED...  ${NC}"
    sleep 1
    echo -e "${R}  [✗] AUTHORIZATION FAILURE. CONTACT AARHIV HACKERS.${NC}"
    exit 1
fi

echo ""
echo -e "${G}  [✓] ACCESS GRANTED. WELCOME TO THE CZH DARK LAB.${NC}"
sleep 1
clear

while true; do
    echo -e "${R}┌──────────────────────────────────────────────────────────┐${NC}"
    echo -e "${R}│${NC} ${C}   ☠ CZH DARK LAB // GREY HAT OPERATIONS  ☠${NC}             ${R}│${NC}"
    echo -e "${R}├──────────────────────────────────────────────────────────┤${NC}"
    echo -e "${R}│${NC} ${Y}[1]${W} INSTALL WEAPONS (nmap, sqlmap, hydra)${NC}                ${R}│${NC}"
    echo -e "${R}│${NC} ${Y}[2]${W} LAUNCH BLACK-SHELL (Testing Environment)${NC}             ${R}│${NC}"
    echo -e "${R}│${NC} ${Y}[3]${W} SYSTEM INFO (Check Permissions & Tools)${NC}              ${R}│${NC}"
    echo -e "${R}│${NC} ${R}[0]${W} ABORT & EXIT LAB${NC}                                     ${R}│${NC}"
    echo -e "${R}└──────────────────────────────────────────────────────────┘${NC}"
    echo ""
    read -r -p "$(echo -e "${C}  DARK LAB ➜ ${NC}")" choice

    case "$choice" in
        1) echo -e "${Y}\n  [*] ARMING WEAPONS...${NC}"; pkg install nmap sqlmap hydra -y; echo -e "${G}  [✓] WEAPONS READY.${NC}" ;;
        2) echo -e "${R}\n  [!] INITIATING BLACK-SHELL...${NC}"; bash ;;
        3) 
            echo -e "${C}\n  [+] SYSTEM DIAGNOSTICS:${NC}"
            command -v nmap >/dev/null && echo -e "${G}      [OK] nmap${NC}" || echo -e "${R}      [X] nmap missing${NC}"
            command -v sqlmap >/dev/null && echo -e "${G}      [OK] sqlmap${NC}" || echo -e "${R}      [X] sqlmap missing${NC}"
            ;;
        0) echo -e "${R}\n  [!] DISCONNECTING. STAY ETHICAL.${NC}"; exit 0 ;;
        *) echo -e "${R}  [✗] Invalid option.${NC}" ;;
    esac
    echo ""
    read -r -p "$(echo -e "${D}  Press Enter...${NC}")"
    clear
done
