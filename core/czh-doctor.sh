#!/data/data/com.termux/files/usr/bin/bash

set -u

G='\033[1;32m'
C='\033[1;36m'
Y='\033[1;33m'
R='\033[1;31m'
W='\033[1;37m'
D='\033[0m'

ROOT="$HOME/CZH/Platform-v2"
CONF="$ROOT/config/platform.conf"
LOG="$HOME/CZH/PrivateData/reports/activity.log"

printf "\n%b" "$G"
printf '%s\n' '================================================'
printf '%s\n' '              CZH SMART ERROR DOCTOR'
printf '%s\n' '================================================'
printf '%b\n' "$D"
printf '%b\n' "${C}CIPHER ZERO HACKERS | WHITE HAT CYBER LAB${D}"
printf '%s\n\n' 'Mode: READ-ONLY — no automatic repairs'

issues=0

check_dir() {
    if [ -d "$ROOT/$1" ]; then
        printf '%b\n' "${G}[OK]${D} Directory: $1"
    else
        printf '%b\n' "${R}[MISSING]${D} Directory: $1"
        issues=$((issues + 1))
    fi
}

check_cmd() {
    if command -v "$1" >/dev/null 2>&1; then
        printf '%b\n' "${G}[OK]${D} Command: $1"
    else
        printf '%b\n' "${R}[MISSING]${D} Command: $1"
        printf '  Suggestion: check Termux package availability for %s.\n' "$1"
        issues=$((issues + 1))
    fi
}

printf '%b\n' "${C}[1] Platform configuration${D}"
if [ -r "$CONF" ]; then
    printf '%b\n' "${G}[OK]${D} platform.conf exists and is readable"
else
    printf '%b\n' "${R}[ISSUE]${D} platform.conf missing or unreadable"
    issues=$((issues + 1))
fi

printf '\n%b\n' "${C}[2] Essential directories${D}"
for d in core config install members ai catalog/tools catalog/labs catalog/projects docs backend; do
    check_dir "$d"
done

printf '\n%b\n' "${C}[3] Essential commands${D}"
for c in bash python git curl; do
    check_cmd "$c"
done

printf '\n%b\n' "${C}[4] CZH commands${D}"
for c in czh-status czh-monitor czh-join czh-assistant czh-tools czh-hub; do
    if command -v "$c" >/dev/null 2>&1; then
        printf '%b\n' "${G}[READY]${D} $c"
    else
        printf '%b\n' "${Y}[NOT FOUND]${D} $c"
        printf '  Suggestion: inspect the relevant module and Termux PATH before reinstalling.\n'
        issues=$((issues + 1))
    fi
done

printf '\n%b\n' "${C}[5] Recent activity errors${D}"
if [ -r "$LOG" ]; then
    if grep -q 'result=ERROR' "$LOG"; then
        printf '%b\n' "${Y}[NOTICE]${D} Historical ERROR entries exist in the local activity log."
        printf '%s\n' 'Most recent entries:'
        tail -n 5 "$LOG"
        printf '\n%s\n' 'Meaning: an earlier command returned a non-zero exit code.'
        printf '%s\n' 'This does not prove the module is currently failing.'
        printf '%s\n' 'Suggestion: rerun the module and inspect its live output if the issue returns.'
    else
        printf '%b\n' "${G}[OK]${D} No ERROR entries found in the activity log."
    fi
else
    printf '%b\n' "${Y}[NOTICE]${D} Activity log not found or unreadable."
fi

printf '\n%b\n' "${C}[6] Summary${D}"
if [ "$issues" -eq 0 ]; then
    printf '%b\n' "${G}Foundation checks passed.${D}"
    printf '%s\n' 'This is not a guarantee that every platform feature is complete.'
else
    printf '%b\n' "${Y}Found $issues missing item(s) to investigate.${D}"
    printf '%s\n' 'Review the messages above before attempting any repair.'
fi

printf '\n%s\n' 'Privacy: this report stays on this device; nothing is uploaded.'
printf '%s\n\n' 'Doctor finished. No repairs or configuration changes were made.'
