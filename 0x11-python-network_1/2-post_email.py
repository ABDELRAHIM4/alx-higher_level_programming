#!/usr/bin/python3
import urllib.request
import sys
import requests
from urllib.parse import urlencode
if __name__ == "__main__":
    val = sys.argv[1]
    em = sys.argv[2]
    data = urlencode({"email": em})
    req =  requests.post(val, data)
    print(req.txt)
