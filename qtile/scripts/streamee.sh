#!/bin/bash

# URL of the website to open
website_url="https://streamee.com/"

# Check if xdg-open command is available
command -v xdg-open > /dev/null 2>&1
if [ $? -eq 0 ]; then
    xdg-open "$website_url"
else
    echo "Error: xdg-open command not found. Please open your web browser and navigate to: $website_url"
fi
