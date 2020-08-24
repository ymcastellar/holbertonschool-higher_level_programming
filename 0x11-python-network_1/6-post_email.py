#!/usr/bin/python3
"""sends a POST request
"""

import requests
import sys

if __name__ == "__main__":
    obj = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data=obj)
    print(response.text)
