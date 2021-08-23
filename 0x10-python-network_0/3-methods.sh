#!/bin/bash
# Connecting to an URL with curl
curl -sI "$1" | grep 'Allow' | cut -d ' ' -f 2-
