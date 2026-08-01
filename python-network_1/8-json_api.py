#!/usr/bin/python3
"""Sends a POST request with a letter and parses the JSON response."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        json_data = r.json()
        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
    except ValueError:
        print("Not a valid JSON")
