#!/data/data/com.termux/files/usr/bin/bash
set -u

ROOT="${CZH_PLATFORM_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
CONFIG="$ROOT/config/platform.conf"

case "${1:-status}" in
  status)
    printf '\n=== CZH CORE STATUS ===\n'
    printf 'Platform: CZH\n'
    printf 'Version: 2.0.0-dev\n'
    printf 'Root: %s\n' "$ROOT"

    if [ -r "$CONFIG" ]; then
      echo 'Configuration: FOUND'
    else
      echo 'Configuration: MISSING'
    fi

    for path in core install members ai catalog/tools catalog/labs catalog/projects backend; do
      if [ -d "$ROOT/$path" ]; then
        printf '[ FOUND ] %s\n' "$path"
      else
        printf '[ MISSING ] %s\n' "$path"
      fi
    done

    echo 'Status check complete.'
    ;;
  *)
    echo 'Usage: czh-core.sh [status]'
    exit 2
    ;;
esac
