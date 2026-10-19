#!/bin/bash
# EMBEDDED LOCAL EDITION FOR CZH PRIVILEGED LAB
RED='\033[1;91m'
GREEN='\033[1;92m'
CYAN='\033[1;96m'
YELLOW='\033[1;93m'
RESET='\033[0m'

clear
echo -e "${RED}╔════════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${RED}║           ⚔️ CZH INTEGRATED TUNNEL ENGINE - ZPHISHER ⚔️           ║${RESET}"
echo -e "${RED}╚════════════════════════════════════════════════════════════════╝${RESET}"
echo -e "\n${CYAN}[ SELECT TARGET PORTAL FOR SIMULATION ]${RESET}\n"
echo -e " ${GREEN}[01]${RESET} Google Portal Template"
echo -e " ${GREEN}[02]${RESET} Facebook Portal Template"
echo -e " ${GREEN}[03]${RESET} Yahoo Security Portal"
echo -e " ${GREEN}[04]${RESET} Terminate Module Interface"
echo ""
echo -e -n "${CYAN}[czh-zphisher@offline]:~# ${RESET}"
read option

case $option in
    3)
        echo -e "\n${GREEN}[*] Synchronizing with local CZH Yahoo Lab assets...${RESET}"
        if [ -d "$HOME/CZH/PrivateData/yahoo_lab" ]; then
            cd "$HOME/CZH/PrivateData/yahoo_lab" || exit 1
            echo -e "${YELLOW}[!] Launching local HTTP Daemon on Port 8080...${RESET}"
            php -S 127.0.0.1:8080
        else
            echo -e "${RED}[×] Path Error: CZH/PrivateData/yahoo_lab node missing.${RESET}"
        fi
        ;;
    4) exit 0 ;;
    *) echo -e "${RED}[!] Option requires network access. Please select [03] for Offline Yahoo Lab.${RESET}"; sleep 2 ;;
esac
