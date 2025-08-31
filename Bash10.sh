#!/bin/bash
# Service monitoring

SERVICE="apache2"

if ! systemctl is-active --quiet "$SERVICE"; then
    echo "$SERVICE is down. Restarting..."
    systemctl start "$SERVICE"
else
    echo "$SERVICE is running."
fi