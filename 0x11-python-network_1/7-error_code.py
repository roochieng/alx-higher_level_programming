#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    try:
        r.raise_for_status()
        print(r.text)
    except Exception as e:
        print(f"Error code: {r.status_code}")
