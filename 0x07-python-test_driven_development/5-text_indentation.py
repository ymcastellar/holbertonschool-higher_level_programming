#!/usr/bin/python3
"""
    [prints a text with 2 new lines after each of these characters: ., ? and :]
"""


def text_indentation(text):
    if text:
        if type(text) is str:
            char = ['.', '?', ':']
            new_text = ""
            for words in text:
                new_text = new_text + words
                if words in char:
                    print(new_text.strip())
                    print("")
                    new_text = ""
            print(new_text.strip(), end="")
        else:
            raise TypeError('text must be a string')
