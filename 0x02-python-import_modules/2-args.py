#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    if arg > 1:
        print("{} arguments".format(arg))
    else:
        print("{} argument".format(arg))
