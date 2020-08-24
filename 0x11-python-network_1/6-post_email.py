#!/usr/bin/python3
"""sends a POST request
"""

import requests
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    response = request.post(sys.argv[1], data)
    print(response.text)
