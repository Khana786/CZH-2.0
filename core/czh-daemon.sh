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
        
        # Check for Academy Completion (10/10)
        PROGRESS_FILE="$HOME/CZH/PrivateData/course-progress.json"
        if [ -f "$PROGRESS_FILE" ]; then
            COMPLETED=$(python3 -c "import json; print(len(json.load(open('$PROGRESS_FILE')).get('completed', [])))" 2>/dev/null || echo 0)
            if [ "$COMPLETED" -eq 10 ] && [ ! -f "$HOME/CZH/PrivateData/cert_notified.flag" ]; then
                termux-notification --title "🎓 CZH ALERT" --content "A member has completed 10/10 modules! Issue their ID Card now." --priority high 2>/dev/null
                echo "[$(date '+%Y-%m-%d %H:%M:%S')] ALERT: Academy 10/10 Completed." >> "$HOME/CZH/PrivateData/daemon_alerts.log"
                touch "$HOME/CZH/PrivateData/cert_notified.flag"
            fi
        fi

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
