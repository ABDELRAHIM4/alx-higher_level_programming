#!/bin/bash
#Bash script that takes in a URL, sends a GET
status=$(curl -s -o /dev/null -w "%{http_code}" "$1")
