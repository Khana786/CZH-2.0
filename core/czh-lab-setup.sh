#!/data/data/com.termux/files/usr/bin/bash
set -eu

ROOT="$HOME/CZH"
PLATFORM="$ROOT/Platform-v2"
CONFIG="$PLATFORM/config/platform.conf"

echo "================================================"
echo "             CZH WHITE HAT CYBER LAB"
echo "          LEARN • SECURE • DEFEND"
echo "================================================"
echo
echo "[1/5] Checking Termux environment..."

if [ -z "${PREFIX:-}" ] || [ ! -d "$PREFIX" ]; then
    echo "ERROR: Run this setup inside Termux."
    exit 1
fi

echo "[2/5] Checking platform configuration..."
if [ ! -f "$CONFIG" ]; then
    echo "ERROR: CZH platform config is missing:"
    echo "$CONFIG"
    exit 1
fi

echo "[3/5] Checking required directories..."
for dir in core config install members ai catalog/tools catalog/labs catalog/projects docs backend; do
    mkdir -p "$PLATFORM/$dir"
    printf '[ OK ] %s\n' "$dir"
done

echo "[4/5] Checking essential dependencies..."
missing=""
for pkg in bash python git curl; do
    if ! command -v "$pkg" >/dev/null 2>&1; then
        missing="$missing $pkg"
    else
        printf '[ FOUND ] %s\n' "$pkg"
    fi
done

if [ -n "$missing" ]; then
    echo
    echo "Missing commands:$missing"
    echo "Install only the missing packages with:"
    echo "pkg install$missing"
    echo
    echo "Then run czh-lab-setup again."
    exit 1
fi

echo "[5/5] Checking CZH commands..."
for cmd in czh-status czh-monitor czh-join czh-assistant; do
    if command -v "$cmd" >/dev/null 2>&1; then
        printf '[ READY ] %s\n' "$cmd"
    else
        printf '[ NOT INSTALLED YET ] %s\n' "$cmd"
    fi
done

echo
echo "================================================"
echo " CZH FOUNDATION CHECK COMPLETED"
echo " This checks the foundation; it does not claim"
echo " that every cybersecurity tool is installed."
echo "================================================"
echo
echo "Next steps:"
echo "  czh-monitor"
echo "  czh-join"
