#!/bin/bash
# Connecting to an URL with curl
curl -sI -o /dev/null -w '%{response_code}' "$1"
