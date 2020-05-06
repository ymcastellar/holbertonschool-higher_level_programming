#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        leng = 0
        first = None
    else:
        leng = len(sentence)
        first = sentence[0]
    return (leng, first)
