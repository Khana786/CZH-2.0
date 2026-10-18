#!/data/data/com.termux/files/usr/bin/bash

KEY_FILE="$HOME/CZH/PrivateData/darkweb.key"
DARKLAB_LOG="$HOME/CZH/PrivateData/darklab_activity.log"
touch "$DARKLAB_LOG"
chmod 600 "$DARKLAB_LOG"

log_action() {
    printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$1" >> "$DARKLAB_LOG"
}

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
GUEST_FILE="$HOME/CZH/PrivateData/darklab_guests.txt"
CURRENT_TIME=$(date +%s)
ACCESS_GRANTED=0

# 1. Check Master Key (Owner)
if [[ "$input_key" == "$MASTER_KEY" ]]; then
    ACCESS_GRANTED=1
else
    # 2. Check Guest Keys (If file exists)
    if [ -f "$GUEST_FILE" ]; then
        while IFS=":" read -r g_token g_expiry; do
            if [[ "$input_key" == "$g_token" ]]; then
                if [ "$CURRENT_TIME" -lt "$g_expiry" ]; then
                    ACCESS_GRANTED=2
                    TIME_LEFT=$((g_expiry - CURRENT_TIME))
                    echo -e "${G}  [i] Guest Access Valid. Time remaining: ${TIME_LEFT}s${NC}"
                else
                    echo -e "${R}  [✗] This guest token has EXPIRED.${NC}"
                fi
            fi
        done < "$GUEST_FILE"
    fi
fi

USER_ROLE="GUEST"
if [ "$ACCESS_GRANTED" -eq 1 ]; then USER_ROLE="ADMIN"; fi

if [ "$ACCESS_GRANTED" -eq 0 ]; then
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

log_action "Guest accessed the Dark Lab Menu."

while true; do
    echo -e "${R}┌──────────────────────────────────────────────────────────┐${NC}"
    echo -e "${R}│${NC} ${C}   ☠ CZH DARK LAB // GREY HAT OPERATIONS  ☠${NC}             ${R}│${NC}"
    echo -e "${R}├──────────────────────────────────────────────────────────┤${NC}"
    echo -e "${R}│${NC} ${Y}[1]${W} INSTALL WEAPONS (nmap, sqlmap, hydra)${NC}                ${R}│${NC}"
    echo -e "${R}│${NC} ${Y}[2]${W} LAUNCH BLACK-SHELL (Testing Environment)${NC}             ${R}│${NC}"
    echo -e "${R}│${NC} ${Y}[3]${W} SYSTEM INFO (Check Permissions & Tools)${NC}              ${R}│${NC}"
    echo -e "${R}│${NC} ${R}[5]${W} TESTING ARSENAL (Ethical Tools)${NC}                     ${R}│${NC}"
    echo -e "${R}│${NC} ${C}[6]${W} OSINT RECON (Public Info Only)${NC}                      ${R}│${NC}"
    if [ "$USER_ROLE" == "ADMIN" ]; then
    echo -e "${R}│${NC} ${C}[4]${W} VIEW ACTIVITY LOGS (Admin Only)${NC}                      ${R}│${NC}"
fi
    echo -e "${R}│${NC} ${R}[0]${W} ABORT & EXIT LAB${NC}                                     ${R}│${NC}"
    echo -e "${R}└──────────────────────────────────────────────────────────┘${NC}"
    echo ""
    read -r -p "$(echo -e "${C}  DARK LAB ➜ ${NC}")" choice

    case "$choice" in
        1) echo -e "${Y}\n  [*] ARMING WEAPONS...${NC}"; log_action "Started installing Weapons (nmap, sqlmap, hydra)"; pkg install nmap -y; echo -e "${G}  [✓] WEAPONS READY.${NC}" ;;
        2) echo -e "${R}\n  [!] INITIATING BLACK-SHELL...${NC}"; log_action "Launched Black-Shell Environment"; bash ;;
        4)
            if [ "$USER_ROLE" == "ADMIN" ]; then
                echo -e "${C}\n  [+] ACTIVITY LOGS:${NC}"
                if [ -s "$DARKLAB_LOG" ]; then cat "$DARKLAB_LOG"; else echo "No logs yet."; fi
            else
                echo -e "${R}  [✗] Access Denied. Admin only.${NC}"
            fi
            ;;
        5)
            echo -e "${C}\n  [+] CZH ETHICAL TESTING ARSENAL${NC}"
            echo -e "${Y}  Tools available: whois, dig, curl, wget, msfconsole${NC}"
            echo -e "${Y}  Use only on authorized targets.${NC}"
            read -r -p "  Enter tool name (or 'exit' to return): " tool_cmd
            if [[ "$tool_cmd" == "exit" ]]; then
                : # do nothing, return to menu
            elif [[ "$tool_cmd" =~ ^(whois|dig|curl|wget|msfconsole)$ ]]; then
                log_action "Used testing tool: $tool_cmd"
                echo ""
                if [ "$tool_cmd" == "msfconsole" ]; then
                    log_action "Launched Metasploit Console (via Debian)"
                    echo -e "${G}  [*] Booting Metasploit inside Debian...${NC}"
                    proot-distro login debian -- msfconsole
                    continue
                fi
                read -r -p "  Enter target (e.g., example.com): " target
                if [ -n "$target" ]; then
                    log_action "Target: $target"
                    $tool_cmd "$target"
                fi
            else
                echo -e "${R}  [✗] Tool not allowed or invalid.${NC}"
            fi
            ;;
        3) 
            echo -e "${C}\n  [+] SYSTEM DIAGNOSTICS:${NC}"
            command -v nmap >/dev/null && echo -e "${G}      [OK] nmap${NC}" || echo -e "${R}      [X] nmap missing${NC}"
            command -v sqlmap >/dev/null && echo -e "${G}      [OK] sqlmap${NC}" || echo -e "${R}      [X] sqlmap missing${NC}"
            ;;
        6)
            echo -e "${C}\n  [+] OSINT RECONNAISSANCE TOOLS${NC}"
            echo -e "${Y}  [1] Domain WHOIS${NC}"
            echo -e "${Y}  [2] DNS Lookup${NC}"
            echo -e "${Y}  [3] Email Breach Check (HIBP)${NC}"
            echo -e "${Y}  [4] IP Location Lookup${NC}"
            echo -e "${Y}  [5] Username Search (Sherlock)${NC}"
            echo -e "${Y}  [0] Back${NC}"
            read -r -p "  Select ➜ " osint_choice

            case "$osint_choice" in
                1)
                    log_action "OSINT: WHOIS Lookup"
                    read -r -p "  Enter domain: " target
                    whois "$target" | head -n 20
                    ;;
                2)
                    log_action "OSINT: DNS Lookup"
                    read -r -p "  Enter domain: " target
                    echo -e "\n  A Record: $(dig +short A "$target")"
                    echo -e "  MX Record: $(dig +short MX "$target")"
                    echo -e "  NS Record: $(dig +short NS "$target")"
                    ;;
                3)
                    log_action "OSINT: HIBP Email Check"
                    echo -e "${Y}\n  Note: HIBP check requires API key. Placeholder for now.${NC}"
                    ;;
                4)
                    log_action "OSINT: IP Lookup"
                    read -r -p "  Enter IP: " ip_target
                    curl -s "http://ip-api.com/json/$ip_target" | python3 -m json.tool 2>/dev/null | head -n 15
                    ;;
                5)
                    log_action "OSINT: Username Search"
                    echo -e "${Y}\n  Username search requires 'sherlock' tool.${NC}"
                    echo -e "${Y}  Install with: pip install sherlock-project${NC}"
                    ;;
                0) ;;
                *) echo -e "${R}  [✗] Invalid option.${NC}" ;;
            esac
            ;;
        0) echo -e "${R}\n  [!] DISCONNECTING. STAY ETHICAL.${NC}"; exit 0 ;;
        *) echo -e "${R}  [✗] Invalid option.${NC}" ;;
    esac
    echo ""
    read -r -p "$(echo -e "${D}  Press Enter...${NC}")"
    clear
done
