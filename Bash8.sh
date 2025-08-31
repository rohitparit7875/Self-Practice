#!/bin/bash
# Backup script

SOURCE="/home/user/documents"
DEST="/home/user/backup"
DATE=$(date +%F)

mkdir -p "$DEST"
tar -czf "$DEST/backup-$DATE.tar.gz" "$SOURCE"

echo "Backup completed: $DEST/backup-$DATE.tar.gz"
