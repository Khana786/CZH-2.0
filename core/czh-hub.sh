#!/data/data/com.termux/files/usr/bin/bash

export TERM="${TERM:-xterm-256color}"
R='\033[0m'
B='\033[1m'
G='\033[38;5;46m'
C='\033[38;5;51m'
P='\033[38;5;201m'
Y='\033[38;5;226m'
X='\033[38;5;196m'
W='\033[38;5;255m'
D='\033[38;5;244m'

# Resolve paths from this CZH installation; allow explicit overrides.
PLATFORM="${CZH_PLATFORM_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
PRIVATE="${CZH_PRIVATE_ROOT:-$PLATFORM/PrivateData}"

trap 'printf "\033[0m"' EXIT

bar() {
    printf "${G}------------------------------------------${R}\n"
}

pause() {
    printf "\n${Y}  [ ENTER ] ${W}RETURN TO CZH COMMAND DECK${R} "
    read -r _
}

banner() {
    clear
    local cols
    cols=$(tput cols 2>/dev/null || echo 40)
    [[ "$cols" =~ ^[0-9]+$ ]] || cols=40
    (( cols < 32 )) && cols=32
    (( cols > 64 )) && cols=64

    local inner=$((cols - 2))
    local edge
    edge=$(printf '%*s' "$inner" '' | tr ' ' '-')

    center() {
        local text="$1"
        local len=${#text}
        local left=$(( (inner - len) / 2 ))
        (( left < 0 )) && left=0
        printf "%*s%b%s%b\n" "$left" '' "$C" "$text" "$R"
    }

    printf "\n${G}+%s+${R}\n" "$edge"
    center "C Z H"
    center "2.0  |  MISSION CONTROL"
    printf "${G}+%s+${R}\n" "$edge"
    center "CIPHER ZERO HACKERS"
    center "AARHIV HACKERS"
    center "WHITE HAT CYBER LAB"
    printf "${G}+%s+${R}\n\n" "$edge"

    printf " ${G}●${R} ${W}READY${R} ${C}◆${R} ${W}LOCAL${R} ${P}◆${R} ${W}SECURE LAB${R}\n"
    printf " ${D}LEARN${G} • ${D}SECURE${C} • ${D}DEFEND${R}\n"
    printf "${G}%s${R}\n" "$edge"
    printf " ${P}${B}| CZH MISSION CONTROL${R}\n"
    printf "${D} +%s+${R}\n" "$edge"
    printf "  ${G}[01]${R} ${W}Platform Health Check${R}\n"
    printf "  ${C}[02]${R} ${W}Ethical Cyber Toolkit${R}\n"
    printf "  ${X}[03]${R} ${W}System Monitor${R}\n"
    printf "  ${Y}[04]${R} ${W}Member Center${R}\n"
    printf "  ${G}[05]${R} ${W}Core Platform Status${R}\n"
    printf "  ${C}[06]${R} ${W}Learning Labs${R}\n"
    printf "  ${P}[07]${R} ${W}Tools Catalog${R}\n"
    printf "  ${Y}[08]${R} ${W}Projects Catalog${R}\n"
    printf "  ${X}[09]${R} ${W}Safe Diagnostic Report${R}\n"
    printf "  ${C}[10]${R} ${W}Activity & Error Center${R}\n"
    printf "  ${G}[11]${R} ${W}CZH Smart Error Doctor${R}\n"
    printf "  ${P}[12]${R} ${W}CZH Admin Center${R}\n"
    printf "  ${G}[13]${R} ${W}File Integrity Checker${R}\n"
    printf "${D} +%s+${R}\n" "$edge"
    printf "  ${X}[00]${R} ${W}Exit CZH${R}\n"
    printf "${G}%s${R}\n" "$edge"
    printf " ${G}${B}CZH${R}${C}@TERMUX${R} ${G}➜ ${Y}"
}
run_command() {
    local cmd="$1"
    local logdir="$HOME/CZH/PrivateData/reports"
    local logfile="$logdir/activity.log"
    local result="OK"
    local rc=0

    mkdir -p "$logdir" || {
        printf "${X}Cannot create private activity log.${R}\n"
        pause
        return 1
    }
    chmod 700 "$HOME/CZH/PrivateData" "$logdir" 2>/dev/null
    touch "$logfile"
    chmod 600 "$logfile"

    printf "${C}\n  [*] Starting CZH module...${R}\n\n"

    if command -v "$cmd" >/dev/null 2>&1; then
        "$cmd"
        rc=$?
        if [ "$rc" -ne 0 ]; then
            result="ERROR"
        fi
    else
        printf "${X}  [!] Module not found: %s${R}\n" "$cmd"
        result="MISSING"
        rc=127
    fi

    printf '%s module=%s result=%s exit_code=%s\n' \
        "$(date '+%Y-%m-%d %H:%M:%S %z')" "$cmd" "$result" "$rc" \
        >> "$logfile"

    printf "\n${D}Local activity log: %s${R}\n" "$logfile"
    printf "${D}Only module name and result are recorded; nothing is uploaded.${R}\n"
    pause
}

show_activity_logs() {
    local logfile="$HOME/CZH/PrivateData/reports/activity.log"

    clear
    printf '\033[38;5;51m'
    printf '%s\n' '=================================================='
    printf '%s\n' '          CZH ACTIVITY & ERROR CENTER'
    printf '%s\n' '             CIPHER ZERO HACKERS'
    printf '%s\n' '=================================================='
    printf '\033[0m'

    if [ ! -f "$logfile" ]; then
        printf '\033[38;5;226mNo activity log found yet.\033[0m\n'
        printf 'Run a module from CZH Hub first.\n'
    else
        printf '\033[38;5;46mRecent activity and module results:\033[0m\n\n'
        tail -n 30 "$logfile"
        printf '\n'
        if grep -q 'result=ERROR\|result=MISSING' "$logfile"; then
            printf '\033[38;5;196mAn error or missing module was recorded above.\033[0m\n'
        else
            printf '\033[38;5;46mNo recorded module errors in this log.\033[0m\n'
        fi
    fi

    printf '\n\033[38;5;244mPrivacy: this log is local to this device; it is not uploaded.\033[0m\n'
    printf '\033[38;5;226mPress ENTER to return to CZH Hub... \033[0m'
    read -r _
}

show_labs() {
    local RELEASE_ROOT LAB_RUNNER LAB_README choice
    RELEASE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    LAB_RUNNER="$RELEASE_ROOT/catalog/labs/czh-labs.py"
    LAB_README="$RELEASE_ROOT/catalog/labs/README.md"

    printf "\n${C}=== CZH LEARNING LABS ===${R}\n"

    if [ -f "$LAB_README" ]; then
        cat "$LAB_README"
    else
        printf "${Y}Learning lab guide not found.${R}\n"
    fi

    if [ -f "$LAB_RUNNER" ]; then
        printf "\n${G}[READY] Practical lab runner found.${R}\n"
        printf "Run practical labs now? [y/N]: "
        read -r choice
        case "$choice" in
            y|Y|yes|YES) python "$LAB_RUNNER" ;;
            *) printf "Returning to CZH Mission Control.\n" ;;
        esac
    else
        printf "\n${Y}Practical lab runner is not installed in this release yet.${R}\n"
    fi

    pause
}
show_catalog() {
    printf "\n${C}=== %s ===${R}\n" "$2"
    if [ -d "$1" ]; then
        if [ -f "$1/README.md" ]; then
            printf "\n${W}--- CATALOG CONTENT ---${R}\n"
            cat "$1/README.md"
            printf "\n"
        else
            printf "${Y}No README.md found in this catalog.${R}\n"
        fi

        printf "\n${W}--- CATALOG FILES ---${R}\n"
        find "$1" -maxdepth 2 -type f ! -name README.md -print | sort
    else
        printf "${Y}Catalog directory not found.${R}\n"
    fi
    pause
}

diagnostic_report() {
    local dir="$PRIVATE/reports"
    local report="$dir/diagnostic-$(date +%Y%m%d-%H%M%S).txt"

    if ! mkdir -p "$dir"; then
        printf "${X}Cannot create report directory.${R}\n"
        pause
        return
    fi
    chmod 700 "$PRIVATE" "$dir" 2>/dev/null

    {
        echo "CZH SAFE LOCAL DIAGNOSTIC REPORT"
        date
        echo
        echo "=== PLATFORM CONFIG ==="
        if [ -f "$PLATFORM/config/platform.conf" ]; then
            grep -E '^(CZH_PLATFORM_NAME|CZH_PLATFORM_VERSION|CZH_COMMUNITY_NAME|CZH_ORGANIZATION|CZH_AI_MODE|CZH_BACKEND_CONFIGURED)=' "$PLATFORM/config/platform.conf"
        else
            echo "Platform config missing."
        fi
        echo
        echo "=== COMMANDS ==="
        for c in bash python git curl czh-status czh-monitor czh-join czh-tools czh-lab-setup; do
            command -v "$c" 2>/dev/null || echo "MISSING: $c"
        done
        echo
        echo "=== STORAGE ==="
        df -h "$HOME" 2>&1
        echo
        echo "This report remains local; it is not uploaded."
    } > "$report" 2>&1

    chmod 600 "$report"
    printf "\n${G}[OK] Diagnostic report saved:${R}\n%s\n" "$report"
    printf "${D}Private local report. Not uploaded.${R}\n"
    pause
}

while true; do
    banner
    read -r choice
    case "$choice" in
        1) run_command czh-lab-setup ;;
        2) run_command czh-tools ;;
        3) run_command czh-monitor ;;
        4) run_command czh-join ;;
        5)
            bash "$PLATFORM/core/czh-core.sh" status
            pause
            ;;
        6) show_labs ;;
        7) show_catalog "$PLATFORM/catalog/tools" "CZH TOOLS CATALOG" ;;
        8) show_catalog "$PLATFORM/catalog/projects" "CZH PROJECTS CATALOG" ;;
        9) diagnostic_report ;;
        10) show_activity_logs ;;
        11) run_command czh-doctor ;;
        12) run_command czh-admin ;;
        13) run_command czh-integrity ;;
        0|00)
            printf "\n${G}CZH SESSION CLOSED — STAY ETHICAL. STAY SECURE.${R}\n"
            exit 0
            ;;
        *)
            printf "\n${X}[!] Invalid selection. Choose 0–13.${R}\n"
            sleep 1
            ;;
    esac
done
