#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_list = list(my_string)
        for i in new_list:
            if i in "Cc":
                new_list.remove(i)
        new_list = "".join(new_list)
    return(new_list)
