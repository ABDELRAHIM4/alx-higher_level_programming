#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request"""
import sys
import requests
def param(letter):
    url = "http://0.0.0.0:5000/search_user"
    let = {"q" : letter}
    response = requests.post(url, data = let)
    try :
        letter = response.json()
        if letter:
            print(f"[{letter.get(id)}] {letter.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
if __name__ == "__main__":
    if len(sys.argv) > 1 :
        letter = sys.argv[1]
        param(letter)
    else:
        print("No result")
