#!/usr/bin/python3
"""Python script that fetches"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print("Body response:\n")
    print("- type: {}\n".format(type(content)))
    print("- content: {}\n".format(content))
    print("- utf8 content: {}\n".format(content.decode('utf-8')))
