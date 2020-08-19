#!/usr/bin/python3
"""  function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """find a peak in a list"""

    if list_of_integers:

        length = len(list_of_integers)

        if length == 1:
            return list_of_integers[0]
        elif length == 2:
            return max(list_of_integers)

        mid = int(length / 2)

        if (list_of_integers[mid] > list_of_integers[mid - 1]
                and list_of_integers[mid] > list_of_integers[mid + 1]):
                    return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            return find_peak(list_of_integers[:mid])
        else:
            return find_peak(list_of_integers[mid + 1:])
    else:
        return None
