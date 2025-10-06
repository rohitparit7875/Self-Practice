#!/bin/bash
# disk_check.sh

THRESHOLD=80
USAGE=$(df / | grep / | awk '{print $5}' | sed 's/%//g')

if [ "$USAGE" -gt "$THRESHOLD" ]; then
  echo "Warning: Disk usage is above $THRESHOLD%! Current usage: $USAGE%"
else
  echo "Disk usage is normal: $USAGE%"
fi
