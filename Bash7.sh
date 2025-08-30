#!/bin/bash
HOUR=$(date +"%H")

if [ $HOUR -lt 12 ]; then
    echo "Good Morning!"
elif [ $HOUR -lt 18 ]; then
    echo "Good Afternoon!"
else
    echo "Good Evening!"
fi
