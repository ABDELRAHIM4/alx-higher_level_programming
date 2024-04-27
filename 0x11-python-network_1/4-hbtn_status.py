#!/usr/bin/python3
"""Python script that fetches"""
import requests
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    gettet = requests.get(url)
    res = gettet.json()
    print("Body response:")
    print("- type: {}".format(get))
    print("- content: {}".format(res['status']))
