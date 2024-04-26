#!/usr/bin/python3
#Python script that takes in a URL
import urllib.request
import sys
if __name__ == "__main__":
    val = sys.argv[1]
    with urllib.request.urlopen(val) as response:
        res = response.getheader('X-Request-Id')
        print(res)
