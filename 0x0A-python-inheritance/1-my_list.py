#!/usr/bin/python3
"""[1. My list]
"""


class MyList(list):
    """[MyList that inherits from list]
    """

    def print_sorted(self):
        """[print sorted list]
        """
        print(sorted(self))
