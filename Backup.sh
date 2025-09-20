#!/bin/bash
# backup.sh

SOURCE_DIR="/home/$USER/Documents"
BACKUP_DIR="/home/$USER/backup"
DATE=$(date +%F)

mkdir -p "$BACKUP_DIR"
tar -czf "$BACKUP_DIR/backup_$DATE.tar.gz" "$SOURCE_DIR"

echo "Backup completed at $BACKUP_DIR/backup_$DATE.tar.gz"
