#!/usr/bin/python3
"""Python script that takes in a URL"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    gettet = requests.get(url)
    var = gettet.headers.get('X-Request-Id')
    print(var)
