#!/usr/bin/python3
"""Python script that fetches"""
import urllib.request
from sys import stdout
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    stdout.write("Body response:\n")
    stdout.write("- type: {}\n".format(type(content)))
    stdout.write("- content: {}\n".format(content))
    stdout.write("- utf8 content: {}\n".format(content.decode('utf-8')))
