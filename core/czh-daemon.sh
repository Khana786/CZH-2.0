#!/data/data/com.termux/files/usr/bin/bash

LOG_FILE="$HOME/CZH/PrivateData/daemon_alerts.log"
REPORTS_DB="$HOME/CZH/PrivateData/BugBounty/reports.db"
PROGRESS_FILE="$HOME/CZH/PrivateData/course-progress.json"

LAST_COUNT=0
touch "$LOG_FILE"
chmod 600 "$LOG_FILE"

echo "[+] CZH AUTO-DAEMON STARTED..." >> "$LOG_FILE"

# Initial count setup
if [ -f "$REPORTS_DB" ]; then
    LAST_COUNT=$(awk -F'|' '$6=="PENDING"{c++} END{print c+0}' "$REPORTS_DB")
fi

while true; do
    # 1. Check for NEW Bug Reports
    if [ -f "$REPORTS_DB" ]; then
        CURRENT_COUNT=$(awk -F'|' '$6=="PENDING"{c++} END{print c+0}' "$REPORTS_DB")
        
        if [ "$CURRENT_COUNT" -gt "$LAST_COUNT" ]; then
            NEW_REPORTS=$((CURRENT_COUNT - LAST_COUNT))
            TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
            
            echo "[$TIMESTAMP] ALERT: $NEW_REPORTS new Bug Report(s) detected!" >> "$LOG_FILE"
            
            # Send Notification
            termux-notification \
              --title "🚨 CZH BUG REPORT ALERT" \
              --content "Admin, $NEW_REPORTS new Bug Report(s) submitted! Check Admin Panel." \
              --priority high \
              --sound \
              --vibrate 500 2>/dev/null

            LAST_COUNT=$CURRENT_COUNT
        fi
    fi

    # 2. Check for Academy Completion (10/10)
    if [ -f "$PROGRESS_FILE" ] && [ ! -f "$HOME/CZH/PrivateData/cert_notified.flag" ]; then
        COMPLETED=$(python3 -c "import json; print(len(json.load(open('$PROGRESS_FILE')).get('completed', [])))" 2>/dev/null || echo 0)
        
        if [ "$COMPLETED" -eq 10 ]; then
            termux-notification \
              --title "🎓 CZH ACADEMY COMPLETE" \
              --content "A member has completed 10/10 modules! Issue their Elite ID Card now." \
              --priority high \
              --sound \
              --vibrate 500 2>/dev/null
            
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] ALERT: Academy 10/10 Completed." >> "$LOG_FILE"
            touch "$HOME/CZH/PrivateData/cert_notified.flag"
        fi
    fi

    sleep 30 # Check every 30 seconds for faster alerts
done
