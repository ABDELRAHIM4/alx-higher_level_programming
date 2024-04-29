#!/bin/bash
#Bash script that sends a JSON POST
curl -s -X post -d "Content-Type: sppliction/json" "$1" "$2"
