#!/bin/bash
# Connecting to an URL with curl
curl -s "$1" -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
