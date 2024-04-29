#!/bin/bash
#Bash script that takes in a URL as an argumen
curl -sH "X-School-User-Id: 98 " $"{1}"
#curl -v -s -o /dev/null -w "%{http_code}" -H "X-School-User-Id: 98" -X GET "http://0.0.0.0:5000/route_5"; echo
