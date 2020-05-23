#!/usr/bin/python3

"""
    function that
    print name
"""


def say_my_name(first_name, last_name=""):
    """say_my_name

    Arguments:
        first_name {[str]} -- [first name]

    Keyword Arguments:
        last_name {str} -- [last name]
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
