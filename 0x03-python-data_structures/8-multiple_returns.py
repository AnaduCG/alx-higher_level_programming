#!/usr/bin/python3
"""multiple_returns() - function that returns a tuple
                    with the length of a string and its
                    first character.
    sentence: word to be handled
"""


def multiple_returns(sentence):
    if sentence == '':
        fc = None
    else:
        fc = sentence[0]
    return (len(sentence), fc)
