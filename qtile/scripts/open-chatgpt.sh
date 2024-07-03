#!/bin/bash
# Replace the following URL with the actual URL where your chat system is hosted
chat_url="https://chat.openai.com/"

# Check if xdg-open command is available
command -v xdg-open > /dev/null 2>&1
if [ $? -eq 0 ]; then
    xdg-open "$chat_url"
else
    echo "Error: xdg-open command not found. Please open your web browser and navigate to: $chat_url"
fi