#!/data/data/com.termux/files/usr/bin/bash

PLATFORM="${CZH_PLATFORM_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
PRIVATE="${CZH_PRIVATE_ROOT:-$PLATFORM/PrivateData}"

R='\033[91m'; G='\033[92m'; Y='\033[93m'; C='\033[96m'; W='\033[97m'; D='\033[90m'
BG_R='\033[41m'; BG_G='\033[42m'; BG_B='\033[44m'; NC='\033[0m'

trap 'printf "\033[0m"' EXIT

pause() {
    printf "\n${Y}  [ ENTER ] ${W}RETURN TO CZH COMMAND DECK${R} "
    read -r _
}

run_command() {
    local cmd="$1"
    local logdir="$HOME/CZH/PrivateData/reports"
    local logfile="$logdir/activity.log"
    local result="OK"
    local rc=0

    mkdir -p "$logdir" || return 1
    chmod 700 "$HOME/CZH/PrivateData" "$logdir" 2>/dev/null
    touch "$logfile"; chmod 600 "$logfile"

    printf "${C}\n  [*] Starting CZH module...${R}\n\n"
    if command -v "$cmd" >/dev/null 2>&1; then "$cmd" || rc=$?; else printf "${R}  [✗] Command not found: %s${R}\n" "$cmd"; rc=127; fi
    if [ $rc -ne 0 ]; then result="ERROR"; fi
    printf '[%s] module=%s result=%s exit_code=%d\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$cmd" "$result" "$rc" >> "$logfile"
    pause
}

banner() {
    clear
    echo -e "${R}"
    echo -e "     ██████╗███████╗██╗  ██╗    ██╗  ██╗██╗   ██╗██████╗ "
    echo -e "    ██╔════╝╚══███╔╝██║  ██║    ██║  ██║██║   ██║██╔══██╗"
    echo -e "    ██║       ███╔╝ ███████║    ███████║██║   ██║██████╔╝"
    echo -e "    ██║      ███╔╝  ██╔══██║    ██╔══██║██║   ██║██╔══██╗"
    echo -e "    ╚██████╗███████╗██║  ██║    ██║  ██║╚██████╔╝██████╔╝"
    echo -e "     ╚═════╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ "
    echo -e "${C}             M I S S I O N   C O N T R O L${NC}\n"

    echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BG_R}${W}  ║  ☠  C Z H   2 . 0   -   M A I N   D A S H B O A R D  ☠           ║${NC}"
    echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
    
    echo -e "${BG_B}${W}  [+] STATUS: ONLINE // CIPHER ZERO HACKERS // SECURE LAB         ${NC}\n"
    
    echo -e "${C}  ┌─────────────────────────────┬─────────────────────────────┐${NC}"
    echo -e "${C}  │${NC} ${Y}[01]${W} Health Check       ${C}│${NC} ${Y}[08]${W} Projects Catalog   ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[02]${W} Cyber Toolkit      ${C}│${NC} ${Y}[09]${W} Diagnostic Report  ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[03]${W} System Monitor     ${C}│${NC} ${Y}[10]${W} Activity & Errors  ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[04]${W} Member Center      ${C}│${NC} ${Y}[11]${W} Smart Error Doctor ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[05]${W} Core Status        ${C}│${NC} ${Y}[12]${W} Admin Center       ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[06]${W} CZH BLACKSITE      ${C}│${NC} ${Y}[13]${W} File Integrity     ${C}│${NC}"
    echo -e "${C}  │${NC} ${Y}[07]${W} Tools Catalog      ${C}│${NC} ${R}[00]${W} ABORT & EXIT       ${C}│${NC}"
    echo -e "${C}  └─────────────────────────────┴─────────────────────────────┘${NC}\n"
    
    echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${D}  ║  [ SESSION MONITORED BY AARHIV HACKERS ]                         ║${NC}"
    echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
    printf " ${G}${B}CZH${R}${C}@TERMUX${R} ${G}➜ ${Y}"
}

while true; do
    banner
    read -r choice
    case "$choice" in
        1) run_command czh-status ;;
        2) run_command czh-tools ;;
        3) run_command czh-monitor ;;
        4) bash "$PLATFORM/members/czh-member-center.sh" ;;
        5) bash "$PLATFORM/core/czh-core.sh"; pause ;;
        6) bash "$PLATFORM/catalog/courses/czh-course.py" ;;
        7) bash "$PLATFORM/core/czh-catalog.sh" "$PLATFORM/catalog/tools" "CZH TOOLS CATALOG" ;;
        8) bash "$PLATFORM/core/czh-catalog.sh" "$PLATFORM/catalog/projects" "CZH PROJECTS CATALOG" ;;
        9) bash "$PLATFORM/core/czh-diagnostic.sh" ;;
        10) bash "$PLATFORM/core/czh-activity.sh" ;;
        11) run_command czh-doctor ;;
        12) bash "$PLATFORM/core/czh-admin-center.sh" ;;
        13) run_command czh-integrity ;;
        0|00)
            printf "\n${G}CZH SESSION CLOSED — STAY ETHICAL. STAY SECURE.${R}\n"
            exit 0
            ;;
        *) printf "${R}Invalid option.${R}\n"; sleep 1 ;;
    esac
done
