#!/bin/bash
# Connecting to an URL with curl
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
