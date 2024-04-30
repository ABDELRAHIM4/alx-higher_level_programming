#!/bin/bash
#Bash script that takes in a URL, sends a GET
res=$(curl -s -o /dev/null -w "%{http_code}" -X GET "$1")
if [ "$res" = "200" ]; then
	curl -s $1
fi
