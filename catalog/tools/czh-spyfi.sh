#!/data/data/com.termux/files/usr/bin/bash

clear
R='\033[91m'; W='\033[97m'; C='\033[96m'; G='\033[92m'; Y='\033[93m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

WHITELIST_FILE="$HOME/CZH/PrivateData/spyfi_whitelist.txt"
mkdir -p "$HOME/CZH/PrivateData"
touch "$WHITELIST_FILE"

scan_network() {
    clear
    echo -e "${C}"
    echo -e "     ███████╗██████╗ ██╗   ██╗    ███████╗██╗"
    echo -e "     ██╔════╝██╔══██╗╚██╗ ██╔╝    ██╔════╝██║"
    echo -e "     ███████╗██████╔╝ ╚████╔╝     █████╗  ██║"
    echo -e "     ╚════██║██╔═══╝   ╚██╔╝      ██╔══╝  ██║"
    echo -e "     ███████║██║        ██║       ██║     ██║"
    echo -e "     ╚══════╝╚═╝        ╚═╝       ╚═╝     ╚═╝"
    echo -e "${W}      W I F I   S P Y   &   T R A C K E R${NC}"
    echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BG_R}${W}  ║  ☠  D E V I C E   S P Y - F I   //   N E T W O R K  ☠           ║${NC}"
    echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"

    IP=$(ip route get 1.1.1.1 2>/dev/null | grep -oP 'src \K\S+' | head -1)
    if [ -z "$IP" ]; then
        IP=$(ifconfig wlan0 2>/dev/null | grep 'inet ' | awk '{print $2}' | head -1)
    fi

    if [ -z "$IP" ]; then
        echo -e "${R}  [✗] ERROR: Not connected to any WiFi network.${NC}"
        read -r -p "  Press Enter to return..."
        return
    fi

    SUBNET=$(echo "$IP" | awk -F. '{print $1"."$2"."$3".0/24"}')
    
    if [[ "$IP" == 100.* ]]; then
        echo -e "${R}  [!] NOTE: You are on a Mobile Carrier Network (CGNAT).${NC}"
        echo -e "${R}  [!] Direct device scan may not work here. Connect to WiFi for best results.${NC}\n"
    fi
    
    echo -e "${W}  ▶ Your IP   : ${G}$IP${NC}"
    echo -e "${W}  ▶ Target    : ${G}$SUBNET${NC}\n"
    echo -e "${Y}  [*] Deploying Spy-Fi Payload...${NC}"
    sleep 1
    echo -e "${C}  [*] Scanning for connected devices...${NC}\n"

    # Try nmap first (faster and better)
    TMP_FILE=$(mktemp)
    if command -v nmap >/dev/null 2>&1; then
        timeout 15s nmap -sn --max-retries 1 --host-timeout 3s "$SUBNET" > "$TMP_FILE" 2>/dev/null
    else
        echo -e "${R}  [✗] nmap not installed. Run: pkg install nmap${NC}"
        rm -f "$TMP_FILE"
        read -r -p "  Press Enter..."
        return
    fi

    echo -e "${C}  ┌──────────────────────────────────────────────────────────┐${NC}"
    echo -e "${C}  │${NC} ${W}IP ADDRESS         │ MAC ADDRESS       │ STATUS    ${C}│${NC}"
    echo -e "${C}  ├──────────────────────────────────────────────────────────┤${NC}"

    COUNT=0
    UNKNOWN=0
    
    # Extract IP and MAC cleanly using grep/awk
    CURRENT_IP=""
    while IFS= read -r line; do
        if [[ "$line" == *"Nmap scan report for"* ]]; then
            CURRENT_IP=$(echo "$line" | sed 's/Nmap scan report for //' | awk '{print $1}')
            CURRENT_MAC="Unknown"
        elif [[ "$line" == *"MAC Address:"* ]]; then
            CURRENT_MAC=$(echo "$line" | sed 's/ *MAC Address: //' | awk '{print $1}')
            
            STATUS="${G}SAFE${NC}"
            if ! grep -q "$CURRENT_MAC" "$WHITELIST_FILE" 2>/dev/null; then
                STATUS="${R}UNKNOWN${NC}"
                UNKNOWN=$((UNKNOWN+1))
            fi
            
            printf "  ${C}│${NC} ${W}%-18s ${C}│${NC} ${Y}%-17s ${C}│${NC} %b\n" "$CURRENT_IP" "$CURRENT_MAC" "$STATUS"
            COUNT=$((COUNT+1))
        fi
    done < "$TMP_FILE"
    
    echo -e "${C}  └──────────────────────────────────────────────────────────┘${NC}\n"

    if [ "$COUNT" -eq 0 ]; then
        echo -e "${Y}  [!] No devices found. (Carrier networks like Jio/Airtel block device discovery).${NC}"
        echo -e "${Y}  [!] Connect to a normal WiFi Router for proper results.${NC}"
    else
        echo -e "${G}  [✓] Scan complete. Total devices: $COUNT${NC}"
        if [ "$UNKNOWN" -gt 0 ]; then
            echo -e "${BG_R}${W}  ⚠ ALERT: $UNKNOWN unknown device(s) found! ⚠ ${NC}"
            termux-notification --title "🚨 SPY-FI ALERT" --content "$UNKNOWN unknown device(s) detected on your WiFi!" --priority high --sound 2>/dev/null
        fi
    fi
    rm -f "$TMP_FILE"
    read -r -p "  Press Enter to return..."
}

whitelist_device() {
    clear
    echo -e "${C}  ┌───[ W H I T E L I S T   M A N A G E R ]────────────────────┐${NC}"
    read -r -p "  [?] Enter MAC Address to Trust (e.g., 00:1A:2B:3C:4D:5E): " mac
    if [ -n "$mac" ]; then
        echo "$mac" >> "$WHITELIST_FILE"
        echo -e "\n${G}  [✓] MAC $mac added to trusted list.${NC}"
    fi
    read -r -p "  Press Enter to return..."
}

view_whitelist() {
    clear
    echo -e "${C}  ┌───[ T R U S T E D   D E V I C E S ]────────────────────────┐${NC}"
    if [ -s "$WHITELIST_FILE" ]; then
        cat "$WHITELIST_FILE" | while read -r m; do echo -e "  ${G}✔${NC} ${W}$m${NC}"; done
    else
        echo -e "  ${Y}No devices in whitelist yet.${NC}"
    fi
    echo -e "${C}  └──────────────────────────────────────────────────────────────┘${NC}"
    read -r -p "  Press Enter to return..."
}

while true; do
    clear
    echo -e "${C}"
    echo -e "     ███████╗██████╗ ██╗   ██╗    ███████╗██╗"
    echo -e "     ██╔════╝██╔══██╗╚██╗ ██╔╝    ██╔════╝██║"
    echo -e "     ███████╗██████╔╝ ╚████╔╝     █████╗  ██║"
    echo -e "     ╚════██║██╔═══╝   ╚██╔╝      ██╔══╝  ██║"
    echo -e "     ███████║██║        ██║       ██║     ██║"
    echo -e "     ╚══════╝╚═╝        ╚═╝       ╚═╝     ╚═╝"
    echo -e "${W}      W I F I   S P Y   &   T R A C K E R${NC}"
    echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "  ║  ☠  C Z H   S P Y - F I   //   N E T W O R K  ☠                  ║"
    echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"

    echo -e "${C}  ┌────────────────────────────────────────────┐${NC}"
    echo -e "  ${C}│${NC} ${Y}[1]${W} SCAN NETWORK (Find Devices)           ${C}│${NC}"
    echo -e "  ${C}│${NC} ${Y}[2]${W} TRUST A DEVICE (Whitelist MAC)        ${C}│${NC}"
    echo -e "  ${C}│${NC} ${Y}[3]${W} VIEW TRUSTED DEVICES                   ${C}│${NC}"
    echo -e "  ${C}├────────────────────────────────────────────┤${NC}"
    echo -e "  ${C}│${NC} ${R}[0]${W} ABORT & EXIT                           ${C}│${NC}"
    echo -e "${C}  └────────────────────────────────────────────┘${NC}\n"
    
    read -r -p "$(echo -e "${R}  CZH-SPYFI ➜ ${NC}")" choice

    case "$choice" in
        1) scan_network ;;
        2) whitelist_device ;;
        3) view_whitelist ;;
        0) echo -e "${G}\n  [✓] Spy-Fi radar closed. Stay Alert.${NC}"; exit 0 ;;
        *) echo -e "${R}  [✗] Invalid option.${NC}"; sleep 1 ;;
    esac
done
