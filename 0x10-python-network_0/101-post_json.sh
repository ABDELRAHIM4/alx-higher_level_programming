#!/bin/bash
#Bash script that sends a JSON POST
curl -s -X post  -H "Content-Type: application/json" -d "@$2" "$1"
