#!/bin/bash
#Bash script that takes in a URL as an argumen
curl -v -s -o /dev/null -w "%{http_code}" -H "X-School-User-Id: 98 " -X GET $1 
