#!/data/data/com.termux/files/usr/bin/bash

VAULT_FILE="$HOME/.czh_vault.dat"
TEMP_FILE="$HOME/.czh_vault.tmp"
ADMIN_KEY="CZH-DARKWEB-QEP5ES"

R='\033[91m'; G='\033[92m'; Y='\033[93m'; C='\033[96m'; W='\033[97m'; D='\033[90m'; BG_R='\033[41m'; NC='\033[0m'

decrypt_vault() {
    if [ -f "$VAULT_FILE" ]; then
        openssl enc -d -aes-256-cbc -pbkdf2 -in "$VAULT_FILE" -out "$TEMP_FILE" -k "$ADMIN_KEY" 2>/dev/null
        if [ $? -ne 0 ]; then
            rm -f "$TEMP_FILE"
            return 1
        fi
    else
        touch "$TEMP_FILE"
    fi
    return 0
}

encrypt_vault() {
    openssl enc -aes-256-cbc -pbkdf2 -in "$TEMP_FILE" -out "$VAULT_FILE" -k "$ADMIN_KEY" 2>/dev/null
    if [ $? -eq 0 ]; then
        rm -f "$TEMP_FILE"
        chmod 600 "$VAULT_FILE"
        return 0
    else
        rm -f "$TEMP_FILE"
        return 1
    fi
}

while true; do
    clear
    echo -e "${C}"
    echo -e "     ██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗"
    echo -e "     ██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝"
    echo -e "     ██║   ██║███████║██║   ██║██║     ██║   "
    echo -e "     ╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║   "
    echo -e "      ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║   "
    echo -e "       ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝   "
    echo -e "${NC}"
    
    echo -e "${R}  ╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BG_R}${W}  ║  ☠  C Z H   S E C U R E   P A S S W O R D   V A U L T  ☠        ║${NC}"
    echo -e "${R}  ╚══════════════════════════════════════════════════════════════════╝${NC}\n"
    
    echo -e "${C}  ┌────────────────────────────────────────────┐${NC}"
    echo -e "  ${C}│${NC} ${Y}[1]${W} ADD NEW CREDENTIAL                     ${C}│${NC}"
    echo -e "  ${C}│${NC} ${Y}[2]${W} VIEW ALL CREDENTIALS (Admin Key)       ${C}│${NC}"
    echo -e "  ${C}│${NC} ${R}[3]${W} WIPE VAULT (Admin Only)                ${C}│${NC}"
    echo -e "  ${C}├────────────────────────────────────────────┤${NC}"
    echo -e "  ${C}│${NC} ${R}[0]${W} ABORT & EXIT                           ${C}│${NC}"
    echo -e "${C}  └────────────────────────────────────────────┘${NC}\n"
    
    read -r -p "$(echo -e "${R}  CZH-VAULT ➜ ${NC}")" choice
    
    case "$choice" in
        1)
            echo ""
            read -r -p "$(echo -e "${Y}  Enter Service/Website (e.g., GitHub): ${NC}")" service
            read -r -p "$(echo -e "${Y}  Enter Username/Email: ${NC}")" user
            read -r -s -p "$(echo -e "${Y}  Enter Password: ${NC}")" pass
            echo ""
            
            if [ -z "$service" ] || [ -z "$pass" ]; then
                echo -e "\n${R}  [✗] Service and Password cannot be empty.${NC}"
            else
                if decrypt_vault; then
                    echo "[$service] | User: $user | Pass: $pass" >> "$TEMP_FILE"
                    if encrypt_vault; then
                        echo -e "\n${G}  [✓] Credential securely encrypted and saved.${NC}"
                    else
                        echo -e "\n${R}  [✗] ERROR: Encryption failed. Credential not saved.${NC}"
                    fi
                else
                    echo -e "\n${R}  [✗] ERROR: Vault decryption failed. Cannot add credential.${NC}"
                fi
            fi
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        2)
            echo ""
            read -r -s -p "$(echo -e "${R}  Enter Admin Key to decrypt: ${NC}")" input_key
            echo ""
            
            if [ "$input_key" != "$ADMIN_KEY" ]; then
                echo -e "\n${R}  [✗] ACCESS DENIED.${NC}"
            else
                if decrypt_vault; then
                    echo -e "\n${C}  --- DECRYPTED VAULT CONTENTS ---${NC}"
                    if [ -s "$TEMP_FILE" ]; then
                        cat "$TEMP_FILE" | awk -F'|' '{print "  \033[92mService:\033[97m"$1"\n  \033[92mUser:   \033[97m"$2"\n  \033[92mPass:   \033[97m"$3"\n  \033[90m-----------------------------------\033[0m"}'
                    else
                        echo -e "  ${Y}Vault is empty.${NC}"
                    fi
                    rm -f "$TEMP_FILE"
                else
                    echo -e "\n${R}  [✗] FATAL: Vault file is corrupted.${NC}"
                fi
            fi
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        3)
            echo ""
            read -r -s -p "$(echo -e "${R}  Enter Admin Key to WIPE vault: ${NC}")" input_key
            echo ""
            
            if [ "$input_key" == "$ADMIN_KEY" ]; then
                rm -f "$VAULT_FILE"
                echo -e "\n${R}  [✗] VAULT WIPED PERMANENTLY.${NC}"
            else
                echo -e "\n${R}  [✗] ACCESS DENIED.${NC}"
            fi
            read -r -p "$(echo -e "${C}  Press Enter to return...${NC}")"
            ;;
        0)
            echo -e "${R}\n  [!] CLOSING SECURE VAULT.${NC}"
            exit 0
            ;;
        *)
            echo -e "${R}  [✗] Invalid option.${NC}"
            sleep 1
            ;;
    esac
done
