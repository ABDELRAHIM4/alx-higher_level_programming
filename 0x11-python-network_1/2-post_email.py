#!/usr/bin/python3
""" Python script that takes in a URL"""
import urllib.request
import sys
import requests
if __name__ == "__main__":
    val = sys.argv[1]
    em = ({"email": sys.argv[2]})
    dat = urllib.parse.urlencode(em).encode("ascii")
    req = urllib.request.Request(val, dat)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
