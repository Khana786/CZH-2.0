#!/data/data/com.termux/files/usr/bin/bash

clear
R='\033[91m'
G='\033[92m'
Y='\033[93m'
C='\033[96m'
W='\033[97m'
D='\033[90m'
BG_R='\033[41m'
BG_B='\033[44m'
NC='\033[0m'

LOG_FILE="$HOME/CZH/PrivateData/reports/netscan.log"
mkdir -p "$HOME/CZH/PrivateData/reports"
touch "$LOG_FILE"
chmod 600 "$LOG_FILE"

echo -e "${C}"
echo -e "     ███╗   ██╗███████╗████████╗"
echo -e "     ████╗  ██║██╔════╝╚══██╔══╝"
echo -e "     ██╔██╗ ██║█████╗     ██║   "
echo -e "     ██║╚██╗██║██╔══╝     ██║   "
echo -e "     ██║ ╚████║███████╗   ██║   "
echo -e "     ╚═╝  ╚═══╝╚══════╝   ╚═╝   "
echo -e "${W}      S C A N N E R${NC}"
echo -e "${NC}"

echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BG_R}${W}  ║  ☠  N E T W O R K   R E C O N N A I S S A N C E   T O O L  ☠    ║${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"

echo -e "${Y}  [!] WARNING: Scan only YOUR OWN network. Unauthorized scanning is illegal.${NC}\n"

# Get Local IP and Subnet
IP=$(ip route get 1.1.1.1 2>/dev/null | grep -oP 'src \K\S+' | head -1)
if [ -z "$IP" ]; then
    IP=$(ifconfig wlan0 2>/dev/null | grep 'inet ' | awk '{print $2}' | head -1)
fi

if [ -z "$IP" ]; then
    echo -e "${R}  [✗] ERROR: Could not determine local network IP. Are you connected to WiFi?${NC}"
    exit 1
fi

# If IP is CGNAT (starts with 100.), warn user
if [[ "$IP" == 100.* ]]; then
    echo -e "${R}  [!] NOTE: You are on a Mobile Carrier Network (CGNAT). Direct device scan may not work here.${NC}"
    echo -e "${R}  [!] Please connect to a WiFi Router for proper results.${NC}\n"
fi

SUBNET=$(echo "$IP" | awk -F. '{print $1"."$2"."$3".0/24"}')

echo -e "${C}  ┌───[ T A R G E T   I N T E L ]────────────────────────────────────┐${NC}"
echo -e "  ${W}▶ Your Local IP : ${G}$IP${NC}"
echo -e "  ${W}▶ Target Subnet : ${G}$SUBNET${NC}"
echo -e "${C}  └──────────────────────────────────────────────────────────────────┘${NC}\n"

read -r -p "$(echo -e "${R}  ▶ INITIATE NETWORK SCAN? (y/N): ${NC}")" confirm
if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo -e "\n${R}  [✗] Scan aborted.${NC}"
    exit 0
fi

echo -e "\n${Y}  [*] INITIATING DEEP SCAN ON $SUBNET...${NC}"
echo -e "${D}  [*] This may take a few seconds. (Timeout: 15s max)${NC}\n"

# Run Nmap with fast timeout to prevent hanging
if ! command -v nmap >/dev/null 2>&1; then
    echo -e "${R}  [✗] Nmap not installed. Install it first using: pkg install nmap${NC}"
    exit 1
fi

TMP_SCAN=$(mktemp)
# --max-retries 1 and --host-timeout 5s makes it much faster
timeout 20s nmap -sn --max-retries 1 --host-timeout 5s "$SUBNET" > "$TMP_SCAN" 2>/dev/null

echo -e "${C}  ┌───[ D I S C O V E R E D   D E V I C E S ]────────────────────────┐${NC}"
COUNT=0
while IFS= read -r line; do
    if [[ "$line" == *"Nmap scan report for"* ]]; then
        HOST=$(echo "$line" | sed 's/Nmap scan report for //')
        COUNT=$((COUNT+1))
        echo -e "  ${G}[$COUNT]${W} Target  : ${C}$HOST${NC}"
        
        DATE=$(date '+%Y-%m-%d %H:%M:%S')
        echo "[$DATE] Found Device: $HOST" >> "$LOG_FILE"
    elif [[ "$line" == *"MAC Address:"* ]]; then
        MAC=$(echo "$line" | sed 's/ *MAC Address: //')
        echo -e "      ${D}└─ MAC   : $MAC${NC}"
    fi
done < "$TMP_SCAN"

if [ "$COUNT" -eq 0 ]; then
    echo -e "  ${Y}[!] No devices found. (Mobile networks often block Ping Sweeps).${NC}"
else
    echo -e "\n  ${G}[✓] SCAN COMPLETE. Total Devices Found: $COUNT${NC}"
fi

echo -e "${C}  └──────────────────────────────────────────────────────────────────┘${NC}\n"
rm -f "$TMP_SCAN"

echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BG_B}${W}  [+] SCAN LOGGED TO: PrivateData/reports/netscan.log                ║${NC}"
echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}"
echo ""
read -r -p "  Press Enter to exit..."
