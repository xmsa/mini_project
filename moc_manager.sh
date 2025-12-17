#!/bin/bash

STATE_FILE="$HOME/.mocp_state"

save_state() {
    TRACK_INFO=$(mocp -i 2>/dev/null)
    
    if [ -z "$TRACK_INFO" ]; then
        echo "MOC server not running. Nothing to save."
        [ -f "$STATE_FILE" ] && rm "$STATE_FILE"
        return
    fi

    POSITION=$(echo "$TRACK_INFO" | grep "CurrentSec" | sed 's/CurrentSec: \([0-9]*\)/\1/')
    STATE=$(echo "$TRACK_INFO" | grep "State" | sed 's/State: //')
    TRACK_FILE=$(echo "$TRACK_INFO" | grep "File" | sed 's/File: //')
    
    echo "$TRACK_FILE,$POSITION,$STATE" > "$STATE_FILE"
    echo "State saved: $TRACK_FILE at $POSITION seconds ($STATE)."
}

load_state() {
    if [ -f "$STATE_FILE" ]; then
        LAST_TRACK=$(awk -F, '{print $1}' "$STATE_FILE")
        LAST_POSITION=$(awk -F, '{print $2}' "$STATE_FILE")
        
        if [ -f "$LAST_TRACK" ]; then
            mocp -l "$LAST_TRACK"
            if [ ! -z "$LAST_POSITION" ]; then
                mocp -j "${LAST_POSITION}s"
                echo "Resuming: $LAST_TRACK from $LAST_POSITION seconds."
            fi
        else
            echo "Last track not found: $LAST_TRACK. Removing state file."
            rm "$STATE_FILE"
        fi
    else
        echo "No previous state found."
    fi
}

is_moc_running() {
    mocp -i >/dev/null 2>&1
    return $?
}

case "$1" in
    start)
        if is_moc_running; then
            echo "MOC server already running. Opening console."
            mocp
        else
            echo "Starting MOC server and loading last track..."
            mocp -S &
            sleep 1
            load_state
            mocp
        fi
        ;;
    stop)
        if is_moc_running; then
            TRACK_INFO=$(mocp -i)
            STATE=$(echo "$TRACK_INFO" | grep "State" | sed 's/State: //')
            
            if [[ "$STATE" == "PLAY" || "$STATE" == "PAUSE" ]]; then
                save_state
            else
                echo "No track or position found. Removing state file."
                [ -f "$STATE_FILE" ] && rm "$STATE_FILE"
            fi

            mocp -x
            echo "MOC server stopped."
        else
            echo "MOC server is not running."
        fi
        ;;
    next)
        if is_moc_running; then
            mocp -f
        else
            echo "MOC server is not running."
        fi
        ;;
    previous)
        if is_moc_running; then
            mocp -r
        else
            echo "MOC server is not running."
        fi
        ;;
    toggle)
        if is_moc_running; then
            mocp -G
        else
            echo "MOC server is not running."
        fi
        ;;
    save)
        save_state
        ;;
    load)
        load_state
        ;;
    *)
        echo "Usage: $0 {save|load|start|stop|next|previous|toggle}"
        exit 1
        ;;
esac
