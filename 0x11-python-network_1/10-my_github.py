#!/usr/bin/python3
"""Python script that takes your GitHub credentials"""
import sys
import requests
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        data = response.json()
        id_n = data.get("id")
        print(id_n)
    else:
        print("None")
