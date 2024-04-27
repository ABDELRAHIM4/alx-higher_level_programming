#!/usr/bin/python3
import urllib.request
import sys
import requests
from urllib.parse import urlencode
if __name__ == "__main__":
    val = sys.argv[1]
    em = sys.argv[2]
    dat = urlencode({"email": em}).encode("utf-8")
    req = urllib.request.Request(val, dat)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
