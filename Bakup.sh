#!/bin/bash
# cleanup_logs.sh

LOG_DIR="/var/log/myapp"
DAYS=7

echo "Cleaning up logs older than $DAYS days..."
find "$LOG_DIR" -type f -name "*.log" -mtime +$DAYS -exec rm -f {} \;
echo "Cleanup complete."
