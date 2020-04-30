#!/usr/bin/python3
if name == "main":
    from hidden_4 import *

for i in dir():
    if i[:2] != "__":
        print(i)
