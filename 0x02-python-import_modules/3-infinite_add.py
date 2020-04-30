#!/usr/bin/python3
if __name__ == "__main__":
    import sys
arg = sys.argv[1:]
sum = 0
for i in arg:
    sum = sum + int(i)
print(sum)
