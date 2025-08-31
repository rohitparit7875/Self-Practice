#!/bin/bash
# Disk usage alert

THRESHOLD=80
USAGE=$(df / | grep / | awk '{print $5}' | sed 's/%//')

if [ "$USAGE" -gt "$THRESHOLD" ]; then
    echo "Warning: Disk usage is at $USAGE%"
fi
