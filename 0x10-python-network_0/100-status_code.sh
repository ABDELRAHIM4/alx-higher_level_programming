#!/bin/bash
#Bash script that sends a request to a URL
curl -o /dev/null -s -w "%{http_code}" "$1"
