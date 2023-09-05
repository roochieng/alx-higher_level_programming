#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
"""
import sys
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    message = requests.get(url)
    commits = message.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                 commits[i].get("sha"),
                 commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
