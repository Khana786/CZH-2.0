#!/data/data/com.termux/files/usr/bin/bash
set -u

ROOT="${CZH_PLATFORM_ROOT:-$HOME/CZH/Platform-v2}"

echo '=== CZH WHITE HAT CYBER LAB ==='
echo 'Foundation check; no automatic installations.'

for command_name in bash python git curl; do
  if command -v "$command_name" >/dev/null 2>&1; then
    printf '[ FOUND ] %s\n' "$command_name"
  else
    printf '[ MISSING ] %s\n' "$command_name"
  fi
done

echo
for path in core config install members ai catalog/tools catalog/labs catalog/projects docs backend; do
  if [ -d "$ROOT/$path" ]; then
    printf '[ FOUND ] %s\n' "$path"
  else
    printf '[ MISSING ] %s\n' "$path"
  fi
done

echo
echo 'This check does not claim every lab or tool is implemented.'
