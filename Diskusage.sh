#!/bin/bash
# disk_alert.sh

THRESHOLD=80

usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$usage" -gt "$THRESHOLD" ]; then
    echo "Warning: Disk usage is ${usage}% on $(hostname)" | mail -s "Disk Alert" user@example.com
fi
