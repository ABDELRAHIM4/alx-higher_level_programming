#!/usr/bin/python3
""" Python script that takes in a URL"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email' : email}
    res = requests.post(url, data=data)
    print("Your email is: {}".format(email))
