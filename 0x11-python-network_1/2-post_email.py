#!/usr/bin/python3
import urllib.request
import sys
from urllib.parse import urlencode
if __name__ == "__main__":
    val = sys.argv[1]
    em = sys.argv[2]
    num = urlencode({'email': em})
    #req =  urllib.request.Request(val, data)
    data = num.encode('utf-8')
    print(data)
    with urllib.request.urlopen(val, data) as response:
        print(response.read().decode('utf-8'))
