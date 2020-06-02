#!/usr/bin/python3
"""[4. Only sub class of]
"""


def inherits_from(obj, a_class):
    """[4. Only sub class of a class, otherwise False]
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
