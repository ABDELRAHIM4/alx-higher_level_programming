#!/usr/bin/python3
import urllib.request
import sys
from urllib.parse import urlencode
if __name__ == "__main__":
    val = sys.argv[1]
    em = sys.argv[2]
    num = urlencode({'email': em})
    data = num.encode('utf-8')
    req =  urllib.request.Request(val, data)
    print(data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
