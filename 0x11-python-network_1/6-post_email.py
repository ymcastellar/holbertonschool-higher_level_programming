#!/usr/bin/python3
"""sends a POST request
"""

import request
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode('ascii')

    response = urllib.request.urlopen(sys.argv[1], data)
    print(response.text)
