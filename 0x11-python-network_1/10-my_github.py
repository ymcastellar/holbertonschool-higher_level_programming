#!/usr/bin/python3
"""takes your Github credentials adn display id"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    req = requests.get(url, auth=auth)
    try:
        print(req.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
