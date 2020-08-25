#!/usr/bin/python3
"""My Github!"""

import requests
import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (sys.argv[1], sys.argv[2])
    req = requests.get(url, auth=auth)
    try:
        print(req.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
