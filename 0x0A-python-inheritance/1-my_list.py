#!/usr/bin/python3
"""[1. My list]
"""


class MyList(list):
    """[MyList that inherits from list]
    """

    def print_sorted(self):
        """[print sorted list]
        """
        new_list = []
        new_list = self.copy()
        new_list.sort()
        print(new_list)
