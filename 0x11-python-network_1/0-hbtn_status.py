#!/usr/bin/python3
"""Python script that fetches"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print("Body response:")
    print("- type: {}".format(type(content)))
    print("- content: {}".format(content))
    print("- utf8 content: {}".format(content.decode('utf-8')))
