#!/usr/bin/python3
"""Python script that takes 2 arguments """
import sys
import requests
if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    ur = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"
    response = requests.get(ur)
    if response.status_code == 200:
        reqs = response.json()
        for req in reqs[-10:]:
            sha = req["sha"]
            name = req["author"]["login"]
            print(f"{sha}: {name}")
