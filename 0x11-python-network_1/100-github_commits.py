#!/usr/bin/python3
"""Python script that takes 2 arguments """
import sys
import requests
if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://developer.github.com/v3/repos/commits/"
    response = requests.get(url, auth=(repository_name, owner_name))
    print(response.status_code)
    if response.status_code == 403 and response.headers.get("X-RateLimit-Remaining") == "0":
        print("Error:", response.status_code, "Rate limit exceeded. Wait for an hour.")
    reqs = response.json()
    for req in reqs:
        name = req["sha"]
        auther = req["auther"]["login"]
        print(f"{name} {auther}")
