#!/bin/bash
#Bash script that takes in a URL
curl -s -X OPTIONS "$1" -D - | grep -i 'allow' | awk '{print $2}'
