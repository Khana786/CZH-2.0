#!/data/data/com.termux/files/usr/bin/bash
set -u

echo '=== CZH SYSTEM MONITOR ==='
date
echo
echo '--- Storage ---'
df -h "$HOME" 2>/dev/null || echo 'Storage information unavailable.'
echo
echo '--- Runtime ---'
printf 'Bash: '
bash --version 2>/dev/null | head -n 1
printf 'Python: '
python --version 2>&1
echo
echo 'Monitor finished. Local checks only.'
