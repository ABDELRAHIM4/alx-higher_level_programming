#!/bin/bash
#Bash script that takes in a URL, sends a GET
url=$1
res=$(curl -s -o /dev/null -w "%{http_code}" -X GET "$url")
if [ "$res" = "200" ]; then
	echo "$res"
fi
