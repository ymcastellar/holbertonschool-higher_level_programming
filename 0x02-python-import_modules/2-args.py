#!/usr/bin/python3
if __name__ == "__main__":
    import sys
arg = len(sys.argv) - 1
name = sys.argv
if arg == 0:
    print("{} arguments.".format(arg))
elif arg == 1:
    print("{} argument:".format(arg))
    for i in range(arg):
        i = i + 1
        print("{}: {}".format(i, name[i]))
else:
    print("{} arguments:".format(arg))
    for i in range(arg):
        i = i + 1
        print("{}: {}".format(i, name[i]))
