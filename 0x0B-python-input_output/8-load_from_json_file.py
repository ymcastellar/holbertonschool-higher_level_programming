#!/usr/bin/python3
"""[Create object from a JSON file]
"""
import json


def load_from_json_file(filename):
    """[load_from_json_file]

    Arguments:
        filename {[obj]} -- [name of the file]
    """
    with open(filename) as f:
        newf = json.load(f)
    f.close()
    return newf
