#!/bin/bash
# service_monitor.sh

SERVICE="nginx"

if ! systemctl is-active --quiet $SERVICE; then
    echo "$SERVICE is down! Restarting..."
    systemctl start $SERVICE
    echo "$SERVICE restarted on $(date)" >> /var/log/service_monitor.log
fi
