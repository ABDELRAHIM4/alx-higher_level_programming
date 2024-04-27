#!/usr/bin/python3
"""Python script that fetches"""
import requests
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    gettet = requests.get(url)
    print("Body response:")
    print("- type: {}".format(type(gettet.text)))
    print("- content: {}".format(gettet.text))
