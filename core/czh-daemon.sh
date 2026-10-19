#!/data/data/com.termux/files/usr/bin/bash

# CZH AUTO-DAEMON: Background Monitoring System
LOG_FILE="$HOME/CZH/PrivateData/daemon_alerts.log"
REPORTS_DB="$HOME/CZH/PrivateData/BugBounty/reports.db"
LAST_COUNT=0

touch "$LOG_FILE"
chmod 600 "$LOG_FILE"

echo "[+] CZH AUTO-DAEMON STARTED..." >> "$LOG_FILE"

while true; do
    if [ -f "$REPORTS_DB" ]; then
        # Count total pending reports
        CURRENT_COUNT=$(awk -F'|' '$6=="PENDING"{c++} END{print c+0}' "$REPORTS_DB")
        
        if [ "$CURRENT_COUNT" -gt "$LAST_COUNT" ]; then
            NEW_REPORTS=$((CURRENT_COUNT - LAST_COUNT))
            TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
            
            # Log Alert
            echo "[$TIMESTAMP] ALERT: $NEW_REPORTS new Bug Report(s) detected!" >> "$LOG_FILE"
            
            # Send Termux Notification (if termux-api is installed)
            if command -v termux-notification >/dev/null 2>&1; then
                termux-notification \
                  --title "🚨 CZH CYBER TEAM ALERT" \
                  --content "Admin, $NEW_REPORTS new Bug Report(s) submitted! Check Admin Panel." \
                  --priority high
            fi
            
            # Update last count
            LAST_COUNT=$CURRENT_COUNT
        fi
    fi
    sleep 60 # Check every 60 seconds
done
