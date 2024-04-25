#!/bin/bash
#Bash script that takes in a URL, sends a GET
curl -s "$1" | { read status; [ $status -eq 200 ] & curl -s "$1"; }
