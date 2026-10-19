#!/data/data/com.termux/files/usr/bin/bash
source "$HOME/CZH/Platform-v2/config/theme.conf" 2>/dev/null
R="${COLOR_MAIN:-\033[91m}"
W="${COLOR_TEXT:-\033[97m}"
C="${COLOR_ACCENT:-\033[96m}"
BG_R="${BG_MAIN:-\033[41m}"

KEY_FILE="$HOME/CZH/PrivateData/darkweb.key"
clear

G='\033[92m'
Y='\033[93m'
D='\033[90m'
NC='\033[0m'

if [ ! -f "$KEY_FILE" ]; then
    echo -e "${R}[-] CRITICAL ERROR: MASTER KEY NOT FOUND.${NC}"
    exit 1
fi

# 5 Second Danger Entry
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

clear
echo -e "${R}"
echo -e "  ██████╗  █████╗ ███╗   ██╗ ██████╗ ███████╗██████╗ "
echo -e "  ██╔══██╗██╔══██╗████╗  ██║██╔════╝ ██╔════╝██╔══██╗"
echo -e "  ██║  ██║███████║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝"
echo -e "  ██║  ██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗"
echo -e "  ██████╔╝██║  ██║██║ ╚████║╚██████╔╝███████╗██║  ██║"
echo -e "  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝"
echo -e "${NC}"

echo -e "${Y}  ⚠ WARNING: YOU ARE ENTERING THE CZH DARK LAB."
echo -e "  ⚠ THIS SYSTEM IS HIGHLY RESTRICTED AND DANGEROUS."
echo -e "  ⚠ ALL ACTIVITIES ARE BEING MONITORED AND RECORDED.${NC}"
echo ""
echo -e "${R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo -e "${R}  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓${NC}"
echo -e "${BG_R}${W}  ┃       ☠  C Z H   D A R K   L A B   L O C K E D  ☠       ┃${NC}"
echo -e "${R}  ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫${NC}"
echo -e "${R}  ┃${NC} ${Y}⚠ DANGER ZONE // UNAUTHORIZED ACCESS PROHIBITED           ${NC} ${R}┃${NC}"
echo -e "${R}  ┃${NC} ${C}⚡ SYSTEM COMPROMISED - FIREWALL ACTIVE                 ${NC} ${R}┃${NC}"
echo -e "${R}  ┃${NC} ${G}✔ AUTHORIZATION REQUIRED TO PROCEED                     ${NC} ${R}┃${NC}"
echo -e "${R}  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${NC}"
echo ""

read -r -s -p "$(echo -e "${R}  ▶ ENTER DARK LAB AUTHORIZATION KEY: ${NC}")" input_key
echo ""

MASTER_KEY=$(cat "$KEY_FILE")
GUEST_FILE="$HOME/CZH/PrivateData/darklab_guests.txt"
CURRENT_TIME=$(date +%s)
ACCESS_GRANTED=0

if [[ "$input_key" == "$MASTER_KEY" ]]; then
    ACCESS_GRANTED=1
else
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

if [ "$ACCESS_GRANTED" -eq 0 ]; then
    echo ""
    echo -e "${BG_R}${W}  [✗] ACCESS DENIED. SELF-DESTRUCT INITIATED...  ${NC}"
    sleep 1
    exit 1
fi

echo ""
echo -e "${G}  [✓] ACCESS GRANTED. WELCOME TO THE CZH DARK LAB.${NC}"
sleep 1
clear

DARKLAB_LOG="$HOME/CZH/PrivateData/darklab_activity.log"
touch "$DARKLAB_LOG"
chmod 600 "$DARKLAB_LOG"
log_action() { printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$1" >> "$DARKLAB_LOG"; }

USER_ROLE="GUEST"
if [ "$ACCESS_GRANTED" -eq 1 ]; then USER_ROLE="ADMIN"; fi

while true; do
    echo -e "${R}┌──────────────────────────────────────────────────────────┐${NC}"
    echo -e "${R}│${NC} ${C}   ☠ CZH DARK LAB // GREY HAT OPERATIONS  ☠${NC}             ${R}│${NC}"
    echo -e "${R}├──────────────────────────────────────────────────────────┤${NC}"
    echo -e "${R}│${NC} ${Y}[1]${W} INSTALL WEAPONS (nmap, sqlmap, hydra)${NC}                ${R}│${NC}"
    echo -e "${R}│${NC} ${Y}[2]${W} LAUNCH BLACK-SHELL (Testing Environment)${NC}             ${R}│${NC}"
    echo -e "${R}│${NC} ${Y}[3]${W} SYSTEM INFO (Check Permissions & Tools)${NC}              ${R}│${NC}"
    echo -e "${R}│${NC} ${R}[5]${W} TESTING ARSENAL (Ethical Tools)${NC}                     ${R}│${NC}"
    echo -e "${R}│${NC} ${Y}[6]${W} OSINT RECON (Public Info Only)${NC}                      ${R}│${NC}"
    if [ "$USER_ROLE" == "ADMIN" ]; then
        echo -e "${R}│${NC} ${C}[4]${W} VIEW ACTIVITY LOGS (Admin Only)${NC}                      ${R}│${NC}"
    fi
    echo -e "${R}│${NC} ${R}[0]${W} ABORT & EXIT LAB${NC}                                     ${R}│${NC}"
    echo -e "${R}└──────────────────────────────────────────────────────────┘${NC}"
    echo ""
    read -r -p "$(echo -e "${C}  DARK LAB ➜ ${NC}")" choice

    case "$choice" in
        1)
            echo -e "${Y}\n  [*] ARMING WEAPONS...${NC}"
            log_action "Started installing Weapons"
            pkg install nmap -y
            echo -e "${G}  [✓] WEAPONS READY.${NC}"
            ;;
        2)
            echo -e "${R}\n  [!] INITIATING BLACK-SHELL...${NC}"
            log_action "Launched Black-Shell"
            bash
            ;;
        3)
            echo -e "${C}\n  [+] SYSTEM DIAGNOSTICS:${NC}"
            command -v nmap >/dev/null && echo -e "${G}      [OK] nmap${NC}" || echo -e "${R}      [X] nmap missing${NC}"
            command -v proot-distro >/dev/null && echo -e "${G}      [OK] proot-distro${NC}" || echo -e "${R}      [X] proot-distro missing${NC}"
            ;;
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
            echo -e "${Y}  Tools available: whois, dig, curl, wget, nikto, whatweb, spiderfoot, msfconsole${NC}"
            echo -e "${Y}  Use only on authorized targets.${NC}"
            read -r -p "  Enter tool name (or 'exit' to return): " tool_cmd
            
            if [[ "$tool_cmd" == "exit" ]]; then
                :
            elif [[ "$tool_cmd" == "msfconsole" ]]; then
                log_action "Launched Metasploit"
                echo -e "${G}  [*] Booting Metasploit inside Debian...${NC}"
                proot-distro login debian -- msfconsole
            elif [[ "$tool_cmd" == "nikto" ]]; then
                read -r -p "  Enter target URL/IP for Nikto (e.g., example.com): " target
                if [ -n "$target" ]; then
                    log_action "Used Nikto on: $target"
                    echo -e "${C}  [*] Starting Nikto Web Vulnerability Scan...${NC}"
                    proot-distro login debian -- nikto -h "$target"
                fi
            elif [[ "$tool_cmd" == "whatweb" ]]; then
                read -r -p "  Enter target URL/IP for WhatWeb (e.g., example.com): " target
                if [ -n "$target" ]; then
                    log_action "Used WhatWeb on: $target"
                    echo -e "${C}  [*] Starting WhatWeb Scanner...${NC}"
                    proot-distro login debian -- whatweb "$target"
                fi
            elif [[ "$tool_cmd" == "spiderfoot" ]]; then
                read -r -p "  Enter target Domain/IP for SpiderFoot: " target
                if [ -n "$target" ]; then
                    log_action "Used SpiderFoot on: $target"
                    echo -e "${C}  [*] Starting SpiderFoot OSINT Scan...${NC}"
                    proot-distro login debian -- bash -c "cd /root/spiderfoot && python3 sf.py -s $target -q"
                fi
            elif [[ "$tool_cmd" =~ ^(whois|dig|curl|wget)$ ]]; then
                read -r -p "  Enter target (e.g., example.com): " target
                if [ -n "$target" ]; then
                    log_action "Used tool: $tool_cmd on $target"
                    $tool_cmd "$target"
                fi
            else
                echo -e "${R}  [✗] Tool not allowed or invalid.${NC}"
            fi
            ;;
        6)
            echo -e "${C}\n  [+] OSINT RECONNAISSANCE TOOLS${NC}"
            echo -e "${Y}  [1] Domain WHOIS${NC}"
            echo -e "${Y}  [2] DNS Lookup${NC}"
            echo -e "${Y}  [3] IP Location Lookup${NC}"
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
                    log_action "OSINT: IP Lookup"
                    read -r -p "  Enter IP: " ip_target
                    curl -s "http://ip-api.com/json/$ip_target" | python3 -m json.tool 2>/dev/null | head -n 15
                    ;;
            esac
            ;;
        0)
            echo -e "${R}\n  [!] DISCONNECTING FROM DARK LAB. STAY ETHICAL.${NC}"
            log_action "Exited Dark Lab"
            exit 0
            ;;
        *)
            echo -e "${R}  [✗] Invalid option.${NC}"
            ;;
    esac
    echo ""
    read -r -p "$(echo -e "${D}  Press Enter to continue...${NC}")"
    clear
done
