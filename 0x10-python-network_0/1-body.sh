#!/bin/bash
#Bash script that takes in a URL, sends a GET
curl -s -X GET "$1" | grep -q 200
