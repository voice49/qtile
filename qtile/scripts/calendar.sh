#!/bin/bash

# Display day and time
date

# Run calcurse in Alacritty terminal
alacritty --hold -e "calcurse" &

# Wait for a brief moment to allow the terminal window to fully open
sleep 1

# Get the PID of the Alacritty terminal
terminal_pid=$!

# Function to check if mouse cursor is over the terminal
is_cursor_over_terminal() {
    # Get the window ID of the terminal
    window_id=$(xdotool search --pid $terminal_pid)

    if [ -z "$window_id" ]; then
        # If the window ID is empty, return false
        return 1
    fi

    # Get the position of the mouse cursor
    mouse_x=$(xdotool getmouselocation --shell | grep 'X' | cut -d '=' -f 2)
    mouse_y=$(xdotool getmouselocation --shell | grep 'Y' | cut -d '=' -f 2)

    # Get the position and dimensions of the terminal window
    eval $(xdotool getwindowgeometry --shell $window_id)

    # Check if the mouse cursor is over the terminal window
    if [ "$mouse_x" -ge "$X" ] && [ "$mouse_x" -le "$(($X + $WIDTH))" ] && [ "$mouse_y" -ge "$Y" ] && [ "$mouse_y" -le "$(($Y + $HEIGHT))" ]; then
        return 0
    else
        return 1
    fi
}

# Loop to continuously check if the mouse cursor is over the terminal
while :
do
    if ! is_cursor_over_terminal; then
        # If the mouse cursor is not over the terminal, kill the terminal
        kill $terminal_pid
        break
    fi
    sleep 1
done
