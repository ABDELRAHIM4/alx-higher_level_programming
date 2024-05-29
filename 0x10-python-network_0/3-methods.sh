#!/bin/bash
#Bash script that takes in a URL
curl -s -X OPTIONS "$1" -D - | grep -i "Allow" | awk '{print $2}'
